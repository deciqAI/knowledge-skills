# Method in Action: Galileo Falling Bodies + Einstein Light Beam + Modern Strategic Applications

> *Example for the [thought-experiment](../SKILL.md) skill.*

**Galileo's chained-balls argument** (~1638) is the canonical refutation-via-thought-experiment. The argument's structure:

1. **Premise:** Aristotle's claim that heavier objects fall faster than lighter ones, proportional to weight.
2. **Construction:** Consider two stones, weights w₁ and w₂, with w₁ > w₂.
3. **By premise:** w₁ falls faster than w₂.
4. **Tie them together** with a string and release as a combined object of weight (w₁ + w₂).
5. **Inference A:** The combined object, being heavier than w₁, should fall faster than w₁.
6. **Inference B:** But the lighter stone w₂ (which falls slower) should drag on w₁, slowing the combined object below w₁'s natural speed.
7. **Contradiction:** The combined object both falls faster than w₁ (by A) and slower than w₁ (by B).
8. **Conclusion:** Aristotle's premise must be wrong — weight does not determine fall speed.

The thought experiment did not require any physical experimentation. The reasoning was clean enough to refute 2000 years of scholarship through pure logic. Galileo's later empirical work (rolling balls down inclined planes, etc.) confirmed the conclusion that fall speeds are independent of weight (modulo air resistance), but the thought experiment alone was enough to refute the Aristotelian view.

**Einstein's chasing-a-light-beam** thought experiment (~1895, formalized in 1905) is the other canonical case. Einstein, then a teenager, asked: what would I see if I rode alongside a beam of light at the speed of light?

- **Classical mechanics:** I would see the light beam as stationary (just as a person on a train sees a fellow passenger as stationary). This was the Galilean-relativity expectation.
- **Maxwell's equations** (the foundational equations of electromagnetism, well-established by 1865): predict that light travels at c relative to every observer, regardless of the observer's motion. By Maxwell, the light beam cannot appear stationary even to an observer moving at c.
- **Contradiction:** Classical mechanics and Maxwell's equations gave incompatible predictions for the same physical scenario.

Einstein could not resolve this within classical physics. The resolution, worked out over the following 10 years, was the special theory of relativity (1905): the classical assumption that simultaneity is absolute is wrong; time and space must transform such that all observers measure light at c. The thought experiment had revealed an inconsistency that no empirical test had yet found, and the resolution was a profound revision of physics.

**Modern strategic thought experiments** follow the same structure, applied to business decisions:

**Bezos's 1000x Amazon experiment.** "What if Amazon were 1000 times larger? What infrastructure would be needed? What products / services would have to exist?" The thought experiment forced consideration of computing infrastructure at scale. The realization: Amazon's internal infrastructure (compute, storage, databases) would itself be a sellable product. AWS launched 2006 and grew into a $80 billion+ business by 2024 — entirely driven by the prior thought experiment that asked "what would be true if we were 1000x larger?"

**Bezos's regret-minimization framework.** When deciding whether to leave D.E. Shaw and start Amazon in 1994, Bezos used a thought experiment: "Imagine I'm 80, looking back at my life. Will I regret not having tried Amazon?" The thought experiment surfaced the long-term regret framing that led to the decision. See [`regret-minimization`](../skills/regret-minimization/SKILL.md).

**Charlie Munger's "invert always invert."** Munger's discipline of thinking backward from disaster is a class of thought experiment: imagine the catastrophic outcome, work backward to what could cause it, then design to prevent. See [`inversion`](../skills/inversion/SKILL.md).

**Premortem analysis** (Klein 2007). The structured premortem is a thought experiment with specific format: imagine the project has failed catastrophically 12 months from now; reason backward to what went wrong; surface failure modes that prospective planning misses. See [`premortem`](../skills/premortem/SKILL.md).

**Rawls's veil of ignorance** (1971). A famous ethical-policy thought experiment: imagine you must design society without knowing whether you'll be born rich/poor, strong/weak, talented/limited. What principles would you choose? The thought experiment surfaces hidden interests in policy debates.

**The trolley problem** (Foot 1967). The ethical thought experiment in which you must decide whether to redirect a runaway trolley to kill one person instead of five. Thousands of versions have been constructed to surface what moral intuitions are doing.

Three operational lessons:

**First, the discipline is in the premises.** Thought experiments are only as reliable as their starting premises. The Galilean refutation works because Aristotle's premise (weight determines fall speed) was specific and refutable. Many failed thought experiments fail because their premises smuggle in conclusions or rely on contested assumptions.

**Second, the value is often in surfacing hidden assumptions, not in producing conclusions.** A thought experiment that produces a surprising conclusion often does so because the conclusion contradicts a hidden assumption you didn't know you held. The surprise is the diagnostic; the value is in identifying what you assumed.

**Third, thought experiments work when empirical testing is impossible or too costly.** They're not better than experiments; they're an available substitute when experiments aren't. For founders facing strategic decisions that cannot be A/B tested, thought experiments are often the only available rigor.
