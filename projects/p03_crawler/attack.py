"""Hostile website for the crawler. Run: python projects/p03_crawler/attack.py"""
import asyncio, inspect, os, random, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PORT = 8765
random.seed(1)


class Site(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def send(self, code, body="", headers=None):
        self.send_response(code)
        self.send_header("Content-Type", "text/html")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body.encode())

    def do_GET(self):
        p = self.path
        if p == "/robots.txt":
            return self.send(200, "User-agent: *\nDisallow: /private/\nCrawl-delay: 0\n")
        if p == "/":
            return self.send(200, '<a href="/a">a</a> <a href="b">rel</a> <a href="/loop1">loop</a> '
                                  '<a href="/hang">hang</a> <a href="/big">big</a> <a href="/private/x">no</a> '
                                  '<a href="/flaky">flaky</a> <a href="ht!tp://bad url">bad</a> '
                                  '<a href="/a#frag">a-again</a> <a href="/a">a-dupe</a> '
                                  '<a href="https://example.com/off">offsite</a>')
        if p in ("/a", "/a/"):
            return self.send(200, '<a href="/">home</a> <a href="../b">up</a>')
        if p == "/b":
            return self.send(200, "<p>leaf</p>")
        if p == "/loop1":
            return self.send(302, "", {"Location": "/loop2"})
        if p == "/loop2":
            return self.send(302, "", {"Location": "/loop1"})
        if p == "/hang":
            time.sleep(30); return self.send(200, "slow")
        if p == "/big":
            return self.send(200, " ".join(f'<a href="/big/{i}">{i}</a>' for i in range(2000)))
        if p.startswith("/big/"):
            return self.send(200, "<p>leaf</p>")
        if p.startswith("/private/"):
            return self.send(200, "<b>YOU SHOULD NOT BE HERE</b>")
        if p == "/flaky":
            return self.send(503 if random.random() < 0.5 else 200, "<p>flaky</p>", {"Retry-After": "0"})
        return self.send(404, "nope")


def main():
    try:
        import crawler  # noqa
    except ImportError:
        print("⬜ projects/p03_crawler/crawler.py not found yet — implement crawl() first."); return
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Site)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{PORT}/"
    # First: a small crawl whose ONLY slow page is /hang. This isolates timeout handling
    # from raw throughput, so the clock below measures your timeouts, not your speed.
    t0 = time.perf_counter()
    small = crawler.crawl(base + "hang", max_depth=0, max_concurrency=10, timeout=3.0)
    if inspect.isawaitable(small):
        small = asyncio.run(small)
    hang_dt = time.perf_counter() - t0

    t0 = time.perf_counter()
    res = crawler.crawl(base, max_depth=2, max_concurrency=10, timeout=3.0)
    if inspect.isawaitable(res):
        res = asyncio.run(res)
    dt = time.perf_counter() - t0
    pages = getattr(res, "pages", res if isinstance(res, dict) else {})
    keys = set(pages)
    errors = getattr(res, "errors", {})
    checks = [
        ("a page that hangs 30 s times out fast (crawl of /hang alone under 10 s)", hang_dt < 10),
        ("the hanging page is recorded as an error, not a crash",
         any("/hang" in k for k in getattr(small, "errors", errors))),
        ("did not crawl /private/ (robots.txt Disallow)", not any("/private/" in k for k in keys)),
        ("/a fetched once despite /a, /a#frag and a duplicate link (fragment + dedupe)",
         sum(1 for k in keys if k.rstrip("/").endswith("/a")) == 1),
        ("stayed on the start host (no example.com)", not any("example.com" in k for k in keys)),
        ("survived the redirect loop without hanging or recursing forever", True),
        ("handled the 2,000-link page (crawled at least 100 of them)",
         sum(1 for k in keys if "/big/" in k) >= 100),
        ("whole crawl finished in reasonable time", dt < 90),
    ]
    ok = 0
    for name, passed in checks:
        print(("✅" if passed else "❌"), name); ok += passed
    print(f"\n{ok}/{len(checks)} passed in {dt:.1f}s, {len(keys)} pages crawled")
    srv.shutdown()


if __name__ == "__main__":
    main()
