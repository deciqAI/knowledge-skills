---
name: sunk-cost-fallacy
description: "Activate when: user says 'we've come too far to quit', 'we can't waste what we've already spent', 'should I keep going or cut my losses', 'we've invested too much to stop now', 'should I continue this project / relationship / position'. Do NOT activate when: prior investment genuinely lowers future marginal costs (real synergies exist); user asks about loss-aversion psychology in general without a concrete continue-or-quit decision."
---

# Sunk-Cost Fallacy

## Overview

The **sunk-cost fallacy** is the tendency to let prior, irrecoverable investments (money, time, effort, reputation) distort current decisions. Only *marginal future* costs and benefits should drive the next choice — sunk costs are already spent regardless of what you decide next. Composes with [`loss-aversion-prospect-theory`](../loss-aversion-prospect-theory/SKILL.md) (mechanism), [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) (correct rule), [`regret-minimization`](../regret-minimization/SKILL.md), and [`inversion`](../inversion/SKILL.md) (fresh-start test).

## When to Use

- "We've come too far to quit" is the dominant argument for continuing
- A project, feature, position, or relationship is being maintained despite negative marginal returns
- Decision-makers defend the original choice rather than evaluating current trajectory
- Team is doubling down after failure without re-examining the underlying thesis
- "We already built our own model / spent the AI capex" is the reason to keep an in-house or on-prem AI stack instead of migrating to a cheaper, better hosted model — or a founder keeps a commoditized AI-wrapper going because of prior investment despite falling API prices and rising foundation-model capability

**Not when:** prior investment genuinely reduces future marginal costs; negative signal is short-term variance; cost of switching exceeds cost of continuing.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete continue/quit decision → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** if you arrived today with no prior investment, would you start this from scratch?
2. **Check fit.** If the sunk cost legitimately lowers future costs, this is not a sunk-cost case.
3. **Elicit the specific decision and prior investment** — what is being continued, how much spent, future cost and expected return.
> **[WAIT — do not advance until user responds]**
4. **One question at a time:** what would you do with no prior investment? Is "we've come too far" the load-bearing reason?
> **[WAIT — do not advance until user responds]**
5. **Close:** frame the decision in marginal future-only terms + name one structural fix.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Specify sunk cost and current decision** (prior investment, current decision, arguments for/against continuing).

**Step 2 — Fresh-start test:** "If I arrived today with no prior investment, would I start this?" If no, that's the signal.

**Step 3 — Marginal future NPV:** additional cost to complete vs. expected future value (continue) vs. expected future value (quit + reallocate). Continue only if marginal NPV(continue) > marginal NPV(quit). The sunk cost does not appear in either side.

**Step 4 — Sunk-cost weight:** substitute "prior investment = $0." If the recommendation changes, the sunk cost is doing illegitimate work.

**Step 5 — Diagnose mechanism:** loss aversion / self-justification / social signaling / completion compulsion / cognitive accounting.

**Step 6 — Structural countermeasure:** pre-committed kill criteria, stage-gate funding, fresh-eyes review, decision-rights separation from project initiator.

## Output Template

```markdown
# Sunk-Cost Decision: <project>
Prior investment: | Current decision (continue/pivot/quit):
Fresh-start test: Would I start today? (Y/N) — if no, why continuing?
Marginal NPV (continue): | Marginal NPV (quit + reallocate):
Sunk-cost weight: if prior = $0, does recommendation change? (Y/N)
Mechanism: loss aversion / self-justification / social signaling / completion compulsion / cognitive accounting
Structural fix: [kill criteria / stage gate / fresh-eyes / decision-rights separation]
```

*→ Method in Action: [Arkes & Blumer's 1985 Studies](examples/arkes-blumers-1985-studies.md) · [The Concorde Program](examples/concorde-program.md)*
*→ 2026 lens: [AI Build-Out Sunk Costs (2023–2026)](examples/ai-buildout-sunk-costs-2023-2026.md)*

## Pack: Sunk-Cost Patterns

| Domain | Manifestation | Countermeasure |
|---|---|---|
| Software | "80% built, let's finish it" | Stage-gate with marginal-only criteria |
| Startup pivots | "We pitched investors on this market" | Fresh-eyes board review; pre-committed pivot triggers |
| Investment | "I'll wait for it to come back" | Pre-committed stop-loss, externally enforced |
| R&D | "Project is 90% complete" | Kill-criteria committee independent of project team |
| Career/education | "I've invested 10 years in this" | Five-year forward analysis ignoring past |
| Government | "We've spent $X billion already" | Sunset clauses; independent re-authorization |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We've come too far to quit now" | Distance traveled has zero causal influence on remaining value. Completion proximity is a feeling, not a fact. |
| [D] "We can't waste what we've already spent" | The spending is already waste-or-not. Continuing adds new spending to the same pile. |
| [D] "Quitting would be a loss" | Continuing is also a loss if marginal NPV is negative. Choice is recognized loss now vs. larger loss later. |
| [D] "We've learned so much" | Learning is realized whether you continue or quit — it doesn't change future project value. |
| [D] "We owe it to the team that built this" | Loyalty to people is real; loyalty to a failing project is not. Reallocate the team. |
| [D] "It would be irresponsible to walk away" | Funding a negative-NPV project with stakeholder money is the irresponsible act. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "We've spent $X" is a primary argument for continuing
- The project initiator is the sole decider on whether to continue
- Project is "90% done" and no one can articulate the marginal value of completion
- Kill criteria are absent or have been modified to accommodate current underperformance
- Loss-frame language dominates ("we'd lose everything") rather than future-frame language

## Verification

- [ ] Sunk cost specifically named and quantified
- [ ] Fresh-start test asked and answered honestly
- [ ] Marginal future NPV (continue vs. quit) computed
- [ ] Argument re-examined with sunk cost set to $0
- [ ] Psychological mechanism named
- [ ] At least one structural countermeasure chosen and assigned
- [ ] If continuing, kill criteria pre-committed for next decision point

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/sunk-cost-fallacy** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
