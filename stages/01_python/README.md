# Stage 01 — Python basics

> **Roadmap Group 1.** This is where the whole journey begins. Literally here.

## If you've never programmed before

Programming is writing very precise instructions that a computer follows exactly. Python
is the friendliest language to learn that in: it reads almost like English, and it's the
language used for most of this road, for data structures practice, for backend services,
and for the machine-learning world you're heading towards.

By the end of this stage you'll be able to write small programs that store values, make
decisions, repeat work, and package logic into functions. That's genuinely most of what
programming *is*; everything after is building on those four ideas.

**Time:** 3–5 weeks at ~10 hours/week. Don't rush it; everything else stands on this.

**Prerequisites:** none. Set up the tools in `LEARNING_GUIDE.md` §8 first (Python 3,
VS Code, git).

---

## The runnable lessons in this folder (⭐ start here)

Work through these files **in order**. For each one:

1. **Read** the file — every line is explained in comments.
2. **Run** it and read the output:
   ```bash
   python3 stages/01_python/01_hello_world.py
   ```
3. **Experiment** — change a value, re-run, see what happens. Break it on purpose and
   read the error message.

| # | File | You'll learn |
|---|------|--------------|
| 1 | `01_hello_world.py` | Running Python, `print`, comments |
| 2 | `02_variables_and_types.py` | Variables and the 4 basic types |
| 3 | `03_numbers_and_math.py` | Math operators, division types |
| 4 | `04_strings.py` | Working with text |
| 5 | `05_lists.py` | Ordered collections (huge for interviews) |
| 6 | `06_conditionals.py` | Making decisions with `if` |
| 7 | `07_loops.py` | Repeating work with loops |
| 8 | `08_functions.py` | Packaging code into reusable functions |

Then head to **`exercises/`** and put your new skills to work. There's an automatic
checker that tells you if your answers are correct:

```bash
python3 stages/01_python/exercises/check.py
```

---

## Modules (pair the lessons with a course so each idea is seen twice)

1. **Getting set up** — install Python, run a file from the terminal, use the REPL,
   read an error message. *(Lesson 1)*
2. **Values and variables** — ints, floats, strings, booleans; naming; `type()`;
   converting between types; `input()`. *(Lessons 2–3)*
3. **Strings** — indexing, slicing, methods (`.lower()`, `.split()`, `.strip()`),
   f-strings, immutability. *(Lesson 4)*
4. **Lists** — creating, indexing, slicing, `append`/`pop`/`insert`, `len`, `in`,
   sorting, iteration. Then tuples (immutable lists). *(Lesson 5)*
5. **Conditionals** — `if / elif / else`, comparison and boolean operators, truthiness,
   nesting. *(Lesson 6)*
6. **Loops** — `for` over a list/range/string, `while`, `break`/`continue`, nested
   loops, accumulating results. *(Lesson 7)*
7. **Functions** — `def`, parameters, `return`, default arguments, scope, docstrings,
   why functions exist (reuse, naming, testing). *(Lesson 8)*
8. **Dictionaries and sets** — key → value lookup, iteration over keys/values/items,
   counting things, `in`, sets for uniqueness. *(Not a lesson file yet; do it from the
   course below — it's the most important structure in all of programming.)*
9. **Putting it together** — a 50–100 line program from a blank file: read input,
   store it, loop, decide, print. This is Project 1's first step.

---

## 📚 Resources

### Courses & videos
- ⭐ **Python for Everybody** (py4e.org, Dr. Charles Severance) 🆓 — the best true-beginner
  course there is. Free videos, book, and auto-graded exercises. Chapters 1–10 match this
  stage exactly. (Also on Coursera, free to audit.)
- ⭐ **CS50's Introduction to Programming with Python** (Harvard, edx.org / YouTube) 🆓 —
  the best-taught beginner course, with problem sets. Do weeks 0–5 here; the rest in Stage 02.
- **freeCodeCamp "Python for Beginners" full course** (YouTube, ~4 h) 🆓 — if you want a
  single video walk-through.
- **Corey Schafer's Python Tutorials** (YouTube) 🆓 — short, clear videos on each topic;
  great as a second explanation when something doesn't click.

### Books
- ⭐ **Automate the Boring Stuff with Python** (Al Sweigart) 🆓 online at
  automatetheboringstuff.com — chapters 1–7 for this stage; it's practical and fun.
- **Python Crash Course** (Eric Matthes) 💰 — part 1 is an excellent structured
  beginner path with exercises. Pick this *or* Automate; you don't need both.
- **Think Python** (Allen Downey) 🆓 online — more "computer-science-y"; good if you like
  understanding *why*.

### Practice
- ⭐ **This folder's `exercises/`** — auto-graded, do them all.
- **Exercism Python track** (exercism.org) 🆓 — small problems with free human mentoring.
  Do the first 15–20.
- **Codewars** 🆓 — 8 kyu and 7 kyu problems only for now.
- **futurecoder.io** 🆓 — interactive, in-browser, beginner-first.

### Reference
- **The official Python tutorial** (docs.python.org/3/tutorial) — sections 1–5. Learning
  to read this is a skill; start now.
- **Python Tutor** (pythontutor.com) 🆓 — visualises your code line by line. Use it
  whenever a loop or function confuses you.

---

## Practice & exercises (beyond the checker)

Write each of these from a blank file, without looking at the lessons:
- A temperature converter that asks for a value and a unit.
- A program that counts the vowels in a sentence.
- FizzBuzz (print 1–100; multiples of 3 → "Fizz", of 5 → "Buzz", both → "FizzBuzz").
- A number-guessing game with a `while` loop and hints ("higher"/"lower").
- A shopping list you can add to, remove from and print, in a loop, until the user quits.
- A function `is_palindrome(text)` and a function `word_count(text)` returning a dict.

## Beginner pitfalls
- **Indentation errors.** Python uses indentation to mean "inside". Use 4 spaces, always.
- **`=` vs `==`.** One assigns, two compares.
- **Off-by-one.** `range(5)` is 0–4. Lists start at index 0.
- **Changing a list while looping over it.** Make a copy or build a new list.
- **Not reading the error.** The last line of a traceback tells you what went wrong and
  the line above it tells you where. Read both.

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Every lesson runs, you've modified each one, and `check.py` reports all green.
- [ ] You can write FizzBuzz, a guessing game and a word counter from a blank file with
      no reference.
- [ ] You can explain, in plain words, what a variable, a list, a dictionary, a loop
      and a function are.
- [ ] You read an error message, find the line, and fix it without help.
- [ ] You've committed to git at least ten times.

## 🛠️ Project
**P1 — Python programs** (see `PROJECTS.md`): start with the number-guessing game and the
word-frequency counter. The rest of P1 comes in Stage 02.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 02"** to get its hands-on lessons built.
