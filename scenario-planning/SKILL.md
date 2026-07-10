---
name: scenario-planning
description: "Activate when: user says 'what are the scenarios,' 'stress test our strategy,' 'what if X happens,' 'multiple futures,' 'strategic resilience,' or is making a high-stakes irreversible decision with a 3+ year horizon where a single forecast could be catastrophically wrong.
  Do NOT activate when: the decision is short-horizon and easily reversible (sprint priorities, A/B test order); or only one driver matters and it is already measurable — use sensitivity analysis instead."
---

# Scenario Planning

## Overview

Scenario planning accepts that certain futures are genuinely *unknowable* and prepares for several of them rather than betting on one forecast. Pierre Wack formalized this at Shell in the early 1970s; Shell's pre-built Scenario B let it survive the 1973 oil shock while competitors were unprepared. Schwartz: "The goal is not to predict the future but to make decisions that are robust across a variety of possible futures." (*The Art of the Long View*, 1991, p. 9.)

**Composition:** [probabilistic-thinking](../probabilistic-thinking/SKILL.md) before (base-rate grounding); [second-order-thinking](../second-order-thinking/SKILL.md) inside each scenario (chain reactions); [inversion](../inversion/SKILL.md) alongside (stress-test current strategy).

## When to Use

Apply when: decision is large and hard to reverse; 3+ year horizon with a genuinely bi-directional driver; non-consensus outcome would be catastrophic; macro forces (geopolitics, regulation, technology) are pivotal; a bet hinges on whether AI capex / AI valuations sustain or correct, or on how AI adoption and chip-supply policy unfold; or you are weighing how deep an AI-vendor commitment or multi-year enterprise AI-adoption bet to make while pricing, compute supply, and vendor viability are unsettled.

**When NOT to use:** Tactical/short-reversibility decisions; single measurable driver (use sensitivity analysis); team lacks authority to change strategy; as a substitute for execution.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete decision → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: scenario planning builds 3–4 different plausible futures and asks "can our strategy survive all of them?" instead of betting on the most likely one.
2. Check fit against When to Use / When NOT to use. If decision is short-horizon and reversible, redirect to a simpler tool.
3. Elicit their real decision. "I want to think about the future" is not a case. "Should we build a factory in Eastern Europe given supply-chain uncertainty?" is. Get specific.
> **[WAIT — do not advance until user responds]**
4. Walk The Process one step per exchange: focal question first, then drivers, then the two critical uncertainties — ask at each gate rather than generating on their behalf.
> **[WAIT — do not advance until user responds]**
5. Close by naming the one scenario the team had not taken seriously before, and the one pre-emptive action it suggests.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Scenario Matrix**. Focal question first, then drivers, then the 2×2, then strategy derivation.

**Stop-rule:** At Step 3, if you cannot find at least one critical uncertainty that is both (a) highly impactful and (b) genuinely bi-directional, stop — run a sensitivity analysis instead.

1. **State the focal strategic question.** Specific: names a decision, a time horizon, and the driving uncertainty.
2. **Identify key drivers.** Sort into *predetermined elements* (background constants) and *critical uncertainties* (highly impactful, genuinely bi-directional).
3. **Select the two most critical uncertainties.** Most impactful on the focal question AND most independent of each other. Each axis has two plausible poles — not "good vs bad."
4. **Build the 2×2 Scenario Matrix.** Name each quadrant memorably. Write a full narrative paragraph per scenario: internally consistent, no contradictions. Quality check: does at least one scenario make the team uncomfortable?
5. **Derive strategic implications.** For each scenario: current strategy performance, biggest opportunities, biggest threats, most valuable capabilities.
6. **Identify robust moves and contingent bets.** Robust moves = act now. Contingent bets = hold until leading indicators fire. Assign 3–5 leading indicators per scenario with monitoring owner and review cadence.

### Output: Scenario Matrix

```
Focal Question | Planning Horizon | Predetermined Elements
Critical Uncertainties: Axis 1 / Axis 2
Four Scenarios (name + narrative each)
Strategic Implications table (performance / opportunities / threats / capabilities)
Robust Moves (act now) | Contingent Bets (trigger + leading indicators)
Leading Indicators & Monitoring (scenario / indicator / threshold / owner / cadence)
```

*→ Method in Action: [Shell Group Planning and the 1973 Oil Crisis](examples/shell-group-planning-1973-oil-crisis.md)*
*→ 2026 lens (buyer's seat): [An Enterprise Buyer's AI-Adoption Bet Under the Capex + Chip Fog (2024–2026)](examples/enterprise-ai-adoption-under-capex-and-chip-fog-2024-2026.md)*

## Scenario Packs

Domain-specific axes (matrix process identical everywhere): **Supply chain** — supplier-country stability × commodity price regime; robust: multi-source, inventory buffers. **Tech/AI** — capability pace × regulatory environment; robust: modular architecture, API abstraction. **Market entry** — political stance × competitor response; must include scenario where stance reverses post-entry. **Org design** — talent tightness × automation pace; robust: skills-based hiring, modular teams.

## Applying It Well

- The uncomfortable scenario is the point — if every quadrant fits current strategy, axes are not genuinely uncertain.
- Narratives must be internally consistent; contradictions invalidate the scenario.
- Robust moves now; contingent bets only when leading indicators confirm a specific scenario.
- Monitoring is not optional — assign owners and a calendar trigger; no cadence = expensive documents.
- Wack's real work was persuasion — budget as much time for communication as for construction.
- Resist the "base case" pull; update the matrix annually or when key indicators move significantly.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **"We have a base case and two sensitivity cases."** | Sensitivity cases vary magnitude on one axis; they are not scenarios. Scenarios require genuinely different causal structures, not just high/low values. |
| [D] **All four scenarios are variations of the current trajectory.** | If every scenario is "like today, but more/less of X," axes are predetermined trends. A real matrix contains at least one world that contradicts the team's current mental model. |
| [D] **"We did scenario planning" — matrix built but no strategy changed.** | Scenario planning without strategy differentiation is documentation theater. If the robust strategy is identical to the pre-exercise plan, scenarios were too tame or are being ignored. |
| [D] **Choosing axes that are actually correlated.** | Correlated axes collapse the matrix into one axis with only two real quadrants. Axes must be independent. |
| [D] **Loading narrative work onto the "most likely" scenario.** | If one scenario has a five-page narrative and others have one paragraph, the team is doing single-point planning with a matrix label. All scenarios deserve full treatment. |
| [D] **Using scenario planning to justify a pre-decided strategy.** | The tell: the "robust strategy" is exactly what the team planned to propose before the exercise. |
| [D] **Skipping the leading indicators.** | A scenario with no leading indicators is a thought experiment, not a management tool. |
| [D] **Treating scenarios as mutually exclusive futures rather than narrative tools.** | Reality will be messier. The point is pre-thought responses so when signals appear, reaction is faster and less reactive. |
| [D] **Letting the "uncomfortable" scenario die in the session.** | Teams consistently under-resource the scenario that most contradicts current bets. Wack documented this explicitly in 1985. |
| [D] **Reusing last year's scenarios without update.** | Scenarios have a shelf life. Stale scenarios create false confidence — worse than no planning. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- All scenarios are consistent with current strategy performing well; no team discomfort
- Team cannot name 3+ leading indicators per scenario
- Matrix axes are correlated rather than independent
- No "robust moves vs. contingent bets" distinction
- No owner or review cadence assigned to monitor leading indicators
- Scenario exercise was a one-day workshop with no follow-up or strategy document references
- Every scenario narrative extrapolates recent trends; no structural break required

## Verification

- [ ] Focal question names a decision, time horizon, and driving uncertainty
- [ ] Two critical uncertainties named, each genuinely bi-directional with evidence
- [ ] Matrix axes are independent (not causally correlated)
- [ ] Each scenario has a full internally consistent narrative
- [ ] At least one scenario contradicts current strategy or planning assumptions
- [ ] Robust moves distinguished from contingent bets
- [ ] Each scenario has >= 3 leading indicators with monitoring owner and review cadence
- [ ] The "uncomfortable scenario" received equal treatment as comfortable ones

---

*Part of **deciqAI Knowledge Skills** — 223 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/scenario-planning** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
