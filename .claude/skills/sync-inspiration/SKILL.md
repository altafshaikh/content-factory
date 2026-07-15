---
name: sync-inspiration
description: "Pull quick-capture notes from inspiration-inbox/inbox.md into the shared raw-ideas/ library. Fetches any URLs found, researches the content, and writes a synthesized idea file with a proper title and context. Use when the user says /sync-inspiration, 'sync my notes', 'sync the inbox', or 'pull inbox into raw ideas'."
trigger: /sync-inspiration
---

# /sync-inspiration

Promotes rough notes jotted in `inspiration-inbox/inbox.md` into the shared, immutable `raw-ideas/` library, one file per idea. When a chunk contains URLs, it fetches and researches each link, synthesizes the key insights, and writes a rich idea file — not just a dump of the raw text.

## Steps

1. Read `inspiration-inbox/inbox.md`. Ignore the leading HTML comment header. If there's no real content below it, report "inbox is empty" and stop — don't touch `raw-ideas/`.
2. Split the remaining content into idea chunks on lines containing only `---`. A file with no `---` at all is a single idea. Discard chunks that are blank/whitespace-only.
3. Find the next available numeric prefix: list `raw-ideas/*.md` filenames matching `NNN-*.md`, take the highest `NNN`, add 1 (zero-padded to 3 digits). Start at `001` if none exist.
4. For each idea chunk, in order:
   a. **Detect URLs.** Scan the chunk for any `http://` or `https://` links.
   b. **If URLs are present:**
      - Fetch each URL using WebFetch. Read the page content thoroughly.
      - If a URL is a social media post (X/Twitter, Instagram, LinkedIn), extract: the post text, any key claim or hook, what makes it interesting or shareable.
      - Synthesize the fetched content into a coherent idea: what is being shown, what is the insight, why would an audience care.
      - Generate a descriptive title and a short kebab-case slug from the synthesized idea (not from the raw URL).
      - Write the idea file with:
        - A `# Title` heading (human-readable, descriptive)
        - A `## Context` section with the synthesized insight in plain prose — what you found, what it demonstrates, what the angle is
        - A `## Source` section listing the original URLs verbatim
   c. **If no URLs are present:**
      - Write the chunk's text **verbatim** — do not rewrite, expand, or clean up the wording.
      - Generate a short kebab-case slug from the chunk's content (gist of the first line or two).
   d. Write to `raw-ideas/NNN-slug.md` using the next available prefix, then increment for the next chunk.
5. Once all chunks are written, reset `inspiration-inbox/inbox.md` back to just the header comment (empty otherwise).
6. Report which new `raw-ideas/` files were created and a one-line summary of each.

## Rules

- Never edit or remove existing files in `raw-ideas/` — it's append-only.
- For URL-based ideas: the synthesized context is your judgment call — write it as insight, not a summary of the webpage.
- For plain-text ideas: verbatim only; slug generation is the only judgment call.
- If `inspiration-inbox/inbox.md` doesn't exist, create it with the standard header and stop — nothing to sync yet.
- No em dashes in any written content. Use plain punctuation or rewrite as two sentences.
