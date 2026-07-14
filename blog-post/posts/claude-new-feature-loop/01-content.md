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

# I Stopped Running My AI Pipeline By Hand

Every day I do the same thing. Open the terminal, run a command, wait, check the output, run the next one. Same steps, same order, same time of day. It works. It's also the kind of work a computer should be doing instead of me.

That's the loop most people building with AI tools get stuck in — not a technical wall, just a habit of manually kicking off things that don't need a human hand on the trigger.

## The problem with "just run it again tomorrow"

I've got a content pipeline that turns raw ideas into posts. It's useful exactly because it's repeatable — same idea in, same quality of output out. But "repeatable" and "I have to remember to do it" are two different things.

Miss a day, and the pipeline doesn't fail loudly. It just doesn't run. Nothing breaks. Nothing tells you. The queue quietly sits there while you're busy with something else. That's a worse failure mode than a crash, because a crash at least gets your attention.

## The reframe

A recurring task isn't a task you repeat. It's a task you schedule once and then leave alone.

That sounds obvious written down. But most of us treat "automate this" as a bigger project than it is — something that needs a cron job, a server, config files. So we keep doing it by hand because the automation feels heavier than the manual work it's replacing.

## The solution — `/loop`

This week Claude Code shipped a feature called `/loop` — run a prompt or a slash command on a recurring interval. No external scheduler, no separate process to babysit. You tell it what to run and how often, and it keeps running it.

I'd already wired up a content factory project — the same pipeline I mentioned above, several channels each consuming from a shared pool of raw ideas. It was already scripted as a slash command. The only missing piece was something to press the button on a schedule. `/loop` is that piece.

## The walkthrough

I pointed `/loop` at the pipeline's existing prompt and set it to fire daily. That's it — no new infrastructure, no separate scheduling tool bolted on. The same command I was typing by hand every day is now just... running.

I'm one day into this experiment, so I don't have a verdict yet. What I do have is the first real test: does the loop actually fire without me watching it, and does the output hold up when nobody's supervising the run in real time. That's the part manual execution was quietly protecting me from — my presence was an implicit check I didn't realize I was relying on.

## What makes it different

**It's built into the tool you're already using.** No separate scheduler, no new service to deploy — the same CLI that runs the command once can run it forever.

**The interval is part of the command, not a separate config file.** You say how often when you say what — one instruction, not two systems to keep in sync.

**It turns "I should automate this" into a one-line decision.** The barrier to scheduling something drops from "set up infrastructure" to "type one more argument."

**It exposes the gaps in a pipeline fast.** Anything that quietly depended on a human noticing something looks wrong will surface the first time nobody's watching.

## When to use it

- A task you already run manually on a fixed cadence
- A pipeline that's scripted enough to run unattended, but hasn't been trusted to yet
- Anything where the real cost isn't the work — it's remembering to start the work

## How to use it

Point `/loop` at the interval and the prompt or slash command you want repeated:

```
/loop 1d <the prompt or slash command to run>
```

Self-paced, where the model decides the cadence instead of a fixed interval:

```
/loop <the prompt or slash command to run>
```

That's the whole setup. No new files, no deployment step — it runs inside the same session model you already use.

## Try this

If you've got something you run by hand on a schedule — a report, a content pipeline, a status check — that's the candidate. Don't automate something new. Automate something you're already doing manually, and see what breaks when you're not the one clicking go.

I'll share how the content factory loop actually performs once it's had more than a day to prove itself — whether the output quality holds, and whether "unattended" turns out to mean what I think it means.

## Let's talk

Have you tried `/loop` yet, or something like it? What's the one manual step in your own workflow you know you should have automated by now but haven't? And if you've run something unattended before — what's the first thing that broke once nobody was watching?

If this was useful, a like helps more people find it. Part two comes once the experiment has real results to report.

---

This is one small piece of a bigger shift: from writing prompts to building systems that run themselves. If you're new to that idea, this is a good place to start following along.
