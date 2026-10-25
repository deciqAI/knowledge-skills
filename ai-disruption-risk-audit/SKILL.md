---
name: ai-disruption-risk-audit
description: "Activate when: user says 'will AI disrupt us?', 'which parts of our business will AI replace?', 'is our moat still there in the AI era?', 'run an AI impact assessment', or customers have started using AI tools to do work they used to pay us for, or an AI-native competitor has entered at a much lower price.
  Do NOT activate when: the question is only which AI tool to adopt for internal efficiency (no business-model question); the business has no formed value chain to break down; a transformation plan already exists and needs stress-testing (use premortem); the question is general disruption theory with no AI angle (use disruptive-innovation). More: deciqai.com/s/ai-disruption-risk-audit"
---

# AI Disruption Risk Audit


## Overview

AI does not hit a company evenly. Inside one business, some activities see their price collapse (they are commoditized) while others become scarcer and more valuable (they are reinforced). Research on AI's effect on work finds the same unevenness at task level: capability is a "jagged frontier," improving some tasks and worsening others of similar apparent difficulty (Dell'Acqua et al., 2023).

The core mechanism: **break the business into its value chain → score each activity for AI substitutability and cost collapse → judge whether customers can route around you → find where advantage migrates → decide hold / attack / retreat per activity.** The unit of analysis is the activity, not the company, because disruption arrives one activity at a time.

Compose with [value-chain-analysis](../value-chain-analysis/SKILL.md) (break into activities) · [disruptive-innovation](../disruptive-innovation/SKILL.md) (low-end and new-market entry) · [economic-moat](../economic-moat/SKILL.md) (what advantage remains) · [switching-costs](../switching-costs/SKILL.md) (can customers leave) · [second-curve](../second-curve/SKILL.md) (when to jump).

## When to Use

- Annual strategy or pre-fundraise review of AI's effect on core revenue
- Customer inquiries falling; customers building in-house or using general-purpose AI instead
- A competitor entering AI-native at a much lower price

**When NOT to use:** tool selection only · no formed business · a transformation plan already in execution (run [premortem](../premortem/SKILL.md) on the plan instead).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete business → run The Process directly.
- **Coach mode:** user is unfamiliar → guide one step at a time.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is:** "Break the business into activities and ask of each one: does AI make it cheaper, or scarcer? Then decide to hold, attack or retreat."
2. **Check fit:** "Which 2–3 pieces of work do customers actually pay you for?"
3. **Elicit the real case:** "List the 5–8 activities from winning a customer to delivering — who does each, and how much time it takes."
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "Here is a first substitutability and cost-collapse score for each activity. Correct it."
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "What gets disrupted is an activity, not the company. Advantage moves — follow it."

## The Process

**Output:** AI impact heat map + hold / attack / retreat action table

1. **Break down the value chain.** 5–12 activities, each tagged with its share of revenue or gross-margin contribution. *Gate: an activity that maps to no revenue or cost → merge it; no empty rows.*
2. **Score substitutability (1–5).** Is the output standardized, digitizable, verifiable? Can today's general-purpose AI produce it at a quality the customer accepts — **tested on real tasks, not imagined**?
3. **Score cost collapse (1–5).** How far does AI cut the cost of the activity against today's cost? Record the basis. *Gate: a score with no test result or price quote behind it → mark "unverified"; it does not enter the conclusion.*
4. **Score customer bypass risk.** Can customers do it themselves with AI? Check switching costs, trust and liability requirements, data access, regulation — and the distribution channel that brings customers to you. *Gate: high substitutability + low switching cost → red zone.*
5. **Find where advantage migrates.** When execution gets cheap, scarcity moves to: proprietary data, distribution and customer relationships, liability-bearing and compliance, integration into workflows, judgment and taste. For each, ask whether you actually own it — and whether AI can reproduce it too.
6. **Decide the action.** Red zone: **retreat** (re-price and bundle, or hand the activity to AI) or **attack** (rebuild it on AI yourself first and take share at the lower price). Reinforced activities: **hold** and invest more. Each row gets an owner, a metric and a 90-day milestone.
7. **Stop-rule:** most scores are "unverified" → run a 2-week test (AI on real tasks) before returning to Step 2.

**Output template:**
`activity | revenue share | substitutability | cost collapse | customer bypass risk | zone (red / amber / green / reinforced) | advantage migration point | action (hold / attack / retreat) | owner | 90-day metric`

*→ Method in Action: [Chegg and generative AI (2023–2025)](examples/chegg-generative-ai-2023-2025.md)*

## Applying It Well

1. **Test AI on real tasks.** Demo videos are not evidence; your own task samples are.
2. **Cannibalize yourself first.** If a red-zone activity's price is going to fall, it is better that you cut it than a new entrant.
3. **Score distribution, not just the product.** Customers can bypass you at the channel that delivers them as well as at the work itself.
4. **Re-score every 6 months.** Model capability moves fast; scores expire.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our industry is too complex for AI" | Complexity is usually several simple activities in sequence. Score each one. |
| [D] "Customers value the relationship; they won't switch" | A relationship protects the purchasing entry point and existing accounts — not the unit price, and not new-customer acquisition. |
| [D] "We'll wait until AI matures" | By the time it matures, a new entrant has already reset the price. |
| [D] "We'll AI-enable everything, so we're safe" | AI that everyone can use is not an advantage. The advantage is at the migration points. |
| [D] "Our proprietary content is the moat" | Test it: if a general model answers the same questions well enough, the content library is a red-zone activity, not a migration point. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Scores by gut feel, with no tests · cost scored but customer bypass not · distribution channel never scored
- Conclusion "limited impact" with no red-zone analysis · actions with no owner

## Verification

- [ ] Every activity maps to revenue or cost
- [ ] Substitutability and cost-collapse scores rest on tests or quotes; unverified scores excluded
- [ ] Customer bypass scored for the product and for the distribution channel
- [ ] Every red-zone row has hold / attack / retreat + owner + 90-day metric
- [ ] Next re-score date set

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ai-disruption-risk-audit** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ai-disruption-risk-audit.json*
