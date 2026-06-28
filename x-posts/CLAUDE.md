# CLAUDE.md — X (Twitter) channel

Briefs any Claude session that opens work inside `./x-posts/`. Read this AND the [parent CLAUDE.md](../CLAUDE.md) before acting.

---

## What this folder is

The X (Twitter) channel of the multi-channel content factory. Consumes ideas from `../raw-ideas/` (shared library, immutable) and produces tweets / threads + images here.

Channel overview: [`README.md`](./README.md).
Craft baseline: [`PLAYBOOK.md`](./PLAYBOOK.md) — X best-practices, read every run (this channel's substitute for an analytics loop).
Loop prompt: [`../x.agent.md`](../x.agent.md).
Full skill definition: `.claude/skills/x-growth-agent/SKILL.md`.

---

## Hard rules (X-specific)

1. **`../raw-ideas/` is read-only from this folder's perspective.** Never move, rename, or delete files there. Shared with other channels.
2. **All writes stay inside `./x-posts/`.** No exceptions.
3. **Consumption is tracked in `./TODO.md`** — Queue = `ls ../raw-ideas/` MINUS the filenames in this channel's Done + In Progress sections.
4. **280 characters HARD per tweet.** Single tweet ≤ 280. Every thread tweet ≤ 280. Over-limit = invalid, never ship it.
5. **Single tweet by default. Thread only when the idea breaks into ≥3 distinct sections.** The Strategist decides and states the rationale.
6. **No hashtags by default.** They suppress reach and read as spam on X. At most 1, only if it's a real live community tag.
7. **Links go in a reply, never the main tweet.** X downranks tweets with external links in the body.
8. **Hook lives in the first ~7 words.** No "a thread 🧵", no "In this post". Open on the payload.
9. **Never invent statistics, quotes, or claims** not in the source raw idea file.
10. **Strip company names, internal tool names, and private details.** Keep the lesson; drop the specifics.
11. **CTA must be public-shareable.** No "DM me to try the tool" for internal tooling. Prefer a reply-inviting question or a builder take.
12. **One idea per run.** Even if queue has many, drain exactly one.
13. **Every handoff is BOTH printed in the conversation AND saved to the per-post folder.** Never one without the other.
14. **No emojis** unless the user explicitly asks.
15. **Respect `channels:` frontmatter.** If a raw idea declares `channels: [...]` and "x" is not in the list, skip it silently.

---

## Decision shortcuts

| User says...                                       | Do this                                                                |
|----------------------------------------------------|------------------------------------------------------------------------|
| "process my X ideas" / "/x-growth-agent"           | Trigger the `x-growth-agent` skill                                    |
| "write a tweet" / "draft a thread about X"         | Trigger the `x-growth-agent` skill                                    |
| "run the loop" inside this folder                  | Use `../x.agent.md` prompt                                            |
| Drops a new file in `../raw-ideas/`                | "Queued. Next loop tick picks it up — or invoke `/x-growth-agent` to run now." |
| Edit a shipped tweet/thread                        | Edit `posts/<slug>-<date>/final-post.md` directly. Don't re-run pipeline unless asked. |
| Redo an idea on X                                  | Remove its line from `TODO.md` Done section. Then trigger the skill.  |
| `TODO.md` drifts out of sync                       | Rebuild Queue: `ls ../raw-ideas/` minus Done+In-Progress. Leave Done untouched. |
| `../raw-ideas/` empty (relative to this channel)   | Print "No new X ideas. Skipping." Stop.                              |
| "add performance data" / "what's working?"         | No analytics on free X. Point to [`PLAYBOOK.md`](./PLAYBOOK.md) — the encoded best-practices that replace a data loop. |
| "what are the rules?" / "X best practices"          | Read / update [`PLAYBOOK.md`](./PLAYBOOK.md). |

---

## Pipeline contract (quick reference)

```
../raw-ideas/<NNN>-<slug>.md
  → Agent 1: Strategist              → 01-post-plan.md  (decides SINGLE vs THREAD)
  → Copywriters × N parallel         → 02a-draft-viral, 02b-draft-story, 02c-draft-contrarian
  → Editor                           → 03-editor-verdict.json  (hard-fails over-limit / link-in-body / hashtags)
  → [revision loop, max 2 rounds]
  → Image Designer (/image-gen-agent) → impact-1.svg + impact-2.svg (X dims: 16:9 / 1:1)
                                       → exports/impact-1.png + exports/impact-2.png
  → final-post.md
  → TODO.md: move entry to Done (DO NOT move source file)
```

**Default N=3 — three X-native angles, each targeting a different engagement signal:**
- **Angle 1 — Viral / reach play:** bold quotable claim engineered for reposts + bookmarks.
- **Angle 2 — Story / build-in-public:** concrete first-person moment → drives replies via relatability.
- **Angle 3 — Contrarian / debate:** a defensible stance against a common belief → drives replies + quote-tweets.

Angles 1 and 2 must read as clearly different posts. Override with `/x-growth-agent 2` to drop the contrarian angle. If the idea can't support a real contrarian take, the Strategist may swap Angle 3 for a Tactical/how-to or Data/proof-point play (and says so). See SKILL.md.

---

## Image defaults (X)

- **Variations:** 2 per post — different dimension AND style, reasoned from content.
- **Formats available:** Landscape 1600×900 (16:9, in-stream default) · Square 1080×1080 (1:1, quote-card). **No portrait.**
- **SVGs:** saved in the post folder (`impact-1.svg`, `impact-2.svg`).
- **PNGs:** auto-converted into `exports/`.
- **No emojis, no logos, no company names** unless explicitly requested.

---

## When to push back

- Asked to add stats not in the raw idea → ask for source.
- Asked to put a link in the main tweet → refuse, links go in a reply.
- Asked to add hashtags → push back unless it's one real community tag.
- Asked to ship a tweet over 280 chars → refuse, tighten it.
- Asked to skip the Editor → push back, it catches over-limit and authenticity issues.
- Asked to move a file out of `../raw-ideas/` → refuse, it's shared and immutable.

---

## What NOT to do

- Don't re-read the source idea on every step — read once at pipeline start, pass through handoffs.
- Don't create README/index files inside individual `posts/<slug>-<date>/` folders — `final-post.md` is the index.
- Don't write into `../raw-ideas/`.
- Don't auto-commit or auto-push.
- Don't suggest folding X into another channel's folder.
