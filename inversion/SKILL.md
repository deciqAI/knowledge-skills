---
name: inversion
description: "Activate when: user says 'do a pre-mortem', 'what could go wrong', 'why might this fail', 'invert the question', 'what would have to be true for this to be a disaster'; a plan keeps generating enthusiasm with no risks named; an investment thesis sounds compelling but no one has named what would kill it; the decision is high-stakes or hard-to-reverse. Do NOT activate when: the decision is genuinely low-stakes and reversible (no meaningful downside to just trying); immediate crisis response is needed and there is no time for analysis."
---

# Inversion

## Overview

Most planning asks "how do I win?" and runs forward from there. Inversion runs the other way: "how could this fail catastrophically?" — then designs the plan around eliminating the failure paths that matter most. The work is not pessimism; it is **eliminating known ways to lose so you keep only the risks you can live with**.

This is one of four composable motions in the deciqAI collection: [first-principles](../first-principles/SKILL.md) decomposes *downward* to bedrock; [occams-razor](../occams-razor/SKILL.md) chooses *sideways* among competing accounts; [second-order-thinking](../second-order-thinking/SKILL.md) traces *forward* through time; **inversion** traces *backward from failure*. Compose freely — use inversion after a first-principles teardown, alongside a parsimony audit, or in parallel with a forward cascade as a failure cascade.

## When to Use

Apply when: decision is high-stakes or hard-to-reverse; enthusiasm is high but no risks named; someone says "pre-mortem," "what could go wrong," "why might this fail."

**When NOT to use:** reversible low-stakes calls; immediate crisis requiring action now; lack domain knowledge to enumerate plausible paths.

## Coaching Novices (Adaptive Front Door)

Two delivery modes: **Engine mode** — user has a concrete decision → run the full Audit directly. **Coach mode** — user signals unfamiliarity → guide one step at a time. When unsure: *"Want me to run this on a specific decision, or walk you through the method?"*

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output that step's question and nothing more.

1. **One-line what-it-is.** Flips "how do I win?" to "how could this fail catastrophically?" — eliminates load-bearing failure paths up front so you commit with eyes open.
2. **Check fit.** Match against *When to Use* / *When NOT to use*. If it doesn't fit, say so and point elsewhere.
3. **Elicit their real decision.** If no concrete case, ask for one. Never invert a hypothetical when a real decision is available.

> **[WAIT — do not advance until user responds]**

4. **One step at a time.** Force them to name 5–7 failure paths *in their own words* before classifying; rank together; design mitigations one at a time.

> **[WAIT — do not advance until user responds]**

5. **Close by naming the payoff.** Name the one failure path *they* had not seen — the new entry on their not-to-do list.

> **[WAIT — do not advance until user responds]**

## The Process

Run the **Inversion Audit**. Trace backward from failure, rank by load-bearing, then mitigate.

1. **State decision + measurable target outcome** ("12-month MAU ≥ 100K," not "the product succeeds").
2. **Invert:** "If this is a total failure by <date>, the most likely reasons are ___." Give explicit permission to speak badly of the plan.
3. **Enumerate failure paths (aim 5–10), uncharitably.** Do not filter. The paths you don't write down quietly survive.
4. **Classify and weight each:** P(occur) × Impact + category tag: Internal / External / Assumption failure / Timing.
5. **Design a response for every load-bearing path** (high-P × high-Impact): ELIMINATE / MITIGATE / HEDGE / ACCEPT-with-plan.
6. **Build your Not-to-Do list.** Crystallize "even under pressure, we will not do X" rules from the load-bearing failure paths.
7. **Name the abort trigger:** "We commit, *and* we will abort if ___ happens by ___ date."

### Output: the Inversion Audit

```
# Inversion Audit: <decision>
## Target outcome (measurable): <numbers + timeframe>
## Inversion question: "If this is a total failure by <date>, the most likely reasons are..."
## Failure paths (uncharitable): 1. <path> — category: internal/external/assumption/timing — P:<H/M/L> × Impact:<fatal/major/minor>
## Load-bearing paths: <path> → ELIMINATE / MITIGATE / HEDGE / ACCEPT-with-plan — <specific action>
## Not-to-Do additions: <new rule we will follow even under pressure>
## Abort trigger: "We will abort and re-invert if <observable> happens by <date>."
## What I might still be missing: <least-confident failure path — and how I'd test for it>
```

*→ Method in Action: [Apollo 1 and the FMEA Mandate (1967)](examples/apollo-1-fmea-1967.md) · [Wald's Bomber Survivorship Analysis (1942–1943)](examples/wald-bomber-survivorship-1943.md)*

## Inversion Packs

The Inversion Audit runs the same way everywhere, but the failure-mode catalog differs by domain. In **startup fundraising**: dilution at terms that make later rounds unraisable; misreading what the next round requires; taking strategic money that closes off other strategics. In **software launches**: capacity failure at launch; onboarding drop-off; negative review cascade; platform-policy surprises.

**Adding an inversion pack for your domain is the easiest way to contribute** — one self-contained file. See the contribution template at the repo root.

## Applying It Well

- **Deliverable = mitigations, not a scary list.** Failure list without paired responses is anxiety in spreadsheet form.
- **Specificity beats coverage.** Three concrete mechanisms beat ten vague paths.
- **Anonymity unlocks honesty.** Written independent submissions surface the failure paths people actually fear (Klein 2007).
- **The Not-to-Do list compounds.** Audits expire; the rules they generate persist.
- **Startups & investing:** eliminate catastrophic-loss paths first; merely-good paths take care of themselves.

*→ Sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

The ways people fake inversion. If you catch yourself in the left column, you are running a critique that doesn't change behavior.

**Note — [D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Pre-mortem theater** | 15 min in front of the plan's approver = safe surface list. Use anonymous written submissions, ≥ 30 min, senior person speaks first. |
| [D] **Failure list with no mitigation plan** | Deliverable = failure paths PLUS what you'll do about each. A list alone is anxiety in spreadsheet form. |
| [D] **Inversion paralysis** | Concluding "every path is risky, so don't move." Job is to eliminate *catastrophic* failures, not chase zero risk. |
| [D] **Asymmetric inversion** | Inverting only the option you don't like. Both sides must be inverted to the same standard, in the same units. |
| [D] **Placeholder labels as failure paths** | "Execution risk," "market shift" are headers. A failure path names a specific mechanism with actors, dates, and observable triggers. |
| [D] **Using inversion as a closure move** | "We did a pre-mortem, so we are done." If nothing in the plan changed, the audit didn't happen. |
| *To add [O] entries: paste a real failure instance here after each production use* | *Description of what happened* |

## Red Flags

- Generic placeholders in failure-path list ("execution," "market") with no specific mechanisms
- No new information surfaced — every path was already discussed
- No P × Impact ranking; no mitigation or abort trigger paired with any path
- Senior person dominated; dissenting paths were socially suppressed
- Audit < 30 minutes; "we did a pre-mortem" used as proof of rigor with nothing in the plan changing

## Verification

- [ ] Target outcome is measurable (number + timeframe)
- [ ] ≥ 5 failure paths enumerated uncharitably; each names a *specific mechanism*, not a placeholder
- [ ] Each path carries P(occur) × Impact rating and a category tag
- [ ] Every load-bearing path has a paired response: ELIMINATE / MITIGATE / HEDGE / ACCEPT-with-plan
- [ ] Explicit abort trigger named; ≥ 1 entry added to the Not-to-Do list

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/inversion** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
