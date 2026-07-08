# Method in Action: Facebook's "7 Friends in 10 Days" Activation Metric (2007–2009)

> *Example for the [aarrr-pirate-metrics](../SKILL.md) skill.*

A worked example from a social network — a different domain and a different bottleneck stage than the Dropbox case. Documented in Chamath Palihapitiya's public 2013 talk on Facebook's growth team and in Sean Ellis & Morgan Brown's *Hacking Growth* (2017).

In 2007–2008, **Facebook's** growth flattened at roughly 90 million monthly users. Inside the company, some believed the product might simply be capped near 100 million — that social networks saturate. Instead of accepting the ceiling, Facebook formed a dedicated Growth team under Chamath Palihapitiya and ran what was, in effect, a funnel audit:

- **Acquisition**: Healthy. Millions of people were still landing on Facebook and signing up every month. Registrations were not the problem.
- **Activation**: Broken — and hidden by the sloppy definition. "Signed up" looked fine; but a large fraction of new registrants arrived to an empty feed, saw no friends, and never returned. Signup was the end of Acquisition, not Activation.
- **Retention**: Weak *downstream of* Activation. Users who never connected to their real-world friends had nothing to come back for; users who did connect retained strongly.
- **Referral**: Structurally strong — a social network's core loop is inviting and finding friends — but only activated users exercised it.
- **Revenue**: Advertising-driven; entirely a function of retained, engaged users. Not the constraint.

The Growth team's decisive move was **Step 1 of the audit: define Activation as a measurable, product-specific event.** By correlating early behavior with long-term retention, they found the aha moment: **a new user who reached 7 friends within 10 days of signup retained; a user who didn't, churned.** "7 friends in 10 days" became the team's north-star activation metric — not a vanity registration count, but the event at which a new user first experienced the product's actual value (a feed full of people they knew).

**The intervention:** With Activation named as the load-bearing bottleneck, the Growth team re-pointed the company's effort at one number. Onboarding was rebuilt around friend-finding — contact importers, the "People You May Know" recommendation engine, prompts that pushed every new user toward their first connections — and internationalization (a crowdsourced translation platform) removed the language barrier that kept non-English users from finding their friends at all. Every experiment was judged by whether it moved new users toward the 7-in-10 threshold, then re-measured — the audit run as a loop, not a one-shot.

**The result:** Growth resumed through the supposed ceiling. Facebook passed 500 million users in 2010 and 1 billion monthly users in October 2012 — the trajectory Palihapitiya's talk describes as the direct product of instrumenting the funnel and concentrating on the activation constraint rather than buying more traffic into a leaky bucket.

**The non-obvious lesson:** Facebook's bottleneck was invisible as long as Activation meant "registered." The single highest-leverage act was definitional — replacing a generic stage label with a measured aha-moment event. Only then did the funnel show where growth was actually dying, and only then could every team optimize the same constraint instead of the stage each happened to own.

The mapped steps:
1. Define stages product-specifically: Activation = 7 friends within 10 days, not signup
2. Measure conversions: registrations healthy; signup→activated conversion the weak link; retention strong conditional on activation
3. Benchmark: activated users retained at healthy social-network rates; non-activated users churned — the gap localized the bottleneck
4. Identify the load-bearing bottleneck: Activation, not Acquisition
5. Pre-commit experiments against the single metric: onboarding friend-finders, People You May Know, translations — each judged by movement toward 7-in-10
6. Re-measure and repeat: continuous experiment loop; growth resumed to 1 billion users by 2012

Primary source: Palihapitiya, Chamath. "How We Put Facebook on the Path to a Billion Users" (public talk, 2013). Case account: Ellis, Sean & Brown, Morgan. *Hacking Growth: How Today's Fastest-Growing Companies Drive Breakout Success*. Crown Business, 2017.
