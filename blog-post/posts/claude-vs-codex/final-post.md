---
title: I Gave the Same Task to Claude and Codex. One Opened a Browser.
tags: [AI, Frontend Development, Developer Tools, Productivity, AI Engineering]
seo_title: Claude vs Codex for Frontend Dev: A Real Experiment
seo_description: One AI tested its own code. The other needed 3 re-explains. What I found building a real app with both tools.
---

<!-- 
BANNER IMAGE
============
SVG hero (generated): blog-hero.svg — upload this to Hashnode as the cover image.

To generate a higher-res version with an external tool, use the prompt below:

PROMPT:
Dark editorial illustration, wide 16:9 format. Two horizontal parallel paths side by side against a deep charcoal background. The left path curves around and connects back to its own start — a closed, self-completing loop, with a faint warm glow at the closure point. The right path travels the same distance but ends abruptly at an open gap — a blinking cursor implied by a small vertical bar, waiting. Geometric, clean, minimal. No text, no code, no people, no UI elements. The contrast between completion and incompletion is the whole image. Atmospheric, editorial, tech-themed.

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

Codex opened my app in a browser. Navigated it like a real user. Confirmed the changes were right.

Claude wrote clean code — and then waited for me to tell it what to do next.

Same task. Same codebase. One tool closed the loop on its own. The other didn't.

---

## The Loop Every Frontend Dev Gets Stuck In

You describe a feature. The AI writes code. It looks reasonable. You run it. Something's slightly off.

You go back: "I meant the nav bar, not the sidebar." It fixes that. You run it again. Something else is off. Three rounds later, you realise you're not building anymore — you're explaining.

The code quality isn't the problem. The tool's ability to check its own work is.

---

## What Actually Happened

I was building a personal fitness tracking app for myself. No clients, no deadlines. I decided to run both Claude and Codex on the same frontend tasks to see what happened.

**With Codex:**

I gave it a task. It generated the code, opened the app in a browser, navigated the UI like a real user, and reported back what worked and what didn't. When something was wrong, it fixed it on its own.

No extra prompting from me. It understood the intention, built the thing, verified it worked, corrected it when it didn't.

**With Claude:**

It wrote code. Genuinely clean code. But getting it to understand exactly what I wanted took three more rounds of explanation.

"This is close, but the button belongs here, not there." It adjusted. Another thing was off. I explained again. And so on.

The code was fine. The autonomous loop wasn't there.

---

## The Real Gap: Closing the Loop

This isn't about which model scores higher on a benchmark. It's about which one closes the feedback loop on its own.

Codex ran the app, behaved like a user, and verified the result. That one step — self-testing — cut out three rounds of my explaining.

Claude waited for me to be the test case. Which means I became the bottleneck.

---

## What Makes the Difference

**Autonomous verification.** A tool that opens the app and checks its own output removes you from the QA cycle entirely. The loop shrinks from minutes (or days, if you're busy) to seconds.

**Intent over instruction.** Visual output is hard to specify in words. A tool that navigates and verifies closes the gap between "what I described" and "what I meant" — automatically.

**Clean code isn't the whole job.** If the tool generates perfect code but can't confirm it behaves as intended, you're still running explanation loops as the human in the circuit.

**This isn't a Claude-is-bad take.** For reasoning-heavy work — architecture decisions, complex refactoring, writing — Claude is still my go-to. This is a right-tool, right-job observation. The shapes of intelligence are different.

---

## When to Use Which

Use autonomous-verification tools when:
- You're building frontend UI where visual output matters
- Any task where "does it work?" requires running the app
- You want fast iterative cycles without being the checker yourself

Use Claude when:
- You need explanation alongside the code
- Complex architecture or trade-off analysis
- Writing and editing tasks
- Refactoring where understanding the change matters as much as making it

---

## Try This Right Now

Give both tools the same frontend task. Count the back-and-forth rounds.

Don't count the first prompt. Count the explanation cycles that follow before you get what you actually wanted.

That number is your signal. It tells you where your attention is going as the human in the loop — and whether it needs to.

---

## What's Your Number?

How many explanation rounds does your current AI tool need on a typical frontend task?

Drop it in the comments. I'm logging these across experiments.

If this was useful, hit like — it helps the next developer find it before they spend three rounds explaining the same thing.

This is **AI Experiment #1** in an ongoing series — real observations from things I'm building, no benchmarks, no sponsored takes. If you landed here from a later experiment, start with Part 1 — this one sets the frame.

---

## Post assets

| File | Use |
|------|-----|
| [blog-hero.svg](./blog-hero.svg) | Hashnode cover image (SVG, 1600×900) |
| [exports/blog-hero.png](./exports/blog-hero.png) | PNG export for upload |
| [03-banner-prompt.md](./03-banner-prompt.md) | Prompt to regenerate with Midjourney / DALL·E / Ideogram |
| [02-title-options.md](./02-title-options.md) | All title options — edit frontmatter above to switch |
