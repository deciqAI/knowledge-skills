---
name: ria-client-margin-of-safety
description: "Activate when: building a retirement/decumulation plan; setting cash buffers/withdrawal rates; stress-testing a plan; client near retirement; 'will they be okay if markets drop early?'. Do NOT activate when: pure accumulation with long horizon and no near-term draws. More: deciqai.com/s/ria-client-margin-of-safety"
---

# RIA — Client Plan Margin of Safety

> **Industry front door for [margin-of-safety](../margin-of-safety/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not investment advice.**

**Activate when:** building a retirement/decumulation plan; setting cash buffers/withdrawal rates; stress-testing a plan; client near retirement; "will they be okay if markets drop early?"
**Do NOT activate when:** pure accumulation with long horizon and no near-term draws.

## Why this variant
The parent [margin-of-safety](../margin-of-safety/SKILL.md) builds a buffer so estimation error doesn't cause ruin. A retiree's plan lives or dies on **sequence-of-returns risk**; the margin of safety is the cash/bond buffer and withdrawal haircut that lets the plan survive an early bad market.

## Domain inputs → parent's Process
- Size a spending buffer (e.g. 1–3 yrs of withdrawals in cash/short bonds) so early drawdowns aren't sold at the bottom.
- Haircut the withdrawal rate below the "optimistic" number; plan to the conservative case.
- Stress-test against an early-crash sequence, not just average returns.

## Worked example
$1.5M portfolio, planned 5% draw, retiring into a rich market.
→ Margin of safety: hold 2 years' spending in cash, set draw at 4% with a guardrail to cut in down years. A crash in year 1 is met from the buffer, not by liquidating equities low. Plan survives the sequence.

## Packs
- **Solo:** buffer + guardrail rule embedded in every decumulation plan.
- **Advisory:** dynamic-spending (guardrails) policy documented in the IPS.

## Red flags
- Planning to average returns, ignoring sequence risk.
- No cash buffer; forced equity sales in downturns.
- Withdrawal rate set at the optimistic edge.

## Verification
- [ ] Spending buffer sized to horizon of concern
- [ ] Withdrawal haircut applied vs optimistic case
- [ ] Early-crash sequence stress-tested
- [ ] Guardrail/dynamic-spending rule documented

---
Part of **deciqAI Knowledge Skills**. Core method: [margin-of-safety](../margin-of-safety/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ria-client-margin-of-safety** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ria-client-margin-of-safety.json*
