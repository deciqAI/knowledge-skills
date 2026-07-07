---
name: occams-razor
description: "Activate when: user says 'simplify this', 'which is more likely', 'are we overcomplicating this?', 'what's the most likely explanation?', or presents multiple competing hypotheses/designs/diagnoses to rank. Do NOT activate when: only one explanation is on the table (nothing to compare), or when the candidates do not equally fit the evidence (establish fit first)."
---

# Occam's Razor

## Overview

When several explanations all fit the evidence, prefer the one that assumes the least. It is a selection heuristic, not a proof — it tells you what to bet on first, pending evidence that can tell the candidates apart.

This is one of three composable motions in the deciqAI collection: [first-principles](../first-principles/SKILL.md) decomposes *downward* to irreducible bedrock; **occams-razor** chooses *sideways* among the competing accounts; [second-order-thinking](../second-order-thinking/SKILL.md) traces *forward* through time and consequence. Compose: reduce to bedrock (first-principles), pick the simplest fitting hypothesis (here), then trace where that pick leads (second-order).

## When to Use

Apply when: **multiple explanations/designs/diagnoses** need ranking; a proposal keeps **accreting special cases**; someone says "simplify this," "which is more likely," "are we overcomplicating this?"

**When NOT:** candidates don't equally fit the evidence (establish fit first); only one option exists; applying it would drop a known datum (over-shaving); cost of being wrong dwarfs cost of one extra assumption.

## Coaching Novices (Adaptive Front Door)

Two delivery modes — pick one: **Engine mode** (user has concrete options → run full Parsimony Audit directly). **Coach mode** (user signals unfamiliarity → guide step by step). Unsure? Ask: *"Want me to run this on specific options, or walk you through the method?"*

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output that step's question and nothing more.

1. **One-line what-it-is.** When several explanations fit the evidence, the razor picks the one that assumes the least — counting *unsupported assumptions*, not words. It selects what to bet on; it doesn't prove what's true.
2. **Check fit.** Match their situation against When to Use / When NOT. If it doesn't fit, say so and point elsewhere.
3. **Elicit their real options.** Ask for ≥2 concrete candidates that actually fit the evidence.

> **[WAIT — do not advance until user responds]**

4. **One step at a time.** Walk the Process one step per turn — enumerate candidates with them, apply the fit gate, count assumption loads — wait for input before advancing.

> **[WAIT — do not advance until user responds]**

5. **Close by naming the payoff.** Name which candidate they chose, the unsupported assumption that sank the loser, and the observation that would overturn the call.

> **[WAIT — do not advance until user responds]**

## The Process

Run the **Parsimony Audit** — fit *before* simplicity, count assumptions not words.

1. **State the question and enumerate candidates.** List competing explanations/designs (need ≥2 — with one the razor does not apply).
2. **Fit gate.** Confirm each candidate accounts for **all** known evidence/requirements. Drop any that don't. *The razor only chooses among explanations that fit.*
3. **Count the assumption load.** For each survivor, list assumptions/entities not independently supported by evidence. Count *those* — not lines, not words.
4. **Compare and prefer.** Choose the candidate with the fewest unsupported assumptions.
5. **Over-shave check.** Does the preferred candidate still fit **all** evidence? If preferring "simple" dropped a datum, restore the necessary entity.
6. **Hold it as a prior, not a verdict.** Name the specific observation that would overturn the preference.

### Output: the Parsimony Audit
```
# Parsimony Audit: <question>
## Candidates:  A: <...>  B: <...>
## Fit check:   A fits all evidence? <yes/no>  B fits? <yes/no>
## Assumption load:  A requires: <list> → count  B requires: <list> → count
## Preferred:   <fewest unsupported assumptions>
## Over-shave check: <preferred still fits everything?>
## What would overturn this: <distinguishing evidence>
```

*→ Method in Action: [Wegener and Continental Drift (1912)](examples/wegener-continental-drift-1912.md) · [Semmelweis and Childbed Fever (1847–1861)](examples/semmelweis-childbed-fever-1847.md)*

## Audit Packs

Domain-specific capture of: (a) valid candidates, (b) what counts as unsupported assumption, (c) fake-simplicity moves the domain habitually accepts.

**Software incident triage:** candidates = failure-mode hypotheses; unsupported = any posited failure the logs don't corroborate; classic fake = "must be the network" while cache TTL data was on screen.

**Clinical differential:** candidates = differentials; unsupported = pathologies disagreeing with labs; classic fake = preferring common over rare even when labs make rare fit better.

**Adding an audit pack for your domain is the easiest way to contribute** — one self-contained file. See the contribution template at the repo root.

## Applying the Razor Well

- **Count entities, not syllables.** "It's the network" posits an unobserved failure; "cache TTL expired at 14:03, as logs show" is longer but assumes less. Parsimony is about unsupported posits, not brevity.
- **Fit is a gate, not a tiebreaker.** Simplicity only adjudicates among accounts that already explain everything.
- **The razor ranks; evidence decides.** Output is "look here first" + "here's what would change my mind" — never "therefore true."
- **Accretion is a smell.** A new epicycle for every new fact means re-examine the base account, not keep patching.

*→ Sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**Note — [D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "It's simpler, so it's true" | The razor is a *preference among fitting explanations*, not a proof. Picks where to look first, not what *is*. |
| [D] Using the razor to dismiss complexity the evidence requires | If a datum needs the extra entity, cutting it is over-shaving. Fit before simplicity, always. |
| [D] "Simpler" = fewer words / shorter to state | Parsimony counts *unsupported assumptions*, not length. A short claim can smuggle many posits. |
| [D] Comparing candidates that don't equally fit the evidence | Run the fit gate first — the razor only adjudicates among accounts that all explain the data. |
| [D] "Occam said entities must not be multiplied beyond necessity" | That formulation is **not** in Ockham's texts — later attribution (SEP). Don't anchor on a misquote. |
| [D] Treating the razor's output as final | It's a tiebreaker pending distinguishing evidence. Can't name what would overturn it? Audit isn't done. |
| [D] One explanation on the table, then "by Occam's razor…" | With a single candidate there is nothing to prefer. Enumerate alternatives first. |
| [D] **Asymmetric assumption-counting** | Strict on the candidate you dislike; generous on the one you want. Counts must be **blinded to preference**. |
| [D] Picking the simplest **story** rather than the simplest **mechanism** | A neat narrative can hide many unstated mechanisms. Parsimony is about *unsupported posits*, not literary economy. |
| *To add [O] entries: paste a real failure instance here after each production use* | *Description of what happened* |

## Red Flags

- Fit gate skipped — candidate preferred without confirming it fits all evidence
- "Simpler" judged by length or vibe, not unsupported assumptions
- Only one explanation ever on the table
- Preferred explanation silently drops a known datum (over-shave)
- Razor deployed to win an argument, not rank hypotheses
- No statement of what evidence would overturn the preference

## Verification

- [ ] Two or more candidates enumerated
- [ ] Every surviving candidate fits all known evidence (fit gate before any comparison)
- [ ] Assumption load counted as unsupported assumptions/entities — not words or steps
- [ ] Preferred candidate has fewest unsupported assumptions
- [ ] Over-shave check confirms preferred candidate still fits everything
- [ ] Distinguishing evidence that would overturn the preference is named

---
*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/occams-razor?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=occams-razor** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
