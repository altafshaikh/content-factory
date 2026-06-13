# How to Feed LinkedIn Analytics Into the Agent

Two paths — use whichever fits the moment.

---

## Path A — LinkedIn Content Analytics CSV (preferred)

LinkedIn lets you export post analytics from the Creator Analytics page.

### Steps

1. Go to **linkedin.com/analytics/creator/content**
2. Set the date range to cover the posts you want to capture
3. Look for an **Export** or **Download CSV** button in the top-right corner
   - This appears for accounts with Creator Mode on
   - If you don't see it: use Path B instead
4. Save the CSV file — it will be named something like `Content_Analytics_YYYYMMDD.csv`
5. Drop it into:
   ```
   linkedin-posts/performance/csv-imports/
   ```
6. Run `/linkedin-growth-agent` — Agent 0 will detect the CSV, parse it, match rows to post folders, write `performance.md` per post, update `tracker.md`, and move the CSV to `csv-imports/processed/`

### What LinkedIn's CSV contains

| Column | What it is |
|--------|-----------|
| Content | First ~200 chars of your post text |
| Date published | YYYY-MM-DD |
| Impressions | Total times the post appeared in feed |
| Members reached | Unique accounts that saw it |
| Reactions | Likes + other reactions |
| Comments | Direct comments |
| Reposts | Shares without added text |
| Clicks | Link or post clicks |
| Engagement rate (%) | (Reactions + Comments + Reposts + Clicks) / Impressions |

---

## Path B — Manual entry (no CSV needed)

Use this when the export button isn't available or you want to log a single post quickly.

1. Open the post on LinkedIn → click **View analytics** under the post
2. Copy the numbers into the post's `performance.md`:
   ```
   linkedin-posts/posts/<slug>-<date>/performance.md
   ```
3. Use the template below — just fill in the numbers and run `/linkedin-growth-agent` so the Strategist picks it up on the next run.

### `performance.md` template (manual)

```markdown
# Performance — <slug>

**Published:** YYYY-MM-DD
**LinkedIn URL:** <paste post URL here>
**Last updated:** YYYY-MM-DD
**Data source:** manual

## Metrics

| Metric | Value |
|--------|-------|
| Impressions | |
| Members reached | |
| Reactions | |
| Comments | |
| Reposts | |
| Link clicks | |
| Engagement rate (%) | |

## Notes

<anything you noticed — what the comments said, what type of people engaged, etc.>
```

4. Run `/linkedin-growth-agent` — Agent 0 will pick it up, run the verdict analysis, and update `tracker.md`.

---

## How often to do this

- **Weekly** is ideal — drop the CSV once a week, let Agent 0 process it before the next post run
- **Monthly minimum** — the Strategist needs at least 3 data points before patterns emerge
- Don't wait for "enough data" before starting — partial data is better than none
