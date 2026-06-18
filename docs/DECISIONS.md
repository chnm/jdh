# Conversion decisions

Why the WordPress→Hugo conversion was done the way it was. Records the strategic
choices (and the alternatives rejected) that the commit messages only imply.
See `scripts/convert.py` for the implementation and `README.md` for build/run.

## 1. Source of truth: the wget archive, not the database
The committed wget HTML (`1-1/ … 3-2/`, `author/`, `category/`, …) is the
conversion input. The 105 MB `db_journalofdh.sql` (PressForward/Edit-Flow/
Anthologize tables, ~7,600 rows incl. 5,000+ revisions) and the live LAMP tree
under `lamp/` are **reference only**.

- **Why:** the static HTML is exactly what was published — shortcodes already
  rendered (footnotes, GeSHi code, captions), URLs already baked in. A DB
  migration would mean importing MySQL, resolving the nested-category permalink
  logic, and de-crufting PressForward/Anthologize internals for the same output.
- **Cost:** per-article publish dates aren't reliably in the HTML (see #8).

## 2. Content format: Markdown *(user choice)*
Article bodies are converted to Markdown (footnotes → Goldmark `[^n]`, code →
fenced blocks). Rejected: (a) preserve rendered HTML verbatim, (b) hybrid.
Complex/irreducible blocks (captioned figures, audio/video, iframes, pulled
quotes) are emitted as **cleaned raw HTML**, not shortcodes — a deliberate
deviation from the plan's `{{< figure >}}` approach, chosen because raw HTML
preserves rich captions and exact CSS classes with less fragility. Goldmark runs
with `unsafe = true` to allow it.

## 3. Site design: port the original `jdh` theme *(user choice)*
The theme CSS (`style.css`, `skeleton.css`, `layout.css`), images, and IcoMoon
fonts are copied verbatim into `static/wp-content/themes/jdh/`; the header / nav /
footer / per-issue TOC sidebar are rebuilt as Hugo layouts so the site looks
identical. Rejected: an off-the-shelf Hugo theme.

## 4. Media: reference externally *(user choice)*
`wp-content/uploads` (~1 GB) and `files/` (~3.6 GB of ebooks/audio/video) are
**not** bundled; image and download links stay absolute to
`https://journalofdigitalhumanities.org/…`. Only internal *page* links are
rewritten. Rejected: bundling images / Git-LFS for the binaries.
- **Implication:** the deployed site depends on that origin still serving
  `/wp-content/uploads` and `/files` for images and downloads to resolve.

## 5. Exact URL preservation
Each primary page is emitted as a bundle at its **canonical** path, so Hugo's
default output (`uglyURLs = false`) reproduces the original pretty URLs
(`/1-1/articles/<slug>/`) byte-for-byte. No permalink config is needed for issue
content; only the `author` taxonomy uses `/author/:slug/` (singular) to match WP.

## 6. Deduplication via `rel="canonical"`
WordPress served many posts under several category-path permalinks. The page's
`<link rel="canonical">` picks the primary; the other URLs become Hugo `aliases`
(redirect stubs). The wget redirect log (`.crawl/wget.log`, ~369 redirects) was
**not** used for this — inspection showed it was mostly asset `?ver=` 301s, not
page-level redirects.

## 7. The 1-3 nested-archive artifact
`1-3/the-difference-the-digital-makes/journalofdigitalhumanities.org/…` is a wget
recursion artifact, and the real `mapping-texts` page's canonical points *into*
it. Decision: discard the nested subtree, treat the top-level pages as primaries
(ignoring their broken canonicals), and collapse any link containing
`/journalofdigitalhumanities.org/` back to the real path. This recovered the
`mapping-texts` article that was otherwise dropped. (`39f4fad`)

## 8. Dates from issue season/year
No reliable per-article dates exist in the HTML, so `date` is derived from the
issue (Winter→Dec, Spring→Mar, Summer→Jun, Fall→Sep of the issue year), which
keeps issues monotonically ordered; intra-issue order is controlled by `weight`
(from the TOC), not by date.

## 9. Section + ordering from the TOC sidebar
A page's section and position come from the per-issue `#menu-table-of-contents`,
**not** its URL path — because WordPress canonicalised some articles to a flat
`/1-1/<slug>/` and others to a sectioned `/1-1/<section>/<slug>/`, inconsistently.
The TOC link targets always match the canonical, so they're authoritative.

## 10. Stray flat `*.html` permalinks
WordPress "ugly" `*.html` captures: duplicates become aliases of their directory
page; sole copies are served at a pretty URL with the original `/<name>.html`
kept as an alias redirect (avoids Hugo file-vs-directory collisions). (`39f4fad`)

## 11. Authors → taxonomy; category archives → content pages
- Co-authors become an `author` taxonomy; `/author/<id>/` term pages render name/
  gravatar/bio from `data/authors.toml`. Author archives present in the wget but
  not credited on any article (the editor "joan") are emitted as static pages
  so inbound links resolve. (196/197 covered.)
- `/category/<issue>/<section>/` archives are regenerated as **content pages**,
  not a Hugo taxonomy — the nested, per-issue slugs (`articles-1-1`) don't fit
  flat taxonomy term URLs. Deep `/page/N/` pagination is intentionally dropped
  (the term/section pages list everything on one page; no content loss).

## 12. Chrome rebuilt from scratch; analytics re-added via the RRCHNM partial
The `<head>`/`<footer>` were rebuilt as clean partials rather than ported
verbatim. Dropped in the process: the WordPress emoji script, `wp-json` /
`xmlrpc` / `pingback` links, the `s.w.org` prefetch, and the `chnmdev.gmu.edu`
dev-host leak.

Analytics was first removed, then **re-added following RRCHNM's standard
pattern** (`chnm/game-sites` `themes/rrchnm/layouts/partials/analytics.html`):
`layouts/partials/analytics.html` renders the Matomo tracker only when
`hugo.IsProduction` **and** `params.matomoSiteId` is set, defaulting to
`https://stats.rrchnm.org/` (overridable via `params.matomoUrl`). This site's id
is **`matomoSiteId = 28`** in `hugo.toml`. So `hugo server` / dev builds emit no
tracker; the production Docker build does.

## 13. Crawl-log–driven link repairs
`wgets/.../.crawl/` artifacts drove concrete fixes (`839e23e`):
- `failures.tsv` (6 genuine 404s) → `LINK_FIXES` repairs 3 malformed schema-less
  links that wget baked into absolute-internal 404s (e.g.
  `…/mith.umd.edu/topicmodeling` → `https://mith.umd.edu/topicmodeling`);
  `MANUAL_MAP` remaps `/review-of-wordseer/` (already dead in the original
  WordPress) to the real `/1-1/wordseer/`.
- `excluded.tsv` + `.gitignore` confirmed what was deliberately not crawled
  (uploads, files, wp-json, feeds, query-param URLs), validating #4 and the
  decision to drop feeds/cruft.

## 14. Search: Pagefind
Full-text search is a Pagefind index built from `public/` **after** Hugo; the
header form posts to `/search/`, which mounts the Pagefind UI. The toolchain is
pinned in `package.json` / `package-lock.json`. (`48f15be`)

## 15. Deploy: Docker (stagex + Caddy) + RRCHNM CI/CD
Two-stage build — stagex Node + Hugo-extended builds the site and the Pagefind
index; Caddy serves static `public/` on :80. The Dockerfile takes a
`hugobuildargs` build-arg (`RUN hugo ${HUGO_BUILD_ARGS}`) so CI can inject the
`--baseURL`/`--environment` per deploy.

`.github/workflows/cicd.yml` calls RRCHNM's reusable workflow
(`chnm/.github/.github/workflows/hugo--build-release-deploy.yml@main`) for
**jdh.dev.chnm.gmu.edu**. Because this repo is a single site at the root, the build
context is `.`; because the image serves from Caddy's `/srv` (not nginx's
`/usr/share/nginx/html/`), `hugo-content-path` is overridden to `/srv/`. The
workflow builds non-`main` branches with `--environment development` (no
analytics, dev baseURL) and `main` with `--environment production --minify`
(analytics on, prod baseURL).

## Verification
`scripts/verify_urls.py`: **446/448** archive URLs resolve (the 2 gaps are deep
`/author/editor/page/N/` pagination — no content loss), **0 broken internal
links** across ~9,400 links.
