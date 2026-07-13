---
name: north-star-metric
description: "Activate when: teams are fighting over which metric to optimize; someone says 'north star metric,' 'NSM,' 'OMTM,' or 'one metric that matters'; a dashboard has 30+ metrics with no clear priority; a leading indicator is needed that predicts revenue before it moves; or someone asks 'what should we optimize?'
  Do NOT activate when: the product has no customers yet (no value to measure — use lean-startup instead); a single team in a mature business needs execution KPIs rather than cross-team alignment."
---

# North Star Metric

## Overview

The **North Star Metric (NSM)** is the single metric that most directly measures *value delivered to customers* and predicts revenue over time. Popularized by Sean Ellis and Amplitude. Revenue is the goal; the NSM is the *leading indicator* that predicts it early enough to act — picking revenue itself produces a lagging dashboard, not a steering wheel.

**Compose:** [aarrr-pirate-metrics](../aarrr-pirate-metrics/SKILL.md) instruments the full funnel; NSM elevates one funnel metric to cross-team primacy. [first-principles](../first-principles/SKILL.md) clarifies what value the product actually delivers. [pmf-crossing-the-chasm](../pmf-crossing-the-chasm/SKILL.md) — the NSM is typically an Activation- or Retention-stage metric.

## When to Use

**Use when:** teams are optimizing conflicting metrics; dashboard has 30+ metrics with no priority; a leading indicator of revenue is needed; someone says "NSM," "OMTM," "what should we optimize," or "we measure too many things"; an AI-native product is chasing sign-ups / prompts / demo plays and needs an activated-value metric that survives high inference/capex costs and AI-adoption churn.

**Do NOT use when:** product has no customers (pre-PMF → use [lean-startup](../lean-startup/SKILL.md)); single-team execution in a mature business; genuinely conflicting strategic objectives (the strategy needs work, not a metric).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: the NSM is the single metric that best captures the value your product delivers to customers — when it grows, revenue grows behind it.
2. Check fit against When to Use / When NOT to use. No customers → redirect to lean-startup. Single mature team → wrong scope.
3. Elicit the product's core value in customer units (time saved, problem solved) — not the product feature.
> **[WAIT — do not advance until user responds]**
4. Walk: value → metric candidate → 3-criteria check → test against company strategy → pick. Pause at each.
> **[WAIT — do not advance until user responds]**
5. Close by naming the chosen NSM + the supporting metrics it should not be confused with. One number on the wall; a list of "useful but not the NSM" metrics.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **NSM Audit**:

1. **Articulate customer value in customer units** — the customer's outcome, not your product's mechanism.
2. **Generate 3–5 NSM candidates** — each proxies that value as a measurable metric.
3. **Apply the 3 criteria** (Amplitude §2): (a) Customer value? (b) Strategy fit? (c) Leads revenue? All three required; two-of-three = supporting metric only.
4. **Time-shifted correlation** — does the candidate *lead* revenue over 6–12 months?
5. **Perverse-incentive stress test** — could the team game this in a way that hurts customers?
6. **Pick one. Put it on the wall.** Explicitly name supporting metrics as supporting, not NSMs.
7. **Re-evaluate quarterly** — early stage → engagement; growth → retention; scale → revenue-adjacent.

### Output: the NSM Audit

```
NSM Audit: <product>
Customer value: "<customer experiences ___, measured in ___>"
Candidates: (1) <metric> (2) <metric> (3) <metric>
3-Criteria check: | Candidate | Value? | Strategy? | Leads rev? | Verdict |
Time-shifted correlation lead: <weeks/months>
Perverse-incentive risk: <what could go wrong> | Mitigation: <guardrail>
Chosen NSM: <NSM> — measured as <operational def>, reported <weekly/monthly>
Supporting (NOT NSM): <metric> — <why supporting>
Re-evaluation date: <next quarter>
```

*→ Method in Action: [Facebook's "Seven Friends in Ten Days" (2007–2010)](examples/facebook-seven-friends-in-ten-days-2007-2010.md)*

*→ 2026 lens: [AI product NSM — activated value vs. vanity metrics (2023–2026)](examples/ai-product-activated-value-vs-vanity-metrics-2023-2026.md)*

## NSM Selection Packs

Typical NSMs by domain: **content platforms** → minutes streamed per active user; **B2B SaaS** → active value moments per account (deals closed, tickets resolved); **marketplaces** → successful transactions; **freemium consumer apps** → core action completions. Adding a pack for your domain (typical NSMs, value-to-revenue mechanism, common mis-picks) is the easiest way to contribute.

## Applying It Well

- NSM is a leading indicator, not the goal. Revenue is the goal; NSM predicts it early enough to act.
- NSM measures customer value, not company convenience. Easy-to-measure ≠ right NSM.
- One metric only. Multiple "north stars" = strategy conflict, not a metric problem.
- Stress-test for perverse incentives. The team will optimize whatever the NSM measures.
- NSM evolves. Pre-commit to quarterly review.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Revenue as the NSM** | Revenue is the goal, not the leading indicator — lagging dashboard, not a steering wheel. |
| [D] **Multiple "north stars"** | Multiple north stars defeat cross-team alignment; if you genuinely need multiple, you have a strategy conflict. |
| [D] **Vanity metric promoted to NSM** | Page views, signups, app downloads move with marketing spend; they don't predict revenue. |
| [D] **NSM fails perverse-incentive test** | If ruthless optimization of this metric hurts customers, the NSM is mis-chosen. Stress-test first. |
| [D] **Treating the NSM as eternal** | Stage 1 → engagement; growth → retention; scale → revenue-adjacent. Re-evaluate quarterly. |
| [D] **No operational definition** | "Engagement" is not an NSM. "Users completing ≥3 core actions per week" is. Specify the event. |
| [D] **NSM as marketing/PR claim** | "Making the world better" is positioning, not a metric. NSM must be a number that goes up or down. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- The NSM is revenue itself (lagging indicator)
- The team has 3+ "north star" candidates and no decision among them
- The NSM is a vanity metric (signups, page views, app downloads)
- No perverse-incentive stress test was done
- No time-shifted correlation with revenue has been examined
- The NSM has no operational definition (e.g., "engagement" without specifying what counts)
- The same NSM has been in place for 2+ years across very different business stages with no review

## Verification

- [ ] The customer value is articulated in customer units (not product mechanism)
- [ ] 3–5 candidate metrics were generated
- [ ] Each candidate passes all three criteria (customer value + strategy + leading indicator)
- [ ] Time-shifted correlation with revenue is examined
- [ ] Perverse-incentive stress test is done with named mitigations
- [ ] Exactly one NSM is chosen with operational definition
- [ ] Supporting metrics are explicitly named *as* supporting, not as NSMs
- [ ] Quarterly re-evaluation is scheduled

---

*Part of **deciqAI Knowledge Skills** — 225 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/north-star-metric** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
