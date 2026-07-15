---
name: social-proof
description: "Activate when: user says 'everyone is doing this,' 'join thousands of others,' 'it's the popular choice,' 'trusted by X customers,' wonders if a trend or consensus is real, suspects fake reviews or manufactured engagement, or is designing testimonials/UX to convert users. Do NOT activate when: the decision is low-stakes and reversible (choosing a lunch spot) or the user already has direct measured evidence stronger than any consensus signal."
---

# Social Proof

## Overview

**Social proof**: we judge what is correct, normal, or worth doing by observing what others — especially similar others — are doing. Usually efficient; failure mode is severe: under unanimous consensus, people publicly endorse answers they privately know are wrong (Asch 1951–56: error rate <1% alone, ~37% under group pressure). Two amplifiers: **uncertainty** (social proof fills the vacuum) and **similarity** (same-type peers drive far stronger conformity than generic crowds).

Composes with [`reciprocity`](../reciprocity/SKILL.md) (Cialdini's two primary levers), [`anchoring`](../anchoring/SKILL.md) (price tiers often function as quasi-social-proof), and [`critical-thinking`](../critical-thinking/SKILL.md) (structured fallback when consensus has been engineered).

## When to Use

**Use when:** purchase/hiring/investment decision leaning on what others chose; proposal cites "everyone is doing this"; designing growth/marketing/UX with social-proof patterns; decision feels unsafe alone without a clear reason; suspecting manufactured consensus (bots, paid reviews, astroturf); a trend is accelerating and private doubt is being suppressed by the fact everyone is on board; a "we must adopt AI because every competitor is deploying it" mandate is driving procurement or a pilot ahead of any validated ROI (AI hype / FOMO buying).

**Do NOT use when:** decision is low-stakes and reversible; you have direct measured evidence stronger than any consensus; the "consensus" is from verified domain experts with better epistemic position; you want to rationalize a contrarian position that lacks independent evidence.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide, don't lecture.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line what-it-is.** We judge what's correct by looking at what others do — useful most of the time, but under enough unanimous consensus, people will publicly agree with answers they privately know are wrong, even on obvious questions.
2. **Check fit** against When to Use / When NOT to use. If direct evidence is stronger, point there.
3. **Elicit the real situation.** A concrete decision shaped by what others are doing, or a design problem deploying social proof. Never run on hypotheticals.
> **[WAIT — do not advance until user responds]**
4. **One element at a time.** Walk through: what's the consensus, who are the consensus-makers, are they similar to you / informed, would you decide the same way if alone — wait for input.
> **[WAIT — do not advance until user responds]**
5. **Close by naming the payoff.** The one move — accept the consensus, reject it, or seek independent evidence — that fits their situation.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Social-Proof Analysis**. Diagnose the source of consensus, then decide whether to use it as evidence.

1. **Name the consensus precisely.** Not "everyone uses Salesforce" but "three cohort companies I respect use Salesforce." Vague consensus cannot be analyzed.
2. **Identify consensus-makers.** Who exactly, how many, how similar to you in ways relevant to the decision?
3. **Classify consensus type.** Informational (converged on evidence) | Social (converged because others did — cascade risk) | Manufactured (engineered appearance via bots, paid reviews, cherry-picked cases).
4. **Test signal strength.** Did consensus form independently or in chain? What are dissenters saying? What is the base rate for consensus being wrong in this domain?
5. **Run the Asch counterfactual.** Alone, with only the underlying evidence, would you reach the same conclusion? If no — you've been pulled in by the rule itself.
6. **Check manufactured-consensus signs:** astroturf, survivorship bias, selected testimonials, engagement-metric inflation.
7. **As a sender:** real named testimonials, third-party reviews, transparent distributions, limitations in case studies.
8. **Stop-rule:** if you cannot defend the decision independently of "many others are doing it," treat it as provisional. Plan a fallback.

### Output template

```
Consensus claim: [specific group, not generic mass; how many; similar to me how?]
Consensus type: [informational / social / manufactured / mix]
Independent vs. chain: [yes/no — cascade risk]
Dissenters: [who, what they say]
Asch counterfactual: [same conclusion alone? yes/no]
Manufactured-consensus check: [astroturf / survivorship / testimonials / metric inflation]
Decision: [follow / depart / seek independent evidence] — because [reason]
Early-warning trigger: [what would signal consensus is wrong]
```

*→ Method in Action: [Solomon Asch's Conformity Experiments, Swarthmore, 1951–1956](examples/solomon-asch-conformity-experiments-swarthmore-1951-1956.md)*

*→ 2026 lens: [Enterprise AI Copilot FOMO Procurement (2024–2026)](examples/enterprise-ai-copilot-fomo-procurement-2024-2026.md)*

## Pack: Social Proof in Practice

- **Sender (marketing/sales):** named logos, real attributed testimonials, third-party reviews, transparent star distributions, case studies with limitations stated. Reference customers similar to the prospect.
- **Receiver (evaluation):** check distribution shapes not averages; distinguish trial users from paying customers; named accounts are top-decile success cases — ask about failures.
- **Product UX:** "popular choice" defaults are powerful — notice when a default is doing your decision-making for you.
- **Astroturf defense:** anomalous account creation timing, repeated language across "independent" voices, engagement metrics inconsistent with audience size → drop consensus signal to near-zero.

## Applying It Well

- Similarity is load-bearing: "other founders chose this" works on a founder; "many people chose this" does not. Always identify whether consensus-makers are similar to you in relevant ways.
- Three well-placed testimonials approach the power of fifteen — the rule saturates at small numbers.
- A single visible dissenter destroys most conformity pressure. Find the dissenter or be the dissenter.
- The rule operates below introspection. The Asch counterfactual is the test, not the self-report.
- Manufactured social proof has a reputational cliff when discovered. Real social proof compounds.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Everyone is doing it, so it must be right" | Asch showed this fails on tasks where the right answer was visually obvious. "Everyone" is one signal to weigh — not the conclusion. |
| [D] "Many smart people are doing X, so X is right" | Smart people are more invested in being seen as smart, raising the cost of public dissent. The "smart people" filter does not defend against engineered consensus. |
| [D] "I have my own opinion regardless of what others do" | Asch's 75% applies even to people who predicted this of themselves. The rule operates below introspection — the counterfactual is the test. |
| [D] "Bestseller / most-popular must be the best" | Popularity reflects discoverability and marketing, not necessarily quality. Treat it as a prior, then update on evidence. |
| [D] "If it were wrong, more people would have noticed" | Public dissent is rare even when private dissent is widespread (Theranos, FTX, 2008 housing market). |
| [D] "I noticed the manufactured social proof, so I'm immune" | Recognition reduces but does not eliminate the pull. Treat recognition as the start of defense, not the conclusion. |
| [D] Confusing aggregated wisdom with social proof | Markets aggregate information. Social proof aggregates behavior — which may not reflect information. Distinguish "independent estimators converged" from "people followed early movers." |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Decision driven by "many others are doing it" with no underlying analysis
- Consensus-makers cannot be verified as similar to you in relevant ways
- No dissenters visible in a domain where you would expect dissent
- Consensus measured in low-cost actions (likes, sign-ups) not high-cost ones (purchases, repeat usage)
- Star distributions are suspiciously skewed (all 5-stars or U-shaped)
- Social-proof claim growing faster than the underlying user/evidence base could plausibly support

## Verification

- [ ] Consensus claim named precisely (specific group, not generic mass)
- [ ] Consensus-makers identified — number, similarity, base of information
- [ ] Consensus classified: informational / social / manufactured
- [ ] Asch counterfactual performed: same conclusion alone?
- [ ] Dissenting voices sought; their reasoning evaluated
- [ ] Manufactured-consensus signs checked
- [ ] If following: early-warning indicator specified
- [ ] If sending: proof is real, named, verifiable, representative

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/social-proof** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
