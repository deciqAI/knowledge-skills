---
name: representativeness-heuristic
description: "Activate when: user says 'this person/startup looks like a winner', 'I know one when I see it', 'they have the profile of a great hire', 'this reminds me of [famous success]', or any judgment where a vivid profile drives a probability estimate without an explicit base rate. Also activate when auditing for the conjunction fallacy or when pattern-matching is cited as the basis for a high-stakes decision.
  Do NOT activate when: probability is computed directly from data with no narrative element; base rate and profile have already been reconciled via explicit Bayesian reasoning."
---

# Representativeness Heuristic

## Overview

The **representativeness heuristic** is judging probability by how closely something resembles a prototype — overriding actual base rates. Named by Tversky & Kahneman (1972); produces three systematic errors: base rate neglect, the conjunction fallacy (A-and-B feels more likely than A), and insensitivity to sample size.

Composes with [`bayesian-reasoning`](../bayesian-reasoning/SKILL.md) (restores the prior), [`survivorship-bias`](../survivorship-bias/SKILL.md) (failures are invisible in the prototype), [`confirmation-bias`](../confirmation-bias/SKILL.md), and [`anchoring`](../anchoring/SKILL.md).

## When to Use

- Evaluating candidates, screening investments, or persona-based product decisions
- Any probability judgment where a vivid profile or narrative is present
- When "she/he/it looks like X" drives a decision without a stated base rate
- Auditing for the conjunction fallacy (more specific = seemingly more likely)

**Not when:** judgment is purely quantitative; base rate and profile align and Bayesian updating has been done explicitly.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete judgment → audit for base rate neglect and conjunction fallacy immediately.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: we judge probability by similarity to a prototype, which feels like reasoning but ignores base rates.
2. Check fit: is a vivid profile driving the judgment? Is a base rate available but being ignored?
3. Elicit their real case: what is the judgment, what profile is driving it, what is the actual base rate?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time: state base rate → apply Bayesian update → decompose any conjunction.
> **[WAIT — do not advance until user responds]**
5. Close by naming the calibrated probability that replaced the prototype-matching estimate.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify judgment + profile:** What probability estimate is being made? What profile information is driving it?

**Step 2 — Reference class + base rate:** What is the base rate of this outcome in the relevant reference class? Was it stated before the profile assessment? (If N while a profile is present, representativeness is active.)

**Step 3 — Conjunction test:** Does the judgment involve multiple attributes (X and Y and Z)? P(A AND B) ≤ P(A). If the conjunction was rated more probable than a component, the conjunction fallacy is active.

**Step 4 — Bayesian correction:** Prior (base rate) × Likelihood ratio → Posterior. Never start from the profile; always start from the base rate.

**Step 5 — Prototype audit:** Was the prototype built from survivorship-biased examples? What did failures that matched this prototype look like?

**Step 6 — Calibrated output:**
```
Base rate: [X%] | Profile adjustment: [direction + magnitude] | Corrected estimate: [Y%]
Conjunction (if applicable): P(A AND B) ≤ [Z%]
Recommendation: proceed / do not proceed / gather more data
```

*→ Method in Action: [Tversky & Kahneman 1972 + 1983 — The Linda Problem](examples/tversky-kahneman-1972-1983-the-linda-problem.md) · [The Hot Hand in Basketball](examples/gilovich-vallone-tversky-1985-the-hot-hand-in-basketball.md)*

## Pack: Representativeness Across Domains

| Domain | Prototype trigger | Base rate ignored | Correction |
|---|---|---|---|
| VC screening | Founder matches "winner" archetype | 75–90% of startups fail | State failure base rate before profile |
| Hiring | Candidate looks like top performers | 50–70% of hires underperform | Structured assessment replacing holistic match |
| Customer persona | "Target customer = power user" | Actual distribution is wide | Segment by behavior data, not persona |
| Product launch | "This looks like Slack / Airbnb" | Analogous success rate < 10% | State success rate for the category explicitly |

## Applying It Well

- State the base rate **before** assessing the profile — never after
- Treat profile as evidence that updates a prior, not as the primary input
- Audit every prototype for survivorship bias: what did the failures look like?
- When a conjunction is involved, decompose it — each added attribute reduces joint probability

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Rationalization | Reality |
|---|---|
| [D] "He just has the DNA of a founder — I know one when I see one." | Representativeness at maximum activation. What is the base rate for "looks like a winner" actually winning? |
| [D] "This is exactly the profile of a successful hire." | Profile built from visible successes. How many with this profile failed? Never checked. |
| [D] "She's a bank teller AND deeply committed to the cause." | Conjunction stated. P(A AND B) ≤ P(A). Narrative fit is not probability. |
| [D] "Every great company looked like this in the early days." | Survivorship bias generating the prototype. How many that looked like this failed? |
| [D] "I've seen this pattern before — it always plays out the same way." | How many times did a similar pattern occur and play out *differently*? |
| [D] "The more I learn about her, the more I'm convinced." | Added detail increases coherence, not probability. Each condition decreases joint probability. |
| [D] "I trust my gut — I've been doing this for 20 years." | Accumulates calibration error, not correction, without structured feedback loops. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Probability judgment driven by vivid narrative with no explicit base rate
- Conjunction of positive attributes treated as more likely than any single attribute
- Prototype drawn entirely from visible successes; failure base rates never checked
- "Pattern recognition" cited without stating the pattern's historical hit rate

## Verification

- [ ] Reference class defined and base rate stated **before** profile assessment
- [ ] Conjunction decomposed; no conjunction rated more probable than its least probable component
- [ ] Prototype audited for survivorship bias
- [ ] Bayesian update applied: prior × likelihood → posterior
- [ ] Final estimate anchored to base rate, not profile similarity

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/representativeness-heuristic?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=representativeness-heuristic** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
