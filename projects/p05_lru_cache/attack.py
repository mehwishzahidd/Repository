"""Attacks the LRU cache. Run: python projects/p05_lru_cache/attack.py"""
import os, random, sys, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        from lru import LRUCache
    except ImportError:
        print("⬜ lru.py not found yet — implement LRUCache first."); return
    checks = []
    c = LRUCache(capacity=2)
    c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
    checks.append(("evicts least-recently-USED (b), not least-recently-inserted",
                   c.get("b") is None and c.get("a") == 1 and c.get("c") == 3))
    c.put("a", 10)
    checks.append(("put on existing key updates value and size stays", c.get("a") == 10 and len(c) == 2))
    checks.append(("get on missing key returns None", c.get("zzz") is None))
    try:
        z = LRUCache(capacity=0); z.put("k", 1); ok0 = z.get("k") is None and len(z) == 0
    except ValueError:
        ok0 = True
    checks.append(("capacity=0 handled deliberately (stores nothing or raises ValueError)", ok0))

    # stress: N threads hammer a small cache; invariants must hold throughout
    c = LRUCache(capacity=50); errors = []; stop = threading.Event()
    def worker(seed):
        rnd = random.Random(seed)
        try:
            for _ in range(20000):
                k = rnd.randrange(200)
                if rnd.random() < 0.5: c.put(k, k)
                else:
                    v = c.get(k)
                    if v is not None and v != k: errors.append(f"corrupt value {k}->{v}")
                if len(c) > 50: errors.append(f"size exceeded capacity: {len(c)}")
        except Exception as e:
            errors.append(repr(e))
    ts = [threading.Thread(target=worker, args=(i,)) for i in range(50)]
    [t.start() for t in ts]; [t.join() for t in ts]
    checks.append(("50-thread stress: no exceptions, no corrupt values, size never > capacity", not errors))
    if errors: print("   first errors:", errors[:3])

    ok = 0
    for name, passed in checks:
        print(("✅" if passed else "❌"), name); ok += bool(passed)
    print(f"\n{ok}/{len(checks)} passed")


if __name__ == "__main__":
    main()
