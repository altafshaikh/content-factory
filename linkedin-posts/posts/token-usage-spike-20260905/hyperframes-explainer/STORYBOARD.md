---
format: 1080x1350
duration: 30s
message: "You think in messages. You get billed in turns: every call re-sends the whole context."
arc: Hook → Mechanism → Worked example → Rule → Fix → Close
audience: engineers running coding agents who read their usage in messages
mode: autonomous
music: none
structure: concept
---

## Video direction

- **Canvas:** 1080x1350 portrait (4:5, the LinkedIn feed default). Silent: no narration, no BGM, no SFX, no captions. Because there is no voice, the on-screen copy carries the argument; every frame lists its copy verbatim under "On-screen copy" and nothing else may be rendered as text.
- **Palette (frame.md roles):** ground = cream; secondary surfaces = tile / tile-strong cards with hairline ink@12% borders; text = ink; the ONE voltage per frame = coral (the growing quantity: turns, the re-sent file, the growing term, the fix). navy is used only for the formula plate in frame 05 and the settings line in frame 06. No other hues.
- **Type:** display ramp EB Garamond 400 (headline / display / number-hero) for statements and hero numbers; JetBrains Mono (kicker, mono-label, number-unit) for units, axis labels and eyebrows; Inter body only for small supporting labels. Sentence case. Kicker eyebrows carry the coral spike prefix.
- **Motion grammar:** one paused timeline per frame; long-tail power3.out entrances; each piece reveals on its beat across the full duration (silent frames pace to the beat, never front-loaded); end each frame on a held, still read. No bouncy springs, no drift, no breathing.
- **Rhythm:** 30s test cut (gap and brake scenes dropped 2026-09-29). 01 is a fast type beat; 03 and 04 are the builds; 05 is the held landing; 07 is steady; 08 is a calm close with the only exit fade.
- **Layout:** 4:5 feed, three bands, all used: top y 80-380 kicker + headline; middle y 380-880 the focal at 40-60% of frame; lower y 880-1120 a real element (payoff line, stat, axis, footer, handle). Settled read reaches y >= 1000, no empty band over 200px. All content above y = 1120 (83% keep-out). Vary framing: centered type (01, 08), stacked contrast (02), full-width strip diagram (03), bar chart (04), centered plate (05), stacked two-row comparison (06), vertical step list (07).
- **Negative list:** no emojis, no company or product names, no em dashes, no gradients, glows, bokeh or purple-blue AI looks, no cursor, no browser chrome, no second coral element in a frame. Never front-load then freeze; never let elements float independently like a screensaver.

## Frame 1 — Hook

- scene: Three short facts slam in one after another, stacked, then hold
- voiceover: ""
- duration: 4.4s
- transition_in: cut
- status: animated
- src: compositions/frames/01-hook.html
- type: hook
- persuasion: Cold open on a surprising number (pattern interrupt)
- beat: surprise
- blueprint: kinetic-type-beats (Adapt)
- focal: the number 427
- roles: cream field with a faint hairline rule grid = background · three stacked fact lines = foreground subject · kicker eyebrow = supporting

narrativeRole: States the messages-versus-calls gap as a bare fact before any argument.
keyMessage: One small session produced a surprising number of API calls.

On-screen copy (verbatim): kicker "ONE SESSION" · line 1 "Five messages." · line 2 "427 API calls." (427 in coral, number-hero scale) · line 3 "Twelve hours."

Adapt: keep the statement-builds-across-beats signature; the three beats stack vertically instead of replacing each other, so the full triple reads at the end.
Scene 1 (0.0–0.9s): cream ground and kicker "ONE SESSION" at top-left; "Five messages." rises in (headline scale), upper third, left-aligned.
Scene 2 (0.9–2.2s): "427 API calls." slams in below (kinetic-beat-slam, scale-slam entrance) at display scale, 427 in coral as number-hero; the biggest element on the frame, around 0.4 x height.
Scene 3 (2.2–3.2s): "Twelve hours." rises in below at headline scale, ink.
Scene 4 (3.2–4.5s): all three hold still; the read settles.

## Frame 2 — Mechanism

- scene: Three calls drawn as growing stacks; each call carries every block from the calls before it
- voiceover: ""
- duration: 5.6s
- transition_in: push-slide
- status: animated
- src: compositions/frames/03-mechanism.html
- type: feature_showcase
- persuasion: Progressive disclosure (build the stack one call at a time)
- beat: comprehension
- blueprint: compose
- focal: the three growing call stacks
- roles: cream field = background · three vertical stacks of blocks = foreground subject · headline and call labels = supporting

narrativeRole: Shows why: the model has no memory, so every call re-sends the whole conversation, and the resend grows.
keyMessage: Call three carries everything from calls one and two.

On-screen copy (verbatim): kicker "NO MEMORY" · headline "Every call re-sends the entire conversation." · block labels (mono-label, inside blocks): "read file", "run command", "read file" · column labels: "CALL 1", "CALL 2", "CALL 3" · footer line "Call three carries calls one and two."

Compose: a full-width strip of three bottom-aligned columns. Each column is a stack of tile blocks; column 1 has one block, column 2 has two, column 3 has three. The newest block in each column is coral; carried-over blocks are tile with hairline borders, so the viewer sees the same blocks reappear.
Scene 1 (0.0–1.2s): kicker and headline fade up at the top (headline scale, two lines max).
Scene 2 (1.2–2.4s): column "CALL 1" builds: one coral block "read file" rises in.
Scene 3 (2.4–3.6s): column "CALL 2" builds: a tile copy of "read file" rises in, then a coral "run command" block lands on top.
Scene 4 (3.6–4.9s): column "CALL 3" builds: tile copies of "read file" and "run command" rise in, then a coral "read file" block lands on top.
Scene 5 (4.9–6.5s): footer "Call three carries calls one and two." fades up below the columns; hold still.

## Frame 3 — The worked example

- scene: A bar chart of context size across a 947-call session; a constant coral slab rides in every bar from call 200
- voiceover: ""
- duration: 6.2s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-example.html
- type: social_proof
- persuasion: Concretization (one real number, shown)
- beat: dawning cost
- blueprint: dataviz-countup (Adapt)
- focal: the coral slab repeated in every bar after call 200
- roles: cream field = background · 10 growing bars with the coral slab = foreground subject · axis labels and the count-up = supporting

narrativeRole: Makes the mechanism concrete with the post's own example: one file read, paid on every later call.
keyMessage: One 21,000-token file read at call 200 was re-sent for 747 more calls.

On-screen copy (verbatim): kicker "ONE FILE READ" · headline "Read once. Re-sent 747 times." · slab label "21,000-token file" · axis labels "CALL 1", "CALL 200", "CALL 947" · stat "~16M tokens" · sub "roughly $8, for one file read"

Adapt: keep the count-up-to-a-hero-metric signature and the stat-bars growth; bars carry the argument (bar height = context re-sent on that call). 10 bars grow left to right; from the bar at call 200 onward each bar contains an identical coral slab at its base (same physical height every time) while the bar above it keeps growing.
Scene 1 (0.0–1.2s): kicker and headline fade up at the top.
Scene 2 (1.2–2.8s): growth bars (stat-bars-and-fills): the first 2 bars (before call 200) grow in, ink@20% tile fills, small; axis label "CALL 1" under the first.
Scene 3 (2.8–3.8s): the bar at call 200 grows in with the coral slab at its base; label "CALL 200" and the slab label "21,000-token file" appear beside it.
Scene 4 (3.8–5.3s): the remaining 7 bars grow in with a short stagger, each taller, each carrying the identical coral slab; "CALL 947" under the last.
Scene 5 (5.3–7.0s): below the chart "~16M tokens" counts up (counting-dynamic-scale) (number-hero figure, mono unit), then the sub "roughly $8, for one file read" fades in; hold still.

## Frame 4 — The rule

- scene: The cost formula assembles term by term on a dark plate, then the quadratic consequence lands
- voiceover: ""
- duration: 4.8s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/05-rule.html
- type: branding
- persuasion: Frame-then-fill (state the formula, then its consequence)
- beat: clarity
- blueprint: compose
- focal: the formula plate
- roles: cream field = background · navy formula plate = foreground subject · consequence lines = supporting

narrativeRole: Generalizes the example into the rule and its non-obvious consequence.
keyMessage: Cost grows with the square of session length.

On-screen copy (verbatim): kicker "THE RULE" · formula on the navy plate: "cost" "=" "average context" "×" "number of calls" (both growing terms in coral text) · line "2× longer session" · line "≈ 4× the cost" (in ink at display scale; the frame's one coral role is the two growing terms)

Compose: centered navy plate (code surface, radius-lg) at about 0.35 x height holding the formula in cream mono and display; the two terms "average context" and "number of calls" are coral text (the frame's one voltage, a single role). Below the plate, a stacked two-line consequence.
Scene 1 (0.0–0.8s): kicker fades up; the navy plate scales in from 0.96.
Scene 2 (0.8–2.6s): the formula assembles term by term inside the plate: "cost", "=", "average context", "×", "number of calls".
Scene 3 (2.6–3.8s): "2× longer session" rises in below the plate (headline scale).
Scene 4 (3.8–5.5s): "≈ 4× the cost" rises in beneath at display scale; hold still (the held landing of the film).

## Frame 5 — The fix

- scene: Two numbered steps assemble as a vertical list
- voiceover: ""
- duration: 5.0s
- transition_in: push-slide
- status: animated
- src: compositions/frames/07-fix.html
- type: feature_showcase
- persuasion: Numbered enumeration
- beat: relief
- blueprint: grid-card-assemble (Adapt)
- focal: the two step cards
- roles: cream field = background · two hairline step cards = foreground subject · kicker and headline = supporting

narrativeRole: Gives the two actions that remove the problem, neither of them a better prompt.
keyMessage: Drop the 1M default and run one session per task.

On-screen copy (verbatim): kicker "TWO FIXES" · headline "Neither of them a better prompt." · card 1 index "01" title "Drop the 1M default." body "Switch it on per session, when a task genuinely needs it." · card 2 index "02" title "One session per task." body "Clear in between."

Adapt: keep the staggered-cascade assemble signature; only two cards, stacked vertically, full width. The coral voltage is the index numerals "01" and "02" (one role).
Scene 1 (0.0–1.2s): kicker and headline fade up at the top.
Scene 2 (1.2–3.2s): card 1 rises in (index, then title, then body in quick succession).
Scene 3 (3.2–5.0s): card 2 rises in the same way below it.
Scene 4 (5.0–6.0s): hold still.

## Frame 6 — Close

- scene: The post's closing challenge, centered, held, then a quiet fade out
- voiceover: ""
- duration: 4.0s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-close.html
- type: cta
- persuasion: Direct challenge (call to check your own data)
- beat: resolve
- blueprint: titlecard-reveal (Reproduce)
- focal: the challenge line
- roles: cream field = background · two-line challenge = foreground subject · handle = supporting

narrativeRole: Turns the explanation into an action the viewer can take today.
keyMessage: Go count the API calls behind one of your messages.

On-screen copy (verbatim): line 1 "Open your longest session from this week." · line 2 "Count how many API calls came out of one message." ("one message" in coral) · handle "@teachmebro" (mono-label)

Reproduce: one restrained slide-up crossfade reveal, then a still hold; this is the final frame so it owns the only exit (a gentle fade of content in the last 0.6s).
Scene 1 (0.0–1.4s): line 1 slides up and fades in, headline scale, centered around 0.35 x height.
Scene 2 (1.4–2.8s): line 2 slides up beneath it, display-italic or headline scale, "one message" in coral.
Scene 3 (2.8–4.9s): handle fades in lower (above the keep-out); hold still.
Scene 4 (4.9–5.5s): all content fades to the cream ground.
