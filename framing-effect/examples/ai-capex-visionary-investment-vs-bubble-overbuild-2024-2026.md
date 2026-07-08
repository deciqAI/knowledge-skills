# Method in Action: The 2024–2026 AI Capex Debate — "Visionary Infrastructure" vs "Bubble-Era Overbuild"

> *Example for the [framing-effect](../SKILL.md) skill.*

Between 2024 and 2026, the largest US technology companies — including Microsoft, Alphabet, Amazon, and Meta — dramatically increased capital expenditure on AI infrastructure: data centers, GPUs, and power. Nvidia, the dominant supplier of AI accelerators, became one of the most valuable companies in the world on the strength of this spending. The identical spending was described in two sharply different ways by different parties, and the two descriptions pointed toward opposite decisions on identical facts. This is a live, unfolding case of the framing effect operating on tens of billions of dollars of capital allocation — not a hypothetical. Below it is run through the skill's own six-step Process.

## Step 1 — Identify the frame

Two dominant frames circulated over 2024–2026 for the same underlying fact set (rapidly rising hyperscaler AI capex, concentrated GPU demand, unprecedented single-company valuations):

- **Gain / goal frame — "visionary infrastructure investment":** Verbatim genre of language from company leadership and bullish analysts — build the compute now to *capture* the generational platform shift; *the risk of under-investing is far greater than the risk of over-investing* (a formulation publicly voiced by several hyperscaler CEOs on 2024–2025 earnings calls). Framer: the companies doing the spending and the vendors selling into it, whose incentives favor continued build-out.

- **Loss / risky-choice frame — "bubble-era overbuild":** Verbatim genre — this is a *bubble*; the capex will be *stranded*; returns on the invested capital are unproven; comparisons to the late-1990s telecom/fiber overbuild and the dot-com bust. Framer: skeptical analysts, short-sellers, and commentators, whose incentives favor caution or a falling price.

Both frames describe the *same facts*: very large, rising AI capital expenditure and historically high AI-linked valuations. The word "investment" pre-loads a gain; the word "overbuild" pre-loads a loss. This is a compound frame — goal ("build to gain the platform" vs "skip and stay lean"), attribute ("visionary" vs "bubble"), and risky-choice (a bet with an uncertain payoff described from the upside vs the downside).

## Step 2 — Construct the equivalent alternative frame

Strip the evaluative words and state the shared math both frames sit on:

> A firm commits a large sum of capital now for AI compute. If demand for AI services materializes at expected scale, the assets earn a strong return (gain). If demand is slower or smaller than expected, some of the assets are under-utilized or written down (loss). The outcome is uncertain.

"Visionary investment" is this same statement told from the branch where demand materializes. "Bubble overbuild" is the same statement told from the branch where it does not. Neither adds a fact the other omits — they select which uncertain branch to name. That is the tell of a framing effect rather than a genuine information difference: **mathematically equivalent, opposite wording.**

(Contrast this with a *non-equivalent* claim, which the skill says to exclude: "these depreciation schedules understate the true useful life of the GPUs" is a substantive factual dispute, not a reframing. Keep those separate from the frame audit.)

## Step 3 — Re-evaluate: does the choice flip under the alternative frame?

Consider an investor or a board deciding whether to keep funding the build-out.

- Under **"visionary infrastructure investment"** (gain frame), the natural response is to lean in: not spending feels like forgoing a sure generational gain — a loss of position. Gain-mode makes the sure-thing-of-inaction feel like the real risk.
- Under **"bubble-era overbuild"** (loss frame), the natural response is to pull back: continuing to spend feels like courting a large, vivid loss. Loss-mode makes further commitment feel reckless.

Identical capex plan, identical facts, opposite lean depending on the label. When the choice flips on the word alone, **the frame is doing the work** — exactly the description-invariance violation the skill targets.

## Step 4 — Compute the frame-independent expected value

Drop both labels and ask the frame-neutral question: *does the probability-weighted return on this capital exceed its cost, and can the balance sheet survive the downside branch?*

This is a genuinely open empirical question as of early 2026, and honesty requires saying so — the framing audit does **not** resolve whether the capex is wise. What it does is force the decision onto the real variables:

- The base-rate outside view (fat-tailed infrastructure build-outs: railroads, fiber — many end in write-downs even when the underlying technology proves transformative) argues for caution on *any single firm's* return.
- The inside view (measured AI revenue growth, utilization, and demand signals available at the time) argues on the other side.
- A firm with a fortress balance sheet that can absorb a stranded-asset scenario faces a different frame-independent EV than a highly leveraged one that cannot survive the loss branch — even on identical capex. (See [`margin-of-safety`](../margin-of-safety/SKILL.md) and [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) for sizing under this uncertainty, and [`black-swan`](../black-swan/SKILL.md) for the fat tail.)

The frame-independent answer is therefore *conditional on numbers and survivability*, not on whether you called it "visionary" or a "bubble."

## Step 5 — Diagnose framer intent

- **Who benefits from the "visionary investment" frame?** The hyperscalers justifying the spend to shareholders, and the hardware and cloud vendors selling the picks and shovels. A gain frame keeps capital flowing toward them.
- **Who benefits from the "bubble overbuild" frame?** Short-sellers positioned for a fall, and commentators for whom a contrarian-crash narrative earns attention.

Neither framer is neutral. The skill's rule: identify the framer's incentive and treat the frame as *chosen to steer*, not as a neutral readout of the facts. Note also the reflexive move to watch for — labeling the opposing frame as "just spin" or "just hype" is itself a frame-defense, not an argument.

## Step 6 — Choose the response

The correct response here is **expose the frame, then decide on the frame-independent EV**, not to adopt either label. Concretely:

1. State both frames side by side so neither dominates the decision environment — the *structural* defense (competitive framing) that the literature shows actually reduces the effect, versus mere vigilance which does not.
2. Route the decision to the frame-neutral variables from Step 4: probability-weighted return, utilization evidence, and downside survivability of *this specific* balance sheet.
3. Size the commitment to survive the loss branch regardless of how confident the gain frame sounds.

The takeaway is not "the AI build-out is good" or "it is a bubble" — the framing audit deliberately refuses to answer that. It is that *the label was silently carrying the argument*, and the actual decision belongs to the numbers underneath both labels.

*Sources: Tversky, A., & Kahneman, D. (1981), "The framing of decisions and the psychology of choice," Science, 211(4481), 453–458 (the framing effect and description invariance). Levin, Schneider & Gaeth (1998) on the risky-choice / attribute / goal frame typology. Company AI-capex increases and Nvidia's rise to among the world's most valuable companies over 2024–2025 are widely reported in mainstream financial coverage (e.g., Reuters, Financial Times, Wall Street Journal earnings-call and market coverage) and in the companies' own quarterly filings and earnings calls; specific figures vary by quarter and are not asserted here. The "risk of under-investing exceeds the risk of over-investing" framing was voiced publicly by hyperscaler executives on 2024–2025 earnings calls; the "bubble"/telecom-overbuild analogy was a recurring theme among skeptical analysts and commentators over the same period.*
