"""
LESSON 7 — The standard library tour
====================================

Python ships with a toolbox. Knowing it means you don't reinvent things badly
under interview pressure. These are the modules you'll reach for constantly.

Run me:
    python3 stages/02_programming/07_standard_library.py
"""
import bisect
import heapq
import itertools
import logging
import random
from collections import Counter, OrderedDict, defaultdict, deque
from datetime import datetime, timedelta
from enum import Enum

# -------------------------------------------------------------------------
# collections.Counter — the counting pattern from lesson 1, built in.
# -------------------------------------------------------------------------
words = "the cat and the hat and the bat".split()
c = Counter(words)
print(c)                        # Counter({'the': 3, 'and': 2, ...})
print(c.most_common(2))         # [('the', 3), ('and', 2)]

# defaultdict — the grouping pattern, without setdefault.
by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)
print(dict(by_len))             # {3: ['the', 'cat', 'and', ...]}

# deque — a double-ended queue: O(1) append/pop at BOTH ends. This is your BFS queue.
q = deque([1, 2, 3])
q.append(4)                     # add to the right
q.appendleft(0)                 # add to the left
print(q.popleft(), q.pop(), q)  # 0 4 deque([1, 2, 3])

# OrderedDict — remembers insertion order AND can move keys. LRU cache, v1.
od = OrderedDict()
od["a"] = 1; od["b"] = 2; od["c"] = 3
od.move_to_end("a")             # "a" was just used → move to the end (most recent)
od.popitem(last=False)          # evict the least recently used ("b")
print(list(od))                 # ['c', 'a']

# -------------------------------------------------------------------------
# heapq — a min-heap on a plain list. Always gives you the smallest. Schedulers,
# "top k", Dijkstra. Push (priority, item) tuples.
# -------------------------------------------------------------------------
tasks = []
heapq.heappush(tasks, (2, "write tests"))
heapq.heappush(tasks, (1, "fix prod"))
heapq.heappush(tasks, (3, "refactor"))
print(heapq.heappop(tasks))     # (1, 'fix prod') — lowest number first
print(heapq.nsmallest(2, [9, 1, 8, 2, 7]))   # [1, 2]

# bisect — binary search on a sorted list, O(log n).
sorted_nums = [1, 3, 5, 7, 9]
print(bisect.bisect_left(sorted_nums, 6))    # 3 = where 6 would go
bisect.insort(sorted_nums, 6)                 # insert keeping it sorted
print(sorted_nums)

# -------------------------------------------------------------------------
# itertools — loops you'd otherwise write by hand.
# -------------------------------------------------------------------------
print(list(itertools.combinations("abc", 2)))          # [('a','b'), ('a','c'), ('b','c')]
print(list(itertools.permutations([1, 2, 3], 2))[:3])  # first 3 of the 6
print(list(itertools.chain([1, 2], [3])))              # [1, 2, 3]
for key, group in itertools.groupby("aaabbc"):          # consecutive runs
    print(key, len(list(group)), end="; ")
print()

# -------------------------------------------------------------------------
# datetime — never do date math by hand.
# -------------------------------------------------------------------------
now = datetime(2026, 1, 15, 9, 30)
print(now + timedelta(days=10))              # 2026-01-25 09:30:00
print(now.strftime("%Y-%m-%d"))              # 2026-01-15
print(datetime.strptime("2026-03-01", "%Y-%m-%d").month)   # 3

# -------------------------------------------------------------------------
# random — seeded so results are reproducible in tests.
# -------------------------------------------------------------------------
random.seed(42)
print(random.randint(1, 6), random.choice(["a", "b", "c"]))
deck = list(range(5)); random.shuffle(deck); print(deck)

# -------------------------------------------------------------------------
# enum — named constants instead of magic strings.
# -------------------------------------------------------------------------
class Status(Enum):
    PENDING = "pending"
    DONE = "done"
print(Status.DONE, Status("pending") is Status.PENDING)   # Status.DONE True

# -------------------------------------------------------------------------
# logging — instead of print() in real programs: levels, timestamps, on/off.
# -------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)
log.info("service started")
log.warning("disk at 91%%")
log.debug("this is hidden because level is INFO")

# TRY: using heapq, write `top_k(words, k)` returning the k most frequent words.
# Then do it again with Counter.most_common and compare.
