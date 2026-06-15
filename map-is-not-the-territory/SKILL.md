---
name: map-is-not-the-territory
description: "Activate when: a metric is improving but customers or employees are signaling problems; a strategy or process hasn't been reviewed in over a planning cycle; a team keeps disagreeing and can't resolve it with data; someone says 'the model shows...' or 'the data doesn't show any problems'; a plan is being followed because 'that's how we do it.' Do NOT activate when: the map is demonstrably current and freshly validated against the territory; the decision is so low-stakes that map imprecision doesn't matter."
---

# Map Is Not the Territory

## Overview

Any representation — metric, model, strategy deck, org chart, or process manual — is a selective, simplified, aging abstraction. Maps omit (reflecting past priorities), distort (projecting dynamic reality onto static surfaces), and age (the territory moves; the map does not). The map is useful because it compresses complexity; dangerous because users forget it is a compression. Composes with `goodharts-law` (optimizing a metric makes it an even worse map), [`first-principles`](../first-principles/SKILL.md) (rebuilding from territory when maps fail), and `narrative-fallacy` (every narrative is a map that ages).

## When to Use

- A key metric improves while customer feedback, morale, or competitor signals deteriorate
- Team disagreement cannot be resolved by data — parties are disagreeing about maps, not territory
- A strategy, model, process, or org chart has not been reviewed in more than one planning cycle
- "The data shows..." but the data is old, narrow, or from a proxy source
- A metric is being optimized directly without asking whether it still maps to the underlying goal

**Not when:** the map is demonstrably current and well-calibrated; decision is low-stakes; territory is stable and map is freshly validated.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete map/decision → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: the metric, model, or plan you are navigating with is not reality — it is a selective, aging abstraction of it. Confusing the two is how smart people make systematic errors.
2. Check fit: is there a map being used to navigate? Is there evidence the territory has moved beyond the map?
3. Elicit their real case: what is the map? what territory does it claim to represent? when was it last calibrated?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input: what does the map omit? how has it aged? what direct territory observations are available?
> **[WAIT — do not advance until user responds]**
5. Close by naming the map-territory gap explicitly: omissions identified, distortions named, calibration action defined, update trigger specified.
> **[WAIT — do not advance until user responds]**

## The Process

**S1 — Name the map:** what is it (metric, model, plan, process)? who made it and when? what territory does it claim to represent?

**S2 — Structural omissions:** what does it omit by design? by measurement limits? by aging? what signals are outside this map?

**S3 — Structural distortions:** what relationships does it assume (linear, causal, static)? what assumptions must be true for it to be accurate?

**S4 — Map age:** when was it last calibrated? what has changed since? is it inside or outside its useful life?

**S5 — Direct territory signal:** what direct observations are available (interviews, field visits, primary data)? where is divergence from the map greatest?

**S6 — Decide:** use as-is / update / replace. what specific updates close the most important gap? what is the update trigger?

## Output: Map-Territory Audit
```
Map: <name> | Created by/when | Territory it represents
Omissions: by design | by measurement limits | by aging
Distortions: linearity assumptions | artificial boundaries | hidden assumptions
Age: last calibrated | territory change rate | inside/outside useful life
Territory signals: source | key divergences from map
Decision: fit Y/N/Partially | required updates | update trigger
```

*→ Method in Action: [McNamara and the Vietnam Kill-Ratio Map](examples/mcnamara-vietnam-kill-ratio-map.md)*

## Pack: Map-Territory Mismatches Across Domains

| Domain | Map | Key omission | Territory signal missed |
|---|---|---|---|
| Startup growth | MAU | Churn drivers, value realization | Users activate but don't retain |
| Sales | Pipeline × close rate | Buying-committee dynamics | Close rate collapses late-stage |
| Team health | Satisfaction scores | Silent disengagement | Top performers leave without warning |
| Financial model | Revenue/cost projections | Cash flow dynamics | Model shows profit; cash crisis arrives |
| Org chart | Formal authority | Informal influence networks | Decisions route through uncharted nodes |

## Applying It Well

- Pair a map audit with at least one direct territory observation — not another map
- Distinguish map-territory decoupling from execution failure before diagnosing either
- Name the update trigger explicitly; maps without recalibration schedules age silently
- Expert confidence does not track map applicability to novel territory

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our metrics are all green — we're doing well." | Metrics are a map. Green metrics with deteriorating qualitative signals indicate map-territory decoupling. |
| [D] "The model shows this will work." | The model encodes assumptions that may be outdated. The territory does not read the model. |
| [D] "We followed the process exactly." | The process was a map of conditions that may no longer exist. Process compliance is not territory compliance. |
| [D] "The data doesn't show any problems." | The data measures a subset of territory designed for past priorities. Absence in data ≠ absence in territory. |
| [D] "We optimized the KPI — we improved the business." | Optimizing a metric is optimizing the map. Only direct territory observation shows whether underlying reality improved. |
| [D] "The expert said this is how the market works." | Expert models are maps from past encounters. Novel conditions may invalidate the map without invalidating the expert's confidence. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Key metric improving but qualitative signals (customers, team, partners) are worsening
- Model or plan not updated within the current competitive or operational cycle
- Team disagreements cannot be resolved by data — parties are disagreeing about maps, not territory
- A process is followed because "it's the process" without reference to its original outcome
- A metric is being managed directly rather than used as a signal of underlying reality
- Field team reports a reality that contradicts the dashboard — and is told the dashboard is correct

## Verification

- [ ] Map named and creation date identified
- [ ] Structural omissions listed (what the map cannot show by design)
- [ ] Structural distortions listed (what the map misrepresents by design)
- [ ] Map age assessed relative to territory's rate of change
- [ ] At least one direct territory observation gathered (not mediated by the map)
- [ ] Most significant map-territory divergence identified and named
- [ ] Decision made: use as-is, update, or replace; update trigger specified

**Stop rule:** if territory observation and map are consistent across multiple independent signals, stop auditing. Over-applying risks paralytic model-skepticism where no map is trusted enough to navigate.

---
*Part of **deciqAI Knowledge Skills** — open-source thinking skills that make rigor executable for AI agents. These 25 skills are a free taste of the 160+ skills wired into every deciqAI agent, which runs them autonomously to operate your company. **Try it free → https://www.deciqai.com/skills?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=map-is-not-the-territory** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
