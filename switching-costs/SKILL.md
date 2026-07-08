---
name: switching-costs
description: "Activate when: user asks why customers don't switch to a better product, how to make a product stickier or build a moat, how to compete against an entrenched incumbent, why churn is low but revenue growth stalled, or mentions lock-in / vendor lock-in / stickiness / data moat / Klemperer.
  Do NOT activate when: the product is a one-shot transaction with no ongoing relationship, or the user is designing adversarial lock-in and needs ethical pushback first."
---

# Switching Costs

## Overview

Switching costs are everything a customer must pay, learn, redo, or risk to move from one product to another — financial, learning, data migration, integration, process, relational, and risk premium. They are routinely larger than founders model and customers anticipate at purchase time.

When switching costs are high, incumbents retain customers even when competitors offer better products, and new entrants must offer dramatically more value to break even. Paul Klemperer formalized this in 1987 (*QJE* 102(2)). IBM's 25-year mainframe dominance is the canonical empirical case.

Composes with [`network-effects`](../network-effects/SKILL.md), [`signaling-games`](../signaling-games/SKILL.md), [`anchoring`](../anchoring/SKILL.md), and [`pmf-crossing-the-chasm`](../pmf-crossing-the-chasm/SKILL.md).

## When to Use

- Building a product and want to design defensible switching costs into it
- Evaluating investment: does incumbent switching cost make the market unwinnable for new entrants?
- New entrant trying to win customers from an incumbent; need strategy around actual cost magnitudes
- Incumbent experiencing churn; need to diagnose which switching-cost component is broken
- Someone says: "lock-in," "vendor lock-in," "stickiness," "data moat," "Klemperer"

**When NOT to use:** one-shot transactions; markets with strict regulatory equivalence; rationalizing adversarial lock-in.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: switching costs are everything a customer must pay, learn, redo, or risk to change products — usually much larger than either side models, which is why incumbents stay incumbents.
2. Check fit against When to Use / When NOT to use. If one-shot transaction, redirect.
3. Elicit their real situation: which market, which product, which role (incumbent or new entrant)?
> **[WAIT — do not advance until user responds]**
4. Work through the 7 types one at a time with their input. Estimate magnitude in dollars/hours.
> **[WAIT — do not advance until user responds]**
5. Close by naming the specific move: a product design decision, an entry strategy, or a retention insight.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Switching-Cost Audit**.

### Step 1: Identify all seven types

Seven types: **1. Financial** (termination fees, lost prepaid) · **2. Learning** (relearning interface/workflows) · **3. Data migration** (export, reformat, lost history) · **4. Integration** (SSO, CRM, scripts — all must be redone) · **5. Process/workflow** (docs, runbooks, training) · **6. Relational/network** (workspaces, orgs, shared docs) · **7. Risk/uncertainty** (risk premium on unknown product, often 2-5x risk-neutral).

```markdown
| Type            | Concrete cost                   | Estimated magnitude |
|-----------------|---------------------------------|---------------------|
| Financial       | termination fee, unused prepaid | $______             |
| Learning        | hours × $/hr × # users          | $______             |
| Data migration  | labor + lost data value         | $______             |
| Integration     | # integrations × redo cost      | $______             |
| Process/workflow| docs rewrite + training         | $______             |
| Relational      | disrupted relationships         | qualitative         |
| Risk premium    | discount rate on new product    | %                   |
| **Total**       |                                 | $______ + qualitative|
```

### Step 2: Asymmetry analysis

Cost to stay = renewal price. Cost to switch = sum above. Years-to-recoup = switching cost ÷ annual value differential. If years-to-recoup > customer planning horizon (2-3 yr B2B SaaS, 5+ enterprise), rational decision is to stay even when the new product is better.

### Step 3: For incumbents — design defensible switching costs

**Extraction-focused** (long contracts, data export restrictions): customers resent it; mass churn when alternatives appear. **Value-focused** (rich integrations, accumulated data history, custom workflows): customers rationalize it; costs compound. Choose value-focused. Design moves: accumulate customer-specific data; reward integration investment; build multi-level relationships.

### Step 4: For new entrants — four strategies

**A** Target greenfield. **B** Offer 3-10x more value at lower price. **C** Absorb the switching cost (free migration, training, integration). **D** Find a segment where incumbent switching costs don't apply (different scale, use case, industry).

*→ Method in Action: [Klemperer's Foundational Theory and IBM Mainframe Lock-in](examples/klemperers-foundational-theory-and-ibm-mainframe-lock-in.md) · [US Wireless Number Portability](examples/us-wireless-number-portability-2003.md)*
## Pack: Switching Costs by Category

| Category | Dominant type | Magnitude |
|---|---|---|
| Enterprise CRM (Salesforce) | Learning + integration + data | $50k-$500k |
| Cloud infra (AWS) | Integration + risk premium | 6-18 months engineering |
| Financial terminals (Bloomberg) | Learning + relational | $20k+ per trader |
| Healthcare EHR (Epic) | Integration + workflow + compliance | $10-100M/hospital |
| ERP (SAP, Oracle) | Process/workflow + integration | $50M+ large enterprise |
| Consumer social media | Relational + content history | High; main retention driver |

*→ Primary sources: [references/sources.md](references/sources.md)*
## Applying It Well

Estimate magnitudes in concrete units. Compute the asymmetry (cost to stay vs. cost to leave) — it is the most important single number. Value-focused integration depth compounds; extraction-focused lock-in decays. Model technological bypass risk: moats break via bypass, not direct competition.
## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Better product will win customers" | Only if value differential > switching cost; typically 3-10x needed, not 20% better |
| [D] "Design extraction-focused lock-in" | Produces resentment; mass churn when alternatives appear; value-focused compounds instead |
| [D] "We let customers leave anytime = no switching costs" | Learning + integration + risk premium still apply; often larger than contractual lock-in |
| [D] Treating switching costs as fixed market property | Cloud + open APIs lower them; generational tech shifts change the substrate |
| [D] Skipping magnitude estimation | Without dollar figures, no strategic decision is possible |
| [D] Confusing retention with switching costs | Love-the-product vs. no-alternative vs. high-cost have different strategic implications |
| [D] New entrant underestimates incumbent's costs | Base CAC on customers who say "I would never switch," not "I might switch" |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "We have a moat" without specifying which costs and magnitudes · Costs presented as uniformly large (they vary 5-10x by customer size) · Extraction-focused lock-in treated as defensibility · New-entrant strategy assumes feature parity is sufficient · No bypass-risk analysis

## Verification

- [ ] All 7 types identified · magnitudes in concrete units · asymmetry computed
- [ ] If incumbent: extraction-focused vs. value-focused choice made explicitly
- [ ] If new entrant: strategy A/B/C/D selected with math supporting it
- [ ] Technological bypass risk considered

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/switching-costs?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=switching-costs** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
