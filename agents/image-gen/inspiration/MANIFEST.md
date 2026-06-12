# Inspiration Library — Style Manifest

Agent reads this file first to survey available styles, then fetches the selected sample file(s).

Accepted file formats: SVG, PNG, JPG, PDF, screenshot — any format works as a design reference.

---

## Style Index

| Style | Folder | File | Dimensions | Channels | Content Type | Mood Tags |
|-------|--------|------|------------|----------|--------------|-----------|
| Dark Stat Card | `stat-card-dark/` | `sample.svg` | 1080×1350 (4:5) | linkedin | stat-heavy, data tiles, before/after | dark, structured, technical, high-contrast |
| Editorial Bold | `editorial-bold/` | `sample.svg` | 1600×900 (16:9) | blog | concept-driven, opinion, big statement | cinematic, atmospheric, bold typography |
| Quote Card Minimal | `quote-card-minimal/` | `sample.svg` | 1080×1080 (1:1) | x | punchy claim, single insight | minimal, clean, dark, typographic |
| Gradient Hero | `gradient-hero/` | `sample.svg` | 1920×1080 (16:9) | presentation | title slide, session cover | cinematic, rich gradient, atmospheric |

---

## Selection Logic (for the agent)

Apply in order — first match wins:

1. `stat-card` + `linkedin` → **stat-card-dark**
2. `editorial` + `blog` → **editorial-bold**
3. `quote-card` + `x` → **quote-card-minimal**
4. `hero` + `presentation` → **gradient-hero**
5. Stat-heavy content on any channel → **stat-card-dark** (adapt dimensions)
6. Concept/opinion content on any channel → **editorial-bold** (adapt dimensions)
7. No direct match → read mood tags from all styles, pick closest to the brief's tone

**Blending:** If the brief combines elements of two styles (e.g., stat-heavy blog banner), take the layout grid from one and the atmosphere/palette from the other. State the blend in the surface block.

---

## Design Tokens (shared defaults)

These are the base tokens. Each style may override them — check the sample file first.

```
Background gradient:  #0a0e1a → #111827 (dark, top-to-bottom)
Accent gradient:      #22d3ee → #a78bfa (cyan → violet, left-to-right)
Body text:            #e2e8f0
Muted text:           #94a3b8
Subtle / labels:      #64748b
Tile background:      #1a2538 → #141e2d
Tile border-radius:   16px
Accent line:          3–5px height, radius 2
Outer margin:         80–100px
Font stack:           -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
```

---

## Adding a New Style

1. Create a subfolder: `inspiration/<style-slug>/`
2. Drop in a reference file with any name and any format (SVG, PNG, JPG, PDF, screenshot)
3. Add a row to the Style Index table above with: folder, file name, dimensions, channels, content type, mood tags
4. Optionally add a selection rule above if the style has a distinct trigger condition

No other changes needed — the agent picks it up on the next run.
