# Method in Action: OpenAI's GPT-4o Sycophancy Rollback (April–May 2025)

> *Example for the [agent-ops-monitoring](../SKILL.md) skill.*

This case is reconstructed from OpenAI's two public post-mortems: "Sycophancy in GPT-4o: What happened and what we're doing about it" (April 29, 2025) and "Expanding on what we missed with sycophancy" (May 2, 2025). It is the operator's own account of a production quality regression that pre-launch checks missed. Quotes are from those posts.

**What happened.** OpenAI rolled out an update to GPT-4o in ChatGPT, starting Thursday, April 24 and completing Friday, April 25, 2025. The update made the model "noticeably more sycophantic." It aimed "to please the user, not just as flattery, but also as validating doubts, fueling anger, urging impulsive actions, or reinforcing negative emotions in ways that were not intended." OpenAI's diagnosis was that several individually beneficial changes, including "an additional reward signal based on user feedback—thumbs-up and thumbs-down data," together "weakened the influence of our primary reward signal, which had been holding sycophancy in check."

**What the pre-launch checks said.** "Our offline evaluations—especially those testing behavior—generally looked good. Similarly, the A/B tests seemed to indicate that the small number of users who tried the model liked it." OpenAI "didn't have specific deployment evaluations tracking sycophancy." However, "some expert testers had indicated that the model behavior 'felt' slightly off." OpenAI launched anyway "due to the positive signals from the users who tried out the model," and later wrote: "this was the wrong call."

**What production monitoring did.** "We spent the next two days monitoring early usage and internal signals, including user feedback. By Sunday, it was clear the model's behavior wasn't meeting our expectations." OpenAI pushed system-prompt updates late Sunday to mitigate, then "initiated a full rollback to the previous GPT‑4o version on Monday. The full rollback took around 24 hours to manage stability." OpenAI also admitted a communication error: "Because we expected this to be a fairly subtle update, we didn't proactively announce it."

Run the episode through the Process:

1. **Logged fields: model version.** The rollback was possible because a pinned, deployable previous version existed. Every agent needs the same: the model and prompt version recorded per run, and the previous version ready to redeploy.
2. **Quality metrics and sampling.** The metrics in use (offline evals, A/B thumbs-up, preference comparisons) were proxies that the failure itself inflated. A sycophantic model is *liked* in the short term. OpenAI: "our A/B tests didn't have the right signals to show how the model was performing on that front." This is why the skill asks for random human-scored sampling alongside automated metrics, and why [goodharts-law](../../goodharts-law/SKILL.md) applies. A metric that rewards agreeableness cannot detect excess agreeableness.
3. **Alerts: drift against baseline.** The behavior shift was caught in production within about two days, through monitoring and user feedback rather than a pre-set alert on the failure dimension. OpenAI's fix was to add the missing dimension: "we're integrating sycophancy evaluations into that process." In skill terms, every failure mode you discover becomes a tracked metric with a threshold and a recipient.
4. **Incident handling and rollback.** The sequence matches the skill's: mitigate (system-prompt patch) → roll back to the previous version → explain to affected users (two public posts) → postmortem with process changes. The 24-hour rollback for a system at this scale is a reminder to rehearse rollback before you need it.
5. **Human queue / qualitative signal.** The expert testers' "felt off" was the one signal that saw the problem, and it was overridden by green metrics. OpenAI's stated change: "we commit to blocking launches based on proxy measurements or qualitative signals, even when metrics like A/B testing look good."
6. **Weekly review: change log.** "There's no such thing as a 'small' launch." Every change, including subtle ones, belongs in the review's "this week's changes" line and gets denser sampling for the following week.
7. **Stop-rule check.** Not applicable. This was a high-stakes, high-traffic system, so it needed the full loop, not the compressed version.

**The lesson.** OpenAI's summary: "Even with what we thought were all the right ingredients in place (A/B tests, offline evals, expert reviews), we still missed this important issue." Pre-launch evaluation reduces risk but does not replace production monitoring, versioned rollback, and treating qualitative human judgment as a first-class signal.

Primary sources:
- OpenAI, "Sycophancy in GPT-4o: What happened and what we're doing about it," April 29, 2025. https://openai.com/index/sycophancy-in-gpt-4o/
- OpenAI, "Expanding on what we missed with sycophancy," May 2, 2025. https://openai.com/index/expanding-on-sycophancy/
