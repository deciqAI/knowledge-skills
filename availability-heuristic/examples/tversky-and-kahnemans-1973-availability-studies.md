# Method in Action: Tversky and Kahneman's 1973 Availability Studies

> *Example for the [availability-heuristic](../SKILL.md) skill.*

The 1973 paper "Availability: A heuristic for judging frequency and probability" was the second in Tversky and Kahneman's seminal 1972-1974 trilogy on judgmental heuristics (the others being representativeness in 1972 and anchoring in 1974). Together with their 1974 *Science* paper "Judgment under Uncertainty," the work established the empirical foundation of behavioral economics — and earned the 2002 Nobel Memorial Prize in Economics.

The 1973 paper proposed a simple but radical claim: people don't compute probability directly. They compute the easier question "how easily can I recall examples?" — and then *substitute* this answer for the probability. The substitution happens automatically, beneath awareness, and produces predictable distortions wherever the ease of recall doesn't track the actual frequency.

The paper ran a sequence of studies. Study 1 was the letter-K demonstration above. Study 4 asked subjects:

> "In four pages of a novel (about 2,000 words), how many words would you expect to find that begin with the letter K?" (Group 1.) "...that have K as their third letter?" (Group 2.)

Group 1 estimated about 12 words; Group 2 estimated about 5. The actual answer for typical English text: roughly twice as many words have K third as begin with K. The retrieval-ease bias produced confident, wrong, and *inverted* frequency estimates.

The most influential extension was the Lichtenstein et al. 1978 study, which scaled the methodology to real-world mortality risks. From their paper:

> "Judged frequencies of causes of death were correlated with their reported frequencies in mass media. Across 41 causes of death, the rank-order correlation between subject estimate and actual frequency was r = .57. The correlation between subject estimate and column-inch coverage in two metropolitan newspapers was r = .89. Subjects' estimates tracked media coverage substantially more closely than they tracked actual mortality. Causes with high media coverage but low actual frequency (homicide, motor vehicle accidents, tornadoes) were systematically overestimated. Causes with low media coverage but high actual frequency (asthma, diabetes, emphysema) were systematically underestimated. The overestimation factor for homicide vs diabetes was approximately 9x in subjects' estimates, when actual mortality runs about 1:4 in the opposite direction."
>
> — Lichtenstein et al. (1978), pp. 565-567.

This was the first systematic real-world demonstration that risk perception is calibrated to media salience rather than to actual harm. The result has been replicated dozens of times over the subsequent decades — across countries, demographic groups, and (with re-collected mortality data) across time periods. The pattern is structural: as long as media coverage diverges from frequency-weighted impact, public risk perception diverges from rational priority.

The empirical follow-up is enormous:

**Slovic, P., Fischhoff, B., & Lichtenstein, S. (1980).** "Facts and fears: Understanding perceived risk." In *Societal Risk Assessment*. Plenum Press. Established that risk perception varies on two principal dimensions: dread (uncontrollable, catastrophic, fatal, inequitable) and unknown (unobservable, unknown to those exposed, delayed effects). The availability heuristic compounds with dread to produce the disproportionate weight given to nuclear power, terrorism, and rare environmental contamination — vs. the muted weight given to automobile travel, alcohol use, and home accidents.

**Schwarz, N., Bless, H., Strack, F., Klumpp, G., Rittenauer-Schatka, H., & Simons, A. (1991).** "Ease of retrieval as information: Another look at the availability heuristic." *Journal of Personality and Social Psychology*, 61(2), 195-202. The key methodological refinement. Showed that it is *ease of retrieval*, not *content* of retrieved examples, that drives the effect. Subjects asked to recall 6 examples of their own assertiveness rated themselves *more* assertive than subjects asked to recall 12 examples — because the 12-example task was harder, and the difficulty was interpreted as "I'm not that assertive after all." The metacognitive feeling of difficulty was being used as the input, not the count of retrieved examples.

**Combs, B., & Slovic, P. (1979).** "Newspaper coverage of causes of death." *Journalism Quarterly*, 56(4), 837-849. Demonstrated the supply side: U.S. newspapers cover mortality events in proportion to vividness and recency, not to frequency. Rare-dramatic deaths get column-inches; routine-statistical deaths get summary tables. The media environment systematically miscalibrates the available evidence the public uses to estimate risk.

**Sunstein, C. R. (2002).** "Probability neglect: Emotion, worst cases, and law." *Yale Law Journal*, 112(1), 61-107. Extended the availability framework to legal and regulatory decision-making. The "salience effect" in regulation systematically misallocates resources to vivid risks. Sunstein's later work with Thaler on *Nudge* operationalizes this insight in choice architecture.

**Pachur, T., Hertwig, R., & Steinmann, F. (2012).** "How do people judge risks: Availability heuristic, affect heuristic, or both?" *Journal of Experimental Psychology: Applied*, 18(3), 314-330. The most rigorous recent test. Found that availability accounts for a large share of risk-judgment variance, but interacts with affect (emotional response). The two heuristics compound rather than competing.

**Tversky, A., & Kahneman, D. (1973).** Notably, the original paper itself anticipated the bias's social implications:

> "An important practical implication of the heuristic is that the availability of an event in memory may be quite different from its actual frequency. The differential coverage of various events in the mass media, for example, may produce a corresponding bias in the public's perception of the relative frequency of these events. This bias may have important consequences for political opinion, social policy, and personal decisions."
>
> — Tversky & Kahneman (1973), p. 229.

This prediction has been borne out at industrial scale. Modern political behavior, public-health policy, infrastructure spending, and personal financial decisions all show systematic availability-driven distortion. The terror response of 2001-2010 in the U.S. (with hundreds of billions of dollars allocated to terrorism prevention while heart disease — killing ~600,000 Americans annually — received a fraction of comparable attention) is the most-cited public-policy case study.

The framework has reshaped multiple operational disciplines:

**Public health.** WHO and CDC risk-communication frameworks explicitly correct for availability bias: present absolute frequencies (deaths per 100,000) rather than relative changes ("doubles your risk"); present cause-of-death-weighted threats rather than recent-vivid threats; deliberately re-emphasize undramatic high-frequency causes.

**Investment management.** The "recency bias" in fund flows (money flows to funds with recent good performance, out of those with recent bad) is a textbook availability case. Sophisticated investors and pension fund administrators explicitly use long-horizon performance metrics and reference-class-based forecasting to correct.

**Project planning.** The "planning fallacy" (Kahneman-Tversky 1979) is partly an availability bias: project planners imagine the specific tasks of their current project (vivid, available) and underweight the reference-class history of comparable projects (statistical, not retrievable). Flyvbjerg's "reference-class forecasting" methodology (2006, *Cambridge Encyclopedia of Project Management*) is the structural countermeasure adopted by major infrastructure projects.

**Medical diagnosis.** "What you've seen recently is what you diagnose now" is the medical-school cliché capturing the availability bias in clinical reasoning. Modern medical decision support systems (UpToDate, Epocrates, IBM Watson) explicitly counter this by presenting differential diagnoses weighted by population base rates rather than physician recall.

**Intelligence analysis.** CIA's *Psychology of Intelligence Analysis* (Heuer 1999) lists availability as one of the seven major biases analysts must structurally counter. The recommended technique: explicit base-rate identification ("how often does this kind of event occur in this kind of country in this kind of year?") before considering current-situation specifics.

**Legal and regulatory.** Cass Sunstein's body of work documents how regulatory cost-benefit analysis is systematically distorted by availability. Reforms include mandatory base-rate inclusion in regulatory impact analyses (OECD guidance), risk-comparison disclosures in product labels (FDA), and structured "expected utility" frameworks in environmental regulation.

Three operational lessons from Tversky-Kahneman 1973:

**First, ease of recall is not frequency.** People who use intuition for probability estimates are estimating retrievability, not probability. The substitution is automatic and invisible. The corrective is structural — force the question to be answered from base-rate data, not from memory.

**Second, media-amplified events distort risk perception systematically and predictably.** The differential coverage of dramatic vs. statistical events is structural in modern media. Risk communicators who present only the dramatic side (or only the statistical side) amplify or counter the bias.

**Third, calibration improves with feedback, not exhortation.** Telling people about the availability heuristic does not eliminate it. Forcing them to log probability estimates and check them against outcomes (Tetlock-style calibration training) does. **The Good Judgment Project's superforecasters consistently outperformed intelligence analysts by 30+ percent on prediction accuracy after calibration training — without other interventions.**
