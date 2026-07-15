---
name: sync-inspiration
description: "Pull quick-capture notes from all files in inspiration-inbox/ into the shared raw-ideas/ library. Fetches any URLs found, researches the content, and writes a synthesized idea file with a proper title and context. Use when the user says /sync-inspiration, 'sync my notes', 'sync the inbox', or 'pull inbox into raw ideas'."
trigger: /sync-inspiration
---

# /sync-inspiration

Promotes rough notes from every file in `inspiration-inbox/` into the shared, immutable `raw-ideas/` library, one file per idea. When a chunk contains URLs, it fetches and researches each link, synthesizes the key insights, and writes a rich idea file — not just a dump of the raw text.

## Steps

1. List all files in `inspiration-inbox/`. Process every file found — not just `inbox.md`. If the folder is empty or every file has no real content, report "inbox is empty" and stop.
2. For each file:
   - If it is `inbox.md`: ignore the leading HTML comment header. Treat the rest as content.
   - For all other files: read the full content as-is.
   - Skip files that are blank or whitespace-only after stripping any header comment.
3. Within each file, split content into idea chunks on lines containing only `---`. A file with no `---` is a single idea. Discard chunks that are blank/whitespace-only.
4. Find the next available numeric prefix: list `raw-ideas/*.md` filenames matching `NNN-*.md`, take the highest `NNN`, add 1 (zero-padded to 3 digits). Start at `001` if none exist.
5. For each idea chunk across all files, in order:
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
6. Once all chunks from a file are written:
   - If it is `inbox.md`: reset it back to just the header comment (empty otherwise).
   - For all other files: delete the file — it has been fully promoted.
7. Report which new `raw-ideas/` files were created and a one-line summary of each.

## Rules

- Never edit or remove existing files in `raw-ideas/` — it's append-only.
- For URL-based ideas: the synthesized context is your judgment call — write it as insight, not a summary of the webpage.
- For plain-text ideas: verbatim only; slug generation is the only judgment call.
- No em dashes in any written content. Use plain punctuation or rewrite as two sentences.
