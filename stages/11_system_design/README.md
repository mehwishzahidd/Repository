# Stage 11 — General system design 🚨

> **Roadmap Groups 13, 14, 31 & 39.** System design is a *communication* skill as much
> as a knowledge one. You need a repeatable process you can run under pressure, and
> enough building-block knowledge to go deep wherever the interviewer points.

## If you're new to this

A system-design interview is 45–60 minutes of "design X" (a URL shortener, a chat app,
an inference API) on a whiteboard, with the interviewer probing every choice. Nobody
expects a perfect answer. They expect a **process**: clarify → estimate → sketch →
deep-dive → find what breaks; and **trade-offs**: "A because X, downside Y, if Z changes
I'd pick B." By this stage you've built enough (API, DB, cache, queue, workers) that the
boxes on the whiteboard are things you've actually run.

**Time:** 6–8 weeks at ~10 hours/week, and then ongoing practice forever.

**Prerequisites:** Stages 06, 07, 10. Stage 12 deepens the distributed parts.

---

## Modules (in order)

1. **The 7-step process** — (1) clarify functional + non-functional requirements
   (scale, latency, availability, durability, consistency); (2) **estimate**: users,
   req/s, storage/day, bandwidth, read/write ratio — know the powers of ten and a few
   latency numbers by heart; (3) **API** design; (4) **data model**; (5) **high-level
   architecture**; (6) **bottlenecks** at 10×/100×/1000×; (7) **deep dive** where asked.
   Practise the *process* on three easy problems before learning more blocks.
2. **Building blocks** — DNS, **load balancers** (L4/L7, algorithms, health checks),
   **reverse proxies / API gateways**, stateless app servers, **caches** (where and
   what), **CDNs**, **object storage** (S3), **databases** (SQL vs NoSQL: KV, document,
   wide-column, graph, time-series, search), **queues / pub-sub**, **workers**,
   **schedulers/cron**, **search** (inverted index, Elasticsearch), **blob/file**
   handling, **websockets / SSE** for push.
3. **Scaling the database (Group 14)** — vertical vs horizontal, **read replicas** and
   **replication lag**, leader/follower, **failover**, **sharding** (key choice, hot
   shards, resharding, cross-shard joins), **consistent hashing** (draw the ring),
   partitioning strategies, indexes at scale, connection pooling/proxies, CQRS in one
   paragraph.
4. **Consistency & availability at design level** — strong vs eventual, read-your-writes,
   where you accept staleness (and where you can't: money, inventory), CAP as a
   design conversation (Stage 12 for the theory).
5. **Rate limiting (Group 31)** — token bucket, leaky bucket, fixed window, sliding
   window log/counter; **distributed** rate limiting with Redis; limits by requests,
   tokens *and* concurrency; 429 + `Retry-After`; where in the stack it lives.
6. **Reliability at design level** — redundancy, no single points of failure, multi-AZ,
   graceful degradation, idempotent APIs, timeouts/retries/breakers (Stage 10), disaster
   recovery basics (RPO/RTO).
7. **Observability & ops in a design** — metrics/logs/traces, SLOs, dashboards,
   alerting, deploys; Stage 13 makes these concrete. Mention them unprompted.
8. **Security in a design** — authn/authz at the gateway, TLS everywhere, secrets, tenant
   isolation, PII handling, abuse limits.
9. **Communication** — think aloud, write as you talk, draw boxes and arrows, state
   assumptions, ask 3 clarifying questions max, drive the conversation, take hints
   gracefully, keep a time budget (5/5/10/15/15).
10. **The catalogue (Group 39)** — practise each one end-to-end with the process:
    *General:* URL shortener, pastebin, rate limiter, key-value store, chat/WhatsApp,
    notification service, news feed, Twitter, file storage/Dropbox, search autocomplete,
    YouTube/streaming, ride sharing, ticket booking (inventory + consistency), payment
    system (idempotency).
    *Infrastructure:* webhook delivery platform, distributed job scheduler, message
    queue, distributed cache, metrics/monitoring system, logging platform, distributed
    KV store, distributed database, web crawler, CI system, feature-flag service.
    *(Inference designs are Stage 18–20.)*

---

## 📚 Resources

### Courses & videos
- ⭐ **ByteByteGo** (YouTube channel + newsletter, Alex Xu) 🆓 — clear diagrams of real
  systems. Watch the whole "System Design" playlist.
- ⭐ **Hello Interview — System Design in a Hurry + guided walkthroughs**
  (hellointerview.com) 🆓 — the most interview-accurate free material right now, with
  written solutions for the catalogue above.
- **Jordan has no life** (YouTube) 🆓 — long-form, deep, opinionated; great after ByteByteGo.
- **Gaurav Sen** (YouTube) 🆓 — approachable intros to each building block.
- **Grokking the System Design Interview** (Educative / designgurus) 💰 — the classic
  structured course. Optional.
- **Martin Kleppmann's DDIA lectures** (Cambridge, YouTube) 🆓 — replication, partitioning.
- **InfoQ / QCon talks, Uber/Netflix/Discord engineering blogs** 🆓 — real systems.

### Books
- ⭐ **System Design Interview – An Insider's Guide, Vol. 1 & 2** (Alex Xu) 💰 — the
  interview books; every chapter is a worked problem.
- ⭐ **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapters 5–7 (replication,
  partitioning, transactions) now; 8–9 in Stage 12.
- **System Design Primer** (github.com/donnemartin/system-design-primer) 🆓 — the
  famous repo; the "study guide" and per-component sections.
- **Understanding Distributed Systems** (Roberto Vitillo) 💰 — short, modern, practical.
- **Web Scalability for Startup Engineers** (Artur Ejsmont) 💰 — underrated, very clear.
- **Site Reliability Engineering** (Google) 🆓 — chapters 3–6 for SLOs and monitoring.
- **Papers (read the ideas, not every proof):** Dynamo (Amazon), Bigtable, GFS,
  MapReduce, Consistent Hashing (Karger), Cassandra, Spanner (abstract), Chubby. 🆓

### Practice
- ⭐ **Mock interviews** — with a peer, or record yourself; Hello Interview 💰 and
  interviewing.io 💰 sell mocks with engineers. Do at least 6 before Stage 20.
- **Excalidraw / draw.io** 🆓 — draw every design; keep them in `notes/designs/`.
- **Write a `DESIGN.md` for P2, P4, P6** as if presenting each in an interview.
- **Estimation drills:** "How many req/s is 100M daily users?" until it's instant.

### Reference
- **Latency numbers every programmer should know** 🆓 (Jeff Dean's table) — memorise.
- **Hello Interview "core concepts" and "key technologies" pages** 🆓.
- **AWS Architecture Center / Well-Architected Framework** 🆓.
- **Stripe, Cloudflare, Figma, Discord engineering blogs** on rate limiting, sharding,
  and caching 🆓.

---

## Practice & exercises
- Run the 7-step process on **URL shortener** in 45 min, recorded, out loud. Watch it
  back. Do it again a week later.
- Estimate, from scratch, storage and QPS for Twitter, WhatsApp and YouTube; check
  against published numbers.
- Design a **rate limiter** four ways; implement token bucket and sliding-window-counter
  in Redis; explain when each is wrong.
- Draw consistent hashing with 5 nodes and virtual nodes; remove a node; count what moves.
- Design a **notification service** with fan-out, dedupe, retries and per-user rate
  limits; then the interviewer says "now 100× traffic and one region goes down".
- Design a **distributed job scheduler**, then a **distributed cache**, then a
  **metrics system** — the infra list is your interview.
- Write `DESIGN.md` for P6 and present it to a friend or an AI playing interviewer.

## Beginner pitfalls
- **Jumping to the diagram** without requirements or numbers.
- **Name-dropping** ("Kafka! Cassandra!") without a reason. Every box needs a why.
- **Over-engineering.** Anthropic's principles and the hiring manager both reward the
  simplest thing that meets the requirements.
- **Silence.** Think aloud; a quiet minute feels like five to the interviewer.
- **Ignoring failure.** Ask yourself what breaks *before* they do.
- **Not managing time.** Deep dive on one thing, not shallow on everything.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You run the 7-step process on any catalogue problem in 45 minutes, out loud, with
      numbers, an API, a data model, a diagram, a deep dive and a failure discussion.
- [ ] You explain replication, sharding, consistent hashing and replication lag, and
      choose a shard key for a given workload.
- [ ] You design and implement a rate limiter and defend the algorithm choice.
- [ ] You've done 6+ recorded or peer mock designs including 3 from the infrastructure
      list, and each has a written `DESIGN.md`.
- [ ] Every design you present mentions observability, failure modes and trade-offs
      without being prompted.

## 🛠️ Project
`DESIGN.md` documents for P2, P4 and P6, presented as interviews. Six mock designs.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 12"** to get its hands-on lessons built.
