---
name: utilitarianism
description: "Activate when: user asks 'what produces the most good,' 'who benefits and who gets hurt,' 'what's the net impact,' 'is this worth the trade-off,' 'what does the greatest good mean here'; user needs to evaluate a policy, product, or organizational decision that affects multiple parties differently; user is performing cost-benefit analysis or ethical trade-off evaluation.
  Do NOT activate when: the decision involves a single party with no stakeholder trade-offs (use expected-value-and-kelly instead); the question is purely about intrinsic rights or deontological constraints with no welfare aggregation needed."
---

# Utilitarianism

## Overview

**Utilitarianism** holds that the right action produces the greatest net well-being across all affected parties, weighted by magnitude and probability. Its power: it forces implicit trade-offs explicit. Its limit: the aggregation problem — summing welfare can justify severe losses to a few for diffuse gains to many, with no individual floor.

**Compose with neighbors:** [expected-value-and-kelly](../expected-value-and-kelly/SKILL.md) for probabilistic welfare estimates · [second-order-thinking](../second-order-thinking/SKILL.md) to trace full consequence chains · [prisoners-dilemma](../prisoners-dilemma/SKILL.md) when welfare-maximizing outcomes require coordination.

## When to Use

Apply when: (a) decision affects multiple parties with heterogeneous impacts; (b) performing cost-benefit analysis; (c) evaluating ethical trade-offs; (d) user asks *"who benefits / who gets hurt," "what's the net impact," "is this worth the trade-off?"*

**When NOT to use:** deontological constraint is present (use as input, not sole framework); impacts too uncertain to aggregate; single-party decision (use [expected-value-and-kelly](../expected-value-and-kelly/SKILL.md)); intrinsic rights question (pair with deontological frameworks).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete multi-party decision → run The Process directly.
- **Coach mode:** user unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What-it-is.** Utilitarianism: choose the action that produces the most well-being for the most people — but *requires* mapping who is affected, how much, and whether some losses are justifiable by others' gains.
2. **Check fit** — name rights violations, deontological constraints, or high uncertainty before proceeding.
3. **Elicit the specific decision and stakeholder set.** "Is policy X good?" is not workable; a concrete framing with identifiable affected parties is.
> **[WAIT — do not advance until user responds]**
4. **Walk through welfare mapping** one step at a time with the user's input.
> **[WAIT — do not advance until user responds]**
5. **Close by naming the most contested welfare assumption** — where the conclusion is most sensitive to a value reasonable people would weigh differently.
> **[WAIT — do not advance until user responds]**

## The Process

Five steps producing a **Utilitarian Welfare Map**.

**Stop rule:** If impacts span qualitatively different dimensions (money vs. physical safety vs. autonomy), do not add them without an explicit conversion rate and its justification.

1. **Map all affected parties.** (a) primary beneficiaries; (b) primary cost-bearers; (c) indirect affected; (d) future/long-term. Omitting any group biases the analysis.
2. **Estimate welfare impacts per party.** Nature (economic/physical/psychological/opportunity), magnitude (significant/moderate/minor), probability. Quantify where possible; rank qualitatively where not.
3. **Assess the aggregation problem.** Are impacts commensurable? Name the aggregation assumption and its ethical weight before summing.
4. **Compute or rank net welfare outcome.** Identify the welfare-maximizing option and the option with best minimum welfare.
5. **Stress-test the most contested assumption.** If wrong by 2x, does the conclusion change? Name the assumption, sensitivity, and what would resolve it.

### Output: Utilitarian Welfare Map

```
# Utilitarian Welfare Map: <decision>
Affected Parties: | Party | Relationship | Size |
Welfare Impacts:  | Party | Impact type | Magnitude | Probability | Expected welfare |
Aggregation Assessment: commensurable? / key assumption / ethical load
Net Welfare: Option A vs B | welfare-maximizing | best minimum welfare
Most Contested Assumption: assumption / 2x sensitivity / what resolves it
```

*→ Method in Action: [Cost-Benefit Analysis of the Clean Air Act (1970)](examples/cost-benefit-analysis-of-the-clean-air-act-1970.md)*

## Welfare Packs

**Healthcare:** QALYs gained, caregiver burden, productivity. Tool: cost per QALY. Key problem: rare vs. common disease aggregation.

**Product / platform:** Time saved, friction reduced, privacy reduced, attention captured. Key problem: gains to many vs. concentrated harms to vulnerable subsets.

**Regulatory / environmental:** Health outcomes, economic costs, ecosystem services. Key contested: discount rate for future benefits (3% vs. 1% changes present value by an order of magnitude).

*→ Primary sources: [references/sources.md](references/sources.md)*

## Applying It Well

- **Completeness of the affected party map determines quality** — omitting future generations or underrepresented groups biases every conclusion.
- **The aggregation problem is the ethical core** — ignoring it produces unacknowledged normative judgments dressed as analysis.
- **State conversion rates explicitly** — VSL, QALYs, utils: source, rate, and limitation every time.
- **Welfare-maximizing is not always ethically optimal** — rights constraints require separate normative input.
- **Stress-test the most influential assumption** — a conclusion that reverses at 20% variation is not robust.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] Omitting identifiable affected parties. | Omitting a cost-bearing group biases the conclusion — not neutral. |
| [D] Claiming net positive welfare without stating the conversion rate. | Every utilitarian analysis embeds a conversion rate; make it explicit. |
| [D] Treating welfare-maximizing as the final answer without checking rights constraints. | Aggregate optimization does not resolve whether non-overridable rights are violated. |
| [D] Using uncertain welfare estimates as if precise. | State uncertainty range; conduct sensitivity analysis. |
| [D] Ignoring second-order welfare effects. | Trace consequence chain at least two orders before concluding. |
| [D] Conflating "most people benefit" with total welfare maximization. | Total welfare = sum of magnitudes, not count of beneficiaries. |
| [D] Discounting future welfare without stating the discount rate. | The discount rate is a contested normative choice, not a technical input. |
| [D] Assuming market prices capture welfare accurately. | Willingness-to-pay is biased toward the wealthy; misses non-market welfare. |
| [D] Building the welfare map to justify a prior decision. | Run the map before committing, not after. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags · Verification

**Red flags:** affected party map omits a cost-bearing group · impacts summed without commensurability check · conversion rate not stated or sourced · contested assumption not stress-tested · second-order effects ignored · future welfare discounted without stating rate · rights constraints not acknowledged.

**Verification checklist:** All affected parties named including indirect/future · welfare impacts estimated per party with magnitude, probability, basis · aggregation problem addressed with conversion rate and source · net welfare outcome computed or ranked per alternative · both welfare-maximizing and best-minimum options identified · most influential assumption named and stress-tested · rights constraints acknowledged.

---

*Part of **deciqAI Knowledge Skills** — 225 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/utilitarianism** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
