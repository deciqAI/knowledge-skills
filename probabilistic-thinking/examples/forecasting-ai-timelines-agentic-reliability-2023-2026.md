# Method in Action: Forecasting AI Timelines and Agentic Reliability (2023–2026)

> *Example for the [probabilistic-thinking](../SKILL.md) skill.*

A worked example on the hardest kind of forecast: one where the reference class is thin, the incentives are loud, and the question is often phrased so vaguely it cannot be scored.

Between 2023 and 2026, "when will we get AGI?" and "when will AI agents be reliable enough to run production workflows unattended?" became boardroom, investor, and policy questions. The public discourse was full of point predictions — "AGI by 2027," "agents will replace X% of jobs" — usually stated with confidence, rarely stated in a form that could ever be checked. Superforecasting-style discipline does not tell you the answer; it tells you how to hold the question so you can be measurably wrong and get better. Walk the Probability Estimate through it.

**Step 1 — Precise question + deadline.** "When AGI?" is unscorable: no agreed definition, no deadline, no resolution criterion. Convert it into something a scorekeeper could adjudicate. Two contrasting examples:
- *Bad (unscorable):* "Will we have AGI soon?"
- *Better (scorable):* "Will a publicly available AI system complete a specified suite of multi-step, real-world office tasks end-to-end at a defined success threshold, verified by an independent benchmark, before 2027-12-31?"

The second version names the outcome, the bar, the verifier, and the deadline. Note that even here the definition (which benchmark, what threshold) does most of the work — an honest forecaster surfaces that the disagreement is often about *definitions*, not *odds*.

**Step 2 — Anchor in a base rate.** There is no clean reference class of prior AGI arrivals, so this is closer to Knightian uncertainty than to an actuarial table. Use *proxy* reference classes and say so:
- Historical accuracy of expert technology-timeline forecasts (generally poor and over-optimistic near hype peaks).
- The base rate of "the last 10% of reliability takes most of the effort" in prior autonomy pushes — self-driving cars are the canonical cautionary case: impressive demos from the mid-2010s did not translate into broad unsupervised deployment on the timelines predicted.
- Benchmark-saturation cadence: through 2023–2025, frontier models saturated many static benchmarks faster than expected, which pushes *some* estimates earlier — a signal in the opposite direction.

The honest output of Step 2 is a range and a caveat, not a point. Naming the reference class is the load-bearing act; a probability without one is undefined (the one-shot probability fallacy).

**Step 3 — Evidence for and against, each tagged.**
- Rapid, repeated capability jumps on reasoning and coding tasks across model generations (2023–2025). ↑ moderate.
- Real, growing enterprise adoption and large capital commitments to AI infrastructure. ↑ weak for *capability*, because spending reflects belief, not demonstrated reliability — a signal about sentiment, not about the physics of the problem.
- The gap between demo success and reliable unattended operation: agents that work in a scripted demo still fail on long-horizon, high-variance real tasks. ↓ strong.
- Compounding error over multi-step chains: a per-step success rate that looks high still collapses over long horizons. ↓ strong, and structural.
- Verification/evaluation itself is unsolved for open-ended tasks — you cannot deploy unattended what you cannot cheaply check. ↓ moderate.

Be uncharitable in *both* directions. The bull case must confront error compounding; the bear case must confront the genuine, repeated benchmark surprises.

**Step 4 — Bayesian update (plain language).** For each signal ask P(we'd see this | the milestone lands by the deadline) vs P(we'd see this | it doesn't). Capability jumps are more likely in the "lands" world, so they shift up — but only moderately, because they were *also* fairly likely in the "doesn't land soon" world (impressive demos preceded the self-driving disappointment too). Persistent long-horizon failure and error compounding are far more likely in the "doesn't land" world, so they pull down harder. The superforecaster's characteristic move: update *often* (each model release, each benchmark result) but *less drastically* than the headlines — resist both the launch-day euphoria and the failure-mode dunk. Capex and valuations move sentiment, not the underlying reliability curve, so they should barely move a *capability* forecast even as they dominate the news.

**Step 5 — Number + confidence interval.** State a number with a wide, honest band, e.g. *"~35%, 80% CI 15–60%, that the defined benchmark-verified milestone is met before 2027-12-31"* — with the explicit caveat that the band is wide because this is proxy-reference-class / partly-Knightian territory, and that the estimate is hostage to how the milestone is defined. The illustrative number matters far less than the discipline: a point with a wide CI and a named reference class beats a confident "2027" with neither. Pseudo-precision ("62.4% AGI by 2027") is the tell of someone who has not done Step 2.

**Step 6 — Most-informative next evidence.** Name observables that would move the estimate most: an *independent, contamination-controlled* benchmark on long-horizon agentic tasks (not a vendor's own demo); measured multi-step task-completion rates over long horizons rather than single-shot accuracy; evidence on whether verification/evaluation scales. If a piece of news would not move your number — another funding round, another slogan — it is sentiment, not evidence.

**Step 7 — Calibration log.** Write the estimate down with date and resolution criteria, and *score it later*. This is the antidote to the discourse: pundits who said "AGI by 2025" in 2023 rarely revisit the claim. A forecaster who logged "35%, resolves 2027-12-31, criterion = benchmark X at threshold Y" can compute a Brier score and improve. Being scorable is the point.

The payoff mirrors the Good Judgment finding: the win is not calling the date. It is thinking in distributions instead of point estimates, separating the capability question from the capex/valuation noise wrapped around it, and producing forecasts you can be measurably wrong about — the only kind you can get better at.

*Sources: Tetlock, Philip E. & Gardner, Dan. *Superforecasting: The Art and Science of Prediction*. Crown, 2015 — the base-rate-first, incremental-update discipline applied here. Grace, Katja et al. "Thousands of AI Authors on the Future of AI" (AI Impacts / Katja Grace et al., 2024 survey of published ML researchers) — documents the wide dispersion and instability of expert AI-timeline forecasts. Metaculus AI forecasting questions (https://www.metaculus.com/questions/) — a public, resolution-criteria-based platform illustrating how AGI/agentic-capability questions must be operationalized to be scorable. Waymo/Cruise self-driving deployment history (widely reported 2016–2024) — the canonical "last 10% of reliability" cautionary reference class. Knight, Frank H. *Risk, Uncertainty, and Profit*, 1921 — the risk-vs-Knightian-uncertainty distinction invoked in Step 2.*
