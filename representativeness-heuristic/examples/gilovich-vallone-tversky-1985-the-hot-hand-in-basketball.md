# Method in Action: The Hot Hand in Basketball (1985)

> *Example for the [representativeness-heuristic](../SKILL.md) skill.*

In the early 1980s, virtually everyone in professional basketball — players, coaches, broadcasters, fans — shared one conviction: a player who has just made several shots in a row is "hot" and more likely to make the next one. Thomas Gilovich, Robert Vallone, and Amos Tversky put that conviction to the test against the actual shooting records, and the result became one of the most famous field demonstrations of the representativeness heuristic operating outside the laboratory.

**The judgment and the profile (Step 1).** The probability estimate: "this player will make the next shot." The driver: a vivid, salient streak — three or four consecutive makes. In their survey of basketball fans, the overwhelming majority (roughly nine in ten respondents) agreed that a player has a better chance of hitting a shot after making two or three in a row than after missing two or three. Players themselves reported the same belief and said they fed the "hot" teammate accordingly.

**The reference class and base rate (Step 2).** The relevant reference class is the player's overall field goal percentage — his base rate. Gilovich, Vallone, and Tversky analyzed the detailed 1980–81 shot records of the Philadelphia 76ers, free-throw records of the Boston Celtics, and a controlled shooting experiment with Cornell varsity players. The base rate was available in every case; the streak-based belief simply overrode it.

**The representativeness mechanism (Step 3).** Here the bias is *insensitivity to the true behavior of random sequences* — the third systematic error the heuristic produces. People expect a chance process to look locally representative of its overall rate: in a 50% shooter, they expect alternation, not runs. But genuine random sequences produce streaks far more often than intuition allows. So when normal chance streaks appear, observers reject randomness and infer a causal state ("hot"). The streak *resembles* the prototype of non-random skill, so it is judged to be non-random.

**The correction against data (Step 4).** The analysis found no positive serial correlation: hit rates following streaks of makes were not higher than hit rates following misses — in the 76ers data they were, if anything, slightly lower. The Bayesian move the fans skipped: start from the player's base rate, then ask how much a short streak should shift it. Given how easily chance produces short streaks, the likelihood ratio is close to 1; the posterior stays near the base rate.

**The prototype audit (Step 5).** The "hot player" prototype was built from remembered streaks — vivid, celebrated, replayed. Equally long streaks that ended in a miss, and the far more numerous unremarkable sequences, never entered the prototype. Memory sampled the pattern, not the distribution.

**The honest coda.** The story did not end in 1985. Miller and Sanjurjo (2018) identified a subtle selection bias in the conditional-probability estimator Gilovich, Vallone, and Tversky used: computing hit rates after streaks within finite sequences is biased downward, so a truly modest hot-hand effect could hide behind an apparently null result. Their re-analysis found evidence of a real, if smaller-than-believed, hot hand in the controlled-shooting data. The corrected lesson is two-sided: fans massively overestimated the effect via representativeness — and researchers then needed careful statistics to detect what little of it was real. Both errors were failures to reason about small samples correctly; neither rehabilitates streak-based intuition as a decision rule.

**Transfer beyond sports.** The identical structure drives "hot" fund managers (three winning years read as skill, though chance alone produces such runs in large manager populations), "hot" sales reps, and "streaky" product launches. Whenever a short run of outcomes triggers a causal-state inference — hot, in the zone, on a roll — run the same audit: state the base rate first, ask how often pure chance produces a run this long in a sample this size, and only then decide whether the streak is evidence of anything.

The mapped steps:
1. Identify judgment + profile: "he'll make the next one" — driven by a vivid streak, not a rate
2. Reference class + base rate: the player's season field goal percentage, available but ignored
3. Mechanism test: expectation of local representativeness makes normal chance streaks look causal
4. Bayesian correction: short streaks carry a likelihood ratio near 1 — posterior ≈ base rate
5. Prototype audit: the "hot" prototype was assembled from remembered highlights, a biased sample
6. Calibrated output: bet the base rate; treat streak talk as narrative, not evidence — while noting (per Miller & Sanjurjo) that a small genuine effect may exist

Primary source: Gilovich, T., Vallone, R., & Tversky, A. (1985). "The Hot Hand in Basketball: On the Misperception of Random Sequences." *Cognitive Psychology*, 17(3), 295–314. https://doi.org/10.1016/0010-0285(85)90010-6

Re-analysis: Miller, J. B., & Sanjurjo, A. (2018). "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers." *Econometrica*, 86(6), 2019–2047.
