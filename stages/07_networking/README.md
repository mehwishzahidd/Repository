# Stage 07 — Networking

> **Roadmap Group 7.** You don't need to be a network engineer, but infra work is *made
> of* network calls that fail. Everything in the crawler, and most of what breaks in
> production, lives here.

## If you're new to this

When your browser loads a page, dozens of things happen: a name becomes an address
(**DNS**), a connection is opened (**TCP**), it's encrypted (**TLS**), a request is sent
(**HTTP**), and a response streams back. You've been using all of this since Stage 06
without looking under the hood. This stage lifts the hood far enough that you can reason
about latency, timeouts, retries, and the weird failures that only show up in production.

**Time:** 3–4 weeks at ~8–10 hours/week.

**Prerequisites:** Stage 06 (you've built an HTTP service) and Stage 04 (shell).

---

## Modules (in order)

1. **The big picture** — the layered model in plain words (link → IP → TCP/UDP →
   application), packets, what a router does, latency vs bandwidth, why the speed of
   light matters (a request across the Atlantic can't beat ~40 ms).
2. **IP, ports, DNS** — IPv4/IPv6 addresses, public vs private, ports, `localhost`,
   **DNS** resolution step by step (recursive resolver, root, TLD, authoritative), record
   types (A, AAAA, CNAME, TXT), TTLs and caching, `dig`/`nslookup`, DNS failures.
3. **TCP and UDP** — the three-way handshake, reliability, ordering, flow and
   congestion control (conceptually), **connection setup cost** (why pooling exists),
   `TIME_WAIT`, UDP for when you don't care about loss, `ss`/`netstat`, **sockets**:
   write a raw TCP echo server and client in Python.
4. **HTTP in depth** — request/response anatomy, methods, headers (`Content-Type`,
   `Accept`, `Authorization`, `Cache-Control`, `ETag`, `Location`, `Retry-After`),
   status-code families, **keep-alive**, **connection pooling** in clients, HTTP/1.1
   vs **HTTP/2** (multiplexing) vs HTTP/3 (QUIC), chunked transfer, **streaming**
   responses (the shape of an LLM reply).
5. **TLS / HTTPS** — what encryption buys you, certificates and CAs, the handshake
  (conceptually), why TLS adds a round trip, `openssl s_client`, self-signed certs
   locally, mTLS as a concept.
6. **URLs** — scheme, host, port, path, query, fragment; percent-encoding; **relative vs
   absolute** resolution (`urllib.parse.urljoin`); **normalization** (case, trailing
   slash, default ports, dot segments, sorted query, fragment removal) — the crawler's
   dedupe depends on getting this right.
7. **Crawler-world failures** — redirects (301/302/307/308) and **redirect loops**,
   `robots.txt` (parse it: user-agents, allow/disallow, crawl-delay), **rate limiting**
   yourself per host, **timeouts** (connect vs read vs total — "a page that hangs for 30
   seconds"), retries with backoff, malformed URLs, DNS and connection failures,
   compressed bodies, encodings.
8. **HTTP clients in Python** — `httpx` (sync + async), sessions/pooling, timeouts on
   every call, streaming downloads, `aiohttp` awareness.
9. **Load balancers, proxies, CDNs (intro)** — reverse proxies (nginx), L4 vs L7,
   forwarding headers (`X-Forwarded-For`), what a CDN caches; deeper in Stage 11.
10. **Tools** — `curl -v`, `ping`, `traceroute`/`mtr`, `dig`, `ss`, `tcpdump`,
    **Wireshark** (capture one HTTP request and read it), browser dev-tools network tab.

---

## 📚 Resources

### Courses & videos
- ⭐ **Kurose & Ross — Computer Networking: A Top-Down Approach, free video lectures**
  (gaia.cs.umass.edu/kurose_ross) 🆓 — chapters 1–3 (intro, application layer, transport).
- ⭐ **Cloudflare Learning Center** (cloudflare.com/learning) 🆓 — short, clear articles
  on DNS, TLS, HTTP/2, CDNs. Start here for any term you don't know.
- **Practical Networking** (YouTube) 🆓 — how packets actually move; superb visuals.
- **Stanford CS144** (cs144.github.io) 🆓 — university networking with labs where you
  build a TCP implementation. Optional, for depth.
- **Hussein Nasser — Network fundamentals / HTTP playlist** (YouTube) 🆓.
- **Julia Evans — "Networking! ACK!" zine** 💰 — the friendliest intro that exists.

### Books
- ⭐ **High Performance Browser Networking** (Ilya Grigorik) 🆓 online at hpbn.co —
  latency, TCP, TLS, HTTP/1.1/2. Chapters 1–4, 9–12.
- ⭐ **Beej's Guide to Network Programming** 🆓 — sockets, from the socket's point of view.
  C examples; read for concepts, redo in Python.
- **Computer Networking: A Top-Down Approach** (Kurose & Ross) 💰 — the textbook.
- **HTTP: The Definitive Guide** (Gourley & Totty) 💰 — old but the HTTP reference.
- **TCP/IP Illustrated, Vol. 1** (Stevens/Fall) 💰 — the deep reference; not now.

### Practice
- ⭐ **Build P3's single-threaded crawler** with every failure mode above.
- **httpbin.org** 🆓 — an HTTP server that returns whatever you ask (redirects, delays,
  status codes). Perfect for testing timeout and retry logic.
- **Wireshark sample captures** 🆓 — read a real HTTP and DNS exchange.
- **"Build your own HTTP server"** (codecrafters.io 💰, or free by following RFC 9110)
  — parse requests from a raw socket.

### Reference
- **MDN HTTP** 🆓, **RFC 9110/9111** (HTTP semantics/caching), **RFC 3986** (URLs),
  **robots.txt RFC 9309**.
- **`urllib.parse`** and **`httpx`** docs.

---

## Practice & exercises
- Write a TCP echo server and client with `socket`; then a tiny HTTP server that parses
  a GET request and returns HTML.
- Resolve `example.com` by hand with `dig +trace`; explain each hop.
- Capture one HTTPS request in Wireshark; identify the handshake, TLS, and data packets.
- Write `normalize_url()` with 20 test cases (relative paths, `..`, ports, fragments,
  case, trailing slash, query order).
- Write a `robots.txt` parser with tests against real sites' files.
- Against httpbin: hit `/delay/30` with a 5 s read timeout; hit `/redirect/10` and
  `/absolute-redirect/…` with loop detection; hit `/status/503` with backoff retries.
- Measure connection reuse: 100 requests with and without a pooled session; explain the
  difference.

## Beginner pitfalls
- **No timeout** — the default in many libraries is *forever*. Set connect and read
  timeouts on every call.
- **Trusting `Content-Length`** or assuming a body is UTF-8.
- **Comparing URLs as strings** without normalizing.
- **Ignoring `Retry-After`** and hammering a 429/503.
- **Thinking "the network is reliable".** It isn't. Design for it (Stage 10).

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You can explain, in order and in plain words, everything that happens between
      typing a URL and seeing a page.
- [ ] You've written a raw TCP server/client and a minimal HTTP server with `socket`.
- [ ] You normalize a messy list of URLs correctly, with tests.
- [ ] Your crawler handles redirect loops, hanging pages, `robots.txt`, and per-host rate
      limits, with timeouts on every request.
- [ ] You can read a Wireshark capture and a `curl -v` trace.

## 🛠️ Project
**P3 — web crawler, single-threaded version** with a site-map output. Concurrency is
added in Stage 09.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 08"** to get its hands-on lessons built.
