# Method in Action: Peter Wason's 2-4-6 Task, 1960

> *Example for the [confirmation-bias](../SKILL.md) skill.*

The empirical foundation for confirmation bias as a formal cognitive phenomenon is **Peter Cathcart Wason**'s 1960 study at University College London. The paper:

> Wason, P. C. (1960). "On the failure to eliminate hypotheses in a conceptual task." *Quarterly Journal of Experimental Psychology*, 12(3), 129-140.

Wason's setup was simple. He gave subjects a sequence — 2, 4, 6 — and told them it followed a rule he had in mind. Their task: discover the rule by proposing further sequences, which he would label as following or not following the rule. When confident, they should announce the rule.

The actual rule was: **any three numbers in ascending order**.

But subjects didn't discover this. The pattern Wason observed:

> "Subjects, on noticing that 2-4-6 was an even-number sequence ascending by 2, proposed sequences such as 8-10-12, 22-24-26, 100-102-104 — and were repeatedly told 'yes, that follows the rule.' They proceeded confidently to announce that the rule was 'ascending even numbers separated by 2.' They were wrong. The rule was 'three numbers in ascending order.'"
>
> "Notably, even when told they were wrong, many subjects refused to consider that the rule might be much broader than they thought. They proposed further sequences of the same type — 14-16-18, 30-32-34 — confirming their existing belief rather than testing it. Only a minority of subjects proposed sequences like 1-2-3 (which would have refuted the 'ascending by 2' hypothesis) or 5-7-9 (which would have refuted 'even numbers'). Most subjects converged on a confident but wrong rule."
>
> — Wason, P. C. (1960). "On the failure to eliminate hypotheses in a conceptual task." *Quarterly Journal of Experimental Psychology*, 12(3), pp. 130-132.

Wason's diagnosis was sharp:

> "It is now widely realized that to test a hypothesis one must seek evidence that would falsify it, not evidence that would merely confirm it. ... My subjects were attempting to verify their hypotheses rather than to refute them. They sought confirming instances rather than disconfirming instances. This is a logical error, but it appears to be a pervasive cognitive habit, even among educated subjects."
>
> — Wason (1960), p. 139.

The "2-4-6 task" became one of the most-replicated studies in cognitive psychology. Tweaks of the original experiment over the following 60 years showed:

- **The bias is robust under explicit instructions.** Telling subjects "try to disconfirm the rule" only slightly improves performance (Mynatt, Doherty & Tweney 1977, *British Journal of Psychology*).
- **The bias holds among scientists.** PhD-level subjects, including scientists by training, show the same pattern.
- **The bias scales to real-world hypothesis testing.** Klayman & Ha (1987, *Psychological Review*) generalized the finding to "positive test strategy" — the tendency to test hypotheses by examining cases where the hypothesis would be true, rather than cases where it would be false.

The deeper philosophical context is **Karl Popper's falsifiability principle** (1934, *Logik der Forschung*; English: *The Logic of Scientific Discovery*, 1959). Popper argued that a scientific hypothesis must be falsifiable — must specify what observations would refute it — and that the proper method is to seek those observations. Wason's empirical work demonstrated that humans systematically fail at this; we seek to confirm, not to falsify. The combination of Popper's normative argument and Wason's empirical finding produced the modern framework: **good thinking requires structural intervention against the default tendency to confirm.**

The bias was extended in influential subsequent work:

**Lord, Ross & Lepper (1979).** *JPSP* 37(11), 2098-2109. Pro- and anti-death-penalty subjects were shown the same mixed evidence; both reported the evidence as supporting their existing position. The bias is not just in evidence-seeking; it operates on interpretation of evidence already received.

**Nickerson, R. S. (1998).** "Confirmation bias: A ubiquitous phenomenon in many guises." *Review of General Psychology*, 2(2), 175-220. The canonical review article, documenting the bias across politics, science, medicine, finance, law, and personal relationships.

**Kahneman, D. (2011).** *Thinking, Fast and Slow.* Farrar, Straus and Giroux. ISBN 978-0374275631. Chapter 7 ("A Machine for Jumping to Conclusions") integrates confirmation bias with System 1 / System 2 framework. The bias is a property of fast, automatic System 1 reasoning; slow, deliberate System 2 reasoning can sometimes correct it, but the correction is effortful and inconsistent.

**Mercier & Sperber (2011).** *Behavioral and Brain Sciences*, 34(2), 57-74. The "argumentative theory of reasoning" — the controversial proposal that human reasoning *evolved* for confirmation-biased argument production, not truth-seeking. The implication: individual confirmation bias is feature, not bug, but functions correctly only in adversarial group settings where rival positions cross-check each other.

This last finding has the most operationally important implication: **individual debiasing efforts are weakly effective; structural intervention through adversarial process is strongly effective.** Hence the operational countermeasures: Devil's advocate, red team, peer review, judicial process, scientific peer review, premortem — all institutions that pit confirmation-biased reasoners against each other so that the biases cancel.

The framework has shaped multiple operational disciplines:

**Science and the peer review process.** Modern scientific methodology institutionalizes falsifiability: pre-registration of hypotheses, control groups, replication requirements. The reproducibility crisis in social psychology (roughly 2011 onward) was partly a confirmation-bias problem: researchers had been testing predicted effects without designed disconfirmation.

**Intelligence analysis.** The CIA's *Psychology of Intelligence Analysis* (Heuer 1999) explicitly trains analysts in "Analysis of Competing Hypotheses" (ACH) — a structured method to surface and weigh disconfirming evidence equally with confirming evidence. The method exists because the alternative — relying on analyst self-discipline — repeatedly produced catastrophic intelligence failures.

**Software engineering.** Test-driven development, code review, automated testing — all institutionalize disconfirmation. The hypothesis "my code works" is tested by writing tests that would fail if it didn't. Self-confirmation ("I read the code; it looks fine") is empirically far worse.

**Medicine.** Randomized controlled trials, blinded evaluation, intention-to-treat analysis — all designed to prevent confirmation bias by researchers convinced of a treatment's efficacy.

**Investment management.** Investment processes that require "kill the deal" sessions (someone tasked with arguing against), pre-commit decision criteria, and forced consideration of bear cases all institutionalize counter-confirmation.

Three operational lessons:

**First, the bias is invisible to introspection.** You will not notice you are confirmation-biased in the moment. The empirical evidence is overwhelming: even people trained in the bias, asked to look for it, fail to detect it in their own reasoning. The corrective must be structural, not vigilance-based.

**Second, the bias amplifies in groups that share priors.** A team of people who all start with the same hypothesis will collectively confirm it, with each member reinforcing the others' confidence. The empirical literature on "groupthink" (Janis 1972) is, in part, confirmation bias scaled to groups.

**Third, falsification-first design produces better hypotheses faster than confirmation-driven testing.** Wason's 2-4-6 subjects who proposed disconfirming sequences (like 5-7-9) discovered the correct rule on average 3-5 times faster than those who proposed confirming sequences only. This pattern holds in scientific research, debugging, due diligence, and strategic planning.
