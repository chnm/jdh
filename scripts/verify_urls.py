#!/usr/bin/env python3
"""Verify the Hugo build against the wget archive.

1. URL COVERAGE: every page URL in the committed wget archive must resolve in
   public/ (as a real page or an alias redirect). Known-acceptable drops
   (per-section RSS feeds, deep /page/N/ pagination) are reported separately.
2. INTERNAL LINKS: no root-relative internal link in public/ may 404.

Run after `hugo`:  python scripts/verify_urls.py
"""
import os, re, sys, glob
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")

ARCHIVE_DIRS = ["1-1", "1-2", "1-3", "1-4", "2-1", "2-2", "2-3", "3-1", "3-2",
                "about", "author", "authors", "category", "featured",
                "submissions", "volumes"]
NESTED = "/journalofdigitalhumanities.org/"


def url_of(path, base):
    rel = os.path.relpath(path, base).replace(os.sep, "/")
    if rel.endswith("/index.html"):
        return "/" + rel[:-len("index.html")]
    if rel == "index.html":
        return "/"
    return "/" + rel


def archive_urls():
    urls = set()
    if os.path.exists(os.path.join(ROOT, "index.html")):
        urls.add("/")
    for d in ARCHIVE_DIRS:
        for f in glob.glob(f"{ROOT}/{d}/**/*.html", recursive=True):
            rp = f.replace(os.sep, "/")
            if NESTED in rp:
                continue
            urls.add(url_of(f, ROOT))
    return urls


def public_urls():
    urls = set()
    for f in glob.glob(f"{PUBLIC}/**/*.html", recursive=True):
        urls.add(url_of(f, PUBLIC))
    return urls


def coverage():
    arc, pub = archive_urls(), public_urls()
    missing = sorted(arc - pub)
    feeds = [u for u in missing if u.endswith("/feed/") or "/feed/" in u]
    pages = [u for u in missing if re.search(r"/page/\d+/?$", u)]
    other = [u for u in missing if u not in feeds and u not in pages]
    print("== URL COVERAGE ==")
    print(f"  archive page URLs : {len(arc)}")
    print(f"  public output URLs: {len(pub)}")
    print(f"  matched           : {len(arc & pub)}")
    print(f"  missing (feeds)   : {len(feeds)}  [expected drop]")
    print(f"  missing (page/N)  : {len(pages)}  [expected drop]")
    print(f"  missing (other)   : {len(other)}")
    for u in other:
        print("      MISSING:", u)
    return other


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for k in ("href", "src"):
            if d.get(k):
                self.links.append(d[k])


def resolves(path):
    """Does a root-relative internal path exist in public/?"""
    p = path.split("#")[0].split("?")[0]
    if not p:
        return True
    p = p.lstrip("/")
    cand = os.path.join(PUBLIC, p)
    if p.endswith("/") or p == "":
        return os.path.isfile(os.path.join(cand, "index.html"))
    if os.path.isfile(cand):
        return True
    # try as a directory (pretty URL without trailing slash)
    return os.path.isfile(os.path.join(cand, "index.html"))


def link_check():
    broken = {}
    checked = 0
    for f in glob.glob(f"{PUBLIC}/**/*.html", recursive=True):
        html = open(f, encoding="utf-8", errors="replace").read()
        p = LinkExtractor()
        try:
            p.feed(html)
        except Exception:
            continue
        for link in p.links:
            if not link.startswith("/"):
                continue                      # external / anchor / protocol-relative
            if link.startswith("//"):
                continue
            checked += 1
            if not resolves(link):
                broken.setdefault(link.split("#")[0], []).append(url_of(f, PUBLIC))
    print("\n== INTERNAL LINKS ==")
    print(f"  root-relative links checked: {checked}")
    print(f"  broken link targets        : {len(broken)}")
    for tgt, srcs in sorted(broken.items())[:40]:
        print(f"      BROKEN {tgt}  <- {len(srcs)} page(s), e.g. {srcs[0]}")
    return broken


if __name__ == "__main__":
    other = coverage()
    broken = link_check()
    print("\n== RESULT ==")
    ok = (not other) and (not broken)
    print("  PASS" if ok else "  see findings above")
    sys.exit(0 if ok else 1)
