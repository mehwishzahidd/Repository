# Stage 03 — Data Structures & Algorithms

> **Roadmap Groups 2 & 34.** The heart of coding interviews, and the language every
> later stage is written in. Trees are file systems, graphs are task dependencies, hash
> maps are caches, heaps are schedulers.

## If you're new to this

A **data structure** is a way of organising data so certain operations are fast. An
**algorithm** is a step-by-step recipe. **Big-O** is how we describe "how much slower
does this get as the input grows". That's the whole subject. It looks mathematical, but
for interviews it's mostly about recognising ~15 patterns and having implemented the
core structures yourself once.

This stage is paired with [`LEETCODE.md`](../../LEETCODE.md) Phase B. The book/course
teaches the idea; LeetCode makes it reflex.

**Time:** 10–14 weeks at ~10–12 hours/week. This is the longest early stage; that's normal.

**Prerequisites:** Stage 02 checkpoint (classes, recursion-ready functions, pytest).

---

## Modules (in order — each maps to a LeetCode pattern)

1. **Complexity** — Big-O, time vs space, best/average/worst, amortized (why
   `list.append` is O(1) "on average"). Practise: look at any function and name its
   complexity. Know the common classes: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ).
2. **Arrays & strings** — how Python lists work under the hood (dynamic arrays,
   resizing), two pointers, sliding window, prefix sums, in-place tricks, string
   building (why `''.join` beats `+=`).
3. **Hashing** — how a hash map works (hash function → bucket, collisions, load factor),
   why lookup is O(1), frequency counting, dedupe, "have I seen this?" problems.
   Implement a tiny hash map yourself once.
4. **Stacks & queues** — implement both; parentheses matching, monotonic stack, the
   call stack (recursion *is* a stack), `deque` as a queue, BFS needs a queue.
5. **Linked lists** — singly & doubly, implement from scratch, reversal, cycle
   detection, dummy-head trick, pointer surgery. **Then the LRU cache: hash map +
   doubly linked list, all O(1).** Do it with `OrderedDict` first, then by hand.
6. **Recursion** — base case + recursive case, call-stack visualisation, recursion vs
   iteration, memoisation (`lru_cache`). Everything in trees/graphs/backtracking/DP is
   recursion.
7. **Sorting & searching** — how merge sort and quick sort work (implement both once),
   why O(n log n) is the floor for comparison sorts, `sorted(key=…)`, binary search and
   its "search the answer space" variant.
8. **Trees** — binary trees, BSTs, the four traversals (pre/in/post/level), recursive
   *and* iterative versions, height/depth/diameter, lowest common ancestor,
   serialisation. **Tries** for prefix problems. **Heaps / priority queues** (`heapq`):
   top-k, merge k lists, schedulers.
9. **Graphs (the most important module for these interviews)** — adjacency list vs
   matrix, directed/undirected/weighted, **BFS** (shortest path in unweighted graphs,
   the crawler), **DFS**, connected components, **cycle detection**, **topological sort**
   (Kahn's and DFS-based), **DAGs**, Dijkstra, Union-Find. Then: the task-system problem
   in full (priorities, worker assignment, dependencies, cascading cancellation).
10. **Backtracking** — subsets, permutations, combinations, N-queens, word search;
    the "choose → explore → un-choose" template.
11. **Greedy & intervals** — when greedy works (and how to argue it), merging intervals,
    meeting rooms, scheduling.
12. **Dynamic programming** — memoisation → tabulation, 1-D then 2-D, the classic
    families (climbing stairs, coin change, LIS, LCS, knapsack, edit distance). Learn to
    *recognise* DP: overlapping subproblems + optimal substructure.
13. **Bit manipulation basics** — AND/OR/XOR/shifts, checking/setting bits, XOR tricks.
14. **Systems-style problems (Group 34)** — rate limiter, worker pool, job queue, log
    parser, in-memory KV store, tiny file system. Algorithms *plus* engineering: these
    are what the real OA looks like.

---

## 📚 Resources

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

## Practice & exercises (implement from scratch, with tests)
- Dynamic array, hash map (with chaining), stack, queue, singly and doubly linked list.
- BST with insert/search/delete and all four traversals; a min-heap; a trie.
- Graph class with BFS, DFS, topological sort (both ways), cycle detection, Dijkstra,
  Union-Find.
- Merge sort, quick sort, binary search (iterative and recursive).
- **LRU cache** three ways: `OrderedDict`, from scratch, then with capacity/edge-case
  handling and tests (capacity 0, duplicate puts, get on missing key).
- **Task system:** tasks with priorities and dependencies; `add`, `complete`,
  `cancel` (cascading), `next_runnable(worker)`; rejects cycles.
- A **rate limiter** (fixed window, then sliding window) and a **log parser** that
  aggregates per-endpoint p50/p99 from a text file.
- **The profiler-to-trace converter** (P-mini in `PROJECTS.md`): it's only stacks and
  careful bookkeeping, so build it *now*, not in Stage 13. Recursion by position, not name.
- **The Anthropic drill**, weekly from week 6: solve a problem, then add three requirements
  yourself (empty/zero/duplicates · two threads · fails halfway) and refactor without
  rewriting. See `LEETCODE.md` rule 8.

## Beginner pitfalls
- **Memorising solutions.** If you can't explain *why* it works, you didn't learn it.
- **Jumping to hards.** Mediums are the interview. Hards are extra credit.
- **Skipping the from-scratch implementations.** The OA asked for the LRU *by hand*.
- **Not analysing complexity.** Say it out loud for every problem, every time.
- **Fear of recursion.** Draw the call stack on paper for three problems and it clicks.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You can implement an LRU cache from scratch and explain why get/put/evict are O(1).
- [ ] Given tasks with dependencies, you produce a valid order or report the cycle, then
      add priorities, worker assignment and cascading cancellation.
- [ ] You've solved ~120–150 problems from `LEETCODE.md` Phase B, mediums included, with
      the redo rule applied, and can talk through complexity for each.
- [ ] You implement BFS, DFS, topological sort, Dijkstra and Union-Find without notes.
- [ ] You can look at unfamiliar code and state its time and space complexity.
- [ ] You've solved two mediums in 45 minutes, timed, while narrating aloud.
- [ ] P-mini (profiler samples → trace events) passes its tests, including recursion.

## 🛠️ Project
**LRU cache v1**, the **task-system / dependency resolver** (P4's core) and **P-mini, the
profiler-to-trace converter** — all with tests and READMEs. LRU and the task system get
concurrency in Stage 09.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 04"** to get its hands-on lessons built.
