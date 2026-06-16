# Method in Action: Goodhart 1975 (M3) and Strathern 1997 (RAE)

> *Example for the [goodharts-law](../SKILL.md) skill.*

The empirical foundation has two key moments. The first is **Charles Goodhart's 1975 critique of UK monetary policy**, originally a conference paper for the Reserve Bank of Australia, later expanded in his 1984 book *Monetary Theory and Practice*.

The context: in the mid-1970s, the Bank of England (and many other central banks) had identified a robust historical correlation between growth in broad money supply (the M3 aggregate) and subsequent inflation. The natural policy implication was straightforward: target M3 growth at a level consistent with low inflation, and inflation would be controlled.

Goodhart was skeptical. His objection was structural, not empirical:

> "It is not the case that there is some fixed and stable relationship between an observed monetary aggregate, such as M3, and other variables in the economic system. Rather, the relationships we observe statistically are the equilibrium outcomes of behavior by banks, depositors, and borrowers, each of whom is responding to a complex set of incentives. When the regulator targets M3 — and especially when the targeting carries policy weight that will affect interest rates and reserve requirements — these economic actors will reorganize their behavior to operate around the regulation. Liquid funds will be reclassified into categories that fall outside the M3 definition. The pre-targeting M3-inflation correlation will not survive the targeting. Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."
>
> — Goodhart (1975), as reprinted in Goodhart (1984), pp. 96-98.

Goodhart's prediction was empirical and falsifiable. It came true within a few years: as the Bank of England's M3 targets bit, UK banks began creating money-substitutes that escaped the M3 definition (most notably, the rise of the eurodollar market and certain types of negotiable certificates of deposit). The M3-inflation correlation collapsed; the Bank quietly abandoned M3 targeting by the mid-1980s.

The principle's second formative moment came two decades later, in **Marilyn Strathern's 1997 ethnographic study of British universities** during the rise of the Research Assessment Exercise (RAE). Strathern, an anthropologist at Cambridge, observed the RAE's effect on academic behavior:

> "The Research Assessment Exercise sets out to evaluate the quality of research conducted in British universities. The exercise was introduced with the goal of identifying excellent research and directing funding toward it. The instrument: publication count, citation analysis, peer-rated quality. The exercise's effect on the academy has been precisely the inversion of its stated goal. Academics have shifted from publishing fewer, more substantial works to publishing more, smaller, shallower ones. They have shifted topic selection toward areas where rapid publication is easier. They have formed citation circles. The exercise has produced not better research, but research-shaped activity that scores well on the exercise. The principle is general: when a measure becomes a target, it ceases to be a good measure."
>
> — Strathern, M. (1997). "'Improving ratings': Audit in the British university system." *European Review*, 5(3), pp. 308-309.

The aphoristic compression of "when a measure becomes a target, it ceases to be a good measure" became the popular form of the law. It is sometimes attributed to Goodhart directly; the precise wording is Strathern's, but she was articulating Goodhart's principle in academic-administration context.

The principle has been documented across an enormous number of empirical cases. A non-exhaustive selection:

**Atlanta Public Schools cheating scandal (2009-2015).** Standardized test scores were used to evaluate schools under No Child Left Behind. Teachers and administrators systematically altered student answer sheets. The scandal involved 178 educators across 44 schools; 11 educators were criminally convicted. The pattern was not unique to Atlanta; subsequent investigations found similar gaming in Houston, Washington D.C., and elsewhere. Same mechanism as Goodhart's M3: pressure on the metric, behavioral response that decoupled metric from goal.

**UK NHS Accident & Emergency 4-hour target (2002-2010s).** Hospitals were required to admit, transfer, or discharge 95% of A&E patients within 4 hours. Observed gaming: parking ambulances outside the A&E entrance (so the clock didn't start), reclassifying patients to delay the count start, discharging patients prematurely just before the 4-hour mark. Studies by the NHS itself documented these behaviors at scale. The metric "improved" while underlying care quality stagnated or in some cases declined.

**Wells Fargo cross-selling scandal (2002-2016).** Employees were given quotas for cross-selling products (checking + savings + credit card + brokerage). Sales numbers improved dramatically. Investigation revealed millions of fraudulent accounts opened without customer consent. Wells Fargo paid $3+ billion in fines. The metric (cross-sells per customer) had been targeted; employees had gamed it; the underlying goal (customer wallet share earned through service quality) had degraded.

**Soviet manufacturing under Gosplan (1930s-1980s).** Factory output measured in tons of nails → factories produced enormous single nails. Output measured in number of nails → factories produced tiny useless nails. Output measured in chandeliers → enormous unliftable chandeliers (the famous case of the Moscow lighting factory). The Soviet planning system was one long case study in adversarial Goodhart's law.

**Academic h-index gaming (2010s-2020s).** Self-citation, citation rings, and predatory open-access journals exploded as the h-index became a primary academic evaluation metric. The 2020+ "paper mill" industry — services that sell fraudulent paper authorship to academics — is a direct Goodhart's-law product.

**Algorithmic recommendation systems.** YouTube, TikTok, Instagram, Facebook all use engagement metrics (watch time, like rate, share rate, comment rate) to drive recommendations. Optimizing for engagement produces: clickbait, outrage content, misinformation amplification, and (well-documented) youth mental-health harm. The 2021 Facebook Files (whistleblower Frances Haugen) showed Facebook's internal research had documented these effects but the metric-target system continued to drive them.

The theoretical literature has been refined:

**Manheim & Garrabrant (2018).** "Categorizing variants of Goodhart's Law." *arXiv:1803.04585*. The taxonomy (Regressional / Extremal / Causal / Adversarial) referenced above. Originated in the AI alignment community as a framework for understanding why machine-learning systems optimized on a metric reliably produce dysfunction.

**Hennessy & Goodhart (2023).** "Goodhart's Law and machine learning: A structural perspective." *Working paper*. The contemporary AI extension.

**Campbell, D. T. (1979).** "Assessing the impact of planned social change." *Evaluation and Program Planning*, 2(1), 67-90. An independent formulation predating Goodhart's wider recognition, now called "Campbell's law": "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor." Same content, different domain emphasis.

**Lucas, R. E. (1976).** "Econometric policy evaluation: A critique." *Carnegie-Rochester Conference Series on Public Policy*, 1(1), 19-46. The "Lucas critique" in macroeconomics — the recognition that econometric relationships estimated under one policy regime are not stable when the regime changes, because actors will respond to the new regime. Adjacent to Goodhart's law in mechanism.

The framework has reshaped operational design in multiple disciplines:

**Modern bank regulation (Basel III, 2017+).** Capital and liquidity ratios are now paired with stress tests, leverage caps, and additional Tier 1 capital buffers — explicitly to constrain optimization of any single metric. The architecture is multi-metric, audit-augmented, and rotation-enabled (regulators update standards every few years specifically to keep ahead of gaming).

**Modern KPI design.** Best-practice OKR frameworks (Doerr 2018) recommend mixing leading and lagging indicators, qualitative and quantitative metrics, and pairing each KR with an explicit audit / quality check. Single-metric reward systems are increasingly regarded as a known-bad design pattern.

**Educational assessment.** Post-NCLB reforms have shifted toward sampling-based assessment, multi-measure school evaluation, and reduction of single-test stakes. Some states have explicitly abandoned standardized testing as an evaluation metric because the gaming costs exceeded the information benefits.

**Algorithmic system design.** ML systems are increasingly designed with multi-objective optimization, adversarial robustness checks, and explicit decoupling of metric (for training) from outcome (for evaluation). The AI alignment field is essentially a deep study of Goodhart-style failure in increasingly powerful optimization systems.

**Healthcare quality metrics.** UK NHS, U.S. CMS, and others have moved away from single-target measurement (e.g., A&E 4-hour) toward composite quality scores that include patient experience, clinical outcomes, and process metrics that can't be simultaneously gamed.

Three operational lessons from Goodhart and Strathern:

**First, all metrics are proxies. The proxy is always narrower than the goal.** The question is not "is this a good metric?" but "what is the gap between the metric and the goal, and how will agents exploit that gap?" Pre-committing to the gap analysis before deployment is the single highest-leverage step.

**Second, gaming is rational behavior under measurement pressure, not character failure.** Blaming the people who game metrics is a category error — they are responding to incentives, often appropriately. The fix is the measurement system, not the people.

**Third, rotation and audit are the only durable defenses.** No metric, however carefully designed, survives indefinite optimization pressure without gaming. The structural defense is to plan rotation (replace or refresh metrics before they're fully corrupted) and external audit (sample the underlying goal directly, periodically, to catch drift). Metrics are not assets; they are decaying assets.
