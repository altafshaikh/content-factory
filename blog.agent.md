# blog.agent.md — Loop prompt for the Blog channel

This is the prompt that fires daily (or on each `/loop` tick) to drain ONE idea from the shared library and turn it into a publish-ready Hashnode blog post.

## How to start the loop

```
/loop 1d <paste the prompt block below>
```

Self-paced (model decides cadence):
```
/loop <paste the prompt block below>
```

Manual one-shot:
```
/blog-writer-agent
```

---

## The prompt (copy from here ↓)

```
You are the daily Blog post runner for Altaf. Today's job is to drain ONE unconsumed raw idea for the Blog channel and turn it into a publish-ready Hashnode blog post.

Project root: ./
Shared idea library: ./raw-ideas/
Channel folder: ./blog-post/

Step 1 — Compute the Blog queue
- List files in ./raw-ideas/ (NOT recursive). Accept .md and .txt only.
- Read ./blog-post/TODO.md and extract the filenames in its "Done" section.
- Also extract any filename in its "In Progress" section.
- Queue = (files in raw-ideas/) MINUS (Done filenames) MINUS (In Progress filenames).
- Filter out any file whose frontmatter declares `channels: [...]` without "blog" in the list.
- If queue is empty: update ./blog-post/TODO.md so the Queue section reads "_(empty — drop new ideas into ../raw-ideas/)_", print one line "No new blog ideas. Skipping today." and STOP. Do not generate anything.
- Otherwise, pick the OLDEST by filename sort (lexical). This is today's idea.

Step 2 — Sync TODO.md
- Rebuild the "Queue (unprocessed)" section in ./blog-post/TODO.md by listing every file from the computed queue, one bullet per file with a one-line preview from the file's first non-empty content line.
- Move today's pick from "Queue" to "In Progress" with the date: "- [ ] <filename> — started YYYY-MM-DD".
- Leave the "Done" section untouched.

Step 3 — Trigger the post pipeline
- Invoke the /blog-writer-agent skill on today's pick. Pass the full file content as the raw idea.
- The skill handles all 5 phases end-to-end: Content Writer → Title Generator → Banner Prompt → SEO → Final Assembly. All handoffs save to ./blog-post/posts/<slug>/.

Step 4 — Finalize the queue
- After the skill writes final-post.md, DO NOT move the source idea. raw-ideas/ is immutable and shared across channels.
- Update ./blog-post/TODO.md:
  - Remove the entry from "In Progress"
  - Prepend a new line to "Done": "- [x] <filename> → [posts/<slug>/final-post.md](./posts/<slug>/final-post.md) — YYYY-MM-DD"
- Print a one-block summary:
    Channel: Blog
    Processed: <filename>
    Post folder: ./blog-post/posts/<slug>/
    Final post: ./blog-post/posts/<slug>/final-post.md
    Queue remaining (Blog): <N> idea(s)

Rules
- Process exactly ONE idea per run.
- raw-ideas/ is immutable — never move, rename, or delete files there.
- Same idea may already be consumed by other channels (LinkedIn, X) — that does not affect Blog's queue. Each channel's TODO.md is independent.
- If a file's frontmatter has `channels: [...]` without "blog", skip it silently.
- Never write outside ./blog-post/ (the channel folder).
- If the skill fails mid-run, leave the idea in In Progress with an error note in TODO.md so the next run can retry it.
```

---

## Notes

- **What gets picked first?** Lexical filename sort within `./raw-ideas/`. Use `001-`, `002-` prefixes.
- **How to add ideas?** Drop a `.md`/`.txt` file into `./raw-ideas/`. Next loop tick picks it up.
- **Restrict an idea to blog only?** Add frontmatter:
  ```
  ---
  channels: [blog]
  ---
  ```
- **Re-run a consumed idea on Blog?** Delete its line from `blog-post/TODO.md` "Done" section. Next loop will re-pick it.
- **Multiple posts in one day?** Invoke `/blog-writer-agent` manually — each call drains one entry.
- **Change the title?** Title options are in `posts/<slug>/02-title-options.md`. Edit `final-post.md` frontmatter directly.
