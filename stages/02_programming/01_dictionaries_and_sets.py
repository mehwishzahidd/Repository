"""
LESSON 1 — Dictionaries and sets, properly
==========================================

A DICTIONARY maps keys to values. It is the single most important data structure
in programming: caches, indexes, graphs, counters and JSON are all dictionaries
underneath. A SET is a bag of unique values with instant "is it in there?" checks.

Run me:
    python3 stages/02_programming/01_dictionaries_and_sets.py
"""

# -------------------------------------------------------------------------
# CREATING and READING. Keys are usually strings or numbers; values can be anything.
# -------------------------------------------------------------------------
ages = {"ana": 31, "ben": 25, "chloe": 40}
print(ages["ana"])            # 31  — look up by key. Fast: O(1) no matter the size.

# Reading a missing key with [] crashes (KeyError). Use .get() when unsure:
print(ages.get("zed"))        # None
print(ages.get("zed", 0))     # 0  — a default value instead of None

# -------------------------------------------------------------------------
# WRITING, UPDATING, DELETING
# -------------------------------------------------------------------------
ages["dan"] = 19              # add a new key
ages["ana"] = 32              # overwrite an existing key
del ages["ben"]               # remove a key
print(ages)                   # {'ana': 32, 'chloe': 40, 'dan': 19}
print("dan" in ages)          # True — `in` checks KEYS, and it's O(1)
print(len(ages))              # 3

# -------------------------------------------------------------------------
# LOOPING. Three ways. .items() is the one you'll use most.
# -------------------------------------------------------------------------
for name in ages:                     # keys
    print(name, end=" ")
print()
for name, age in ages.items():        # keys and values together
    print(f"{name} is {age}")

# -------------------------------------------------------------------------
# THE COUNTING PATTERN. You'll write this a hundred times in interviews.
# -------------------------------------------------------------------------
words = "the cat and the hat and the bat".split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1   # "current count (or 0) plus one"
print(counts)                          # {'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1}

# -------------------------------------------------------------------------
# THE GROUPING PATTERN. Values can be lists; append into them.
# -------------------------------------------------------------------------
people = [("ana", "eng"), ("ben", "ops"), ("chloe", "eng")]
by_team = {}
for name, team in people:
    by_team.setdefault(team, []).append(name)   # create the list if missing, then append
print(by_team)                                  # {'eng': ['ana', 'chloe'], 'ops': ['ben']}

# -------------------------------------------------------------------------
# NESTED dictionaries — this is what JSON looks like (lesson 3).
# -------------------------------------------------------------------------
user = {"name": "ana", "address": {"city": "Lahore", "zip": "54000"}, "tags": ["admin"]}
print(user["address"]["city"])   # Lahore
print(user["tags"][0])           # admin

# -------------------------------------------------------------------------
# SETS — unique values, instant membership, and set math.
# -------------------------------------------------------------------------
seen = set()
for w in words:
    seen.add(w)
print(seen)                       # unique words (order is not guaranteed)
print("cat" in seen)              # True — O(1)
print(len(set([1, 1, 2, 3, 3])))  # 3 — the classic "how many unique?" trick

a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a & b)   # {3, 4}        intersection: in both
print(a | b)   # {1,2,3,4,5}   union: in either
print(a - b)   # {1, 2}        difference: in a but not b

# -------------------------------------------------------------------------
# WHY THIS MATTERS: "have I seen this before?" with a list is O(n) per check.
# With a set or dict it's O(1). That difference is the whole reason hash maps
# exist, and it's the first thing interviewers look for.
# -------------------------------------------------------------------------
# TRY: change `words` to a sentence of your own and watch `counts` update.
