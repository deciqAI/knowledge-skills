# Method in Action: The Search for Air France Flight 447 (2009–2011)

> *Example for the [bayesian-reasoning](../SKILL.md) skill.*

The search for the wreckage of Air France Flight 447 is one of the best-documented modern applications of Bayesian reasoning to a physical search — and a demonstration that a disciplined update on *negative* evidence, with an honest likelihood model, can succeed where two years of intuition-guided searching failed.

On June 1, 2009, AF 447 crashed into the equatorial Atlantic en route from Rio de Janeiro to Paris, killing all 228 aboard. Floating debris was recovered within days, but the wreckage — and the flight recorders needed to establish the cause — lay on the ocean floor at roughly 3,900 meters depth. Three search phases in 2009–2010, including a passive acoustic search for the recorders' underwater locator beacons and wide-area side-scan sonar surveys, covered enormous swaths of seabed and found nothing.

In 2010, France's accident-investigation bureau (BEA) commissioned Lawrence Stone and colleagues at Metron, Inc. to build a formal Bayesian posterior distribution for the wreck's location — the same methodology Stone's school of search theory had used to help locate the sunken submarine USS Scorpion in 1968.

**The hypothesis space (Step 1).** The wreck lies in exactly one cell of a grid covering a 40-nautical-mile-radius circle around the aircraft's last known position (LKP) — the maximum distance the aircraft could have traveled after its final position report. The cells are exhaustive and mutually exclusive.

**The prior (Step 2).** Anchored *before* re-weighing the search evidence, as a weighted mixture of independent scenario models: flight-dynamics analysis of possible trajectories after the LKP, data on where commercial aircraft in loss-of-control accidents have hit relative to their last known position, and reverse-drift models projecting recovered bodies and debris backward through currents and wind to an impact point. No single story was trusted; each model contributed probability mass in proportion to its assessed credibility.

**The likelihood ratio of negative evidence (Step 3).** Each unsuccessful search was treated as evidence E = "sensor passed over the area and detected nothing." For any cell actually searched, P(E | wreck in cell) = 1 − the sensor's detection probability there; for unsearched cells, P(E | wreck elsewhere) ≈ 1. The likelihood ratio is below 1 for searched cells — so failed searches *shrink* a cell's probability in proportion to how good the sensor was, but never to zero.

**The decisive move — questioning P(E | H).** The 2009 acoustic search had passed near the LKP and heard no beacon pings, and searchers had largely written that area off. Stone's team refused to treat "no pings" as proof of "no wreck": the update is only as strong as the assumption that the beacons were transmitting. They assigned a material probability that both beacons had been destroyed or had failed in the crash. Weighting the negative acoustic evidence by that failure probability collapsed its likelihood ratio toward 1 — and the seabed near the LKP retained substantial posterior mass instead of being falsely "cleared." (Examination after recovery indicated the beacons had indeed not been functioning as assumed.)

**The posterior (Step 4).** Multiplying the prior by the accumulated likelihoods of every search outcome produced a posterior map whose probability concentrated in an unswept region close to the LKP. BEA used this map to plan the fourth search phase.

**The result.** In April 2011, about one week after autonomous underwater vehicles began sweeping the high-posterior region, the debris field was found on the seabed near the LKP, inside the area the Bayesian analysis had flagged. The flight recorders were recovered the following month, and BEA's final report on the accident followed in 2012. Two years of searching guided by strong intuitions had failed; one week guided by a posterior distribution succeeded.

The mapped steps:

1. **Name hypothesis and alternatives:** the wreck is in exactly one cell of a grid over the 40 NM circle around the LKP — exhaustive and mutually exclusive.
2. **Anchor the prior before evidence:** a weighted mixture of flight-dynamics, historical-crash, and reverse-drift models, committed before re-analysis of the search data.
3. **Estimate the likelihood ratio:** for each failed search, LR = P(no detection | wreck here) / P(no detection | wreck elsewhere), driven by sensor detection probability — and critically, discounted by the probability the acoustic beacons never transmitted.
4. **Compute the posterior:** prior × accumulated likelihoods → a posterior map concentrating near the LKP.
5. **Check evidence dependence:** the acoustic "all clear" was conditional on a single common factor — working beacons — so it could not be compounded at face value across the area it covered.
6. **Commit and act:** search effort was allocated to the highest-posterior cells; the wreck was found within a week.

The operational lesson: negative evidence only rules out a hypothesis to the degree that P(E|H) is genuinely low. When a search sensor, a test, or a monitor can fail silently, "we looked and saw nothing" carries a likelihood ratio much closer to 1 than it feels — and the vivid conclusion "it's not there" is an over-update.

Primary source: Stone, L. D., Keller, C. M., Kratzke, T. M., & Strumpfer, J. P. (2014). "Search for the Wreckage of Air France Flight AF 447." *Statistical Science*, 29(1), 69-80. https://doi.org/10.1214/13-STS420. Methodological foundation: Stone, L. D. (1975). *Theory of Optimal Search.* Academic Press.
