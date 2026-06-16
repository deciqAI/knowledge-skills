# Method in Action: Tversky & Kahneman's Wheel of Fortune, 1974

> *Example for the [anchoring](../SKILL.md) skill.*

The empirical foundation for anchoring as a strategic concern was established in a single, brief experiment described in a 1974 *Science* paper that has become one of the most-cited articles in 20th-century behavioral science. Amos Tversky and Daniel Kahneman, then collaborating between the Hebrew University of Jerusalem and the Oregon Research Institute, were systematically documenting the heuristics by which people produce estimates under uncertainty. Their paper "Judgment under Uncertainty: Heuristics and Biases" (*Science*, Vol. 185, No. 4157, 27 September 1974, pp. 1124–1131) introduced three heuristics — representativeness, availability, and anchoring — that have since framed the entire field. The anchoring experiment was perhaps the most visually arresting of the three.

The setup, as described by Tversky and Kahneman in the paper:

> "In a demonstration of this effect, subjects were asked to estimate various quantities, stated in percentages (for example, the percentage of African countries in the United Nations). For each quantity, a number between 0 and 100 was determined by spinning a wheel of fortune in the subjects' presence. The subjects were instructed to indicate first whether that number was higher or lower than the value of the quantity, and then to estimate the value of the quantity by moving upward or downward from the given number."

— Tversky, A., & Kahneman, D. (1974). "Judgment under Uncertainty: Heuristics and Biases." *Science*, 185(4157), p. 1128. https://doi.org/10.1126/science.185.4157.1124

There are several features of this design worth noting before reading the result. **First**, the wheel was rigged. It had been physically constructed to stop only at 10 or 65; this was unknown to the subjects, who saw it spin and stop in the ordinary fashion. **Second**, the subjects were told explicitly that the wheel was random — there was no claim that the number had any informational connection to African UN membership. **Third**, the subjects had to **first compare** their own internal estimate to the wheel's number (saying whether their answer was higher or lower) before producing the estimate, ensuring they had consciously processed the wheel number. **Fourth**, the question being asked — what percentage of UN member states are in Africa — has a single correct numerical answer that the subjects either knew or didn't; there is no ambiguity about what is being estimated.

The result, in Tversky and Kahneman's own words:

> "For example, the median estimates of the percentage of African countries in the United Nations were 25 and 45 for groups that received 10 and 65, respectively, as starting points."

— Tversky & Kahneman (1974), p. 1128.

Two groups of subjects, drawn from the same population, given identical instructions, identical questions, identical incentives, differed in median estimate by twenty percentage points. The only thing that differed was the number on the wheel they had watched spin. The number was random. The subjects had been told it was random. They had every reason to ignore it. The effect operated anyway.

Tversky and Kahneman noted a further feature of the result that has become the operational core of the anchoring literature:

> "Payoffs for accuracy did not reduce the anchoring effect."

— Tversky & Kahneman (1974), p. 1128.

This sentence is short and it matters. In the standard rational-actor framework of decision theory, paying subjects for accuracy should eliminate any irrational deviation from the truth: if subjects know they will earn more by getting closer to the right answer, and if the wheel number is genuinely irrelevant, they should ignore it. They did not. The bias survived the incentive structure that, in theory, should have switched it off. This is the property that elevates anchoring from a laboratory curiosity to a structural feature of human judgment: it operates **below the level where economic incentives can reliably reach it**.

The 1974 paper extended the anchoring finding in a second experiment with quantitative compounding. Two groups of high-school students were given five seconds to estimate the value of a mathematical product:

- One group: **8 × 7 × 6 × 5 × 4 × 3 × 2 × 1**
- Other group: **1 × 2 × 3 × 4 × 5 × 6 × 7 × 8**

The two expressions have the same product: 40,320. They are mathematically identical. But the order in which the numbers were presented produced dramatically different anchoring effects, because subjects given five seconds to estimate could only perform the first few multiplications and then extrapolate. The descending-order group had early products in the thousands and produced a median estimate of **2,250**. The ascending-order group had early products in the dozens and produced a median estimate of **512**. The correct answer is 40,320. Both groups underestimated dramatically; the descending group underestimated less because their early multiplications anchored them higher.

This second experiment is operationally illuminating because it reveals **how anchoring actually operates in real estimation**. In the wheel-of-fortune setup, the anchor is overtly external — a spinning wheel. In the multiplication experiment, the anchor arises from the first few steps of the subject's own reasoning. The mechanism is the same: **early information disproportionately weights the final estimate**, even when the early information is just the order in which numbers were presented. Anchoring is not a separate cognitive process; it is a property of how human estimation proceeds — starting from a reference, adjusting insufficiently, stopping when the answer feels approximately right.

The 1974 paper has been replicated, refined, and stress-tested for the past fifty years across a startling range of domains. **A short selection of consequential replications:**

- **Real estate valuation (Northcraft & Neale 1987).** Experienced real-estate agents were shown a house and given a packet of information including the listing price. The listing prices were varied between groups — some agents saw a high listing, others a low one. The agents then produced their own "professional" valuations. Their valuations followed the listing price by approximately 41% of the variation, even though every agent denied that the listing price had influenced their judgment.

- **Legal sentencing (Englich, Mussweiler & Strack 2006).** Experienced judges read a hypothetical criminal case file, then learned that the prosecutor had requested a sentence; the requested sentence was varied between groups. Judges' final sentences were systematically influenced by the prosecutorial anchor. Even more strikingly: the same effect occurred when the "anchor" was the result of the judges literally rolling dice in front of the experimenter, with the dice rigged. Sentences differed by months depending on the dice result.

- **Salary negotiations (Galinsky & Mussweiler 2001).** MBA students participated in a simulated negotiation. Those who made aggressive opening offers — high if they were selling, low if they were buying — achieved final outcomes substantially more favorable to them than those who opened conservatively. Critically, the conservative openers had *expected* their approach to be more successful (because they thought it would generate goodwill); the data went the other way.

- **Auction outcomes (Ariely, Loewenstein & Prelec 2003).** MIT MBA students were asked to write down the last two digits of their Social Security number, then participate in an auction for various items. The Social Security number — random, irrelevant, known to be so by the subjects — predicted bid amounts. Subjects with higher Social Security number suffixes bid up to 3x more for the same items than subjects with lower suffixes.

The episode teaches the following points that running an anchoring analysis correctly requires you to internalize.

**First, anchoring is not weakness; it is structural.** The wheel-of-fortune experiment used educated subjects in a context where the irrelevance of the anchor was explicit. The bias operated anyway. Subsequent replications used professional judges, real-estate experts, and MBA students; the bias operated on all of them. The bias is not a result of failing to notice the anchor or failing to be smart enough to ignore it. It is a structural property of how human cognition produces estimates — starting from whatever number is present and adjusting insufficiently. **You cannot defeat anchoring by being smarter, more careful, or more skeptical.** You can only defeat it through structured procedures (counterfactual generation, opposite-anchor consideration) and through structural arrangements (producing your number before any external anchor is introduced).

**Second, the irrelevance of the anchor does not protect you.** This is the most counterintuitive finding in the literature and the one most often denied by sophisticated subjects. The 1974 wheel was overtly random. The Social Security number in the Ariely auction was overtly irrelevant. The dice in the Englich sentencing experiment were rolled in front of the judges. In all three cases, the subjects knew the anchor was uninformative. In all three cases, the bias operated. **The cognitive machinery that produces estimates does not first check whether the available reference is informative; it uses what is there.** This is why the standard verbal disclaimer ("just throwing out a number, don't take it seriously") does not actually neutralize the anchor — and why anyone who introduces such a disclaimer should be assumed to be doing it as a courtesy, not as a real reset.

**Third, incentives do not switch off the bias.** Tversky and Kahneman's noted finding — that "payoffs for accuracy did not reduce the anchoring effect" — has been replicated repeatedly. People who are paid more for accuracy do not anchor less; in some studies they anchor slightly more, because the higher stakes make them more risk-averse about deviating from a reference point. **In your business decisions, the high stakes of the deal are not, by themselves, going to protect you from anchoring.** If anything, they may amplify it.

**Fourth, the proposer has structural power.** If you are the one putting the first number on the table, you are anchoring everyone in the conversation, including yourself. Galinsky & Mussweiler's negotiation research is the cleanest evidence: bold openers do better, and they do better by amounts large enough to dominate any goodwill cost from being aggressive. The cost of "going first with a number that feels too aggressive" is almost always lower than the cost of letting the counterparty anchor first. **In any negotiation where the order of opening offers is yours to choose, default to going first with a bold number.**

**Fifth, defense is structural before it is procedural.** The procedural defenses — generate-your-own-number-first, consider-the-opposite, name-the-anchor — measurably reduce but do not eliminate the bias. The strongest defense is **structural**: arrange the process so you have your own number before any external anchor is introduced. Do the valuation work before reading the seller's listing. Set the salary range before opening the offer email. Forecast the project duration before hearing the executive's deadline. The anchor pulls toward itself; the only way to neutralize it is to bring your own anchor.

The 1974 *Science* paper is barely seven pages long and reports a handful of small experiments. Yet, alongside Kahneman's later Nobel Prize, it stands as one of the most consequential empirical results in the cognitive sciences. The wheel-of-fortune demonstration is the irreducible core of the modern operational understanding of anchoring: a random number, known to be random, told to be ignored, moved median estimates by twenty percentage points. Every modern application of anchoring in business, law, negotiation, and policy ultimately rests on that finding.
