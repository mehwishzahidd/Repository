# Stage 04 — Git, GitHub, the shell and Linux

> **Roadmap Group 1 · general software skills.** Every codebase, job, and project from
> here on lives in git and runs on Linux. You've been using git since Stage 01; this
> stage makes it fluent and adds the command line and Linux fundamentals infra engineers
> live in.

## If you're new to this

**Git** records the history of your code so you can undo mistakes, work on ideas in
parallel (branches), and collaborate. **GitHub** hosts git repositories online and adds
pull requests and code review. **The shell** (terminal) is how engineers actually talk to
computers: faster than clicking, scriptable, and the only interface on a server.
**Linux** is the operating system nearly every server, container and GPU box runs.

**Time:** 2–3 weeks at ~8 hours/week, then used daily forever.

**Prerequisites:** Stage 01 (you've made commits). Windows users: install **WSL2** now.

---

## Modules (in order)

1. **Git fundamentals** — the three areas (working dir / staging / repo), `init`,
   `status`, `add`, `commit`, `log`, `diff`, `.gitignore`, good commit messages.
2. **Branching** — `branch`, `switch`/`checkout`, `merge`, fast-forward vs merge
   commits, resolving **conflicts** (do it on purpose three times), `stash`.
3. **Undoing things** — `restore`, `reset` (soft/mixed/hard), `revert`, `reflog` (the
   "nothing is ever lost" tool), amending the last commit.
4. **Remotes & GitHub** — `clone`, `remote`, `fetch`/`pull`/`push`, `-u`, forks, **pull
   requests**, reviewing a PR, protected branches, README/LICENSE conventions.
5. **Rebase (basics)** — `rebase` vs `merge`, interactive rebase to squash, and the rule
   "never rewrite shared history".
6. **The shell** — navigation, paths, globbing, `ls -la`, `cat/less/head/tail`, pipes
   `|`, redirection `> >> 2>&1`, `grep`, `find`, `sort | uniq -c`, `xargs`, `sed` & `awk`
   basics, `cut`, `wc`, `diff`, `tar`, `curl`, environment variables, `PATH`, aliases,
   a minimal shell script with variables and loops.
7. **Linux essentials** — the filesystem layout (`/etc`, `/var/log`, `/proc`), users and
   **permissions** (`chmod`, `chown`, `sudo`), **processes** (`ps`, `top`/`htop`,
   `kill`, signals, background jobs, `nohup`), **package managers** (`apt`), services
   (`systemctl`), **SSH** (keys, `ssh`, `scp`), reading logs (`journalctl`, `tail -f`),
   cron, disk (`df`, `du`), network basics (`ip`, `ss`, `ping`, `dig` — more in Stage 07).
8. **Editor & debugger** — VS Code well (multi-cursor, go-to-definition, integrated
   terminal), Python **debugger** (breakpoints, step, watch, call stack), `pdb` basics,
   and enough `vim` to edit a file on a server (`i`, `Esc`, `:wq`).
9. **Reading documentation** — `man`, `--help`, official docs, how to search errors.
10. **Code review as a skill** — reading a pull-request diff top to bottom, asking "what
    could break?", leaving comments that are specific and kind ("this loop is O(n²) for
    large inputs; a set would fix it" not "this is slow"), receiving comments without
    defending, and the reviewer's checklist: correctness → tests → edge cases → naming
    → style. Practise on your own PRs first (review yesterday's code as if a stranger wrote
    it), then on open-source PRs you read but don't comment on, then on a study partner's
    code. Half of the OpenAI deep-dive round is you being reviewed live; this is the
    rehearsal. Resource: **Google's Engineering Practices, "How to do a code review"** 🆓.

---

## 📚 Resources

### Courses & videos
- ⭐ **MIT — The Missing Semester of Your CS Education** (missing.csail.mit.edu) 🆓 — shell,
  shell tools, editors, data wrangling, git, debugging & profiling. Made exactly for this
  gap. Do all lectures and exercises.
- ⭐ **Learn Git Branching** (learngitbranching.js.org) 🆓 — interactive, visual; do the
  whole thing, including the remote levels.
- **GitHub Skills** (skills.github.com) 🆓 — hands-on PR/review courses inside GitHub.
- **Linux Journey** (linuxjourney.com) 🆓 — gentle, structured Linux basics.
- **freeCodeCamp Linux/Bash full courses** (YouTube) 🆓.

### Books
- ⭐ **Pro Git** (Chacon & Straub) 🆓 online — chapters 1–3, 5, 7 now; the reference for life.
- ⭐ **The Linux Command Line** (William Shotts) 🆓 PDF at linuxcommand.org — parts 1–3
  now, part 4 (scripting) later.
- **How Linux Works** (Brian Ward) 💰 — the "what's actually happening" book; read in
  Stage 08 alongside OS.
- **Efficient Linux at the Command Line** (Barrett) 💰 — great for speed habits.

### Practice
- ⭐ **OverTheWire: Bandit** (overthewire.org) 🆓 — a game that teaches the shell one
  level at a time. Get to level ~20.
- **Oh My Git!** 🆓 — a git game.
- **Exercism Bash track** 🆓 — for scripting.
- **cmdchallenge.com** 🆓 — one-liner puzzles.

### Reference
- **git-scm.com docs**, `man git-<command>`
- **explainshell.com** 🆓 — paste any command, it explains every flag.
- **tldr pages** (tldr.sh) 🆓 — short examples for any command.
- **Oh Shit, Git!?!** (ohshitgit.com) 🆓 — how to get out of git messes.

---

## Practice & exercises
- Create a repo, make a feature branch, cause a conflict with `main`, resolve it, open a
  PR, review it yourself, merge it, delete the branch.
- Break your repo on purpose (bad `reset --hard`) and recover it with `reflog`.
- Write a shell script that finds the 10 largest files under a directory.
- From a log file: count requests per status code with one pipeline
  (`grep | awk | sort | uniq -c | sort -rn`).
- SSH into a Linux VM (a free-tier cloud VM or a local VirtualBox/Multipass one),
  create a user, set permissions, run a Python script under `nohup`, find it with `ps`,
  kill it.
- Step through a buggy Stage 03 solution with the debugger instead of `print`.

## Beginner pitfalls
- **Committing secrets** (API keys, `.env`). Add `.gitignore` before the first commit.
- **Giant commits.** Small, frequent, described commits. Future-you will thank you.
- **Force-pushing shared branches.** Don't. Ever, on a branch someone else uses.
- **Fear of the terminal.** You cannot break your computer with `ls`. Explore.
- **`sudo` everything.** Understand permissions instead.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You've committed daily for two weeks and can branch/merge/rebase/resolve conflicts
      without looking anything up.
- [ ] You can recover from a bad reset, a merge conflict and a detached HEAD.
- [ ] You can write a pipeline with `grep`, `awk`, `sort`, `uniq` to answer a question
      about a log file.
- [ ] You can SSH into a Linux machine, inspect processes, permissions and logs, and run a
      script in the background.
- [ ] You use the debugger to find a bug, not `print`.

## 🛠️ Project
This repo already has a `Makefile` and a GitHub Actions workflow (`.github/workflows/
check.yml`) that run the lessons and checkers. Your project: **read both until you can
explain every line**, then extend the workflow with `ruff` linting and a `pytest` step for
`projects/`, and add `format` and `lint` targets to the Makefile. Then open it as a PR and
review your own diff using the checklist in module 10.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 05"** to get its hands-on lessons built.
