---
name: lean-startup
description: "Activate when: user says 'lean startup', 'build-measure-learn', 'MVP', 'validated learning', 'pivot or persevere', 'should we just build it?', 'we need to test this idea before building', or 'how do we know if anyone wants this?'; team is about to build something significant before testing demand; a pivot decision is on the table after early data.
  Do NOT activate when: operating a known business model in known conditions (use execution frameworks instead); decision is below business-model level (button color, which CRM)."
---

# Lean Startup

## Overview

A startup is a **temporary organization searching for a repeatable, scalable business model under extreme uncertainty** (Steve Blank). Most early-stage failures are from building something no one wanted because the demand assumption was never tested.

**Eric Ries** (2011): name the riskiest assumption, build the smallest test (MVP), measure real behavior, decide to **pivot or persevere** — the **Build–Measure–Learn loop**, run as fast as possible.

**Compose:** [first-principles](../first-principles/SKILL.md) to find what the model truly depends on; [probabilistic-thinking](../probabilistic-thinking/SKILL.md) to calibrate experiments; [inversion](../inversion/SKILL.md) before each Build phase; [business-model-canvas](../business-model-canvas/SKILL.md) to surface the riskiest assumption blocks.

## When to Use

Apply when: high uncertainty + limited capital; a team is about to build before testing demand; a pivot-or-persevere decision is on the table; no clear answer to "what is the load-bearing assumption and how would we know if it's wrong?"

**When NOT to use:** known business model in known conditions (execution, not search); decision is not business-model-level; cannot ethically run a test with real customers; using "lean" as a schedule excuse to ship buggy software.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete hypothesis → run The Process directly.
- **Coach mode:** no concrete hypothesis or signals unfamiliarity → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line what-it-is.** Most startups fail by building before knowing if anyone wants it; lean startup names the riskiest assumption, tests it with the smallest MVP, measures real behavior, and decides pivot or persevere — fast.
2. **Check fit.** Match against When to Use / When NOT to use; if low uncertainty + known model, redirect.
3. **Elicit their real hypothesis.** Force them to name one load-bearing assumption — specific segment, specific value, specific willingness-to-pay.
> **[WAIT — do not advance until user responds]**
4. **Walk the loop step by step.** Name assumption → design MVP → define metric → set threshold. Pause at each.
> **[WAIT — do not advance until user responds]**
5. **Close by naming the next-week experiment.** One assumption, one MVP, one threshold, one date — not a strategy doc.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Build–Measure–Learn cycle**. Identify, test, decide.

1. **State the load-bearing assumption.** Specific segment, specific value, specific willingness-to-pay, specific timeframe. Not "users want X."
2. **Pre-commit to a pivot-or-persevere threshold.** Write the metric value *before* running the experiment. You will rationalize if you have not pre-committed.
3. **Design the smallest MVP that tests the assumption.** Often not a product — a landing page, concierge/"Wizard of Oz" version, or 3-minute video. Purpose is *learning*, not selling.
4. **Build the MVP fast.** Time-box. If an early-stage test takes more than 4–6 weeks, cut.
5. **Measure real customer behavior, not stated intent.** Actionable metrics (conversion, retention, willingness-to-pay) test the assumption. Vanity metrics (signups, likes) do not.
6. **Compare result to the pre-committed threshold.** Don't move the goalposts.
7. **Decide pivot or persevere — explicitly.** Persevere = assumption held; pivot = assumption failed in a specific way, change the load-bearing block and re-test.
8. **Document and iterate.** Write: assumption, MVP, threshold, result, decision, rationale. Each loop must produce a durable carry-forward learning.

### Output: Experiment Card

```
Assumption: "<segment> will <action> at <rate> for <value> by <date>"
Threshold: Persevere if <metric ≥ X> | Pivot if <metric < X>
MVP: <what / why smallest / time-box ≤ 4–6 wk>
Metric: <actionable> | Vanity to ignore: <list>
Result: <actual vs. threshold>
Decision: [ ] Persevere  [ ] Pivot (type: ___)  [ ] Re-test
Validated learning: <one sentence carry-forward>
```

*→ Method in Action: [Dropbox's Video MVP (2007)](examples/dropboxs-video-mvp-2007.md) · [Votizen's Pivot Sequence (2010–2011)](examples/votizens-pivot-sequence-2010-2011.md)*
## Experiment Packs

| Domain | Load-bearing assumption | MVP type | Common failure |
|---|---|---|---|
| Consumer apps | install + day-7 retention | concierge, video, single-feature build | testing acquisition, ignoring retention |
| B2B SaaS | willingness-to-pay vs. specific budget owner | pre-order page or 3–5 paid pilots | talking to users (love it), not buyers (hold budget) |
| Two-sided marketplaces | liquidity on the harder side (usually supply) | manually-matched concierge, single ZIP | launching both sides at once |
| Hardware | people willing to pay (not just click) | video demo + Kickstarter or pre-order | conflating click-throughs with payment intent |

## Applying It Well

- MVPs are for learning, not revenue — the deliverable is evidence, not a launch.
- Pre-commit to the threshold or you will rationalize whatever you get.
- In B2B, talk to buyers (hold budget), not just users (love the product).
- Vanity metrics (signups, likes) ≠ actionable metrics (conversion, retention, willingness-to-pay).
- The MVP is disposable — a test instrument, not v0 of your product.

*→ Primary sources: [references/sources.md](references/sources.md)*
## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **"We're lean" while shipping a six-month build with no validated demand** | Lean Startup is a loop, not a label. If you haven't tested the load-bearing demand assumption before building, you are doing waterfall. |
| [D] **MVP confused with v1 of the product** | The MVP is a test instrument, designed to be disposable. Polishing it as v1 inflates scope and breaks the loop. |
| [D] **No pre-committed pivot/persevere threshold** | Without it, you will explain any result. The pre-commitment IS the discipline. |
| [D] **Counting vanity metrics** (signups, traffic, likes) | These move with marketing spend, not product-market fit. Actionable metrics test the assumption. |
| [D] **Talking only to users, not buyers** (especially in B2B) | User love is necessary but not sufficient. The buyer's willingness-to-pay is the load-bearing test. |
| [D] **"The customer said they'd buy"** | Stated intent is famously unreliable. Measure behavior (a credit card swipe, retention to day 7), not intent. |
| [D] **Pivoting on noise** | A single bad week is not a signal to pivot. Pre-commit the threshold and time-window; pivot only when both fire. |
| [D] **Pivoting "because we got bored"** | A pivot is a response to invalidated assumptions, not to founder restlessness. |
| [D] **Using "lean" as schedule cover** | Lean is not "ship buggy fast." It is "test the demand-side assumption before building the supply-side capability." |
| [D] **No documented validated learning** | If each loop doesn't produce a written carry-forward insight, you are running random experiments. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |
## Red Flags

- The team is building for months with no MVP yet shipped
- "MVP" is a six-month build with full polish
- Vanity metrics dominate the dashboard; conversion/retention/willingness-to-pay are absent or untracked
- Customer interviews reported as "they love it" with no behavioral data
- Pivot decisions made on a single week's noise, or after founders simply got bored
- No pre-committed pivot/persevere threshold exists for any experiment
- "Lean" is being used to justify low-quality shipping rather than test-before-build
## Verification

- [ ] The load-bearing assumption is named in specific segment/value/willingness-to-pay/timeframe form
- [ ] The pivot-or-persevere threshold is pre-committed in writing, before the experiment runs
- [ ] The MVP is the smallest test of the assumption (time-boxed ≤ 4–6 weeks early-stage)
- [ ] An *actionable* metric (not vanity) is pre-specified for evaluation
- [ ] Result is compared to the pre-committed threshold — without moving goalposts
- [ ] Pivot vs. persevere decision is made explicitly, with type if pivoting
- [ ] Validated learning is documented in one sentence carry-forward
---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/lean-startup?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=lean-startup** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
