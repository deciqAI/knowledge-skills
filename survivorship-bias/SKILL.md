---
name: survivorship-bias
description: "Activate when: user says 'look at what winners/billionaires/champions did,' investment returns or fund performance are being cited, a strategy is justified by pointing to companies that succeeded, historical data is treated as representative of all cases, or someone says 'this works because X did it.'
  Do NOT activate when: population data is available and already selection-corrected; analysis is explicitly about survivors only with no claim about the broader population."
---

# Survivorship Bias

## Overview

**Survivorship bias** is drawing conclusions from a sample pre-filtered by survival — treating survivor traits as the *cause* of survival when non-survivors (absent from data by definition) may have had identical traits and still failed.

Canon: Wald (1943) reversed the Navy's bomber-armor recommendation — returning planes showed damage where hits were survivable; the missing planes (shot down) were hit where returning planes showed no damage. Armor the gaps, not the hits.

Composes with [`bayesian-reasoning`](../bayesian-reasoning/SKILL.md) (prior = population, not survivors), [`critical-thinking`](../critical-thinking/SKILL.md) (what would non-survivors say?), [`first-principles`](../first-principles/SKILL.md) (population is bedrock), and [`abductive-reasoning`](../abductive-reasoning/SKILL.md) ("winners have trait Y" is one hypothesis; randomness is another).

## When to Use

- Someone draws lessons from "what successful X did"
- Investment returns / fund performance / backtested strategies are cited
- A business strategy is justified by pointing to companies that used it
- Medical / treatment success rates are reported without dropout data
- Career advice comes from what top performers did

**Not when:** population data available and filter already corrected; analysis is intentionally about survivors only with no population claim.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete claim and data → run The Process directly.
- **Coach mode:** unfamiliar or no case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: "Before believing 'X worked because winners did X,' ask whether the losers did the same X — they're not in your sample to refute it."
2. Check fit: if sample is explicitly restricted to survivors with no population claim, this lens doesn't apply.
3. Elicit their real claim and the visible data they have.
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time: what filter produced this sample? what's missing? if missing data looked like the sample, would the conclusion hold?
> **[WAIT — do not advance until user responds]**
5. Close by naming the selection-corrected conclusion (or marking it unprovable from this data alone).
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State the claim:** What is being concluded, from what sample, from what source?

**Step 2 — Identify the survival filter:** What process produced this sample? What was the population before the filter? What fraction was removed? What did the filter select for/against?

**Step 3 — Construct the non-survivor hypothesis:** What did non-survivors likely have? Did they share the trait attributed to success? Would the claim hold if we could see them?

**Step 4 — Re-estimate strength:** Best case = trait explains survival (non-survivors lacked it). Worst case = trait doesn't explain survival (non-survivors had it too). What evidence distinguishes these?

**Step 5 — Correct or mark:** Get population data and re-run analysis with selection correction. If unavailable, mark conclusion as conditional on survivor sample.

## Output Template

```markdown
# Survivorship Bias Analysis: <claim>
Claim / sample / source:
Survival filter (what removed non-survivors, population size est., survival rate est.):
Non-survivor hypothesis (what they likely had/lacked, could they have had same trait):
Corrected inference (conclusion, confidence, what data would settle it):
```

*→ Method in Action: [Abraham Wald and the Statistical Research Group, 1943](examples/abraham-wald-and-the-statistical-research-group-1943.md)*

## Pack: Common Survivor Patterns

| Domain | Survivor sample | Missing non-survivor data | Biased claim |
|---|---|---|---|
| Business / startup | Surviving companies | Failed companies | "Successful companies do X" |
| Investment returns | Active funds / listed stocks | Closed funds / delisted stocks | "Stocks return 10% annually" |
| Career advice | Top performers | People who left the field | "To succeed, do X" |
| Scientific findings | Published studies | Unpublished null results | "X is significant" |
| Treatment efficacy | Patients who completed | Drop-outs, deaths during treatment | "X% recovered" |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Look at the data" (survivor sample) | Survivor data ≠ population data. Correct or mark as conditional. |
| [D] Citing one famous example as proof | N=1 in survivor sample tells you nothing about the rate. |
| [D] "X is the formula for success" | If failures did the same X, X is not the formula. Get non-survivor data or stop claiming. |
| [D] "We use a backtested strategy" | If backtest excludes failed/delisted stocks, results are upward-biased. |
| [D] "If we had non-survivor data, we'd see the same pattern" | Unfalsifiable without the data. Get it or hold the claim. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Sample described as "successful X" or "the X who made it"
- Data source is survivor-filtered (active funds, surviving companies, published studies)
- Base rate of failure / dropout not stated
- Conclusions about a population drawn from the survivor subset

## Verification

- [ ] Survival filter identified
- [ ] Non-survivor population size estimated
- [ ] Non-survivor hypothesis constructed
- [ ] Conclusions conditional on survivor sample, or formally selection-corrected
- [ ] Recommendation robust to worst-case non-survivor hypothesis

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/survivorship-bias?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=survivorship-bias** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
