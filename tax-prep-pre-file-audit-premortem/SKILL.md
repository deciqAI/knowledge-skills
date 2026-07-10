---
name: tax-prep-pre-file-audit-premortem
description: "Activate when: a return has aggressive/uncertain positions (large Schedule C losses, high meals/vehicle, hobby-vs-business, real-estate professional status, R&D/ERC-type credits, crypto); before releasing a complex return; client says 'will this get me audited?'. Do NOT activate when: simple W-2-only standard-deduction return; the question is a straight lookup."
---

# Tax Prep — Pre-File Audit Premortem

> **Industry front door for [premortem](../premortem/SKILL.md).** Adds domain triggers, example, packs only. Run the parent's Process; parent content unchanged.
> **Not legal or tax advice.** Verify positions against current IRC/IRS guidance.

**Activate when:** a return has aggressive/uncertain positions (large Schedule C losses, high meals/vehicle, hobby-vs-business, real-estate professional status, R&D/ERC-type credits, crypto); before releasing a complex return; client says "will this get me audited?"
**Do NOT activate when:** simple W-2-only standard-deduction return; the question is a straight lookup.

## Why this variant
The parent [premortem](../premortem/SKILL.md) runs the clock forward to a failure and works backward. Here the "failure" is a **notice/exam disallowing a position + preparer penalty (§6694) or client interest & penalties**. Assume the return was pulled — what got disallowed and why? Fix before filing.

## Domain inputs → parent's Process
- Imagine an IRS/state exam letter 18 months out.
- List every position that could be disallowed; rate substantial-authority / reasonable-basis + disclosure need (Form 8275).
- For each: is contemporaneous substantiation in hand *now*? If not, the position is a future loss.

## Worked example
Client claims 95% business use of one vehicle, no mileage log.
→ Premortem: exam disallows for lack of a contemporaneous log → back-tax + accuracy penalty. Mitigation now: reconstruct/obtain log or reduce the position + note it. Decide before e-file.

## Compliance anchors
- §6694 preparer penalty · substantial authority / reasonable basis · Form 8275 disclosure · Circular 230 §10.34.

## Packs
- **Solo:** 10-minute pre-file "what would an examiner kill" pass on flagged lines.
- **Firm:** partner review gate for returns above a complexity/position threshold.

## Red flags
- Position depends on a record the client "has somewhere" but hasn't produced.
- Round numbers on large deductions.
- Year-over-year swing with no life event.

## Verification
- [ ] Each uncertain position rated for authority level
- [ ] Substantiation confirmed in hand or position adjusted
- [ ] Disclosure (8275) decision made where needed
- [ ] Client informed of residual exam risk

---
Part of **deciqAI Knowledge Skills**. Core method: [premortem](../premortem/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 223 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/tax-prep-pre-file-audit-premortem** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
