# Method in Action: Kahneman and Tversky's 1979 Prospect Theory

> *Example for the [loss-aversion-prospect-theory](../SKILL.md) skill.*

The 1979 paper that founded prospect theory was the culmination of a decade of work by Daniel Kahneman and Amos Tversky at Hebrew University, then at the Center for Advanced Study in the Behavioral Sciences at Stanford. The pair had already published the seminal "Judgment under Uncertainty: Heuristics and Biases" (1974, *Science*), which established availability, representativeness, and anchoring as systematic violations of probability theory. The 1979 paper extended the program to decisions under risk.

The motivating puzzle: classical economics, axiomatized by von Neumann and Morgenstern in 1944, said rational agents should maximize the expected value of a concave utility function over total wealth. This framework explained risk aversion (people prefer a sure $X to a 50% chance of $2X). But it failed to explain a series of empirical anomalies:

- The Allais paradox (1953), in which subjects' choices over lotteries systematically violated the independence axiom of expected utility theory.
- The fact that the same person buys both lottery tickets (risk-seeking for small-probability large-payoff gambles) and insurance (risk-averse for small-probability large-loss events).
- The equity premium puzzle: stock returns historically outperform bonds by more than rational risk aversion alone can justify.
- The "Asian disease" framing effect (Tversky-Kahneman 1981, separately): the same decision is made differently depending on whether outcomes are presented as gains saved or losses incurred.

Prospect theory's contribution was a single descriptive model that predicted all of these anomalies. The model had two components:

**The value function v(x)**, replacing the expected utility u(x):

- Defined over *changes* from a reference point, not absolute wealth.
- Concave for gains (v'' < 0 when x > 0).
- Convex for losses (v'' > 0 when x < 0).
- Steeper for losses than for gains (loss aversion: |v(−x)| > v(x), with the 1992 estimate ≈ 2.25:1).

**The probability weighting function π(p)**:

- π(0) = 0, π(1) = 1.
- π(p) > p for small p (overweighting of small probabilities).
- π(p) < p for moderate-to-large p (underweighting of moderate-to-large probabilities).
- Subadditive: π(p) + π(1−p) < 1 (subjective probabilities don't sum to certainty).

The combined "value" of a prospect is then Σ π(pᵢ) × v(xᵢ), where outcomes are evaluated as deviations from the reference point.

Kahneman and Tversky tested the model with a series of choice problems, including the gain-loss asymmetry shown above, the certainty effect (Allais paradox), and the reflection effect (preferences reverse when outcomes are negated). The consistency of the results across hundreds of subjects and dozens of problems established prospect theory as the dominant descriptive theory.

From the paper itself:

> "The present analysis suggests that, in addition to the curvature of the value function, the probability weighting function plays an important role in the explanation of risk attitudes. The certainty effect, the reflection effect, and the isolation effect are all consequences of the discrepancy between the curvature of v in the loss and gain regions, and the nonlinear weighting of probabilities. These phenomena, which are robust and not artifacts of artificial laboratory tasks, suggest that the standard model of choice — expected utility theory with concave utility — must be replaced by a model that allows for reference dependence, loss aversion, and probability distortion."
>
> — Kahneman & Tversky (1979), pp. 286-287.

The 1992 cumulative extension addressed an internal inconsistency in the original theory (it violated stochastic dominance in some edge cases) and produced the modern version, "cumulative prospect theory":

> Tversky, A., & Kahneman, D. (1992). "Advances in prospect theory: Cumulative representation of uncertainty." *Journal of Risk and Uncertainty*, 5(4), 297-323.

Empirical follow-up over 40+ years has established the four findings as cross-culturally robust:

**Thaler, R. H. (1980).** "Toward a positive theory of consumer choice." *Journal of Economic Behavior & Organization*, 1(1), 39-60. Documented the endowment effect (people demand more to give up a possession than they would pay to acquire it) — a direct prediction of prospect theory.

**Tversky, A., & Kahneman, D. (1981).** "The framing of decisions and the psychology of choice." *Science*, 211(4481), 453-458. The "Asian disease" framing study — same decision flipped by gain/loss framing.

**Samuelson, W., & Zeckhauser, R. (1988).** "Status quo bias in decision making." *Journal of Risk and Uncertainty*, 1(1), 7-59. Status quo bias as a reference-point phenomenon.

**Benartzi, S., & Thaler, R. H. (1995).** "Myopic loss aversion and the equity premium puzzle." *Quarterly Journal of Economics*, 110(1), 73-92. Explained the equity premium puzzle via prospect theory + frequent portfolio evaluation.

**Camerer, C. F. (2005).** "Three cheers — psychological, theoretical, empirical — for loss aversion." *Journal of Marketing Research*, 42(2), 129-133. Meta-analysis and defense of the loss-aversion finding's robustness.

**Gal, D., & Rucker, D. D. (2018).** "The loss of loss aversion: Will it loom larger than its gain?" *Journal of Consumer Psychology*, 28(3), 497-516. A critique arguing that the 2:1 ratio is overstated in many domains; the actual ratio varies with stakes, domain, and individual differences. Important methodological refinement, not refutation.

**Camerer, C., Babcock, L., Loewenstein, G., & Thaler, R. (1997).** "Labor supply of New York City cabdrivers: One day at a time." *Quarterly Journal of Economics*, 112(2), 407-441. Famous applied demonstration: cab drivers quit early on high-fare days (reference-dependent income targeting) when an EV-maximizer would work longer on those days. Real-world money, real-world behavior, prospect-theory-predicted.

The framework has reshaped multiple operational disciplines:

**Behavioral economics as a field.** Prospect theory is the foundational paper. Modern behavioral econ (Thaler's Nobel work, the field of behavioral finance, "Nudge" policy interventions) all derive from this base.

**Investment management.** Disposition effect (selling winners too early, holding losers too long), home bias, equity premium puzzle — all predicted by prospect theory. Modern behavioral funds (e.g., Fuller & Thaler Asset Management) explicitly trade against these patterns.

**Insurance and product design.** The way insurance products are framed (deductibles, partial payouts, "you save X by bundling") leverages reference-point and loss-aversion mechanics. Same product re-framed can have wildly different adoption.

**Pricing strategy.** Discounting from a high "anchor" price (vs. always-low pricing) leverages prospect theory: $1000 marked down to $500 feels like a $500 gain; $500 priced directly is just $500 spent. Same physical price; different psychological frame.

**Negotiation.** Anchoring (Tversky-Kahneman 1974) and reference-point manipulation (prospect theory) are the twin engines of negotiation tactics. A skilled negotiator opens with an anchor that makes the target's eventual concession feel like a loss-frame gain ("you got it down by $X from my opening").

**Public policy ("Nudge").** Cass Sunstein and Richard Thaler's "choice architecture" framework (2008) uses default-setting (status quo bias), framing, and reference points to shift behavior without restricting choice. Major applied use: organ donation defaults, retirement savings auto-enrollment.

**Medical decision-making.** Patients' willingness to undergo surgery shifts dramatically based on whether outcomes are framed as survival rates (gain frame) or mortality rates (loss frame). Same statistics, different choices. Clinical decision support tools are being redesigned with this in mind.

**Marketing.** Free trials (creating an endowment that loss-aversion then resists giving up), free shipping framed as "loss" if added later, "limited time" framing (scarcity + loss aversion) — all prospect-theory applications. The empirical effect sizes on conversion are enormous.

Three operational lessons from Kahneman-Tversky:

**First, the reference point is the decision.** Whoever frames the decision sets the reference point, and whoever sets the reference point determines whether the chooser is in gain-mode (risk averse) or loss-mode (risk seeking). The most important strategic choice in many decisions is what the comparison baseline is.

**Second, loss aversion is asymmetric, not symmetric vigilance.** Awareness of the 2:1 ratio is necessary but not sufficient to correct it. The correction comes from forcing yourself to compute expected value and explicitly noting "I am about to choose against EV because the loss frame is more salient — is the irreversibility/catastrophe magnitude actually that high?"

**Third, probability weighting reverses depending on probability magnitude.** This is the crucial counterintuitive piece. People over-insure small probabilities (catastrophe insurance with bad value) and under-insure moderate-to-large probabilities (no flu shot, no will, no rainy-day fund). The corrective is to use explicit numerical probability, not verbal descriptions ("rare," "common," "unlikely"), and to compute expected loss explicitly.
