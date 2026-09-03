# Stage 10 — Caching, queues, workers and reliability

> **Roadmap Groups 10, 11 & 12.** Real systems are an API, a cache, a queue and a pool
> of workers — and then a long list of ways they fail. This is where you start to
> automatically ask *what happens if this process dies exactly here?* It's also the
> stage that builds the OpenAI take-home.

## If you're new to this

A **cache** keeps copies of expensive-to-get things somewhere fast. A **queue** is a line
of jobs waiting for **workers** to process them, so the API can say "got it" instantly and
do the slow work later. **Reliability patterns** (timeouts, retries, backoff, leases,
circuit breakers, dead-letter queues) are the difference between a demo and something
that survives a bad day in production.

**Time:** 5–7 weeks at ~10–12 hours/week.

**Prerequisites:** Stages 06 and 09.

---

## Modules (in order)

1. **Caching fundamentals (Group 10)** — what caches solve (latency, load, cost), hit
   rate, TTL, **eviction** (LRU/LFU/FIFO — you built one), where caches live (browser,
   CDN, in-process, Redis, DB buffer pool).
2. **Redis** — install, data types (strings, hashes, lists, sets, sorted sets), TTLs,
   `INCR` for counters and rate limits, pub/sub, Lua for atomic ops, persistence
   (RDB/AOF) and what it doesn't promise, `redis-py`.
3. **Cache patterns** — **cache-aside**, read-through, **write-through**, **write-back**,
   write-around; **invalidation** (the famously hard problem), stale data and TTLs,
   negative caching.
4. **Cache failure modes** — **stampede / dogpile** (and fixes: locking, early
   recompute, jitter on TTLs), **hot keys**, **cache penetration** (bloom filters),
   avalanche, consistency between cache and DB.
5. **Queues (Group 11)** — producer / broker / consumer, push vs pull, **acknowledgement**,
   **visibility timeout**, redelivery, **dead-letter queues**, ordering (per-key), fan-out,
   durability, delivery semantics: **at-most-once**, **at-least-once**, and why
   **exactly-once** is really "at-least-once + idempotency".
6. **Brokers in practice** — Redis lists/streams (simplest), **RabbitMQ** (AMQP, routing),
   **Kafka** (a log, partitions, consumer groups, offsets, retention — different animal),
   **SQS** concepts. Use one; understand the trade-offs of all three.
7. **Workers** — the polling worker (select-for-update / `SKIP LOCKED` pattern in
   Postgres), long-polling, prefetch, concurrency per worker, graceful shutdown, poison
   messages, Celery/RQ/arq/Dramatiq as ready-made frameworks.
8. **Reliability toolkit (Group 12)** — **timeouts** everywhere, **retries** with
   **exponential backoff + jitter**, **idempotency keys**, **circuit breakers** (closed →
   open after N failures → half-open probe; choosing N and the cool-down), **bulkheads**,
   **health checks** (liveness vs readiness), **heartbeats**, **leases** (time-limited
   ownership so dead workers' jobs get picked up), **backpressure** (bounded queues,
   429s), **load shedding**, **graceful degradation**, **graceful shutdown**.
9. **The webhook delivery system (the take-home)** — endpoint registration, event
   ingestion, delivery worker, retries + backoff, DLQ, status API, HMAC signatures,
   event-type filtering, per-endpoint circuit breaker, leases for crashed workers,
   idempotency keys. Clean code and tests over feature count.
10. **The DAG task scheduler (P4)** — dependencies, topological execution with a worker
    pool, priorities, worker assignment, cascading cancellation, retries, timeouts.
11. **Failure injection** — kill workers, drop the broker, make the receiver time out,
    duplicate messages, run at 100× — and watch what your system does.

---

## 📚 Resources

### Courses & videos
- ⭐ **Redis University — RU101 Introduction to Redis Data Structures** (redis.io/university) 🆓.
- ⭐ **AWS Builders' Library** (aws.amazon.com/builders-library) 🆓 — Marc Brooker et al.
  on *timeouts, retries and backoff with jitter*, *avoiding fallback*, *caching challenges*,
  *using load shedding*, *leader election*. Short, from people who run it at scale.
- **Confluent Developer — Apache Kafka 101** 🆓 — Kafka concepts in an afternoon.
- **RabbitMQ tutorials** (rabbitmq.com/tutorials, Python) 🆓 — do 1–6.
- **Hussein Nasser — Message queues, Redis, Kafka videos** (YouTube) 🆓.
- **Marc Brooker's blog** 🆓 — backoff, jitter, "exactly once", metastable failures.

### Books
- ⭐ **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapters 1, 4, 11
  (stream processing) now; it becomes your main book in Stages 11–12.
- ⭐ **Release It!** (Michael Nygard, 2nd ed.) 💰 — stability patterns: timeouts, circuit
  breakers, bulkheads, steady state, fail fast. The reliability book.
- **Redis in Action** (Josiah Carlson) 🆓 online at redis.com — patterns with real code.
- **Kafka: The Definitive Guide** (Confluent, free PDF) 🆓 — chapters 1–4, 6.
- **Site Reliability Engineering** (Google) 🆓 online — chapters 21–22 (overload,
  cascading failures).
- **Enterprise Integration Patterns** (Hohpe & Woolf) 💰 — the messaging pattern
  catalogue; skim the site (enterpriseintegrationpatterns.com) 🆓.

### Practice
- ⭐ **Build P6 as a 48-hour take-home**, then keep going with the "then add" list.
- **Redis "Try Redis" sandbox** 🆓, **Play with Docker** 🆓 for a throwaway Kafka.
- **Stripe's idempotency blog post** and **Stripe webhooks docs** 🆓 — read how a real
  company does it; copy the ideas.

### Reference
- **Redis docs** (commands, "Redis as a cache", "Streams"), **Kafka docs**, **Postgres
  `SELECT … FOR UPDATE SKIP LOCKED`**, **Celery / arq docs**, **`tenacity`** (retries
  library) docs.

---

## Practice & exercises
- Add Redis cache-aside to P2's hottest endpoint; measure hit rate; expire a key under
  load and *cause* a stampede; fix it with a lock + jittered TTL.
- A Redis sorted-set sliding-window rate limiter; a Lua-scripted token bucket.
- A queue with at-least-once delivery on Postgres (`SKIP LOCKED`), then on Redis Streams,
  then on Kafka; observe duplicates; add idempotency keys.
- A circuit breaker class with tests for closed/open/half-open transitions and cool-down.
- Retry with exponential backoff + full jitter; plot retry timing for 100 clients with
  and without jitter (the thundering herd, visualised).
- Leases: worker A claims a job, is `kill -9`'d, worker B picks it up after the lease
  expires; prove it with a test.
- The DAG scheduler: run a 20-task graph on 4 workers; cancel a middle task and show the
  cascade; inject a cycle and show the rejection.
- Chaos day: run P6 under load while killing workers, stalling the receiver, duplicating
  events, and filling the DLQ. Write down what broke.

## Beginner pitfalls
- **Retrying without backoff or jitter** — you DDoS your own dependency.
- **Retrying non-idempotent operations** — double charges, duplicate emails.
- **Caching without a TTL or invalidation plan** — stale forever.
- **"Exactly once" as a checkbox.** It's a design: at-least-once + idempotent consumers.
- **Marking a job "in progress" with no lease.** The stuck-forever bug from the OpenAI
  deep-dive.
- **Unbounded queues.** They hide overload until the machine dies.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] Redis cache-aside on P2 with a demonstrated and fixed stampede.
- [ ] You explain at-most/at-least/exactly-once and how idempotency keys make retries safe.
- [ ] A crashed worker's job is recovered via a lease, proven by a test.
- [ ] You've built a circuit breaker and a backoff-with-jitter retry, with tests, and can
      say why each parameter is set the way it is.
- [ ] P6 delivers webhooks with HMAC signatures, filtering, DLQ, status API and leases, and
      survives the chaos day.
- [ ] P4 runs DAGs on a worker pool with priorities, cascading cancellation and cycle rejection.

## 🛠️ Project
**P4 — DAG task scheduler** and **P6 — Webhook delivery system** (see `PROJECTS.md`).

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 11"** to get its hands-on lessons built.
