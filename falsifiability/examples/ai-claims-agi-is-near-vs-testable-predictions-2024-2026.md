# Method in Action: Separating Falsifiable from Unfalsifiable AI Claims (2024–2026)

> *Example for the [falsifiability](../SKILL.md) skill.*

Between 2024 and 2026, public discourse around large AI models filled with two very different kinds of statement. Some were slogans — "AGI is near," "the model truly understands," "scaling will just keep working" — and some were concrete, dated predictions with numbers attached. Popper's criterion sorts them cleanly: a claim is empirical knowledge only if you can say in advance what observation would prove it wrong. This walkthrough runs the anchor claims through the falsifiability skill's own six-step Process.

## Step 1 — State the claim

Take three representative claims from the period:

- **Claim A (slogan):** "AGI is near."
- **Claim B (mentalistic):** "The model *truly understands* what it's saying."
- **Claim C (testable):** "By the end of 2025, a frontier model will exceed a specified accuracy threshold on the competition-mathematics benchmark AIME," or similar dated, metric-bound predictions of the kind researchers publish.

*Who asserts them:* executives, commentators, and researchers, respectively. *Decision at stake:* whether an enterprise should bet a roadmap (or an investor a position) on imminent general capability. *Current evidential basis:* rapid, genuine benchmark gains from roughly 2023 onward, plus extrapolation.

## Step 2 — Test whether empirical

- **Claim A ("AGI is near")** is empirical *only if* "AGI" and "near" are defined. As typically used, neither is: "AGI" has no agreed operational definition, and "near" has no date. Without those, it is not yet a testable claim — it is a mood.
- **Claim B ("truly understands")** invokes an inner mental state. As stated it is closer to metaphysics than to empirical science: no external observation is specified that would distinguish "truly understands" from "produces the same outputs without understanding." Step 2 says: if it stays non-empirical, stop and label it belief.
- **Claim C** is empirical: it is a statement about a measurable score on a fixed benchmark by a fixed date.

## Step 3 — Specify falsification conditions

Force each claim to complete: *"This would be falsified if I observed: ___."*

- **Claim A** can be *rescued into* an empirical claim by pinning it down — e.g. "A single model will pass [a specified operationalization, such as the ARC-AGI abstraction-and-reasoning benchmark at human-level, or a stated economically-valuable-task bar] before 31 December 2026." Now it can fail. Note the discipline: the version that can be proven wrong is the only version worth arguing about.
- **Claim B** resists completion. "Understanding" that predicts no observable difference from "not understanding" has no falsification condition. The productive move is to *replace* it with a behavioral proxy that does — e.g. "the model will maintain accuracy when the same problem is presented with surface features (names, numbers, framing) changed," which is testable and, as documented in 2024–2025 work on reasoning robustness, sometimes fails.
- **Claim C** already has its condition: *falsified if the reported score is below the stated threshold on the stated date.*

## Step 4 — Plan to observe

- *When observable:* Claim A at its stated deadline; Claim C at the benchmark's next reported evaluation; the Claim-B proxy on demand via a perturbed test set.
- *How measured / who tracks:* published benchmark results and independent replications; assign a named owner to record the number when it lands, not to reinterpret the slogan afterward.
- *Threshold for "falsified":* the pre-stated number and date. A crucial guardrail specific to AI benchmarks — **contamination**: if the evaluation items may have appeared in training data, a high score does not confirm the capability claim, so the observation plan must include held-out or post-cutoff items.

## Step 5 — Pre-commit to action

- If the operationalized **Claim A** deadline passes unmet: downgrade "imminent AGI" from a planning premise to a possibility, and stop staking irreversible roadmap bets on it.
- For **Claim B**: if perturbation collapses performance, treat the system as pattern-competent but not robustly understanding, and design guardrails accordingly.
- **Ad-hoc preservation risk (the core failure mode here):** the stock defenses — "it's *almost* AGI," "the benchmark was flawed," "true AGI is just around the corner," "you're moving the goalposts" — are exactly the moves Popper flagged. Each rescue that explains away a missed prediction without a *new* falsifiable commitment converts the claim back into unfalsifiable belief.

## Step 6 — Iterate

- **Confirmed** (Claim C threshold met on clean data): keep monitoring; a passed test is not a general guarantee, only a survived attempt.
- **Falsified** (deadline missed, proxy collapses): revise or abandon the stronger claim rather than defending it.
- **Unfalsifiable** (Claim B left as "it just understands"): recognize it as belief and route the actual decision through the behavioral proxies instead.

## The operational lesson

The right question to put to any 2024–2026 AI capability or safety claim is the skill's highest-leverage one: **"What specific evidence, observable by when, would prove this wrong?"** Claims that can answer — "score below X on held-out set Y by date Z" — are doing empirical work. Claims that cannot — "it's near," "it truly understands," "trust the trajectory" — are marketing or metaphysics wearing the costume of a prediction. The same test applies to safety claims: "the model is safe" is unfalsifiable until it is rewritten as "the model will not produce [specified harmful output] under [specified red-team protocol]," which can, and sometimes does, fail.

*Sources: Karl Popper, *The Logic of Scientific Discovery* (1959; orig. *Logik der Forschung*, 1934) and *Conjectures and Refutations* (1963) for the falsifiability criterion. On operationalized AGI-style benchmarks: François Chollet, "On the Measure of Intelligence" (arXiv:1911.01547, 2019) and the ARC-AGI benchmark. On competition-math evaluation of frontier models: the AIME/MATH benchmark literature and vendors' publicly reported 2024–2025 results (treat specific figures as reported, not independently audited). On benchmark contamination and on reasoning robustness under input perturbation: peer-reviewed and arXiv work published 2023–2025 (e.g., studies of train/test contamination and of accuracy drops when numeric/surface features of problems are altered). Exact scores and dates vary by model and report; the reasoning here does not depend on any single unverified figure.*
