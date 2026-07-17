---
name: anchoring
description: "Activate when: user says 'what's a fair price / starting number / ballpark'; counterparty just opened with a number; user is about to negotiate salary, valuation, or deal terms; user is making a forecast and a number has already been floated; user asks about 'first offer', 'framing effect', or 'being anchored'.
  Do NOT activate when: the number in question is a verifiable data point (audited financials, confirmed comparable) and is genuinely informative; or the decision is so trivial that the economic impact of anchoring is negligible. More: deciqai.com/s/anchoring"
---

# Anchoring

## Overview

When people estimate an unknown quantity they start from a reference point — an **anchor** — and adjust. The adjustment is almost always insufficient, so the final answer stays closer to the anchor than it should. This pattern holds even when the anchor is explicitly random and subjects are told to ignore it (Tversky & Kahneman 1974). It survives expertise, explicit warnings, and financial incentives for accuracy.

Strategically: almost every consequential negotiation, valuation, or forecast begins with an anchor. The first number said or written — asking price, salary band, prior-round valuation, revenue projection — anchors everything that follows.

Composes with: [`pricing-strategy`](../pricing-strategy/SKILL.md) · [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) · [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md) · [`signaling-games`](../signaling-games/SKILL.md)

## When to Use

Apply when:
- About to negotiate a price, salary, valuation, contract term, or settlement
- Estimating an uncertain quantity after a number has already been mentioned
- A counterparty has opened and your reasoning is gravitating toward their number
- Resetting expectations after an anchor has already been set
- Sizing an AI startup valuation, raise, or AI-capex/adoption estimate where a headline round or a benchmark like Nvidia's market cap has already been floated as "the market"

**When NOT to use:**
- The number is genuinely informative (verifiable comparable, audited cost basis) — data, not an anchor
- Decision is trivial; you are past the negotiating phase; or anchor was set by you intentionally

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: when you estimate or negotiate a number, the first number you hear pulls your answer toward it — even when you know it's random or wrong.
2. Check fit against When to Use / When NOT to use. If the number is genuine data, say so.
3. Elicit their real situation — a number that's been mentioned, an upcoming negotiation, a figure that's been floated. > **[WAIT — do not advance until user responds]**
4. Walk through The Process one step at a time with their input. > **[WAIT — do not advance until user responds]**
5. Close by naming the one concrete move that fits their situation (open with X / counter with Y / reset to Z). > **[WAIT — do not advance until user responds]**

## The Process

Run the **Anchoring Analysis**. Detect anchors, judge their informational content, decide deliberately.

1. **Identify the anchor.** Name the specific number explicitly — it often arrives as casual mention, "data," or expectation, not as a labeled offer.
2. **Classify informational content.** Genuinely informative → use as evidence. Partial (real signal + proposer's interest) → discount. Pure anchor → treat as zero information; bias still operates, apply structural defense.
3. **Run the anchor-free counterfactual.** What number would you have produced without hearing the anchor? Write it down first.
4. **Consider an opposite-side anchor.** Deliberately generate a number in the opposite direction and articulate the reasons — not to use as a counter, but to break the asymmetry.
5. **If proposer:** open bold but defensible. Bold openers consistently outperform soft ones; absurd anchors lose power and damage the relationship.
6. **If respondent:** name it, reset with your own independently-generated number, or work with it knowingly — discounting your natural agreement point.
7. **Audit hidden anchors in forecasts.** Last quarter, board expectations, prior-year baselines are all anchors. Identify which is doing the work.
8. **Stop-rule:** if the analysis doesn't change the decision, you may have rationalized. Re-run the anchor-free counterfactual.

### Output: the Anchoring Analysis

```
Anchor: [number] | Source: [who/how] | Status: [offer/comparable/casual/expectation]
Informational content: [genuinely informative / partial / pure anchor] — Evidence: […] Counter-evidence: […]
Anchor-free counterfactual: [my number without the anchor] | Gap vs. current "natural" answer: […]
Opposite-anchor test: [what would justify the other extreme] → range implication: […]
Decision: [proposer: bold-but-defensible opening] / [respondent: name/reset/work-with + specific number]
Risk anchor still operating: […] (how I'll know if I've been pulled too far)
```

*→ Method in Action: [Tversky & Kahneman's Wheel of Fortune, 1974](examples/tversky-kahneman-wheel-of-fortune-1974.md) · [Judges Playing Dice with Criminal Sentences, 2006](examples/englich-judges-dice-criminal-sentences-2006.md)*
*→ 2026 lens: [AI Fundraising and Valuation Anchors (2023–2026)](examples/ai-fundraising-valuations-anchoring-2023-2026.md) — headline AI rounds and Nvidia's market cap anchoring the next valuation*

## Pack: Anchoring in Practice

- **Pricing/sales:** list premium tier first; generate willingness-to-pay before seeing the seller's price.
- **Salary:** candidates who name first do better; open bold from market data. Employers: the first number in the offer email anchors negotiation.
- **Real estate:** buyers pull sold (not listed) comparables before viewing the listing.
- **Startup funding:** bold-but-defensible asks correlate with higher closes; investors build their valuation model before reading the pitch deck.
- **Forecasting:** zero-based forecasting and independent pre-aggregation estimates defend against last-year anchoring.
- **Legal:** high opening demands → higher settlements; defendants counter-anchor with evidence-based numbers.

## Applying It Well

- Generate your anchor-free number **before** any external anchor is introduced — structural defense beats procedural.
- Bold-and-flexible beats soft-and-firm: open aggressively, concede during negotiation.
- Recognition is the start of defense, not the conclusion; pair it with counterfactual generation.
- "Consider the opposite" (Mussweiler et al. 2000) reduces but does not eliminate the bias.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I'm an expert — I'm not anchored" | Northcraft & Neale 1987 (real-estate agents) and Englich et al. 2006 (judges) show expertise is not protective. |
| [D] "I know the anchor is random, so it won't affect me" | The 1974 wheel told subjects it was random. Effect operated anyway. Knowing is the start of defense, not the conclusion. |
| [D] "I'll consider the anchor and then make my own judgment" | Every anchored subject believed this. Defense is generate-your-number-first, then look at the anchor. |
| [D] "Going first shows my cards — I'll let them open" | Galinsky & Mussweiler 2001: bold first offers produce better outcomes. Letting them open loses money on average. |
| [D] "Our forecast is bottom-up, not anchored" | If it started from last year's number or referenced the board's expectation, it is anchored. |
| [D] Setting an anchor outside the bounds of plausibility | Absurd anchors lose power and damage the negotiation. Bold = maximum within the plausibility range. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- A casual number ("ballpark," "let's just say X") is now the implicit baseline of the conversation
- Your estimate was generated after hearing the anchor, with no anchor-free counterfactual written down
- You are deferring on opening offers to avoid "showing your hand" — this intuition is systematically wrong
- Forecast = "last year ± adjustment" — adjustment is almost always insufficient
- Decision-maker says "the number isn't supposed to influence me, but…" — that "but" is the anchor

## Verification

- [ ] Anchor explicitly identified and named
- [ ] Informational content classified (genuinely informative / partial / pure anchor)
- [ ] Anchor-free counterfactual generated before the anchor settles in
- [ ] Proposer: opening anchor bold but defensible within plausibility range
- [ ] Respondent: chose name / reset / work-with and named the specific number
- [ ] Decision meaningfully different from pre-analysis — if not, may have rationalized rather than de-anchored
- [ ] In forecasting: hidden anchors (last period, board expectation) identified, not just explicit ones

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/anchoring** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/anchoring.json*
