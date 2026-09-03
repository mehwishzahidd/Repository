# P3 — Concurrent web crawler (Stages 07–09)

## Interface contract (what `attack.py` calls)
```python
from crawler import crawl            # projects/p03_crawler/crawler.py
result = crawl(start_url, max_depth=2, max_concurrency=10, timeout=5.0)
# result.pages: dict[url -> list of links found]   (the site map)
# result.errors: dict[url -> str]
```
`crawl` may be sync or `async`; `attack.py` handles both. Normalise URLs, dedupe,
respect `robots.txt`, rate-limit per host, time out per request, detect redirect loops,
resolve relative URLs, and stop cleanly on Ctrl-C.

## Attack
```bash
python projects/p03_crawler/attack.py
```
It starts a hostile local website (redirect loops, a page that hangs 30 s, 2,000 links
on one page, relative and malformed URLs, a `robots.txt` that forbids `/private/`,
random 503s) and checks your crawler's result and wall-clock time.
