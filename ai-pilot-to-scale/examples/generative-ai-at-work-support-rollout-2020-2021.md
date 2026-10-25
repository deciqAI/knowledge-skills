# Method in Action: Generative AI at Work — A Staggered Support-Desk Rollout (2020–2021)

> *Example for the [ai-pilot-to-scale](../SKILL.md) skill.*

The best-documented pilot-to-scale path for a generative AI tool in a real business is the one studied by Erik Brynjolfsson, Danielle Li and Lindsey Raymond in *Generative AI at Work* (NBER Working Paper 31161, 2023; published in the *Quarterly Journal of Economics*, 2025). The authors had access to the deployment data of a GPT-based assistant at a Fortune 500 enterprise software company's chat-based technical support operation. The firm is not named in the paper; everything below is taken from the paper itself.

**The setup.** Support agents — most in the Philippines, a smaller group in the US and elsewhere — answer technical questions from US small-business owners by chat. Sessions average about 40 minutes. The firm already measured agents on three standard metrics: average handle time, resolution rate, and net promoter score. An AI vendor built a tool on a GPT-family model, fine-tuned on the firm's labeled historical conversations, that shows each agent real-time suggested replies and links to internal documentation. The agent sees the suggestions; the customer never does; the agent is free to ignore them.

**The path.** The tool was rolled out agent by agent **after an initial seven-week randomized pilot featuring 50 agents**. The bulk of adoption happened between November 2020 and February 2021. Data covers 5,179 agents (5,172 in the published version).

**The result.** Access to the tool raised issues resolved per hour by **14% on average**, with a **34% improvement for novice and low-skilled workers** and minimal impact on experienced, highly skilled workers — the authors even report evidence that it may have lowered conversation quality for the most skilled agents. Customer sentiment toward agents improved and attrition fell. Average adherence to the suggestions was **38%**: agents frequently ignored them.

Now run the **Pilot Charter** against the record.

**1. Pick one narrow workflow.** One workflow (chat technical support), one job that is "fairly uniform" across locations, very high frequency. This is the shape the gate demands: narrow, repetitive, value measurable. **Pass.**

**2. Measure the baseline.** The baseline existed before the AI did — handle time, resolution rate and NPS were already the firm's operating metrics, recorded per agent. The pre-AI distribution of handle times (centered at ~40 minutes) is what the post-AI distribution is compared against. **Pass — and this is why the result is credible.** A pilot with no pre-existing metric would have had nothing to compare against.

**3. Write success criteria in advance.** The paper does not publish the firm's internal go/no-go criteria, so this step cannot be audited from the public record. What the record does show is that the outcome metrics were the firm's standing metrics, not ones chosen after the results came in — the closest public evidence of pre-commitment. **Not verifiable; flag rather than assume.**

**4. Name the owner.** The paper describes team managers who hold weekly one-on-ones and an operation paid on performance metrics — i.e. the result lands in an existing business line with an accountable management structure, not in an IT side-project. Ownership of the rollout decision itself is not documented. **Partly verifiable.**

**5. Integrate into existing systems.** Suggestions appear inside the chat window agents already work in, beside the live conversation (Figure 1 of the paper). No new tool, no copy-paste. **Pass.** This is the step most failed pilots skip.

**6. Grant autonomy in stages.** The tool sat at **L1 — suggest only**: output shown only to the agent, who has full discretion, and no suggestion at all when training data is insufficient. The authors note this design "reduces the likelihood that off-topic or incorrect outputs make their way into customer conversations." Nothing in the study moves to L2 or L3. **Pass at L1** — and the 38% adherence rate is exactly the signal that would have to rise before any higher stage is earned.

**7. Decide on the date.** The seven-week randomized pilot was followed by a staged rollout — the scale decision was made after a bounded test, and widened gradually rather than switched on for everyone. **Scale, staged.**

**8. Stop-rule / uneven effects.** The heterogeneity finding is what the "look for uneven effects" principle is for. A company-wide average of +14% conceals that the gain is concentrated in newer agents and may be slightly negative for top performers. A charter that scaled on the average alone would miss that the next adjacent workflow should be chosen by *who* does the work, not just *what* the work is.

### The mapped steps

1. **Workflow:** chat technical support — one uniform, high-frequency job
2. **Baseline:** firm's standing metrics (handle time, resolution rate, NPS), pre-AI handle time ~40 min
3. **Success/kill criteria:** internal criteria not published — cannot be audited
4. **Owner:** existing managed support line; rollout owner not documented
5. **Integration:** suggestions inside the existing chat window
6. **Autonomy stage:** L1 suggest-only; 38% average adherence
7. **Verdict:** seven-week, 50-agent randomized pilot → staged rollout (bulk Nov 2020–Feb 2021)
8. **Uneven effects:** +14% average, +34% for novices, minimal (possibly negative on quality) for top performers

**The lesson.** The rollout that produced one of the cleanest positive results in the literature had the unglamorous parts in place: a workflow narrow enough to measure, metrics that predated the tool, integration into the existing screen, a suggest-only autonomy level, and a bounded pilot before scaling. The parts the paper cannot show — pre-signed criteria and a named decision owner — are the parts a charter must write down, because they leave no trace in the outcome data.

*Primary source: Brynjolfsson, E., Li, D., & Raymond, L. R. "Generative AI at Work." NBER Working Paper 31161 (April 2023, revised November 2023), https://www.nber.org/papers/w31161 ; published version: *The Quarterly Journal of Economics* 140(2), 2025, https://academic.oup.com/qje/article/140/2/889/7990658 . Figures quoted are from the NBER version (Sections 1, 2.2, 2.3, 3.1 and the adherence analysis).*
