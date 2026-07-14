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

# I Scheduled Three AI Employees. They Haven't Missed a Shift.

Three weeks ago I built a content factory. One shared folder of raw ideas, four channels, each supposed to turn those ideas into posts on its own schedule.

There was one problem. "On its own schedule" meant "whenever I remembered to run it."

## The problem

Automation built on a script only runs when something starts it. A cron job on your laptop only fires when the laptop is open. And an AI agent you trigger manually only works when you remember to open the terminal and type the command.

I had the pipeline. Strategist, copywriter, editor, image designer, all wired together and working well when I ran them by hand. But "by hand" means some evenings I forgot. The LinkedIn post that was supposed to go out at 8:30pm went out the next morning instead, if it went out at all. The whole point of building a factory was to stop being the bottleneck, and I was still the bottleneck — just a bottleneck with better tooling.

Every fix I considered was the same shape: some external scheduler (cron, a serverless function, a CI job) calling my agent on a timer. Which meant building and maintaining infrastructure just to press my own button for me.

## The reframe

The scheduler doesn't need to be external. It can be part of the agent.

That's the actual shift with Claude Code Routines: instead of a script that calls an agent, you get an agent that already knows when to wake up. You're not orchestrating a dumb timer that triggers a smart process. You're describing a job — what to do, how often, what "done" looks like — and the agent carries the job description itself, cloud-side, independent of whether your laptop is open.

The mental model stops being "I need to remember to run this" and becomes "I already told it what to do and when. My job is to review the output."

## The solution

A Routine is a scheduled Claude Code session that runs in the cloud on an interval you set, with a persistent prompt describing the job. No laptop required, no separate scheduler to stand up. It clones the repo it's pointed at, runs whatever skill or instructions you gave it, and — this is the part that matters for anything beyond a one-off script — it can push a branch and open a pull request for you to review, instead of just doing the thing silently and hoping it was right.

That last part changes what you're willing to automate. A script that edits files unattended is scary. A routine that proposes a change and waits for your merge is not. You get the "runs without me" benefit without giving up the "nothing ships without my eyes on it" safety net.

## Real walkthrough

I now have three of these running against the content factory: one for LinkedIn at 8:30pm IST, one for Instagram Reels at 9:00pm IST, one for X at 10:00am IST. Each one clones the repository, runs that channel's growth-agent skill, picks the next unprocessed idea from the shared idea pool, and generates the post — copy, images, the works.

Then it does the part I actually care about: it opens a pull request. Not a push to main. A PR, with a description of what it picked and why, sitting there waiting for me the next time I check GitHub.

If a channel has nothing new to say — the idea queue is empty, or an idea already has a PR open from yesterday's run — it says so and stops. No duplicate content, no noise, no PR for the sake of a PR. That idempotency check turned out to matter more than the scheduling itself. A routine that runs on time but doesn't know when to do nothing is just a more expensive way to spam yourself.

Blog is the fourth channel, and — worth admitting — it isn't on that daily schedule yet. Today it's still a routine in the informal sense: something I invoke by hand when I want a post. This post exists because of that same manual invocation. The honest next step for me is doing to Blog what I already did to LinkedIn, Instagram, and X: give it a slot on the schedule and let it start opening its own pull requests too.

## What makes it different

**It survives you closing the laptop.** The routine lives in the cloud, not on your machine. It fires whether you're at your desk or asleep.

**It reviews before it merges.** The output lands as a pull request, not a fait accompli. You stay the last checkpoint, even for something that runs unattended.

**It knows when to stop.** A well-written routine checks its own state — what's already been done, what's already in flight — before doing anything. That check is what makes "run this every day" safe instead of chaotic.

**It's a job description, not a cron expression.** You're not encoding "at what time" so much as "what counts as done, and what to skip." The scheduling is almost the boring part.

## When to use it

- A recurring content or reporting pipeline that currently depends on you remembering to run it
- Nightly checks — dependency updates, broken links, stale documentation — that nobody wants to do by hand
- A daily digest or summary that needs to exist before you sit down to work, not after
- Any task where the actual work is already automated and the only missing piece is "something has to press start"

## How to set one up

You don't install anything for this one — Routines are a feature of Claude Code itself, not a skill you paste into a folder. The steps are closer to writing a job posting than writing code:

1. **Decide the job.** One sentence: what should run, and how often.
2. **Write the prompt like a job description**, not a script. State the goal, what "nothing to do" looks like, and what output you expect (a PR, a report, a message).
3. **Point it at the right repo and tools.** Give it only what it needs — for the content factory routines, that's the fork repo and permission to open pull requests, nothing more.
4. **Schedule it and walk away.** Check back on the pull requests it opens, not on whether it ran.

Manage and inspect your routines at claude.ai/code/routines.

## Try this

Pick the one task you automate by hand today — the one where the code already exists and the only manual step left is you remembering to run it. Turn that one into a routine this week. Don't start with something ambiguous; start with something that already has a clear "done."

## Questions for you

Have you scheduled an agent to do something recurring yet, or are you still the one pressing the button? If you have, what was the first task you trusted to run without you watching? And if a routine of yours ever did something you didn't expect — what caught it before it shipped?

If this was useful, a like helps more people find it. Part two will get into what happens when two routines' outputs start conflicting with each other.

If you've been following the content factory build, this is the point where the automation stops needing you in the loop for the routine parts — and starts needing you only for the judgment calls.
