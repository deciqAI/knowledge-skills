# Method in Action: Tversky & Kahneman 1972 + 1983 — The Linda Problem

> *Example for the [representativeness-heuristic](../SKILL.md) skill.*

**Amos Tversky** (1937–1996) and **Daniel Kahneman** (b. 1934) formed the most productive collaboration in the history of behavioral science. Their program, begun in the late 1960s, systematically documented the ways in which human intuitive probability judgment departs from normative statistical reasoning. Kahneman won the Nobel Prize in Economics in 2002 (Tversky had died in 1996; the prize is not awarded posthumously).

The 1972 *Cognitive Psychology* paper introduced the concept and named the three major heuristics: representativeness, availability, and anchoring-and-adjustment. Representativeness was the most theoretically central: it explained base rate neglect, the conjunction fallacy, and insensitivity to sample size within a single framework — the tendency to judge probability by resemblance to a prototype.

The 1983 paper delivered the decisive empirical demonstration through the Linda problem. The design was methodologically elegant: the description of Linda was constructed to be maximally representative of a feminist activist and minimally representative of a bank teller. The conjunction question — "bank teller" vs. "bank teller AND feminist" — was a logical trap. Option B is a strict subset of option A; it cannot be more probable. Yet 85–89% of respondents across multiple studies (including statistically trained graduate students at Stanford and British Columbia) chose B.

Tversky and Kahneman's framing of the significance:

> "The conjunction fallacy is not a fringe phenomenon. It was observed in 89% of the respondents who encountered the feminist bank teller problem in a standard format. ... A conjunction can appear more probable than one of its constituents if it represents a more coherent and plausible story."
>
> — Tversky & Kahneman (1983), p. 308.

The key insight: **coherence is not probability.** A detailed, specific, narrative-consistent description feels more probable because it is easier to imagine — but every added detail reduces the probability of the conjunction. The more a story "fits," the lower its mathematical probability. Representativeness confuses "fit" with "frequency."

**Venture capital application.** In VC screening, the representativeness heuristic produces systematic overrating of founders who match the prototypical "successful startup founder" profile: technical co-founder, aged 22–32, pedigreed university (Stanford/MIT/Harvard dropout), prior experience at a top company, operating in a software-based market. These characteristics are associated with the portfolio of successful companies — but they are drawn from a survivorship-biased sample. The base rate for any individual VC-backed startup (regardless of founder profile) failing within 10 years is approximately 75–90%, depending on definition of failure.

When a founder matches the prototype strongly, the base rate is effectively ignored. The investment decision is driven by representativeness ("this is what a winner looks like") rather than calibrated probability. The conjunction fallacy compounds the error: "technically excellent AND market-focused AND team-complete AND in the right sector" is judged as more probable than any single dimension — but the actual probability is the product of each dimension's probability, all less than 1.

The Bayesian correction in VC practice: before assessing the profile, anchor to the base rate. "Startups in this sector/stage/geography fail at X% rate. How much does this specific profile shift that prior?" Even a very strong profile typically shifts a 75% failure rate to 60% — not to 20%. The uncalibrated representativeness-based judgment ("this one is different, this is a winner") produces a 20% estimate. The calibrated judgment is 60%.

**Hiring application.** A candidate who "looks like" your best performer — shares the same university, previous employer, communication style, and extracurricular profile — is rated more likely to succeed. The base rate of success in the role (which for most knowledge work positions is 50–70% depending on definition) is displaced by the profile match. Research by Tversky and Kahneman, and subsequent work by Kahneman, Klein, and others, consistently shows that unstructured interview assessments relying on profile matching are only marginally better than chance at predicting performance — precisely because representativeness dominates base rate reasoning.

The correction: structured job-relevant skill assessment replaces holistic profile matching. The base rate for this role's success in the population of similarly credentialed candidates is the prior; each structured assessment is evidence that updates the prior.

**Three operational lessons:**

1. **The question to ask before every profile judgment:** "What is the base rate for this outcome in people I cannot describe individually?" If the answer to that question is well below the current probability estimate, representativeness is likely inflating the estimate.

2. **The conjunction test:** every time a decision involves multiple favorable attributes simultaneously ("she's X and Y and Z"), compute the conjunction probability. Each attribute's probability is less than 1; the conjunction is always less than the minimum component. If the conjunction was rated as highly probable, the conjunction fallacy is active.

3. **Audit the prototype for survivorship bias.** The prototypical "successful founder" / "successful hire" / "successful product" was built from the visible successes. Every failure that looked similar is invisible. The prototype over-represents success; it is not a probability model; it is a survivorship-biased archetype.
