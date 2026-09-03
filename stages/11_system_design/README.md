# Stage 11 — General system design 🚨

> **Roadmap Groups 13, 14, 31 & 39.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

System design is a *communication* skill as much as a knowledge one. You need a repeatable process you can run under pressure, and enough building-block knowledge to go deep wherever the interviewer points.

**Prerequisite:** Stage 10 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### The 7-step process
1 clarify requirements (functional + scale/latency/availability/durability/consistency) → 2 estimate scale (req/s, storage/day, bandwidth, read/write ratio) → 3 API design → 4 data model → 5 high-level architecture → 6 find bottlenecks (10×? 100×? 1000×?) → 7 deep dive

### Building blocks
load balancers · API gateways · reverse proxies · databases · caches · queues · pub/sub · workers · object storage · CDN · search · rate limiters · schedulers

### Database scaling (Group 14)
replication (read replicas, lag, failover, leader/follower) · sharding (shard keys, hot shards, resharding, **consistent hashing**, cross-shard queries)

### Rate limiting (Group 31)
token bucket · leaky bucket · fixed window · sliding window · distributed rate limiting · requests/min *and* tokens/min *and* concurrency limits

### Questions to master (Group 39)
URL shortener · chat · notifications · file storage · autocomplete · news feed · rate limiter · webhook platform · distributed job scheduler · message queue · distributed cache · metrics system · logging platform · KV store · web crawler

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Run the 7-step process on 'design a URL shortener' in 45 minutes, out loud, and record yourself.
- [ ] Draw the load-balancer → API → cache → DB → queue → workers diagram and explain what breaks at 100× traffic.
- [ ] Design a rate limiter and explain the trade-offs between the four algorithms.

## 🛠️ Project

Write a `DESIGN.md` for P2/P6 as if presenting it in an interview.

## 📚 Free resources

- System Design Primer (GitHub, free) · ByteByteGo (blog + YouTube)
- *Designing Data-Intensive Applications* (Kleppmann) — the essential book
- *Grokking the System Design Interview*

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 12"** to get its hands-on lessons built.
