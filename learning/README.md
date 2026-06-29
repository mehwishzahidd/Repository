# 🚀 Learn to Code — the complete roadmap

Your personal, hands-on curriculum to go from **complete beginner** to a strong
software engineer / competitive programmer / quant — covering **everything** you set out
to learn:

> **Python · C++ · Rust · Data Structures & Algorithms · Competitive Programming
> (Codeforces) · Math for Quant · Quant Trading · System Design · Git & GitHub**

---

## 👉 Before anything else, read [`HOW_TO_LEARN.md`](./HOW_TO_LEARN.md)

It explains the **order** to learn these in and why. Short version: **start with Python +
DSA + git** (the foundation for all the rest), and don't try to learn three languages at
once. Five minutes there will save you months.

---

## 🗺️ The tracks

Each track has its own folder with a full syllabus, recommended free resources, and
(as you reach it) hands-on lessons. They're numbered in the **recommended learning order**.

| # | Track | Folder | Status |
|---|-------|--------|--------|
| 1 | **Python** — the language, start to finish | [`01_python_basics/`](./01_python_basics/) | 🟢 Module 1 ready |
| 2 | **Data Structures & Algorithms** — heart of interviews | [`tracks/dsa/`](./tracks/dsa/) | 📋 Syllabus ready |
| 3 | **C++** — speed, competitive programming, quant | [`tracks/cpp/`](./tracks/cpp/) | 📋 Syllabus ready |
| 4 | **Competitive Programming** — Codeforces & friends | [`tracks/competitive_programming/`](./tracks/competitive_programming/) | 📋 Syllabus ready |
| 5 | **Rust** — modern systems programming | [`tracks/rust/`](./tracks/rust/) | 📋 Syllabus ready |
| 6 | **Math for Quant** — probability, stats, linear algebra | [`tracks/math_for_quant/`](./tracks/math_for_quant/) | 📋 Syllabus ready |
| 7 | **Quant Trading** — the interviews & the job | [`tracks/quant_trading/`](./tracks/quant_trading/) | 📋 Syllabus ready |
| 8 | **System Design** — scalable systems (advanced) | [`tracks/system_design/`](./tracks/system_design/) | 📋 Syllabus ready |
| ⭐ | **Git & GitHub** — used in *every* track | [`GIT_AND_GITHUB.md`](./GIT_AND_GITHUB.md) | 🟢 Guide ready |

> **Status key:** 🟢 lessons you can do now · 📋 full syllabus + resources mapped, lessons
> built when you reach the track. This keeps you from drowning in content you're not ready for.

---

## 🟢 Start here, today

You are at the very beginning of **Track 1 (Python)**. Do this now:

1. Read [`HOW_TO_LEARN.md`](./HOW_TO_LEARN.md) and [`GIT_AND_GITHUB.md`](./GIT_AND_GITHUB.md).
2. Run your first program:
   ```bash
   python3 learning/01_python_basics/01_hello_world.py
   ```
3. Work through Module 1's lessons in order, then the exercises:
   ```bash
   python3 learning/01_python_basics/exercises/check.py
   ```
4. Commit your progress with git after each session (see the git guide).

When Module 1's exercises all pass, tell me **"ready for the next module"** and I'll build it.

---

## 📈 The big-picture phases

This is the whole journey at a glance. You'll spend most of the early months in Phase 1–2.

- **Phase 1 — Foundation:** Python fundamentals + git. *(You are here.)*
- **Phase 2 — The core:** Data Structures & Algorithms + Big-O, practiced in Python.
- **Phase 3 — Sharpening:** C++ + Competitive Programming (Codeforces). Start timed practice.
- **Phase 4 — Breadth:** Rust, deeper Python, more advanced algorithms.
- **Phase 5 — Specialize:** Pick your dream — **Quant** (with the Math track) and/or
  **System Design** for senior-level interviews.

Each phase builds directly on the last. Follow the order, stay consistent, and you'll get
there. 💪

---

## How this repo is organized

```
learning/
├── README.md            ← you are here (the master map)
├── HOW_TO_LEARN.md      ← how to sequence it all (read first!)
├── GIT_AND_GITHUB.md    ← git guide (used in every track)
├── 01_python_basics/    ← Track 1, Module 1: runnable lessons + auto-graded exercises
└── tracks/              ← syllabus + resources for every other track
    ├── dsa/
    ├── cpp/
    ├── rust/
    ├── competitive_programming/
    ├── math_for_quant/
    ├── quant_trading/
    └── system_design/
```
