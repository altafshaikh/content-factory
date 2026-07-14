<!-- 
BANNER IMAGE
============
Generate this image using Midjourney, DALL·E, Ideogram, or any image tool, then upload to Hashnode as the cover image.

PROMPT:
[filled in from Phase 3]

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

# Your Python Script Never Forgets. Your Agent Does.

Write a function in Python. Give it the same input a thousand times. You get the same output a thousand times. That's not a feature you think about — it's just how code works. It's the deal you signed up for the day you learned to program.

Now put an AI agent in that same spot. Same input, same prompt, same instructions. Run it Monday, it does the job perfectly. Run it Wednesday, it skips a step you never told it to skip. Nothing in your code changed. Nothing in your prompt changed. The output did anyway.

## The problem

I've been building automation with AI agents — using them to write security fixes, ship features, run parts of my workflow end to end. And the longer I do it, the more one thing bothers me: it doesn't give you the same result twice.

The first run is often great. You give it an input, it gives you a clean output, you think "this is solved." Then you run it again next week and it skips an instruction. Not because the instruction changed. Not because the input changed. Because that's what a non-deterministic system does — it gives you *a* plausible answer, not *the* answer.

Compare that to the code I've written for fifteen years. A JavaScript function doesn't have moods. Feed it the same input on any day, in any year, and it returns the same output — forever, until I change the code myself. I write it once. I forget it. It keeps working.

I can't forget an agent. I'm constantly re-checking it, re-instructing it, patching the gap between what it did last time and what I need it to do this time.

## The reframe

Here's the mental model shift that made this click for me: **traditional code is a contract, AI output is a negotiation.**

A function is a contract — same input, same output, no exceptions, enforced by the machine itself. You can build a career on that guarantee. Entire industries — banking, aviation, compilers — are built on the assumption that a program does the same thing every time you run it.

An agent doesn't offer that contract. It offers a negotiation that happens to go well most of the time. You're not calling a function — you're asking a very capable, very inconsistent collaborator to do something for you, and hoping today is a day it's paying full attention. Sometimes it is. Sometimes it skips a step and you don't find out until something downstream breaks.

That's not a flaw you patch once and move on from. It's the nature of the tool. Which means the job changes too — from "write it once, forget it" to "write it, then keep watching it."

## The part that isn't even in your control

The instruction-drift problem is annoying but at least it's yours to manage — add more detail, tighten the prompt, add guardrails. There's a second problem that isn't yours to manage at all.

The companies building these frontier models — the ones with the best agents today — have a well-documented pattern: when a new model ships, the old one gets quietly deprioritized, throttled, or nudged toward retirement. You didn't ask for an upgrade. You built and tuned your automation against a specific model at a specific effort level, and one day the ground under it just moves.

Change the effort level, swap the model version, anything shifts upstream — and the same agent, running the same instructions you spent weeks refining, starts making new mistakes or repeating old ones you thought you'd fixed. You didn't touch your code. The rules just changed underneath it.

A traditional program never does this to you. Nobody silently swaps out your Python interpreter and makes your `for` loop behave differently overnight. With agents, that's not a hypothetical — it's a maintenance cost baked into the tool, and it doesn't show up in any changelog you get to read in advance.

## The solution — where to draw the line

None of this means "don't use agents." I'm not walking that back — I use them daily and they're genuinely useful. It means being deliberate about *where* you let non-determinism into a workflow, and where you don't.

The practical split I've landed on:

**Let the agent make judgment calls.** Anything that requires reading context, weighing tradeoffs, or producing a first draft — code review comments, drafting a fix, summarizing a diff, deciding *what* needs to change. This is where the agent's flexibility is the whole point. You don't want deterministic behavior here; you want good judgment, and you're willing to review the output.

**Never let the agent be the enforcement layer.** The actual security check, the actual test suite, the actual gate that decides whether code ships — that has to be deterministic code. Write the agent's proposed fix through a real program: a linter, a test, a static check, something that gives the same verdict every time given the same input. The agent proposes. The program disposes.

This is the same reason compilers, not humans, decide whether your code type-checks. You want the fuzzy, context-aware part to run *before* the strict, repeatable gate — never instead of it.

## What this looks like in practice

Take the security-fix automation I mentioned. Early version: agent finds a vulnerability pattern, agent writes the fix, agent applies the fix. That's three non-deterministic steps in a row, and each one compounds the odds that something drifts.

Better version: agent finds the pattern and proposes a fix (non-deterministic — fine, that's judgment). The fix runs through the existing test suite and a static analyzer (deterministic — this is the gate). Only fixes that pass the deterministic gate get applied automatically; anything that fails goes to a human, not back to the agent for a retry loop that might "fix" it differently each time.

The agent still does real work. It's just not the last word.

## What makes this different from "just prompt engineering harder"

**It's not a prompting problem, it's an architecture problem.** Adding more instructions delays the drift; it doesn't remove it. The fix is deciding which parts of your pipeline are allowed to be non-deterministic at all.

**The model changing under you is a dependency risk, not a bug.** Treat frontier model access the way you'd treat any third-party dependency you don't control — version-pin where you can, and design for the day it changes anyway.

**"It worked once" is not evidence it's solved.** With deterministic code, one clean run under a covered test case tells you a lot. With an agent, one clean run tells you it's *possible* — not that it's reliable.

**The deterministic gate is what makes the non-deterministic part safe to use at all.** Without it, you're not automating a workflow — you're just hoping, on a loop.

## When to reach for this split

- Any pipeline where an agent's output triggers an action with real consequences (deploys, merges, security fixes)
- Any workflow you plan to "set and forget" — if you can't forget it today, don't assume you'll be able to forget it after "one more instruction"
- Any place you've caught yourself adding the same clarifying instruction more than once — that's the signal the agent needed a deterministic check, not another sentence of prompt

## Try this right now

Pick one agent-driven step in something you already have running. Ask: if this step's output were wrong, would anything downstream catch it automatically — or would you only find out when something breaks? If the honest answer is "I'd only find out later," that's the step that needs a deterministic gate in front of it, not a longer prompt.

---

Have you hit this with your own agent workflows — the same input giving you a different result a week later? Did tightening the prompt actually fix it, or just push the drift somewhere else? What's the deterministic check you'd put in front of your riskiest automation if you built it today? Drop your experience in the comments — I'm genuinely trying to figure out where this settles as these tools mature.

If you liked this, the next post in this series digs into what a deterministic gate actually looks like for an AI-driven pipeline — worth a follow if you want it when it lands.

---

This one sits in the **Mindset** part of the series — before the tools and the building, it's worth being honest about what you're actually trading away when you hand a step to an agent.
