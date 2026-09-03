# Stage 02 — Programming: classes, files, the standard library, stronger Python

> **Roadmap Groups 1 & 3.** Stage 01 taught you the atoms. This stage makes Python
> *yours*, and starts the production-quality habits that separate "it runs" from
> "it's good".

## If you're new to this

Once you can write loops and functions, the next jump is organising bigger programs:
grouping data and behaviour into **classes**, saving things to **files**, handling
**errors** gracefully instead of crashing, and using Python's built-in toolbox (the
**standard library**) instead of reinventing everything. You'll also learn to write
**tests** — small programs that check your program — which every later stage relies on.

**Time:** 5–7 weeks at ~10 hours/week.

**Prerequisites:** Stage 01 checkpoint ticked.

---

## Modules (in order)

1. **Dictionaries and sets, properly** — nested dicts, `.get()`, `.items()`, counting,
   grouping, sets for membership and dedupe. *This is the most important structure you'll
   ever learn; the LRU cache, caches, indexes and graphs are all built on it.*
2. **Errors and exceptions** — `try / except / else / finally`, raising your own,
   custom exception classes, why "fail loudly" beats silent bugs.
3. **Files and data formats** — reading/writing text files, `with` blocks, `pathlib`,
   CSV, **JSON** (the format every API speaks), command-line arguments (`argparse`).
4. **Modules and packages** — splitting a program into files, `import`, `if __name__ ==
   "__main__"`, virtual environments (`venv`), installing packages with `pip`,
   `requirements.txt`.
5. **Classes and objects** — `class`, `__init__`, `self`, methods, attributes;
   `__repr__`, `__eq__`, `__lt__`; inheritance vs **composition** (prefer composition);
   `@dataclass`; `@property`; class vs instance attributes.
6. **Iterators, generators, comprehensions** — list/dict/set comprehensions, `yield`,
   generator expressions, why generators save memory (you'll stream tokens with them
   in Stage 17), `iter()`/`next()`.
7. **Functions, deeper** — `*args`/`**kwargs`, first-class functions, `lambda`,
   closures, **decorators**, `functools` (`lru_cache`, `partial`, `wraps`).
8. **Context managers** — `with`, writing your own with `__enter__/__exit__` and
   `contextlib`. (Locks in Stage 09 are used this way.)
9. **The standard library tour** — `collections` (`Counter`, `deque`, `defaultdict`,
   `OrderedDict`), `heapq`, `bisect`, `itertools`, `datetime`, `random`, `math`, `re`
   (regular expressions), `logging`, `time`, `os`/`sys`, `enum`, `typing`.
10. **Type hints** — annotating functions and dataclasses, `Optional`, `list[int]`,
    running `mypy`/`pyright`. Interviewers read them as a sign of care.
11. **Testing with pytest** — writing `test_*.py`, `assert`, arrange/act/assert,
    parametrized tests, fixtures, testing exceptions, running with `-k` and `-x`.
    Write tests for everything from now on.
12. **Production habits (Group 3)** — naming, small functions, one job per function,
    validating inputs, handling edge cases (*empty? zero? duplicate? huge?*), docstrings,
    `black` + `ruff` for formatting/linting, reading your own code as if someone else
    wrote it.
13. **Performance basics** — timing with `timeit`, why lists are slow for membership
    and sets are fast, `cProfile` as a first taste of profiling (Stage 13 goes deep).

---

## 📚 Resources

### Courses & videos
- ⭐ **CS50P** weeks 6–9 (files, exceptions, unit tests, regular expressions, OOP) 🆓 —
  continues straight from Stage 01.
- ⭐ **Python for Everybody** chapters 11–16 🆓 — regex, networking-lite, files, OOP.
- **Corey Schafer: OOP series, generators, decorators, context managers, `unittest`/
  `pytest`** (YouTube) 🆓 — the best short explanations on the internet.
- **ArjanCodes** (YouTube) 🆓 — software-design habits in Python: when to use classes,
  dataclasses, dependency injection. Watch after the OOP module.
- **Talk Python: Python for Absolute Beginners / Python Language Jumpstart** 💰 — polished,
  if you prefer a paid guided path.

### Books
- ⭐ **Automate the Boring Stuff** chapters 8–13 🆓 — files, regex, JSON/CSV, real tasks.
- ⭐ **Python Crash Course** part 1 chapters 9–11 (classes, files & exceptions, testing) 💰.
- **Python Tricks** (Dan Bader) 💰 — short, intermediate idioms; read after the modules.
- **Effective Python** (Brett Slatkin) 💰 — 90 specific ways to write better Python.
  Read the items on functions, classes, comprehensions and generators now; the rest later.
- **Fluent Python** (Luciano Ramalho) 💰 — the deep book. **Not yet**; return in Stage 09
  when you hit its concurrency chapters.
- **Python Testing with pytest** (Brian Okken) 💰 — the pytest book; chapters 1–5 now.

### Practice
- ⭐ **Exercism Python track** 🆓 — do 30+ more exercises; they're built around exactly
  these topics (classes, generators, errors).
- **Codewars** 🆓 — 7 kyu / 6 kyu.
- **Advent of Code** (adventofcode.com, any past year) 🆓 — days 1–10 are perfect for
  file parsing + dicts + loops, and genuinely fun.
- **`LEETCODE.md` Phase A** — 3–4 easies a week once the modules are done.

### Reference
- **Official docs:** the tutorial sections 6–12, the `collections` and `itertools`
  pages, the pytest "Get started" page.
- **Real Python** (realpython.com) 🆓/💰 — search any topic above; their articles are
  consistently excellent.
- **PEP 8** — the Python style guide. Skim once; let `black`/`ruff` enforce it.

---

## Practice & exercises
- Rewrite Stage 01's guessing game and shopping list with classes and file persistence.
- A `Bank` class with `Account` objects that raises a custom `InsufficientFunds` error.
- A CSV → JSON converter with `argparse` flags and error handling for bad rows.
- A generator that yields lines matching a regex from a large log file.
- A `@timer` decorator that logs how long any function takes.
- A `Counter`-based word-frequency tool that prints the top 10, with tests.
- An `LRU`-shaped warm-up: a class that remembers the last N items added (use `deque`).

## Beginner pitfalls
- **Mutable default arguments** (`def f(x=[])`) — the list is shared between calls.
- **Catching everything** (`except:`) — hides real bugs; catch specific exceptions.
- **Inheritance for everything.** Most of the time a class *has* a thing; it isn't one.
- **Skipping tests** because "it's a small script". Write one test. It's a habit.
- **Not using a virtual environment** — one per project, always.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You can write a 150–200 line program with classes, file I/O, JSON, error handling
      and `argparse` from a blank file.
- [ ] You can explain what a generator is, why it saves memory, and write one.
- [ ] You can write a decorator and a context manager and explain what each is for.
- [ ] You use `Counter`, `defaultdict`, `deque` and `heapq` without looking them up.
- [ ] Every program you've written this stage has pytest tests, including edge cases.
- [ ] `ruff` and `black` pass on your code, and it has type hints.

## 🛠️ Project
Finish **P1 — Python programs**: the to-do list saved to JSON, the contact book with a
`Contact` dataclass and a `ContactBook` class, all with tests. Commit it with a README.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 03"** to get its hands-on lessons built.
