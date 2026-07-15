---
name: mvp
description: "Activate when: someone says 'MVP', 'minimum viable product', 'smoke test', 'concierge MVP', or 'Wizard of Oz'; a team is scoping a build and hasn't named the assumption they're testing; engineers are about to build for months on an unvalidated idea; someone asks 'what's the smallest thing we can ship?'.
  Do NOT activate when: the product already has validated PMF and the question is scaling or polishing; the deliverable is a contractual obligation already sold."
---

# Minimum Viable Product

## Overview

An MVP is **not a small version of your product** — it is a **test instrument**: the smallest artifact that produces trustworthy evidence about one specific demand-side assumption, with the least possible investment. Success criterion is **learning per dollar**, not features per dollar.

Coined by Frank Robinson (SyncDev, 2001); operationalized by Eric Ries (*The Lean Startup*, 2011, p. 77) — sometimes the artifact has no software at all. Compose: [lean-startup](../lean-startup/SKILL.md) defines Build-Measure-Learn — this skill covers the Build phase. Use [business-model-canvas](../business-model-canvas/SKILL.md) to identify the assumption; [inversion](../inversion/SKILL.md) to stress-test it.

## When to Use

- Scoping a build and need to decide what minimum produces trustworthy evidence
- "MVP" is being used to mean "small version of the real product" (this skill corrects that)
- Engineers are building for months on an unvalidated assumption
- Choosing between concierge / Wizard-of-Oz / smoke test / video / single-feature / paid pilot
- AI made building cheap and you're about to "just build the whole thing" — vibe-coded a prototype in a weekend but can't name the assumption it tests

**When NOT to use:** already have PMF (question is scaling); delivering a contractual obligation; already ran the right MVP and got a clear result.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** specific assumption → pick type, set metric, scope the build.
- **Coach mode:** no assumption or signals unfamiliarity → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: an MVP is the smallest test instrument for one specific assumption, not a small product.
2. Check fit against When to Use / When NOT to use. If scaling a validated product, redirect.
3. Elicit their real assumption. Without one, "MVP" is just "small version."
> **[WAIT — do not advance until user responds]**
4. Walk through MVP type selection, metric specification, time-box — one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close by naming the time-box (1–4 weeks), the pre-committed metric, and the disposability commitment.
> **[WAIT — do not advance until user responds]**

## The Process

1. **Name the single assumption being tested.** One load-bearing claim with segment, behavior, rate, and value.
2. **Pick the MVP type that fits the assumption.**
   - **Smoke test** (landing + email): tests awareness-to-interest. Tests nothing about retention or pay.
   - **Landing + pre-order** (credit card captured): tests willingness-to-pay at a price point.
   - **Video demo** (no working product): tests demand at scale. Famous case: Dropbox 2007.
   - **Concierge** (manual delivery): tests whether service has perceived value — no product built.
   - **Wizard-of-Oz** (automated front, human back-end): tests willingness-to-use before automation investment.
   - **Single-feature** (one feature polished, rest absent): tests whether one feature drives the use case.
   - **Paid pilot** (B2B, 3–5 design partners paying real money): tests enterprise WTP and integration complexity.
3. **Specify the actionable metric in advance.** Measurable behavior: conversion %, day-N retention, paid signup count.
4. **Time-box aggressively.** 1–4 weeks. Exceeding means scope is wrong — cut scope, never extend time.
5. **Strip every feature not load-bearing.** Auth, accounts, polish — all out unless the test requires it.
6. **Build, measure, throw away.** If assumption holds, rebuild for production from scratch.
7. **Document validated learning** in one sentence. Artifact is disposable; learning is durable.

### Output: MVP Design Card (copy-paste)

| Field | Fill in |
|---|---|
| Single assumption | "<segment> will <behavior> at <rate> for <value>" |
| MVP type | smoke / pre-order / video / concierge / WoZ / single-feature / paid pilot |
| Why this type fits | 1–2 sentences on evidence produced vs. alternatives |
| Actionable metric + threshold | e.g., day-7 retention ≥ 40% within 14 days |
| Build time-box | e.g., 2 weeks — cut scope if exceeded, never extend |
| Features IN (load-bearing only) | list + reason each is required for the test |
| Features OUT | list + reason each is deferred |
| Disposability commitment | ☐ MVP code thrown away; production rebuilt from validated learning |
| Validated learning (post-test) | one sentence |

*→ Method in Action: [Zappos's Concierge MVP (1999)](examples/zappos-concierge-mvp-1999.md) · [Airbnb's Air-Mattress MVP (2007)](examples/airbnbs-air-mattress-mvp-2007.md)*
*→ 2026 lens: [The AI-Era MVP — when building got cheap and validation didn't (2023–2026)](examples/ai-era-mvp-when-building-is-cheap-2023-2026.md) — the bottleneck moved from engineering to evidence.*

## MVP Type Packs

| Domain | First-choice MVP type | Why it fits the assumption | Common failure |
|---|---|---|---|
| Consumer apps | smoke test, then single-feature build | smoke test screens awareness-to-interest cheaply; single-feature tests whether one feature drives day-N retention; concierge rarely reaches consumer scale | polish creep turns the single-feature build into v1 before the retention data is in |
| B2B SaaS | paid pilot with 3–5 design partners | enterprise WTP and integration complexity only surface when real budget moves; a smoke test can't reach the budget owner | free pilots treated as validated demand — everyone says yes to free |
| Marketplaces | concierge in one ZIP code or one event | matching value is testable with the founders as the manual back-end before any platform exists (Airbnb 2007) | building both sides of the platform before proving anyone wants the match |
| Hardware | video demo + pre-order (credit card captured) | tests demand and price point with zero tooling cost; the pre-order forces a payment decision, not a click | conflating pre-order revenue with retention or repeat-purchase signal |

*Contribute a pack for your domain — see the template at the repo root.*

## Applying It Well

- Test instrument, not small product. If you'd be embarrassed to show it outside the test cohort, you built it right.
- Pick the cheapest type that tests the load-bearing assumption; pre-commit the metric before launch.
- Throw the MVP away — code optimized for the experiment is wrong for the product.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **"MVP" = small version of the real product** | MVP is a test instrument. A six-month polished build is not an MVP. |
| [D] **No assumption stated** | No assumption = no learning. "Test the MVP" is just "ship a product." |
| [D] **No pre-committed metric** | Deciding success after seeing data means you've already cheated. |
| [D] **Type chosen without assumption-fit reasoning** | Wrong type = wrong evidence, regardless of build quality. |
| [D] **Time-box ignored** | An MVP taking six months is product development with optimistic naming. Cut scope. |
| [D] **Polish creep** | "One more week of polish" turns MVP into v1, delaying learning by months. |
| [D] **Keeping MVP code as production basis** | MVP code is optimized for the test, not the product — inheriting it inherits all shortcuts. |
| [D] **Free pilots treated as validated B2B demand** | Free pilots produce false positives. Paid pilots test WTP. |
| [D] **Traffic / signups counted as validation** | Vanity metrics. Conversion, retention, and WTP test the assumption. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags / Verification

**Red flags:** MVP described as "smaller version of product" · time-box exceeds 4–6 weeks · no testable assumption named · no pre-committed metric · type chosen by engineering preference · plan to iterate MVP into final product.

- [ ] Single specific testable assumption named
- [ ] MVP type is one of the 7 canonical types; fit to assumption explicitly reasoned
- [ ] Actionable metric + threshold pre-committed before launch
- [ ] Build time-boxed (1–4 weeks); scope cut if exceeded — never extend
- [ ] Excluded features listed with reasoning
- [ ] Disposability commitment made — MVP code will not be the production basis
- [ ] Validated learning captured in one sentence post-test

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/mvp** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
