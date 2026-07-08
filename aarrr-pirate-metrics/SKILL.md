---
name: aarrr-pirate-metrics
description: "Activate when: user says 'our growth is stalling and we don't know why,' 'product and marketing are arguing about whose fault it is,' 'where is our funnel breaking,' 'pirate metrics,' or 'acquisition vs activation vs retention.' Also activate for: designing end-to-end metrics for a new product, building a shared instrumentation framework across teams.
  Do NOT activate when: the product has no users yet (use lean-startup instead), or the bottleneck is already obvious and obvious to fix."
---

# AARRR (Pirate Metrics)

## Overview

A startup's growth is a **sequential funnel** — each stage gates the next. Great Acquisition is worthless if Activation is broken; great Activation is worthless if Retention is zero. Optimizing the wrong stage produces work that looks like progress while the bottleneck stays.

The **AARRR framework** (Dave McClure, *Startup Metrics for Pirates*, 2007) names five stages: Acquisition (do they show up?), Activation (good first experience?), Retention (do they come back?), Referral (do they tell others?), Revenue (do they pay?). The bottleneck stage governs total growth — improving any other stage produces no system-level gain (Goldratt, *The Goal*, 1984).

**Compose with:** [first-principles](../first-principles/SKILL.md) to identify your specific Activation event; [pmf-crossing-the-chasm](../pmf-crossing-the-chasm/SKILL.md) to recognize when Retention will always be the bottleneck pre-PMF; [probabilistic-thinking](../probabilistic-thinking/SKILL.md) to set base rates per stage.

## When to Use

- Growth is **stalling** and the cause is not obvious — multiple teams have plausible explanations
- Product, marketing, and sales are **arguing about whose problem it is**
- You need a **shared instrumentation framework** across teams
- Designing **end-to-end metrics for a new product**
- Someone says: *"AARRR," "pirate metrics," "growth funnel," "where is our funnel breaking?"*

**When NOT to use:** No users yet → use [lean-startup](../lean-startup/SKILL.md). Signups still in the tens — AARRR rates need volume. Bottleneck already obvious → fix that first, then return.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has funnel data and wants the bottleneck named → run The Process directly.
- **Coach mode:** vague situation or unfamiliarity → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line what-it-is.** AARRR is a five-stage funnel (Acquisition / Activation / Retention / Referral / Revenue) — the point is to find which stage is broken so you don't waste effort on the wrong one.
2. **Check fit.** No users / tiny base → redirect. Bottleneck already obvious → fix it first.
3. **Elicit their real case.** Force the user to define their *specific* Activation event — not "signed up" but e.g. *"completed onboarding and used the core feature once within day 1."* > **[WAIT — do not advance until user responds]**
4. **One stage at a time.** Walk Acquisition → Activation → Retention → Referral → Revenue. Compute conversion rate stage-to-stage if possible. > **[WAIT — do not advance until user responds]**
5. **Close by naming the bottleneck and the next experiment.** They leave with one stage identified and one specific experiment. > **[WAIT — do not advance until user responds]**

## The Process

Run the **Funnel Audit**: define stages, measure conversions, identify bottleneck.

1. **Define each stage for this specific product.** Generic definitions hide the bottleneck. Activation = the *aha moment*, not signup. Name a measurable event per stage.
2. **Measure conversion at each stage.** Acquisition→Activation %, Activation→Retention %, Retention→Referral %, Activation/Retention→Revenue %.
3. **Compare against domain benchmarks.** A stage below benchmark is a bottleneck candidate (B2B SaaS day-30 retention 70%+; consumer freemium paid conversion 1–5% typical, 5–10% strong).
4. **Identify the load-bearing bottleneck.** Worst conversion *relative to its benchmark* — fixing it produces the largest system-level gain.
5. **Pre-commit one experiment.** Name the specific change, the metric, and the pre-committed threshold (per [lean-startup](../lean-startup/SKILL.md)).
6. **Re-measure and re-identify.** After the experiment, the bottleneck moves. Repeat — the audit is iterative.

### Output: Funnel Audit

```
# AARRR Funnel Audit: <product>
Stage definitions: Acquisition <event> | Activation <aha moment> | Retention <window+event> | Referral <event> | Revenue <event>
Conversions: [Stage | Users | Conv.% from prior | vs. benchmark ↑↓]
Bottleneck: <stage with worst conversion vs. domain benchmark>
Experiment: Change <intervention> · Metric <conversion rate> · Threshold <value> · Window <days>
```

*→ Method in Action: [Dropbox's Referral Program (2009)](examples/dropbox-referral-program-2009.md) · [Facebook's "7 Friends in 10 Days" (2007–2009)](examples/facebook-7-friends-in-10-days-2008.md)*

## Funnel Packs

Stage definitions and benchmarks are domain-specific. **Consumer freemium:** Activation = first core value; paid conversion 1–5% typical, 5–10% strong. **B2B SaaS:** Activation = first non-trivial team use week 1; gross retention 90%+, net 100%+ mid-market. **Marketplaces:** Activation = first transaction; bottleneck = liquidity-thin side. **E-commerce:** Activation = first order; Retention = second order within 90 days.

Contribution: add a pack for your domain — one file with (a) stage definitions, (b) benchmarks, (c) typical bottleneck pattern, (d) canonical experiments.

## Applying It Well

- **Activation is the most often-sloppily-defined stage.** "Signed up" is not Activation. Specify the aha moment event.
- **The bottleneck is relative to benchmark** — not the stage with the lowest absolute number.
- **Fixing the bottleneck moves the bottleneck.** Re-identify after each experiment.
- **Each team optimizes the stage they own** — dangerous if the bottleneck is elsewhere. The audit forces cross-team prioritization.
- **Domain benchmarks matter more than absolute numbers.** 3% paid conversion = great freemium, terrible enterprise SaaS.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Optimizing Acquisition while Activation is broken** | Most common failure. More users into a broken funnel = more wasted CAC. Fix the bottleneck first. |
| [D] **"Activation" = "signed up"** | Signup is end of Acquisition. Activation = first time user experiences the value. Sloppy definition hides the real funnel. |
| [D] **Treating low absolute conversion as the bottleneck** | Acquisition always has the lowest absolute count. What matters: each stage *relative to its domain benchmark*. |
| [D] **Adding paid ads when Retention is weak** | A leaky bucket doesn't fill faster when bigger. Fix Retention before scaling Acquisition. |
| [D] **One-shot audit, never re-run** | The bottleneck moves once fixed. Running the audit once and never again misses the next bottleneck. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Activation is defined as "signed up"
- Dashboards show absolute counts but not stage-to-stage conversion rates
- No domain benchmarks referenced
- Resource allocation matches which stage is easy to instrument, not which is the bottleneck
- The funnel audit has been run once and never repeated
- Teams don't share a bottleneck consensus
- Acquisition spend scaled while Retention is below benchmark

## Verification

- [ ] Each stage has a product-specific measurable definition (Activation = aha moment, not signup)
- [ ] Conversion rates between stages measured, not just absolute counts
- [ ] Each stage compared against a domain benchmark
- [ ] Load-bearing bottleneck named (worst conversion relative to benchmark)
- [ ] Experiment pre-committed with metric + threshold + time window
- [ ] Re-audit scheduled (bottleneck will move)
- [ ] All teams agree on the bottleneck

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/aarrr-pirate-metrics?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=aarrr-pirate-metrics** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
