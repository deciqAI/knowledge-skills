---
name: lindy-effect
description: "Activate when: user asks 'should we use this old technology or switch to something newer', 'how do I know if a book is worth reading', 'this institution has been around forever — is that meaningful', 'we should modernize / this time is different', 'how long will this practice / tool / framework last'.
  Do NOT activate when: the item is perishable or has a deterministic life cycle (humans, hardware, organisms); elimination forces are absent and the old thing survives only due to regulatory lock-in."
---

# Lindy Effect

## Overview

For **non-perishable items** — ideas, books, technologies, institutions, practices — life expectancy is proportional to current age. The longer something has survived competitive elimination, the longer its expected remaining life. Math: if survival follows a Pareto distribution with α ≈ 1, expected remaining life ≈ current age. Not nostalgia — statistical inference from a track record of passing elimination tests.

Composes with [`antifragile`](../antifragile/SKILL.md) (Lindy-survival is the signature of antifragility), [`survivorship-bias`](../survivorship-bias/SKILL.md) (paired warning), [`first-principles`](../first-principles/SKILL.md) (Lindy says *that*; first-principles says *why*), [`switching-costs`](../switching-costs/SKILL.md), and [`chestertons-fence`](../chestertons-fence/SKILL.md).

## When to Use

- Choosing a foundational technology / library / framework with high switching cost
- Evaluating a long-established practice or institution someone is proposing to discard
- Assessing a new methodology being marketed as "modern" or "evidence-based"
- Allocating reading time across old vs. new books
- Designing institutional partnerships with multi-decade horizons
- Someone says "this has stood the test of time," "we should modernize," "this time is different"

**Not when:** item is perishable or has a deterministic life cycle; elimination forces are absent (old institution survives only via regulatory protection); conditions have genuinely changed enough to invalidate survival evidence; decision time-horizon is too short for long-run durability to matter.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete old-vs-new decision → run The Process directly.
- **Coach mode:** user unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: for non-perishable items where elimination forces still operate, prefer the older — its survival is evidence of durability the newer item hasn't yet earned.
2. Check fit: perishable item or absent elimination forces → Lindy doesn't apply.
3. Elicit their case: what's the old item? the new? the domain?
> **[WAIT — do not advance until user responds]**
4. Run The Process: non-perishable? elimination forces continuous? Lindy prior? conditions justify this-time-is-different?
> **[WAIT — do not advance until user responds]**
5. Close: state the decision with Lindy-prior + conditions that would override it.
> **[WAIT — do not advance until user responds]**

## The Process

```
Step 1 — Items: old item (age) / new item (age) / decision / time horizon / switching cost
Step 2 — Applicability: non-perishable? | elimination forces operating? | power-law plausible? | conditions changed?
Step 3 — Lindy prior: old expected remaining life (≈ age) / new expected remaining life / ratio
Step 4 — This-time-is-different: which conditions changed / invalidates survival evidence? / cost if wrong
Step 5 — Decision: foundational → lean Lindy; exploration → lean new; document Lindy weight
Step 6 — Reversibility (if going against Lindy): reversal plan / reversal signals / monitoring owner
```

### Output: Lindy-Informed Decision
```
# Lindy-Informed Decision: <decision>
Items: old (age) / new (age) / time horizon / switching cost
Applicability: non-perishable Y/N | elimination forces Y/N | power-law Y/N | conditions changed Y/N
Prior: old remaining life / new remaining life / ratio
This-time-is-different: claim / evidence / verdict
Decision: old/new/hybrid | Lindy weight | override reasoning
Reversibility: plan / signals / owner
```

*→ Method in Action: [Goldman 1964, Mandelbrot 1982, Taleb 2012](examples/goldman-1964-mandelbrot-1982-taleb-2012.md)*

## Pack: Lindy Effect Application Patterns

| Domain | Lindy-stronger choice | Common error |
|---|---|---|
| Programming languages | C (1972), Python (1991) over 3-year-old languages | Adopting new language for foundational layer |
| Databases | PostgreSQL (1996), Oracle (1977) over new graph DBs | Choosing newest for load-bearing tier |
| Reading | 100-year-old in-print book over this month's release | Reading only the new; assuming old is irrelevant |
| Scientific findings | 50-year replicated finding over new single study | Treating new study as more credible than decades-replicated old finding |
| Investment principles | Graham (1934), Bogle (1975) principles over recent strategies | Adopting recent quantitative strategy as foundation |

## Applying It Well

- Lindy is a **prior**, not a verdict — it shifts burden of proof to "why new?" without banning new.
- Lindy weight is high for load-bearing foundations (high switching cost, long horizon), low for exploration layers.
- "This time is different" bears the burden: name *which* conditions changed and *why* that invalidates survival evidence.
- Compose with first-principles: Lindy says *that* something works; first-principles says *why* — test whether modern conditions break the mechanism.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "It's old, so it's outdated" | Lindy says the opposite: old non-perishables have *more* durability evidence, not less. |
| [D] "This time is different" | Reinhart's 800 years: this is rarely as different as claimed. Burden of proof on the change-claim. |
| [D] "Modern conditions changed everything" | Some conditions did. Name *which* changed and *whether* that invalidates the survival evidence. |
| [D] "New = better" | Empirically false in many domains. Lindy-strong systems outlasted multiple generations of "improvements." |
| [D] "We'll switch back if it doesn't work" | Switching costs are non-symmetric. New systems create lock-in that prevents rollback. |
| [D] "Tradition isn't a reason" | Long-surviving tradition is statistical evidence — add first-principles, don't dismiss it. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- An "outdated" technology is being replaced without specific reason beyond age
- A new methodology is being adopted because "it's the new standard"
- "This time is different" is the primary justification for a major change
- The cost of the new (if it fails) is much higher than the cost of staying with the old
- The decision-maker has personal career incentive for the new

## Verification

- [ ] Lindy-applicability tested (non-perishable, elimination forces, power-law)
- [ ] Lindy prior for the old item's continued survival computed or qualitatively estimated
- [ ] This-time-is-different claim (if any) specifically articulated and evaluated
- [ ] Cost of being wrong about overriding Lindy computed
- [ ] If going against Lindy: reversibility plan in place
- [ ] Lindy weighting documented in the decision

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/lindy-effect?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=lindy-effect** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
