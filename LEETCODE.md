# 🧩 LEETCODE — the practice plan

LeetCode is where DSA knowledge becomes interview reflex. It is **not** where you learn
DSA — that's Stage 03 with a book/course. It's also not the whole prep: the interview
loops in `ROADMAP.md` are mostly *build-a-system* coding, not puzzle coding. But every
round starts from the same reflexes (hash maps, BFS, heaps, linked-list surgery) and this
is how you build them.

🔒 = LeetCode Premium problem. NeetCode.io hosts free versions of most, and LintCode
mirrors the rest. You do not need Premium to follow this plan.

---

## How to practise (this matters more than which problems)

1. **Timebox.** 25 minutes on a medium, 15 on an easy. If you're stuck at the limit,
   read the *approach* (not the code), close it, and implement it yourself.
2. **The 3-attempt rule.** Every problem you couldn't solve goes on a "redo" list. Redo it
   from a blank editor after 2 days, then 1 week, then 1 month. A problem is "done" only
   when you've solved it cold three times.
3. **Say the complexity out loud** before you submit. Every time. Interviewers ask.
4. **Talk while you code.** Practise narrating: "I'll use a hash map to get O(1) lookup…
   the edge case is an empty list…". This is half of what's graded live.
5. **Patterns, not problems.** Learn the 15 patterns below; then any new problem is
   "which pattern is this?" not "have I seen this exact one?".
6. **Python idioms to know cold:** `collections.deque`, `Counter`, `defaultdict`,
   `heapq`, `bisect`, `sorted(key=lambda…)`, list/dict comprehensions, `enumerate`,
   `zip`, slicing, `functools.lru_cache` for memoised recursion.
7. **Quantity:** ~150 well-chosen problems solved *properly* (rule 2) beats 500 done once.
8. **The Anthropic drill (from Stage 03, week 6 on).** After every accepted solution, add
   three requirements yourself and refactor *without rewriting*:
   - "Capacity is 0 / input is empty / duplicates exist" — what changes?
   - "Two threads call this at once" — reason about it now; implement it in Stage 09.
   - "An operation can fail halfway — what state are you left in?"
   Then state time and space complexity, list three edge cases, and write it the way you'd
   ship it: names, small helpers, a docstring. The OA is graded on code quality and on how
   well your solution survives "now add X", not on acceptance alone.
9. **Before any real interview:** a 4-week ramp at one problem a day from that company's
   tagged list, plus the Phase C set redone cold.

Free resources: **NeetCode.io** (roadmap + video for every problem below, 🆓),
**Tech Interview Handbook** grind list (🆓), LeetCode itself (🆓 for most problems).
Paid, optional: LeetCode Premium 💰 (company tags, locked problems), AlgoExpert 💰.

---

## Phase A — after Stage 01/02: get comfortable (2–3 weeks, easies only)

Goal: stop fighting syntax. 20–30 easy problems. Don't worry about optimal solutions yet.

Two Sum (1) · Valid Anagram (242) · Contains Duplicate (217) · Valid Palindrome (125) ·
Reverse Linked List (206) · Merge Two Sorted Lists (21) · Valid Parentheses (20) ·
Best Time to Buy and Sell Stock (121) · Maximum Subarray (53) · Climbing Stairs (70) ·
Binary Search (704) · Invert Binary Tree (226) · Maximum Depth of Binary Tree (104) ·
Same Tree (100) · Linked List Cycle (141) · Plus One (66) · Missing Number (268) ·
Number of 1 Bits (191) · Happy Number (202) · Fizz Buzz (412) · Roman to Integer (13) ·
Palindrome Number (9) · Move Zeroes (283) · Majority Element (169) · Min Stack (155) ·
First Bad Version (278) · Squares of a Sorted Array (977) · Ransom Note (383) ·
Isomorphic Strings (205) · Intersection of Two Arrays (349) · Pascal's Triangle (118) ·
Length of Last Word (58) · Remove Duplicates from Sorted Array (26) · Reverse String (344)

Need more? LeetCode's "Top Interview 150" list, filtered to Easy.

---

## Phase B — during Stage 03: the patterns (8–12 weeks, this is the core)

Work pattern by pattern in this order, matching the Stage 03 modules. This is
essentially the NeetCode 150 / Blind 75 ordering, chosen because it builds each idea
on the previous one. Do the easies, then mediums; hards are marked and optional
until you're solid.

### 1 · Arrays & hashing
Two Sum (1) · Contains Duplicate (217) · Valid Anagram (242) · Group Anagrams (49) ·
Top K Frequent Elements (347) · Product of Array Except Self (238) ·
Valid Sudoku (36) · Encode and Decode Strings (271 🔒) · Longest Consecutive Sequence (128)

### 2 · Two pointers
Valid Palindrome (125) · Two Sum II (167) · 3Sum (15) · Container With Most Water (11) ·
Trapping Rain Water (42, hard)

### 3 · Sliding window
Best Time to Buy and Sell Stock (121) · Longest Substring Without Repeating Characters (3) ·
Longest Repeating Character Replacement (424) · Permutation in String (567) ·
Minimum Window Substring (76, hard) · Sliding Window Maximum (239, hard)

### 4 · Stack
Valid Parentheses (20) · Min Stack (155) · Evaluate Reverse Polish Notation (150) ·
Generate Parentheses (22) · Daily Temperatures (739) · Car Fleet (853) ·
Largest Rectangle in Histogram (84, hard) · **Simplify Path (71)** · **Decode String (394)** ·
**Basic Calculator II (227)** · **Asteroid Collision (735)**

### 5 · Binary search
Binary Search (704) · Search a 2D Matrix (74) · Koko Eating Bananas (875) ·
Find Minimum in Rotated Sorted Array (153) · Search in Rotated Sorted Array (33) ·
**Time Based Key-Value Store (981)** · Median of Two Sorted Arrays (4, hard)

### 6 · Linked list
Reverse Linked List (206) · Merge Two Sorted Lists (21) · Reorder List (143) ·
Remove Nth Node From End (19) · Copy List with Random Pointer (138) · Add Two Numbers (2) ·
Linked List Cycle (141) · Find the Duplicate Number (287) · **LRU Cache (146)** ·
Merge K Sorted Lists (23, hard) · Reverse Nodes in k-Group (25, hard)

### 7 · Trees
Invert Binary Tree (226) · Maximum Depth (104) · Diameter of Binary Tree (543) ·
Balanced Binary Tree (110) · Same Tree (100) · Subtree of Another Tree (572) ·
Lowest Common Ancestor of a BST (235) · Level Order Traversal (102) ·
Binary Tree Right Side View (199) · Count Good Nodes (1448) · Validate BST (98) ·
Kth Smallest Element in a BST (230) · Construct Tree from Preorder and Inorder (105) ·
Binary Tree Maximum Path Sum (124, hard) · Serialize and Deserialize Binary Tree (297, hard)

### 8 · Tries
Implement Trie (208) · Design Add and Search Words (211) · Word Search II (212, hard)

### 9 · Heap / priority queue
Kth Largest Element in a Stream (703) · Last Stone Weight (1046) · K Closest Points (973) ·
Kth Largest Element in an Array (215) · **Task Scheduler (621)** · **Design Twitter (355)** ·
Find Median from Data Stream (295, hard)

### 10 · Backtracking
Subsets (78) · Combination Sum (39) · Permutations (46) · Subsets II (90) ·
Combination Sum II (40) · Word Search (79) · Palindrome Partitioning (131) ·
Letter Combinations of a Phone Number (17) · N-Queens (51, hard)

### 11 · Graphs — the big one for these interviews
Number of Islands (200) · Clone Graph (133) · Max Area of Island (695) ·
Pacific Atlantic Water Flow (417) · Surrounded Regions (130) · Rotting Oranges (994) ·
Walls and Gates (286 🔒) · **Course Schedule (207)** · **Course Schedule II (210)** ·
Redundant Connection (684) · Number of Connected Components (323 🔒) ·
Graph Valid Tree (261 🔒) · Word Ladder (127, hard)

**Advanced graphs:** Reconstruct Itinerary (332) · Min Cost to Connect All Points (1584) ·
Network Delay Time (743, Dijkstra) · Swim in Rising Water (778) · Alien Dictionary (269 🔒) ·
Cheapest Flights Within K Stops (787) · Accounts Merge (721, union-find) ·
Evaluate Division (399) · Minimum Height Trees (310)

### 12 · Dynamic programming
**1-D:** Climbing Stairs (70) · Min Cost Climbing Stairs (746) · House Robber (198) ·
House Robber II (213) · Longest Palindromic Substring (5) · Palindromic Substrings (647) ·
Decode Ways (91) · Coin Change (322) · Maximum Product Subarray (152) · Word Break (139) ·
Longest Increasing Subsequence (300) · Partition Equal Subset Sum (416)
**2-D:** Unique Paths (62) · Longest Common Subsequence (1143) ·
Best Time to Buy and Sell Stock with Cooldown (309) · Coin Change II (518) · Target Sum (494) ·
Interleaving String (97) · Longest Increasing Path in a Matrix (329) · Edit Distance (72) ·
Distinct Subsequences (115, hard) · Burst Balloons (312, hard) · Regular Expression Matching (10, hard)

### 13 · Greedy
Maximum Subarray (53) · Jump Game (55) · Jump Game II (45) · Gas Station (134) ·
Hand of Straights (846) · Partition Labels (763) · Valid Parenthesis String (678)

### 14 · Intervals
Insert Interval (57) · Merge Intervals (56) · Non-overlapping Intervals (435) ·
Meeting Rooms (252 🔒) · Meeting Rooms II (253 🔒) · Minimum Interval to Include Each Query (1851, hard)

### 15 · Math & bit manipulation
Rotate Image (48) · Spiral Matrix (54) · Set Matrix Zeroes (73) · Pow(x, n) (50) ·
Multiply Strings (43) · Single Number (136) · Counting Bits (338) · Reverse Bits (190) ·
Sum of Two Integers (371) · Reverse Integer (7)

---

## Phase C — Stage 09 onwards: the problems that look like the actual interviews

These map directly onto the rounds in `ROADMAP.md`. Do them when you reach the stage
that teaches the concept; redo them all in Stage 20.

### The LRU / cache round
LRU Cache (146) — then from scratch with your own doubly linked list, then thread-safe ·
LFU Cache (460, hard) · Time Based Key-Value Store (981) · Insert Delete GetRandom O(1) (380) ·
Design Hit Counter (362 🔒) · Logger Rate Limiter (359 🔒) · Number of Recent Calls (933) ·
Design Authentication Manager (1797) · Snapshot Array (1146 — a taste of MVCC) ·
Design Memory Allocator (2502 — a taste of KV-cache allocation) ·
Design HashSet (705) / Design HashMap (706) — build the thing under the dict ·
Design Circular Queue (622)

### The task-system / DAG round
Course Schedule (207) · Course Schedule II (210) · Parallel Courses (1136 🔒) ·
Parallel Courses III (2050 — critical path with durations) · Find All Possible Recipes (2115) ·
Sequence Reconstruction (444 🔒) · Alien Dictionary (269 🔒) · Task Scheduler (621) ·
**Kill Process (582 🔒 — this is cascading cancellation)** · Minimum Height Trees (310) ·
**Single-Threaded CPU (1834)** and **Process Tasks Using Servers (1882)** — priority
scheduling with a heap, exactly the worker-assignment shape · Find Eventual Safe States
(802 — cycle detection)

### The web-crawler round
Web Crawler (1236 🔒) · **Web Crawler Multithreaded (1242 🔒)** · Clone Graph (133) ·
Word Ladder (127) · Rotting Oranges (994) · Shortest Path in Binary Matrix (1091) — all
BFS with visited-sets, the crawler's skeleton · Simplify Path (71) and Remove Sub-Folders
from the Filesystem (1233) — path/URL normalization

### The profiler / call-stack round
**Exclusive Time of Functions (636 — this *is* the profiler problem)** ·
Basic Calculator (224, hard) · Basic Calculator II (227) · Simplify Path (71) ·
Decode String (394) · Asteroid Collision (735) · Daily Temperatures (739) ·
Dinner Plate Stacks (1172, hard) · Flatten Nested List Iterator (341)

### The in-memory database round
**Design SQL (2408 🔒)** · Design In-Memory File System (588 🔒) · Design File System (1166 🔒) ·
Design Log Storage System (635 🔒) · Range Module (715, hard) · Snapshot Array (1146) ·
Design a Text Editor (2296, hard) · Stock Price Fluctuation (2034)

### Rate limiting / intervals / streams
Meeting Rooms II (253 🔒) · Merge Intervals (56) · Employee Free Time (759 🔒, hard) ·
Find Median from Data Stream (295) · Sliding Window Maximum (239) · Stock Price
Fluctuation (2034) · Car Pooling (1094) · Number of Recent Calls (933)

### Concurrency problems (LeetCode's own "Concurrency" tag — do every one)
Print in Order (1114) · Print FooBar Alternately (1115) · Print Zero Even Odd (1116) ·
Building H2O (1117) · Fizz Buzz Multithreaded (1195) · The Dining Philosophers (1226) ·
Design Bounded Blocking Queue (1188 🔒) · Traffic Light Controlled Intersection (1279 🔒) ·
Web Crawler Multithreaded (1242 🔒) — once with threads, once with asyncio

Then, beyond LeetCode: implement a **thread-safe LRU**, a **bounded worker pool**, a
**token-bucket rate limiter**, and a **read-write lock** from scratch, with stress tests.

### Other "design a system" problems worth doing
Design Twitter (355) · Design Underground System (1396) · Design Browser History (1472) ·
Design a Leaderboard (1244 🔒) · Design Circular Queue (622) · Encode and Decode TinyURL (535) ·
Design Search Autocomplete System (642 🔒, hard) · Tweet Counts Per Frequency (1348) ·
Design Movie Rental System (1912, hard) · Implement Trie (208)

---

## Phase D — maintenance and hards (Stages 14 onward)

Two problems a week: one random medium from NeetCode 250, and every other week one
hard from this list: Merge K Sorted Lists (23) · Trapping Rain Water (42) · Median of Two
Sorted Arrays (4) · Serialize and Deserialize N-ary Tree (428 🔒) · Minimum Window
Substring (76) · Longest Valid Parentheses (32) · Regular Expression Matching (10) · Word
Ladder II (126) · Alien Dictionary (269 🔒) · Sliding Window Median (480). Redo three
starred Phase C problems cold each month.

Extra pattern lists if you want them: **Sean Prashad's LeetCode Patterns** 🆓 and
**AlgoMonster** 💰.

---

## Weekly cadence

| Stage you're in | LeetCode load |
|---|---|
| 01–02 | Phase A: 3–4 easies a week, once the lessons are done |
| 03 | Phase B: 1 pattern a week, ~8–12 problems, plus redo list |
| 04–08 | Maintenance: 3 problems a week from the redo list + one new medium |
| 09–13 | Phase C for the current stage + 2 maintenance problems a week |
| 14–19 | Maintenance: 2 a week, don't lose the reflexes |
| 20 | Timed: one full mock (2 mediums in 45 min) + all of Phase C, redone cold |

Track it in `PROGRESS.md` or a `notes/leetcode.md` with columns: problem · pattern ·
attempts · last solved cold. That redo list is your most valuable file.

> Reminder: the Anthropic OA is 90 minutes for *two* build-a-system problems, and the
> loop's coding rounds are engineering problems, not puzzles. LeetCode builds the
> reflexes; `PROJECTS.md` builds the rest. Do both.
