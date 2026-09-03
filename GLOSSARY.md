# 📖 GLOSSARY — the scary words, in plain English

Every term below sounded like ancient runes to someone once. Each entry says what it
means in one or two plain sentences, and which stage makes it *actually* click. Don't
memorize this page; come back to it whenever a word in the roadmap makes your brain go
"girl WHAT".

| Term | Plain English | Click in |
|---|---|---|
| **Programming** | Writing precise instructions a computer follows exactly, step by step. | 01 |
| **Variable** | A named box you store a value in so you can use it later. | 01 |
| **Function** | A named, reusable chunk of instructions you can call with inputs and get an output back. | 01 |
| **Class / object** | A blueprint (class) for things that bundle data and behaviour together; an object is one thing made from the blueprint. | 02 |
| **API** | A defined way for one program to ask another program to do something. A menu of things you're allowed to request. | 06 |
| **Server / client** | A server is a program that waits for requests; a client is the program that sends them. Your browser is a client; a website runs on a server. | 06, 07 |
| **Database** | A program whose whole job is storing data safely and finding it fast. | 05 |
| **SQL** | The language you use to ask a relational database questions. | 05 |
| **Data structure** | A particular way of organising data in memory so certain operations are fast (lists, dictionaries, trees, graphs). | 03 |
| **Algorithm** | A step-by-step recipe for solving a problem, e.g. for sorting or searching. | 03 |
| **Big-O** | A way to describe how the time (or memory) a piece of code needs grows as the input gets bigger. | 03 |
| **Hash map / dictionary** | A structure that stores key → value pairs and finds any key almost instantly. | 03 |
| **Linked list** | A chain of items where each one points to the next. Cheap to insert/remove in the middle. | 03 |
| **Tree** | Data organised like a family tree: one root, branches, leaves. Folders on your computer are a tree. | 03 |
| **Graph** | Dots (nodes) connected by lines (edges). Cities and roads, people and friendships, tasks and their dependencies. | 03 |
| **DAG** | Directed Acyclic Graph: a graph where connections have a direction and there are no loops. "Some tasks depend on other tasks, and you can't have a cycle." | 03 |
| **Topological sort** | Putting the nodes of a DAG in an order where every task comes after the tasks it depends on. | 03 |
| **Cache** | A small, fast place to keep copies of things you use often so you don't have to fetch them from the slow place again. | 03, 10 |
| **LRU cache** | A cache that, when full, throws out the thing you used **L**east **R**ecently. A dictionary + a linked list. | 03 |
| **Thread** | One independent sequence of instructions running inside a program. A program can have several running at once. | 08, 09 |
| **Process** | A running program, with its own memory. Threads live inside a process. | 08 |
| **Concurrency** | Dealing with many things at once (taking turns quickly). | 09 |
| **Parallelism** | Actually doing many things at the exact same time on different CPU cores. | 09 |
| **Race condition** | A bug where the result depends on which of two threads happens to get there first. | 09 |
| **Lock / mutex** | A "one at a time, please" sign that a thread must hold before touching shared data. | 09 |
| **Semaphore** | A lock that allows up to N holders at once. "Only 10 downloads at a time." | 09 |
| **Deadlock** | Two threads each waiting for the other to release a lock. Neither ever moves. 💀 | 09 |
| **async / await** | A way to write code that waits for slow things (network, disk) without blocking everything else. | 09 |
| **HTTP** | The language browsers and servers speak: a request goes out, a response comes back. | 07 |
| **TCP / IP** | The plumbing that gets bytes reliably from one computer to another over the internet. | 07 |
| **DNS** | The phone book of the internet: turns `example.com` into an IP address. | 07 |
| **TLS / HTTPS** | Encryption so nobody in between can read or tamper with the request. | 07 |
| **REST** | A common style for designing web APIs around URLs and HTTP verbs (GET, POST, …). | 06 |
| **JSON** | A simple text format for sending structured data between programs. | 06 |
| **Index (database)** | A lookup structure that makes finding rows fast, like the index at the back of a book. | 05 |
| **B-tree** | The balanced tree structure most database indexes are built on. | 05, 12 |
| **Join** | Combining rows from two tables based on a matching column. | 05 |
| **Transaction** | A group of database changes that either all happen or none happen. | 05 |
| **ACID** | The four promises a good transaction makes: Atomic, Consistent, Isolated, Durable. | 05 |
| **WAL** | Write-Ahead Log: the database writes "what I'm about to do" to a log first, so it can recover after a crash. | 12 |
| **MVCC** | Multi-Version Concurrency Control: keep old versions of rows so readers don't have to wait for writers. | 12 |
| **Queue (message)** | A line of jobs waiting to be processed. Producers add, workers (consumers) take. | 10 |
| **Worker** | A process whose job is to take items off a queue and do them. | 10 |
| **Dead-letter queue** | Where jobs go after they've failed too many times, so a human can look. | 10 |
| **Retry with backoff** | Try again after a failure, waiting longer each time (and randomly — "jitter") so you don't hammer a struggling service. | 10 |
| **Idempotent** | Doing it twice has the same effect as doing it once. Essential when retries can duplicate work. | 10 |
| **Lease** | A time-limited claim on a job. If the worker dies, the lease expires and someone else can take the job. | 10 |
| **Circuit breaker** | After N failures in a row, stop calling the failing thing for a while instead of failing slowly forever. | 10 |
| **Backpressure** | Telling upstream "slow down, I'm full" instead of silently drowning. | 10 |
| **Load balancer** | A machine that spreads incoming traffic across several servers. | 11 |
| **Sharding** | Splitting one big database across many machines by some key (e.g. users 0–999 here, 1000–1999 there). | 11 |
| **Replication** | Keeping copies of data on several machines for safety and read speed. | 11 |
| **Consistent hashing** | A trick for deciding which machine holds which key so that adding a machine only moves a little data. | 11 |
| **Rate limiter** | Something that says "you may make at most N requests per minute." | 11 |
| **Distributed system** | Several computers working together as one system — and therefore able to partially fail. | 12 |
| **CAP theorem** | When the network splits, a system must choose between staying consistent and staying available. | 12 |
| **Consensus / Raft** | How a group of machines agree on one value (e.g. who's the leader) even when some of them fail. | 12 |
| **Quorum** | A majority. Many distributed decisions need a majority of machines to agree. | 12 |
| **Observability** | Being able to tell what your system is doing from the outside: logs, metrics, traces. | 13 |
| **p99 latency** | The response time that 99% of requests beat. Tells you how bad the slow tail is. | 13 |
| **Container / Docker** | A packaged-up program with everything it needs, so it runs the same everywhere. | 13 |
| **Kubernetes** | A system for running and managing lots of containers across many machines. | 13 |
| **CI/CD** | Automatically testing (CI) and deploying (CD) code every time it changes. | 13 |
| **Profiler** | A tool that measures where a program spends its time. | 13 |
| **Call stack** | The list of functions currently in progress, innermost last: `main → foo → bar`. | 08, 13 |
| **Model / weights / parameters** | A neural network is a giant pile of numbers (weights). Training adjusts them; inference uses them. | 14 |
| **Training vs inference** | Training: the model learns from data. Inference: the trained model answers a prompt. | 14 |
| **Token** | A chunk of text (roughly a word or part of a word) the model reads and writes one at a time. | 15 |
| **Transformer / attention** | The neural-network design behind modern LLMs; attention lets each token look at the others. | 15 |
| **Context window** | The maximum number of tokens the model can look at at once. | 15 |
| **GPU / VRAM** | A chip that does thousands of simple calculations at once; VRAM is its own memory, and it's always too small. | 16 |
| **Prefill / decode** | Prefill: the model reads your whole prompt. Decode: it generates the answer one token at a time. | 17 |
| **TTFT / TPOT** | Time To First Token (how long until the reply starts); Time Per Output Token (how fast it streams). | 17 |
| **Batching** | Running several requests through the GPU together to keep it busy. | 18 |
| **KV cache** | Saved attention state for tokens already processed, so the model doesn't recompute it for every new token. Lives in VRAM. | 18 |
| **PagedAttention** | Managing KV-cache memory in fixed-size pages, like an operating system does, to avoid wasting VRAM. | 18 |
| **Inference scheduler** | The part of a serving system that decides which requests run, when, on which GPU, batched with whom. | 18 |
| **Tensor / pipeline parallelism** | Ways to split one model across several GPUs when it doesn't fit on one. | 19 |
| **Speculative decoding** | A small model guesses several tokens; the big model checks them all at once. Faster when the guesses are good. | 19 |
| **Quantization** | Storing weights with fewer bits to save memory and go faster, at a small accuracy cost. | 19 |
