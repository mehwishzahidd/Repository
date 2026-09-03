# Stage 03 — Data Structures & Algorithms

> **Roadmap Groups 2 & 34 · a major interview category.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

This is the heart of coding interviews and the language everything later is written in. Trees are file systems, graphs are task dependencies, hash maps are caches. Learn to *implement* the important ones yourself, not just call them.

**Prerequisite:** Stage 02 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Complexity first
Big-O · time & space · amortized · best/average/worst · reason O(1)/O(log n)/O(n)/O(n log n)/O(n²) by reading code

### Arrays & strings
two pointers · sliding window · prefix sums · parsing · string building · normalization

### Hash maps & sets
hashing & collisions (conceptually) · frequency counting · dedupe · O(1) lookup

### Stack, queue, deque
monotonic stack · parentheses · BFS with a queue · task queues

### Linked lists
singly & doubly · pointer surgery · **LRU cache = hash map + doubly linked list, all O(1)**

### Trees & heaps
binary trees · BSTs · pre/in/post/level order, recursive *and* iterative · tries · heaps / priority queues

### Graphs (very important)
adjacency list/matrix · directed/undirected/weighted · **DAGs** · BFS · DFS · **topological sort** · **cycle detection** · Dijkstra · connected components · Union-Find; later SCCs, MST

### Patterns
sorting · binary search · recursion · backtracking · greedy · divide & conquer · intervals · dynamic programming · bit manipulation basics

### Systems-style problems (Group 34)
rate limiter · worker pool · job queue · log parser · in-memory KV store — algorithms *plus* engineering

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Implement an LRU cache from scratch and explain why get/put/evict are all O(1).
- [ ] Given tasks with dependencies, produce a valid order or report the cycle (`A → B → C → A`), then add priorities, worker assignment and cascading cancellation.
- [ ] Solve ~100 mixed LeetCode-style problems (easy → medium) and analyse each one's complexity out loud.
- [ ] Implement BFS, DFS, topological sort, Dijkstra and Union-Find without notes.

## 🛠️ Project

**LRU cache v1** (single-threaded) and a **dependency resolver** — these become P5 and P4 later.

## 📚 Free resources

- NeetCode 150 roadmap (free) · *Grokking Algorithms* (Bhargava) for intuition
- *Algorithms* (Sedgewick) or CLRS for depth · MIT 6.006 lectures (free)
- LeetCode / HackerRank for practice

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 04"** to get its hands-on lessons built.
