#!/usr/bin/env python3
"""Classify every WordPress (wget-archive) URL against the Hugo build.

For each old URL, report whether the Hugo site serves it as a DIRECT page
(identical URL), an ALIAS (redirect stub -> a different canonical URL), or
MISSING. Also emits a ready-to-paste Caddy 301 block for the URLs that changed.

Run after `hugo`:  python scripts/url_analysis.py [--caddy]
"""
import os, re, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "public")
ARCHIVE_DIRS = ["1-1", "1-2", "1-3", "1-4", "2-1", "2-2", "2-3", "3-1", "3-2",
                "about", "author", "authors", "category", "featured",
                "submissions", "volumes"]
NESTED = "/journalofdigitalhumanities.org/"
# pagination URLs intentionally not reproduced (content is on the parent page)
EXTRA_REDIRECTS = [("/author/editor/page/2/", "/author/editor/"),
                   ("/author/editor/page/3/", "/author/editor/")]

REFRESH = re.compile(r'http-equiv=["\']?refresh', re.I)
URLRE = re.compile(r'url=([^"\'>\s]+)', re.I)


def url_of(p, base):
    r = os.path.relpath(p, base).replace(os.sep, "/")
    if r.endswith("/index.html"):
        return "/" + r[:-len("index.html")]
    if r == "index.html":
        return "/"
    return "/" + r


def archive_urls():
    u = {"/"} if os.path.exists(f"{ROOT}/index.html") else set()
    for d in ARCHIVE_DIRS:
        for f in glob.glob(f"{ROOT}/{d}/**/*.html", recursive=True):
            if NESTED in f.replace(os.sep, "/"):
                continue
            u.add(url_of(f, ROOT))
    return u


def classify(u):
    rel = u.strip("/")
    f = os.path.join(PUB, rel, "index.html") if (u == "/" or u.endswith("/")) else os.path.join(PUB, rel)
    if not os.path.isfile(f):
        return ("MISSING", None)
    h = open(f, encoding="utf-8", errors="replace").read()
    if REFRESH.search(h) and len(h) < 2000:
        m = URLRE.search(h)
        t = re.sub(r"^https?://[^/]+", "", m.group(1)) if m else "?"
        return ("ALIAS", t)
    return ("DIRECT", None)


def main():
    arc = sorted(archive_urls())
    buckets = {"DIRECT": [], "ALIAS": [], "MISSING": []}
    for u in arc:
        k, t = classify(u)
        buckets[k].append((u, t))

    if "--caddy" in sys.argv:
        red = sorted((u, t) for u, t in buckets["ALIAS"]) + EXTRA_REDIRECTS
        print("# JDH legacy-URL redirects (paste inside the Caddy site block)")
        for o, n in red:
            print(f"redir {o} {n} permanent")
        return

    print(f"Existing WordPress URLs: {len(arc)}")
    print(f"  DIRECT  (identical URL) : {len(buckets['DIRECT'])}")
    print(f"  ALIAS   (URL changed)   : {len(buckets['ALIAS'])}")
    print(f"  MISSING                 : {len(buckets['MISSING'])}")
    print("\nALIASES (old -> new):")
    for u, t in buckets["ALIAS"]:
        print(f"  {u}\n      -> {t}")
    print("\nMISSING:")
    for u, _ in buckets["MISSING"]:
        print(f"  {u}")


if __name__ == "__main__":
    main()
