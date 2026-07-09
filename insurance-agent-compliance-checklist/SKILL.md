---
name: insurance-agent-compliance-checklist
description: "Activate when: an insurance agent/agency must not skip licensing, disclosure, suitability, and replacement steps on a sale; 'am I compliant on this policy', selling/replacing a policy, onboarding a producer. Do NOT activate when: the question is pure coverage/rating with no compliance action."
---

# Insurance Agent — Sales Compliance Checklist

> **Industry front door for [checklist](../checklist/SKILL.md).** Adds domain triggers, example, packs. Parent Process unchanged.
> **Not legal advice.** Insurance rules are state-specific; verify against your state DOI and carrier requirements.

**Activate when:** binding a new policy; replacing an existing policy; selling annuities/life with suitability rules; onboarding a producer; building the agency's sales SOP.
**Do NOT activate when:** internal rating/coverage design with no compliance step.

## Why this variant
The parent [checklist] is a must-not-skip gate. Insurance sales carry state-mandated, penalty-backed steps (licensing/appointment, suitability, replacement disclosure, E&O) that are easy to skip at speed. This maps them onto the gate.

## Domain inputs → the checklist gate
- **License + appointment**: producer licensed in the state + line, appointed with the carrier; CE current.
- **Suitability** (esp. life/annuity/LTC): documented basis that the product fits the client's needs/finances. *Gate: no documented suitability basis on a replacement/annuity = do not bind.*
- **Replacement rules**: required replacement notices/comparison delivered and signed; no unjustified churning.
- **Disclosures**: fees, surrender charges, conflicts, agent-vs-broker capacity.
- **E&O + records**: E&O coverage active; application, disclosures, and suitability retained.

## Worked example
Agent replaces a client's existing annuity with a new one for a bonus, no comparison shown.
→ Gate fails on suitability + replacement disclosure (churning risk). Document the client's benefit vs surrender cost, deliver the replacement notice, or don't proceed.

## Compliance anchors
- State producer licensing/appointment; NAIC suitability/best-interest (annuity) model as adopted by state; replacement regulations; E&O.

## Packs
- **Solo agent**: per-sale compliance card (license/suitability/replacement/disclosure).
- **Agency**: CE + appointment tracker; suitability documentation template.

## Red flags
- Selling a line/state you're not appointed/licensed for.
- Replacement with no comparison or client benefit shown.
- Annuity/life sale with no suitability record.

## Verification
- [ ] License + carrier appointment + CE current
- [ ] Suitability basis documented (life/annuity/LTC)
- [ ] Replacement notices delivered where applicable
- [ ] Fees/surrender/conflicts disclosed
- [ ] E&O active; records retained

---
Part of **deciqAI Knowledge Skills**. Core method: [checklist](../checklist/SKILL.md).
