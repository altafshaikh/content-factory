# Inspiration Library — Style Manifest

Agent reads this file first to survey available styles, then fetches the selected sample file(s).

Accepted file formats: SVG, PNG, JPG, PDF, screenshot — any format works as a design reference.

---

## Style Index

### SVG-native styles (generated from scratch)

| Style | Folder | File | Dimensions | Channels | Content Type | Mood Tags |
|-------|--------|------|------------|----------|--------------|-----------|
| Dark Stat Card | `stat-card-dark/` | `sample.svg` | 1080×1350 (4:5) | linkedin | stat-heavy, data tiles, before/after | dark, structured, technical, high-contrast |
| Editorial Bold | `editorial-bold/` | `sample.svg` | 1600×900 (16:9) | blog | concept-driven, opinion, big statement | cinematic, atmospheric, bold typography |
| Quote Card Minimal | `quote-card-minimal/` | `sample.svg` | 1080×1080 (1:1) | x | punchy claim, single insight | minimal, clean, dark, typographic |
| Gradient Hero | `gradient-hero/` | `sample.svg` | 1920×1080 (16:9) | presentation | title slide, session cover | cinematic, rich gradient, atmospheric |

### Real-image inspiration styles (use as visual reference — read files to extract design DNA)

| Style | Folder | Files | Best For | Mood Tags |
|-------|--------|-------|----------|-----------|
| Warm Illustrated | `warm-illustrated/` | 9 jpegs | How-to posts, agent pipeline explainers, process flows, step-by-step | warm, friendly, approachable, educational, cream background, stick figures, pastel bubbles |
| Dark Terminal Cream | `dark-terminal-cream/` | 4 jpegs | Claude Code features, developer tools, CLI concepts, agentic workflows | cream bg, dark terminal window, pixel characters, technical, bold left headline |
| Bold Editorial Type | `bold-editorial-type/` | 2 jpegs | Mental model shifts, contrarian claims, big insight moments, minimal data stats | white/cream bg, giant multi-color bold typography, sparse layout, striking |
| Minimal Sketch | `minimal-sketch/` | 3 jpegs | Concise insight, opinion, less-is-more messaging, abstract concept | white bg, watercolor or sketch illustration, purple accent, clean |
| Diagram Explainer | `diagram-explainer/` | 3 jpegs | Comparisons, architecture breakdowns, concept taxonomies, technical deep dives | light bg, structured diagram, circular or grid layout, educational |

---

## Selection Logic (for the agent)

Apply in order — first match wins:

**SVG-native (dark brand):**
1. `stat-card` + `linkedin` → **stat-card-dark**
2. `editorial` + `blog` (concept-driven / opinion / big statement) → **editorial-bold**
3. `quote-card` + `x` → **quote-card-minimal**
4. `hero` + `presentation` → **gradient-hero**

**Real-image inspired — use when the post calls for a lighter, more approachable feel:**
5. Post is a step-by-step how-to OR explains an agent pipeline → **warm-illustrated**
6. Post is about a Claude Code feature, CLI command, or developer tool → **dark-terminal-cream**
7. Post is a single bold mental model shift or contrarian claim with minimal data → **bold-editorial-type**
8. Post is a short insight, opinion, or "less is more" message → **minimal-sketch**
9. Post compares two approaches OR breaks down a system/architecture → **diagram-explainer**

**Blog-specific style selection (channel: blog, dimensions: 1600×900):**

When channel is `blog`, override the generic rules above with these — first match wins:

| Blog post type | Best style | Reasoning |
|---|---|---|
| Tutorial / how-to / step-by-step / skill install | `warm-illustrated` | Approachable, process-friendly, educational tone |
| Claude Code feature / CLI / developer tool deep-dive | `dark-terminal-cream` | Developer-native, terminal aesthetic fits the topic |
| Mental model shift / "you've been doing X wrong" / contrarian | `bold-editorial-type` | Giant typography carries the reframe; sparse layout forces the reader to sit with the claim |
| Architecture breakdown / comparison / before-after / system design | `diagram-explainer` | Structured layout mirrors the structured thinking in the post |
| Short opinion / abstract concept / "less is more" | `minimal-sketch` | Restraint in visuals matches restraint in writing |
| Series cover / concept-driven / atmospheric / big statement | `editorial-bold` | Cinematic 1600×900 hero; strongest for Hashnode cover images |
| Fallback (no clear match) | `editorial-bold` | Safe SVG-native default for blog at 1600×900 |

Blog dimension is always **1600×900** (16:9) — the Hashnode cover image format.

**Blending (use freely):**
- The agent MAY combine elements from two styles — e.g. take the layout grid from `warm-illustrated` and the typography weight from `bold-editorial-type`.
- When blending, read at least one sample file from EACH style being combined.
- State the blend explicitly: "Layout: warm-illustrated · Typography: bold-editorial-type"

**Fallback:**
- No direct match → read mood tags from all styles, pick closest to the brief's tone and channel.
- When uncertain between dark-brand SVG styles and real-image-inspired styles: for blog, prefer real-image-inspired styles (more editorial-magazine feel); for LinkedIn, prefer real-image-inspired (more feed-native); for presentation, prefer dark-brand SVG.

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

## LinkedIn Dimension Reference

Use this when `Dimensions: auto` is passed for a LinkedIn brief, or when the Image Designer is choosing dimensions. First match wins.

| Condition | Format | Dimensions | Notes |
|-----------|--------|------------|-------|
| Post includes a URL or link | Landscape | **1200×627** | Link-share preview format |
| ≥3 stats AND content-type is `stat-card` | Portrait | **1080×1350** | Max mobile feed real estate |
| content-type is `editorial` or `quote-card` | Square | **1080×1080** | Most versatile, best mobile performance |
| 1–2 stats or qualitative only | Square | **1080×1080** | Versatile, clean |
| Fallback | Portrait | **1080×1350** | Safe default |

**When generating two concepts for the same post, always use DIFFERENT dimensions** — one Portrait, one Square (or Landscape if the post has a URL). Never generate both at the same size.

Max file size: 8 MB (keep under 5 MB for optimal delivery).
Supported export formats: JPG, PNG, GIF.

---

## Adding a New Style

1. Create a subfolder: `inspiration/<style-slug>/`
2. Drop in a reference file with any name and any format (SVG, PNG, JPG, PDF, screenshot)
3. Add a row to the Style Index table above with: folder, file name, dimensions, channels, content type, mood tags
4. Optionally add a selection rule above if the style has a distinct trigger condition

No other changes needed — the agent picks it up on the next run.
