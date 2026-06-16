# Method in Action: ACH at the CIA and the Cuban Missile Crisis Pattern (1962 → 1999)

> *Example for the [critical-thinking](../SKILL.md) skill.*

A worked example. Not folklore — primary-source documented in the CIA's own institutional history.

In **October 1962**, the U.S. Intelligence Community failed to anticipate the Soviet deployment of nuclear missiles to Cuba. **Sherman Kent**, then chair of the Office of National Estimates, had personally written the National Intelligence Estimate (NIE 85-3-62, September 19, 1962) that concluded the Soviets would *not* deploy nuclear missiles to Cuba because "to do so would be inconsistent with their established practice." Three weeks later, U-2 photographs proved the conclusion wrong. The intelligence failure was not absence of evidence — there had been multiple human-source reports of missile-like equipment being moved into Cuba — but a structural failure to take alternative hypotheses seriously enough to test them against the evidence.

This pattern — analysts anchoring on the most plausible hypothesis, then unconsciously discounting evidence against it — was identified by CIA analyst **Richards J. Heuer Jr.** as the dominant intelligence-analytic failure mode across multiple cases (Iran Revolution 1979, Iraq WMD assessments 2002, etc.). In *Psychology of Intelligence Analysis* (1999), Heuer documented:

> "**The problem is not insufficient evidence; the problem is the cognitive shortcut by which analysts evaluate evidence against a preferred hypothesis instead of an array of plausible hypotheses.** Analysis of Competing Hypotheses (ACH) was developed to counter this by structurally requiring analysts to evaluate each piece of evidence against every hypothesis they have entertained. … Done properly, ACH almost always produces a different ranking of hypotheses than the analyst's initial intuition."
> — Heuer, *Psychology of Intelligence Analysis* (CIA, 1999), ch. 8 introduction.

The CIA's Sherman Kent School subsequently institutionalized ACH as part of analyst training. Heuer and **Randolph Pherson** then formalized 50+ structured analytic techniques in *Structured Analytic Techniques for Intelligence Analysis* (CQ Press, 2014), now standard reference inside the U.S. Intelligence Community.

Walk a simplified ACH on a contemporary business case (illustrative — *should our SaaS startup hire a VP of Sales now?*):

- **Hypotheses (Step 1):**
  - H1: Yes, hire now — we have PMF and need to scale.
  - H2: No, founder-led sales for 6 more months — we don't have repeatable playbook yet.
  - H3: Hire a Head of Sales (more junior, less expensive) instead of a VP.

- **Evidence (Step 2):**
  - E1: Last 3 deals closed without founder involvement — we have a playbook.
  - E2: Sales cycle is still wildly variable (2 weeks to 4 months).
  - E3: We have $4M ARR.
  - E4: Founder is spending 70% of time on sales (not other priorities).
  - E5: VP-level candidates we've talked to want > $300K base + equity > 1%.

- **Matrix (Step 3):**

| Evidence | H1 (VP) | H2 (Wait) | H3 (Head) |
|---|---|---|---|
| E1 (playbook) | C | I | C |
| E2 (variable cycle) | I | C | C |
| E3 ($4M ARR) | C | I | C |
| E4 (founder time) | C | I | C |
| E5 (VP cost) | I | C | C |
| **Inconsistencies** | **2** | **3** | **0** |

- **Surviving hypothesis (Step 5):** H3 (hire a Head of Sales). Zero inconsistencies. **Not** the founder's initial preference (H1).
- **Linchpin assumption (Step 6):** If E2 (variable cycle) is actually because of *one bad customer profile* that can be excluded from the ICP — not a general playbook problem — then H1 becomes viable.
- **Alternatives rejected (Step 7):**
  - H1 rejected because E2 (variable cycle = no repeatable playbook yet) and E5 (VP cost is high relative to risk if playbook isn't proven).
  - H2 rejected because E1 (closing without founder shows playbook exists in some form) and E4 (founder bottleneck = clear sign waiting hurts).
- **Milestones (Step 8):** If next 4 weeks the variable-cycle issue concentrates in *one* segment, revisit H1.

The lesson the framework names: **the founder's initial intuition was H1**. **ACH surfaced H3 as the answer with zero inconsistencies** — not by being smarter, but by *requiring* every piece of evidence to be matched against every hypothesis. The same mechanism that failed for Kent in 1962 (settling on the most-plausible hypothesis, then evaluating evidence selectively) is what ACH structurally prevents.
