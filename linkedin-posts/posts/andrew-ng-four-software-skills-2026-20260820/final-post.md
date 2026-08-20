# andrew-ng-four-software-skills-2026

**Source idea:** [../../../raw-ideas/008-andrew-ng-four-software-skills-2026.md](../../../raw-ideas/008-andrew-ng-four-software-skills-2026.md)
**Generated:** 2026-08-20
**Rounds:** 1  ·  **Revised:** no
**Format:** Document carousel (8 slides, 1080×1350) + caption. Second carousel on the account (first, five-rung-ai-automation-ladder, is still unshipped).

## Variation Scores (Round 1)

| Variant | Angle                 | Hook | Authenticity | Readability | Compliance | CTA | Avg |
|---------|-----------------------|------|--------------|-------------|------------|-----|-----|
| A       | Story-first           |  7   |      9       |      8      |     9      |  9  | 8.4 |
| B       | Bold claim-first      |  9   |      8       |      9      |     10     |  9  | 9.0 |
| C       | Tactical/how-to-first |  6   |      8       |      8      |     9      |  9  | 8.0 |

**Winner:** Variant B — B opens with a stance the reader has a stake in arguing with ("coding is not the skill that protects your job"), which is the hook property the tracker credits for the account's strongest posts. C reads closer to the neutral listicle open the Performance Context explicitly says to avoid.

---

## Final Post

Coding is not the skill that protects your job in 2026. It is just the entry fee.

Andrew Ng analyzed 10,000 job postings to find out what actually separates engineers now. Four skills came back.

1. Building and deploying AI applications. Not the demo, the discipline. Normal software is predictable. AI is not, ask it the same question twice and get two different answers. The real skill is controlling that with evals and error analysis.

2. Software fundamentals, and you need them more now, not less. Every software decision trades something off: fast, secure, cheap. Tell an AI to hit all three and it will quietly decide which one loses. You find out in production.

3. Using coding agents well. Knowing what they're good at, where they break, how far to trust them. One careless instruction and your production database is gone.

4. Shaping the build. Deciding which problem deserves solving, not just executing the ticket.

You used to be the bricklayer who built perfect walls. There's a robot that lays bricks faster now. Your value was never the bricklaying.

Of the four, which one are you actually building, and which one are you just hoping the agent handles for you?

#AIEngineering #SoftwareEngineering #AIAgents #BuildingWithAI

---

## Carousel

**Upload:** `exports/andrew-ng-four-software-skills-carousel.pdf` (8 pages, 1080×1350, ~748 KB)
**Style:** Layout: diagram-explainer · Typography and palette: bold-editorial-type (same brand system as the five-rung deck, kept identical so carousels read as one system)
**Source:** `deck.py` regenerates all 8 SVGs. Rebuild: `OUT_DIR="$PWD" python3 deck.py`

| Slide | File | Carries |
|-------|------|---------|
| 1 | [slide-1.svg](./slide-1.svg) | Hook: "You used to lay bricks. Now a robot lays them faster." Highlighter swipe, then the thesis at full size ("It was deciding where the wall goes"), brickwork motif with one brick filled, and the Ng attribution. The four skills are deliberately NOT listed here so slide 2 still has a reveal |
| 2 | [slide-2.svg](./slide-2.svg) | The four skills, numbered 01-04, one line each, attributed to Andrew Ng's 10,000-job analysis. The saveable slide |
| 3 | [slide-3.svg](./slide-3.svg) | Skill 1 detail: Build & deploy AI. Predictable vs. unpredictable, callout on evals + error analysis |
| 4 | [slide-4.svg](./slide-4.svg) | Skill 2 detail: Fundamentals. The tradeoff the AI quietly makes for you, callout on catching it before production |
| 5 | [slide-5.svg](./slide-5.svg) | Skill 3 detail: Use coding agents well. Limits, trust, efficiency, callout on the wiped-database risk |
| 6 | [slide-6.svg](./slide-6.svg) | Skill 4 detail: Shape the build. Order-taker vs. architect, callout on deciding where the wall goes |
| 7 | [slide-7.svg](./slide-7.svg) | The diagnostic. Four habits, four architect-moves, one per skill. Second saveable slide |
| 8 | [slide-8.svg](./slide-8.svg) | The takeaway line, all four skills recapped, then the CTA |

**Exported PNGs:** `exports/slide-1.png` through `exports/slide-8.png`

---

## Publishing notes

- Upload the PDF via **Add a document**, not as separate images. Suggested document title: `Four Software Skills That Matter in 2026`.
- No links in the body, nothing needed in the first comment.
- This is the account's first carousel to actually ship (the five-rung deck is still sitting unpublished) — there is no format baseline yet. Judge it on engagement rate against the account's ~4% average, and pull single-post analytics if impressions clear 1,000, since capture rate (not impressions) is what tells you whether it actually built the account.

---

**Unresolved issues:** none.
