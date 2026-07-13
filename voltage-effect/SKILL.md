---
name: voltage-effect
description: "Diagnoses whether a result that worked at small scale will keep working when scaled — by testing an idea against John List's five reasons ideas lose 'voltage' (false positives, unrepresentative population, unrepresentative situation, spillovers, and the supply-side cost trap) BEFORE committing to scale.
  Activate when: user says 'the pilot worked, let's roll it out', 'this crushed it in the beta', 'we're ready to scale', 'the unit economics will improve with volume', 'it worked in one city/market/segment', 'should we franchise / expand nationally', or wants to predict whether a promising early result will survive scaling.
  Do NOT activate when: the question is purely how to build scale infrastructure with no doubt the result generalizes (use economies-of-scale); the idea has already scaled and held, and you are optimizing a mature operation; or the decision has no scale step at all (a one-off, non-repeatable choice)."
---

# Voltage Effect

## Overview

The **voltage effect** is John A. List's name for what happens to most promising ideas when they scale: they lose voltage — they fail, shrink, or reverse — because the conditions that produced the small-scale win do not survive being scaled. The discipline is to predict scalability *before* you scale, by interrogating an early win against **five vital signs**: (1) **false positives** — the pilot result was never real (underpowered, p-hacked, or a fluke); (2) an **unrepresentative population** — it worked on early adopters or a hand-picked group that will not generalize; (3) an **unrepresentative situation** — it worked in one context, channel, or market that will not replicate; (4) **spillovers** — general-equilibrium effects (congestion, saturation, competitive response) that only appear at scale; (5) the **supply-side cost trap** — unit economics, talent, or operations that break as volume grows, so the idea is unscalable even when demand is real.

List frames the burden of proof plainly:

> "The vast majority of ideas—no matter how great they seem at first blush—don't scale. And it's often not until we take these ideas to scale that we discover their fatal flaws."
> — John A. List, *The Voltage Effect* (2022)

List's larger point: what makes an idea *scalable* is not the same as what makes it *seem promising* in the first place.

The correct default is skeptical: an idea is presumed **non-scalable** until it survives all five vital signs. List's scalable *levers* are the other half: **high-fidelity implementation** (the scaled version must deliver what the pilot delivered, not a diluted copy), **marginal thinking** (decide on marginal cost and marginal benefit at scale, not on pilot averages), and **designing for scale from day one** (build the population, the situation, and the cost curve you will need at volume into the first test).

**Compose with neighbors.** Run voltage-effect *before* [economies-of-scale](../economies-of-scale/SKILL.md): economies-of-scale asks whether cost per unit falls with volume, but that is only vital sign #5 — clearing it while ignoring #1–#4 scales a fluke efficiently. Use it *instead of* raw optimism about [network-effects](../network-effects/SKILL.md): claimed network effects are a scale-only benefit that must be *demonstrated*, and their mirror image (congestion, saturation) is exactly the spillover of vital sign #4. Use it *after* [pmf-crossing-the-chasm](../pmf-crossing-the-chasm/SKILL.md): the chasm names *why* early-adopter traction fails to generalize; voltage-effect vital sign #2 makes that failure a checkable gate. It shares machinery with [representativeness-heuristic](../representativeness-heuristic/SKILL.md) (a vivid pilot is a prototype that overrides base rates) and with [lean-startup](../lean-startup/SKILL.md) (validated learning is the antidote to false positives — but voltage-effect insists the learning generalize, not merely replicate the same test).

## When to Use

Apply when:
- A pilot, beta, A/B test, or single-market launch succeeded and someone proposes rolling it out
- You must forecast whether an early result will hold at 10×, 100×, or national scale
- Unit economics are claimed to "improve with volume" without a mechanism
- A franchise, new-location, or new-market expansion is on the table
- Someone says: *"the pilot worked," "it crushed it in beta," "we're ready to scale," "it worked in one city"*

**When NOT to use:**
- There is no scale step — a genuinely one-off, non-repeatable decision
- The result has already scaled and held; you are optimizing a mature operation (use economies-of-scale)
- You only need cost-curve analysis with no doubt the effect generalizes (use economies-of-scale)
- The pilot itself has not concluded — there is no result to interrogate yet

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete pilot result and a scale proposal → run The Process directly against the five vital signs.
- **Coach mode:** user is unfamiliar or has only a vague "we want to grow" → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. What-it-is: most ideas that work small lose "voltage" at scale. Before scaling, we test the win against five specific ways it can be an illusion or a trap.
2. Check fit — is there an actual early result *and* a proposed scale step? If not (idea not tested, or nothing to scale), redirect.
3. Elicit the concrete case: what worked, how big was the pilot, and what does "scale" mean here (10×? new markets? national)?
> **[WAIT — do not advance until user responds]**
4. Walk the five vital signs one at a time with their numbers — is the result real, the people representative, the setting representative, are there spillovers, does the cost curve hold?
> **[WAIT — do not advance until user responds]**
5. Close by naming the single vital sign most likely to kill this at scale, and the cheapest test that would de-risk it before committing.
> **[WAIT — do not advance until user responds]**

## The Process

**Stop rule:** If the pilot's effect size, sample size, and selection method are unknown, stop at vital sign #1 and name the data gap — a result you cannot characterize cannot be scaled, only gambled.

1. **False-positive test (is the result real?).** Get the effect size, sample size, and how many things were tested. Ask: was it powered? Was one winner cherry-picked from many comparisons (p-hacking)? Has it *replicated* independently at least once? **Gate:** a single, unreplicated, underpowered, or multiple-comparison result fails — demand a confirmatory test before proceeding.
2. **Population representativeness (who did it work on?).** Characterize the pilot participants vs. the population at scale. Were they early adopters, volunteers, a hand-picked site, or a founder-adjacent group? **Gate:** if the scale population differs materially from the pilot population on any driver of the result, the effect is presumed to shrink — quantify the expected dilution.
3. **Situation representativeness (where/how did it work?).** Characterize the pilot context — market, channel, season, operator skill, novelty. **Gate:** if the winning condition (a star operator, a single channel, a launch-buzz moment) will not replicate across all scaled sites, the effect is presumed to shrink.
4. **Spillover test (what only appears at scale?).** Ask what changes when *everyone* does this: congestion, market saturation, price/wage response, competitive imitation, cannibalization, general-equilibrium feedback. **Gate:** if a plausible spillover reverses or materially erodes the effect at volume, model it — do not assume the per-unit pilot effect is additive.
5. **Supply-side cost trap (do the economics hold at volume?).** Trace marginal cost and the scarce input (talent, supervision, inputs, ops) as volume grows. Does the pilot rely on non-scalable inputs (a heroic founder, a subsidized input, a scarce specialist)? **Gate:** if marginal cost rises with volume or the scarce input cannot be reproduced, the idea is unscalable even if demand is real.
6. **Scale-decision + levers.** For each surviving vital sign, name the lever that preserves voltage: high-fidelity implementation (so the scaled version = the pilot), marginal thinking (decide on the margin, not the pilot average), and design-for-scale (rebuild the test at representative population, situation, and cost before betting).

### Output: Voltage Diagnosis

```
Idea: <what worked> | Pilot: <size/effect/selection> | Scale = <10×? new markets? national?>

Vital sign 1 — False positive:      PASS / FAIL / UNKNOWN  — <effect, n, #comparisons, replicated?>
Vital sign 2 — Population:          PASS / FAIL            — <pilot pop vs scale pop; expected dilution>
Vital sign 3 — Situation:           PASS / FAIL            — <winning condition; replicable across sites?>
Vital sign 4 — Spillovers:          PASS / FAIL            — <congestion/saturation/competitive response at scale>
Vital sign 5 — Supply-side cost:    PASS / FAIL            — <marginal cost trend; scarce input>

Weakest link: <vital sign most likely to kill it at scale>
Cheapest de-risking test: <the one experiment that would resolve the weakest link>
Levers to preserve voltage: <high-fidelity impl / marginal thinking / design-for-scale>
Verdict: SCALE / DE-RISK FIRST / DO NOT SCALE
```

*→ Method in Action: [The Chicago Heights Early Childhood Center (2010–)](examples/list-chicago-heights-early-childhood-2010.md)*

*→ Also: [Pets.com — demand was real, the cost curve was not (1998–2000)](examples/petsdotcom-supply-side-cost-trap-1998-2000.md) · [Krispy Kreme's franchise over-expansion (2000–2005)](examples/krispy-kreme-franchise-overexpansion-2000-2005.md) · [Groupon merchant spillovers (2008–2012)](examples/groupon-merchant-spillover-2008-2012.md)*

## Scale Packs

*This is the contribution surface — add domains and documented voltage-drops via PR.* A "voltage drop" is the specific way an early win loses its charge when scaled. Defining what it looks like per domain turns the five vital signs into pattern-matching.

| Domain | Looks great in the pilot because… | Voltage-drop at scale | Dominant vital sign |
|---|---|---|---|
| **SaaS / startup** | Beta users are hand-picked design partners who love the founder and tolerate rough edges; conversion and retention look elite | The general market is not design partners — activation and retention collapse; CAC rises as you exhaust the warm early-adopter pool; the "it sells itself" motion needs a paid sales team | #2 Population + #3 Situation |
| **SMB / franchise expansion** | The first locations run by the founder-operator (or a star franchisee) hit exceptional unit economics and quality | New sites are run by average operators at average locations; quality and margin regress to the mean; growth outruns supply chain, real estate, and management bench | #3 Situation + #5 Supply-side |
| **Marketplace / two-sided platform** | A dense pilot geography has enough supply and demand that match quality and liquidity feel effortless | New geos start cold (no liquidity); at national scale, supply congestion, take-rate-driven merchant churn, and competitive subsidy wars appear — the promised network effect meets its saturation twin | #4 Spillovers |

## Applying It Well

- **Presume non-scalable.** The base rate is that most ideas lose voltage; the burden of proof is on the idea to clear all five signs, not on the skeptic to find the flaw.
- **The weakest link governs.** Voltage is a chain — clearing four vital signs and failing one still kills it at scale. Find and de-risk the weakest link first, cheaply, before spending on scale.
- **Startup founders:** your beta cohort is almost never your market (vital sign #2). Before you "roll it out," re-run the test on strangers you cannot personally onboard, in the acquisition channel you will actually pay for — and price in that founder-led magic (#3) will not clone across your first ten hires. "Do things that don't scale" wins the pilot; it cannot win the scale-up.
- **SMB / franchise founders:** your flagship store's numbers were produced by *you* (#3) and by a location you cherry-picked. Model average-operator, average-location economics *before* signing franchisees, and confirm supply chain, hiring, and real estate can feed the growth curve (#5). Expanding faster than your management bench is the classic voltage drop.
- **Distinguish "demand is real" from "this scales."** Pets.com had real demand and still died on the cost curve. Proving people want it clears nothing about vital signs #4 and #5.
- **Use high-fidelity implementation as the test, not an afterthought.** If you cannot deliver the pilot's quality at 100× (same people, same care), you are scaling a different, weaker product — and that is the voltage drop.
- **Decide on the margin.** Pilot averages hide the truth; the scale question is always marginal cost vs. marginal benefit of the *next* unit at volume.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The pilot crushed it — let's roll it out." | A pilot win is the *starting* hypothesis, not the conclusion. It must survive all five vital signs; most wins don't. |
| [D] "It's statistically significant, so it's real." | Significance from one underpowered test, or one winner among many comparisons, is exactly vital sign #1. Demand independent replication. |
| [D] "Our beta users love it." | Beta users are hand-picked early adopters (#2). The question is whether *strangers you must pay to acquire* love it. |
| [D] "It worked in our first city, so it'll work everywhere." | One market is one situation (#3). Name what was special about that city — operator, density, novelty — and whether it replicates. |
| [D] "Unit economics will improve with volume." | That is a claim about vital sign #5, and it needs a mechanism. Absent one, marginal cost often *rises* (scarce talent, supervision, support). |
| [D] "The network effects will kick in once we're big." | Network effects are a scale-only benefit that must be demonstrated, and their twin — congestion/saturation (#4) — often kicks in first. |
| [D] "We'll just hire people to do what the founder does." | Founder-delivered magic rarely clones at fidelity (#3). If the effect depends on a scarce operator, it's a supply-side trap (#5). |
| [D] "Demand is obviously there — people want this." | Real demand says nothing about spillovers (#4) or the cost curve (#5). Pets.com had demand and still died on unit economics. |
| [D] "We can't afford to wait — we have to scale now." | Speed doesn't convert a false positive into a true one. It converts a cheap failed test into an expensive failed scale-up. |
| [D] "It's the same as [famous company that scaled], so it'll scale too." | Resemblance to a scaled winner is a prototype override (see representativeness-heuristic), not evidence your five signs pass. |
| *→ Add [O] entries here after each real use — paste the actual voltage-drop pattern* | *Which vital sign it failed, and why nobody caught it* |

## Red Flags

- A scale decision resting on a single pilot that has never been independently replicated
- The pilot population is volunteers, early adopters, design partners, or a hand-picked site — and the scale population isn't
- The winning condition is a specific person (founder, star operator) or a one-time moment (launch buzz, promotion, subsidy)
- "Unit economics improve with volume" asserted with no marginal-cost mechanism
- No one has asked what changes when *everyone* does this (congestion, saturation, competitive response)
- The scarce input that made the pilot work (a specialist, a subsidized input, founder attention) cannot be reproduced at volume
- Growth plan outpaces the management, hiring, supply-chain, or real-estate bench that must feed it

## Verification

- [ ] Vital sign #1: effect size, sample size, and number of comparisons stated; independent replication confirmed or flagged as missing
- [ ] Vital sign #2: pilot population characterized vs. scale population; expected dilution quantified or reasoned
- [ ] Vital sign #3: the winning condition named and tested for replicability across every scaled site
- [ ] Vital sign #4: at least one scale-only spillover (congestion, saturation, competitive/price response) explicitly modeled, not assumed away
- [ ] Vital sign #5: marginal cost trend at volume traced and the scarce input identified
- [ ] Weakest link named, cheapest de-risking test specified, and verdict (SCALE / DE-RISK FIRST / DO NOT SCALE) recorded

## Sources

- **List, J. A. (2022). *The Voltage Effect: How to Make Good Ideas Great and Great Ideas Scale.* Currency / Penguin Random House. ISBN 978-0593239483.** The primary source; defines the voltage effect and the five vital signs. Verbatim: *"The vast majority of ideas—no matter how great they seem at first blush—don't scale. And it's often not until we take these ideas to scale that we discover their fatal flaws."* Publisher page: https://www.penguinrandomhouse.com/books/652077/the-voltage-effect-by-john-a-list/
- **List, J. A. (2011). "Why Economists Should Conduct Field Experiments and 14 Tips for Pulling One Off." *Journal of Economic Perspectives*, 25(3), 3–16.** https://www.aeaweb.org/articles?id=10.1257/jep.25.3.3 — List's own account of field-experiment method, including the warnings about representativeness and scaling that underlie vital signs #2–#3. List's argument, in paraphrase: field experiments combine the naturally-occurring realism of the world with the clean identification of a treatment effect that experimental control provides.
- **Al-Ubaydli, O., List, J. A., & Suskind, D. (2017). "What Can We Learn from Experiments? Understanding the Threats to the Scalability of Experimental Results." *American Economic Review: Papers & Proceedings*, 107(5), 282–286.** https://www.aeaweb.org/articles?id=10.1257/aer.p20171115 — the peer-reviewed statement of the scalability threats (statistical inference / false positives, representativeness of the population and situation, and general-equilibrium/spillover and supply-side effects) that *The Voltage Effect* later popularized.
- **List, J. A., Momeni, F., & Zenou, Y. (2020). "The Social Side of Early Human Capital Formation" (and related Chicago Heights / Griffin Early Childhood Center working papers).** NBER Working Paper series — documents the early-childhood field experiments List draws on when illustrating scaling threats. Used for the Method-in-Action case with qualified language where figures are approximate.

*Not cited and why:* No press write-ups of Pets.com, Krispy Kreme, or Groupon are treated as primary; those examples rely on the companies' own SEC filings and List's framework, and are flagged in their example files where any figure is approximate rather than asserted as precise.

---

*Part of **deciqAI Knowledge Skills** — 225 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/voltage-effect** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
