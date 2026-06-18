# jdh

[journalofdigitalhumanities.org](https://journalofdigitalhumanities.org) as a
**Hugo static site**, converted from a `wget` archive of the original
WordPress 5 (PressForward) site (on hiatus since Summer 2014).

## Layout

| Path | What it is |
|------|------------|
| `1-1/ … 3-2/`, `about/`, `author/`, `category/`, `featured/`, `volumes/`, … | The committed **wget archive** — the conversion *input* / source of truth. |
| `content/` | Generated Hugo content (article bundles, issue landings, archives, homepage). |
| `layouts/`, `static/`, `data/`, `hugo.toml` | Hugo site (ported `jdh` theme + templates). |
| `scripts/convert.py` | HTML→Markdown converter that builds `content/` from the archive. |
| `scripts/verify_urls.py` | Checks URL coverage vs the archive and internal links. |

URLs are preserved exactly (e.g. `/1-1/articles/<slug>/`); duplicate and stray
permalinks are emitted as alias redirects. Media (`wp-content/uploads`, `/files`)
is referenced by absolute URL, not bundled.

## Build

```sh
python -m venv .venv && ./.venv/bin/pip install beautifulsoup4 lxml
./.venv/bin/python scripts/convert.py      # regenerate content/ from the archive
hugo --gc --minify                         # build to public/
./.venv/bin/python scripts/verify_urls.py  # verify (run after hugo)
```

The converter is idempotent: it rebuilds `content/<issue>/`, `content/category/`,
`content/featured/`, the top-level pages, the homepage, and `data/authors.toml`
on each run.

## Verification

Latest run: **446/448** archive URLs resolve (the 2 gaps are deep
`/author/editor/page/N/` pagination — all those posts are listed on
`/author/editor/`), **0 broken internal links** across ~9,400 links.

## Search

Full-text search is served by [Pagefind](https://pagefind.app). The header
search box submits to `/search/`, which mounts the Pagefind UI over an index
built from `public/` after the Hugo build. `package.json` / `package-lock.json`
pin the toolchain.

## Deploy (Docker)

The `Dockerfile` is a two-stage build: stage 1 (stagex Node + Hugo-extended)
runs `hugo` then `pagefind --site public`; stage 2 serves the static `public/`
with Caddy on port 80.

```sh
docker build -t jdh-site .
docker run -d --name jdh -p 8090:80 jdh-site   # browse http://<host>:8090/
```

To build/deploy on a remote Docker host over SSH:

```sh
docker --context <ctx> build -t jdh-site .
docker --context <ctx> run -d --name jdh -p 8090:80 jdh-site
```
