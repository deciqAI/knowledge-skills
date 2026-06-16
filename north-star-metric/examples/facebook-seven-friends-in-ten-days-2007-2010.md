# Method in Action: Facebook's "Seven Friends in Ten Days" (2007–2010)

> *Example for the [north-star-metric](../SKILL.md) skill.*

A worked example. Not Silicon Valley legend — discussed publicly by Chamath Palihapitiya, head of Facebook's growth team 2007–2011, in lectures and interviews.

When Facebook's growth team formed in **2007**, the site had ~50 million users and was facing competition from MySpace, Friendster, and emerging social products. The company had many metrics — signups, MAU, time spent, photos uploaded, messages sent, friends added. Each team optimized different ones.

The growth team, looking at retention data, identified a **load-bearing leading indicator**: users who connected with **7 friends in their first 10 days** retained at multiples of the rate of users who did not. The "7 friends in 10 days" metric was not the most-counted, the easiest to grow, or the most "viral-feeling." It was the metric that *predicted long-term retention* most strongly — which itself predicted long-term revenue.

Palihapitiya, speaking publicly years later:

> "We figured out a way to identify, with very high accuracy and statistical relevance, who was actually likely to be retained… It was 'within the first ten days, did this person register a sufficient number of friends?' And the threshold was seven. So our number, the only number that mattered, was making sure that as many users as possible got to seven friends within ten days."
> — Chamath Palihapitiya, "How We Put Facebook On The Path To 1 Billion Users," lecture at Stanford GSB, ca. 2013. Public excerpts archived at: https://www.businessinsider.com/the-secret-to-facebooks-explosive-growth-2014-12

Walk the NSM Audit on Facebook 2007:

- **Customer value (Step 1):** Users connected to their existing social network and using it as their primary social communication tool.
- **Candidate metrics (Step 2):** Signups, DAU/MAU ratio, time spent, photos posted, messages sent, friends-added per user, friends-added-in-first-N-days.
- **3-criteria check (Step 3):**
  - Signups: customer value? weak (signup ≠ value). **Reject as NSM.**
  - Time spent: customer value? mixed (could be addiction-y, not genuine value). **Supporting, not NSM.**
  - Friends added in first 10 days ≥ 7: customer value ✓ (network-effect value); strategy fit ✓ (Facebook bet on social graph density); leads revenue ✓ (retention → DAU → ad inventory). **NSM ✓.**
- **Time-shifted correlation (Step 4):** Users hitting "7 in 10" predicted day-30, day-60, day-180 retention at materially higher rates than those who did not — a clean leading-indicator profile.
- **Perverse-incentive stress test (Step 5):** Could the team game "friends added" by spammy auto-suggest? Yes — and they did push social discovery aggressively, but balanced against quality signals (was the friend reciprocated, did messages flow). The NSM's main risk was that *quantity of friend connections* could be cheap-grown; Facebook addressed this with quality guardrails on what counted.
- **Pick (Step 6):** "7 friends in 10 days" became the growth team's official cross-team NSM for the 2007–2010 period. Every product change, signup flow optimization, friend-recommendation algorithm, and onboarding tweak was evaluated against this single number.
- **Re-evaluation (Step 7):** As Facebook scaled past ~500M users and saturated the addressable graph, the NSM evolved — toward DAU/MAU ratio, then engagement quality, then mobile-DAU specifically, then ad-impressions-per-DAU. The NSM is not eternal.

Facebook grew from ~50M users in 2007 to 1 billion in 2012. The growth team consistently credited the "7 in 10" NSM as the single most important focusing tool — *not because it was the most important business number* (revenue was), *but because it was the leading indicator that predicted revenue early enough to course-correct*.

**Sources:** Ellis, Sean. "The North Star Metric for Sustainable Growth." *GrowthHackers*, 2017. https://growthhackers.com/articles/north-star-metric **Primary source for the term**. Amplitude. *The North Star Playbook* (2nd ed., Amplitude Inc., 2022). https://amplitude.com/north-star **Operational framework**. Croll, Alistair & Yoskovitz, Benjamin. *Lean Analytics: Use Data to Build a Better Startup Faster*. O'Reilly, 2013. **The "OMTM" framing**. Palihapitiya, Chamath. "How We Put Facebook On The Path To 1 Billion Users." Stanford GSB lecture, ca. 2013. Public excerpts: https://www.businessinsider.com/the-secret-to-facebooks-explosive-growth-2014-12 **Primary source for the Facebook NSM case**. Andrew Chen's writings on growth metrics: https://andrewchen.com/
