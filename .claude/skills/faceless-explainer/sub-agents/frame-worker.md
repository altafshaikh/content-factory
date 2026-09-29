# Frame worker — faceless-explainer delta

> The shared law is the core contract above (the packet builder prepends `../hyperframes/references/frame-worker-core.md` to this file as `_role.md`) — read the two as one role. This file carries only what's specific to a faceless-explainer frame; you run N-up, **one frame each** — your dispatch carries exactly one packet. Tempted to add a generic GSAP / timeline rule here? Wrong home — it belongs in the core contract or `hyperframes-core`.

## Your `focal:` / `roles:` — invented elements

- `focal:` — which **invented** element is the hero.
- `roles:` — each invented element's role: `foreground subject` / `background` full-bleed / `supporting`. Because the explainer is **faceless, these are elements you design** (a hero word, a diagram node, a chart series, a coined-term card), not captured assets. The **only** real media is a user-supplied image, when present: `public/<basename> — description` (a **`[video]`** tag marks a `.mp4` clip the user provided).

## Designing each element (faceless-explainer constraint)

**Design each element by its `roles`** (the `focal` is the hero): a `foreground subject` is the thing the eye lands on — respect the 83% keep-out, lay text around it, not over it; a `background` is full-bleed and dimmed ~30–50% so foreground content stays legible; `supporting` elements (labels, secondary shapes, ambient layers) stay quiet. These are **invented** — you build them in SVG / CSS / type from `frame.md`'s atoms, never from a fetched file (build the idea the narrative describes; never fall back to generic decorative bokeh or stock filler). **If the user supplied a real image** named in `roles:`/`focal:`, place it: a `[video]` candidate (`.mp4`) renders as a **muted** `<video class="clip">` (`data-start` / `data-duration` / `data-track-index` per the core clip contract), a **direct child of the frame root** — never nested in another timed element, or the renderer freezes it; an untagged image → `<img>`.

## 4:5 portrait feed canvas (1080x1350) — overrides the core "anchor the hero high" line

When your canvas is 1080x1350 (4:5, the LinkedIn/Instagram feed format), the content area is y 80 to 1120 (keep-out at 0.83 x height). "Anchor the hero high" on its own leaves the lower 40% dead on this canvas; build to these bands instead:

- **Three bands, all used.** Top band y 80-380: kicker + headline. Middle band y 380-880: the `focal` (the diagram, chart, number, card stack) at 40-60% of the frame. Lower band y 880-1120: a real element, never empty: the payoff line, the stat, the footer rule, the chart's axis and count-up, the CTA handle.
- **Settled-state fill test.** At the frame's final held read the content reaches the lower band with no dead strip; the orchestrator measures it after render with `scripts/fill-check.mjs` (thresholds in `scripts/lib/dimensions.mjs` `FILL_RULES`, today: lowest content y >= 1000, no empty band over 200px). A frame that fails comes back to you with that line as retry feedback.
- **Type-only frames scale up, not down.** Use the 1080-wide ramp: kicker/mono 26-30px, body 30-34px, headline 84-100px, display 120-150px, number-hero 220-300px. Lay the stack out as a full-height flex column (`justify-content: space-between` or explicit band positions), not a top-aligned block.
- **Diagrams and charts get height.** A chart's plot area is at least 520px tall; columns, bars and cards are sized so the diagram's base sits in the lower band.
- Horizontal margins stay 72-96px; nothing crosses y 1120.
