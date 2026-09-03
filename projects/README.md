# projects/ — where the ladder gets built

One folder per project from [`PROJECTS.md`](../PROJECTS.md). Each has a `README.md`
with the spec and the **interface contract** the attack script expects, a `DESIGN.md`
template with a decision log, an empty `tests/`, and, where it makes sense, an
`attack.py` that tries to break your implementation.

| Folder | Project | Stage | Attack script |
|---|---|---|---|
| `p01_python_programs/` | P1 Python programs | 01–02 | — |
| `p02_rest_api/` | P2 REST API + Postgres | 05–06 | — (the test suite is the attack) |
| `p03_crawler/` | P3 Concurrent web crawler | 07–09 | `attack.py` (a hostile local website) |
| `p04_dag_scheduler/` | P4 DAG task scheduler | 09–10 | `attack.py` |
| `p05_lru_cache/` | P5 Thread-safe LRU cache | 03, 09 | `attack.py` (50-thread stress) |
| `p06_webhooks/` | P6 Webhook delivery system | 10 | `attack.py` (flaky receiver + chaos) |
| `p07_mini_db/` | P7 Mini database | 12 | — (crash tests live in your `tests/`) |
| `p08_distributed_queue/` | P8 Distributed job queue | 12 | — |
| `p09_inference_api/` | P9 LLM inference API | 17 | — (load generator in README) |
| `p10_llm_scheduler/` | P10 LLM scheduler simulator | 18–19 | — (the simulator *is* the attack) |
| `pmini_profiler/` | P-mini Profiler → trace events | 03, 13 | sample input in README |

How to start one: copy `_template/` into the project folder is already done — just
open the README, write `DESIGN.md` *before* coding (a paragraph is enough), write the
first test, then code. Run `attack.py` only once the basic version works; then fix
whatever it breaks and write down what happened in the decision log.

The attack scripts assume the interface contract in each README. They skip cleanly
if the project isn't implemented yet, so you can run `make attack` any time.
