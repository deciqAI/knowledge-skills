---
name: mortgage-loan-program-matching
description: "Activate when: matching a borrower to Conventional/FHA/VA/USDA/Jumbo/Non-QM; deciding fixed vs ARM; 'which program fits this borrower?'; borderline DTI/LTV/credit. Do NOT activate when: borrower is pre-committed to one specific product with no alternative. More: deciqai.com/s/mortgage-loan-program-matching"
---

# Mortgage — Loan Program Matching

> **Industry front door for [decision-tree](../decision-tree/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not lending advice.** Program rules change; verify current agency/investor guidelines.

**Activate when:** matching a borrower to Conventional/FHA/VA/USDA/Jumbo/Non-QM; deciding fixed vs ARM; "which program fits this borrower?"; borderline DTI/LTV/credit.
**Do NOT activate when:** borrower is pre-committed to one specific product with no alternative.

## Why this variant
The parent [decision-tree](../decision-tree/SKILL.md) maps branching choices to outcomes. Program selection is a decision tree over borrower attributes (credit, DTI, LTV, down payment, property type, VA eligibility) → eligible programs → net cost/fit.

## Domain inputs → parent's Process
Branch on gating attributes and roll back to best fit:
- Credit + DTI + LTV + reserves → which agencies qualify.
- Down payment / MI: FHA (MIP) vs Conventional (PMI removable) vs VA (0% + funding fee).
- Property/occupancy and loan size (conforming vs jumbo).
- Compare total cost + approval probability, not just rate.

## Worked example
680 credit, 3.5% down, moderate DTI, first-time buyer.
→ Tree: FHA qualifies now but carries lifetime MIP; Conventional 97 may work with removable PMI. Compare 5-yr total cost + approval odds; recommend on net fit, documented. Present options fairly (ECOA).

## Compliance anchors
- Present options without steering to your own benefit; fair-lending (ECOA/Reg B); ATR/QM feasibility.

## Packs
- **Solo LO:** program-fit matrix by borrower profile.
- **Brokerage:** investor-overlay quick reference.

## Red flags
- Matching on rate alone, ignoring MI/total cost.
- Steering toward higher-comp product (fair-lending + LO-comp risk).
- Ignoring ATR/QM feasibility.

## Verification
- [ ] Eligible programs derived from borrower attributes
- [ ] Total cost + approval odds compared (not just rate)
- [ ] Options presented fairly; rationale documented
- [ ] ATR/QM feasibility checked

---
Part of **deciqAI Knowledge Skills**. Core method: [decision-tree](../decision-tree/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 233 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/mortgage-loan-program-matching** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/mortgage-loan-program-matching.json*
