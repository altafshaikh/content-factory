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
8. **Every push must sync the fork.** The cloud routines clone the FORK `altaf-shaikh-cs/content-factory`, not this local `origin` (`altafshaikh/content-factory`). After ANY `git push origin main`, immediately run `bash scripts/sync-fork.sh` so the routines run current code. See **Deploy & routines** below. Don't consider a change "shipped" until the fork is synced.

---

## Deploy & routines

The daily channel runs are **cloud routines** (scheduled Claude Code agents), not local cron. Each clones the **fork** `altaf-shaikh-cs/content-factory` (a fork of this repo's `origin`, `altafshaikh/content-factory`), runs the channel's growth-agent skill, and pushes its output to a `claude/<channel>-<date>` branch on the fork.

**Repo visibility:** `altafshaikh/content-factory` is **PUBLIC**. (It was assumed private earlier; it is not.) This is why the routine can `git fetch` it with no auth. If you want it private, the routine self-sync below must switch to an authenticated fetch.

**Personal `main` is the single source of truth. Three moving parts:**

- **Routine self-sync (down, at generation time) — PRIMARY:** the first thing each routine does is `git fetch https://github.com/altafshaikh/content-factory.git main && git reset --hard FETCH_HEAD`, so it always generates against current upstream regardless of how stale the fork is. No dependence on the Mac or on cron timing. (Works because the repo is public.)
- **Content up (fork → personal):** the routine pushes a `claude/<channel>-<date>` branch to the fork — it does NOT open the PR (the cloud's `gh` isn't authenticated for the upstream). The PR is opened **from your local machine** (which has the personal token) by `scripts/open-content-prs.sh`. You review + merge; unreviewed PRs just stay open.
- **The 11:00 AM cron** (`scripts/daily-content-sync.sh`, run by a launchd agent) does, in order: (1) `sync-fork.sh` — fast-forward the fork's `main` from personal (picks up whatever you merged since), then (2) `open-content-prs.sh` — open PRs for any new fork content branches. Only fires when the Mac is awake; if it's asleep, run `bash scripts/daily-content-sync.sh` by hand — nothing is lost (branches accumulate until pulled). See [`scripts/launchd/README.md`](./scripts/launchd/README.md).

**Code changes (down, for the skills/configs the routines run):** after editing, `git push origin main`, then `bash scripts/sync-fork.sh`. The routine self-sync also covers this (it fetches upstream at run time), but syncing the fork keeps it tidy and current for manual inspection.

**Deploy path for any repo change a routine depends on:**
1. `git push origin main` (land it on upstream `main`).
2. `bash scripts/sync-fork.sh` (fast-forward the fork's `main` from upstream).

A change is not live for the routines until step 2 completes.

**Set up / change a routine:** use the repo-scoped skill `setup-channel-routine` (`.claude/skills/setup-channel-routine/SKILL.md`) — `/setup-channel-routine <linkedin|x|instagram>`. It bakes in the canonical config (environment, fork repo, tools, no MCP connectors, commit+PR prompt) and staggered schedules. Manage/disable routines at https://claude.ai/code/routines.

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
