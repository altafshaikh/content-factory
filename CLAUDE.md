# CLAUDE.md — content-stratergy (top level)

Briefs any Claude session that opens this project. Read before doing anything here.

---

## What this project is

A multi-channel content factory. One shared pool of raw ideas at `./raw-ideas/`. Each channel (LinkedIn, X, blog, presentations) consumes ideas independently via its own daily loop and its own skill.

Full overview: [`README.md`](./README.md).

---

## Hard rules (apply project-wide)

1. **`./raw-ideas/` is immutable.** Files are never moved out, deleted, or renamed by any agent. Each channel tracks its own consumption in its own `TODO.md`. The library is append-only.
2. **One channel = one folder = one CLAUDE.md.** When working on LinkedIn output, stay inside `linkedin-posts/`. Don't write LinkedIn artifacts into `x-posts/` or vice versa.
3. **Channels don't talk to each other.** They share only `./raw-ideas/`. No cross-channel imports, no shared scratch space.
4. **Never invent statistics, quotes, or claims** that aren't in the source raw idea file.
5. **Strip company names, internal tool names, and private details** from any generated content unless explicitly told otherwise.
6. **No emojis** in generated content unless the user explicitly asks.
7. **Filesystem is the source of truth.** Don't invent sidecar state files or JSON manifests. `TODO.md` per channel is enough.

---

## Routing — what to trigger for what

| User says...                                  | Trigger                                                                 |
|-----------------------------------------------|-------------------------------------------------------------------------|
| "LinkedIn post" / "/linkedin-growth-agent"    | Skill `linkedin-growth-agent` (writes into `linkedin-posts/`)           |
| "X post" / "tweet" / "thread"                 | Skill `x-growth-agent` (writes into `x-posts/`)                         |
| "blog post" / "write a blog"                  | Skill `idea-to-blog` (writes into `blog-post/`)                         |
| "presentation" / "slides" / "deck"            | Skill `idea-to-presentation` then `anthropic-skills:pptx`              |
| "add an idea" / "new idea: ..."               | Write to `./raw-ideas/<NNN>-<slug>.md` with the next available prefix   |
| "process my ideas" (ambiguous)                | Ask which channel, OR run all active channel loops in sequence          |
| "/loop"                                       | Use the loop prompt file matching the channel (e.g. `linkedin.agent.md`)|
| "generate image" / "redo the image" / "/image-gen-agent" | Skill `image-gen-agent` (reads `./agents/image-gen/inspiration/`) |

---

## Shared agents

Agents that serve all channels live in `./agents/`. They are not channels — they produce no posts — they are shared services called by channel pipelines.

| Agent | Folder | Skill | What it does |
|-------|--------|-------|--------------|
| image-gen | `agents/image-gen/` | `.claude/skills/image-gen-agent/SKILL.md` | Generates on-brand SVGs for any channel. Reads inspiration library, picks style, produces SVG. |

**To edit an agent's behavior:** open its folder, read `AGENT.md` — it points to the project-local skill file.
**To add inspiration styles:** drop a file (SVG/PNG/JPG/PDF/screenshot) into `agents/image-gen/inspiration/<style-slug>/` and add a row to `MANIFEST.md`.

---

## Idea-file conventions

- **Naming:** `NNN-<kebab-slug>.md` where `NNN` is a 3-digit ordering prefix. `001-` runs before `002-`. Lexical sort wins.
- **Contents:** anything — rough notes, transcripts, bullet dumps, voice-memo paste. The channel skill's Strategist agent figures out structure.
- **Optional frontmatter:** if the user wants to restrict an idea to specific channels, add:
  ```
  ---
  channels: [linkedin, blog]   # only these channels will consume it; others skip
  ---
  ```
  If absent, all channels can consume it.

---

## Adding a new channel (procedure)

1. Create `<channel>-posts/` (or similar) with:
   - `CLAUDE.md` — channel-specific behavior contract
   - `README.md` — human onboarding
   - `TODO.md` — Queue + In Progress + Done sections
   - `posts/` — empty, will fill with per-idea folders
2. Create or install a skill at `.claude/skills/<channel>-growth-agent/SKILL.md`.
3. Create `<channel>.agent.md` at the top level — the `/loop` prompt for that channel. Reference [`linkedin.agent.md`](./linkedin.agent.md) as the template.
4. Update the **Channels — current status** table in this project's `README.md`.

---

## Don't do

- Don't move or delete anything in `./raw-ideas/`
- Don't write outside the relevant channel folder when working on a single channel
- Don't auto-commit or auto-push unless explicitly asked
- Don't suggest folding multiple channels into one folder — the multi-channel structure is intentional
- Don't create new top-level folders without being asked
