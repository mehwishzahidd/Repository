"""Attacks the DAG scheduler. Run: python projects/p04_dag_scheduler/attack.py"""
import os, sys, threading, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        from scheduler import Scheduler, CycleError
    except ImportError:
        print("⬜ scheduler.py not found yet — implement Scheduler first."); return
    results = []
    checks = []

    # 1. ordering + parallelism
    s = Scheduler(workers=4); order = []; lock = threading.Lock()
    def mk(name, dur=0.05):
        def fn():
            time.sleep(dur)
            with lock: order.append(name)
        return fn
    s.add_task("c", mk("c")); s.add_task("b", mk("b"), depends_on=["c"])
    s.add_task("a", mk("a"), depends_on=["b"])
    for i in range(8): s.add_task(f"p{i}", mk(f"p{i}", 0.2))
    t0 = time.perf_counter(); s.run(); dt = time.perf_counter() - t0
    checks.append(("dependencies respected (c before b before a)",
                   order.index("c") < order.index("b") < order.index("a")))
    checks.append(("independent tasks ran in parallel (8×0.2s on 4 workers < 1.0s)", dt < 1.0))

    # 2. cycle detection
    s = Scheduler(workers=2)
    s.add_task("x", mk("x"), depends_on=["y"]); s.add_task("y", mk("y"), depends_on=["z"])
    try:
        s.add_task("z", mk("z"), depends_on=["x"]); cyc = False
    except CycleError:
        cyc = True
    checks.append(("cycle x→y→z→x rejected with CycleError", cyc))

    # 3. cascading cancellation on failure
    s = Scheduler(workers=2)
    def boom(): raise RuntimeError("boom")
    s.add_task("root", boom); s.add_task("child", mk("child"), depends_on=["root"])
    s.add_task("grandchild", mk("gc"), depends_on=["child"]); s.add_task("other", mk("other"))
    s.run()
    checks.append(("failed task marked failed", s.status("root") == "failed"))
    checks.append(("dependants cancelled (cascade)", s.status("child") == "cancelled"
                   and s.status("grandchild") == "cancelled"))
    checks.append(("unrelated task still done", s.status("other") == "done"))

    # 4. explicit cancel cascades
    s = Scheduler(workers=2); ran = []
    s.add_task("b", mk("b")); s.add_task("a", lambda: ran.append("a"), depends_on=["b"])
    s.cancel("b"); s.run()
    checks.append(("cancel(b) cascades to a; a never ran", s.status("a") == "cancelled" and not ran))

    # 5. priority: premium behind 500 batch tasks
    s = Scheduler(workers=1); seq = []
    for i in range(500): s.add_task(f"batch{i}", (lambda i=i: seq.append("batch")), priority=1)
    s.add_task("premium", lambda: seq.append("premium"), priority=100)
    s.run()
    checks.append(("premium ran before the 500 batch tasks", seq and seq[0] == "premium"))

    ok = 0
    for name, passed in checks:
        print(("✅" if passed else "❌"), name); ok += bool(passed)
    print(f"\n{ok}/{len(checks)} passed")


if __name__ == "__main__":
    main()
