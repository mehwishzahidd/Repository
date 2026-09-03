# P4 — DAG task scheduler (Stages 03, 09–10)

## Interface contract (what `attack.py` calls)
```python
from scheduler import Scheduler, CycleError   # projects/p04_dag_scheduler/scheduler.py
s = Scheduler(workers=4)
s.add_task("a", fn, priority=5, depends_on=["b", "c"])   # fn() runs when deps complete
s.cancel("b")          # cascades: everything depending on b is cancelled too
s.run()                # blocks until all tasks are done/failed/cancelled
s.status("a")          # "pending" | "running" | "done" | "failed" | "cancelled"
```
Adding a dependency that creates a cycle raises `CycleError` immediately.
Higher priority runs first among runnable tasks. A task whose `fn` raises is
"failed" and its dependants are cancelled.

## Attack
```bash
python projects/p04_dag_scheduler/attack.py
```
