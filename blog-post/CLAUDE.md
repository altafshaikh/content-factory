# CLAUDE.md — Blog channel

Briefs any Claude session that opens work inside `./blog-post/`. Read this AND the [parent CLAUDE.md](../CLAUDE.md) before acting.

---

## What this folder is

The Blog channel of the multi-channel content factory. Consumes ideas from `../raw-ideas/` (shared library, immutable) and produces Hashnode-ready blog posts here.

Channel overview: [`README.md`](./README.md).
Loop prompt: [`../blog.agent.md`](../blog.agent.md).
Full skill definition: `.claude/skills/blog-writer-agent/SKILL.md`.

---

## Hard rules (Blog-specific)

1. **`../raw-ideas/` is read-only from this folder's perspective.** Never move, rename, or delete files there. The library is shared with other channels.
2. **All writes stay inside `./blog-post/`.** No exceptions.
3. **Consumption is tracked in `./TODO.md`** — not on the filesystem of `../raw-ideas/`. Queue = `ls ../raw-ideas/` MINUS the filenames in this channel's Done + In Progress sections.
4. **Never invent statistics, quotes, or claims** that aren't in the source raw idea file.
5. **Strip company names, internal tool names, and private details.** Keep the lesson; drop the specifics.
6. **One idea per run.** Even if queue has many, drain exactly one. Manual invocations also drain one.
7. **Every handoff is BOTH printed in the conversation AND saved to the per-post folder.** Never one without the other.
8. **No emojis** unless the user explicitly asks.
9. **Respect `channels:` frontmatter.** If a raw idea declares `channels: [...]` and "blog" is not in the list, skip it silently.
10. **No interactive pauses.** The pipeline runs end-to-end (5 phases) without waiting for confirmation. Altaf reviews by editing `final-post.md` directly.

---

## Decision shortcuts

| User says...                                         | Do this                                                                |
|------------------------------------------------------|------------------------------------------------------------------------|
| "process my blog ideas" / "/blog-writer-agent"       | Trigger the `blog-writer-agent` skill                                  |
| "run the loop" inside this folder                    | Use `../blog.agent.md` prompt                                          |
| Drops a new file in `../raw-ideas/`                  | "Queued. Next loop tick picks it up — or invoke `/blog-writer-agent` to run now." |
| Edit a shipped post                                  | Edit `posts/<slug>/final-post.md` directly. Do NOT re-run pipeline unless asked. |
| Want a different title                               | Edit `final-post.md` frontmatter. Title options are in `02-title-options.md`. |
| Redo an idea on Blog                                 | Remove its line from `TODO.md` Done section. Then trigger the skill.   |
| `TODO.md` drifts out of sync                         | Rebuild Queue section: `ls ../raw-ideas/` minus Done+In-Progress filenames. Leave Done untouched. |
| `../raw-ideas/` empty (relative to this channel)     | Print "No new blog ideas. Skipping." Stop.                             |

---

## Pipeline contract (quick reference)

```
../raw-ideas/<NNN>-<slug>.md
  → Phase 1: Content Writer    → 01-content.md  (full blog body, narrative arc)
  → Phase 2: Title Generator   → 02-title-options.md  (6-8 options + recommendation)
  → Phase 3: Banner Prompt     → 03-banner-prompt.md  (image gen prompt, not the image)
  → Phase 4: SEO               → 04-seo.md  (seo_title + seo_description)
  → Phase 5: Final Assembly    → final-post.md  (complete Hashnode-ready .md)
  → TODO.md: move entry to Done section (DO NOT move source file)
```

All five phases run sequentially, end-to-end, without interactive pauses.

---

## Post folder structure

```
blog-post/posts/<slug>/
├── 01-content.md        ← full blog body (narrative arc)
├── 02-title-options.md  ← 6-8 title options grouped by angle + recommendation
├── 03-banner-prompt.md  ← image generation prompt for Midjourney / DALL·E / Ideogram
├── 04-seo.md            ← seo_title + seo_description
└── final-post.md        ← complete Hashnode-ready .md (frontmatter + content)
```

---

## When to push back

- Asked to add stats not in the raw idea → ask for source
- Asked to publish a phase output directly without final assembly → push back, Phase 5 is the publish artifact
- Asked to move a file out of `../raw-ideas/` → refuse, it's shared and immutable
- Asked to generate a banner image → produce only the prompt (Phase 3), never the image itself

---

## What NOT to do

- Don't re-read the source idea on every phase — read it once at pipeline start, pass it through
- Don't create README/index files inside individual `posts/<slug>/` folders — `final-post.md` is the index
- Don't write into `../raw-ideas/`
- Don't auto-commit or auto-push
- Don't suggest folding Blog into another channel's folder
