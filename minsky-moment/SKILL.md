---
name: minsky-moment
description: "Activate when: user asks 'is this a bubble?', 'what's the tail risk here?', 'this time is different', 'leverage has been stable for years', 'the fundamentals support these prices', someone wants to diagnose credit cycle fragility, analyze debt structure risk, or assess whether a calm financial period is hiding systemic danger.
  Do NOT activate when: the entity has no meaningful leverage and is funded entirely from operating cash flows; collapse risk is primarily operational rather than financial (e.g., a debt-free tech company facing competitive displacement)."
---

# Minsky Moment

## Overview

A **Minsky Moment** is the point at which a leveraged financial system tips from apparent stability into rapid self-reinforcing collapse — caused by the internal dynamic of debt accumulation that sustained stability itself produced. Minsky identified three debt stages systems cycle through: **Hedge** (income covers principal + interest), **Speculative** (income covers interest only; must roll over principal), **Ponzi** (income covers neither; depends on asset appreciation). Stability breeds instability: prolonged calm leads rational actors to accumulate more risk until debt cannot be serviced from income alone.

**Compose with neighbors:** Use [black-swan](../black-swan/SKILL.md) to distinguish Minsky dynamics from genuine tail events — a Minsky Moment is predictable, not random. Use [antifragile](../antifragile/SKILL.md) to identify who gains from Minsky collapses. Use [margin-of-safety](../margin-of-safety/SKILL.md) to operationalize the hedge financing requirement.

## When to Use

Apply when:
- Analyzing credit cycles, asset price levels, or financial system fragility after prolonged stability
- Evaluating debt structure of a company, sector, or economy
- Building a risk scenario for an investment, loan, or counterparty exposure
- Someone says: *"this time is different," "leverage has been stable," "what's the tail risk," "is this a bubble?"*
- Assessing an AI-capex / AI-infrastructure boom, circular ("round-trip") vendor financing, GPU-collateralized debt, or whether prolonged AI-boom stability is hiding an "AI bubble"

**When NOT to use:**
- Entity has no meaningful leverage — Minsky dynamics require debt
- Stability period is less than 18–24 months — risk-accumulation requires sustained calm
- Collapse risk is primarily operational, not financial
- You need to predict *when* collapse will occur — Minsky identifies structural fragility, not timing

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific leveraged entity, market, or credit cycle → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. What-it-is: A Minsky Moment is when a system collapses under debt built up precisely *because* things were going well — stability creates the conditions for instability.
2. Check fit — no leverage or stability period under 18 months → redirect to a simpler risk framework.
3. Elicit the specific entity or market (e.g., "debt structure fragility in US CRE after 3 years of low defaults").
> **[WAIT — do not advance until user responds]**
4. Walk through the four diagnostic steps one at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Name the specific stress that would trigger the moment and what the first-order collapse sequence looks like.
> **[WAIT — do not advance until user responds]**

## The Process

**Stop rule:** If cash flow and debt service data are unavailable, name the data gap — do not force a diagnosis.

1. **Classify debt structure.** Hedge (income covers P+I) / Speculative (interest only, rollover-dependent) / Ponzi (appreciation-dependent). Assign stage or distribution.
2. **Measure stability runway.** Duration of low-volatility regime; leverage ratio trend; lending standard trend. Key signal: loosening standards *during* stability.
3. **Identify trigger stress.** For speculative units: credit tightening that prevents rollover. For Ponzi units: price decline below obligation. Name mechanism and magnitude.
4. **Map collapse cascade.** First-order consequences → price compression / credit tightening → second-order reach to speculative units → cascade floor.

### Output: Minsky Fragility Diagnosis

```
Entity: <name> | Stage: <Hedge/Speculative/Ponzi distribution>
Stability runway: <duration> | Leverage trend: <up/flat/down> | Lending standards: <loosening/stable>
Speculative trigger: <credit event + magnitude>
Ponzi trigger: <price decline + magnitude>
Cascade: <1st-order> → <2nd-order> → floor: <backstop>
Fragility: <High/Medium/Low> | Implication: <...>
```

*→ Method in Action: [US Subprime Mortgage Market (2003–2008)](examples/us-subprime-mortgage-market-2003-2008.md)*

*→ 2026 lens: [The AI capex financing loop (2023–2026)](examples/ai-capex-circular-financing-2023-2026.md) — circular vendor financing among Nvidia, OpenAI, Oracle, CoreWeave and the hyperscalers*

## Minsky Packs

| Domain | Hedge | Speculative | Ponzi | Trigger |
|---|---|---|---|---|
| Corporate credit | Coverage > 5x | LBO, 1.5–3x, refi-dependent | Distressed/PIK | Credit spread widening |
| Real estate | Rent covers debt service | Negative carry, appreciation-dependent | Development, sale-proceeds only | Rising cap rates + loan rates |
| Sovereign | Primary surplus | Rolling maturing debt | Borrowing > deficit + interest | Loss of market access |

## Applying It Well

- Causation, not correlation: debt is dangerous when high *because of* stability, not just when high.
- Lending standards are the leading indicator — loosening during calm signals the debt-stage shift before Ponzi dominates.
- The cascade is always worse than the first-order shock — trace second and third-order transmission vectors.
- Structural fragility can persist longer than seems rational — Minsky does not predict timing.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Leverage has been stable for years — this is sustainable." | Sustained stability is the diagnostic signal, not reassurance. It drives the debt-stage shift. |
| [D] "The fundamentals support these prices." | The issue is whether debt can be serviced from income *at current prices*, not whether fundamentals exist. |
| [D] "Central bank intervention will prevent a Minsky Moment." | Backstops raise the cascade floor; they do not eliminate the mechanism. 2008 proceeded despite Fed intervention. |
| [D] "This is a temporary liquidity problem, not a solvency problem." | Liquidity problems *become* solvency problems when forced sales compress prices below book value. |
| [D] Conflating Minsky with any market decline. | Requires: stability-induced leverage accumulation + debt-stage shift + trigger converting speculative to unsustainable. |
| [D] Treating the three debt stages as mutually exclusive. | Any real system contains all three simultaneously. Diagnosis is about the *distribution*. |
| [D] Assigning a stage without debt service coverage data. | "It looks like Ponzi" is not a diagnosis. Staging requires actual cash flow and rollover data. |
| [D] "We have more financial sophistication now." | Sophisticated risk tools enable more leverage via apparent precision — creating moral hazard. |
| [D] Ignoring second-order leverage. | CDOs-of-CDOs, repo collateral chains amplify the first-order cascade; missing these misses the primary mechanism. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- 3+ years of unusual calm with no Minsky check run
- Lending standards loosening during the stable period (covenant-lite, rising LTV, declining coverage)
- Share of Ponzi/speculative financing growing during stability
- Risk models showing lower volatility than historical norms — trained on stability, they understate tail risk
- "Fundamentals support prices" without checking whether they generate income-based debt service capacity

## Verification

- [ ] Debt stages classified using actual cash flow and debt service data (not impressionistic)
- [ ] Stability runway measured: duration, leverage trend, lending standard trend
- [ ] Trigger stress named for speculative and Ponzi units with specific mechanism and magnitude
- [ ] Cascade traced two orders minimum (first-order → second-order → floor)
- [ ] Timing uncertainty acknowledged — fragility diagnosis is not a timing prediction

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/minsky-moment** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
