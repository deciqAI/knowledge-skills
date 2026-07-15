---
name: pricing-strategy
description: "Activate when: user says 'how should we price this', 'we should just charge more', 'our competitors charge X', 'willingness to pay', 'anchor price', 'value-based pricing', 'freemium structure', setting a first price for a new product, considering a price increase and worried about churn, or needing to design tiered/usage-based pricing.
  Do NOT activate when: the product has no demonstrated value yet (use lean-startup instead); price is fixed by regulation."
---

# Pricing Strategy

## Overview

Price is a structural decision, not a calculated number. Cost-plus and competitor-matching both ignore 50 years of pricing research: **what people pay is shaped by reference points, anchoring, loss aversion, and offer structure** — not by cost. Kahneman & Tversky (*Econometrica* 1979): losses hit ~2× harder than equal gains. Thaler (1980): endowment effect and mental accounting drive consumer pricing behavior.

Compose with: [first-principles](../first-principles/SKILL.md) · [probabilistic-thinking](../probabilistic-thinking/SKILL.md) · [pareto-principle](../pareto-principle/SKILL.md) · [pmf-crossing-the-chasm](../pmf-crossing-the-chasm/SKILL.md).

## When to Use

Apply when: setting initial prices; planning a price change (especially raising); designing freemium/tiered/usage structures; sales asks for discounts >1/week; competitors' price is the only input; pricing an AI product against volatile/falling inference costs and choosing seat- vs. usage- vs. outcome-based models, protecting gross margin as AI capex and model releases shift the cost floor, or defending price against AI-native competitors pricing off the same collapsing token cost.

**When NOT to use:** no demonstrated value (use [lean-startup](../lean-startup/SKILL.md)); price regulated; purely tactical single-deal discount; LTV/CAC already working and question is execution only.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has segment + value data → run The Process directly.
- **Coach mode:** vague or unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is.** Pricing is a designed signal — what people pay depends on reference points and loss aversion far more than on cost.
2. **Check fit.** No demonstrated value → [lean-startup](../lean-startup/SKILL.md). Regulated → wrong scope.
3. **Elicit value.** What outcome does the customer get, in their metric? ("save 8 eng-hours/week" not "makes them faster")
> **[WAIT — do not advance until user responds]**
4. **Walk The Process one step at a time** with their input.
> **[WAIT — do not advance until user responds]**
5. **Close** with one price, one anchor, one structure, one 60-day experiment.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Pricing Audit**. Value-first, anchor, structure, frame, test.

1. **Articulate value to the customer in customer units.** Not "our software does X" but "saves them $50K/year in engineering-hours." If you cannot name the value in the customer's metric, pricing is guesswork.
2. **Estimate WTP per segment.** Use Van Westendorp Price Sensitivity Meter (4-question survey), conjoint analysis, or direct evidence from paid pilots (B2B — most reliable).
3. **Choose an anchor.** First price seen frames every subsequent price. Anchor high if defensibly justified; the high anchor lifts the entire tier structure.
4. **Design the tier structure.** 3 tiers (Starter / Pro / Enterprise): Starter makes Pro feel affordable; Enterprise anchors and captures top WTP; Pro is the target sweet spot.
5. **Frame for loss aversion.** "Save $X by paying annually" beats "monthly costs $Y more" ~30%. Money-back guarantee converts ~10–30% higher than free trial. Per-user vs. flat-fee: per-user for SMB, flat-fee captures more enterprise value.
6. **Stress-test the anchor.** Show prices to 5–10 target-segment buyers: "expensive but worth it?" / "too expensive?" / "I'd buy at this price." Adjust if segment reference point is materially below anchor.
7. **Run a 60-day measurement.** Track: conversion rate, upgrade rate (Starter → Pro), discount-request frequency, revenue per tier. High upgrade rate + low discount-request frequency = right structure.

### Output: Pricing Audit (fill after each step)

| Field | Your answer |
|---|---|
| Value to customer (customer units) | |
| Segment WTP range + method | |
| Chosen anchor + justification | |
| Tier structure (Starter / Pro / Enterprise) | |
| Loss-aversion framing chosen | |
| Anchor stress-test result (5–10 buyers) | |
| 60-day metrics + re-evaluation date | |

*→ Method in Action: [De Beers and the Engagement Ring (1947 → ongoing)](examples/de-beers-and-the-engagement-ring-1947-ongoing.md) · [Netflix's Qwikster Failure (2011)](examples/netflix-qwikster-price-restructuring-2011.md)*

*→ 2026 lens: [Pricing an AI product under volatile inference costs — seat vs. usage vs. outcome (2023–2026)](examples/ai-product-pricing-under-volatile-inference-costs-2023-2026.md)*

## Pricing Packs

Domain patterns (anchors / tier structure / key framing / dominant failure):
- **B2B SaaS:** TCO-comparison / 3-tier Team-Pro-Enterprise / "save 20% annual" / underpricing Enterprise.
- **Consumer subscriptions:** Category norms / 2-tier Free-Paid / free-trial auto-conversion / free tier too generous.
- **Enterprise services:** Peer-engagement / project-priced / cost-of-NOT-engaging / hourly billing.
- **Luxury/signaling:** Social reference points / quality-attribute ladder / identity framing / anchor commodifies.

## Applying It Well

- **Price is a designed signal.** Cost-plus leaves money on the table; competitor-matching anchors you to someone else's (possibly wrong) positioning.
- **The anchor matters more than the price.** First number frames every subsequent one. Anchor high if defensibly justified.
- **Loss aversion ~2× gain framing.** Frame upgrades around what's lost by not upgrading.
- **WTP variance is larger than founders expect.** Top-segment WTP often 5–10× bottom for the same product.
- **Discount frequency is the leading indicator.** >1/week = structure is wrong. Fix structure, not the deal.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Cost-plus pricing** | Cost is unrelated to value. Systematically underprices high-value products, overprices commodity ones. |
| [D] **"Competitors charge X so we should too"** | Anchors you to their (possibly wrong) positioning for *their* segment. Use as data, not anchor. |
| [D] **Discounting deal-by-deal** | Erodes the public anchor, training all customers to negotiate. Fix structure, not the deal. |
| [D] **Single-tier pricing** | Misses segment-WTP variance. Tier structure captures multiple WTP points without changing the product. |
| [D] **"We should just charge more"** | Without identifying which segment pays more for what value, this is wishful thinking. |
| [D] **Underpricing to "establish" first** | Initial pricing anchors permanent expectations. Raising later triggers loss aversion. Launch at intended price. |
| [D] **Free tier too generous** | Eliminates the loss-aversion upgrade lever. Free = enough to taste, not enough to satisfy. |
| [D] **Ignoring loss-aversion framing** | "Save $200/year" converts ~30% better than "monthly costs $200 more" for identical economics. |
| [D] **No WTP measurement** | Setting price without Van Westendorp, paid pilot, or conjoint is guessing. Free methods exist. |
| [D] **No 60-day re-evaluation** | Pricing is a hypothesis. Conversion data should refine the structure, not be ignored. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Rationale is "cost + markup" or "competitor matching" without value reasoning
- Single tier only; no A/B test on framing; no WTP measurement
- Discount requests >1/week; free tier delivers most of the product's value
- No re-evaluation in 12+ months despite material business changes

## Verification

- [ ] Value in customer units (not features); WTP estimates with method named
- [ ] Anchor explicitly chosen and justified; stress-tested with 5+ buyers
- [ ] Tier structure: middle tier is the designed sweet spot
- [ ] At least one loss-aversion framing applied
- [ ] 60-day measurement plan with re-evaluation date

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/pricing-strategy** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
