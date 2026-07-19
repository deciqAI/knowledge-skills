---
name: black-swan
description: "Activate when: user says 'this can't happen,' 'never happened in N years,' 'our models say it's near-zero'; user is stress-testing a strategy or portfolio against extreme scenarios; someone mentions fat tails, Taleb, narrative fallacy, or turkey problem; a past catastrophic event is being analyzed and it 'seemed obvious in hindsight.'
  Do NOT activate when: the domain is genuinely thin-tailed (human heights, daily caloric intake); user is invoking 'black swan' as an excuse for a planning failure they could have avoided. More: deciqai.com/s/black-swan"
---

# Black Swan

## Overview

Taleb (2007): a black swan is (1) outside all prior expectations, (2) extreme impact, (3) obvious in hindsight only. Many domains (markets, careers, tech) are **Extremistan** (power-law / fat-tail), yet most models assume **Mediocristan** (Gaussian / thin-tail) — underestimating tail risk by orders of magnitude. The Turkey Problem: 1000 days of feeding creates confidence; day 1001 is Thanksgiving.

Composes with [`antifragile`](../antifragile/SKILL.md), [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md), [`inversion`](../inversion/SKILL.md), [`first-principles`](../first-principles/SKILL.md).

## When to Use

Use when: a risk model assumes normality in a fat-tailed domain; "never happened in N years" dismisses tail risk; strategy assumes stable environment; you're constructing a retrospective narrative; stress-testing against extreme scenarios; someone says "fat tails / Taleb / narrative fallacy / turkey problem"; a thesis rests on a one-directional trend like "AI demand can only go up," AI-capex payoff, or concentrated mega-cap / AI-bubble exposure.

**Not when:** domain is genuinely Mediocristan; "black swan" is being used to excuse a foreseeable planning failure.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: some domains have rare events that dominate everything (markets, careers, tech); models assuming "normal" distributions miss them — and we always invent stories afterward that make them look predictable.
2. Check fit: genuinely thin-tailed domain (heights, commutes)? Point elsewhere.
3. Elicit the real situation — what decision or system are we auditing?
> **[WAIT — do not advance until user responds]**
4. One question at a time: is this Extremistan or Mediocristan? What's the tail-survival design? What narrative am I constructing post-hoc?
> **[WAIT — do not advance until user responds]**
5. Close: name the specific tail-event preparation — not prediction — they've uncovered.
> **[WAIT — do not advance until user responds]**

## The Process

### Step 1: Classify the domain (Extremistan vs Mediocristan)

Sample 30+ historical observations. Bell-shaped → Mediocristan. Power-law / long-tail → Extremistan. **Specific test:** does the largest observation dominate the sum of the others? If yes → Extremistan.

### Step 2: Identify hidden Mediocristan assumptions in your Extremistan domain

For each assumption: does it imply "normal distribution"? Use "rarely happens" or "the average is X"? Ignore outliers dominating outcomes? If yes and domain is Extremistan — structurally vulnerable.

### Step 3: Design for tail survival

Tail survival ≠ tail prediction. Options: **Bounded downside** (no single event breaks you), **Optionality** (many small bets, convex upside), **Redundancy** (multiple suppliers / revenue lines), **Skin in the game** (decision-makers bear tail consequences). See [`antifragile`](../antifragile/SKILL.md).

### Step 4: Defend against the narrative fallacy

Resist "we should have seen it coming." Ask: *what was the epistemic state of well-informed people the day before?* The "obvious in retrospect" feeling is hindsight bias, not predictability. Design for the category, not the specific next event.

### Step 5: Distinguish black swans from grey swans

- **White swans:** routine, well-modeled. **Grey swans:** rare but predictable (hurricane in a hurricane zone). **Black swans:** rare AND unpredictable.
- Grey swan failure = planning failure. Black swan loss = design failure. The distinction matters.

## Output: Black Swan Audit

```markdown
# Black Swan Audit: <system / decision>
## Domain: Extremistan / Mediocristan / mixed — Evidence: <…>
## Hidden Mediocristan assumptions: <list>
## Tail-survival design: bounded downside via <…> | optionality via <…> | redundancy via <…>
## Narrative-fallacy check: past event <…> | story told <…> | actual epistemic state <…>
```

*→ Method in Action: [Long-Term Capital Management Collapse, 1998](examples/long-term-capital-management-collapse-1998.md) · [Fukushima Daiichi Tsunami, 2011](examples/fukushima-daiichi-tsunami-2011.md)*
*→ 2026 lens: [Concentration risk in the AI trade (2023–2026)](examples/ai-trade-concentration-2023-2026.md)*

## Pack: Black Swan Domains

| Domain | Extremistan evidence | Tail-survival design | Common failure |
|---|---|---|---|
| Finance / trading | single crash day dominates decades of returns; 1987 was 20+ sigma under Gaussian | leverage that survives correlations→1; no ruin-level position sizing | VaR under Gaussian assumptions; "diversification" across risks that converge in crises |
| Venture / startups | one fund-returner outweighs the rest of the portfolio combined | many small bets, convex upside; reserves for winners, not averages | modeling outcomes with expected values; concentrating on one "sure thing" |
| Infrastructure / engineering | worst recorded flood / quake / tsunami dominates all damage totals | design margin above the full historical record; backups with no common-cause failure | design basis anchored to recent-instrumental maximum (Fukushima's 5.7 m seawall) |
| Careers / creative work | a handful of hits, roles, or books produce most lifetime payoff | barbell: stable base + repeated cheap shots at unbounded upside | betting everything on one employer or project; reading a hot streak as a stable trend |

Mediocristan (safe to use averages): human heights, daily caloric intake, commute times on normal days.

*Contribute a pack for your domain — see the template at the repo root.*

## Applying It Well

- Goal is tail-survival design, not prediction — you cannot predict the specific next black swan.
- Most "diversified" portfolios are not: in crises, correlations jump toward 1. True diversification is across *uncorrelated* risks.
- Mathematical sophistication does not protect against domain misclassification (LTCM lesson).
- "This has worked for years" is the turkey's argument.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "It's never happened in N years, so it can't happen" | The turkey problem. N years of data is consistent with both impossible and "imminent." |
| [D] "We have sophisticated models" | Models that assume the wrong distribution are sophisticated in the wrong direction. |
| [D] Constructing a confident retrospective narrative | Hindsight bias. The actual epistemic state before the event was much less clear. |
| [D] "Insurance / hedges / risk management protect us" | If those mechanisms also use Mediocristan assumptions, they fail in the same event. |
| [D] Predicting the specific next black swan | Not possible. Predict the category; design for tail-event survival. |
| [D] Treating "black swan" as an excuse for poor planning | Grey swans get mislabeled as black swans by people who failed to plan. |
| [D] Diversification across correlated risks | True diversification is across uncorrelated risks. In crises, correlations jump toward 1. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Risk model assumes Gaussian distribution in an Extremistan domain
- "Has never happened" used as evidence of impossibility
- Diversification claimed without analysis of correlation in crises
- Confident prediction of when the next tail event will occur
- Retrospective "obvious in hindsight" claims about past events
- Mathematical sophistication treated as protection against domain misclassification

## Verification

- [ ] Domain classified (Extremistan / Mediocristan / mixed) with evidence
- [ ] Hidden Mediocristan assumptions identified
- [ ] Tail-survival design specified (bounded downside / optionality / redundancy / skin)
- [ ] Past "black swans" in domain checked for narrative-fallacy framing
- [ ] Grey swans distinguished from true black swans
- [ ] Plan does not depend on predicting specific tail events

---

*Part of **deciqAI Knowledge Skills** — 233 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/black-swan** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/black-swan.json*
