---
name: death-spiral
description: "Activate when: user says 'we're losing market share,' 'our growth keeps slowing and I don't know why,' 'a competitor is gaining on us fast,' 'what's the worst-case trajectory here,' or a business shows two or more consecutive quarters of declining key metrics with no identified reversal mechanism.
  Do NOT activate when: decline is clearly seasonal or macro-cyclical with demonstrated historical recovery; or the company is pre-product/pre-revenue with no existing moat to audit."
---

# Death Spiral

## Overview
A death spiral is a self-reinforcing negative feedback loop in competitive markets. Unlike ordinary decline — which is linear and potentially reversible — a death spiral is non-linear: each deterioration step actively causes the next to be worse and faster. The cycle begins when a competitor breaches a company's primary moat, then propagates through share loss → revenue decline → R&D contraction → product lag → further moat erosion.

**Cross-skill composition:** Use WITH [second-order-thinking] to trace downstream consequences early. Use BEFORE [margin-of-safety] to know which buffer to maintain. Use WITH [dynamic-core-competence] to diagnose which competence decay triggers the spiral.

## When to Use
- Multi-quarter deterioration in key metrics with no identified reversal mechanism
- Competitor has established a durable product, distribution, or network advantage
- R&D budget being cut in response to revenue shortfalls (most dangerous early-spiral indicator)
- Leadership team minimizing a competitive threat as "temporary" without quantitative analysis

**When NOT to use:** Decline is cyclical with demonstrated historical recovery; company is pre-product/pre-revenue; feedback loop has already completed (post-mortem use only).

## Coaching Novices (Adaptive Front Door)
- **Engine mode:** user has concrete multi-quarter data → run The Process directly.
- **Coach mode:** user says "we're losing customers and I'm worried" → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is:** A death spiral is a feedback loop where decline causes the conditions that accelerate further decline — self-amplifying, not just bad performance.
2. **Check fit:** Are any declines causing other declines? Revenue loss → R&D cuts → product lag → more revenue loss? Feedback loop = yes; standard problem = no.
3. **Elicit:** What makes customers stay? Which moat dimension has a competitor made progress against in the last 12 months?
> **[WAIT — do not advance until user responds]**
4. **Map trigger:** Has the moat been breached (durable advantage established), or is it being tested?
> **[WAIT — do not advance until user responds]**
5. **Close:** You'll know whether this is a standard performance problem or a structural spiral requiring intervention at a specific step within a specific time window.
> **[WAIT — do not advance until user responds]**

## The Process
**Step 1 — Audit moat dimensions:** Name 3–5 advantages (network effects, switching costs, data, brand, distribution, patents). Rate each: strength (strong/moderate/weak) + trend (stable/eroding/rapidly eroding).

**Step 2 — Identify breach conditions:** For each moat, name the specific competitor action or tech shift that would establish a durable advantage over it.

**Step 3 — Check early-warning signals:** Multi-quarter share decline? Rising CAC? Rising churn? Any confirmed = spiral may have started.

**Step 4 — Calculate the cascade:** breach → share loss → revenue decline → R&D cut → product lag → further breach. Estimate timeline per step.

**Step 5 — Identify intervention window:** Work backwards from "irreversibility" (typically when R&D falls below product-parity threshold). Design intervention 2–3 steps earlier.

**Step 6 — Design intervention:** Step 1–2: competitive response. Step 3–4: strategic repositioning. Step 5–6: platform shift.

**Gate:** Confirm structural (not cyclical) decline before proceeding. **Stop-rule:** Cannot name a specific breach scenario for each moat → audit incomplete, return to Step 2.

### Output: Death Spiral Risk Map
```
MOAT AUDIT: [Dimension] — Strength / Trend / Breach condition / Likelihood
EARLY WARNINGS: Share | CAC | Churn | R&D% (all trailing 4–6Q)
Verdict: [NOT active / possible / confirmed at step __]
CASCADE MAP: Steps 1–6 with magnitude + timeline estimates
INTERVENTION WINDOW: Last viable step __ | Current position __ | Time remaining __
INTERVENTION: Type | Actions | Resources | Success metrics
```
*→ Method in Action: [Kodak's Death Spiral (1994–2012)](examples/kodaks-death-spiral-1994-2012.md)*

## Death Spiral Packs
**Startup Pack:** Apply pre-emptively — identify which early moats could be breached and design moat diversity before the first breach. For founders + early-stage investors.

**Incumbent Pack:** High current revenue masks early moat erosion. Audit moat health independently of current financials. For strategy teams + board directors.

**Investor Pack:** Death spiral risk is underweighted in equity models projecting from trailing revenue — especially for single-dimension moats with high R&D dependency.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Applying It Well
1. Always test for cyclicality first — structural vs. cyclical decline require different interventions.
2. Audit all moat dimensions; breaches come from unexpected directions.
3. R&D% of revenue is the leading indicator; revenue decline is the lagging indicator.
4. Calculate the intervention window before designing — step 1–2 responses are counterproductive at step 4–5.
5. Name the specific breacher: "feature parity at 60% of our price within 18 months," not "technology disruption."
6. Cash reserves extend the window; they do not reverse the feedback loop.

## Common Rationalizations
**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We're experiencing temporary market softness." | If decline creates conditions for further decline, "temporary" is a fatal misdiagnosis. Test: is the feedback loop active? |
| [D] "Our brand is too strong for this to be a serious threat." | Brand trust is a lagging function of product quality — not protective after 2–3 years of product lag. |
| [D] "We're investing in transformation — we'll catch up." | Test R&D % of revenue trend, not announcement. Investment funded by cuts elsewhere is not net new. |
| [D] "We have to focus on profitability — R&D can wait." | R&D cuts are the mechanism that makes product lag worse, which makes revenue shortfall worse. Self-amplifying. |
| [D] "We'll acquire the best competitor once we've stabilized." | Target's value is highest before the spiral; by "stabilized" the price may be unaffordable. |
| [D] "This is a pricing issue — we'll fix it with a promotion." | Promotions address demand curve position, not a moat. Accelerates revenue decline without fixing the product gap. |
| [D] "We'll focus on our core and let this new segment develop." | Cedes the emerging segment; entrant builds network effects they will use to re-enter your core. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags
1. R&D% of revenue declining for 2+ consecutive years — structural signature of self-amplifying phase.
2. Management attributing multi-quarter decline to cyclical factors without a defined reversal mechanism.
3. Competitor gaining distribution in primary channels while achieving product parity simultaneously.
4. Core customer retention declining while new customer acquisition is still positive.
5. Top engineering talent attriting to competitors — revealed-preference signal about product health.
6. Ecosystem partners building integrations with competitors "just in case."

## Verification
- [ ] All moat dimensions named with breach condition + likelihood
- [ ] Decline tested structural vs. cyclical (historical + industry-wide comparison)
- [ ] R&D% of revenue trended over trailing 4–6 quarters
- [ ] Cascade map: all 6 steps with timelines
- [ ] Intervention window: "last viable step" explicitly named
- [ ] Intervention type matched to current spiral step
- [ ] Stop-rule: each moat has a named specific breach scenario
- [ ] False-positive check: cyclical/execution explanations explicitly ruled out

---
*Part of **deciqAI Knowledge Skills** — 225 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/death-spiral** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
