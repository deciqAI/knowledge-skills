---
name: incentive-design
description: "Activate when: user asks why a team keeps doing the wrong thing despite training; user is designing compensation, bonuses, or commissions; user says 'people are gaming the metric' or 'our OKRs aren't working'; user wants to fix a performance management system; user asks what incentives are driving a behavior; user is drafting contracts or platform rules to shape behavior.
  Do NOT activate when: the situation is clearly individual misconduct with no systemic pattern; user wants psychological persuasion tactics rather than structural system design. More: deciqai.com/s/incentive-design"
---

# Incentive Design

## Overview

Behavior follows incentives more reliably than character, intent, or training. Get the incentives right and mediocre operators produce excellent results; get them wrong and talented teams produce dysfunction. This is Charlie Munger's "Reward and Punishment Superresponse Tendency" — his first and most important of 25 psychological tendencies (1995 Harvard Law School lecture). The operational question: when behavior is undesirable, ask "what incentive makes this rational?" before asking "what's wrong with these people?"

Composes with [`principal-agent`](../principal-agent/SKILL.md), [`goodharts-law`](../goodharts-law/SKILL.md), [`signaling-games`](../signaling-games/SKILL.md), [`okr-goal-setting`](../okr-goal-setting/SKILL.md), [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md).

## When to Use

- Designing compensation, bonuses, commissions, OKRs, or performance management
- Diagnosing why a team is producing undesirable behavior despite training or management
- Drafting contracts, regulations, or platform rules where behavior must be shaped
- Evaluating an existing system for hidden perverse incentives
- Designing reward signals or pricing in AI-native products (RLHF/reward hacking, usage-based vs outcome-based pricing, scarce AI-talent comp amid heavy AI capex and fast AI adoption)

**Not when:** clearly individual misconduct unrelated to systemic incentives; using incentive framing to excuse deliberate bad-faith behavior.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete incentive design challenge → run The Process directly.
- **Coach mode:** user is new to the framework → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** rational actors produce the behavior incentives favor, regardless of stated intent — check incentives before character.
2. **Check fit.** If the behavior is clearly individual misconduct, this framework adds less value. Otherwise, apply.
3. **Elicit the goal and current incentives.** What behavior do you want? What incentives exist now? What are those incentives producing?

> **[WAIT — do not advance until user responds]**

4. **Diagnose and design.** What behavior do current incentives make rational? Where's the gap? What would make goal-behavior the rational choice?

> **[WAIT — do not advance until user responds]**

5. **Close:** redesigned structure + gaming countermeasures + monitoring plan.

> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Goal and actors:** desired outcome · required behavior · actors · time horizon.
**Step 2 — Map current incentives:** rewards (financial, status, autonomy) · penalties · timing · observability.
**Step 3 — Diagnose alignment gap:** what behavior do current incentives rationally produce? where's the mismatch (metric, magnitude, timing)?
**Step 4 — Design new structure (7-item checklist):** (1) alignment (2) measurability (3) timing (4) threshold structure (5) anti-gaming predictions (6) long-short balance (7) tampering defense.
**Step 5 — Anticipate Goodhart's Law:** whatever you incentivize will be optimized — map the most-likely gaming pattern and close it.
**Step 6 — Implement and monitor:** pilot first · monitor 3-6 months · review cycle every 6-12 months · build in actor feedback.

## Output Template
```
Incentive Design: <system>
Goal/actors | Current incentives | Alignment diagnosis
Redesign (7-item) | Pilot scope / Monitoring / Review cycle
```

*→ Method in Action: [Munger 1995 + FedEx + Modern Applications](examples/munger-1995-fedex-modern-applications.md)*
*→ 2026 lens: [Incentive Design in the AI Economy — RLHF reward design, scarce-talent comp, usage-based pricing (2024–2026)](examples/ai-economy-incentives-rlhf-talent-pricing-2024-2026.md)*

## Pack: Application Patterns

| Domain | Common misalignment | Aligned design |
|---|---|---|
| Sales | Pay on closed deals only | Mix acquisition + retention + customer-fit |
| Executive comp | Options vest 1-4 years | Multi-year vesting + clawbacks + risk-adjusted metrics |
| Engineering | Promote on velocity | Add quality + on-call + cross-team metrics |
| Customer support | Pay on tickets closed | Add reopen rate + satisfaction |
| Recruiter | Bonus per hire | Add 12-month retention + performance ratings |
| Health system | Fee-for-service | Outcomes-based; bundled payments |

## Applying It Well

- Look at the incentives before you look at the people
- Incentive-caused bias is invisible to the actor — they sincerely believe they are doing the right thing
- The most important incentive design is at the founding moment; embedded structures become hard to change
- "Roughly right" incentives often produce dramatically wrong behavior at scale — precision matters

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our people just need more training" | Training rarely fixes incentive misalignment. Fix the incentives. |
| [D] "We hire for character" | Even good character bends under bad incentives. Incentives reliably dominate character in systematic behavior. |
| [D] "The incentive structure is industry-standard" | Industry-standard structures produce industry-standard dysfunctions. |
| [D] "Our team understands the goal" | Understanding the goal doesn't override misaligned incentives. |
| [D] "We can't change comp mid-year" | Real constraint — but plan the change for next cycle, don't accept the misalignment indefinitely. |
| [D] "Goodhart's Law is overstated" | Wells Fargo, standardized testing, gaming KPIs say otherwise. Pre-commit anti-gaming defenses. |
| [D] "We can't anticipate gaming" | You can. Spend time pre-launch imagining how it'll be gamed. The probabilities are higher than you think. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Behavior attributed to character/capability rather than incentives
- New people hired or fired without examining the incentive structure
- Compensation or KPI system not reviewed in 2+ years
- Previously-functioning incentive system starting to produce gaming
- Anti-gaming countermeasures absent from a metric-driven system

## Verification

- [ ] Goal-behavior explicitly specified
- [ ] Current incentives mapped
- [ ] Alignment gap diagnosed
- [ ] Redesigned incentives address the alignment
- [ ] 7-item checklist applied
- [ ] Goodhart-style gaming anticipated
- [ ] Monitoring and review cycle in place

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/incentive-design** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/incentive-design.json*
