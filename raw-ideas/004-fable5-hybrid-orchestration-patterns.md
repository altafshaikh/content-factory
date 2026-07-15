# Two Patterns for Running Fable 5 at a Fraction of the Cost

## Context

Anthropic published benchmark data showing two concrete ways to get near-Fable-5 performance while keeping costs far lower. Both rely on mixing Fable 5 with Sonnet 5 in a structured workflow rather than routing every token through the most expensive model.

**Pattern 1 — Advisor (escalate up):** Sonnet 5 runs the main loop as the executor. It calls Fable 5 as an on-demand advisor tool only when it needs guidance. Fable 5 is invoked roughly once per task to steer, not to do the work. Most tokens are billed at the cheaper executor rate. On SWE-bench Pro, this setup achieved 92% of Fable 5's solo score at 63% of the price.

**Pattern 2 — Orchestrator (delegate down):** Fable 5 handles planning and then fans out the actual work to multiple Sonnet 5 worker sub-agents. Most tokens are billed at the cheaper worker rate. On BrowseComp, this setup achieved 96% of Fable 5's solo performance at 46% of the price ($18.53 vs $40.56 per problem, 86.8% vs 90.8% accuracy). Running all Sonnet 5 was cheaper at $16.01 but dropped accuracy to 77.8%.

A key detail: each sub-agent keeps its own cache, so repeated context is not paid for multiple times across calls.

**In Claude Code:** You can define lightweight helper roles in `~/.claude/agents/worker.md` with a cheaper model (Sonnet or Haiku) and lower reasoning effort. A short instructions file tells the main model which tasks to hand off. The workflow is reusable across projects without rebuilding it each time.

The broader insight is that "which model should I use?" is the wrong question. The right question is "which model should handle which part of this task?" Planning and final review go to the main model. Routine reads, edits, and execution go to the cheaper helper.

## Source

- https://x.com/ClaudeDevs/status/2074606063509528855
- https://www.instagram.com/p/DaypoWancqb/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ==
