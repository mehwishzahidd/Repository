# 🌳 Git & GitHub — your developer toolkit

Every professional developer uses **git** every single day. Interviewers expect you to
know it. The good news: you only need a handful of commands for 95% of your work.

---

## What problem does git solve?

Imagine writing an essay and saving copies named `essay_final.doc`,
`essay_final_v2.doc`, `essay_REALLY_final.doc`... It's a mess, and you can't easily
see what changed or undo a mistake.

**Git** is a "time machine" for your code. It saves snapshots (called **commits**) of
your project. You can see the full history, compare versions, undo mistakes, and work
on experiments safely without breaking your main code.

**GitHub** is a website that stores your git projects in the cloud, so you can back
them up, share them, and collaborate. (Think "Google Drive, but built for code.")

---

## The mental model: 3 areas

```
   Working Directory          Staging Area              Repository
   (your files)               (the "on-deck" box)       (saved history)
        │                            │                        │
        │   git add <file>          │     git commit         │
        │ ─────────────────────────▶│ ──────────────────────▶│
        │                            │                        │
                                                              │  git push
                                                              │ ─────────▶  GitHub (cloud)
```

1. **Working directory** — the files you actually edit.
2. **Staging area** — files you've marked as "ready to be saved" with `git add`.
3. **Repository** — the permanent history, where `git commit` saves your snapshot.
4. **GitHub** — the cloud copy, updated with `git push`.

---

## The daily commands (this is 95% of git)

| Command | What it does |
|---|---|
| `git status` | Show what's changed and what's staged. **Run this constantly.** |
| `git add <file>` | Stage a file (mark it ready to commit). `git add .` stages everything. |
| `git commit -m "message"` | Save a snapshot of staged files, with a description. |
| `git push` | Upload your commits to GitHub. |
| `git pull` | Download the latest changes from GitHub. |
| `git log --oneline` | See the history of commits. |
| `git diff` | See exactly what lines you changed (before staging). |

### A typical cycle looks like this:

```bash
git status                          # See what changed
git add learning/my_solution.py     # Stage the file I worked on
git commit -m "Solve exercise 3"    # Save a snapshot with a clear message
git push                            # Back it up to GitHub
```

That's it. That loop — **edit → add → commit → push** — is the heartbeat of coding.

---

## Branches (the safe-experiment feature)

A **branch** is a parallel copy of your code where you can try things without affecting
the main version. You're on one right now! Check with:

```bash
git branch          # lists branches; the * marks the one you're on
```

When work on a branch is ready, you open a **Pull Request (PR)** on GitHub — a request
to merge your branch into the main one. PRs are how teams review code before it becomes
official. (I'll create one for you so you can see what it looks like.)

---

## ✍️ Writing good commit messages

A commit message explains *why* a change was made. Good ones are short and clear:

- ✅ `Add solution for two-sum exercise`
- ✅ `Fix off-by-one error in loop`
- ❌ `stuff` / `asdf` / `update` (these tell your future self nothing)

---

## 🏋️ Your first git exercise

Once you've run a lesson or edited a file, try the full cycle yourself:

```bash
git status                              # what changed?
git add learning/                       # stage your work
git commit -m "Complete first Python lesson"   # save a snapshot
git push                                # send it to GitHub
```

Then go to your repository on GitHub.com and look at the **commit history** — you'll
see your message there. That's your work, permanently recorded. 🎉

> **Tip:** there is no way to "break" git by experimenting on your own branch. Be brave.
> Almost anything in git can be undone. When you're unsure, run `git status` — it usually
> tells you exactly what to do next.
