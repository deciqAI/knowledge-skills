---
name: freight-carrier-vetting-checklist
description: "Activate when: a freight broker is booking a carrier and must vet authority/insurance/safety before tendering a load; 'is this carrier legit', onboarding a new carrier, preventing fraud/double-brokering. Do NOT activate when: the carrier is an established, already-vetted partner with current records on file."
---

# Freight Broker — Carrier Vetting Checklist

> **Industry front door for [checklist](../checklist/SKILL.md).** Adds domain triggers, a worked example, and packs. The engine is the parent checklist skill; parent content unchanged.
> **Not legal advice.** Verify against current FMCSA rules and your broker authority/bond obligations.

**Activate when:** onboarding/booking a carrier; a load is about to be tendered; a carrier looks too cheap/too eager; rebuilding your carrier-vetting SOP.
**Do NOT activate when:** the carrier is a current, documented, insured partner.

## Why this variant
The parent [checklist](../checklist/SKILL.md) is a must-not-skip gate. Booking an unvetted carrier is how brokers get hit with cargo loss, double-brokering fraud, and liability. This maps the parent's gate onto carrier due diligence.

## Domain inputs → the checklist gate
- **Active authority**: FMCSA operating authority (MC/DOT) active, not revoked; broker vs carrier authority correct for the move.
- **Insurance**: cargo + auto liability on file, adequate limits, broker named as certificate holder, verified with the insurer (not just a PDF).
- **Safety**: FMCSA safety rating / SMS BASIC scores; out-of-service history.
- **Identity match**: phone/email/address match FMCSA record; watch VoIP + gmail + brand-new authority (fraud signals).
- **Double-brokering guard**: confirm the carrier hauling = the carrier booked; no re-brokering without consent.

## Worked example
Carrier quotes 30% under market, authority active 3 weeks, gmail contact, address = a UPS store.
→ Gate fails on identity + freshness fraud signals → do not tender; verify insurance directly with insurer and confirm equipment/driver before load.

## Compliance anchors
- FMCSA operating authority & insurance (49 CFR 387); broker surety bond (BMC-84/$75k); reasonable vetting standard.

## Packs
- **Solo broker**: 8-point pre-tender vetting card.
- **Brokerage**: automated FMCSA + insurance re-check on every booking (feed the deadline/monitor agents).

## Red flags
- Rate far below market; authority < 6 months; VoIP/gmail; address mismatch; reluctance to verify insurance.

## Verification
- [ ] Authority active + correct type
- [ ] Insurance verified with insurer, limits adequate
- [ ] Safety scores/OOS history reviewed
- [ ] Identity matches FMCSA; fraud signals cleared
- [ ] Double-brokering consent confirmed

---
*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/freight-carrier-vetting-checklist** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
