---
name: latticework
description: "Activate when: user says 'I don't know which framework to use', 'our analysis keeps missing something', 'we need a second opinion on our model', 'how do we stress-test this decision from multiple angles', 'one framework isn't enough here', or a decision keeps surfacing objections from different stakeholders that don't overlap.
  Do NOT activate when: the problem is fully contained in one discipline with no cross-domain interactions (pure legal text, pure engineering spec); time is too short for multi-model deliberation (crisis triage)."
---

# Latticework

## Overview

**Latticework** is the practice of cross-wiring mental models from multiple disciplines on the same situation. Power comes from *inter-connection*: independent lenses converging = high-confidence signal; lenses diverging = unknown to investigate. When multiple forces align simultaneously they amplify — the **lollapalooza effect** (Munger, 1994). Composes with [`first-principles`](../first-principles/SKILL.md), [`second-order-thinking`](../second-order-thinking/SKILL.md), [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md), and [`map-is-not-the-territory`](../map-is-not-the-territory/SKILL.md).

## When to Use

- Stakeholders keep raising non-overlapping objections — each is right from their model
- Post-mortem shows failure was "outside the model we used"
- "Our analysis is solid" — but only one framework was applied
- Situation looks like a classic X but has anomalous features X cannot explain
- Designing a strategy/product where market, psychology, operations, and incentives all interact
- Judging an AI-boom / AI-adoption / AI-hype bet where "is it a bubble?" and "is it real?" are being argued through one lens each

**Not when:** problem is contained in one discipline; crisis triage (no time); decision too small for multi-model overhead.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: facts don't become knowledge until they hang on a latticework of theory (Munger's rule #1).
2. Check fit: has one model already failed or felt incomplete? If yes, proceed.
3. Elicit: what models applied so far? What disciplines are missing?

> **[WAIT — do not advance until user responds]**

4. Run The Process one step at a time with their input.

> **[WAIT — do not advance until user responds]**

5. Close: name the convergence map, blind spots, and any lollapalooza effects found.

> **[WAIT — do not advance until user responds]**

## The Process + Output Template

```
# Latticework Analysis: <situation>

## 1 — Phenomenon
  Core question:
  Prior single-model framing + its known blind spot:

## 2 — Lenses (3–5, genuinely independent disciplines)
| # | Discipline | Key Prediction | Force (+/-/0) |
|---|-----------|---------------|--------------|
| 1 | Economics | | |
| 2 | Psychology | | |
| 3 | Systems | | |

## 3 — Convergence Map
  ≥2 lenses agree (higher-confidence):
  Lenses disagree (live unknown — investigate):
  Lollapalooza: multiplicatively aligned forces?

## 4 — Blind Spots
  What no lens covers:

## 5 — Calibrated Conclusion
  Recommendation + Confidence:
  Key residual uncertainty:
  Information that would most change the picture:
```

*→ Method in Action: [Charlie Munger 1994 USC Business School Address](examples/charlie-munger-1994-usc-business-school-address.md)*

*→ 2026 lens: [Reasoning About the AI Boom (2024–2026)](examples/reasoning-about-the-ai-boom-2024-2026.md) — economics × psychology × systems × game theory on one situation*

## Pack: Latticework Across Domains
| Domain | Typical single lens | Key missing lens |
|---|---|---|
| Startup PMF | Customer interviews | Systems (adoption loops) + History |
| Pricing | Demand curve | Game theory (competitive response) |
| M&A | Financial synergies | Psychology (culture) + History (base rates) |

## Applying It Well

- Independence matters: 3 re-labeled versions of the same model is not a latticework
- Divergence = information; stop adding lenses when marginal new predictions cease (3–5)

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We already did a full analysis" | One framework applied thoroughly is a single-lens deep dive — not a latticework. |
| [D] "Adding more models adds confusion" | Confusion from diverging models is *information* — it shows where understanding is incomplete. |
| [D] "We consulted multiple advisors" | If all advisors share the same disciplinary lens, that is triangulation within one model. |
| [D] "The model has worked before" | A model that predicted correctly in past contexts may be in a regime where its assumptions no longer hold. |
| [D] "Convergence is confirmation bias with extra steps" | Confirmation bias seeks evidence for a pre-held view. Latticework compares independent predictions — divergence check is the anti-bias mechanism. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Only one discipline's vocabulary used throughout
- Stakeholder objections dismissed without checking if they represent another model's prediction
- Decision called "rigorous" because the single model was applied thoroughly
- Diverging data forced into the primary model instead of triggering a model-check
- The analysis cannot name its own blind spots

## Verification

- [ ] ≥3 genuinely independent disciplinary lenses applied
- [ ] Each lens produced an explicit, falsifiable prediction (not just "we considered X")
- [ ] Convergence zones marked higher-confidence; divergence zones named as live unknowns
- [ ] At least one blind spot named (phenomenon no lens covers)
- [ ] Lollapalooza check: any convergent forces multiplicatively aligned?

---
*Part of **deciqAI Knowledge Skills** — 223 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/latticework** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
