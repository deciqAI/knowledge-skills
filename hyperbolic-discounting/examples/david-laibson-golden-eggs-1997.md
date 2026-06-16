# Method in Action: David Laibson's "Golden Eggs and Hyperbolic Discounting," 1997

> *Example for the [hyperbolic-discounting](../SKILL.md) skill.*

David Laibson's 1997 paper at Harvard was the formal economics breakthrough that turned a behavioral curiosity (the documented preference reversal in psychology) into a tractable mathematical framework with policy implications. The paper title "Golden Eggs" referred to retirement accounts as illiquid savings devices that bind the future-self.

The motivating puzzle Laibson identified:

> "Many U.S. households accumulate the majority of their lifetime wealth in retirement accounts — which charge severe penalties for early withdrawal — while simultaneously holding low or negative balances in liquid accounts and carrying high-interest credit card debt. Under standard exponential discounting, this is irrational: the household pays interest to a credit card company at 18% while a portion of its wealth sits earning 7% inside a 401(k), and the household refuses to liquidate the 401(k) to pay off the card. The behavior cannot be explained by standard models of intertemporal choice."
>
> — Laibson (1997), pp. 444-445.

Laibson's β-δ model resolved the puzzle. A present-biased household:

- Knows that the retirement account is binding (early withdrawal incurs penalty + tax).
- Knows that the credit card debt is liquid (could be paid off if liquid funds existed).
- Future-self's preferences: pay off the debt to save the 18% interest charge.
- Present-self's preferences: keep current consumption high; the future will save.

The retirement account's penalty is doing welfare-enhancing work: it is a *Ulysses contract* the household is using against its own future impatience. Removing the penalty (allowing free withdrawal) would let the present-self drain the account, defeating the savings purpose.

Laibson's paper formalized this in three sections:

**Section 2** introduced the β-δ utility function:
- u(c₀, c₁, c₂, ...) = u(c₀) + β·Σ_{t=1}^∞ δᵗ·u(cₜ)

This is exponentially-discounted future utility, with an *additional* one-shot β discount applied to *all* future periods. β ∈ (0, 1) creates the present bias.

**Section 3** derived consumer choice under this preference structure. The key result:

> "A naive hyperbolic consumer — who believes their future-self will be patient — will save less than the sophisticated hyperbolic consumer, who correctly anticipates their future impatience and uses commitment devices. Both will save less than the standard exponential consumer. The welfare loss to naive consumers, in calibrated simulations, is substantial: 6 to 12 percent of lifetime wealth in plausible parameter ranges."
>
> — Laibson (1997), p. 461.

**Section 4** extended the analysis to retirement accounts and other commitment devices. The empirical implications were testable and were confirmed in subsequent work (Madrian & Shea 2001; Choi, Laibson, Madrian, & Metrick 2002, 2003).

Two follow-up empirical papers established the field:

**Madrian, B. C., & Shea, D. F. (2001).** "The power of suggestion: Inertia in 401(k) participation and savings behavior." *Quarterly Journal of Economics*, 116(4), 1149-1187. This paper studied a single Fortune 500 company that switched its 401(k) default from "opt-in" (employees must elect to participate) to "opt-out" (employees are auto-enrolled at 3% unless they elect not to). Participation jumped from 49% to 86% — a 37-percentage-point shift. This is the canonical empirical demonstration of present-bias's policy implications: the default matters because future-self relies on present-self's inaction.

**Thaler, R. H., & Benartzi, S. (2004).** "Save More Tomorrow: Using behavioral economics to increase employee saving." *Journal of Political Economy*, 112(S1), S164-S187. The SMarT program asks employees to commit *now* to increasing their savings rate at *each future raise*. The future increase is far away (low present-bias penalty), but the commitment binds when the raise arrives. In field trials, average savings rates tripled from 3.5% to 13.6% over four pay raises. Real money, real workers, real behavior change.

**DellaVigna, S., & Malmendier, U. (2006).** "Paying not to go to the gym." *American Economic Review*, 96(3), 694-719. The classic real-world demonstration. The authors analyzed three U.S. health clubs and found that gym members who chose a monthly contract ($85/month) paid an average of $17 per workout — substantially more than the $10 pay-per-visit price they could have paid. The members had future-projected themselves into a regular gym-goer; the actual self showed up less often. ~80% of members would have been better off on the pay-per-visit plan.

**Frederick, S., Loewenstein, G., & O'Donoghue, T. (2002).** "Time discounting and time preference: A critical review." *Journal of Economic Literature*, 40(2), 351-401. The canonical review, reviewing 40+ years of empirical work on time preference. Documents the wide range of estimated discount rates (from negative to over 1000%), the contextual factors, and the operational implications. A key conclusion: discount rates are not a stable individual trait but vary with domain, magnitude, sign (gains vs losses), and framing.

**O'Donoghue, T., & Rabin, M. (1999).** "Doing it now or later." *American Economic Review*, 89(1), 103-124. Formalized the distinction between *naive* and *sophisticated* hyperbolic discounters. Naives believe their future-self will be patient (and so don't seek commitment); sophisticates know their future-self will be present-biased (and demand commitment devices). This sophistication distinction is operationally important: education about present bias converts naives into sophisticates, which dramatically improves their behavior even without other intervention.

The framework has shaped policy and practice:

**Retirement policy.** Auto-enrollment in 401(k) is now common in the U.S. and mandatory in some jurisdictions (UK auto-enrollment 2012). The 2006 Pension Protection Act in the U.S. explicitly removed legal barriers to auto-enrollment, citing Madrian-Shea evidence. Direct Laibson application.

**Public health.** "Default" donor status (Austria, Belgium, etc., where you are an organ donor unless you opt out) produces > 90% donor rates, vs. < 30% in opt-in countries (Johnson & Goldstein 2003). This is present-bias and inertia, not active preference difference.

**Behavioral finance products.** "Set it and forget it" investment products (target-date funds), automatic contribution escalators, lock-up periods on certain mutual funds — all engineered against present bias.

**Tech / SaaS pricing.** Free trials with automatic billing exploit present bias: the trial signup is for present-self who values "free," the future billing arrives when present-self is gone and the inertia keeps the subscription active. The 21st-century equivalent of gym membership.

**Subscriptions.** Subscription bundling, annual prepayment with steep monthly markup, "easy signup / hard cancellation" — all classic present-bias exploitation patterns. Regulatory pushback (FTC click-to-cancel rule, 2024) acknowledges the consumer-protection dimension.

Three operational lessons from Laibson and the literature:

**First, "willpower" is the wrong frame.** The naive theory of self-control says present-bias is a willpower failure that better discipline can overcome. The behavioral economics result is that **willpower is unreliable; commitment devices are reliable.** Don't blame people (or yourself) for present-bias failures; install structural fixes.

**Second, defaults are extraordinarily powerful.** A choice architecture in which the desired behavior is the default and the undesired behavior requires deliberate opt-out outperforms any amount of education, signage, exhortation, or training. The auto-enrollment 37-percentage-point shift is not an outlier; it's typical of default effects across domains.

**Third, sophistication matters.** Naïve present-biased people don't seek commitment devices because they (incorrectly) believe future-self will choose well. Sophisticated present-biased people seek commitment devices because they accurately predict future-self's impatience. **Education that converts naives to sophisticates is high-leverage** — even when the underlying bias is unchanged.
