# 🧭 LEARNING GUIDE — how to actually learn this from zero

You have no skills yet. That is the correct starting point for this repo, and this page
is the operating manual. Read it once now and again whenever you feel stuck or lost.

---

## 1. The rules that matter more than any resource

1. **One stage at a time.** Do not open Stage 09 because concurrency sounds exciting.
   Every stage assumes the one before it. Skipping ahead feels like progress and is the
   fastest way to quit.
2. **Code every day.** 45–90 focused minutes a day beats an 8-hour Sunday. Consistency
   is the whole game.
3. **Never skip the "do it yourself" part.** Watching a video is not learning. Reading
   a chapter is not learning. Typing the code, running it, breaking it, fixing it — that's
   learning. If a resource says "try this", you try it before reading on.
4. **Type, don't paste.** Even when following a tutorial. Your fingers learning the
   syntax is part of the point.
5. **Build the project for every stage.** The projects in `PROJECTS.md` are not
   optional extras. They are where knowledge turns into skill, and they become your
   interview stories.
6. **Commit to git daily.** From Stage 01. It builds the habit and gives you a visible
   trail of progress to look back on.

---

## 2. How to use the resources in each stage

Every stage lists **books**, **courses & videos**, **practice sites** and **references**.
You do **not** do all of them. Here's how to choose:

- Every list marks **⭐ START HERE** on one or two items. Do those first, fully.
- **Books** are for depth and for going back to. Read with a code editor open; run every
  example.
- **Courses & videos** are for the first pass on a topic you've never seen. Watch at 1×,
  pause, type along. If a course has exercises, do them.
- **Practice sites** are where you make it stick. Little and often.
- **References** are for looking things up, not reading cover-to-cover. Learning to read
  official documentation is itself a skill you need.
- 🆓 = free · 💰 = paid. Free options exist for every stage; paid ones are optional.

**A rule of thumb per topic:** one course or book for the first pass → practice until it's
boring → the deeper book when you reach the stage that needs it.

---

## 3. A weekly rhythm that works

| Day | What |
|---|---|
| Mon–Thu | 60–90 min: new material (course/book) + type along + one small exercise |
| Fri | 60 min: practice only (exercises, problems), no new material |
| Sat | 2–3 h: project work for the current stage |
| Sun | 30 min: review your notes, update `PROGRESS.md`, plan next week. Rest. |

That's roughly **10–12 hours a week**. At 5 you still get there, just later. Missing a day
is fine. Missing a week is how habits die — do 15 minutes rather than zero.

If you can do **20–25 hours a week** (the pace the `ROADMAP.md` milestones assume), use
this shape instead:

| Slot | What |
|---|---|
| 5 × 2 h | building the current project |
| 2 × 1.5 h | DSA / LeetCode (Stages 03–09) or design practice (Stages 11–20) |
| 1 × 1 h | reading the ⭐ resource for the current stage |
| 1 × 1 h | writing: story bank, README, project write-up |

---

## 4. How to study so it actually sticks

- **Active recall.** After a lesson, close it and write out (or say aloud) what you
  learned without looking. Then check. The struggle to remember is what builds memory.
- **Explain it to a rubber duck.** If you can't explain a concept in plain words, you
  don't know it yet. This is also exactly what interviews test.
- **Keep a learning journal** (`notes/` folder, one file per stage). Write: what I
  learned, what confused me, what I'd tell past-me. Two minutes a day.
- **Spaced review.** Every Sunday, re-do one exercise from two stages ago. Use Anki
  (free flashcard app) for vocabulary if you like — but for code, re-typing beats cards.
- **Vary the problems.** Doing 30 near-identical exercises teaches less than 10 varied
  ones.

---

## 5. When you're stuck (you will be, constantly — this is normal)

1. **Read the error message.** Top to bottom, slowly. It usually tells you the line and
   the problem. Beginners skip this; don't.
2. **Print things.** Add `print()` calls to see what your variables actually hold. Later,
   use the debugger (Stage 04).
3. **Make the problem smaller.** Delete everything until it works, then add back one line
   at a time.
4. **Search the exact error text** (without your file names). Someone has hit it before.
5. **Ask an AI assistant — the right way.** Ask it to *explain* the concept or the error,
   not to write the solution. If it writes code, retype it yourself and make sure you can
   explain every line. Copy-paste from AI is the new copy-paste from Stack Overflow: it
   feels like progress and teaches nothing.
6. **Time-box it.** 30–45 minutes genuinely stuck → take a walk → come back → if still
   stuck, note it in your journal, move on, and return tomorrow. Sleep fixes bugs.
7. **Ask a human.** Discord servers (Python Discord, r/learnpython), study groups. Post
   your code, the exact error, and what you've tried.

---

## 6. Things beginners get wrong (so you don't)

- **Tutorial hell:** watching course after course and never building anything. Cure:
  the project for each stage, no exceptions.
- **Perfectionism:** trying to understand *everything* in a chapter before moving on.
  You'll understand 70% now and the rest when you come back with more context. Keep
  moving.
- **Comparing timelines:** someone online did it in 6 months. They had a CS degree, or
  they're lying, or they're a genius. Irrelevant. Compare to yourself last month.
- **Collecting resources instead of using them.** Bookmarking 40 courses feels
  productive. Pick the ⭐ one and finish it.
- **Skipping fundamentals to get to the "cool" stuff.** The cool stuff (GPUs, LLM
  serving) is 90% fundamentals wearing a lab coat. The fundamentals are the cool stuff.
- **Not reading documentation.** Docs feel intimidating. Every senior engineer reads
  them daily. Start with the Python tutorial and the FastAPI docs; they're excellent.
- **Quitting at the dip.** Around weeks 6–10 the excitement wears off and it gets hard.
  Everyone hits this. The people who make it are the ones who show up the next day anyway.

---

## 7. What "done with a stage" means

Each stage has a **✅ Checkpoint**. You're done when you can do every item on it
**without looking anything up** — not when you've watched the videos. If you can't,
that's fine; that's information about what to practise next, not a failure.

Then: tick it in `PROGRESS.md`, commit, write two lines in your journal, and start the
next stage the following day. Don't take a "well-earned week off" between stages — that's
where momentum goes to die.

---

## 8. The running threads (don't leave these to the end)

From day one, keep a `notes/` folder with `stories.md` (behavioral story bank — add to it
every stage), `journal.md`, `leetcode.md` (the redo list) and, from Stage 06, a
`designs/` folder. `ROADMAP.md` → *Running threads* lists the five habits (story bank,
values & safety, take-home craft, communication, public proof of work) and when each
starts. They're cheap weekly and impossible to fake at the end.

## 9. Tools to set up in week one

- **Python 3.12+** (python.org, or via your OS package manager)
- **VS Code** (free) with the Python extension — or PyCharm Community (free)
- **Git** (git-scm.com) and a **GitHub** account
- A terminal you're comfortable with (Terminal on macOS, Windows Terminal + WSL on
  Windows — install WSL, you'll want Linux for the whole road)
- This repo cloned locally, and `python3 stages/01_python/01_hello_world.py` running

That's it. You don't need Docker, Postgres, Redis or a GPU until the stage that uses them.

> **Bottom line:** show up daily, type everything, build every project, explain things in
> plain words, commit your work. Do that and the mountain takes care of itself.
