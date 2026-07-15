---
name: mortgage-loan-fallout-premortem
description: "Activate when: a file is submitted or in underwriting; rate lock is ticking; 'what could kill this loan before closing?'; thin-file or borderline borrower. Do NOT activate when: clear-to-close with no open conditions."
---

# Mortgage — Loan Fallout Premortem

> **Industry front door for [premortem](../premortem/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.

**Activate when:** a file is submitted or in underwriting; rate lock is ticking; "what could kill this loan before closing?"; thin-file or borderline borrower.
**Do NOT activate when:** clear-to-close with no open conditions.

## Why this variant
The parent [premortem](../premortem/SKILL.md) imagines the failure and works backward. Loan fallout (denied/withdrawn after lock) wastes the borrower's rate, the LO's pipeline, and risks a lock extension cost. Premortem surfaces the killers while there's still time to cure.

## Domain inputs → parent's Process
Imagine the loan died at underwriting — why?
- Income/employment: VVOE fails, gap, variable-income miscalc.
- Assets: large deposits unsourced, insufficient reserves.
- Credit: new inquiry/tradeline mid-process changes DTI.
- Appraisal: comes in low; property/condition issues.
- Title/insurance/HOA: liens, uninsurable, HOA litigation.
For each likely killer, cure or condition *now*, before the lock burns.

## Worked example
Self-employed borrower, lock expires in 21 days.
→ Premortem flags: unsourced $20k deposit + P&L not yet CPA-reviewed. Cure now (paper trail + statement) so it doesn't detonate on day 18 forcing a costly extension.

## Compliance anchors
- If denial results, ECOA adverse-action notice within required timing; document the reason.

## Packs
- **Solo LO:** top-10 fallout-cause pre-submission scrub.
- **Brokerage:** condition-clearing SLA tied to lock timeline.

## Red flags
- Large deposits / new credit not addressed early.
- Variable income taken at face value.
- Appraisal risk ignored on unique properties.

## Verification
- [ ] Likely fallout causes enumerated
- [ ] Each cured or conditioned before lock burns
- [ ] Lock timeline vs condition SLA reconciled
- [ ] Adverse-action path ready if denied

---
Part of **deciqAI Knowledge Skills**. Core method: [premortem](../premortem/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/mortgage-loan-fallout-premortem** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
