# Method in Action: Samuelson & Zeckhauser 1988 + Johnson & Goldstein 2003

> *Example for the [status-quo-bias](../SKILL.md) skill.*

**William Samuelson** (Boston University) and **Richard Zeckhauser** (Harvard Kennedy School) were motivated by observations of apparent irrationality in economic behavior — people seemed to cling to existing arrangements far beyond what rational switching-cost calculations would justify. Their 1988 paper is the foundational empirical document for status quo bias.

The inheritance experiment used a simple structure: subjects were given a hypothetical inheritance and four investment options (moderate-risk company, high-risk company, treasury bills, municipal bonds). In the "neutral" condition, subjects chose freely. In the "status quo" conditions, the problem was identical except one option was labeled as the current holding.

The results were unambiguous across all conditions: whatever option was designated "status quo" attracted 2–4× higher selection rates. The bias persisted even when:

- Transaction costs were explicitly set to zero
- The status quo option was objectively dominated by other options on the subject's stated preferences
- The "status quo" was arbitrary (randomly assigned)

> "Individuals exhibit a significant status quo bias. When an option is labeled as the status quo, they are more likely to choose it. This is not a rational response to transaction costs: the bias holds even when transaction costs are explicitly set to zero."
>
> — Samuelson & Zeckhauser (1988), p. 8.

The authors identified three mechanisms: loss aversion (change involves both gains and losses; losses are weighted more heavily), regret avoidance (worse outcomes from active change feel worse than same outcomes from inaction), and psychological commitment (the existing option has been previously chosen; abandoning it implies the previous choice was wrong — a form of cognitive dissonance avoidance).

**Johnson & Goldstein 2003 — the organ donation natural experiment.** This is the most consequential real-world documentation of status quo bias at population scale. Johnson and Goldstein exploited the natural variation in organ donation policy design across European countries with broadly similar demographics and values.

| Country | Default | Consent rate |
|---|---|---|
| Germany | Opt-in | ~12% |
| Netherlands | Opt-in | ~28% |
| United Kingdom | Opt-in | ~17% |
| Denmark | Opt-in | ~4% |
| Austria | Opt-out | ~99% |
| Belgium | Opt-out | ~98% |
| France | Opt-out | ~99% |
| Sweden | Opt-out | ~86% |

The difference is not explained by differences in attitudes toward organ donation, religious composition, healthcare quality, or trust in institutions. Survey data on underlying willingness to donate show similar rates across opt-in and opt-out countries. The near-deterministic difference is driven entirely by which option requires active effort to change.

> "Defaults save lives. The difference between countries is not in their laws or their citizens' values — it is in which option requires action to change."
>
> — Johnson & Goldstein (2003), p. 1338.

**Madrian & Shea 2001 — 401(k) automatic enrollment.** A parallel natural experiment in retirement savings:

> Madrian, B. C., & Shea, D. F. (2001). "The Power of Suggestion: Inertia in 401(k) Participation." *Quarterly Journal of Economics*, 116(4), 1149–1187.

When a U.S. firm changed its 401(k) enrollment default from opt-in to automatic enrollment (with an opt-out), participation rates among new employees rose from approximately 37% to 86%. The automatic enrollment rate and contribution percentage became "sticky" defaults: even employees who would have chosen different rates under opt-in conditions rarely changed the automatically assigned defaults.

**Business applications across domains:**

**Product subscription defaults.** Annual renewal subscriptions default to "renew" (opt-out of cancellation). The status quo bias ensures that users who never actively evaluate renewal will continue — independent of value delivered. Operationally this is the basis of SaaS net revenue retention above 100%: the default is "stay," and only dissatisfied users actively leave.

**Software default settings.** Security configurations (e.g., two-factor authentication default off vs. on), privacy settings (data sharing default on vs. off), and notification preferences all exhibit near-deterministic effects from the default direction. Apple's App Tracking Transparency (2021) — changing the default from opt-in for users to opt-out for tracking — reduced tracking consent rates from ~70% to ~25%, a result driven almost entirely by default direction change.

**Board and governance.** Corporate governance structures persist long after their designers are gone because changing governance requires active effort and a coalition for change. The status quo in governance — number of board seats, veto rights, voting thresholds — is nearly always determined by the first document that was signed, not by ongoing deliberate optimization.

**Hiring decisions.** Retaining an underperforming employee is significantly easier than terminating them — not because the deliberate calculation favors retention, but because the status quo (this person is on the team) persists until someone actively changes it. Organizations routinely maintain talent configurations that no one would choose from scratch.

Three operational lessons:

**First, ask the fresh-choice question systematically.** For any persistent arrangement — vendor, process, team configuration, product feature, governance structure — the question is not "should we change it?" but "would we choose this if we were deciding from scratch today?" If the answer is no and the difference exceeds switching costs, status quo bias is operating.

**Second, design defaults with explicit intent.** When you control a default, you are making a decision that will affect the behavior of the majority of users who never actively choose. That is a design responsibility, not a technical detail. State the justification for the default explicitly.

**Third, use opt-out structures for high-social-value behaviors.** The organ donation and 401(k) evidence is unambiguous: when behavior serves both the individual's stated interests and a social good, opt-out enrollment dramatically increases participation without coercing anyone. The person who genuinely prefers not to participate can always opt out.
