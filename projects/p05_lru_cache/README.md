# P5 — Thread-safe LRU cache (Stages 03, 09)

## Interface contract (what `attack.py` calls)
```python
from lru import LRUCache            # projects/p05_lru_cache/lru.py
c = LRUCache(capacity=2)
c.put("a", 1); c.get("a") -> 1; c.get("missing") -> None
len(c) -> number of items
```
Three versions, in order: `OrderedDict` → from scratch (hash map + doubly linked list,
O(1) get/put/evict, complexity in comments) → thread-safe. `capacity=0` must be handled
(decide: raise, or a cache that stores nothing) and documented. Optional: TTL.

## Attack
```bash
python projects/p05_lru_cache/attack.py
```
Correctness, eviction order, capacity 0, duplicates, and a 50-thread stress test that
would corrupt an unlocked implementation.
