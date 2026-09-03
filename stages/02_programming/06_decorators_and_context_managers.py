"""
LESSON 6 — Functions as values, decorators, context managers
============================================================

In Python a function is a value: you can store it, pass it, return it. A
DECORATOR is a function that wraps another to add behaviour (timing, logging,
caching, retries). A CONTEXT MANAGER is the thing behind `with`: setup, then
guaranteed cleanup. Locks in Stage 09 are used exactly this way.

Run me:
    python3 stages/02_programming/06_decorators_and_context_managers.py
"""
import functools
import time
from contextlib import contextmanager

# -------------------------------------------------------------------------
# FUNCTIONS ARE VALUES
# -------------------------------------------------------------------------
def shout(text):
    return text.upper() + "!"

say = shout                  # no parentheses: we're handing over the function itself
print(say("hi"))             # HI!

def apply_twice(func, value):
    return func(func(value))
print(apply_twice(shout, "hey"))          # HEY!!

# lambda: a tiny anonymous function, handy as a sort key
people = [("ana", 31), ("ben", 25)]
print(sorted(people, key=lambda p: p[1]))   # sort by age

# -------------------------------------------------------------------------
# CLOSURES: an inner function remembers variables from where it was made.
# -------------------------------------------------------------------------
def make_multiplier(k):
    def multiply(x):
        return x * k          # `k` is remembered
    return multiply

triple = make_multiplier(3)
print(triple(10))             # 30

# -------------------------------------------------------------------------
# A DECORATOR: takes a function, returns a new function that wraps it.
# -------------------------------------------------------------------------
def timer(func):
    @functools.wraps(func)            # keeps the original name/docstring
    def wrapper(*args, **kwargs):     # accept anything, pass it through
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed*1000:.2f} ms")
        return result
    return wrapper

@timer                                # same as: slow_sum = timer(slow_sum)
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))

# -------------------------------------------------------------------------
# A decorator WITH arguments: a retry decorator (you'll use this idea in Stage 10).
# -------------------------------------------------------------------------
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  attempt {attempt} failed: {e}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator

calls = {"n": 0}
@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("network blip")
    return "success"

print(flaky())

# -------------------------------------------------------------------------
# functools.lru_cache: memoisation in one line. Huge for recursion (Stage 03).
# -------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(80))                # instant; without the cache this would take forever

# -------------------------------------------------------------------------
# CONTEXT MANAGERS: `with` calls __enter__ at the start and __exit__ at the end,
# even if the block raises. Files, locks, DB transactions all work this way.
# -------------------------------------------------------------------------
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self                        # becomes the `as t` value
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"  block took {self.elapsed*1000:.2f} ms")
        return False                       # False = don't swallow exceptions

with Timer() as t:
    sum(range(500_000))

# The shortcut: a generator function + @contextmanager. Code before `yield` is
# setup; code after is cleanup (put it in `finally` so it always runs).
@contextmanager
def opened_resource(name):
    print(f"  open {name}")
    try:
        yield name
    finally:
        print(f"  close {name}")

with opened_resource("db-connection") as r:
    print(f"  using {r}")

# TRY: write a `@log_calls` decorator that prints the function name and its
# arguments every time it's called, then apply it to `shout`.
