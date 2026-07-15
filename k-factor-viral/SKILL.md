---
name: k-factor-viral
description: "Activate when: user says 'viral coefficient,' 'K-factor,' 'going viral,' 'our product is viral,' 'referral program,' 'invite mechanic,' 'built in sharing,' growth plateauing despite viral elements, or a growth forecast is being justified by virality without a K calculation.
  Do NOT activate when: product is B2B enterprise (sales-led growth); focus is engagement/retention not new-user acquisition; product has not yet achieved PMF."
---

# K-Factor and Viral Coefficient

## Overview

**K = i × c**, where **i** = average invites per existing user, **c** = conversion rate into new *activated* users. K > 1 → exponential growth; K < 1 → finite ceiling; K = 1 → linear. Most "viral" products have K in the 0.1-0.6 range — social transmission, not a growth engine.

Codified by Steve Jurvetson (DFJ) via the Hotmail case (1996); formalized by Andrew Chen, David Skok, and early Facebook/LinkedIn growth teams.

Composes with [`aarrr-pirate-metrics`](../aarrr-pirate-metrics/SKILL.md) (K sits in Referral), [`network-effects`](../network-effects/SKILL.md) (value vs. user count — different things), [`mvp`](../mvp/SKILL.md) (smoke tests cannot establish K), [`feedback-loops`](../feedback-loops/SKILL.md) (K > 1 is a specific reinforcing-loop condition).

## When to Use

- A product is described as "viral" without an explicit K calculation
- Growth plateauing despite "viral elements" (share buttons, referral programs, invite flows)
- A growth team debating which lever to pull without the K = i × c decomposition
- An investor or founder using "viral" to justify a growth forecast
- **Not when:** B2B enterprise; focus is engagement/retention; pre-PMF product

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: virality is **K = i × c > 1** — below 1, the product doesn't grow by itself.
2. Check fit: B2B / enterprise / pre-PMF → not this lens yet.
3. Elicit the product and current invite mechanic.
> **[WAIT — do not advance until user responds]**
4. One question at a time: what's i? what's c? what's K? is K stable across waves?
> **[WAIT — do not advance until user responds]**
5. Close: name the specific i lever or c lever to attack.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Define units:** New user = *activated* (not signed up). Identify invite event and conversion event. Set cohort window (typically 7-30 days).

**Step 2 — Calculate:** i = total invites / N users. c = conversions / total invites. K = i × c.

**Step 3 — Growth math:** K < 1 → ceiling = N₀/(1-K). K = 1 → linear. K > 1 → exponential. (1000 users: K=0.9 → ~10K ceiling; K=1.5 → ~3.3M after 20 cycles.)

**Step 4 — Decompose separately:** i levers (one-click invite, address-book import, prompt at high-intent moments) vs. c levers (personalize invite, reduce signup friction, make value obvious, activation in <60s). Separate design problems — separate owners.

**Step 5 — Cycle time (t):** time from activation → first invite sent + time from invite → recipient activates. Reducing t is often more impactful than improving K.

**Step 6 — K stability:** measure K across waves 1-5. If K < 1 by wave 3, growth has a finite ceiling regardless of early K.

## Output: K-Factor Analysis

```markdown
# K-Factor Analysis: <product>
- Activated new user definition: | Invite event: | Conversion event: | Cycle window t:
- i: | c: | K = i × c: | Interpretation: <K<1 ceiling / =1 linear / >1 exponential>
- Ceiling or multiplier: | Time to N users:
- i levers — barrier: | test:
- c levers — barrier: | test:
- K wave 1: | wave 3: | wave 5: | Stable above 1?
```

*→ Method in Action: [Hotmail, 1996-1998](examples/hotmail-1996-1998.md)*

## Pack: K-Factor by Product Type

| Product type | Typical K | Dominant lever |
|---|---|---|
| Email / messaging (Hotmail, Zoom) | 1.5-3+ | i (use IS an invite) |
| Referral-program-driven (PayPal, Dropbox) | 0.8-1.8 | i (financial incentive; decays) |
| Consumer SaaS (Notion, Figma) | 0.3-0.8 | c (collaboration-driven) |
| B2B SaaS | 0.05-0.3 | Virality rarely the engine |

## Applying It Well

- Measure K on *activated* users — K drops 50-70% vs. signups
- Treat i and c as separate sprints with separate owners
- Check K decay across waves before declaring viral success
- Consent-based mechanics only — aggressive address-book imports risk platform bans

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We're viral, look at our share button" | A share button is not a viral mechanic. Calculate K. |
| [D] K calculated on signups | Recalculate on activated users — K usually drops 50-70%. |
| [D] "Our K is 1.2, we're set" | K decays across waves. K_wave1=1.2 + K_wave3=0.5 = finite ceiling. |
| [D] Optimizing i and c as one project | Separate design problems; one vague project moves neither. |
| [D] Long viral cycle times ignored | K=1.5 at t=60d is far slower than K=1.2 at t=7d. Reduce t. |
| [D] Treating word-of-mouth as virality | Word-of-mouth boosts c on paid acquisition; K>1 virality is different. |
| [D] Building viral mechanics pre-PMF | Viral invites bring people who churn if retention is broken. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "Viral" used without a K calculation; K on signups not activated users
- K stability across waves not measured; cycle time t not measured
- i and c treated as one optimization; network effects and K-factor conflated
- High K via non-consensual mechanics (platform ban risk)

## Verification

- [ ] New user = activated, not signed up
- [ ] i, c, K calculated separately with cohort + time window stated
- [ ] Cycle time t measured
- [ ] K stability checked across at least 3 waves
- [ ] i and c levers designed and tested separately
- [ ] K < 1 acknowledged; growth model reflects finite ceiling; invitation mechanics are consent-based

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/k-factor-viral** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
