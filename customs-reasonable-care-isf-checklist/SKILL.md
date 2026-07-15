---
name: customs-reasonable-care-isf-checklist
description: "Activate when: filing an entry or ISF; onboarding an importer (POA); building the compliance file; 'did we file ISF in time?', 'is our reasonable-care record complete?'. Do NOT activate when: the shipment is exempt and no entry/ISF is required."
---

# Customs — Reasonable Care & ISF Compliance Checklist

> **Industry front door for [checklist](../checklist/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not legal advice.** Verify against current 19 CFR and CBP guidance.

**Activate when:** filing an entry or ISF; onboarding an importer (POA); building the compliance file; "did we file ISF in time?", "is our reasonable-care record complete?"
**Do NOT activate when:** the shipment is exempt and no entry/ISF is required.

## Why this variant
The parent [checklist](../checklist/SKILL.md) is a verifiable gate. Customs entry is a **reasonable-care** obligation with hard filing clocks (ISF) and 5-year recordkeeping. This maps those duties onto the parent's gate.

## Domain inputs → parent's gate
- **ISF (10+2):** importer security filing transmitted no later than **24 hours before lading** (ocean); update as info changes.
- **Entry data:** classification, valuation, origin, quantity — each supported and documented (reasonable care).
- **POA:** valid power of attorney + importer identity (KYC) on file.
- **PGA:** any FDA/USDA/EPA/other agency data flagged and filed.
- **Recordkeeping:** entry records retained **5 years** from date of entry.

## Worked example
New importer, ocean shipment, mixed goods, one FDA-regulated item.
→ Gate: ISF must transmit ≥24h pre-lading (late = liquidated damages up to $5k/violation); the FDA item needs prior notice + PGA data; POA + reasonable-care file must exist before entry. Any gap = do not file until cleared.

## Compliance anchors
- 19 CFR 149 (ISF); 19 U.S.C. 1484/1485 reasonable care; 19 CFR 163 recordkeeping (5 yrs); PGA requirements.

## Packs
- **Solo broker:** per-importer compliance folder template.
- **Brokerage:** ISF timing alerts into the deadline engine; PGA triage.

## Red flags
- ISF filed inside the 24-hour window.
- Valuation/classification with no supporting record.
- PGA-regulated goods entered without agency data.

## Verification
- [ ] ISF transmitted ≥24h before lading; updated on change
- [ ] Entry data supported & documented (reasonable care)
- [ ] Valid POA + importer KYC on file
- [ ] PGA requirements identified and met
- [ ] 5-year recordkeeping started

---
Part of **deciqAI Knowledge Skills**. Core method: [checklist](../checklist/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/customs-reasonable-care-isf-checklist** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
