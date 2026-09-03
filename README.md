# 🧗 Zero → Infrastructure / ML Inference SWE

A from-scratch, one-person curriculum for going from **"what is programming?"** to being
able to walk into an **Anthropic / OpenAI-style infrastructure & inference SWE interview**
and have nothing they ask feel unfamiliar.

Right now words like *KV cache, MVCC, WAL, DAG, semaphores, sharding, inference
scheduling* sound like another language. That's fine. Those are Level-100 words. You are
at Level 1, and this repo is the road between the two.

```
📍 START                                                              🏁 FINISH
   Python / programming fundamentals   ───────────────────▶   Advanced infrastructure SWE
                                                              distributed systems + ML systems
```

---

## The three files that matter

| File | What it is |
|---|---|
| [`ROADMAP.md`](./ROADMAP.md) | **The destination map.** All 40 skill groups, the honest timeline, how it maps to the interview rounds, and what "ready" actually means. Read once now, re-read every few months. |
| [`PROJECTS.md`](./PROJECTS.md) | **The 10 projects you will build**, in order, plus the ways each one gets attacked afterwards. |
| [`PROGRESS.md`](./PROGRESS.md) | **Your checklist.** Tick things off as you go. Commit it. |

---

## 🚦 The learning order (this is the order, not the checklist)

Each step is a folder under [`stages/`](./stages/) with its goals, topics, a checkpoint
that tells you when you're done, and the project that goes with it.

| Step | Stage | Roadmap groups | Project |
|---|---|---|---|
| 1 | [`01_python`](./stages/01_python/) — runnable lessons 🟢 | 1 | P1 Python programs |
| 2 | [`02_programming`](./stages/02_programming/) — classes, files, stdlib, stronger Python | 1, 3 | P1 |
| 3 | [`03_dsa`](./stages/03_dsa/) — data structures & algorithms | 2, 34 | LRU cache v1 |
| 4 | [`04_git_linux`](./stages/04_git_linux/) — Git, GitHub, shell, Linux | 1 | — |
| 5 | [`05_sql_databases`](./stages/05_sql_databases/) — SQL, schema design, indexes | 9 | — |
| 6 | [`06_backend`](./stages/06_backend/) — APIs, FastAPI, Postgres, testing | 4, 8 | P2 REST API + Postgres |
| 7 | [`07_networking`](./stages/07_networking/) — TCP, HTTP, URLs, DNS | 7 | — |
| 8 | [`08_operating_systems`](./stages/08_operating_systems/) — processes, threads, memory | 5 | — |
| 9 | [`09_concurrency`](./stages/09_concurrency/) — threads, asyncio, locks, deadlocks 🚨 | 6, 33 | P3 crawler · P5 thread-safe LRU |
| 10 | [`10_caching_queues_workers`](./stages/10_caching_queues_workers/) — Redis, queues, reliability | 10, 11, 12 | P4 DAG scheduler · P6 webhooks |
| 11 | [`11_system_design`](./stages/11_system_design/) — the repeatable process 🚨 | 13, 14, 31, 39 | — |
| 12 | [`12_distributed_systems`](./stages/12_distributed_systems/) — consensus, replication, time 🚨 | 15 | P7 mini DB · P8 job queue |
| 13 | [`13_production_infra`](./stages/13_production_infra/) — Docker, k8s, cloud, CI/CD, observability, security | 16–19, 35, 36 | — |
| 14 | [`14_ml_fundamentals`](./stages/14_ml_fundamentals/) — training vs inference, neural nets | 20 | — |
| 15 | [`15_transformers`](./stages/15_transformers/) — tokens, attention, context window | 20 | — |
| 16 | [`16_gpus`](./stages/16_gpus/) — VRAM, bandwidth, kernels | 22 | — |
| 17 | [`17_llm_inference`](./stages/17_llm_inference/) — prefill/decode, serving, streaming, metrics | 21, 26, 27, 30 | P9 inference API |
| 18 | [`18_batching_kvcache_scheduling`](./stages/18_batching_kvcache_scheduling/) — the heart of it 🚨🚨 | 23, 24, 25, 32 | P10 LLM scheduler |
| 19 | [`19_multi_gpu_inference`](./stages/19_multi_gpu_inference/) — parallelism, collectives, optimization | 28, 29 | — |
| 20 | [`20_mock_interviews`](./stages/20_mock_interviews/) — behavioral, communication, mock loops | 37, 38, 39 | 🔥 |

> 🟢 = lessons you can run today. Everything else has a full syllabus and checkpoint, and
> gets hands-on lessons built out when you reach it, so you don't drown in content you're
> not ready for.

---

## ⏱️ The honest timeline

| Time from now | Realistic level |
|---|---|
| 0–3 months | Programming fundamentals, Python, Git, basic SQL, basic DSA |
| 3–6 months | Backend apps, APIs, databases, testing, Docker |
| 6–12 months | Solid junior SWE, stronger DSA, basic system design, concurrency intro |
| 12–18 months | Strong backend interview prep, distributed-systems foundations |
| 18–24 months | Advanced infra projects, database internals, production-style systems |
| 2–3+ years | Realistic shot at OpenAI/Anthropic-style infra loops |

**"Could I apply?"** — within the first year (internships / junior roles).
**"Could I understand all the rounds?"** — ~1.5–2 years.
**"Could I be competitive with people who ran infra in production?"** — 2–4 years.

You get jobs, build experience and earn money *during* the climb. You don't wait until
you're Anthropic-ready to do anything.

---

## 🟢 Start here, today

1. Skim [`ROADMAP.md`](./ROADMAP.md) once so you know where the road goes. Don't try to
   learn it. Just look at the map.
2. Run your first program:
   ```bash
   python3 stages/01_python/01_hello_world.py
   ```
3. Work through the Stage 01 lessons in order, then the auto-graded exercises:
   ```bash
   python3 stages/01_python/exercises/check.py
   ```
4. Tick off Stage 01 in [`PROGRESS.md`](./PROGRESS.md) and commit.

When Stage 01's exercises all pass, say **"ready for Stage 02"** and it gets built.

---

## How this repo is organized

```
.
├── README.md        ← you are here: the order + how to start
├── ROADMAP.md       ← the 40-group destination map
├── PROJECTS.md      ← the 10-project ladder + attack scenarios
├── PROGRESS.md      ← your checklist
└── stages/
    ├── 01_python/                       🟢 runnable lessons + exercises
    ├── 02_programming/
    ├── 03_dsa/
    ├── ...
    └── 20_mock_interviews/
```

> The rules: **one stage at a time. Code every day. Never skip the "build it yourself"
> part.** Consistency beats intensity, every time.
