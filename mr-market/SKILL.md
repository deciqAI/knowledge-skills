---
name: mr-market
description: "Activate when: user says 'the market is telling us X', 'valuation has dropped/risen so we should act', 'everyone is selling/buying so I should too', or is making an investment/fundraising decision based on a quoted price under emotional pressure.
  Do NOT activate when: the market quote genuinely reflects new economic information about the underlying business (not mood); or the user must transact at quoted price for forced-sale/liquidity reasons."
---

# Mr. Market

## Overview

**Mr. Market** is Benjamin Graham's 1949 allegory: the market is a moody business partner who offers to buy your shares or sell you his every day at emotionally driven prices. His quote reflects his current mood, not intrinsic value. Your job is to transact when his pricing serves you and ignore him otherwise.

Three features: (1) quote ≠ intrinsic value; (2) you are never obligated to respond; (3) panics are highest-opportunity moments for those with cash and independent conviction.

Composes with [`margin-of-safety`](../margin-of-safety/SKILL.md) (price discipline), [`anchoring`](../anchoring/SKILL.md) (quotes as anchors), [`social-proof`](../social-proof/SKILL.md) (consensus = mass Mr. Market), [`loss-aversion-prospect-theory`](../loss-aversion-prospect-theory/SKILL.md) (panic exploits loss aversion).

## When to Use

- Public equity investing decisions during market volatility
- Fundraising valuation negotiations (your Mr. Market = the VC ecosystem)
- Acquisition pricing where comparable transaction markets have moved sharply
- Any decision where a quoted price or implied valuation is pressuring your judgment
- Someone says "the market is telling us," "valuation has dropped/risen," "everyone is doing X"

**Not when:** the quote reflects genuine new business information (not mood); forced sale or liquidity requirement; asset has no underlying value independent of its price (pure speculation).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete market-pricing decision → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: are you treating the market quote as information about value, or as an offer to transact at a price? These require different responses.
2. Check fit: does the quote reflect new business information (discipline less applicable) or emotion/sentiment (discipline central)?
3. Elicit the specific quote and underlying business reality. What's the quote? What has the business actually done? Have they diverged?
> **[WAIT — do not advance until user responds]**
4. One question at a time: what's your independent view of intrinsic value? Is Mr. Market dislocated from it? In which direction? What's the right response?
> **[WAIT — do not advance until user responds]**
5. Close: decision (transact / ignore / wait) + acknowledgment of which way emotional contagion was pulling.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State quote and business reality:** What is the market quoting? What has the underlying business actually done? Have they diverged?

**Step 2 — Form an independent view of intrinsic value:** Based on fundamentals, what is the long-term value? Confidence? Sensitivity? How far is the current quote from your estimate?

**Step 3 — Diagnose Mr. Market's state:** Sober (consistent with fundamentals) / manic (elevated by enthusiasm) / depressed (fear/panic) / disappeared (liquidity crisis, no quote).

**Step 4 — Choose the response:** Quote ≈ value → ignore. Quote >> value (manic) → consider selling. Quote << value (depressed) → consider buying. Disappeared → opportunity for cash holders; danger for liquidity-needy.

**Step 5 — Check for emotional contagion:** Am I feeling what Mr. Market is feeling? Is my response driven by his emotion or my analysis? Would I decide the same if I hadn't seen today's quote?

**Step 6 — Document:** Decision + rationale referenced to intrinsic value + calendar-date re-evaluation trigger.

## Output

```markdown
# Mr. Market Decision: <asset>
Quote: | Business reality: | Divergence:
Intrinsic value estimate: | Confidence: | Sensitivity:
Mr. Market's state (sober/manic/depressed/disappeared):
Decision (transact/ignore/wait): | Rationale (vs intrinsic value):
Contagion check — feeling: | analysis says: | gap:
Re-evaluation trigger (date):
```

*→ Method in Action: [Graham 1949, Buffett 1987 + 2008](examples/graham-1949-buffett-1987-2008.md)*

## Pack: Application Patterns

| Domain | Mr. Market looks like | Common error | Disciplined response |
|---|---|---|---|
| Public equities | Daily stock quote | Treating quote as valuation | Form independent view; transact only on dislocations |
| VC fundraising | Comparable round valuations | Market multiple = fair price | Form independent view of business value; raise on it |
| Real estate | Comparable sales | Buying because prices rise | Income-based valuation; transact on dislocation |
| Acquisition | Comp transaction multiples | Paying market multiple regardless | Compute deal-specific value; walk if not accepted |
| Crypto | Daily price | Buying because price rises | No underlying anchor; bound exposure or abstain |

## Applying It Well

- Without an independent intrinsic value, you have nothing to compare the quote to — build it first.
- The discipline is hardest when most-needed: panics are when consensus says "sell" and conviction is rarest.
- Checking quotes hourly produces worse decisions than quarterly — each check is another contagion opening.
*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The market knows something I don't" | Sometimes. Often just emotion. Distinguish new information from mood. |
| [D] "If I don't act now, I'll miss the window" | FOMO is exactly when Mr. Market discipline is most valuable. |
| [D] "Every expert agrees" | Universal consensus is often Mr. Market mood, not analytical depth. |
| [D] "I can't stand watching it drop" | Emotional contagion. Act on your independent valuation, not the feeling. |
| [D] "The market crashed; I should wait to re-enter" | Backwards. Crashes are buying opportunities for those with conviction and cash. |
| [D] "I'm not Buffett; I can't time markets" | Not market-timing — it's price-vs-value discipline. Know what it's worth; transact on dislocations. |
| [D] "I don't have time to form independent valuations" | Then you don't have time to invest. Without it, you are pure Mr. Market dependent. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Checking quotes hourly; your view of value moves in lockstep with the market quote
- Feeling relief or despair based on quotes, not underlying business performance
- Cannot articulate intrinsic value independent of the quote; "everyone is fleeing/piling in" is your justification

## Verification

- [ ] Independent intrinsic value formed (not just the market quote)
- [ ] Mr. Market's state diagnosed (sober / manic / depressed / disappeared)
- [ ] Decision referenced to intrinsic value, not to quote; emotional contagion checked
- [ ] Re-evaluation trigger is calendar-based, not quote-based; reasoning documented

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/mr-market?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=mr-market** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
