"""
LESSON 5 — Comprehensions, iterators and generators
===================================================

Comprehensions build lists/dicts/sets in one readable line. Generators produce
values one at a time, on demand, so you can process a million lines without
holding them all in memory. Token streaming in Stage 17 is a generator.

Run me:
    python3 stages/02_programming/05_comprehensions_and_generators.py
"""

# -------------------------------------------------------------------------
# LIST comprehension: [expression for item in iterable if condition]
# -------------------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6]
squares = [n * n for n in nums]                 # [1, 4, 9, 16, 25, 36]
evens = [n for n in nums if n % 2 == 0]         # [2, 4, 6]
print(squares, evens)

# The same thing as a loop — comprehensions are just shorter, not magic:
squares_loop = []
for n in nums:
    squares_loop.append(n * n)
print(squares == squares_loop)                  # True

# -------------------------------------------------------------------------
# DICT and SET comprehensions
# -------------------------------------------------------------------------
lengths = {word: len(word) for word in ["hi", "hello", "hey"]}   # {'hi': 2, ...}
first_letters = {word[0] for word in ["apple", "avocado", "banana"]}   # {'a', 'b'}
print(lengths, first_letters)

# Nested: flatten a list of lists
grid = [[1, 2], [3, 4], [5]]
flat = [x for row in grid for x in row]         # [1, 2, 3, 4, 5]
print(flat)

# -------------------------------------------------------------------------
# ITERATORS: anything you can loop over. `iter()` gets one; `next()` advances it.
# -------------------------------------------------------------------------
it = iter([10, 20, 30])
print(next(it), next(it), next(it))             # 10 20 30
try:
    next(it)
except StopIteration:
    print("exhausted")                          # a for-loop catches this for you

# -------------------------------------------------------------------------
# GENERATORS: a function with `yield` instead of `return`. Calling it does NOT
# run it — it returns a generator object that runs lazily, pausing at each yield.
# -------------------------------------------------------------------------
def countdown(n):
    print("  (starting)")
    while n > 0:
        yield n            # hand out a value, then PAUSE here until asked for the next
        n -= 1
    print("  (done)")

gen = countdown(3)
print("created, nothing ran yet")
for value in gen:
    print("got", value)

# -------------------------------------------------------------------------
# WHY: memory. This "list" of a billion numbers would need gigabytes as a list.
# As a generator it needs one number at a time.
# -------------------------------------------------------------------------
def numbers_up_to(limit):
    i = 0
    while i < limit:
        yield i
        i += 1

total = 0
for n in numbers_up_to(1_000_000):     # one million values, almost no memory
    total += n
print(total)                            # 499999500000

# The same as a GENERATOR EXPRESSION (like a comprehension, with parentheses):
print(sum(n * n for n in range(1000)))  # no list is ever built

# -------------------------------------------------------------------------
# A REAL pattern: stream lines from a big file, filter them, never load it all.
# -------------------------------------------------------------------------
def error_lines(lines):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()

fake_log = ["INFO ok\n", "ERROR disk full\n", "INFO ok\n", "ERROR timeout\n"]
print(list(error_lines(fake_log)))      # ['ERROR disk full', 'ERROR timeout']

# -------------------------------------------------------------------------
# A token stream, the way an LLM API sends words: one at a time, as ready.
# -------------------------------------------------------------------------
def stream_tokens(text):
    for word in text.split():
        yield word + " "

for tok in stream_tokens("this arrives one word at a time"):
    print(tok, end="", flush=True)
print()

# TRY: write `chunks(items, size)` — a generator that yields lists of `size`
# items at a time from `items`. chunks([1,2,3,4,5], 2) -> [1,2], [3,4], [5]
