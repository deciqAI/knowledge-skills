---
name: status-quo-bias
description: "Activate when: user says 'we've always done it this way', 'changing now would be too disruptive', or 'no one is complaining so why change'; a team is slow to adopt a clearly better option; someone frames inaction as safe when omission carries real costs; you are designing enrollment/default settings and need to choose opt-in vs opt-out.
  Do NOT activate when: the status quo was explicitly evaluated and confirmed optimal (correct analysis, not bias); primary driver is risk aversion over outcomes (use loss-aversion-prospect-theory). More: deciqai.com/s/status-quo-bias"
---

# Status Quo Bias

## Overview

**Status quo bias** is the systematic preference for the current state over available alternatives — even when alternatives are objectively superior by the person's own values. "Doing nothing" is an active decision to accept the current state with real opportunity costs, not a non-choice. Coined by Samuelson & Zeckhauser (1988). Organ donation consent rates of 4–99% across European countries differ almost entirely by whether the default is opt-in or opt-out.

Two directions: (1) **Design** — choose defaults that serve user interests, not historical accident; (2) **Audit** — recognize when you are defaulting rather than actively choosing. Composes with [`endowment-effect`](../endowment-effect/SKILL.md), [`loss-aversion-prospect-theory`](../loss-aversion-prospect-theory/SKILL.md), [`inversion`](../inversion/SKILL.md), [`first-principles`](../first-principles/SKILL.md).

## When to Use

- A strategy, product, vendor, or policy has been in place without explicit re-evaluation
- Team says "we've always done it this way" or "changing now would be disruptive"
- A product or system default needs to be designed or redesigned
- Decision-maker is "leaning toward no change" but cannot articulate a positive case for the status quo
- Benefits elections, 401(k) enrollment, subscription renewals, or governance votes are being designed
- An organization is deferring AI adoption — defaulting to incumbent SaaS/vendors or existing workflows over AI-native alternatives, or waiting on AI capex/adoption decisions — and framing the delay as prudence

**Not when:** status quo was explicitly evaluated and found optimal; primary mechanism is risk aversion (use [`loss-aversion-prospect-theory`](../loss-aversion-prospect-theory/SKILL.md)).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete decision or design problem → run The Process directly.
- **Coach mode:** user is encountering organizational inertia or is new to the framework → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: "doing nothing" is a choice to accept the current state with real costs.
2. Check fit: is the option retained because it was actively evaluated as best, or because changing requires effort?
3. Elicit structure: what is the status quo, alternatives, who controls the default, cost of inaction?
> **[WAIT — do not advance until user responds]**
4. Run fresh-choice test: would you choose this today if starting fresh? What is the explicit opportunity cost of not changing?
> **[WAIT — do not advance until user responds]**
5. Close: bias identified + fresh-choice reframe applied + default redesigned or active decision made.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify default:** Current state · who controls it · how established · how long without re-evaluation.
**Step 2 — Identify alternatives:** List alternatives · why not adopted · substantive cost vs. inertia?
**Step 3 — Fresh-choice test:** Which option would you choose starting from scratch today? Gap from status quo? Switching cost estimate · net value of better alternative minus switching cost.
**Step 4 — Cost of inaction:** Annual cost of status quo over optimal · over 3 years · break-even switching point · is the status quo deteriorating?
**Step 5 — Direction:** Design (what default serves average user?) or Audit (override / accept with justification / redesign)?
**Step 6 — Implement:** Change plan · timeline · ownership · review date.

## Output: Status Quo Audit

```markdown
# Status Quo Audit: <decision / system / default>
Status quo: | Alternatives: | Fresh-choice result:
Inertia vs. cost share: | Switching cost: | Cost of inaction (1yr / 3yr):
Default design justification: | Decision: [ ] Override [ ] Accept [ ] Redesign | Review date:
```

*→ Method in Action: [Samuelson & Zeckhauser 1988 + Johnson & Goldstein 2003](examples/samuelson-zeckhauser-1988-johnson-goldstein-2003.md) · [NJ–PA Auto Insurance Defaults](examples/new-jersey-pennsylvania-auto-insurance-defaults.md)*
*→ 2026 lens: [Enterprise AI Adoption and the Incumbent-Vendor Default (2023–2026)](examples/enterprise-ai-adoption-incumbent-default-2023-2026.md)*

## Pack: Status Quo Bias Across Domains

| Domain | Default lever | Audit question |
|---|---|---|
| SaaS / subscription | Opt-out cancellation default | Would we re-subscribe at today's price if starting fresh? |
| 401(k) / retirement | Automatic enrollment at a sensible rate | Has this employee ever actively reviewed their allocation? |
| Product privacy / security | Default to what user would want if informed | What would users choose if onboarding required an active choice? |
| Board governance / vendor / team | Explicit review triggers in founding docs | Would we choose these terms / this vendor / this person today from scratch? |

## Applying It Well

Ask the fresh-choice question systematically for any persistent arrangement. Design defaults with explicit intent and a stated justification. Use opt-out structures for high-social-value behaviors (organ donation, 401(k), safety settings). Set a review date whenever a default is maintained to prevent it becoming the next unexamined default.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Rationalization (Fake Move) | Reality |
|---|---|
| [D] "If it ain't broke, don't fix it" | Applies only when the status quo has been actively evaluated and found optimal. Most uses avoid an evaluation entirely. |
| [D] "The switching costs are too high" | Frequently overestimated by the person who would manage the change. Model it explicitly before accepting as decisive. |
| [D] "We've always done it this way" | Historical persistence is a description of inertia, not a justification. |
| [D] "Change would be disruptive right now" | "Right now" is always now. Disruption costs must be weighed against the ongoing cost of the inferior status quo. |
| [D] "No one is complaining about it" | Absence of complaint means friction to complain exceeds dissatisfaction, not that users are satisfied. |
| [D] "Our default settings reflect what most users want" | Unless tested with active-choice design, the default reflects what most users don't actively change. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- A policy, product, vendor, or team has not been re-evaluated in more than two years
- Switching costs cited to justify inaction without being explicitly modeled
- The question "would we choose this from scratch?" has never been asked about a persistent arrangement
- Opt-in enrollment used for a behavior that clearly serves user interests (retirement savings, safety settings)

## Verification

- [ ] Fresh-choice question asked: "would we choose this if deciding from scratch today?"
- [ ] Switching costs explicitly modeled (not just cited as "too high")
- [ ] Cost of inaction quantified over 1–3 years
- [ ] For default design: justification for the chosen default stated explicitly
- [ ] Review date set to prevent new state from becoming next unexamined default
- [ ] Stop-rule: if status quo was found optimal by active evaluation, documented as such (not bias)

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/status-quo-bias** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/status-quo-bias.json*
