---
workflow: faceless-explainer
flow: automation
storyboard: no
message: "You think in messages. You get billed in turns: every call re-sends the whole context."
destination: linkedin-feed
aspect: 1080x1350
language: en
audience: engineers running coding agents who read their usage in messages
length: 40s
angle: concept
---

## Intent

A silent motion-graphics explainer of the token-usage-spike LinkedIn post (final-post.md, the
2026-09-05 mechanism rewrite). The subject is the mechanism: a turn re-sends everything before it,
so one file read is paid on every later call and cost grows with the square of session length.
Calm, precise, typographic; the numbers carry it.

## Assets

- none. Every visual is invented; the source text is capture/extracted/visible-text.txt.

## Customizations

- Silent: no narration, no music, no SFX, no captions.
- Portrait 1080x1350, light theme (the factory's explainer default for LinkedIn).
- Seven scenes, 4.5-7s each, one idea per scene, in the factory's explainer shape: hook, gap,
  mechanism, worked example, rule, fix, close.

## Notes

- Every number on screen must appear in the post verbatim: 5 messages, 427 calls, 12 hours,
  21,000-token file, call 200, 947 calls, 747 more calls, about 16 million tokens, roughly eight
  dollars, 213 to 1, 1,196M read, 5.6M written, 200k window, 160k, 1M default, about 4x.
- No emojis, no company or internal tool names, no em dashes in on-screen copy.
- Close with the post's CTA: "Open your longest session from this week. Count how many API calls came out of one message."
- Brief confirmed by the bench card (Altaf 2026-09-29, "make a silent explainer from the latest post"); no interview run.
