# 🛠️ PROJECTS — the ladder you climb

Knowing vocabulary isn't enough. These ten projects are built **in this order**, and each
one uses what the previous one taught. **No copying tutorials.** You build V1, then it gets
attacked, and you fix it. That's how the reasoning the interviews actually test gets built.

```
P1  Python programs
 ↓
P2  REST API + Postgres
 ↓
P3  Concurrent web crawler
 ↓
P4  Task scheduler using DAGs
 ↓
P5  Thread-safe LRU cache
 ↓
P6  Webhook delivery system (workers + retries + DLQ + leases)
 ↓
P7  Mini database (SQL-ish queries + indexes + joins)
 ↓
P8  Distributed job queue
 ↓
P9  LLM inference API
 ↓
P10 LLM scheduler (batching + priorities + streaming + KV-cache simulation)
 ↓
🔥  Advanced Anthropic interview prep
```

Each project lives in its own folder under `projects/` once you start it (e.g.
`projects/03_crawler/`). Write a short `DESIGN.md` in each one: what it does, the key
decisions, and what broke when it was attacked.

---

## P1 — Python programs *(Stage 01–02)*
**Build:** a handful of small CLI programs: a number-guessing game, a to-do list saved to
a file, a word-frequency counter, a unit converter, a tiny contact book using dictionaries
and classes.
**Done when:** you can write a 100-line program from a blank file without looking up
basic syntax.
**Attacks:** empty input · file doesn't exist · user types letters where a number is expected.

## P2 — REST API + Postgres *(Stage 05–06)*
**Build:** `Client → FastAPI → Postgres`. A notes/bookmarks API with create / read /
list / update / delete, pagination, input validation, proper error responses, and pytest
tests (with the DB mocked *and* a real integration test).
**Done when:** every endpoint is tested and the service runs from a `Dockerfile`.
**Attacks:** duplicate create · huge page size · malformed JSON · DB is down · two
clients update the same row at once.

## P3 — Concurrent web crawler *(Stage 07–09)*
**Build:** start URL → fetch → extract links → dedupe → BFS to the next level, with
`asyncio`, a semaphore for max concurrency, a max depth, and timeouts.
**Then add:** rate limiting per host, `robots.txt`, retries with backoff, redirect and
loop detection, relative-URL resolution and normalization, cancellation.
**Done when:** it crawls a real site politely, never hangs, and never crawls the same
page twice.
**Attacks:** redirect loop · a page that never responds · malformed HTML · DNS failure ·
10,000 links on one page · you press Ctrl-C mid-crawl.

## P4 — Task scheduler using DAGs *(Stage 09–10)*
**Build:** tasks with dependencies (`A → B → C`), topological ordering, parallel
execution of independent tasks with a worker pool, and **cycle detection**
(`A → B → C → A` must be rejected).
**Then add:** priorities, retries, per-task timeouts, a "what's blocked on what" view.
**Attacks:** a task fails halfway · a worker dies · a cycle is introduced at runtime ·
a premium task arrives behind 500 low-priority ones.

## P5 — Thread-safe LRU cache *(Stage 09)*
**Build:** hash map + doubly linked list, O(1) get / put / evict, from scratch. Then make
it **thread-safe** without making it slow. Then add TTL.
**Done when:** you can explain *why* each operation is O(1) and prove thread safety with
a stress test.
**Attacks:** capacity = 0 · duplicate puts · 50 threads hammering it · a get during
eviction · what if the value is huge?

## P6 — Webhook delivery system *(Stage 10)*
**Build:** producers enqueue events; workers deliver them over HTTP with timeouts,
retries with exponential backoff + jitter, a dead-letter queue, **leases** so a dead
worker's job gets picked up by another, and idempotency keys so nothing is delivered twice.
**Attacks:** the receiver is down for an hour · a worker crashes mid-delivery · the same
event is enqueued twice · 100× the traffic · graceful shutdown mid-batch.

## P7 — Mini database *(Stage 12)*
**Build:** an in-memory (then on-disk) table store with a SQL-ish query language:
`SELECT ... WHERE ...`, inserts, a B-tree or hash **index**, and **joins** (nested-loop,
then hash join). Then add a write-ahead log so it survives a crash.
**Done when:** you can explain when you'd choose nested-loop vs hash vs sort-merge join.
**Attacks:** crash between the WAL write and the data write · a query that ignores the
index · 1M rows · two transactions writing the same key.

## P8 — Distributed job queue *(Stage 12)*
**Build:** P6's queue, but across multiple processes/machines: at-least-once delivery,
acknowledgements, visibility timeouts, ordering guarantees per key, and a simple leader
election for the coordinator.
**Attacks:** the network partitions · the leader dies · a message arrives twice · clocks
disagree between nodes · a consumer is 10× slower than the others (backpressure).

## P9 — LLM inference API *(Stage 17)*
**Build:** a small model (Hugging Face / vLLM) behind an API: `User → API → Scheduler →
GPU worker → Model → stream tokens` using SSE. Measure **TTFT**, **TPOT**, throughput,
p50/p95/p99.
**Attacks:** the client disconnects mid-generation · 50 concurrent requests · a
150k-token prompt · the worker OOMs.

## P10 — LLM scheduler *(Stage 18–19)*
**Build:** a scheduler (simulated GPU is fine) that does continuous **batching**,
**priority** tiers with starvation prevention, admission control by token count and
memory, **streaming**, cancellation, and a **KV-cache simulation** (allocation, eviction,
paging, prefix reuse).
**Done when:** you can dial the batching knob and *show* the latency-vs-throughput
trade-off on a graph, and explain why GPU utilization can look fine while users wait.
**Attacks:** one GPU dies · p99 doubles, investigate · queue is full (backpressure /
load shedding) · premium customers starve normal traffic · autoscale on the right signal.

---

## 🔥 Then: the interview loop, for real
With P1–P10 done you have covered every round of that five-round loop (LRU cache,
task-system DAG, crawler, inference system design, profiler coding, hiring manager).
Stage 20 turns it into timed mock interviews.
