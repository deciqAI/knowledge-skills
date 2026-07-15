---
name: customs-duty-optimization-opportunity-cost
description: "Activate when: an importer has recurring, material duty spend; evaluating FTZ, duty drawback, first-sale valuation, bonded warehouse, or FTA use; 'are we leaving duty savings on the table?'. Do NOT activate when: de minimis / trivial duty where program cost exceeds benefit."
---

# Customs — Duty Optimization (Opportunity Cost)

> **Industry front door for [opportunity-cost](../opportunity-cost/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not legal advice.** Each program has strict eligibility; verify with counsel/CBP before relying on savings.

**Activate when:** an importer has recurring, material duty spend; evaluating FTZ, duty drawback, first-sale valuation, bonded warehouse, or FTA use; "are we leaving duty savings on the table?"
**Do NOT activate when:** de minimis / trivial duty where program cost exceeds benefit.

## Why this variant
The parent [opportunity-cost](../opportunity-cost/SKILL.md) measures the value of the best foregone alternative. Every duty dollar paid when a lawful program would have avoided/deferred it is a foregone saving. This surfaces those foregone alternatives and sizes them against setup cost.

## Domain inputs → parent's Process
Enumerate lawful alternatives and their net value vs status quo:
- **Duty drawback:** refund on duties for re-exported/destroyed goods (up to 99%).
- **Foreign-Trade Zone (FTZ):** defer/reduce/eliminate duty; inverted-tariff benefit.
- **First-sale valuation:** dutiable value = earlier bona fide sale price in multi-tier transactions.
- **FTA/preference** (see USMCA variant), bonded warehouse (deferral).
- Weigh each program's admin/setup cost; opportunity cost = savings foregone by *not* adopting the best-fit one.

## Worked example
Importer pays $800k/yr duty, re-exports ~30% of goods.
→ Foregone saving: drawback could refund ~99% on the re-exported portion (~$240k base) — far exceeding program setup. Not filing drawback is a recurring opportunity cost. FTZ may add inverted-tariff savings on the domestic portion.

## Compliance anchors
- 19 U.S.C. 1313 (drawback); FTZ Act / 19 CFR 146; first-sale (Nissho Iwai); bonded warehouse 19 CFR 19.

## Packs
- **Broker/advisory:** annual duty-spend audit → program-fit shortlist with net-savings sizing.
- **Enterprise importer:** FTZ feasibility + drawback recovery program.

## Red flags
- Paying recurring duty with no program review.
- Assuming programs are "too complex" without sizing the foregone savings.
- First-sale claimed without qualifying multi-tier documentation.

## Verification
- [ ] Applicable programs enumerated with net savings sized
- [ ] Setup/admin cost weighed against savings
- [ ] Eligibility documentation feasible for the chosen program
- [ ] Best-fit program recommended vs status-quo duty

---
Part of **deciqAI Knowledge Skills**. Core method: [opportunity-cost](../opportunity-cost/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/customs-duty-optimization-opportunity-cost** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
