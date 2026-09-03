# 📚 RESOURCES — the whole library, one page

Every book, course, practice site and reference from every stage, in stage order. Tags:
⭐ = the one to do if you only do one · 🆓 free · 💰 paid. Don't collect these — pick the
⭐ item for your *current* stage and finish it (see `LEARNING_GUIDE.md` §2).

Stage guides own the detail (what chapters, when); this page is for finding things fast.
See also `LEETCODE.md` (practice plan), `AI_TUTOR.md` (using AI as a tutor) and
`BUDGET.md` (what each stage costs, and the free path).


---

## Stage 00 — How computers and programs work (the on-ramp)
*→ [`stages/00_how_computers_work/`](./stages/00_how_computers_work/)*

- ⭐ **CS50x** (Harvard, free on edX/YouTube) 🆓 — Week 0 (Scratch) and Week 1 (C). Don't
  worry about C long-term; it teaches what programs *are*.
- ⭐ **Crash Course Computer Science** (YouTube, PBS) 🆓 — episodes 1–20. Painless overview
  of how hardware runs software.
- **But How Do It Know?** (J. Clark Scott) 💰 — optional, if you want the "how does a CPU
  actually work" itch scratched now (Nand2Tetris in Stage 21 does it properly later).
- **Code** (Charles Petzold) 💰 — the same story told beautifully; also optional.
- **How the Internet Works** — Cloudflare Learning Center 🆓 or the *"How does the
  internet work?"* MDN page 🆓.


---

## Stage 01 — Python basics
*→ [`stages/01_python/`](./stages/01_python/)*

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


---

## Stage 02 — Programming: classes, files, the standard library, stronger Python
*→ [`stages/02_programming/`](./stages/02_programming/)*

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


---

## Stage 03 — Data Structures & Algorithms
*→ [`stages/03_dsa/`](./stages/03_dsa/)*

### Courses & videos
- ⭐ **NeetCode.io roadmap + videos** 🆓 — the practice backbone. Every pattern above has
  a section; every problem has a clear video. Follow the order in `LEETCODE.md`.
- ⭐ **Abdul Bari — Algorithms** (YouTube) 🆓 — the clearest lectures on sorting,
  recursion, DP and graphs. Watch the topic *before* practising it.
- **William Fiset — Graph Theory playlist** and **Data Structures playlist** (YouTube) 🆓
  — the best graph explanations anywhere; go through the whole graph playlist in module 9.
- **MIT 6.006 Introduction to Algorithms** (OCW, free lectures) 🆓 — the university
  course; heavier. Do the lectures on hashing, sorting, BFS/DFS, shortest paths, DP.
- **Princeton Algorithms I & II** (Coursera, Sedgewick) 🆓 to audit — superb on union-find,
  heaps, graphs; examples in Java, ideas universal.
- **Back To Back SWE** (YouTube) 🆓 — deep walk-throughs of hard problems.

### Books
- ⭐ **Grokking Algorithms** (Aditya Bhargava) 💰 — the illustrated beginner book. Read it
  in week 1; it makes everything else easier.
- ⭐ **Problem Solving with Algorithms and Data Structures using Python** (Miller & Ranum)
  🆓 at runestone.academy — implementations in Python of every structure here.
- **A Common-Sense Guide to Data Structures and Algorithms** (Jay Wengrow) 💰 — gentle,
  good second pass.
- **Cracking the Coding Interview** (McDowell) 💰 — interview-process advice + problems.
- **Algorithms** (Sedgewick & Wayne) 💰 or **CLRS** 💰 — references for depth; not for
  reading cover-to-cover now.
- **Competitive Programmer's Handbook** (Laaksonen) 🆓 PDF — compact, for graphs/DP depth.
- **The Algorithm Design Manual** (Skiena) 💰 — reference; chapters 1–5 are gold, and the
  "war stories" teach how to *choose* an algorithm.
- **A Philosophy of Software Design** (Ousterhout) 💰 — short; the best book on writing
  code that survives "now add X". Read it alongside the Anthropic drill.

### Practice
- ⭐ **`LEETCODE.md` Phase B** — pattern by pattern, with the redo rule.
- **NeetCode 150 / Blind 75** — the same list, curated.
- **Tech Interview Handbook** (techinterviewhandbook.org) 🆓 — the "Grind 75" list and
  excellent cheat-sheets per data structure.
- **AlgoExpert** 💰 — optional; curated explanations if you want a paid track.
- **VisuAlgo** (visualgo.net) 🆓 — animates every algorithm; use it when stuck.
- **Structy** 💰 — great for graph/recursion beginners.
- **CodeSignal practice area** 🆓 — one problem a week here, because it's the OA's actual
  environment. Also try a problem in a bare Colab notebook.

### Reference
- **Big-O Cheat Sheet** (bigocheatsheet.com) 🆓
- **Python `heapq`, `bisect`, `collections` docs**
- **Tech Interview Handbook algorithms cheatsheets** 🆓

---


---

## Stage 04 — Git, GitHub, the shell and Linux
*→ [`stages/04_git_linux/`](./stages/04_git_linux/)*

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


---

## Stage 05 — SQL and databases
*→ [`stages/05_sql_databases/`](./stages/05_sql_databases/)*

### Courses & videos
- ⭐ **SQLBolt** (sqlbolt.com) 🆓 — interactive, 18 short lessons; the perfect first day.
- ⭐ **CMU 15-445/645 Intro to Database Systems** (Andy Pavlo, YouTube + course site) 🆓 —
  *the* database course. Lectures 1–2 (relational model, SQL) now; lectures on storage,
  indexes, joins, and concurrency control in modules 9–11 and again in Stage 12.
- **Stanford Databases self-paced** (edX / online.stanford.edu) 🆓 — relational algebra,
  SQL, design theory.
- **Hussein Nasser — Database Engineering** (YouTube) 🆓 — practical deep-dives on
  indexes, isolation, connection pooling.
- **freeCodeCamp SQL / PostgreSQL full courses** (YouTube) 🆓.

### Books
- ⭐ **Learning SQL** (Alan Beaulieu) 💰 — the classic; chapters 1–10, 13, 16.
- ⭐ **Use The Index, Luke** (Markus Winand) 🆓 online — the indexing book. Read all of it
  in module 9.
- **The Art of PostgreSQL** (Dimitri Fontaine) 💰 — SQL as a real language, Postgres-first.
- **SQL Antipatterns** (Bill Karwin) 💰 — schema mistakes and their fixes.
- **Database Design for Mere Mortals** (Hernandez) 💰 — gentle design theory.
- **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapter 2 (data models) and
  3 (storage & retrieval) now; the rest in Stages 10–12.
- **PostgreSQL docs** — the tutorial chapters are genuinely good.

### Practice
- ⭐ **pgexercises.com** 🆓 — Postgres exercises from basic to window functions.
- **Select Star SQL** (selectstarsql.com) 🆓 — narrative SQL tutorial with a real dataset.
- **Mode SQL Tutorial** 🆓 — intermediate/advanced with analytics flavour.
- **LeetCode Database problems** 🆓 — do the "SQL 50" study plan.
- **HackerRank SQL** 🆓.
- **DataLemur SQL** 🆓/💰 — interview-style questions.

### Reference
- **PostgreSQL manual** (postgresql.org/docs) — especially "Indexes", "Performance
  Tips", "Concurrency Control".
- **explain.depesz.com / explain.dalibo.com** 🆓 — paste an `EXPLAIN` plan, get it
  visualised.

---


---

## Stage 06 — Backend development
*→ [`stages/06_backend/`](./stages/06_backend/)*

### Courses & videos
- ⭐ **FastAPI official tutorial** (fastapi.tiangolo.com) 🆓 — genuinely the best
  framework docs in existence. Do "Tutorial – User Guide" end to end, then "Advanced".
- ⭐ **TestDriven.io — "Test-Driven Development with FastAPI and Docker"** 💰 — builds
  exactly this stage's project with tests and Docker.
- **ArjanCodes — FastAPI / software design videos** (YouTube) 🆓.
- **freeCodeCamp — "Python API Development" (FastAPI, Postgres, Docker, ~19 h)** 🆓.
- **Hussein Nasser — Backend Engineering** (YouTube) 🆓 — connection pooling, HTTP,
  proxies; excellent intuition.
- **roadmap.sh/backend** 🆓 — a map of the field to see where you are.
- **CS50W — Web Programming with Python and JavaScript** (Harvard) 🆓 — lectures 0–4 for
  how web apps fit together, if you want the wider picture.

### Books
- ⭐ **Architecture Patterns with Python** (Percival & Gregory) 🆓 online at
  cosmicpython.com — repositories, services, unit of work, events, testing strategy.
  Read part 1 now.
- ⭐ **Python Testing with pytest** (Okken) 💰 — the rest of the book now.
- **Test-Driven Development with Python** (Percival) 🆓 online — Django-based but the
  testing mindset is the point.
- **Designing Web APIs** (Jin, Sahni, Shevat) 💰 — API design from the product side.
- **FastAPI** (Bill Lubanovic, O'Reilly) 💰 — a solid book-length tour.
- **The Twelve-Factor App** (12factor.net) 🆓 — read it twice.
- **Web Application Security** (Andrew Hoffman) 💰 or **OWASP Top 10** 🆓 — for module 7.

### Practice
- ⭐ **Build P2** — nothing substitutes for it.
- **PortSwigger Web Security Academy** 🆓 — labs for injection, auth, CSRF; do the
  "Apprentice" level.
- **Public APIs list** (github.com/public-apis) 🆓 — pick one, wrap it, cache it, test it.
- **Exercism** — keep going, but the project is the practice now.

### Reference
- **MDN HTTP docs** 🆓 — status codes, headers, caching.
- **SQLAlchemy 2.0 docs**, **Alembic tutorial**, **Pydantic docs**, **Docker docs
  "Get started"**.
- **httpstatuses.com**, **jwt.io** 🆓.

---


---

## Stage 07 — Networking
*→ [`stages/07_networking/`](./stages/07_networking/)*

### Courses & videos
- ⭐ **Kurose & Ross — Computer Networking: A Top-Down Approach, free video lectures**
  (gaia.cs.umass.edu/kurose_ross) 🆓 — chapters 1–3 (intro, application layer, transport).
- ⭐ **Cloudflare Learning Center** (cloudflare.com/learning) 🆓 — short, clear articles
  on DNS, TLS, HTTP/2, CDNs. Start here for any term you don't know.
- **Practical Networking** (YouTube) 🆓 — how packets actually move; superb visuals.
- **Stanford CS144** (cs144.github.io) 🆓 — university networking with labs where you
  build a TCP implementation. Optional, for depth.
- **Hussein Nasser — Network fundamentals / HTTP playlist** (YouTube) 🆓.
- **Julia Evans — "Networking! ACK!" zine** 💰 — the friendliest intro that exists.

### Books
- ⭐ **High Performance Browser Networking** (Ilya Grigorik) 🆓 online at hpbn.co —
  latency, TCP, TLS, HTTP/1.1/2. Chapters 1–4, 9–12.
- ⭐ **Beej's Guide to Network Programming** 🆓 — sockets, from the socket's point of view.
  C examples; read for concepts, redo in Python.
- **Computer Networking: A Top-Down Approach** (Kurose & Ross) 💰 — the textbook.
- **HTTP: The Definitive Guide** (Gourley & Totty) 💰 — old but the HTTP reference.
- **TCP/IP Illustrated, Vol. 1** (Stevens/Fall) 💰 — the deep reference; not now.

### Practice
- ⭐ **Build P3's single-threaded crawler** with every failure mode above.
- **httpbin.org** 🆓 — an HTTP server that returns whatever you ask (redirects, delays,
  status codes). Perfect for testing timeout and retry logic.
- **Wireshark sample captures** 🆓 — read a real HTTP and DNS exchange.
- **"Build your own HTTP server"** (codecrafters.io 💰, or free by following RFC 9110)
  — parse requests from a raw socket.

### Reference
- **MDN HTTP** 🆓, **RFC 9110/9111** (HTTP semantics/caching), **RFC 3986** (URLs),
  **robots.txt RFC 9309**.
- **`urllib.parse`** and **`httpx`** docs.

---


---

## Stage 08 — Operating systems
*→ [`stages/08_operating_systems/`](./stages/08_operating_systems/)*

### Courses & videos
- ⭐ **Crash Course Computer Science** (YouTube, episodes 1–20) 🆓 — the friendliest
  "what is a computer" series ever made. Watch first if module 1 is new.
- ⭐ **CMU 15-213 Introduction to Computer Systems** (free lectures) 🆓 — the course
  behind CS:APP; lectures on memory hierarchy, virtual memory, exceptional control flow,
  concurrency.
- **Neso Academy — Operating System** (YouTube) 🆓 — short, exam-style clarity on
  processes, scheduling, synchronization, memory.
- **Berkeley CS162** (YouTube) 🆓 — a full OS course, if you want the real thing.
- **Nand2Tetris** (nand2tetris.org / Coursera) 🆓 — build a computer from logic gates
  to an OS. Optional; the single best way to make "how computers work" click. (Also in
  Stage 21.)
- **Brendan Gregg — Linux Performance** (brendangregg.com, talks) 🆓 — for module 11.

### Books
- ⭐ **Operating Systems: Three Easy Pieces** (Arpaci-Dusseau) 🆓 at ostep.org — the one
  OS book to read. Virtualization (CPU + memory) and Persistence now; Concurrency in
  Stage 09.
- **Computer Systems: A Programmer's Perspective** (Bryant & O'Hallaron) 💰 — chapters
  1, 6, 8, 9, 10, 12. Deeper and C-based; the memory-hierarchy chapter is gold.
- **How Linux Works** (Brian Ward) 💰 — the practical Linux internals companion.
- **The Linux Programming Interface** (Kerrisk) 💰 — the syscall bible; a reference.
- **Code** (Charles Petzold) 💰 — the story of how computers work, zero prerequisites.
- **Julia Evans zines** 💰 — *Linux debugging tools*, *Bite Size Linux* — delightful.

### Practice
- ⭐ **OSTEP homework and projects** 🆓 (the simulators are Python) — do the CPU
  scheduling, paging and `xv6`-free ones.
- **Write a shell** 🆓 — a tiny shell in Python/C that forks, execs, pipes, and handles
  Ctrl-C. The classic OS project.
- **`strace` / `ltrace` your own programs.**

### Reference
- **`man 2 <syscall>`**, **`man 7 signal`**, **`/proc` documentation**.
- **Brendan Gregg's Linux Performance page** 🆓 — the tool map.

---


---

## Stage 09 — Concurrency 🚨
*→ [`stages/09_concurrency/`](./stages/09_concurrency/)*

### Courses & videos
- ⭐ **Łukasz Langa — "import asyncio" series** (YouTube, by a CPython core dev) 🆓 — the
  best from-scratch asyncio explanation; watch all episodes.
- ⭐ **Corey Schafer — Threading and Multiprocessing tutorials** (YouTube) 🆓.
- **ArjanCodes — asyncio / concurrency videos** (YouTube) 🆓.
- **Real Python — "Async IO in Python", "An Intro to Threading", "Speed Up Your Python
  Program With Concurrency"** 🆓 articles — clear and current.
- **OSTEP concurrency lectures** (ostep.org videos) 🆓.
- **Raymond Hettinger — "Keynote on Concurrency" (PyBay 2017)** (YouTube) 🆓 — how to
  *think* about threads safely; watch twice.

### Books
- ⭐ **Python Concurrency with asyncio** (Matthew Fowler) 💰 — the asyncio book; all of it.
- ⭐ **OSTEP, part II "Concurrency"** 🆓 — threads, locks, condition variables, semaphores,
  common bugs, event-based concurrency. The *why* behind every primitive.
- **The Little Book of Semaphores** (Allen Downey) 🆓 PDF — the classic problems as
  puzzles. Do the first half.
- **Using Asyncio in Python** (Caleb Hattingh) 💰 — short, opinionated, good.
- **Fluent Python** (Ramalho) 💰 — chapters 19–21 (concurrency models, executors, asyncio).
- **High Performance Python** (Gorelick & Ozsvald) 💰 — the chapters on multiprocessing
  and asyncio.
- **Seven Concurrency Models in Seven Weeks** (Butcher) 💰 — actors, CSP, STM: broader view.
- **Java Concurrency in Practice** (Goetz) 💰 — language aside, the best book on the
  *principles* of thread safety. Optional, later.

### Practice
- ⭐ **`LEETCODE.md` Phase C — the Concurrency section** (Print in Order, FooBar, H2O,
  Dining Philosophers, Bounded Blocking Queue, Multithreaded Web Crawler): do every one.
- **Build P3 (concurrent) and P5** — the real practice.
- **httpbin.org `/delay/N`** — your load generator for timeouts and concurrency limits.

### Reference
- **Python docs:** `threading`, `queue`, `concurrent.futures`, `multiprocessing`,
  `asyncio` (read the "Coroutines and Tasks" and "Synchronization Primitives" pages
  slowly).
- **Python asyncio cheat-sheet** (various) 🆓, **`httpx` async docs**.

---


---

## Stage 10 — Caching, queues, workers and reliability
*→ [`stages/10_caching_queues_workers/`](./stages/10_caching_queues_workers/)*

### Courses & videos
- ⭐ **Redis University — RU101 Introduction to Redis Data Structures** (redis.io/university) 🆓.
- ⭐ **AWS Builders' Library** (aws.amazon.com/builders-library) 🆓 — Marc Brooker et al.
  on *timeouts, retries and backoff with jitter*, *avoiding fallback*, *caching challenges*,
  *using load shedding*, *leader election*. Short, from people who run it at scale.
- **Confluent Developer — Apache Kafka 101** 🆓 — Kafka concepts in an afternoon.
- **RabbitMQ tutorials** (rabbitmq.com/tutorials, Python) 🆓 — do 1–6.
- **Hussein Nasser — Message queues, Redis, Kafka videos** (YouTube) 🆓.
- **Marc Brooker's blog** 🆓 — backoff, jitter, "exactly once", metastable failures.

### Books
- ⭐ **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapters 1, 4, 11
  (stream processing) now; it becomes your main book in Stages 11–12.
- ⭐ **Release It!** (Michael Nygard, 2nd ed.) 💰 — stability patterns: timeouts, circuit
  breakers, bulkheads, steady state, fail fast. The reliability book.
- **Redis in Action** (Josiah Carlson) 🆓 online at redis.com — patterns with real code.
- **Kafka: The Definitive Guide** (Confluent, free PDF) 🆓 — chapters 1–4, 6.
- **Site Reliability Engineering** (Google) 🆓 online — chapters 21–22 (overload,
  cascading failures).
- **Enterprise Integration Patterns** (Hohpe & Woolf) 💰 — the messaging pattern
  catalogue; skim the site (enterpriseintegrationpatterns.com) 🆓.

### Practice
- ⭐ **Build P6 as a 48-hour take-home**, then keep going with the "then add" list.
- **Redis "Try Redis" sandbox** 🆓, **Play with Docker** 🆓 for a throwaway Kafka.
- **Stripe's idempotency blog post** and **Stripe webhooks docs** 🆓 — read how a real
  company does it; copy the ideas.

### Reference
- **Redis docs** (commands, "Redis as a cache", "Streams"), **Kafka docs**, **Postgres
  `SELECT … FOR UPDATE SKIP LOCKED`**, **Celery / arq docs**, **`tenacity`** (retries
  library) docs.

---


---

## Stage 11 — General system design 🚨
*→ [`stages/11_system_design/`](./stages/11_system_design/)*

### Courses & videos
- ⭐ **ByteByteGo** (YouTube channel + newsletter, Alex Xu) 🆓 — clear diagrams of real
  systems. Watch the whole "System Design" playlist.
- ⭐ **Hello Interview — System Design in a Hurry + guided walkthroughs**
  (hellointerview.com) 🆓 — the most interview-accurate free material right now, with
  written solutions for the catalogue above.
- **Jordan has no life** (YouTube) 🆓 — long-form, deep, opinionated; great after ByteByteGo.
- **Gaurav Sen** (YouTube) 🆓 — approachable intros to each building block.
- **Grokking the System Design Interview** (Educative / designgurus) 💰 — the classic
  structured course. Optional.
- **Martin Kleppmann's DDIA lectures** (Cambridge, YouTube) 🆓 — replication, partitioning.
- **InfoQ / QCon talks, Uber/Netflix/Discord engineering blogs** 🆓 — real systems.

### Books
- ⭐ **System Design Interview – An Insider's Guide, Vol. 1 & 2** (Alex Xu) 💰 — the
  interview books; every chapter is a worked problem.
- ⭐ **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapters 5–7 (replication,
  partitioning, transactions) now; 8–9 in Stage 12.
- **System Design Primer** (github.com/donnemartin/system-design-primer) 🆓 — the
  famous repo; the "study guide" and per-component sections.
- **Understanding Distributed Systems** (Roberto Vitillo) 💰 — short, modern, practical.
- **Web Scalability for Startup Engineers** (Artur Ejsmont) 💰 — underrated, very clear.
- **Site Reliability Engineering** (Google) 🆓 — chapters 3–6 for SLOs and monitoring.
- **Papers (read the ideas, not every proof):** Dynamo (Amazon), Bigtable, GFS,
  MapReduce, Consistent Hashing (Karger), Cassandra, Spanner (abstract), Chubby. 🆓

### Practice
- ⭐ **Mock interviews** — with a peer, or record yourself; Hello Interview 💰 and
  interviewing.io 💰 sell mocks with engineers. Do at least 6 before Stage 20.
- **Excalidraw / draw.io** 🆓 — draw every design; keep them in `notes/designs/`.
- **Write a `DESIGN.md` for P2, P4, P6** as if presenting each in an interview.
- **Estimation drills:** "How many req/s is 100M daily users?" until it's instant.

### Reference
- **Latency numbers every programmer should know** 🆓 (Jeff Dean's table) — memorise.
- **Hello Interview "core concepts" and "key technologies" pages** 🆓.
- **AWS Architecture Center / Well-Architected Framework** 🆓.
- **Stripe, Cloudflare, Figma, Discord engineering blogs** on rate limiting, sharding,
  and caching 🆓.

---


---

## Stage 12 — Distributed systems and database internals 🚨
*→ [`stages/12_distributed_systems/`](./stages/12_distributed_systems/)*

### Courses & videos
- ⭐ **MIT 6.824 / 6.5840 Distributed Systems** (pdos.csail.mit.edu/6.824, lectures on
  YouTube) 🆓 — *the* course. Lectures 1–8 and the Raft lectures. The labs (in Go) are
  optional but transformative if you do them (Stage 21 covers Go).
- ⭐ **Martin Kleppmann — Distributed Systems lecture series** (Cambridge, YouTube) 🆓 —
  8 hours that cover Part A beautifully, with free lecture notes.
- ⭐ **CMU 15-445 Intro to Database Systems** (YouTube) 🆓 — the storage, index, join,
  query-execution, concurrency-control and recovery lectures for Part B; then **15-721
  Advanced Database Systems** for MVCC/columnar depth.
- **Raft visualisation** (thesecretlivesofdata.com/raft, raft.github.io) 🆓 — watch before
  reading the paper.
- **Jepsen — "Consistency models" page and analyses** (jepsen.io) 🆓 — what real databases
  actually guarantee, tested to destruction.
- **Aleksey Charapko's paper reading group; Murat Demirbas's blog** 🆓 — for later.

### Books
- ⭐ **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapters 5–9 are Part A;
  chapter 3 is Part B's warm-up. Read every page; take notes.
- ⭐ **Database Internals** (Alex Petrov) 💰 — Part I (storage engines, B-trees, LSM,
  transactions) and Part II (distributed). The Part B book.
- **Distributed Systems** (van Steen & Tanenbaum) 🆓 PDF at distributed-systems.net —
  the textbook; use as a reference.
- **Understanding Distributed Systems** (Vitillo) 💰 — practical, fast read.
- **Architecture of a Database System** (Hellerstein, Stonebraker, Hamilton) 🆓 paper —
  the 100-page overview of how a DBMS is built.
- **Papers** 🆓: *In Search of an Understandable Consensus Algorithm* (Raft), *Paxos Made
  Simple*, *Time, Clocks and the Ordering of Events* (Lamport), *Dynamo*, *Spanner*,
  *Bigtable*, *The Log* (Jay Kreps' blog post), *ARIES* (skim), *Redbook* (readings in
  database systems, redbook.io).

### Practice
- ⭐ **Fly.io Distributed Systems Challenges ("Gossip Glomers")** (fly.io/dist-sys) 🆓 —
  echo → unique IDs → broadcast → grow-only counter → Kafka-style log → totally-available
  transactions. Built on Maelstrom/Jepsen; Python works. Do all of them.
- ⭐ **Build P7 and P8.** Guides for P7: **Build Your Own Database From Scratch** (James
  Smith, free online) 🆓 and **Let's Build a Simple Database** (cstack, SQLite clone in C,
  free) 🆓 — follow the ideas in Python.
- **MIT 6.824 labs** 🆓 (Go) — MapReduce, Raft, KV service on Raft, sharded KV. The gold
  standard if you have the time.
- **Run a real distributed DB** — a 3-node CockroachDB or Cassandra in Docker; kill nodes
  mid-write; read what happens. Read their docs' "architecture" sections.
- **Jepsen reports** — read three; write a summary of what broke and why.

### Reference
- **Jepsen consistency map** 🆓, **Postgres docs "Concurrency Control" and "Reliability
  and the WAL"** 🆓, **etcd/Raft docs**, **Kleppmann's lecture notes PDF** 🆓.

---


---

## Stage 13 — Production infrastructure
*→ [`stages/13_production_infra/`](./stages/13_production_infra/)*

### Courses & videos
- ⭐ **Docker — Get Started guide** (docs.docker.com) 🆓 and **Kubernetes — official
  tutorials + "Kubernetes Basics"** (kubernetes.io) 🆓.
- ⭐ **KodeKloud — Kubernetes for the Absolute Beginners** 💰 (with free labs) or
  **TechWorld with Nana — Kubernetes / Docker / Terraform / Prometheus full courses**
  (YouTube) 🆓 — Nana's are the best free hands-on intros.
- ⭐ **AWS Cloud Practitioner Essentials** (AWS Skill Builder) 🆓 or **Google Cloud
  Fundamentals: Core Infrastructure** 🆓 — the provider's own intro.
- **GitHub Actions docs + "GitHub Actions for CI/CD" (GitHub Skills)** 🆓.
- **HashiCorp Learn — Terraform Get Started** 🆓.
- **Prometheus docs + Grafana tutorials** 🆓; **OpenTelemetry Python getting-started** 🆓.
- **Brendan Gregg — flame graph talks, "Systems Performance" lectures** (YouTube) 🆓.
- **PortSwigger Web Security Academy** 🆓 — the security labs; do Apprentice + Practitioner
  on injection, auth, SSRF.
- **Dan Boneh — Cryptography I** (Coursera) 🆓 — optional, if crypto interests you.

### Books
- ⭐ **Site Reliability Engineering** + **The Site Reliability Workbook** (Google) 🆓
  online — SLOs, monitoring, on-call, postmortems, load balancing, overload.
- ⭐ **Kubernetes Up & Running** (Burns, Beda, Hightower) 💰 — the practical intro.
- **Kubernetes in Action** (Lukša) 💰 — deeper; the best k8s book.
- **Docker Deep Dive** (Poulton) 💰.
- **Observability Engineering** (Majors, Fong-Jones, Miranda) 💰 — modern observability.
- **Prometheus: Up & Running** (Brazil) 💰.
- **Systems Performance** (Brendan Gregg, 2nd ed.) 💰 — the performance bible; chapters
  1–2, 6 (CPUs), 7 (memory), plus the profiling chapters.
- **Continuous Delivery** (Humble & Farley) 💰 or **Accelerate** (Forsgren) 💰 — why CI/CD.
- **Terraform: Up & Running** (Brikman) 💰.
- **Security Engineering** (Ross Anderson) 🆓 online — a reference; dip in.
- **Web Application Security** (Hoffman) 💰; **OWASP Cheat Sheet Series** 🆓.

### Practice
- ⭐ **Deploy P6 and P8** to a real cluster with probes, metrics, dashboards, alerts.
- **killercoda.com / Play with Kubernetes** 🆓 — browser k8s sandboxes.
- **Kubernetes the Hard Way** (Kelsey Hightower) 🆓 — optional, deep.
- **Build P-mini (the profiler)** and view your traces in **Perfetto** 🆓.
- **k6 / locust** load tests against P2; find the bottleneck with py-spy.
- **CTFs:** picoCTF 🆓 for security fundamentals, if you enjoy it.

### Reference
- **`kubectl` cheat sheet** 🆓, **12factor.net**, **OWASP Top 10**, **Brendan Gregg's
  Linux performance tools map**, **Chrome trace-event format doc**, **OpenTelemetry
  semantic conventions**.

---


---

## Stage 14 — ML fundamentals 🧠
*→ [`stages/14_ml_fundamentals/`](./stages/14_ml_fundamentals/)*

### Courses & videos
- ⭐ **3Blue1Brown — Neural Networks series** (YouTube) 🆓 — four videos that give you the
  intuition for everything else. Watch first.
- ⭐ **Andrej Karpathy — Neural Networks: Zero to Hero** (YouTube) 🆓 — build micrograd
  (autograd from scratch), then makemore, then GPT. Type along. This is the spine of
  Stages 14–15.
- ⭐ **fast.ai — Practical Deep Learning for Coders** 🆓 — top-down, code-first, PyTorch.
- **Andrew Ng — Machine Learning Specialization** (Coursera) 🆓 to audit — the classic
  bottom-up course; gentle on math.
- **PyTorch official tutorials — "Learn the Basics" and the 60-minute blitz** 🆓.
- **StatQuest** (YouTube) 🆓 — every ML/stat concept, gently, with songs.
- **Kaggle Learn** (Intro to ML, Intermediate ML, Deep Learning) 🆓 — short, hands-on.

### Books
- ⭐ **Dive into Deep Learning** (d2l.ai) 🆓 — interactive, PyTorch, math explained inline.
  Chapters 1–7.
- **Mathematics for Machine Learning** (Deisenroth et al.) 🆓 PDF — when you want the math
  properly; chapters 2–5 as needed.
- **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow** (Géron) 💰 — the
  practical classic (parts on fundamentals, NNs).
- **Deep Learning with PyTorch** (Stevens, Antiga, Viehmann) 💰 / **Deep Learning with
  PyTorch Step-by-Step** (Godoy) 💰.
- **The Little Book of Deep Learning** (François Fleuret) 🆓 PDF — 160 dense, clear pages.
- **Deep Learning** (Goodfellow, Bengio, Courville) 🆓 online — the reference; not now.

### Practice
- ⭐ **Karpathy's exercises** in each Zero-to-Hero video.
- **Kaggle** 🆓 — Titanic, Digit Recognizer; one tabular and one image competition.
- **Google Colab** 🆓 — free GPU for all of Stages 14–19.

### Reference
- **NumPy / pandas / PyTorch docs**, **Khan Academy** (linear algebra, calculus,
  probability) 🆓 for any math gap, **Papers With Code** for what's state of the art.

---


---

## Stage 15 — Transformers
*→ [`stages/15_transformers/`](./stages/15_transformers/)*

### Courses & videos
- ⭐ **Andrej Karpathy — "Let's build GPT: from scratch, in code, spelled out"** and
  **"Let's build the GPT Tokenizer"** and **"Let's reproduce GPT-2 (124M)"** (YouTube) 🆓 —
  the core of this stage. Type every line.
- ⭐ **3Blue1Brown — "But what is a GPT?" and "Attention in transformers, visually
  explained"** (YouTube) 🆓 — the intuition, beautifully.
- **Karpathy — "Intro to Large Language Models" and "Deep Dive into LLMs like ChatGPT"**
  (YouTube) 🆓 — the whole pipeline (pretraining → SFT → RLHF) in plain language.
- **Hugging Face — LLM Course** (huggingface.co/learn) 🆓 — tokenizers, `transformers`,
  fine-tuning; chapters 1–3, 6.
- **Stanford CS224N** (YouTube) 🆓 — the NLP course; the Transformer and pretraining
  lectures.
- **Stanford CS25 — Transformers United** (YouTube) 🆓 — guest lectures, including
  serving-adjacent ones.

### Books
- ⭐ **Build a Large Language Model (From Scratch)** (Sebastian Raschka) 💰 — exactly this
  stage as a book, PyTorch, meticulously explained.
- **The Illustrated Transformer / Illustrated GPT-2** (Jay Alammar, blog) 🆓 — read
  before and after Karpathy.
- **The Annotated Transformer** (Harvard NLP) 🆓 — the paper with runnable code.
- **Attention Is All You Need** (Vaswani et al.) 🆓 — read it *after* building one.
- **Dive into Deep Learning** ch. 11 (attention & transformers) 🆓.
- **Lilian Weng — "The Transformer Family v2"** (blog) 🆓 — the variants.

### Practice
- ⭐ **nanoGPT** (github.com/karpathy/nanoGPT) 🆓 — train it, then read every line.
- **minbpe** (Karpathy) 🆓 — the tokenizer exercise.
- **Transformer Explainer** (poloclub.github.io/transformer-explainer) 🆓 — interactive.
- **Hugging Face Hub** — run a 0.5B–1B model locally; measure tokens/s.

### Reference
- **Hugging Face `transformers` docs**, **tiktoken**, **the GPT-2 / LLaMA papers** for
  configs, **"Transformer Inference Arithmetic"** (kipp.ly blog) 🆓 — the cost formulas.

---


---

## Stage 16 — GPU fundamentals
*→ [`stages/16_gpus/`](./stages/16_gpus/)*

### Courses & videos
- ⭐ **Horace He — "Making Deep Learning Go Brrrr From First Principles"** (blog) 🆓 —
  compute vs memory vs overhead; read three times.
- ⭐ **GPU MODE** (YouTube lectures + Discord, formerly CUDA MODE) 🆓 — the community
  course working through PMPP with PyTorch/Triton; lectures 1–8.
- **NVIDIA DLI — "Fundamentals of Accelerated Computing with CUDA Python"** 💰 (often
  free vouchers) or **"An Even Easier Introduction to CUDA"** (NVIDIA blog) 🆓.
- **Triton tutorials** (triton-lang.org) 🆓 — vector add, fused softmax, matmul.
- **"How GPU Computing Works" (NVIDIA GTC talk, Stephen Jones)** (YouTube) 🆓 — the best
  single hour on the topic.
- **Chips and Cheese** (blog) 🆓 — microarchitecture deep dives, for the curious.

### Books
- ⭐ **Programming Massively Parallel Processors** (Kirk & Hwu, 4th ed.) 💰 — the GPU
  textbook; chapters 1–6.
- **CUDA C++ Programming Guide** (NVIDIA) 🆓 — reference; the "Programming Model" and
  "Hardware Implementation" chapters.
- **"What Every Programmer Should Know About Memory"** (Drepper) 🆓 — parts 1–3 for the
  memory-hierarchy mindset.
- **"Transformer Inference Arithmetic"** (kipp.ly) 🆓 and **"How to Scale Your Model"**
  (Google DeepMind, jax-ml.github.io/scaling-book) 🆓 — parts 1–2 on rooflines and
  hardware; the rest in Stage 19.

### Practice
- ⭐ **Colab / Kaggle GPUs** 🆓 — everything here runs on a free T4.
- **LeetGPU / Tensara** 🆓 — kernel-writing practice problems.
- **`torch.profiler` + TensorBoard / Perfetto** 🆓.

### Reference
- **NVIDIA GPU spec sheets** (memory, bandwidth, FLOPs), **`nvidia-smi` docs**,
  **PyTorch CUDA semantics page**.

---


---

## Stage 17 — LLM inference 🚨🚨
*→ [`stages/17_llm_inference/`](./stages/17_llm_inference/)*

### Courses & videos
- ⭐ **vLLM docs + "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention"
  (blog)** 🆓 — read the architecture docs; run it.
- ⭐ **Databricks — "LLM Inference Performance Engineering: Best Practices"** (blog) 🆓 —
  the metrics, explained by people who serve at scale.
- **Anyscale — "How continuous batching enables 23× throughput"** (blog) 🆓.
- **Hugging Face — Text Generation Inference docs, "LLM inference optimisation" guide** 🆓.
- **NVIDIA — "Mastering LLM Techniques: Inference Optimization"** (blog) 🆓.
- **GPU MODE — inference/serving lectures** (YouTube) 🆓.
- **Baseten, Modal, Character.AI, Anyscale engineering blogs on serving** 🆓.
- **Full Stack Deep Learning / "LLM Bootcamp"** (YouTube) 🆓 — the deployment lectures.

### Books & papers
- ⭐ **Lilian Weng — "Large Transformer Model Inference Optimization"** (blog) 🆓 — the
  survey to read first.
- ⭐ **Efficient Memory Management for LLM Serving with PagedAttention** (vLLM paper) 🆓.
- **Orca: A Distributed Serving System for Transformer-Based Generative Models** 🆓 —
  continuous batching's origin.
- **"Towards Efficient Generative LLM Serving: A Survey"** 🆓 — the map of the field.
- **Designing Machine Learning Systems** (Chip Huyen) 💰 — chapter 7 (deployment) and the
  ML-infra mindset.
- **AI Engineering** (Chip Huyen) 💰 — the inference-optimisation chapter.
- **Anthropic and OpenAI API docs** (streaming, rate limits, usage) 🆓 — the product
  shape you'd be building.

### Practice
- ⭐ **Build P9.**
- **Run vLLM/SGLang locally or on Colab**; hit it with a load generator (`locust`, or
  vLLM's `benchmark_serving.py`); plot latency vs throughput.
- **Ollama / llama.cpp** 🆓 — inspect a simpler serving loop.

### Reference
- **MDN Server-Sent Events**, **vLLM engine args and metrics docs**, **OpenTelemetry
  GenAI semantic conventions**, **`sse-starlette`**.

---


---

## Stage 18 — Batching, KV cache and inference scheduling 🚨🚨
*→ [`stages/18_batching_kvcache_scheduling/`](./stages/18_batching_kvcache_scheduling/)*

### Courses & videos
- ⭐ **vLLM source: `core/scheduler.py`, block manager, prefix caching** (GitHub) 🆓 — read
  it with the paper open; it's the reference implementation of this stage.
- ⭐ **SGLang docs + RadixAttention paper/blog** 🆓 — prefix caching done right.
- **Anyscale — continuous batching blog**; **Character.AI — "Optimizing AI Inference"**
  (blog) 🆓 — real KV-cache and prefix-sharing numbers.
- **NVIDIA TensorRT-LLM docs — in-flight batching, paged KV, scheduling policies** 🆓.
- **GPU MODE — vLLM / serving lectures** (YouTube) 🆓.
- **Kubernetes GPU autoscaling docs (KEDA, HPA custom metrics)** 🆓; **Ray Serve docs**
  (autoscaling on queue length) 🆓.

### Papers 🆓 (read the ideas; skim the evals)
- ⭐ **Orca** (OSDI '22) — continuous (iteration-level) batching.
- ⭐ **PagedAttention / vLLM** (SOSP '23) — paged KV cache.
- **SGLang / RadixAttention** — prefix caching as a radix tree.
- **Sarathi-Serve** (OSDI '24) — chunked prefill, stall-free scheduling.
- **DistServe / Splitwise** — disaggregated prefill and decode.
- **Llumnix** — request rescheduling across instances.
- **FastServe / "Fairness in Serving LLMs" (VTC)** — preemptive and fair scheduling.
- **"Efficiently Scaling Transformer Inference"** (Pope et al.) — the cost model.

### Books
- **Designing Data-Intensive Applications** — revisit ch. 11 (streams) and 8 (failure);
  **Release It!** — revisit stability patterns for the failure module.
- **AI Engineering** (Chip Huyen) 💰 — inference optimisation chapter.

### Practice
- ⭐ **Build P10** — the simulator is the practice.
- **vLLM `benchmark_serving.py`** on a real model: sweep max-num-seqs and chunked-prefill
  settings; watch the metrics move; explain why.
- **Design drills:** the inference-API design question, out loud, weekly.

### Reference
- **vLLM engine args (scheduler-related)**, **SGLang server args**, **Stage 15 cost
  calculator**, **Stage 16 roofline notebook**.

---


---

## Stage 19 — Distributed / multi-GPU inference and optimization
*→ [`stages/19_multi_gpu_inference/`](./stages/19_multi_gpu_inference/)*

### Courses & videos
- ⭐ **Hugging Face — "The Ultra-Scale Playbook: Training LLMs on GPU Clusters"** 🆓 —
  the clearest walk-through of every parallelism and every collective, with numbers
  (it's about training; the parallelism and communication chapters apply directly).
- ⭐ **"How to Scale Your Model"** (Google DeepMind, jax-ml.github.io/scaling-book) 🆓 —
  parts on inference, sharding and collectives; systems-level and rigorous.
- **GPU MODE — NCCL / distributed / FlashAttention / quantisation lectures** (YouTube) 🆓.
- **NVIDIA — NCCL docs and "Doubling all2all performance" style blogs** 🆓.
- **vLLM / SGLang / TensorRT-LLM docs on tensor & pipeline parallel serving,
  quantisation, speculative decoding** 🆓.
- **Lilian Weng — inference optimisation post** (revisit) 🆓.

### Papers 🆓
- ⭐ **Megatron-LM** (tensor parallelism) and **GPipe** (pipeline parallelism).
- ⭐ **Efficiently Scaling Transformer Inference** (Pope et al.) — the inference partitioning
  cost model.
- **FlashAttention 1/2** — why attention is memory-bound and how to fix it.
- **Fast Inference from Transformers via Speculative Decoding** (Leviathan) and
  **Medusa / EAGLE**.
- **GPTQ**, **AWQ**, **SmoothQuant**, **LLM.int8()** — quantisation.
- **DistServe / Splitwise / Mooncake** — disaggregated serving and KV transfer.
- **DeepSpeed-Inference / ZeRO-Inference** — offloading.

### Books
- **Programming Massively Parallel Processors** — the remaining chapters.
- **AI Engineering** (Huyen) 💰 — optimisation chapter, revisited.

### Practice
- ⭐ **Extend P10** to a multi-GPU simulation (TP groups, PP stages, replica routing,
  collective costs from a bandwidth model).
- **Rent 2 GPUs for an afternoon** (Lambda, RunPod, Vast) 💰 — run vLLM with TP=2; measure
  vs TP=1; run a NCCL all-reduce benchmark.
- **Quantise a model** with AWQ/GPTQ or bitsandbytes; measure memory, throughput, quality.
- **Run speculative decoding** in vLLM/SGLang; sweep the draft model; plot acceptance rate
  vs speedup.

### Reference
- **NCCL docs**, **NVIDIA interconnect spec sheets**, **vLLM distributed serving docs**,
  **Hugging Face quantisation docs**.

---


---

## Stage 20 — Mock interviews: behavioral, communication, the full loops
*→ [`stages/20_mock_interviews/`](./stages/20_mock_interviews/)*

### Courses & videos
- ⭐ **Anthropic Careers — interview guide / "how we hire"** and **OpenAI's interview
  guides** 🆓 — read the actual source.
- ⭐ **Hello Interview** 🆓/💰 — system-design walkthroughs and paid mocks with engineers.
- **interviewing.io** 💰 (some free peer mocks) and **Pramp/Exponent peer mocks** 🆓.
- **Jackson Gabbard — "Behavioral interviews for software engineers"** (YouTube) 🆓.
- **Tech Interview Handbook — behavioral section** 🆓.
- **ByteByteGo / Jordan has no life** — one design a week, watched *after* you attempt it.

### Books
- ⭐ **System Design Interview Vol. 1 & 2** (Alex Xu) 💰 — the drill book.
- ⭐ **Cracking the Coding Interview** (McDowell) 💰 — the process chapters + behavioral prep.
- **The Staff Engineer's Path** (Tanya Reilly) 💰 — judgment, trade-offs, "simplest thing";
  reads like a hiring-manager round.
- **The Pragmatic Programmer** (Hunt & Thomas) 💰 — how good engineers think; quotable.
- **A Philosophy of Software Design** (Ousterhout) 💰 — complexity and simplicity, the
  argument the hiring manager wants to hear.
- **Anthropic's "Core Views on AI Safety", the Responsible Scaling Policy, Claude's
  constitution, and the engineering blog** 🆓 — to answer "why Anthropic" and the
  safety round with substance.
- **Hello Interview — behavioral guide** 🆓.

### Practice
- ⭐ **`LEETCODE.md` Phase C, all of it, cold and timed.**
- ⭐ **Weekly recorded inference-API design.**
- **Write your STAR stories in `notes/stories.md`.**
- **AI as interviewer:** give Claude/ChatGPT the rubric ("you are a senior engineer;
  probe every decision; interrupt with failures") and run designs against it between
  human mocks.

### Reference
- **Latency numbers**, **your Stage 15 cost calculator**, **your `DESIGN.md`s**, the
  round tables in `ROADMAP.md`.

---


---

## Cross-cutting

- **`LEETCODE.md`** — the practice plan and problem lists.
- **`LEARNING_GUIDE.md`** — how to use all of this without drowning.
- **`AI_TUTOR.md`** — using Claude/ChatGPT as a tutor, not a crutch.
- **`YEAR_ONE_JOB.md`** — the first job, the résumé, referrals.
- **Anthropic and OpenAI careers pages / interview guides** 🆓 — the primary sources on the loops.
- **Google's Engineering Practices (code review guide)** 🆓 — read once in Stage 04, again in Stage 20.
- **Newsletters:** ByteByteGo 🆓, The Pragmatic Engineer 🆓/💰, Interconnects 🆓, SemiAnalysis 🆓/💰 (GPU economics), Latent Space 🆓.
- **Communities:** Python Discord, GPU MODE Discord, MLOps Community, r/learnprogramming, r/ExperiencedDevs.
