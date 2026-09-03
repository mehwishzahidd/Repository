# Stage 10 — Caching, queues, workers and reliability

> **Roadmap Groups 10, 11 & 12.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Real systems are an API, a cache, a queue and a pool of workers — and then a long list of ways they fail. This stage is where you start to automatically ask *what happens if this process dies exactly here?*

**Prerequisite:** Stage 09 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Caching (Group 10)
what caches solve · Redis · hit/miss · TTL · eviction · cache-aside / write-through / write-back · stale data · invalidation · **cache stampede** · hot keys · penetration

### Queues (Group 11)
`Producer → Queue → Consumer` · brokers · workers · acknowledgement · retry · **visibility timeout** · **dead-letter queue** · ordering · durability · Kafka / RabbitMQ / SQS concepts · at-most-once vs at-least-once vs "exactly once"

### Reliability (Group 12)
timeouts · retries · exponential backoff · **jitter** · circuit breakers (open after N consecutive failures; pick N deliberately) · health checks · heartbeats · **leases** · **idempotency** · **backpressure** · load shedding · graceful degradation & shutdown · failure recovery

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Add Redis caching to P2 and demonstrate a stampede, then prevent it.
- [ ] Explain why exactly-once delivery is hard and how idempotency keys sidestep it.
- [ ] Kill a worker mid-job and show another worker picking it up via a lease (the bug the OpenAI interviewer found: without leases the event is stuck 'in progress' forever).
- [ ] Sign a webhook delivery with HMAC and verify it on the receiving side.

## 🛠️ Project

**P4 — DAG task scheduler** and **P6 — Webhook delivery system** (see `PROJECTS.md`).

## 📚 Free resources

- Redis docs · *Redis in Action* (free online)
- *Designing Data-Intensive Applications* (Kleppmann) ch. 1–4, 11
- AWS SQS / Google Pub/Sub docs on delivery semantics

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 11"** to get its hands-on lessons built.
