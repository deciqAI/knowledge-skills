---
name: estimated-tax-safety-buffer
description: "Activate when: self-employed / K-1 / variable-income client planning quarterly 1040-ES; 'how much should I set aside?', 'will I owe a penalty?', volatile income year. Do NOT activate when: W-2 withholding fully covers liability. More: deciqai.com/s/estimated-tax-safety-buffer"
---

# Tax Prep — Estimated-Tax Safe-Harbor Buffer

> **Industry front door for [margin-of-safety](../margin-of-safety/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not legal or tax advice.** Confirm safe-harbor percentages against current IRC §6654/§6655.

**Activate when:** self-employed / K-1 / variable-income client planning quarterly 1040-ES; "how much should I set aside?", "will I owe a penalty?", volatile income year.
**Do NOT activate when:** W-2 withholding fully covers liability.

## Why this variant
The parent [margin-of-safety](../margin-of-safety/SKILL.md) sizes a buffer against estimation error. Estimated taxes are exactly that: pay enough to clear a **safe harbor** so a bad income estimate never triggers an underpayment penalty. The safe harbor *is* the margin of safety.

## Domain inputs → parent's Process
- Floor = safe harbor: generally 90% of current-year tax **or** 100% of prior-year (110% if prior AGI > $150k).
- Buffer sizing: pay to the *higher-certainty* harbor (prior-year is known; current-year is a guess).
- Volatility: for lumpy income, use annualized-income installment method rather than flat quarters.

## Worked example
Consultant, prior-year tax $40k, this year wildly up.
→ Safe harbor = 110% × $40k = $44k across 4 quarters removes penalty risk regardless of how high this year lands. That is the margin of safety; anything above is optional smoothing.

## Packs
- **Solo:** default clients to prior-year safe harbor; revisit at Q3 if income spikes.
- **Advisory:** annualized method for seasonal/lumpy earners.

## Red flags
- Estimating current-year liability precisely and paying to it (no buffer) → penalty on any upside miss.
- Ignoring the 110% high-AGI threshold.

## Verification
- [ ] Safe-harbor floor computed (higher-certainty basis)
- [ ] High-AGI 110% applied if relevant
- [ ] Annualized method considered for lumpy income
- [ ] Quarterly reminders set (see deadline engine)

---
Part of **deciqAI Knowledge Skills**. Core method: [margin-of-safety](../margin-of-safety/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/estimated-tax-safety-buffer** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/estimated-tax-safety-buffer.json*
