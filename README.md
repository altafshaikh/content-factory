# Content Strategy — Multi-Channel Idea Factory

One pool of raw ideas. Many channels. Each channel has its own agent, its own pipeline, its own publish-ready outputs.

```
                       ┌──────────────────┐
                       │   raw-ideas/     │  ← single source of truth
                       │ (shared library) │     (immutable, append-only)
                       └────────┬─────────┘
                                │
            ┌───────────────────┼───────────────────┬──────────────────┐
            ▼                   ▼                   ▼                  ▼
      ┌──────────┐        ┌──────────┐       ┌───────────┐    ┌────────────────┐
      │ LinkedIn │        │     X    │       │   Blog    │    │  Presentation  │
      │  agent   │        │  agent   │       │   agent   │    │     agent      │
      └─────┬────┘        └─────┬────┘       └─────┬─────┘    └────────┬───────┘
            ▼                   ▼                  ▼                   ▼
     linkedin-posts/       x-posts/          blog-post/         (future)
       (channel out)     (channel out)     (channel out)       (channel out)
```

---

## Top-level layout

```
content-stratergy/
├── README.md                     ← you are here
├── CLAUDE.md                     ← AI agent contract for this whole project
├── raw-ideas/                    ← SHARED idea library (one file = one idea)
│   ├── 001-claude-vs-codex.md
│   ├── 002-SuperReps-learnings.md
│   ├── 003-claude-new-feature-loop.md
│   ├── ai drinks water more than humans do.md
│   └── ai-non-deterministic-code-vs-program-deterministic-code.md
├── agents/                       ← shared service agents (not channels)
│   └── image-gen/                ← image generation agent + inspiration library
│       └── inspiration/          ← style samples (SVG, JPEG) + MANIFEST.md
├── linkedin.agent.md             ← /loop prompt for the LinkedIn channel
├── x.agent.md                    ← /loop prompt for the X channel
├── blog.agent.md                 ← /loop prompt for the blog channel    (stub)
├── linkedin-posts/               ← LinkedIn channel — CLAUDE.md + TODO + posts/
├── x-posts/                      ← X channel — CLAUDE.md + TODO + posts/
└── blog-post/                    ← Blog channel                         (stub)
```

---

## How it works

1. **You drop ideas** into `./raw-ideas/`. One file per idea — notes, transcripts, voice-memo dumps. Anything that could become content on any channel.
2. **Each channel runs its own daily loop.** The loop prompts live at the top level (`linkedin.agent.md`, `x.agent.md`, `blog.agent.md`).
3. **Each loop picks the oldest unprocessed idea for THAT channel** (filename-sorted) and runs the channel-specific skill.
4. **The same idea can fuel multiple channels.** LinkedIn consumes idea #001 today; X can still consume it tomorrow. Raw ideas are never deleted or moved — each channel tracks its own consumption in its own `TODO.md`.

---

## Consumption tracking model

`raw-ideas/` is **immutable** — files never move out.

Each channel folder maintains its own `TODO.md` with a **Done** section listing the raw-idea filenames that channel has already consumed.

A channel's pending queue at runtime =
```
ls raw-ideas/  MINUS  filenames in <channel>/TODO.md "Done" section
```

This means:
- ✅ One idea → many channels (use it for LinkedIn, then X, then a blog post)
- ✅ Each channel runs at its own pace, independently
- ✅ No coordination needed between channels
- ✅ Re-running an idea on a channel = remove its line from that channel's Done section

---

## Adding a new channel

1. Create `<channel>-posts/` (or similar) with its own `CLAUDE.md`, `README.md`, `TODO.md`, `posts/` subfolder.
2. Create or commission a skill at `.claude/skills/<channel>-growth-agent/SKILL.md`.
3. Create `<channel>.agent.md` at the top level — the loop prompt that picks an idea, calls the skill, updates the channel's `TODO.md`.
4. Start the loop: `/loop 1d <paste the prompt from <channel>.agent.md>`.

---

## Channels — current status

| Channel       | Skill                                | Loop prompt           | Folder            | Status      |
|---------------|--------------------------------------|------------------------|-------------------|-------------|
| LinkedIn      | `linkedin-growth-agent`              | `linkedin.agent.md`   | `linkedin-posts/` | ✅ active   |
| X (Twitter)   | `x-growth-agent`                     | `x.agent.md`          | `x-posts/`        | ✅ active   |
| Blog          | (TBD — `blog-growth-agent` / `idea-to-blog`) | `blog.agent.md` (stub) | `blog-post/`      | 🟡 stub     |
| Presentation  | (TBD — `idea-to-presentation`)       | (not yet)             | (not yet)         | ⚪ planned   |

### LinkedIn pipeline — current spec

| Setting | Value |
|---------|-------|
| Copywriter variants per post | 3 (A: story-first · B: bold claim-first · C: adaptive) |
| Max editor revision rounds | 2 |
| Images per post | 2 (always different LinkedIn formats) |
| Image generation | `/image-gen-agent` skill — reads `agents/image-gen/inspiration/` |
| Image formats | Square 1080×1080 · Portrait 1080×1350 · Landscape 1200×627 (URL posts) |
| Brand handle on images | @teachmebro (accent color, above byline) |
| Performance feedback | LinkedIn CSV/XLSX → `linkedin-posts/performance/tracker.md` |
| Scheduled runner | `linkedin-daily-post-runner` (cloud scheduled task) |

---

## Adding a new idea

```bash
# Create a new file in raw-ideas/, prefix with the next number for queue priority
echo "Raw notes about whatever..." > raw-ideas/002-mcp-vs-tools.md
```

Within 24h all active channel loops will pick it up (one per channel per day).

To run immediately, invoke the channel skill manually: `/linkedin-growth-agent`.
