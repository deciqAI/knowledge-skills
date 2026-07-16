---
name: jobs-to-be-done
description: "Activate when: user says 'customers aren't switching to us even though we're better,' 'our churn surveys aren't predicting who actually leaves,' 'we're debating features instead of what the customer actually needs,' 'who is our real customer,' or mentions 'JTBD / jobs to be done / what are they hiring this for.'
  Do NOT activate when: product is a commodity with no job-level differentiation (electricity, raw materials); purchase is driven entirely by regulatory/legal compliance with no real customer choice. More: deciqai.com/s/jobs-to-be-done"
---

# Jobs to Be Done (JTBD)

## Overview

People don't buy products — they **hire** products to do a job (make progress in a specific circumstance, across functional, emotional, and social dimensions). Customers switch when a new hire does the job better; they churn when your product stops serving the job. Developed by Christensen, Moesta, and Taddy Hall; codified in *Competing Against Luck* (2016). Rooted in Levitt's 1960 insight: "People don't want a quarter-inch drill, they want a quarter-inch hole."

Composes with [`pmf-crossing-the-chasm`](../pmf-crossing-the-chasm/SKILL.md), [`mvp`](../mvp/SKILL.md), [`switching-costs`](../switching-costs/SKILL.md), [`first-principles`](../first-principles/SKILL.md).

## When to Use

- Product is technically excellent but customers don't switch from incumbents
- Demographic segmentation produces segments that don't behave alike
- Churn is high but exit surveys don't predict it; roadmap debate is feature-vs-feature
- New market entry: "who is our customer" instead of "what job"
- Building an AI-native product or "AI wrapper": are users hiring us for output/features, or for progress (get unblocked, ship faster) — and are we losing to AI adoption, the base model's own app, or non-consumption?

**Not when:** commodity; regulatory-compliance purchase; org buyer with different motivations than end-user.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete product/customer case → run The Process directly.
- **Coach mode:** unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: people hire products to do a job — the competitor set is *everything* the buyer considered, not just your category.
2. Check fit: commodity / regulatory-buy / no-choice → not this lens.
3. Elicit the real product and customer behavior they're trying to understand.
> **[WAIT — do not advance until user responds]**
4. One question at a time: what job is the customer hiring this for? what circumstance? what did they hire before?
> **[WAIT — do not advance until user responds]**
5. Close: job statement + the non-obvious competitor they're actually choosing between.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State product + assumed customer** (starting point; will be dismantled).

**Step 2 — Switch Interviews.** Interview recent switchers to/from your product. Reconstruct the switching moment: (1) First thought — when did you first realize you needed something different? (2) Circumstance — what was going wrong? (3) What else did you consider? (4) Push — what was actively wrong with the old? (5) Pull — what attracted the new? (6) Anxiety — what almost stopped you? (7) Habit — what behavior had to change? (8) First use — how did you feel?

**Step 3 — Extract job statement:** *When [circumstance], I want to [motivation], so I can [outcome].*

**Step 4 — Identify actual competitor set:** Direct (same category) / Adjacent (different category, same job) / Non-consumption (do nothing) / Surprising non-obvious.

**Step 5 — Map all three dimensions:** Functional (practical task) / Emotional (how they want to feel) / Social (how they want to be seen).

**Step 6 — Diagnose churn or wins:** Churn: what job? what did they hire instead? what did the new hire do better? Wins: what did they fire? what became unbearable? what anxiety was overcome?

**Step 7 — Design from the job.** Every feature: does it help progress in the specific circumstance? does it serve functional/emotional/social dimensions? does it reduce Push/Pull/Anxiety/Habit barriers?

## Output Template
```
JTBD Analysis: <product>
Job statement: When [circumstance], I want to [motivation], so I can [outcome].
Competitor set: Direct / Adjacent / Non-consumption / Surprising
Dimensions: Functional / Emotional / Social
Forces of progress: Push / Pull / Anxiety / Habit
Implications: Features to build / cut / Marketing angle / Competitive set to track
```

*→ Method in Action: [Christensen and the Milkshake Study, 2003](examples/christensen-and-the-milkshake-study-2003.md)*

*→ 2026 lens: [What People Hire an AI Assistant to Do (2023–2026)](examples/what-people-hire-an-ai-assistant-to-do-2023-2026.md)*

## Pack: Common JTBD Patterns

| Domain | Job shape | Non-obvious competitor |
|---|---|---|
| Productivity SaaS | "Under deadline, make artifact look credible to boss" | Boss not asking; meeting cancelled |
| Consumer food | "Tired after work, feed kids without feeling like failure" | Ordering delivery; cereal |
| Banking/fintech | "Worried about money, feel like I have a plan" | Calling a parent; not checking balance |
| Dating apps | "Lonely Tuesday night, feel like there are possibilities" | Re-watching a show; texting an ex |

## Applying It Well

- Customers articulate the job reliably; they cannot reliably predict which features serve it. Ask "what were you trying to accomplish when you switched?" not "what should we build?"
- The most dangerous competitor is usually outside your category — a different way of doing the job, or non-consumption.
- Most products serve 3-7 distinct jobs. Discovering the second and third explains cohort behavior differences.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We surveyed customers and they want X feature" | Customers articulate jobs, not features. Re-interview using Switch methodology. |
| [D] "Our customer is millennials / mid-market companies" | Demographic categories are not jobs. Same person has 5 different jobs across her day. |
| [D] "We don't have competitors" | Every job has alternatives, including non-consumption. Can't name the competitor = don't understand the job. |
| [D] "JTBD is just user-needs research" | User-needs lists features; JTBD reconstructs the switching moment. Different output. |
| [D] Treating the job as functional only | Emotional and social dimensions are where premium pricing and brand loyalty live. |
| [D] Skipping Switch Interviews because "we already know" | If you can't name Push/Pull/Anxiety/Habit for 10 recent switchers, you don't already know. |
| [D] Treating churn as "they lost interest" | Customers fire your product because something else does the job better. Identify the new hire. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Segmentation is purely demographic; competitor set lists only same-category products
- Roadmap features justified by "customers asked" without job context
- Churn analysis stops at "less engaged" instead of identifying the new hire
- Job statements without a circumstance; functional dimension only; no Switch Interview ever run

## Verification

- [ ] 5-10 Switch Interviews conducted (not feature surveys)
- [ ] Job statement: When/I want to/So I can with explicit circumstance
- [ ] Functional, emotional, social dimensions named
- [ ] Competitor set includes adjacent, non-consumption, and surprising alternatives
- [ ] Push, Pull, Anxiety, Habit forces identified
- [ ] Product implications derived from the job; primary job chosen if multiple exist

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/jobs-to-be-done** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/jobs-to-be-done.json*
