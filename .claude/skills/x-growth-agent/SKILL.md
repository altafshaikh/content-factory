---
name: x-growth-agent
description: "Daily-loop X (Twitter) post factory inside a multi-channel content factory. Reads ideas from a SHARED ../raw-ideas/ library (immutable) and writes X-specific outputs into ./x-posts/. Each run picks the oldest unconsumed idea (queue = ls raw-ideas/ minus this channel's TODO.md Done section), runs a pipeline (Strategist decides single-tweet vs thread → N Copywriters → Editor) + an Image Designer, saves every handoff to a per-post folder, and updates TODO.md. The source idea NEVER moves — it stays in the shared library so other channels (LinkedIn, blog, presentation) can also consume it. If no unconsumed ideas exist for X, the run exits quietly. Use when user says /x-growth-agent, 'write a tweet', 'draft a thread about X', 'process my X ideas', or when invoked via /loop. Always trigger this skill."
trigger: /x-growth-agent
extends: linkedin-growth-agent
---

# /x-growth-agent

A daily-loop X (Twitter) post factory. The user keeps dropping raw ideas into a shared folder; each invocation processes ONE new idea end-to-end (or no-ops if there are none).

This is the X sibling of `linkedin-growth-agent`. The shape is the same — compute queue, pick oldest, run a writer pipeline, generate images, finalize TODO.md — but the platform rules differ. Where this file is silent, the LinkedIn skill's structure applies; where it speaks, X wins.

**Default variations per post: 3 (one per X-native angle — see Angle Assignments). Override with `/x-growth-agent 2` to drop the contrarian angle for this run. Max 3.**

---

## What makes X different from LinkedIn (read first)

| Dimension | LinkedIn | X (this skill) |
|-----------|----------|----------------|
| **Output unit** | One long-form post | **Single tweet by default; thread only when the idea genuinely breaks into sections** (Strategist decides) |
| **Length** | ~1300 chars, line-break heavy | **280 chars HARD per tweet.** Single tweet ≤ 280. Each thread tweet ≤ 280. |
| **Hashtags** | 3–5 niche tags | **None by default.** Hashtags suppress reach and read as spam on X. At most 1, only if it's a real live community tag. |
| **Links** | Link in first comment | **Link in a reply, never the main tweet** (X downranks tweets with external links). |
| **Hook** | First line, room to breathe | First ~7 words decide the scroll. Front-load the payload. No "a thread 🧵" preamble. |
| **Tone** | Professional-personal | Sharper, faster, more conversational. Punchy beats polished. |
| **Image dims** | Portrait 1080×1350 | **Landscape 1600×900 (16:9, in-stream default) and Square 1080×1080.** No portrait. |

Everything else (immutable `../raw-ideas/`, one-idea-per-run, save-every-handoff, no emojis, strip company/tool names, never invent stats) is identical to LinkedIn — see `.claude/skills/linkedin-growth-agent/SKILL.md` for the shared rules.

---

## Project folder layout (canonical)

```
content-factory/                            ← project root
├── raw-ideas/                              ← SHARED, immutable, read-only from this skill
│   ├── 001-<slug>.md
│   └── 002-<slug>.md
├── x.agent.md                              ← daily /loop prompt (calls this skill)
└── x-posts/                                ← X channel folder (this skill writes here)
    ├── README.md
    ├── CLAUDE.md
    ├── PLAYBOOK.md                         ← X best-practices; the craft baseline (read every run)
    ├── TODO.md                             ← Queue + In Progress + Done sections
    └── posts/                              ← one folder per generated post
        └── <slug>-<YYYYMMDD>/
            ├── 01-post-plan.md
            ├── 02a-draft-<angle>.md
            ├── 02b-draft-<angle>.md
            ├── 02c-draft-<angle>.md            (if N=3)
            ├── 03-editor-verdict.json
            ├── 02-revised-draft.md             (if revision round)
            ├── 03-editor-verdict-final.json    (if revision round)
            ├── impact-1.svg
            ├── impact-2.svg
            ├── exports/
            │   ├── impact-1.png
            │   └── impact-2.png
            └── final-post.md
```

**`../raw-ideas/` is immutable.** Never move, rename, or delete files in it. Consumption is tracked in `./x-posts/TODO.md` Done section.

**Bootstrap on first run:** if `./x-posts/` is missing its scaffold (`TODO.md`, `posts/`), create it (templates below) and continue. If `../raw-ideas/` doesn't exist, create it, tell the user where to drop ideas, and exit.

> **No performance loop on X — read the PLAYBOOK instead.** This channel runs on a free X account with no analytics export, so there is no Agent 0, no `performance/` folder, and no `performance.md`. In its place, **`./x-posts/PLAYBOOK.md` encodes X's known rules of the game** (hooks, reach suppressors, thread craft, the rookie-mistake checklist). Every agent in this pipeline reads it: the Strategist before planning, the Copywriters while writing, the Editor while scoring. It is the craft baseline that keeps us from naive mistakes. (The base `performance-marketing-agent` still serves other channels; X simply doesn't use it.)

---

## Step 0 — Compute the queue and pick the idea

Identical mechanics to LinkedIn, but the channel token is `"x"`.

**Mode A — Loop / autonomous run** (no idea content in args, or invoked via `/loop`):

1. List files in `../raw-ideas/` (relative to `./x-posts/`). Accept `.md` and `.txt`.
2. Read `./x-posts/TODO.md`. Extract filenames in the **Done** and **In Progress** sections.
3. Compute the X queue:
   ```
   queue = (files in ../raw-ideas/) MINUS (Done filenames) MINUS (In Progress filenames)
   ```
4. Filter: drop any file whose frontmatter declares `channels: [...]` without `"x"` in the list.
5. If queue is empty → print `No new X ideas. Skipping.` and exit. **Generate nothing.**
6. Otherwise pick the **oldest by filename sort** (lexical — `001-` before `002-`).
7. Read the chosen file. Its content (minus frontmatter) is the **raw idea**.
8. Derive `<slug>` from the filename (strip extension AND numeric prefix, kebab-case).

**Mode B — Direct invocation with content in args** (`/x-growth-agent <idea text>`):

1. Treat args as the raw idea.
2. Derive `<slug>` from the first 3–5 meaningful words.
3. Find the next numeric prefix in `../raw-ideas/` and write the idea to `../raw-ideas/<NNN>-<slug>.md` so other channels can also consume it. Then continue.

**N parsing:** if args start with a small integer (`/x-growth-agent 2 ...`), that's N. Otherwise N=3 (the default). Max N=3.

Create the per-post folder `./x-posts/posts/<slug>-<YYYYMMDD>/` and move the idea to **In Progress** in `./x-posts/TODO.md`.

---

## Pipeline overview

```
[Raw Idea from ../raw-ideas/<NNN>-<slug>.md]
    ↓
Strategist (once)           → 01-post-plan.md  (decides SINGLE vs THREAD)
    ↓
Copywriters × N (parallel)  → 02a..02c-draft-*.md   (all write in the chosen format)
    ↓
Editor                      → 03-editor-verdict.json
    ↓ if needs_revision AND round < 2
Copywriter (winner)         → 02-revised-draft.md
    ↓
Editor (final verdict)      → 03-editor-verdict-final.json
    ↓
Image Designer (/image-gen-agent × 2) → impact-1.svg, impact-2.svg
    ↓
[FINAL OUTPUT]              → final-post.md
    ↓
DO NOT touch ../raw-ideas/  (immutable, shared)
Update ./x-posts/TODO.md: move filename from In Progress → Done with link to post folder
```

Max revision rounds: **2**.

---

## Strategist (runs once)

**Job:** Analyze the raw idea → decide the FORMAT → produce a master plan AND define N distinct angles.

**Before planning, read `./x-posts/PLAYBOOK.md`.** It is the X craft baseline (this channel's substitute for a performance loop). Let it shape the format decision, the hook direction, and the angle choices. There is no analytics tracker to read.

### Format decision (X-specific, do this FIRST)

Decide **SINGLE** or **THREAD** and state the verdict + rationale at the top of the plan.

- **Default to SINGLE.** A single tweet is the right unit unless the idea structurally demands more.
- Choose **THREAD** only when the idea genuinely breaks into **≥3 distinct sections** — sequential steps, a numbered list, a multi-part argument, or a before→after→lesson arc that loses meaning when compressed. If you can land the payload in one ≤280-char tweet without gutting it, do that.
- A thread must earn every tweet. 3–7 tweets. No filler. Tweet 1 is a standalone hook that works even if no one expands the thread.

Print `[HANDOFF: STRATEGIST]` AND save to `01-post-plan.md`:

```
## Format Decision
<SINGLE | THREAD> — <one-line rationale: why this idea fits this format; if THREAD, how many tweets and the section breakdown>

## Core Insight
<the central idea in one sentence — the "so what">

## Target Audience
<who specifically — be precise>

## Structure
SINGLE → the one beat the tweet must land.
THREAD → tweet-by-tweet outline:
  1. <hook tweet>
  2. <beat>
  3. <beat>
  ... (3–7 total)

## CTA / Reply hook
<the close. For X, the primary CTA is engagement (a question or a take that invites replies). If the idea has a link, it goes in a REPLY, never the main tweet — note the reply text here.>

## Tone
<punchy | contrarian | tactical | story | analytical>

## Hashtags
None — unless one real community tag genuinely helps. State it or write "none".

## Image Brief
<2–5 numbers/data points or contrast pairs the image should carry · 1 tagline>

## Angle Assignments
X is its own platform — these angles are X-native, not LinkedIn carry-overs. Each targets a DIFFERENT X engagement signal so the three drafts can't collapse into the same tweet. Angles 1 and 2 must read as clearly different posts.

  - **Angle 1 — Viral / reach play (always):** engineered for reposts + bookmarks. One pattern-interrupt or bold, quotable claim that stops the scroll and begs to be screenshotted/re-shared. Sharpest possible hook; strip everything that isn't the punch.
  - **Angle 2 — Build-in-public / story play (always):** a concrete first-person moment — what you did, what happened, what surprised you. Curiosity gap up front, authentic and specific. Targets replies through relatability ("same thing happened to me").
  - **Angle 3 — Contrarian / debate play (at N=3):** a clear, defensible stance against a common belief in the space, framed to invite civil disagreement. Targets replies + quote-tweets — the conversation play. Must be a REAL position drawn from the idea, never manufactured outrage or engagement bait.

When N=2, use Angles 1 and 2 (the two most reliably distinct). When N=3, add Angle 3.

If the idea genuinely can't support a defensible contrarian take, the Strategist MAY swap Angle 3 for a **Tactical/how-to play** (lead with the practical payoff, then the steps — targets bookmarks) or a **Data/proof-point play** (open on the hardest number). State the swap and the one-line reason.
```

---

## Copywriters (N instances, run in parallel)

Run all N simultaneously. Each receives the plan + its assigned angle + the FORMAT decision.

**Read `./x-posts/PLAYBOOK.md` first** — it's the craft baseline every draft must respect (hooks, character economy, reach suppressors, voice). The rules below are the enforced subset; the playbook is the full picture.

**Rules for every X Copywriter:**
- Write in the format the Strategist chose (SINGLE or THREAD).
- **Hard 280-char limit per tweet.** Count characters. A single tweet over 280 is invalid. Each thread tweet over 280 is invalid.
- First ~7 words carry the hook. No "a thread:", no "🧵", no "In this post". Open on the payload.
- Short, declarative lines. Cut every word that isn't load-bearing.
- **No hashtags** unless the plan explicitly named one real community tag.
- **No link in the main tweet/first tweet.** If there's a link, it goes in the reply-hook line (label it `Reply:`).
- For THREAD: number tweets `1/`, `2/`, … (or `1/n`). Each tweet must read as a coherent unit. The last tweet lands the CTA / invites replies.
- End on the CTA from the plan — for X this is usually a question or a take that invites replies, not a "DM me".
- **CTA must be public-shareable** — never offer DM access to internal/proprietary tools.
- Never add ideas not in the plan. Never invent stats, quotes, or claims. Strip company/tool names — keep the lesson.
- No emojis unless Altaf explicitly asks.

Each Copywriter prints its block AND writes its file. File naming `02<x>-draft-<angle-slug>.md`:
- Angle 1 → `02a-draft-viral.md`
- Angle 2 → `02b-draft-story.md`
- Angle 3 → `02c-draft-contrarian.md` (or `02c-draft-tactical.md` / `02c-draft-data.md` if the Strategist swapped Angle 3)

Block format:
```
[HANDOFF: COPYWRITER — <Angle Name>]

Format: <SINGLE | THREAD>

<the tweet, OR the numbered thread — paste-ready>

Reply: <reply-hook text with link, if any — else "none">

---
Angle: <angle name>
Hook: <exact first line>
Char counts: <single: N>  OR  <thread: t1=N, t2=N, ...>  (all must be ≤280)
```

**On revision round** (winner only): print `[HANDOFF: COPYWRITER — REVISED <Angle>]`, save to `02-revised-draft.md` with a `Changes made:` list.

---

## Editor

**Read `./x-posts/PLAYBOOK.md` §9 (the rookie-mistake checklist) and score against it.** The Editor is the gate that catches playbook violations before anything ships.

**Round 1:** score every variant, pick the winner, decide on revision.
**Round 2:** final verdict on the revised draft.

Print `[HANDOFF: EDITOR]` — valid JSON only. Save to `03-editor-verdict.json` (round 1) or `03-editor-verdict-final.json` (round 2):

```json
{
  "round": 1,
  "format": "SINGLE | THREAD",
  "variants_reviewed": ["A", "B", "C"],
  "status": "approved | needs_revision",
  "winner": "A | B | C",
  "why_winner": "<1-2 sentences>",
  "scores": {
    "A": { "hook_strength": 9, "scroll_stop": 8, "conciseness": 9, "authenticity": 8, "cta_clarity": 7, "avg": 8.2 },
    "B": { "hook_strength": 7, "scroll_stop": 7, "conciseness": 8, "authenticity": 9, "cta_clarity": 8, "avg": 7.8 },
    "C": { "hook_strength": 8, "scroll_stop": 8, "conciseness": 8, "authenticity": 8, "cta_clarity": 9, "avg": 8.2 }
  },
  "char_check": { "A": "pass | FAIL (t3=291)", "B": "pass", "C": "pass" },
  "runner_up_notes": { "B": "<what the winner should borrow>" },
  "issues": [
    {
      "type": "weak_hook | over_limit | buries_payload | off_plan | missing_cta | jargon | inauthentic | wrong_format | non_shareable_cta | link_in_main_tweet | has_hashtags",
      "severity": "high | medium | low",
      "description": "<exact problem in the WINNER draft>",
      "action": "<exact fix instruction>"
    }
  ]
}
```

**Hard fails (always `needs_revision` if present in the winner):** any tweet over 280 chars (`over_limit`), a link in the main/first tweet (`link_in_main_tweet`), or unrequested hashtags (`has_hashtags`).

**Decision logic:**
- `approved` → Image Designer
- `needs_revision` AND round < 2 → loop winner through one Copywriter
- round = 2 → output best available, list unresolved issues

---

## Image Designer (runs once, after final post is locked)

**Job:** Generate TWO distinct image variations by invoking `/image-gen-agent` once with `Variations: 2`. Pass `Channel: x` so it uses X formats and styles.

**X dimensions (no portrait):** the image agent should choose between **Landscape 1600×900 (16:9)** — the in-stream default — and **Square 1080×1080 (1:1)** — quote-card. The two variations must differ in BOTH dimension and style.

```
[IMAGE BRIEF]
Channel: x
Variations: 2
Dimensions: reason   ← X options only: 1600×900 (16:9) or 1080×1080 (1:1)
Style hint: reason
Final post: <paste the full final tweet/thread text>
Stats:
  - <label>: <value>
  (from final post + 01-post-plan.md Image Brief; use qualitative contrast pairs if no numbers)
Winning angle: <angle name from editor verdict>
Tagline: <from Image Brief in 01-post-plan.md>
Author: Altaf Shaikh
Handle: @teachmebro
Domain: <e.g. "AI Engineering">
Output path: ./x-posts/posts/<slug>-<YYYYMMDD>/impact
```

The image-gen-agent emits an `[IMAGE REASONING]` block, then generates `impact-1.svg` and `impact-2.svg` (+ `exports/*.png`). Do NOT write SVG inline. Always delegate.

**After image generation, the pipeline is NOT done — immediately proceed to Step N.**

---

## Step N — Finalize and update the queue

**Mandatory every run. Never skip.**

1. **Write `final-post.md`** (template below).
2. **DO NOT touch `../raw-ideas/`.** Immutable, shared.
3. **Update `./x-posts/TODO.md`:** remove from In Progress; prepend a Done line with source filename, post-folder link, date.
4. **Print the final output block.**

---

## `TODO.md` template

```markdown
# X — Queue & Status

This is the X channel's consumption ledger. Raw ideas live in `../raw-ideas/` (shared across all channels). Queue = files in `../raw-ideas/` MINUS the filenames listed under **Done** below.

## Queue (unprocessed for X)
- [ ] <NNN>-<slug>.md — <one-line preview>

## In Progress
- [ ] <NNN>-<slug>.md — started <YYYY-MM-DD>

## Done
- [x] <NNN>-<slug>.md → [posts/<slug>-<YYYYMMDD>/final-post.md](./posts/<slug>-<YYYYMMDD>/final-post.md) — <YYYY-MM-DD>
```

Regenerate the Queue section each run. Append to Done; never delete a Done entry unless the user asks to re-run an idea.

---

## `final-post.md` template

```markdown
# <slug>

**Source idea:** [../../../raw-ideas/<NNN>-<slug>.md](../../../raw-ideas/<NNN>-<slug>.md)
**Generated:** <YYYY-MM-DD>
**Format:** <SINGLE | THREAD>  ·  **Rounds:** <1 or 2>  ·  **Revised:** <yes/no>

## Variation Scores (Round 1)

| Variant | Angle | Hook | Scroll-stop | Conciseness | Authenticity | CTA | Avg |
|---------|-------|------|-------------|-------------|--------------|-----|-----|
| A       | Viral | 9 | 8 | 9 | 8 | 7 | 8.2 |
| B       | Story | 7 | 7 | 8 | 9 | 8 | 7.8 |
| C       | Contrarian | 8 | 8 | 8 | 8 | 9 | 8.2 |

**Winner:** Variant <X> — <why_winner>

---

## Final Post

<SINGLE → the one tweet, paste-ready (≤280 chars)>
<THREAD → numbered tweets 1/ 2/ 3/ …, each ≤280, paste-ready>

**Reply (post after the main tweet):** <reply-hook text + link, or "none">

---

## Images

| File | Format | Style | Carries |
|------|--------|-------|---------|
| [impact-1.svg](./impact-1.svg) | <W>×<H> (<16:9 Landscape \| 1:1 Square>) | <style name> | <stats/elements> |
| [impact-2.svg](./impact-2.svg) | <W>×<H> (<16:9 Landscape \| 1:1 Square>) | <style name> | <stats/elements> |

**Exported PNGs:** `exports/impact-1.png` · `exports/impact-2.png`

---

**Unresolved issues:** <list or "none">
```

---

## Conversation output (every run)

**No-op:**
```
No new X ideas. Skipping.
```

**Processed an idea:**
```
Channel: X
Processed: <NNN>-<slug>.md
Format: <SINGLE | THREAD>
Post folder: ./x-posts/posts/<slug>-<YYYYMMDD>/
Final post: ./x-posts/posts/<slug>-<YYYYMMDD>/final-post.md
Images (SVG): impact-1.svg · impact-2.svg
Images (PNG): exports/impact-1.png · exports/impact-2.png
Queue remaining (X): <N> idea(s)
```

---

## Loop integration (`/loop`)

Wrapped by `../x.agent.md`:
```
/loop 1d <paste x.agent.md prompt>
```
Each firing: computes X queue (`../raw-ideas/` MINUS TODO.md Done + In Progress), processes ONE idea if non-empty, no-ops silently if empty, never re-processes a Done filename, respects `channels:` frontmatter. Other channels keep independent queues against the same shared library.

---

## Shared rules (all agents)

Identical to `linkedin-growth-agent`'s shared-rules section — plus the X-specific hard rules: 280-char ceiling per tweet, no hashtags by default, links only in replies, hook in the first ~7 words. Never write outside `./x-posts/` (except Mode B may write ONE new file to `../raw-ideas/`). Never move, rename, or delete anything in `../raw-ideas/`.
