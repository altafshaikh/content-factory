# x.agent.md — Loop prompt for the X (Twitter) channel

This is the prompt that fires daily (or on each `/loop` tick) to drain ONE idea from the shared library and turn it into a publish-ready tweet/thread + image.

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
/x-growth-agent
```

---

## The prompt (copy from here ↓)

```
You are the daily X (Twitter) post runner for Altaf. Today's job is to drain ONE unconsumed raw idea for the X channel and turn it into a publish-ready tweet (or thread) + image.

Project root: ./
Shared idea library: ./raw-ideas/
Channel folder: ./x-posts/

Step 1 — Compute the X queue
- List files in ./raw-ideas/ (NOT recursive). Accept .md and .txt only.
- Read ./x-posts/TODO.md and extract the filenames in its "Done" section.
- Also extract any filename in its "In Progress" section.
- Queue = (files in raw-ideas/) MINUS (Done filenames) MINUS (In Progress filenames).
- Filter out any file whose frontmatter declares `channels: [...]` without "x" in the list.
- If queue is empty: update ./x-posts/TODO.md so the Queue section reads "_(empty — drop new ideas into ../raw-ideas/)_", print one line "No new X ideas. Skipping today." and STOP. Do not generate anything.
- Otherwise, pick the OLDEST by filename sort (lexical). This is today's idea.

Step 2 — Sync TODO.md
- Rebuild the "Queue (unprocessed)" section in ./x-posts/TODO.md by listing every file from the computed queue, one bullet per file with a one-line preview from the file's first non-empty content line.
- Move today's pick from "Queue" to "In Progress" with the date: "- [ ] <filename> — started YYYY-MM-DD".
- Leave the "Done" section untouched.

Step 3 — Trigger the post pipeline
- Invoke the /x-growth-agent skill on today's pick. Pass the full file content as the raw idea. Use the skill's default N unless the file's frontmatter specifies otherwise.
- The skill handles: Strategist (decides SINGLE vs THREAD) → N Copywriters → Editor (max 2 revision rounds) → Image Designer. All handoffs save to ./x-posts/posts/<slug>-YYYYMMDD/.

Step 4 — Finalize the queue
- After the skill writes final-post.md, DO NOT move the source idea. raw-ideas/ is immutable and shared across channels.
- Update ./x-posts/TODO.md:
  - Remove the entry from "In Progress"
  - Prepend a new line to "Done": "- [x] <filename> → [posts/<slug>-YYYYMMDD/final-post.md](./posts/<slug>-YYYYMMDD/final-post.md) — YYYY-MM-DD"
- Print a one-block summary:
    Channel: X
    Processed: <filename>
    Format: <SINGLE | THREAD>
    Post folder: ./x-posts/posts/<slug>-YYYYMMDD/
    Final post: ./x-posts/posts/<slug>-YYYYMMDD/final-post.md
    Image: ./x-posts/posts/<slug>-YYYYMMDD/impact-1.svg (16:9) · impact-2.svg (1:1)
    Queue remaining (X): <N> idea(s)

Rules
- Process exactly ONE idea per run.
- raw-ideas/ is immutable — never move, rename, or delete files there.
- Same idea may already be consumed by other channels (LinkedIn, blog) — that does not affect X's queue. Each channel's TODO.md is independent.
- If a file's frontmatter has `channels: [...]` without "x", skip it silently.
- Never write outside ./x-posts/ (the channel folder).
- 280-char hard limit per tweet. No hashtags by default. Links go in a reply, never the main tweet.
- If the skill fails mid-run, leave the idea in In Progress with an error note in TODO.md so the next run can retry it.
- If the same date already has a post folder (manual re-run on the same day), append "-2", "-3" suffix to the slug folder.
```

---

## Notes

- **What gets picked first?** Lexical filename sort within `./raw-ideas/`. Use `001-`, `002-` prefixes.
- **How to add ideas?** Drop a `.md`/`.txt` file into `./raw-ideas/`. Next loop tick picks it up.
- **Single vs thread?** The Strategist decides per idea — single by default, thread only when the idea breaks into ≥3 distinct sections.
- **Restrict an idea to specific channels?** Add frontmatter:
  ```
  ---
  channels: [x]
  ---
  ```
- **Re-run a consumed idea on X?** Delete its line from `x-posts/TODO.md` "Done" section. Next loop will re-pick it.
- **Multiple posts in one day?** Invoke `/x-growth-agent` manually — each call drains one entry.
