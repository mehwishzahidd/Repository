# Stage 07 — Networking

> **Roadmap Group 7.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

You don't need to be a network engineer, but infra work is *made of* network calls that fail. Everything in the crawler, and most of what breaks in production, lives here.

**Prerequisite:** Stage 06 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Internet basics
client/server · IP addresses · ports · **DNS** · **TCP** vs **UDP** · sockets (write a tiny echo server)

### Web
HTTP/HTTPS · **TLS** · headers · cookies · methods · status codes · request/response lifecycle · keep-alive · **connection pooling**

### URLs
scheme · domain · port · path · query · fragment · relative vs absolute · **normalization**

### Failure modes (the crawler's world)
redirects & redirect loops · `robots.txt` · rate limiting · timeouts · malformed URLs · DNS and connection failures

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Write a raw TCP echo server and client with `socket`.
- [ ] Explain, in order, what happens from typing a URL to seeing a page.
- [ ] Normalize a messy list of URLs correctly (relative paths, trailing slashes, case, fragments).

## 🛠️ Project

Start **P3 — the web crawler** (single-threaded first). Concurrency is added in Stage 09.

## 📚 Free resources

- *High Performance Browser Networking* (free online) — the first chapters
- *Computer Networking: A Top-Down Approach* (Kurose) for depth
- MDN HTTP docs

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 08"** to get its hands-on lessons built.
