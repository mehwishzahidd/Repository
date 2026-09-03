"""
Stage 02 — EXERCISES
====================

Fill in each function. Replace `pass` with your code. Check any time with:
    python3 stages/02_programming/exercises/check.py

Each exercise maps to a lesson. Read the docstring, decide the edge cases
FIRST (empty? missing? duplicate?), then write the code.
"""
import re
from dataclasses import dataclass, field


# -------------------------------------------------------------------------
# EXERCISE 1 — word_counts  (lesson 1: dictionaries)
# Return a dict mapping each lowercase word to how many times it appears.
# Words are separated by whitespace. word_counts("a b a") -> {"a": 2, "b": 1}
# word_counts("") -> {}
# -------------------------------------------------------------------------
def word_counts(text):
    pass


# -------------------------------------------------------------------------
# EXERCISE 2 — group_by_first_letter  (lesson 1: grouping pattern)
# Return a dict mapping the first letter to a list of the words starting with it,
# keeping the words in their original order.
# group_by_first_letter(["apple", "bob", "avocado"]) -> {"a": ["apple", "avocado"], "b": ["bob"]}
# -------------------------------------------------------------------------
def group_by_first_letter(words):
    pass


# -------------------------------------------------------------------------
# EXERCISE 3 — parse_age  (lesson 2: exceptions)
# Convert text to an int age. Raise ValueError if it isn't a whole number or is
# outside 0..150 inclusive. Surrounding spaces are allowed: " 42 " -> 42.
# -------------------------------------------------------------------------
def parse_age(text):
    pass


# -------------------------------------------------------------------------
# EXERCISE 4 — safe_load_json  (lesson 3: files/JSON)
# Given a Path to a JSON file, return the parsed object. If the file does not
# exist, return the `default` argument instead of crashing.
# (Use json.load inside a `with open(...)` and catch FileNotFoundError.)
# -------------------------------------------------------------------------
def safe_load_json(path, default=None):
    pass


# -------------------------------------------------------------------------
# EXERCISE 5 — Stack  (lesson 4: classes)
# A class with push(item), pop() -> item, peek() -> item, and __len__.
# pop()/peek() on an empty stack must raise IndexError.
# -------------------------------------------------------------------------
class Stack:
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def __len__(self):
        pass


# -------------------------------------------------------------------------
# EXERCISE 6 — chunks  (lesson 5: generators)
# A GENERATOR that yields lists of `size` items at a time from `items`.
# list(chunks([1,2,3,4,5], 2)) -> [[1,2],[3,4],[5]]      list(chunks([], 3)) -> []
# Raise ValueError if size < 1.
# -------------------------------------------------------------------------
def chunks(items, size):
    pass


# -------------------------------------------------------------------------
# EXERCISE 7 — count_calls  (lesson 6: decorators)
# A decorator that counts how many times the wrapped function has been called
# and stores it on the wrapper as `.calls`. Must return the function's result.
#     @count_calls
#     def f(x): return x * 2
#     f(1); f(2); f.calls -> 2
# Hint: define wrapper, set wrapper.calls = 0 before returning it.
# -------------------------------------------------------------------------
def count_calls(func):
    pass


# -------------------------------------------------------------------------
# EXERCISE 8 — top_k  (lesson 7: Counter / heapq)
# Return the k most frequent words as a list of (word, count), most frequent
# first; ties broken alphabetically. top_k(["b","a","b","a","c"], 2) -> [("a",2),("b",2)]
# -------------------------------------------------------------------------
def top_k(words, k):
    pass


# -------------------------------------------------------------------------
# EXERCISE 9 — extract_links  (lesson 8: regex)
# Return every href value from an HTML string, in order. Only double-quoted
# href="..." attributes count.  extract_links('<a href="/a">x</a>') -> ["/a"]
# -------------------------------------------------------------------------
def extract_links(html):
    pass


# -------------------------------------------------------------------------
# EXERCISE 10 — parse_log_line  (lesson 8: regex groups)
# Lines look like: "2026-01-15 09:30:12 ERROR db: connection timed out"
# Return a dict with keys "date", "time", "level", "component", "message".
# Return None if the line doesn't match that shape.
# -------------------------------------------------------------------------
def parse_log_line(line):
    pass


# -------------------------------------------------------------------------
# EXERCISE 11 — Contact / ContactBook  (lessons 4 & 9: dataclass + composition)
# Contact is a dataclass with name (str), email (str), tags (list, default empty).
# ContactBook: add(contact) raises ValueError on a duplicate email; find(email)
# returns the Contact or None; with_tag(tag) returns a list of contacts having it.
# -------------------------------------------------------------------------
@dataclass
class Contact:
    name: str
    email: str
    tags: list = field(default_factory=list)


class ContactBook:
    def __init__(self):
        pass

    def add(self, contact):
        pass

    def find(self, email):
        pass

    def with_tag(self, tag):
        pass


# -------------------------------------------------------------------------
# EXERCISE 12 — lru_v1  (lesson 7: OrderedDict) — a first taste of the LRU cache
# Return a class instance? No — simpler: implement the two functions on a plain
# OrderedDict. `lru_get(cache, key)` returns the value (moving key to most-recent)
# or None. `lru_put(cache, key, value, capacity)` inserts/updates and evicts the
# least-recently-used key if the cache exceeds capacity.
# -------------------------------------------------------------------------
def lru_get(cache, key):
    pass


def lru_put(cache, key, value, capacity):
    pass
