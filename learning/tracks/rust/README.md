# Track 5 — Rust

> A modern systems language that gives you C++-level speed **with** memory safety
> guaranteed at compile time. Beloved by developers and increasingly used in industry
> (browsers, operating systems, blockchains, and high-performance backends).

**Prerequisite:** Be solid in at least one language (ideally Python *and* some C++). Rust's
signature feature — **ownership & borrowing** — is genuinely hard for true beginners, so
this track comes after you have programming fundamentals down. Learning it after C++ is
ideal, because you'll *appreciate* what Rust is protecting you from.

---

## Why it matters for your goals
- **Systems programming** without the foot-guns of C++ (no segfaults, no data races).
- **Growing job market** — used at Microsoft, Amazon, Cloudflare, Discord, and more.
- **Makes you a better programmer** — its compiler forces you to understand ownership of
  data, a concept that improves your code in *every* language.

---

## Syllabus (in order)

### Part A — Getting comfortable
1. **Setup & Cargo** — `rustup`, `cargo new`, `cargo run`; Rust's excellent tooling
2. **Variables & types** — immutability by default, `let`/`mut`, type inference
3. **Control flow & functions** — familiar from Python/C++, with expressions everywhere

### Part B — The Rust mindset (the famous hard part)
4. **Ownership** — the rule that makes Rust safe: each value has one owner
5. **Borrowing & references** — `&` and `&mut`, the borrow checker
6. **Lifetimes** — how Rust tracks how long references are valid
7. **The `String` vs `&str`** distinction (a classic beginner stumbling block)

### Part C — Rust's powerful type system
8. **Structs & methods** — `impl` blocks
9. **Enums & pattern matching** — `match`, `Option<T>` (no null!), `Result<T, E>`
10. **Error handling** — `Result`, the `?` operator (no exceptions)
11. **Traits & generics** — Rust's version of interfaces + templates
12. **Collections** — `Vec`, `HashMap`, iterators and closures

### Part D — Going further
13. **Concurrency** — "fearless concurrency"; threads without data races
14. **Modules, crates & the ecosystem** — `cargo` dependencies, publishing
15. **A real project** — a CLI tool or small web service

---

## Free resources
- **"The Rust Programming Language"** (a.k.a. "The Book") — *doc.rust-lang.org/book* — the
  official, free, and genuinely excellent starting point
- **Rustlings** — small interactive exercises that compile-check your answers (perfect
  hands-on practice, very similar in spirit to our Python exercises)
- **Rust by Example** — learn by reading annotated runnable snippets
- **"Programming Rust"** (book) — the deeper dive, for later

> This is a **Phase 4 (breadth)** track. Get Python + DSA + C++ going first; then Rust
> will click much faster. Tell me when you're ready and I'll build the lessons.
