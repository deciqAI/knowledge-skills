---
name: thought-experiment
description: "Activate when: user says 'what if,' 'let's reason through this,' 'imagine that,' or 'thought experiment'; a strategic decision is too risky or irreversible to test empirically; someone wants to refute a claim by reasoning rather than data; hidden assumptions in a business model need surfacing; counterfactual or ethical analysis is requested. Do NOT activate when: the question can be empirically tested at reasonable cost; time pressure makes structured reasoning impractical."
---

# Thought Experiment

## Overview

A thought experiment is structured reasoning: construct a scenario, trace logical consequences of explicit premises, examine the result for contradiction, hidden assumptions, or new hypotheses. Not vague speculation — formal procedure with defensible steps.

Galileo (1638) refuted 2000 years of physics without climbing any tower. Einstein (1905) derived special relativity by asking what he'd see riding alongside a light beam. For founders, thought experiments substitute for A/B tests when stakes are too high or actions are irreversible.

Composes with [`first-principles`](../first-principles/SKILL.md), [`inversion`](../inversion/SKILL.md), [`abductive-reasoning`](../abductive-reasoning/SKILL.md), [`premortem`](../premortem/SKILL.md).

## When to Use

- Strategic decisions too high-stakes or irreversible to test empirically
- Refuting claims that rest on premises you suspect are wrong
- Surfacing hidden assumptions in business models or strategies
- Counterfactual, ethical analysis, or scenario planning for long-horizon decisions

**Not when:** empirical testing is feasible at reasonable cost; premises are deeply contested; time pressure makes structured reasoning impractical.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete question → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: when you can't test empirically, set up an explicit premise, reason through consequences, watch for contradiction or surprise.
2. Check fit: if the question can be empirically tested at reasonable cost, do that instead.
3. Elicit the question and candidate premises from the user.
> **[WAIT — do not advance until user responds]**
4. Work through The Process one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight uncovered and its reliability caveat.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Frame:** question being reasoned about | why it can't be tested | type of useful conclusion (refute / surface assumption / generate hypothesis).

**Step 2 — Premises:** main premise | auxiliary premises (surface unstated ones) | most-controversial premise.

**Step 3 — Reason step by step:** each step follows from prior premises by a named inference rule; each step defensible in isolation.

**Step 4 — Examine conclusion:** contradiction? (one premise is wrong — identify which) | surprising implication? (points to hidden assumption) | new hypothesis? (make explicit, design test).

**Step 5 — Reliability check:** premises empirically true? | inference steps logically valid? | unconscious auxiliary premises? | thoughtful skeptic's likely hole?

**Step 6 — Apply:** refuted claim → abandon or revise | surfaced assumption → now explicit, can be tested | new hypothesis → design follow-up. Document so conclusion is recoverable.

## Output Template
```
# Thought Experiment: <question>
Premises: [main] | [auxiliary] | [most-controversial]
Reasoning: Step 1 → Step 2 → ... → Step n
Conclusion: [result] — contradictory / surprising / new hypothesis
Reliability: premise confidence | reasoning rigor | hidden assumptions surfaced | skeptic's hole
Application: what follows | next step
```

*→ Method in Action: [Galileo + Einstein + Strategic Applications](examples/galileo-einstein-strategic-applications.md) · [Rawls's Veil of Ignorance](examples/rawls-veil-of-ignorance.md)*

## Pack: Domain Patterns

| Domain | Thought experiment | What it surfaces |
|---|---|---|
| Strategy | "If we 10x'd our customer base, what breaks?" | Scalability constraints |
| Pricing | "If we charged 0 / 10x, who still buys?" | Segments, value capture |
| Competition | "If a $100M competitor copied us exactly, what protects us?" | Real moat |
| Product | "If we removed our most-loved feature, what happens?" | Actual value drivers |
| Ethics | "If everyone did this, what would the world look like?" | Universalizability |

## Applying It Well

- Discipline lives in the premises — garbage in, garbage out.
- Surprise in the conclusion signals a hidden assumption — that's the finding.
- Use when empirical testing is impossible or too costly; not a replacement for real data.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "It's just hypothetical; what does it matter?" | Galileo refuted 2000 years of physics through pure hypothetical. |
| [D] "My intuition tells me X" | Thought experiments are how you check intuition — run it. |
| [D] "Real-world is too complicated" | Reasoning hinges on a small number of structural features; thought experiments isolate those. |
| [D] "We need data" | Yes, when available. This is the available rigor when data isn't. |
| [D] "It will produce the answer I want" | Rigorous construction produces conclusions you didn't expect — that's the point. |
| [D] "The premises are obvious" | Stating them explicitly usually reveals they aren't. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Strategic decision made without thought experiments to test it
- "What if X?" reasoning dismissed as speculation
- Empirically untestable claim treated as established
- Surprising thought-experiment conclusion rationalized away

## Verification

- [ ] Premises are explicit and minimally controversial
- [ ] Each reasoning step is defensible
- [ ] Conclusion examined for inconsistency, surprise, or new hypothesis
- [ ] Hidden assumptions surfaced and made explicit
- [ ] Thoughtful skeptic's likely critique pre-empted
- [ ] Premise reliability acknowledged; application documented

---

*Part of **deciqAI Knowledge Skills** — 225 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/thought-experiment** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
