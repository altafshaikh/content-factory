#!/usr/bin/env python3
"""
Builds the 8-slide LinkedIn document carousel for the
andrew-ng-four-software-skills-2026 post.

Style: same brand system as the five-rung-ai-automation-ladder deck --
blend of `diagram-explainer` (layout structure, pastel blocks, annotation
callouts) and `bold-editorial-type` (cream ground, giant bold type,
orange/blue accents, mono captions, hairline footer with signature dots).
Kept identical so the account's carousels read as one system.

Outputs slide-1.svg .. slide-8.svg into the post folder.
"""
import os

W, H = 1080, 1350
M = 88                      # outer margin
RIGHT = W - M               # 992
COL = RIGHT - M             # 904 usable width

# --- palette (from bold-editorial-type sample, shared across carousels) ---
CREAM   = "#EDEAE3"
CREAM_2 = "#E4E0D6"
INK     = "#1A1A18"
ORANGE  = "#E14B16"
BLUE    = "#1668D6"
GREY    = "#8A8578"
HAIR    = "#D2CEC4"
PEACH   = "#F6C9A8"

# pastel block fills (from diagram-explainer sample)
PASTELS = ["#DDD9CF", "#C3D8EF", "#C9DCC2", "#F6D6B8", "#D5C4EC"]

SANS = "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', Menlo, 'DejaVu Sans Mono', monospace"

TAGLINE = ["Coding is the floor now,", "not the ceiling."]


def esc(s):
    """Escape for XML and normalise typography to entities."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("'", "&#8217;").replace("·", "&#183;")
    s = s.replace("->", "&#8594;").replace("→", "&#8594;")
    return s


def txt(x, y, s, size=30, weight=400, fill=INK, font=SANS, anchor="start", ls=None, op=None):
    a = [f'x="{x}"', f'y="{y}"', f'font-family="{font}"', f'font-size="{size}"',
         f'font-weight="{weight}"', f'fill="{fill}"']
    if anchor != "start":
        a.append(f'text-anchor="{anchor}"')
    if ls is not None:
        a.append(f'letter-spacing="{ls}"')
    if op is not None:
        a.append(f'opacity="{op}"')
    return f'  <text {" ".join(a)}>{esc(s)}</text>'


def rect(x, y, w, h, fill, r=0, op=None, stroke=None, sw=None):
    a = [f'x="{x}"', f'y="{y}"', f'width="{w}"', f'height="{h}"', f'fill="{fill}"']
    if r:
        a.append(f'rx="{r}"')
    if op is not None:
        a.append(f'opacity="{op}"')
    if stroke:
        a += [f'stroke="{stroke}"', f'stroke-width="{sw or 2}"']
    return f'  <rect {" ".join(a)}/>'


def line(x1, y1, x2, y2, stroke=HAIR, sw=2, op=None):
    a = [f'x1="{x1}"', f'y1="{y1}"', f'x2="{x2}"', f'y2="{y2}"',
         f'stroke="{stroke}"', f'stroke-width="{sw}"']
    if op is not None:
        a.append(f'opacity="{op}"')
    return f'  <line {" ".join(a)}/>'


def eyebrow(label, y=148):
    return [line(M, y - 10, M + 46, y - 10, GREY, 3),
            txt(M + 66, y, label.upper(), size=23, weight=700, fill=GREY, font=MONO, ls=6)]


def slide_no(n):
    return [txt(RIGHT, 148, f"{n} / 8", size=22, weight=400, fill=GREY, font=MONO, anchor="end")]


def footer():
    y = 1196
    o = [line(M, y, RIGHT, y, HAIR, 2)]
    o += [txt(M, y + 52, "Altaf Shaikh", size=27, weight=700, fill=INK)]
    o += [txt(M, y + 86, "// AI Engineering", size=20, weight=400, fill=GREY, font=MONO)]
    o += [txt(RIGHT - 46, y + 48, "@teachmebro", size=30, weight=700, fill=ORANGE,
              font=MONO, anchor="end")]
    o += [txt(RIGHT - 46, y + 82, TAGLINE[0], size=18, weight=400, fill=GREY,
              font=MONO, anchor="end")]
    o += [txt(RIGHT - 46, y + 106, TAGLINE[1], size=18, weight=400, fill=GREY,
              font=MONO, anchor="end")]
    o += [f'  <circle cx="{RIGHT - 26}" cy="{y + 40}" r="11" fill="{ORANGE}"/>',
          f'  <circle cx="{RIGHT - 2}" cy="{y + 40}" r="11" fill="{BLUE}"/>']
    return o


def frame(body, n):
    head = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
            '  <defs>',
            f'    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1">',
            f'      <stop offset="0%" stop-color="{CREAM}"/>',
            f'      <stop offset="100%" stop-color="{CREAM_2}"/>',
            '    </linearGradient>',
            '  </defs>',
            f'  <rect width="{W}" height="{H}" fill="url(#ground)"/>']
    return "\n".join(head + slide_no(n) + body + footer() + ['</svg>', ''])


# ---------------------------------------------------------------- slide 1: hook
def bricks(x0, y0):
    """Brickwork in running bond, one brick filled: the decision, not the labour."""
    o = []
    bw, bh, g = 84, 44, 6
    for r in range(3):                       # 3 courses, laid bottom-up
        y = y0 + (2 - r) * (bh + g)
        off = -(bw // 2) if r % 2 else 0     # stagger every other course
        for c in range(3):
            o.append(rect(x0 + off + c * (bw + g), y, bw, bh, "none", r=3, stroke=HAIR, sw=3))
    o.append(rect(x0 + 2 * (bw + g), y0, bw, bh, ORANGE, r=3, op=0.9))
    return o


def slide1():
    b = eyebrow("the 2026 skill shift")
    y = 300
    for ln in ["You used to", "lay bricks."]:
        b.append(txt(M, y, ln, size=100, weight=900, fill=INK))
        y += 118
    b += bricks(700, 300)
    b.append(rect(M - 10, 566, 830, 74, PEACH, r=4, op=0.95))
    b.append(txt(M, 624, "Now a robot lays them faster.", size=56, weight=900, fill=INK))
    # The thesis of the whole deck -- carried at the second-largest size on the
    # slide, and the only orange type here, so the eye lands on it last.
    b.append(rect(M, 712, 6, 200, ORANGE, r=3))
    b.append(txt(M + 34, 752, "Your value was never the bricklaying.", size=34, weight=400, fill=GREY))
    b.append(txt(M + 34, 836, "It was deciding", size=68, weight=900, fill=INK))
    b.append(txt(M + 34, 906, "where the wall goes.", size=68, weight=900, fill=ORANGE))
    # Credibility only. The four skills stay unspoiled so slide 2 has a reveal.
    b.append(line(M, 1024, RIGHT, 1024, HAIR, 2))
    b.append(txt(M, 1078, "Andrew Ng analyzed 10,000 job postings.", size=30, weight=700, fill=INK))
    b.append(txt(M, 1120, "Four skills came back. Coding was not one of them.", size=30, weight=400, fill=INK))
    return frame(b, 1)


# --------------------------------------------------------- slide 2: the four skills
SKILLS = [
    ("01", "BUILD & DEPLOY AI", "control the unpredictable"),
    ("02", "FUNDAMENTALS",      "catch the tradeoff it made"),
    ("03", "USE AGENTS WELL",   "know the limits, calibrate trust"),
    ("04", "SHAPE THE BUILD",   "decide what's worth solving"),
]


def slide2():
    b = eyebrow("the four skills that matter")
    b.append(txt(M, 262, "Coding isn't one of them.", size=54, weight=900, fill=INK))
    b.append(txt(M, 324, "Nothing here works without it.", size=54, weight=900, fill=INK))
    y = 404
    for i, (num, name, sub) in enumerate(SKILLS):
        b.append(rect(M, y, COL, 168, PASTELS[i], r=16))
        b.append(rect(M, y, 8, 168, ORANGE if i >= 2 else GREY, r=4))
        b.append(txt(M + 40, y + 62, num, size=32, weight=900, fill=GREY, font=MONO))
        b.append(txt(M + 108, y + 66, name, size=38, weight=900, fill=INK))
        b.append(txt(M + 108, y + 108, sub, size=23, weight=400, fill=GREY, font=MONO))
        y += 190
    b.append(txt(RIGHT, y + 12, "Andrew Ng, from 10,000 job postings analyzed",
                 size=20, weight=700, fill=GREY, font=MONO, anchor="end"))
    return frame(b, 2)


# ------------------------------------------------------ single-detail slide helper
def detail_slide(n, eb, h1, h2, num, name, tint, body, callout):
    b = eyebrow(eb)
    b.append(txt(M, 268, h1, size=58, weight=900, fill=INK))
    b.append(txt(M, 334, h2, size=58, weight=900, fill=INK))
    y = 452
    b.append(rect(M, y, COL, 366, tint, r=18))
    b.append(txt(M + 44, y + 82, num, size=46, weight=900, fill=GREY, font=MONO))
    b.append(txt(M + 132, y + 84, name, size=42, weight=900, fill=INK))
    yy = y + 158
    for ln in body:
        b.append(txt(M + 44, yy, ln, size=32, weight=400, fill=INK))
        yy += 44
    y += 366 + 40
    b.append(rect(M, y, COL, 158, "#FFFFFF", r=16, op=0.55))
    b.append(rect(M, y, 6, 158, ORANGE, r=3))
    yy = y + 54
    for ln in callout:
        b.append(txt(M + 40, yy, ln, size=32, weight=700,
                     fill=ORANGE if ln == callout[-1] else INK))
        yy += 46
    return frame(b, n)


# ------------------------------------------------------------- slide 3: skill 1
def slide3():
    return detail_slide(
        3, "skill 1 of 4", "Normal software is", "predictable. AI is not.",
        "01", "BUILD & DEPLOY AI", PASTELS[0],
        ["Ask it the same question twice,", "get two different answers back.",
         "Building the thing is not the skill.", "Controlling it is."],
        ["The real work is disciplined evals", "and error analysis, measuring and",
         "improving the system on purpose."])


# ------------------------------------------------------------- slide 4: skill 2
def slide4():
    return detail_slide(
        4, "skill 2 of 4", "Fundamentals matter more", "now, not less.",
        "02", "SOFTWARE FUNDAMENTALS", PASTELS[1],
        ["Every software decision is a", "tradeoff: fast, secure, cheap.",
         "Tell an AI to hit all three and it", "will quietly pick which one loses."],
        ["You won't know what it traded away", "until it breaks in production.",
         "Fundamentals are how you catch it first."])


# ------------------------------------------------------------- slide 5: skill 3
def slide5():
    return detail_slide(
        5, "skill 3 of 4", "Know what it's good at.", "Know where it isn't.",
        "03", "USE CODING AGENTS WELL", PASTELS[2],
        ["What agents are perfect at, their", "limits, and how much to trust them.",
         "Do it efficiently too, the time and", "tokens you burn count."],
        ["One small wrong instruction can", "wipe a production database.",
         "Trust is calibrated, never assumed."])


# ------------------------------------------------------------- slide 6: skill 4
def slide6():
    return detail_slide(
        6, "skill 4 of 4", "You're not an order-taker.", "You're the architect.",
        "04", "SHAPE THE BUILD", PASTELS[3],
        ["Deciding which problem is worth", "solving is part of the job now,",
         "not a bonus round after the ticket", "lands in your queue."],
        ["The robot lays the bricks.", "You still decide where the wall goes."])


# ---------------------------------------------------------- slide 7: diagnostic
DIAG = [
    ("SKILL 1", PASTELS[0], "You ship the AI feature and hope it works",
     "run evals, do error analysis"),
    ("SKILL 2", PASTELS[1], "You accept whatever tradeoff the AI made",
     "name the tradeoff yourself, first"),
    ("SKILL 3", PASTELS[2], "You approve every agent suggestion by default",
     "calibrate trust, verify the risky ones"),
    ("SKILL 4", PASTELS[3], "You wait for the ticket to tell you what to build",
     "pick the problem before it's assigned"),
]


def slide7():
    b = eyebrow("find yourself in the four")
    b.append(txt(M, 262, "One habit.", size=58, weight=900, fill=INK))
    b.append(txt(M, 326, "One architect move.", size=58, weight=900, fill=INK))
    y = 400
    for chip, tint, symptom, move in DIAG:
        b.append(rect(M, y + 14, 152, 58, tint, r=10))
        b.append(txt(M + 76, y + 52, chip, size=20, weight=900, fill=INK,
                     font=MONO, anchor="middle", ls=1))
        b.append(txt(M + 182, y + 42, symptom, size=27, weight=700, fill=INK))
        b.append(txt(M + 182, y + 84, "→  " + move, size=24, weight=400,
                     fill=ORANGE, font=MONO))
        if chip != "SKILL 4":
            b.append(line(M, y + 128, RIGHT, y + 128, HAIR, 2))
        y += 152
    b.append(txt(M, y + 30, "Still a bricklayer on the left.", size=24, weight=400, fill=GREY))
    b.append(txt(M, y + 66, "Already the architect on the right.", size=24, weight=700, fill=INK))
    return frame(b, 7)


# -------------------------------------------------------- slide 8: close + CTA
def slide8():
    b = eyebrow("the takeaway")
    b.append(txt(M, 268, "Don't just learn to", size=58, weight=900, fill=INK))
    b.append(txt(M, 332, "write code.", size=58, weight=900, fill=INK))
    b.append(txt(M, 396, "Learn to think like a", size=58, weight=900, fill=INK))
    b.append(txt(M, 460, "senior engineer.", size=58, weight=900, fill=ORANGE))
    b.append(rect(M, 560, COL, 300, "#FFFFFF", r=18, op=0.5))
    b.append(txt(M + 40, 620, "THE FOUR, ONE MORE TIME",
                 size=21, weight=900, fill=GREY, font=MONO, ls=2))
    recap = ["1. Build & deploy AI applications",
             "2. Software fundamentals",
             "3. Use coding agents well",
             "4. Shape the build"]
    y = 672
    for r in recap:
        b.append(txt(M + 40, y, r, size=30, weight=700, fill=INK))
        y += 52
    b.append(rect(M, 902, 6, 152, ORANGE, r=3))
    b.append(txt(M + 34, 958, "Of the four, which one are you", size=42, weight=900, fill=INK))
    b.append(txt(M + 34, 1008, "actually building, and which one", size=42, weight=900, fill=INK))
    b.append(txt(M + 34, 1058, "are you just hoping the agent", size=42, weight=900, fill=INK))
    b.append(txt(M + 34, 1108, "handles for you?", size=42, weight=900, fill=ORANGE))
    return frame(b, 8)


BUILDERS = [slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8]

if __name__ == "__main__":
    out = os.environ["OUT_DIR"]
    for i, fn in enumerate(BUILDERS, start=1):
        p = os.path.join(out, f"slide-{i}.svg")
        with open(p, "w") as f:
            f.write(fn())
        print(f"wrote {p} ({os.path.getsize(p)} bytes)")
