# 💼 YEAR_ONE_JOB — getting hired on the way up

The plan says get hired around month 13–18, from Stage 10 onward. That job is part of
the curriculum: it's where "production experience" comes from, and it's what the OpenAI
candidate was told they lacked. This page is where and how.

## The three realistic first roles

| Role | What it is | What it adds to this curriculum | Extra to learn |
|---|---|---|---|
| **Junior backend engineer** | Build and maintain APIs and services | Real code review, incidents, deploys, a team's conventions | The team's framework (Django/Flask/Node), more SQL, a frontend basics week (HTML/CSS/JS + `fetch`) so you can read the other half |
| **Data engineer (junior)** | Pipelines that move and clean data | Serious SQL, batch/stream processing, scheduling (Airflow), big data volumes | pandas, Airflow or dbt, Spark basics, warehouse concepts (columnar!), data modelling |
| **Platform / SRE / DevOps (junior)** | Keep systems running; build internal tooling | On-call, observability, Kubernetes, IaC, incident response — the closest to infra SWE | Terraform, Kubernetes ops, Linux depth, Go basics, a cloud cert if postings ask |

Also viable: **support engineer at an infra/cloud/AI company** (a foot in the door with
real production exposure), **QA / test automation** (if it includes writing code), and
**internships** at any of the above. Titles matter less than: do you ship code, does it run
in production, do you see it break.

## When to apply
Start at Stage 10 (backend deployed, tests, Docker, a queue). Don't wait for "ready";
interviews are practice and rejections are data for `notes/questions.md`. Expect 50–150
applications per offer as a career-changer; that's normal, not a verdict.

## Reading a job posting
- "Required" lists are wish lists. Apply if you have ~60%.
- Look for: Python, SQL, Postgres, Docker, REST, Git, "junior" / "associate" / "early
  career" / "II". Avoid for now: "5+ years", "senior", "lead".
- Look for signals of a healthy team: code review mentioned, tests mentioned, on-call
  rotation described honestly, a real tech blog.

## The résumé, built from this repo
- One page. Projects section above education for career-changers.
- Each project: one line of what, one line of **numbers** (p99 latency, throughput,
  test count, request volume in a load test, lines of Terraform), one line of what broke
  and what you fixed. `P2`, `P3`, `P6` are the strongest early ones.
- GitHub link with READMEs, architecture diagrams, CI badges, and a pinned P6.
- Previous non-tech work stays on: ops, retail, warehouse, school — framed as
  prioritisation, reliability, ownership. It's real experience.
- No "aspiring", no "passionate". State what you built.

## Referrals and people
Most infra hiring is referral-driven. From Stage 02: one study partner or Discord
group. From Stage 06: post your project write-ups publicly (GitHub, a small blog, or a
LinkedIn post) and ask for feedback. From Stage 10: reach out to engineers at companies
you like with a specific question about their blog post or open-source project, not a
job ask. Contribute a small fix to a tool you use (FastAPI, httpx, vLLM docs). Local
meetups if you can; online ones (MLOps Community, GPU MODE, Python Discord) otherwise.

## Once you're in
- Ask for on-call and incident exposure as soon as it's reasonable. That's the
  experience the loops reward.
- Keep the road going at a lower cadence (`LEARNING_GUIDE.md` §3 bad-week plan):
  one design a week, three problems a week, one stage every few months.
- Write down every incident, every production bug and every disagreement in
  `notes/stories.md` while it's fresh. Those become your best interview answers.
- Aim for 18–24 months of production work before the Anthropic/OpenAI infra loops.
  Reapply windows after a rejection are usually 6–12 months; plan for a second attempt.
