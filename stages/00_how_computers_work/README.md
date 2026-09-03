# Stage 00 — How computers and programs work (the on-ramp)

> **Before Stage 01.** Two to three weeks, optional if you already know what a file, a
> program and a server are — mandatory if words like "CPU", "terminal" or "server" are
> fuzzy. Goal: understand what a program *is* before writing one.

## What you learn

1. **What a computer does** — CPU (does arithmetic and follows instructions), memory
   (RAM: fast, forgets when off), storage (disk: slow, remembers), input/output.
2. **What a program is** — a list of instructions the CPU executes in order; the idea of
   binary, bits and bytes (just the idea, no math).
3. **Languages and tools** — what a programming language is, compiler vs interpreter
   (Python is interpreted), what the **terminal** is and why programmers use it, the
   **file system** (folders, paths, extensions).
4. **The internet at cartoon level** — client, server, request, response; what a URL is;
   what "the cloud" means (someone else's computer).
5. **What a "variable" is going to be** — a named box for a value. That's the first idea
   in Stage 01.

## 📚 Resources
- ⭐ **CS50x** (Harvard, free on edX/YouTube) 🆓 — Week 0 (Scratch) and Week 1 (C). Don't
  worry about C long-term; it teaches what programs *are*.
- ⭐ **Crash Course Computer Science** (YouTube, PBS) 🆓 — episodes 1–20. Painless overview
  of how hardware runs software.
- **But How Do It Know?** (J. Clark Scott) 💰 — optional, if you want the "how does a CPU
  actually work" itch scratched now (Nand2Tetris in Stage 21 does it properly later).
- **Code** (Charles Petzold) 💰 — the same story told beautifully; also optional.
- **How the Internet Works** — Cloudflare Learning Center 🆓 or the *"How does the
  internet work?"* MDN page 🆓.

## Practice
- Open a terminal; make a folder, make a file in it, list it, delete it. Find the same
  folder in your file browser.
- Draw, on paper, what happens when you type a URL and press Enter (client → DNS →
  server → response → browser draws it). Keep the drawing; you'll redraw it in Stage 07
  with ten more boxes.
- Install Python and VS Code (`LEARNING_GUIDE.md` §8) and run one line: `print("hi")`.

## ✅ Checkpoint
- [ ] You can explain to a friend what a CPU, memory and storage each do.
- [ ] You can explain what a program is and the difference between a compiler and an
      interpreter, roughly.
- [ ] You can explain what happens when you type a URL and press Enter, at cartoon level.
- [ ] You've used the terminal to create and delete a file, and run one line of Python.

> Done? Go to [`../01_python/`](../01_python/). Update [`PROGRESS.md`](../../PROGRESS.md).
