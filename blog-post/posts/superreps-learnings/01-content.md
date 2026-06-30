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

---

Everyone sees the tweet: "I built a full app in one afternoon with AI."

Nobody posts the follow-up.

---

## The Part That Doesn't Make It to Twitter

I wanted to build a personal fitness tracker. Not a generic CRUD app — a personalized clone of a popular tracker I already used, with features tuned exactly to how I train.

The plan: paste a design, get code, ship. How hard could it be?

Turns out, pretty hard.

---

## What AI Is Good At (And What It Isn't)

AI is great at building *parts*. Hand it a screen mockup, it gives you a component. Give it a spec, it gives you a function.

But a working product is not a pile of parts.

It's transitions that feel smooth. Flows that don't break mid-session. Features that talk to each other correctly. Data that actually persists. A UI where the right thing is always in the right place.

AI doesn't hold that vision. You do.

---

## The Real Problem With Vibe Engineering

The mistake I kept making: thinking "AI builds, I review."

That's backwards.

Vibe engineering is: "I own the product intent. AI executes one piece at a time."

Lose that distinction, and you spend hours debugging code that was never well-defined to begin with.

---

## What Happened When I Built SuperReps

I started building SuperReps — a fitness app for myself. The goal was to clone the core idea of a popular training app I liked and add my own customizations on top.

I started with the UI.

I grabbed a reference design from an app I admired and handed it to the AI. It built something that looked great. Actually polished. I was impressed.

Then I tried to use it.

The start screen worked fine. The workout screen loaded. But the moment I tapped "start workout" — nothing worked.

The timer didn't run. The set counter reset itself. After a set, the data didn't save. The history screen was empty.

So I went back in. Fixed the timer. Tested again. Timer worked, but now the counter was off. Fixed the counter. Now the save broke again. Fixed the save. Now the flow between screens felt wrong — too many steps, awkward transitions, confusing state.

Not because the AI wrote bad code. But because I'd built a collection of screens, not a product.

---

## What Makes the Difference

**Own the end-to-end flow, not the individual screens.**

The biggest mistake was thinking feature-by-feature. Build the start screen. Build the workout screen. Build the history screen. Each one working in isolation. But when you put them together, everything breaks at the seams.

Start with one complete user journey instead. Opening the app → starting a workout → logging sets → finishing → viewing history. Make that one path work, feel right, and test clean. Then expand.

**"Looks right" and "works right" are different problems.**

AI is very good at the first one. Getting the UX tight — timing, feedback, the small details that make something feel polished — takes many iterations. Plan for it.

**Re-explaining is a signal, not a frustration.**

Every time I had to re-explain context from two prompts ago, it meant I'd scoped the task too broadly. The AI didn't forget anything. I was asking too much in one go. Smaller, tighter prompts move faster.

**Test the full flow, not just the current screen.**

I kept testing screens in isolation. Everything looked fine. But running the full path — start workout → log sets → finish → view history — always surfaced something broken at the transitions. That's where you learn whether the app actually works.

---

## When This Approach Works Best

- You have a clear reference: your own sketch, an app you like, a Figma file
- You're building for yourself first — the tight feedback loop lets you iterate fast
- You're okay with "working before polished"
- You want to understand what the AI built, not just trust that it did

---

## One Thing to Try Right Now

Take one user flow you're working on. Not the whole app — one path, start to finish.

Prompt the AI to build that path completely: one screen, one action, one result. Test it end-to-end. Then move to the next flow.

The fastest way to build with AI is not to build everything at once. It's to build one thing completely, then move.

---

## What's Your Experience?

A few things I'm genuinely curious about:
- Have you hit the same wall — parts work, the flow doesn't?
- What's your strategy for testing AI-generated UIs end-to-end?
- Are you doing one flow at a time, or trying to build the whole thing in a session?

Drop your experience below. This series gets more useful when it reflects more than one person's experiments.

If this was useful, a like helps others find it.

---

## This Is Part of a Series

AI Experiment #1 covered Claude vs Codex for frontend work — specifically, which one tested its own output. If you missed it, start there — this experiment builds on it.
