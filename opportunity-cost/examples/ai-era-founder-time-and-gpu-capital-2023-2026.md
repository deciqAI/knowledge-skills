# Method in Action: The AI-Era Opportunity Cost of Founder Time and GPU Capital (2023–2026)

> *Example for the [opportunity-cost](../SKILL.md) skill.*

Since the public release of ChatGPT in November 2022, the generative-AI wave reset the opportunity-cost calculus for nearly every founder, engineer, and capital allocator in technology. The visible costs — GPU dollars, salaries, the quarters spent building a roadmap — are easy to name. The *unseen* alternative, in Bastiat's language, is what those same resources would have produced under the best forgone plan. This example runs the skill's six-step Process over that anchor case: **every quarter spent on a non-AI roadmap, and every GPU dollar, measured against the best forgone alternative.**

The point of the exercise is *not* to conclude "everyone should have pivoted to AI." That is hindsight. Opportunity cost is prospective and subjective (Buchanan, 1969): the analysis is only honest when it uses what was reasonably knowable at the moment of choice, and prices *both* the road taken and the road forgone. We run it in that spirit.

---

## Step 1 — State the choice + resources committed

**Choice under examination:** A well-funded software company (or founder) allocating its scarce resources across the 2023–2026 window.

**Resources committed, per quarter:**
- **Founder / senior-engineer time** — the highest-opportunity-cost input in any company. A quarter of the founding team's attention is a large, non-recoverable slice of an early-stage company's limited runway.
- **Capital, increasingly in the form of compute.** By 2024–2025 a large and rising share of frontier-AI spending went to GPUs and data-center capacity. Nvidia's data-center revenue grew several-fold year over year through fiscal 2024–2025, and the company's market capitalization crossed the $1 trillion mark in 2023 and continued climbing thereafter — a market-priced signal of how much capital was flowing into AI compute. (Nvidia investor filings; widely reported.)
- **Roadmap quarters** — the sequential, non-recoverable unit. A roadmap is a queue; a quarter spent shipping feature A is a quarter not spent shipping feature B.

**Timeframe:** Rolling quarters, 2023 through 2026.

---

## Step 2 — List 3–5 realistic alternatives (including "do nothing / hold the resource")

For a given quarter of founder-time and a given dollar of capital, the realistic alternatives an operator faced in this window included:

- **A — Ship the existing non-AI roadmap.** Continue the pre-2023 plan (core product, existing verticals).
- **B — Add an AI layer to the existing product.** Integrate hosted models (e.g., via the OpenAI or Anthropic APIs, both broadly available to developers by 2023–2024) into the current product rather than rebuilding.
- **C — Rebuild around AI / train or fine-tune models, buying or renting GPU capacity.** The capital-intensive path.
- **D — Hold the resource: extend runway, bank the cash, keep the team small.** The "do nothing" branch — never omit it.
- **E — Deploy capital into the AI-adjacent picks-and-shovels layer** (tooling, data, infrastructure) rather than an end-user app.

---

## Step 3 — Estimate value per alternative (financial + non-financial; ranges are fine)

Precise forward values were unknowable; the discipline is to bound them, not to fake precision.

| Alternative | Financial value (range / direction) | Non-financial value |
|---|---|---|
| A — Ship non-AI roadmap | Known near-term revenue; but rising risk of being leapfrogged as AI-native entrants appeared across categories | Continuity, low execution risk, but eroding narrative and hiring pull |
| B — AI layer on existing product | Moderate cost (API usage priced per token, falling sharply over 2023–2025 as providers cut prices); fast time-to-ship | Preserves roadmap; captures "AI" positioning; low lock-in |
| C — Rebuild + own GPU compute | Very high cash burn; GPU capacity was supply-constrained and expensive in 2023–2024; outcome highly uncertain | Potential deep moat *or* stranded capital; large distraction risk |
| D — Hold / extend runway | Preserves optionality; low variance | Buys time to observe; risks irrelevance if the window closes |
| E — Picks-and-shovels layer | Rode aggregate AI demand rather than one app's success | Less headline upside; more durable if the app layer commoditizes |

The single most important 2023–2025 fact for this table: **the price of using frontier models via API fell dramatically** over the window as providers repeatedly cut per-token prices and released cheaper model tiers. That falling price steadily improved the expected value of Alternative B relative to Alternative C — renting intelligence got cheaper faster than owning it usually paid off.

---

## Step 4 — Identify the opportunity cost (value of the highest-ranked *unchosen* alternative)

Opportunity cost is the *next-best* forgone option, not the average and not the worst.

- **For the operator who chose A (pure non-AI roadmap):** the OC is typically **B** — the AI layer they could have shipped cheaply on falling-price APIs. Each quarter on A forgoes the compounding positioning, data, and learning of B. This is the "quarter spent on a non-AI roadmap" cost made explicit.
- **For the operator who chose C (own the GPUs / train from scratch):** the OC is frequently **B or E** — the far cheaper integration path, plus the runway that the GPU capital would otherwise have bought. When model prices fell and hosted models improved, capital sunk into owned training frequently underperformed the forgone "rent + integrate" alternative. This is the "every GPU dollar" cost made explicit.

Note the asymmetry: the OC of *inaction* (staying on A) and the OC of *over-action* (over-committing to C) are both real. Bastiat's parable cuts both ways.

---

## Step 5 — Compare: Net benefit = Value of chosen − OC

- **Chose A, OC = B:** Net benefit is often **negative** by 2025 in categories where AI-native competitors emerged — the visible near-term revenue was outweighed by the forgone, cheaply-attainable AI position. Reconsider.
- **Chose C, OC = B/E:** Net benefit is **negative** precisely when hosted-model price/performance improved faster than the owned-compute bet could pay back — a well-documented direction of travel across 2023–2025. For most application-layer companies, renting beat owning. (For a handful of frontier labs with genuine scale and differentiated data, C could clear its OC — the analysis is decision-maker-specific, exactly as Buchanan insisted.)
- **Chose B:** Frequently **positive** — low cost, falling further, preserved roadmap, captured positioning.

---

## Step 6 — Surface non-financial opportunity costs

These usually dominate the cash line:

- **Time / attention.** Founder attention is the company's highest-OC resource (Grove, 1983). A rebuild-everything AI pivot (C) can consume the founding team's focus for multiple quarters — the true cost is every other thing that focus would have produced.
- **Headcount.** Engineers assigned to train/serve models in-house are engineers not shipping product. Through 2023–2025, AI/ML talent was scarce and expensive, raising this OC further.
- **Optionality.** Renting intelligence (B) keeps options open; sinking capital into owned GPUs (C) converts flexible cash into a specific, hard-to-reverse bet. In a market where model prices and capabilities moved fast, optionality was itself worth a great deal.
- **Reputation / narrative.** By 2024, "AI story" affected hiring and fundraising. Staying on A carried a narrative OC; over-hyping a thin AI bolt-on carried a credibility OC.

---

## The takeaway

The AI era did not change the model — it raised the stakes on getting the model right. Opportunity cost says the true cost of a quarter on the non-AI roadmap is the best AI-adjacent thing that quarter could have built, and the true cost of a GPU dollar is the best forgone use of that dollar (often: runway, or renting the same intelligence for less as prices fell). Both the founder who ignored the wave *and* the founder who over-rotated into owning compute can be shown, by the same skill, to have paid an opportunity cost they never put on the visible ledger. Run Steps 1–6 before committing the next quarter and the next dollar — not after.

*Sources: Nvidia Corporation investor relations and quarterly filings, fiscal 2024–2025 (data-center revenue growth; market-capitalization milestones), nvidianews.nvidia.com and investor.nvidia.com. OpenAI and Anthropic public model and API pricing announcements, 2023–2025 (per-token price reductions and lower-cost model tiers), openai.com and anthropic.com. Buchanan, J. M. (1969), *Cost and Choice* (cost is prospective, subjective, decision-maker-specific). Grove, A. S. (1983), *High Output Management* (founder/manager time as the highest-opportunity-cost input). Bastiat, F. (1850), *Ce qu'on voit et ce qu'on ne voit pas* (the seen-vs-unseen asymmetry). General market context (ChatGPT public launch, Nov 2022; the 2023–2025 generative-AI investment wave) is widely and durably documented in mainstream financial and technology press.*
