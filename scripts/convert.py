#!/usr/bin/env python3
"""Convert the JDH wget archive into Hugo content bundles.

Source of truth: the committed wget archive at the repo root (1-1/ ... 3-2/,
author/, category/, etc.). This script extracts each primary issue-article page
(`<div id="article">`), converts the body to Markdown, and writes a Hugo page
bundle at the article's CANONICAL path. Duplicate URLs become `aliases`.

Idempotent: writes into a fresh content/<issue> tree each run. Media (uploads,
files) stays referenced by absolute external URL; only internal page links are
rewritten.

Usage:
    python scripts/convert.py [issue ...]      # default: all issues
"""
import os, re, sys, glob, html, shutil
from urllib.parse import urljoin, urlsplit, quote
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

ROOT = os.environ.get("JDH_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT = os.path.join(ROOT, "content")
DATA = os.path.join(ROOT, "data")
SITE = "https://journalofdigitalhumanities.org"

ISSUES = {
    "1-1": dict(volume=1, number=1, season="Winter", year=2011),
    "1-2": dict(volume=1, number=2, season="Spring", year=2012),
    "1-3": dict(volume=1, number=3, season="Summer", year=2012),
    "1-4": dict(volume=1, number=4, season="Fall",   year=2012),
    "2-1": dict(volume=2, number=1, season="Winter", year=2012),
    "2-2": dict(volume=2, number=2, season="Spring", year=2013),
    "2-3": dict(volume=2, number=3, season="Summer", year=2013),
    "3-1": dict(volume=3, number=1, season="Spring", year=2014),
    "3-2": dict(volume=3, number=2, season="Summer", year=2014),
}
SEASON_MONTH = {"Winter": 12, "Spring": 3, "Summer": 6, "Fall": 9}

BLOCK = {"p", "div", "section", "article", "blockquote", "ul", "ol", "li",
         "h1", "h2", "h3", "h4", "h5", "h6", "pre", "hr", "table", "figure",
         "header", "footer", "dl", "dd", "dt"}
RAW_KEEP = {"audio", "video", "iframe", "table", "object", "embed"}

# Accumulators (filled while converting)
AUTHORS = {}          # id -> {"name":..., "gravatar":..., "bio":...}
URL_MAP = {}          # duplicate url -> canonical url (built in prescan)


# --------------------------------------------------------------------------- #
# URL helpers
# --------------------------------------------------------------------------- #
def url_of(path):
    """Filesystem path under ROOT -> site-absolute URL path."""
    rel = os.path.relpath(os.path.realpath(path), ROOT)
    rel = rel.replace(os.sep, "/")
    if rel.endswith("/index.html"):
        return "/" + rel[:-len("index.html")]
    if rel == "index.html":
        return "/"
    return "/" + rel


def norm_site_path(u):
    """Normalise a site path: strip trailing index.html, ensure leading slash."""
    if u.endswith("index.html"):
        u = u[:-len("index.html")]
    if not u.startswith("/"):
        u = "/" + u
    return u


def resolve_canonical(path, href):
    if not href:
        return None
    u = urljoin(url_of(path), href)
    sp = urlsplit(u)
    p = sp.path
    if p.endswith("index.html"):
        p = p[:-len("index.html")]
    return p


DOMAINISH = re.compile(r"^[a-z0-9][a-z0-9-]*(\.[a-z0-9-]+)+$", re.I)
SKIP_EXT = (".html", ".htm", ".php", ".png", ".jpg", ".jpeg", ".gif", ".svg",
            ".pdf", ".css", ".js", ".xml", ".mp3", ".m4v", ".mov", ".ogg")


def rewrite_link(href, page_path):
    """Rewrite an href found on the page at page_path."""
    if href is None:
        return None
    href = href.strip()
    if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("data:"):
        return href
    sp = urlsplit(href)
    if sp.scheme in ("http", "https"):
        host = sp.netloc.lower().split(":")[0]
        if host.endswith("journalofdigitalhumanities.org"):
            path = sp.path or "/"
            if "/wp-content/" in path or "/wp-includes/" in path or path.startswith("/files"):
                rest = path
                if sp.query:
                    rest += "?" + sp.query
                return SITE + rest                       # media: external, https
            return map_internal(path, sp.fragment)       # internal page
        return href                                       # external, keep
    if sp.scheme:
        return href
    # schema-less. Distinguish internal-relative from bare-domain external.
    first = href.split("/")[0].split("#")[0].split("?")[0]
    if (first and DOMAINISH.match(first) and not first.lower().endswith(SKIP_EXT)
            and not href.startswith((".", "/"))):
        if first.lower().endswith("journalofdigitalhumanities.org"):
            sp3 = urlsplit("https://" + href)             # schema-less SELF link -> internal
            p = sp3.path or "/"
            if "/wp-content/" in p or "/wp-includes/" in p or p.startswith("/files"):
                return SITE + p + (("?" + sp3.query) if sp3.query else "")
            return map_internal(p, sp3.fragment)
        return "https://" + href                          # bare-domain external (crawl 404 fix)
    # internal relative link -> resolve against the page, then map
    target = urljoin(url_of(page_path), href)
    sp2 = urlsplit(target)
    if "/wp-content/" in sp2.path or "/wp-includes/" in sp2.path or sp2.path.startswith("/files"):
        rest = sp2.path + (("?" + sp2.query) if sp2.query else "")
        return SITE + rest
    return map_internal(sp2.path, sp2.fragment)


NESTED = "/journalofdigitalhumanities.org/"


def map_internal(path, fragment=""):
    path = norm_site_path(path)
    if NESTED in path:                                     # collapse nested-archive artifact
        path = "/" + path.split(NESTED, 1)[1]
        path = norm_site_path(path)
    path = URL_MAP.get(path, path)                         # duplicate -> canonical
    if fragment:
        path += "#" + fragment
    return path


# --------------------------------------------------------------------------- #
# Markdown serialisation
# --------------------------------------------------------------------------- #
def md_escape(text):
    return re.sub(r"([\\`])", r"\\\1", text)


def collapse_ws(text):
    return re.sub(r"[ \t\r\n]+", " ", text)


class Converter:
    def __init__(self, page_path):
        self.page_path = page_path
        self.footnotes = {}     # "1" -> markdown definition text

    # -- inline -------------------------------------------------------------
    def inline(self, node):
        out = []
        for c in node.children:
            out.append(self.inline_node(c))
        return "".join(out)

    def inline_node(self, c):
        if isinstance(c, Comment):
            return ""
        if isinstance(c, NavigableString):
            return md_escape(collapse_ws(str(c)))
        name = c.name
        if name in ("script", "style"):
            return ""
        if name == "br":
            return "  \n"
        if name == "sup" and c.select_one("a.footnoted"):
            a = c.select_one("a.footnoted")
            return "[^%s]" % a.get_text(strip=True)
        if name in ("em", "i", "cite"):
            inner = self.inline(c).strip()
            return "_%s_" % inner if inner else ""
        if name in ("strong", "b"):
            inner = self.inline(c).strip()
            return "**%s**" % inner if inner else ""
        if name == "code":
            return "`%s`" % c.get_text()
        if name == "a":
            text = self.inline(c).strip()
            href = rewrite_link(c.get("href"), self.page_path)
            if not href:
                return text
            if not text:
                return ""
            title = c.get("title")
            if title:
                title = title.replace('"', "'")
                return '[%s](%s "%s")' % (text, href, title)
            return "[%s](%s)" % (text, href)
        if name == "img":
            return self.img_inline(c)
        if name in ("sup", "sub", "abbr", "span", "u", "small", "mark", "q",
                    "time", "label", "del", "ins", "s", "strike", "font", "var",
                    "kbd", "samp", "wbr", "bdi", "ruby"):
            # spans/sup/sub etc: pass through inner; keep del/ins as raw for fidelity
            if name in ("del", "s", "strike", "ins"):
                inner = self.inline(c)
                return "<%s>%s</%s>" % (name, inner, name) if inner.strip() else ""
            return self.inline(c)
        # unknown inline -> just its text
        return self.inline(c)

    def img_inline(self, img):
        src = rewrite_link(img.get("src"), self.page_path) or ""
        alt = (img.get("alt") or "").replace("\n", " ").strip()
        return "![%s](%s)" % (alt, src)

    # -- blocks -------------------------------------------------------------
    def blocks(self, node):
        out = []
        for child in node.children:
            b = self.block_node(child)
            if b is not None and b.strip() != "":
                out.append(b)
        return out

    def block_node(self, c):
        if isinstance(c, Comment):
            return None
        if isinstance(c, NavigableString):
            t = collapse_ws(str(c)).strip()
            return md_escape(t) if t else None
        name = c.name
        if name in ("script", "style", "form", "noscript"):
            return None
        classes = set(c.get("class") or [])

        # author-bio is extracted separately; skip if present
        if "author-bio" in classes:
            return None
        # footnote list
        if name == "ol" and "footnotes" in classes:
            self.collect_footnotes(c)
            return None
        # GeSHi code block (outermost wrapper)
        if any(cl.startswith("wp-geshi-highlight-wrap") for cl in classes) and not self._inside_geshi(c):
            return self.code_block(c)
        # captioned figure
        if "wp-caption" in classes or (name == "figure"):
            return self.figure(c)
        # audio / video players
        if "audio_wrap" in classes or "video_wrap" in classes:
            return self.media(c)
        # pulled quote
        if name == "p" and "pulled-quote" in classes:
            return self.pulled_quote(c)
        # raw-keep elements
        if name in RAW_KEEP:
            return self.raw_keep(c)
        if name == "pre":
            return self.code_block(c)
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(name[1])
            txt = self.inline(c).strip()
            return ("#" * level + " " + txt) if txt else None
        if name == "hr":
            return "---"
        if name == "blockquote":
            inner = "\n\n".join(self.blocks(c)) or self.inline(c).strip()
            return "\n".join("> " + ln for ln in inner.splitlines()) if inner.strip() else None
        if name in ("ul", "ol"):
            return self.list_block(c, ordered=(name == "ol"))
        if name in ("div", "section", "article", "header", "footer", "dl", "dd"):
            # unwrap: render children as blocks
            return "\n\n".join(self.blocks(c)) or None
        if name == "p":
            txt = self.inline(c).strip()
            return txt or None
        # fallback: treat as paragraph of inline content, else recurse blocks
        txt = self.inline(c).strip()
        if txt:
            return txt
        return "\n\n".join(self.blocks(c)) or None

    def _inside_geshi(self, c):
        p = c.parent
        while p is not None and isinstance(p, Tag):
            if any(cl.startswith("wp-geshi-highlight-wrap") for cl in (p.get("class") or [])):
                return True
            p = p.parent
        return False

    def list_block(self, node, ordered, depth=0):
        lines = []
        i = 1
        for li in node.find_all("li", recursive=False):
            marker = ("%d." % i) if ordered else "-"
            # split li into leading inline content + nested lists
            sub_lists = li.find_all(["ul", "ol"], recursive=False)
            # render li inline/blocks excluding nested lists
            tmp = []
            for child in li.children:
                if isinstance(child, Tag) and child.name in ("ul", "ol"):
                    continue
                if isinstance(child, Tag) and child.name in BLOCK and child.name not in ("span",):
                    tmp.append(self.block_node(child) or "")
                else:
                    tmp.append(self.inline_node(child) if not isinstance(child, NavigableString)
                               else md_escape(collapse_ws(str(child))))
            content = collapse_ws(" ".join(t for t in tmp if t)).strip()
            indent = "    " * depth
            lines.append("%s%s %s" % (indent, marker, content))
            for sl in sub_lists:
                lines.append(self.list_block(sl, ordered=(sl.name == "ol"), depth=depth + 1))
            i += 1
        return "\n".join(lines)

    def code_block(self, node):
        # find innermost <pre>
        pre = node if node.name == "pre" else node.select_one("pre")
        if pre is None:
            return None
        lang = ""
        pre_classes = set(pre.get("class") or [])
        in_geshi = ("de1" in pre_classes) or self._inside_geshi(pre)
        if in_geshi:
            # language sits on the div directly wrapping the <pre> (e.g. <div class="python">)
            parent = pre.parent
            if isinstance(parent, Tag):
                for cl in (parent.get("class") or []):
                    if cl not in ("de1", "wp-geshi-highlight"):
                        lang = cl
                        break
        code = pre.get_text()
        code = code.replace("\r\n", "\n").rstrip("\n")
        fence = "```"
        while fence in code:
            fence += "`"
        return "%s%s\n%s\n%s" % (fence, lang, code, fence)

    def figure(self, node):
        # rewrite img src / a href to absolute external; drop srcset/sizes/loading
        node = BeautifulSoup(str(node), "html.parser").find(True)
        for img in node.find_all("img"):
            img["src"] = rewrite_link(img.get("src"), self.page_path) or ""
            for attr in ("srcset", "sizes", "loading", "data-src"):
                if img.has_attr(attr):
                    del img[attr]
        for a in node.find_all("a"):
            if a.get("href"):
                a["href"] = rewrite_link(a.get("href"), self.page_path)
        return str(node)

    def media(self, node):
        el = node.find(["audio", "video"])
        if el is None:
            return None
        el = BeautifulSoup(str(el), "html.parser").find(["audio", "video"])
        for junk in el.find_all(["script", "a", "object", "param", "embed"]):
            junk.decompose()
        for src in el.find_all("source"):
            if src.get("src"):
                src["src"] = rewrite_link(src.get("src"), self.page_path)
        # normalise attributes
        for attr in ("autobuffer", "autoplay", "id", "class"):
            if el.has_attr(attr):
                del el[attr]
        el["controls"] = None
        el["preload"] = "metadata"
        return str(el)

    def pulled_quote(self, node):
        nxt = node.find_next_sibling()
        author = ""
        if nxt and isinstance(nxt, Tag) and "quote-author" in (nxt.get("class") or []):
            author = nxt.get_text(strip=True)
        inner = self.inline(node).strip()
        out = '<p class="pulled-quote">%s</p>' % inner
        if author:
            out += '<span class="quote-author">%s</span>' % html.escape(author)
        return out

    def raw_keep(self, node):
        node = BeautifulSoup(str(node), "html.parser").find(True)
        for a in node.find_all(["a", "source", "img"]):
            for attr in ("href", "src"):
                if a.get(attr):
                    a[attr] = rewrite_link(a.get(attr), self.page_path)
        for junk in node.find_all(["script"]):
            junk.decompose()
        return str(node)

    # -- footnotes ----------------------------------------------------------
    def collect_footnotes(self, ol):
        for li in ol.find_all("li", recursive=False):
            num = None
            strong = li.find("strong")
            if strong:
                m = re.search(r"\d+", strong.get_text())
                if m:
                    num = m.group()
                strong.decompose()
            if num is None and li.get("id"):
                m = re.search(r"-n-(\d+)$", li["id"])
                num = m.group(1) if m else None
            for ret in li.select("a.note-return"):
                ret.decompose()
            text = collapse_ws(self.inline(li)).strip()
            if num:
                self.footnotes[num] = text

    # -- top-level ----------------------------------------------------------
    def convert(self, body):
        parts = self.blocks(body)
        md = "\n\n".join(p for p in parts if p and p.strip())
        if self.footnotes:
            defs = []
            for num in sorted(self.footnotes, key=lambda x: int(x)):
                defs.append("[^%s]: %s" % (num, self.footnotes[num]))
            md += "\n\n" + "\n\n".join(defs)
        md = re.sub(r"\n{3,}", "\n\n", md)
        return md.strip() + "\n"


# --------------------------------------------------------------------------- #
# Page parsing
# --------------------------------------------------------------------------- #
def soup_of(path):
    return BeautifulSoup(open(path, encoding="utf-8", errors="replace").read(), "lxml")


def parse_authors(article):
    authors = []
    for h4 in article.select("h4.author-name"):
        for a in h4.select('a[rel="author"]'):
            href = a.get("href", "")
            aid = ""
            if "/author/" in href:
                aid = href.split("/author/")[1].split("/")[0]
            authors.append({"name": a.get_text(strip=True), "id": aid})
    return authors


def extract_author_bios(article, authors):
    """Pull .author-bio blocks out of the tree; record bios into AUTHORS."""
    names_to_id = {a["name"]: a["id"] for a in authors if a["id"]}
    for bio in article.select(".author-bio"):
        h2 = bio.find(["h2", "h3"])
        name = ""
        if h2:
            name = re.sub(r"^\s*About\s+", "", h2.get_text(strip=True))
        grav = bio.find("img")
        gravatar = ""
        if grav and grav.get("src"):
            gravatar = re.sub(r"^http:", "https:", grav.get("src"))
        paras = bio.select("p.coauthor") or [p for p in bio.find_all("p")]
        bio_html = "".join(str(p) for p in paras)
        aid = names_to_id.get(name)
        if aid and aid not in AUTHORS:
            AUTHORS[aid] = {"name": name, "gravatar": gravatar, "bio": bio_html}
        bio.decompose()


def is_article_page(soup):
    art = soup.select_one("#article")
    return bool(art and art.find("h1"))


def page_canonical(f, soup):
    """(own_url, canonical_url) with broken nested-artifact canonicals ignored."""
    can = soup.find("link", rel="canonical")
    canurl = resolve_canonical(f, can.get("href") if can else None)
    myurl = url_of(f)
    if canurl and NESTED in canurl:
        canurl = myurl
    return myurl, canurl


def clean_html_fragment(node, page_path):
    """Rewrite links inside a kept HTML subtree (front pages, etc.)."""
    node = BeautifulSoup(str(node), "html.parser").find(True)
    for s in node.find_all(["script", "style", "form"]):
        s.decompose()
    for a in node.find_all("a"):
        if a.get("href"):
            a["href"] = rewrite_link(a["href"], page_path)
    for img in node.find_all("img"):
        if img.get("src"):
            img["src"] = rewrite_link(img["src"], page_path)
        for at in ("srcset", "sizes", "loading", "data-src"):
            if img.has_attr(at):
                del img[at]
    for src in node.find_all("source"):
        if src.get("src"):
            src["src"] = rewrite_link(src["src"], page_path)
    return str(node)


# --------------------------------------------------------------------------- #
# TOC (section + ordering) from the per-issue sidebar
# --------------------------------------------------------------------------- #
def parse_toc(issue, sample_page):
    """Return {url: (section_name, section_url, section_weight, weight)}."""
    soup = soup_of(sample_page)
    toc = soup.select_one("ul#menu-table-of-contents")
    result = {}
    if not toc:
        return result
    sw = 0
    for parent in toc.find_all("li", recursive=False):
        a = parent.find("a", recursive=False)
        sub = parent.find("ul", recursive=False)
        if not sub:
            continue
        sw += 1
        section = a.get_text(strip=True) if a else ""
        section_url = ""
        if a and a.get("href"):
            section_url = norm_site_path(urlsplit(urljoin(url_of(sample_page), a["href"])).path)
        w = 0
        for li in sub.find_all("li", recursive=False):
            la = li.find("a")
            if not la:
                continue
            w += 1
            target = urljoin(url_of(sample_page), la.get("href", ""))
            tpath = norm_site_path(urlsplit(target).path)
            result[tpath] = (section, section_url, sw, w)
    return result


# --------------------------------------------------------------------------- #
# TOML front matter
# --------------------------------------------------------------------------- #
def tstr(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def front_matter(meta):
    L = ["+++"]
    L.append("title = " + tstr(meta["title"]))
    L.append("slug = " + tstr(meta["slug"]))
    L.append('type = "article"')
    if meta.get("url"):
        L.append("url = " + tstr(meta["url"]))
    L.append("date = " + meta["date"])
    L.append('issue = ' + tstr(meta["issue"]))
    L.append("volume = %d" % meta["volume"])
    L.append("number = %d" % meta["number"])
    L.append("season = " + tstr(meta["season"]))
    L.append("year = %d" % meta["year"])
    if meta.get("section"):
        L.append("section = " + tstr(meta["section"]))
        L.append("section_url = " + tstr(meta["section_url"]))
        L.append("section_weight = %d" % meta["section_weight"])
        L.append("weight = %d" % meta["weight"])
    if meta["authors"]:
        ids = [a["id"] for a in meta["authors"] if a["id"]]
        names = [a["name"] for a in meta["authors"]]
        L.append("authors = [" + ", ".join(tstr(n) for n in names) + "]")
        L.append("author_ids = [" + ", ".join(tstr(i) for i in ids) + "]")
        L.append("author = [" + ", ".join(tstr(i) for i in ids) + "]")  # taxonomy
    if meta.get("aliases"):
        L.append("aliases = [" + ", ".join(tstr(a) for a in sorted(meta["aliases"])) + "]")
    L.append("+++")
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def discover(issue):
    pages = []
    for f in glob.glob(f"{ROOT}/{issue}/**/index.html", recursive=True) + glob.glob(f"{ROOT}/{issue}/*.html"):
        rp = os.path.realpath(f)
        if "/journalofdigitalhumanities.org/" in rp.replace(os.sep, "/"):
            continue
        if rp not in [p[0] for p in pages]:
            pages.append((rp, f))
    return [p[1] for p in pages]


def prescan(issues):
    """Build URL_MAP (duplicate -> canonical) across the given issues."""
    for issue in issues:
        for f in discover(issue):
            soup = soup_of(f)
            if not is_article_page(soup):
                continue
            myurl, canurl = page_canonical(f, soup)
            if canurl and canurl != myurl:
                URL_MAP[myurl] = canurl
            elif os.path.basename(f) != "index.html":      # stray flat *.html primary
                URL_MAP[myurl] = pretty_url(myurl)


def content_path_for(url):
    """Canonical site URL -> content bundle file path."""
    rel = url.strip("/")
    return os.path.join(CONTENT, rel, "index.md")


def pretty_url(url):
    """Ugly /foo.html -> pretty /foo/ (for stray flat *.html primaries)."""
    if url.endswith(".html"):
        return url[:-5] + "/"
    return url


def emit_issue_index(issue):
    """Issue landing page (<issue>/index.html) -> content/<issue>/_index.md."""
    path = os.path.join(ROOT, issue, "index.html")
    if not os.path.exists(path):
        return False
    soup = soup_of(path)
    fp = soup.select_one(".front-page")
    if not fp:
        return False
    info = ISSUES[issue]
    title = "Vol. %d, No. %d, %s %d" % (info["volume"], info["number"], info["season"], info["year"])
    fm = ["+++", "title = " + tstr(title), 'type = "issue"',
          "date = %04d-%02d-01" % (info["year"], SEASON_MONTH[info["season"]]),
          "issue = " + tstr(issue), "volume = %d" % info["volume"],
          "number = %d" % info["number"], "season = " + tstr(info["season"]),
          "year = %d" % info["year"], "+++"]
    body = clean_html_fragment(fp, path)
    out = os.path.join(CONTENT, issue, "_index.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(fm) + "\n\n" + body + "\n")
    return True


def emit_home():
    path = os.path.join(ROOT, "index.html")
    soup = soup_of(path)
    fp = soup.select_one(".front-page")
    if not fp:
        return
    fm = ["+++", "title = " + tstr("Journal of Digital Humanities"), "+++"]
    body = clean_html_fragment(fp, path)
    out = os.path.join(CONTENT, "_index.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(fm) + "\n\n" + body + "\n")
    print("  content/_index.md (homepage / Vol 3 No 2 landing)")


def convert_issue(issue):
    shutil.rmtree(os.path.join(CONTENT, issue), ignore_errors=True)
    files = discover(issue)
    # choose a sample article page to read the TOC from
    sample = None
    for f in files:
        if is_article_page(soup_of(f)):
            sample = f
            break
    toc = parse_toc(issue, sample) if sample else {}

    primaries = {}     # canonical_url -> file
    aliases = {}       # canonical_url -> [dup urls]
    for f in files:
        soup = soup_of(f)
        if not is_article_page(soup):
            continue
        myurl, canurl = page_canonical(f, soup)
        if canurl and canurl != myurl:
            aliases.setdefault(canurl, []).append(myurl)
        else:
            primaries[myurl] = f

    info = ISSUES[issue]
    date = "%04d-%02d-01" % (info["year"], SEASON_MONTH[info["season"]])
    n = 0
    for url, f in sorted(primaries.items()):
        soup = soup_of(f)
        article = soup.select_one("#article")
        h1 = article.find("h1")
        title = h1.get_text(strip=True)
        h1.extract()
        authors = parse_authors(article)
        for h4 in article.select("h4.author-name"):
            h4.extract()
        extract_author_bios(article, authors)
        is_flat = os.path.basename(f) != "index.html"     # stray flat *.html primary
        out_url = pretty_url(url) if is_flat else url      # serve flat copies at a pretty URL
        page_aliases = list(aliases.get(url, []))
        if is_flat:
            page_aliases.append(url)                       # keep original /<name>.html (redirect)
        section, section_url, sw, w = toc.get(norm_site_path(out_url),
                                              toc.get(norm_site_path(url), ("", "", 0, 0)))
        meta = dict(title=title, slug=out_url.strip("/").split("/")[-1],
                    date=date, issue=issue, volume=info["volume"], number=info["number"],
                    season=info["season"], year=info["year"],
                    section=section, section_url=section_url, section_weight=sw, weight=w,
                    authors=authors, aliases=page_aliases)
        out = content_path_for(out_url)
        body_md = Converter(f).convert(article)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(front_matter(meta) + "\n\n" + body_md)
        n += 1
    has_index = emit_issue_index(issue)
    print(f"  {issue}: {n} articles, {sum(len(v) for v in aliases.values())} aliases"
          f"{'' if has_index else '  (no landing page)'}")
    return n


def write_authors_data():
    os.makedirs(DATA, exist_ok=True)
    out = os.path.join(DATA, "authors.toml")
    lines = []
    for aid in sorted(AUTHORS):
        a = AUTHORS[aid]
        lines.append("[%s]" % tstr(aid))
        lines.append("name = " + tstr(a["name"]))
        lines.append("gravatar = " + tstr(a["gravatar"]))
        lines.append("bio = '''" + a["bio"].replace("'''", "''") + "'''")
        lines.append("")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"  data/authors.toml: {len(AUTHORS)} authors")


def main():
    issues = sys.argv[1:] or list(ISSUES)
    print("Prescanning for canonical/duplicate map ...")
    prescan(list(ISSUES))     # global map so cross-issue links resolve
    print(f"  URL_MAP: {len(URL_MAP)} duplicate->canonical entries")
    total = 0
    for issue in issues:
        total += convert_issue(issue)
    if set(issues) >= {"3-2"}:
        emit_home()
    write_authors_data()
    print(f"Done: {total} article bundles.")


if __name__ == "__main__":
    main()
