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
3. **Channels don't WRITE to each other.** A channel never writes into, moves, renames, or deletes anything in another channel's folder. **Read-only cross-channel signal is allowed** as an advisory input: e.g. the X channel (which has no analytics on a free account) may READ the LinkedIn channel's `TODO.md` and a post's `performance.md` to judge topic fit and borrow what performed. Reads are advisory only; writes stay isolated to the channel's own folder.
4. **Never invent statistics, quotes, or claims** that aren't in the source raw idea file.
5. **Strip company names, internal tool names, and private details** from any generated content unless explicitly told otherwise.
6. **No emojis** in generated content unless the user explicitly asks.
7. **Filesystem is the source of truth.** Don't invent sidecar state files or JSON manifests. `TODO.md` per channel is enough.
8. **Code ships to the FORK, not personal.** The fork `altaf-shaikh-cs/content-factory` is the single integration point — cloud routines clone it, and you merge content into it. Push code/config changes with `bash scripts/deploy-code.sh` (after committing locally). The personal repo `altafshaikh/content-factory` (this local `origin`) is a downstream MIRROR, refreshed by `bash scripts/mirror-personal.sh` (also the daily cron). **Don't `git push origin main` for code** — that diverges the mirror. Push to the fork; the mirror follows. See **Deploy & routines** below.

---

## Deploy & routines

The daily channel runs are **cloud routines** (scheduled Claude Code agents), not local cron. Each clones the **fork** `altaf-shaikh-cs/content-factory` (a fork of this repo's `origin`, `altafshaikh/content-factory`), runs the channel's growth-agent skill, and opens a PR on the fork for review.

**The fork is the single integration point. The personal repo is a downstream mirror.** Everything — generated content AND code — lands on the fork's `main` first; personal `main` is fast-forwarded from it. This is the clean topology because the cloud's `gh` is authenticated for the fork (the work account owns it) but NOT for the personal upstream, so the routine can open its own review PR on the fork but never could on personal.

**Repo visibility:** `altafshaikh/content-factory` is **PUBLIC** (assumed private earlier; it is not). The mirror fetches the fork over https with no auth.

**Three moving parts:**

- **Content (routine → fork PR):** each routine picks the next item, derives a STABLE idea slug (not a date), and — if no open PR already covers that idea and there's something new worth producing — pushes a `claude/<channel>-<slug>` branch to the fork and opens a **within-fork PR** into the fork's own `main`. If the idea already has an open PR, or nothing new is worth producing, it stops without creating a PR. You review + merge on the fork; unmerged PRs just stay open. (Idempotent: re-running the next day won't duplicate an in-flight idea.)
- **Code (you → fork):** commit locally, then `bash scripts/deploy-code.sh` pushes to the fork's `main` (via the `fork` remote / work SSH key). Routines pick it up on their next run. **Never `git push origin main`** — that puts commits on personal the fork lacks and breaks the mirror's fast-forward.
- **Mirror (fork → personal):** `bash scripts/mirror-personal.sh` fast-forwards personal `main` from the fork's `main`. Runs daily at 11:00 AM via a launchd agent, and safe to run by hand. Non-destructive (only fetches the fork + pushes `origin/main`). Mac-awake only; if asleep, run it by hand — nothing is lost since the fork is the source of truth. See [`scripts/launchd/README.md`](./scripts/launchd/README.md).

**Deploy path for any repo change a routine depends on:**
1. Commit locally on `main`.
2. `bash scripts/deploy-code.sh` (push to the fork's `main`).
3. (optional) `bash scripts/mirror-personal.sh` to refresh the public mirror now instead of waiting for the cron.

A change is live for the routines once step 2 completes (their next run clones the fork).

**Set up / change a routine:** use the repo-scoped skill `setup-channel-routine` (`.claude/skills/setup-channel-routine/SKILL.md`) — `/setup-channel-routine <linkedin|x|instagram>`. It bakes in the canonical config (environment, fork repo, tools, no MCP connectors, the within-fork-PR prompt) and staggered schedules. Manage/disable routines at https://claude.ai/code/routines.

| Channel | Routine name | Schedule (IST) |
|---------|--------------|----------------|
| LinkedIn | Daily Linkedin Post Creator | 8:30 PM |
| Instagram | Daily Instagram Reel Creator | 9:00 PM |
| X | Daily X Post Creator | 10:00 AM |

---

## Routing — what to trigger for what

| User says...                                  | Trigger                                                                 |
|-----------------------------------------------|-------------------------------------------------------------------------|
| "LinkedIn post" / "/linkedin-growth-agent"    | Skill `linkedin-growth-agent` (writes into `linkedin-posts/`)           |
| "X post" / "tweet" / "thread"                 | Skill `x-growth-agent` (writes into `x-posts/`)                         |
| "reel" / "Instagram" / "suggest reels" / "/instagram-reels-agent" | Skill `instagram-reels-agent` (writes into `instagram-reels/`) |
| "blog post" / "write a blog"                  | Skill `idea-to-blog` (writes into `blog-post/`)                         |
| "presentation" / "slides" / "deck"            | Skill `idea-to-presentation` then `anthropic-skills:pptx`              |
| "add an idea" / "new idea: ..."               | Write to `./raw-ideas/<NNN>-<slug>.md` with the next available prefix   |
| "sync my notes" / "sync the inbox" / "/sync-inspiration" | Skill `sync-inspiration` (processes all files in `inspiration-inbox/` into `raw-ideas/`) |
| "process my ideas" (ambiguous)                | Ask which channel, OR run all active channel loops in sequence          |
| "/loop"                                       | Use the loop prompt file matching the channel (e.g. `linkedin.agent.md`)|
| "generate image" / "redo the image" / "/image-gen-agent" | Skill `image-gen-agent` (reads `./agents/image-gen/inspiration/`) |
| "sync the mirror" / "update personal repo" / "/mirror-personal" | Skill `mirror-personal` (runs `scripts/mirror-personal.sh`) |

---

## Shared agents

Agents that serve all channels live in `./agents/`. They are not channels — they produce no posts — they are shared services called by channel pipelines.

| Agent | Folder | Skill | What it does |
|-------|--------|-------|--------------|
| image-gen | `agents/image-gen/` | `.claude/skills/image-gen-agent/SKILL.md` | Generates on-brand SVGs for any channel. Reads inspiration library, picks style, produces SVG. |

**To edit an agent's behavior:** open its folder, read `AGENT.md` — it points to the project-local skill file.
**To add inspiration styles:** drop a file (SVG/PNG/JPG/PDF/screenshot) into `agents/image-gen/inspiration/<style-slug>/` and add a row to `MANIFEST.md`.

---

## Quick idea capture

For low-friction capture, drop rough notes into any file in `./inspiration-inbox/` (separate multiple ideas within a file with a `---` line). `inbox.md` is the default scratch file; you can also drop in any `.md` file (e.g. a screenshot-to-text paste, a dedicated topic file). Run `/sync-inspiration` to process every file in the folder: it fetches any URLs, synthesizes context, promotes each idea into `./raw-ideas/<NNN>-<slug>.md`, clears `inbox.md`, and deletes other processed files. `inspiration-inbox/` is a mutable scratch folder — only the promoted files in `raw-ideas/` are immutable.

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
