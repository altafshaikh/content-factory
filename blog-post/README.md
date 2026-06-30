# Blog channel — README

This is the Blog channel of the multi-channel content factory. It consumes ideas from the shared `../raw-ideas/` library and produces publish-ready Hashnode blog posts.

---

## How it works

1. Drop an idea file into `../raw-ideas/` (shared with all channels).
2. Run `/blog-writer-agent` (or let `/loop` pick it up).
3. The skill runs a 5-phase pipeline and produces a `final-post.md` in `posts/<slug>/`.
4. Review and copy the content into Hashnode.

---

## Quick commands

| Want to... | Do this |
|---|---|
| Process the next queued idea | `/blog-writer-agent` |
| Run in daily loop | `/loop 1d <paste blog.agent.md prompt>` |
| Check what's queued | Open `TODO.md` |
| Review a post | `posts/<slug>/final-post.md` |
| Try a different title | Edit `final-post.md` frontmatter; options are in `02-title-options.md` |
| Re-run an idea | Remove its line from `TODO.md` Done section, then run `/blog-writer-agent` |

---

## Per-post folder

Each processed idea produces a folder at `posts/<slug>/`:

```
posts/<slug>/
├── 01-content.md        ← full blog body
├── 02-title-options.md  ← 6-8 title options + recommendation
├── 03-banner-prompt.md  ← image prompt for Midjourney / DALL·E / Ideogram
├── 04-seo.md            ← seo_title + seo_description
└── final-post.md        ← publish-ready Hashnode .md (copy this into Hashnode)
```

---

## Series arc

Posts in the AI Engineering series follow this arc:

**Mindset → Skills → Tools → Building → Advanced Patterns**

Each post stands alone, but connects to the progression. The series connector line (last section of every post) links forward and back.

---

## Idea library

Ideas live in `../raw-ideas/`. They are **never moved or deleted**. Each channel tracks its own consumption in its own `TODO.md`. The same idea can fuel a LinkedIn post, a blog post, and a presentation — independently.

To add an idea: create a `.md` or `.txt` file in `../raw-ideas/` with the next numeric prefix (e.g. `006-your-idea-slug.md`).

---

## Agent contract

Full pipeline spec: `.claude/skills/blog-writer-agent/SKILL.md`
Loop prompt: `../blog.agent.md`
Channel rules: `CLAUDE.md` (this folder)
