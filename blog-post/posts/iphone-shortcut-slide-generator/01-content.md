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

# I Stopped Writing Slides. I Started Shipping Notes.

You gave a talk once. Or you're about to. Somewhere in your Notes app is the raw version of it — a voice memo transcript, a wall of half-formed bullet points, the thing you actually think about the topic before it gets flattened into slide format.

And it's still sitting there. Untouched. Because turning that raw material into an actual deck is a different kind of work than having the idea, and most days you don't have the energy for both.

## The problem isn't the idea. It's the handoff.

Here's the part nobody says out loud: you already know how to structure a good deck. You've given enough talks, made enough slides, sat through enough bad ones, to have opinions about what belongs on a title slide, how a section should open, which points earn a slide of their own and which get cut. That knowledge exists. It's just stuck in your head instead of in your slides.

The gap isn't "I don't know how to make this good." It's "going from raw notes to structured slides is high-effort, and my brain is very good at finding reasons to do it later." Procrastination isn't laziness here — it's an accurate prediction that the next step is going to cost more attention than you have right now. So the raw idea sits in Notes. Forever, if you let it.

## The reframe: this was never a content problem

I kept assuming the fix was a better prompt, or a smarter model, or more discipline. It wasn't any of those. The fix was removing the step where I had to *decide* to do the work.

Every time I wanted slides, I had two jobs: remember the structure I like, and manually feed my raw notes into a prompt that encoded it. Two decisions, every single time, both of which are exactly the kind of small friction that kills a task before it starts. The model was never the bottleneck. The activation energy was.

## The solution: bake the decision into a shortcut, not a prompt you have to remember

So I stopped treating "generate slides from notes" as something I do. I turned it into something that happens when I drag a note into the right place.

I built an iPhone Shortcut. It does two things:

1. It holds a **fixed custom prompt** — the layout rules I've learned the hard way over time. What goes on the title slide. How each section should open. Which points make the cut and which don't. My whole personal opinion about "what a good slide deck looks like," written down once instead of re-derived every time.
2. It takes whatever raw text I hand it — the talk transcript sitting in Notes — and feeds it, alongside that fixed prompt, into ChatGPT.

That's it. No new decisions at generation time. The judgment call already happened, once, when I wrote the prompt. Every run after that is just execution.

## The walkthrough

The raw material starts in my Notes app — a talk transcript, spoken and captured as-is, no cleanup. When I want slides, I open the note, hit share, and pick the shortcut I built. The shortcut passes the note's text into ChatGPT along with the prompt I've already written — the one with my structure, my "don't put more than one idea per slide" rule, my opinion on how a section transition should read. What comes back is a structured slide layout: a title, sectioned points, the shape of a deck, not just a paraphrase of my notes.

I'm on an iPhone 15 Pro Max, using ChatGPT specifically because that's what the shortcut was wired to when I built it — the mechanism doesn't care which model answers, as long as something on the other end can take a prompt and text and return structured output.

The manual version of this — open ChatGPT, retype or paste my notes, retype the structure I want, wait, copy the output — has a dozen small moments where I could stop and not finish. The shortcut version has one: drag, share, done.

## What makes this different

**The prompt does the thinking once, not every time.** You're not asking the model to guess what a good deck looks like — you already told it, permanently, in one prompt you wrote when you had the energy to think it through.

**The shortcut removes the decision, not just the typing.** The friction was never "typing is slow." It was "starting requires a decision," and a share-sheet action doesn't ask you to decide anything — it just runs.

**It works on garbage input on purpose.** The raw note is not supposed to be clean. That's the point — you're allowed to think out loud, and the automation is what turns "out loud" into "structured," not you.

**It's small enough that you'll actually finish it.** This isn't a framework or a platform. It's one shortcut, one prompt, one share-sheet action. Small enough to build in an afternoon and small enough to actually use.

## When to use something like this

- You have a recurring "raw notes → structured output" step you keep putting off
- You've done that step enough times to have real opinions about what "good" looks like
- The blocker is starting, not knowing what to do once you start
- The output format is roughly the same every time — slides, but it could just as easily be an outline, a script, a report

## How to build your own version

You don't need my exact prompt or my exact deck structure — you need your own. The steps are the same regardless:

**Step 1 — Write down your structure, once.** Whatever you currently do "in your head" when you build a deck — how you pick a title, how you open a section, what earns a slide and what gets cut — write it down as a prompt. Be as specific as your actual opinions are. Vague instructions produce vague slides.

**Step 2 — Wire a Shortcut (or equivalent) to it.** On iPhone, that's the Shortcuts app: a "Share Sheet" action that takes selected text, appends your fixed prompt, and sends both to whichever AI tool you use. On other platforms, the equivalent is any automation tool that can capture text and call an LLM with a fixed system prompt — a browser extension, a CLI alias, a small script.

**Step 3 — Make it a share-sheet action, not a new app to open.** The whole point is that it should be less effort than opening a chat window and pasting. If your version still requires you to context-switch into a new tool and retype your ask, you've rebuilt the friction you were trying to remove.

## Try this

Pick the one "raw to structured" step you procrastinate on most. Write down your actual opinion about what good output looks like, once, as a prompt. Then wire it to the lowest-friction trigger available to you — a share sheet, a hotkey, a saved snippet. Don't build the general-purpose version. Build the one that gets you from "I have an idea" to "it's already there" for the exact thing you do over and over.

What's the raw-to-structured step you keep procrastinating on? And if you've automated something like this already, what does your version wire together?

If this was useful, a like helps more people find it — and if you try building your own version, I'd genuinely like to hear what it ends up looking like.

## What's next

This isn't part of a numbered series — it's a small workflow win, the kind that's easy to miss because it doesn't look like "AI progress." But it's the same underlying idea running through a few other posts here: the model was rarely the bottleneck. The friction around using it was.
