# image-gen agent

Project-side home for the image generation agent. Everything image-related lives here.

---

## Global skill

The agent brain (instructions, selection logic, SVG generation rules) lives at:

```
~/.claude/skills/image-gen-agent/SKILL.md
```

Edit that file to change how the agent behaves. This folder holds the assets the agent draws from.

---

## What this agent does

Generates on-brand SVG images for any channel in the content factory. When invoked by a channel pipeline, it:

1. Reads `inspiration/MANIFEST.md` to survey available styles
2. Picks the best-matching style(s) based on channel + content context
3. Reads the selected inspiration file(s) — any format: SVG, PNG, JPG, PDF, screenshot
4. Extracts design DNA: color palette, typography, layout grid, spacing rhythm
5. Generates a fresh SVG that carries the actual post content in that style

---

## Folder layout

```
agents/image-gen/
├── AGENT.md                        ← this file
├── inspiration/
│   ├── MANIFEST.md                 ← style index — agent reads this first
│   ├── stat-card-dark/
│   │   └── sample.svg              ← LinkedIn-style dark stat card
│   ├── editorial-bold/
│   │   └── sample.svg              ← Blog hero banner, wide cinematic
│   ├── quote-card-minimal/
│   │   └── sample.svg              ← X/Twitter quote card, clean minimal
│   └── gradient-hero/
│       └── sample.svg              ← Presentation cover, atmospheric
```

---

## Adding new inspiration

Drop any file (SVG, PNG, JPG, PDF, screenshot) into a new subfolder under `inspiration/`, then add an entry to `inspiration/MANIFEST.md`. The agent picks it up on the next run — no other changes needed.

File format doesn't matter. The agent reads image files visually and SVG files structurally. Both work as design references.

---

## How channels invoke the agent

Channel pipelines pass a brief at the image step:

```
[IMAGE BRIEF]
Channel: <linkedin | blog | x | presentation>
Dimensions: <W>×<H>
Content-type: <stat-card | editorial | quote-card | hero>
Stats:
  - <stat label>: <value> [optional comparison, e.g. "↓ from 30h"]
Tagline: <one short line>
Author: <name>
Domain: <e.g. "AI Engineering">
Output path: <path/to/impact.svg>
```

The agent writes the SVG to the output path and prints a surface block.
