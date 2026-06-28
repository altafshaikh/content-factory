# X (Twitter) Channel

The X pipeline of the [content-factory](../README.md) multi-channel factory. Consumes ideas from the shared `../raw-ideas/` library and produces publish-ready tweets / threads + images.

---

## Folder layout

```
x-posts/
├── README.md                        ← you are here
├── CLAUDE.md                        ← AI agent contract (X-specific)
├── PLAYBOOK.md                      ← X best-practices; the craft baseline (read every run)
├── TODO.md                          ← queue + done ledger for this channel
└── posts/
    └── <slug>-<YYYYMMDD>/
        ├── 01-post-plan.md          ← Strategist output (incl. SINGLE vs THREAD decision)
        ├── 02a-draft-viral.md       ← Copywriter 1 — Viral / reach play
        ├── 02b-draft-story.md       ← Copywriter 2 — Story / build-in-public
        ├── 02c-draft-contrarian.md  ← Copywriter 3 — Contrarian / debate (N=3 default)
        ├── 03-editor-verdict.json   ← Editor round 1
        ├── 02-revised-draft.md      ← (only if revision round)
        ├── 03-editor-verdict-final.json ← (only if revision round)
        ├── impact-1.svg             ← Image concept 1 (16:9 or 1:1)
        ├── impact-2.svg             ← Image concept 2 (different format)
        └── final-post.md            ← 👈 PUBLISH THIS
```

Source ideas live ONE FOLDER UP at `../raw-ideas/`. They are shared with the LinkedIn, Blog, and Presentation channels.

---

## Pipeline

```
../raw-ideas/<NNN>-<slug>.md
        ↓
Strategist (decides SINGLE vs THREAD → 01-post-plan.md)
        ↓
3 Copywriters in parallel (1: viral/reach · 2: story/build-in-public · 3: contrarian/debate)
        ↓
Editor (scores all, picks winner, hard-fails any tweet >280 / link-in-body / hashtags — max 2 rounds)
        ↓
Image Designer — invokes /image-gen-agent (Channel: x) TWICE:
  impact-1.svg  (16:9 or 1:1)
  impact-2.svg  (the other format)
  Both carry @teachmebro handle in accent color
        ↓
posts/<slug>-<YYYYMMDD>/final-post.md   ← publish-ready
```

**X output format (the big difference from LinkedIn):**

| Format | When chosen |
|--------|-------------|
| **Single tweet** (default) | The idea lands in one ≤280-char beat without gutting it |
| **Thread** (3–7 tweets) | The idea genuinely breaks into ≥3 distinct sections / steps / a multi-part arc |

**X image formats (selected automatically):**

| Format | Dimensions | When chosen |
|--------|------------|-------------|
| Landscape | 1600×900 (16:9) | In-stream default; big single-statement tweets |
| Square | 1080×1080 (1:1) | Quote-card tone, mobile-first versatility |

The two concepts always use **different formats**.

---

## Consumption model

`../raw-ideas/` is **immutable** — files never move. This X channel tracks consumption via the **Done** section in [`TODO.md`](./TODO.md). The same idea can also be consumed by LinkedIn, the blog, etc. — those channels track independently in their own `TODO.md`.

An X queue at runtime =
```
ls ../raw-ideas/  MINUS  filenames in TODO.md "Done" + "In Progress" sections
```

---

## Daily workflow

**Loop runs (see [`../x.agent.md`](../x.agent.md)):**
1. Computes queue
2. Picks oldest unconsumed idea
3. Triggers `/x-growth-agent`
4. Updates `TODO.md` Done section

**You publish:**
1. Open `posts/<slug>-<date>/final-post.md`
2. Copy the "Final Post" section → paste into X (single tweet, or post the thread tweet-by-tweet)
3. If there's a `Reply:` line, post it as the first reply to your own tweet (this is where links go)
4. Pick your image — `impact-1.svg` or `impact-2.svg` — and export to PNG:
   ```bash
   brew install librsvg   # once
   rsvg-convert -w 1600 -h 900 impact-1.svg -o impact-1.png    # 16:9
   rsvg-convert -w 1080 -h 1080 impact-2.svg -o impact-2.png   # 1:1
   ```
5. Attach PNG, ship.

---

## Re-running an idea on X

Remove the idea's line from `TODO.md` Done section. Next loop tick will re-queue it.

## Restricting an idea to specific channels

In the raw idea file (`../raw-ideas/NNN-slug.md`), add frontmatter:
```yaml
---
channels: [x]
---
```
Only listed channels will consume the idea. If frontmatter is absent, all channels can consume.

---

## The skill & the playbook

- Generation pipeline: `.claude/skills/x-growth-agent/SKILL.md`
- Craft baseline: [`PLAYBOOK.md`](./PLAYBOOK.md)

> **No performance loop — the playbook is its replacement.** Free X account = no analytics export, so there's no tracker or feedback agent. Instead, [`PLAYBOOK.md`](./PLAYBOOK.md) encodes X's known rules of the game (hooks, reach suppressors, thread craft, a rookie-mistake checklist). The Strategist, Copywriters, and Editor all read it every run, so we craft from what's known about the platform rather than guessing. Keep it sharp as you learn X.
