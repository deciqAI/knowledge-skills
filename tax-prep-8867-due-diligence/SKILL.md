---
name: tax-prep-8867-due-diligence
description: "Activate when: preparing any return claiming EITC, CTC/ACTC/ODC, AOTC, or Head-of-Household status; onboarding a paid-preparer workflow; a reviewer says 'did we document due diligence?', 'are we 8867-covered?', 'EITC audit risk.'. Do NOT activate when: no refundable credit / HOH is claimed; the return is self-prepared with no paid preparer; the question is purely tax-law calculation (use a calc tool, not this)."
---

# Tax Prep — Refundable-Credit Due-Diligence (Form 8867)

> **Industry front door for [checklist](../checklist/SKILL.md).** This variant only adds domain triggers, a worked example, and industry packs. The reasoning engine is the parent checklist skill — run its Process. Nothing in the parent is modified or duplicated here.
> **Not legal or tax advice.** Guardrails reflect general IRS requirements; verify against the current Circular 230, Form 8867 instructions, and IRC §6695(g) before filing.

**Activate when:** preparing any return claiming EITC, CTC/ACTC/ODC, AOTC, or Head-of-Household status; onboarding a paid-preparer workflow; a reviewer says "did we document due diligence?", "are we 8867-covered?", "EITC audit risk."
**Do NOT activate when:** no refundable credit / HOH is claimed; the return is self-prepared with no paid preparer; the question is purely tax-law calculation (use a calc tool, not this).

## Why this variant
The parent [checklist](../checklist/SKILL.md) turns fuzzy "did we cover everything" into a verifiable gate. Paid-preparer due diligence under IRC §6695(g) is exactly that: a per-credit documented gate whose failure = **$635/return (2024, indexed) penalty each**. This maps the parent's gate discipline onto the four due-diligence requirements.

## Domain inputs → parent's checklist gate
The four §6695(g) requirements become the checklist's items:
1. **Completion & submission** of Form 8867 for each covered credit.
2. **Computation** — worksheets/records showing each credit was computed correctly.
3. **Knowledge** — no info appears incorrect/inconsistent/incomplete; document questions asked.
4. **Record retention** — keep 8867, worksheets, and the docs relied on (3 years).

## Worked example
Single filer, 2 qualifying children, Schedule C cash income near the EITC-max plateau.
→ Knowledge requirement triggers: document the reasonableness inquiry into cash receipts/expenses, residency of children (school/medical records seen), and relationship. Missing any = incomplete gate → **do not file**; return to intake.

## Compliance anchors
- IRC §6695(g) · Form 8867 & instructions · Circular 230 §10.22 (diligence) · Pub 4687 (paid preparer due diligence).

## Packs
- **Solo preparer:** minimum viable 8867 evidence folder per client.
- **Firm/season:** reviewer sign-off gate before e-file release; sampling for QC.
- **Enterprise:** tie gate to e-file blocker in software; log ruleId per return.

## Red flags
- Income sitting exactly at a credit's maximizing plateau.
- Inconsistent dependents vs prior year with no life-event explanation.
- Preparer "assumed" residency/relationship without any record.

## Verification
- [ ] 8867 completed for every covered credit
- [ ] Computation worksheets retained
- [ ] Reasonableness inquiries documented (who/what/when)
- [ ] Contemporaneous notes on any inconsistency resolved
- [ ] Retention folder started (3-yr clock)

---
Part of **deciqAI Knowledge Skills** — executable rigor for AI agents. Core method: [checklist](../checklist/SKILL.md).
