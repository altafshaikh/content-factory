# CLAUDE.md — LinkedIn channel

Briefs any Claude session that opens work inside `./linkedin-posts/`. Read this AND the [parent CLAUDE.md](../CLAUDE.md) before acting.

---

## What this folder is

The LinkedIn channel of the multi-channel content factory. Consumes ideas from `../raw-ideas/` (shared library, immutable) and produces posts + images here.

Channel overview: [`README.md`](./README.md).
Loop prompt: [`../linkedin.agent.md`](../linkedin.agent.md).
Full skill definition: `~/.claude/skills/linkedin-growth-agent/SKILL.md`.

---

## Hard rules (LinkedIn-specific)

1. **`../raw-ideas/` is read-only from this folder's perspective.** Never move, rename, or delete files there. The library is shared with other channels.
2. **All writes stay inside `./linkedin-posts/`.** No exceptions.
3. **Consumption is tracked in `./TODO.md`** — not on the filesystem of `../raw-ideas/`. Queue = `ls ../raw-ideas/` MINUS the filenames in this channel's Done + In Progress sections.
4. **Never invent statistics, quotes, or claims** that aren't in the source raw idea file.
5. **Strip company names, internal tool names, and private details.** Keep the lesson; drop the specifics.
6. **CTA must be public-shareable.** No "DM me to try the tool" if the tool is internal. Use a builder-identity hook or open question instead.
7. **One idea per run.** Even if queue has many, drain exactly one. Manual invocations also drain one.
8. **Every handoff is BOTH printed in the conversation AND saved to the per-post folder.** Never one without the other.
9. **No emojis** unless the user explicitly asks.
10. **Respect `channels:` frontmatter.** If a raw idea declares `channels: [...]` and "linkedin" is not in the list, skip it silently.

---

## Decision shortcuts

| User says...                                          | Do this                                                                |
|-------------------------------------------------------|------------------------------------------------------------------------|
| "process my LinkedIn ideas" / "/linkedin-growth-agent"| Trigger the `linkedin-growth-agent` skill                              |
| "run the loop" inside this folder                     | Use `../linkedin.agent.md` prompt                                      |
| Drops a new file in `../raw-ideas/`                   | "Queued. Next loop tick picks it up — or invoke `/linkedin-growth-agent` to run now." |
| Edit a shipped post                                   | Edit `posts/<slug>-<date>/final-post.md` directly. Do NOT re-run pipeline unless asked. |
| Redo an idea on LinkedIn                              | Remove its line from `TODO.md` Done section. Then trigger the skill.   |
| `TODO.md` drifts out of sync                          | Rebuild Queue section: `ls ../raw-ideas/` minus Done+In-Progress filenames. Leave Done untouched. |
| `../raw-ideas/` empty (relative to this channel's done) | Print "No new LinkedIn ideas. Skipping." Stop.                       |
| "add performance data" / drops CSV in csv-imports/    | Run `/linkedin-growth-agent` — Agent 0 will detect and process the CSV automatically. |
| "how do I export from LinkedIn?"                      | Point to [`performance/HOWTO.md`](./performance/HOWTO.md).             |
| "what's working?" / "show me patterns"                | Read [`performance/tracker.md`](./performance/tracker.md) Pattern Summary section. |

---

## Pipeline contract (quick reference)

```
[csv-imports/ has new files?]
  → Agent 0: Performance Sync         → performance.md per post + tracker.md

../raw-ideas/<NNN>-<slug>.md
  → Agent 1: Strategist               → 01-post-plan.md  (reads tracker.md first)
  → Copywriters × N parallel          → 02a-..., 02b-..., 02c-... (if N≥3)
  → Editor                            → 03-editor-verdict.json
  → [revision loop, max 2 rounds]
  → Image Designer                    → impact.svg (1080×1350 default)
  → final-post.md
  → TODO.md: move entry to Done section (DO NOT move source file)
```

Default N=2. User can override to 3 or 4. When N=3, Strategist picks Angle C adaptively (vulnerability / tactical / comparison / data-first / contrarian) — see SKILL.md for the decision tree.

---

## Image defaults

- **Format:** Vertical 1080×1350 (4:5) — best LinkedIn mobile feed coverage
- **Style:** Dark gradient bg (`#0a0e1a → #111827`), cyan→violet accent (`#22d3ee → #a78bfa`)
- **Carries:** 3-4 big-number tiles + tagline + byline
- **No emojis, no logos, no company names** unless explicitly requested
- Keep exported PNG under 5 MB

---

## When to push back

- Asked to add stats not in the raw idea → ask for source
- Asked for a "DM me" CTA tied to an internal tool → suggest builder-identity hook
- Asked to skip the Editor / publish a 02a-... draft directly → push back, Editor exists to catch authenticity issues
- Asked to move a file out of `../raw-ideas/` → refuse, it's shared and immutable

---

## What NOT to do

- Don't re-read the source idea on every step — read it once at pipeline start, pass it through handoffs
- Don't create README/index files inside individual `posts/<slug>-<date>/` folders — `final-post.md` is the index
- Don't write into `../raw-ideas/` or `../raw-ideas/processed/` (the latter no longer exists — `raw-ideas/` is immutable)
- Don't auto-commit or auto-push
- Don't suggest folding LinkedIn into another channel's folder
