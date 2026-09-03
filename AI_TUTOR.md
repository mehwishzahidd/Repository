# 🤖 AI_TUTOR — using Claude / ChatGPT without cheating yourself

You will use an AI assistant constantly on this road. Used well it's a patient tutor
available at 2 a.m. Used badly it's the fastest way to *feel* like you're learning while
learning nothing — and it shows up instantly in a live interview, where there's no AI.

## The one rule
**The AI explains, quizzes and reviews. You write the code.** If it writes code, you
retype it yourself and must be able to explain every line to a rubber duck. If you can't,
delete it and try again.

## Green: always fine
- "Explain X like I'm new to programming, then give me a 3-question quiz on it."
- "Here's my code and the error. Don't fix it. Ask me questions that lead me to the bug."
- "Review my solution for clarity, naming and edge cases. Don't rewrite it."
- "I think the complexity is O(n log n). Argue with me."
- "Give me 5 edge cases for this function that I haven't tested."
- "Play a senior engineer interviewing me on this design. Interrupt with failures."
- "Summarise chapter 3 of OSTEP in 10 bullet points so I can check my own notes."
- "What's the difference between a mutex and a semaphore, in one sentence each?"

## Yellow: fine with care
- "Show me an example of a decorator" → fine, then close it and write your own from
  memory for a *different* purpose.
- "Is there a standard-library function for this?" → fine; that's documentation.
- Asking it to generate test data, sample logs, or a hostile input.

## Red: this is cheating yourself
- Pasting an exercise or LeetCode problem and asking for the solution.
- Asking it to write the project, then "reviewing" what it wrote.
- Letting it fix your bug without you understanding why it was a bug.
- Using it during a timed practice session.

## Prompts by stage
- **00–02:** "Explain, then quiz me." "Here's my error, ask me leading questions."
- **03:** "Don't solve it. Tell me which *pattern* this problem is and why." Then solve.
  After: "Here's my solution; what's the complexity and what edge case did I miss?"
- **05–06:** "Review this schema / this API design for mistakes; ask me why I chose X."
- **09:** "Here's my concurrent code. Describe an interleaving that breaks it." (It's very
  good at this, and so is an interviewer.)
- **11–12:** "You are the interviewer. I'll design X out loud; probe every decision;
  ask what breaks at 100×; interrupt with a failure every few minutes." Record yourself.
- **20:** Full mock loops with the rubrics from `ROADMAP.md`. Then get a human.

## Two habits that keep it honest
1. Close the AI window before you type your solution. Open it after.
2. Once a week, do a problem or a lesson with no AI at all, and note how it felt in
   `notes/journal.md`. If it felt much harder than usual, you've been leaning too hard.
