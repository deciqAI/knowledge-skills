---
name: customs-origin-usmca-decision
description: "Activate when: determining country of origin; testing USMCA (or other FTA) preference eligibility; marking; 'does this qualify for duty-free?'; goods with multi-country inputs. Do NOT activate when: wholly-obtained single-country goods with no preference question."
---

# Customs — Country of Origin & USMCA Qualification

> **Industry front door for [decision-tree](../decision-tree/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not legal advice.** Origin is rule-specific; verify against the current USMCA text and CBP guidance.

**Activate when:** determining country of origin; testing USMCA (or other FTA) preference eligibility; marking; "does this qualify for duty-free?"; goods with multi-country inputs.
**Do NOT activate when:** wholly-obtained single-country goods with no preference question.

## Why this variant
The parent [decision-tree](../decision-tree/SKILL.md) maps branching qualification logic. Origin/preference is a decision tree: wholly obtained? → tariff-shift met? → RVC threshold met? → de minimis? Each branch leads to duty-free, MFN, or special treatment.

## Domain inputs → parent's Process
Walk the branches:
- Wholly obtained/produced entirely in territory? → originates.
- Else: does each non-originating input meet the **product-specific rule** (tariff shift)?
- If not by shift: is **Regional Value Content** (transaction-value or net-cost) met?
- **De minimis** allowance for small non-originating value?
- Confirm certification of origin support + marking rules (substantial transformation for marking).

## Worked example
Assembly in Mexico using Chinese components.
→ Tree: check the PSR — do the Chinese inputs make the required tariff shift on assembly? If yes → USMCA-eligible with a valid certification; if no → test RVC/de minimis. Fails all → MFN duty + China Section 301 exposure. Document the path.

## Compliance anchors
- USMCA product-specific rules, RVC, de minimis; certification of origin recordkeeping; marking (19 CFR 134).

## Packs
- **Solo broker:** origin worksheet per product/BOM.
- **Brokerage:** supplier solicitation for origin certs; PSR library.

## Red flags
- Claiming preference without the PSR/RVC actually met.
- Confusing marking origin with preference origin.
- No supporting certification retained.

## Verification
- [ ] Wholly-obtained vs PSR path determined
- [ ] Tariff-shift / RVC / de minimis tested in order
- [ ] Valid certification support on file
- [ ] Marking origin assessed separately

---
Part of **deciqAI Knowledge Skills**. Core method: [decision-tree](../decision-tree/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/customs-origin-usmca-decision** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
