# Method in Action: Baruch Fischhoff's Nixon-China Trip Study, 1972-1975

> *Example for the [hindsight-bias](../SKILL.md) skill.*

The empirical foundation for hindsight bias as a formal cognitive phenomenon is **Baruch Fischhoff**'s doctoral work at Hebrew University, published in two landmark 1975 papers:

> Fischhoff, B. (1975). "Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty." *Journal of Experimental Psychology: Human Perception and Performance*, 1(3), 288-299.
>
> Fischhoff, B., & Beyth, R. (1975). "'I knew it would happen': Remembered probabilities of once-future things." *Organizational Behavior and Human Performance*, 13(1), 1-16.

The Nixon-Beyth study (often called the "Nixon-China study") had a clean design. In February 1972, before President Richard Nixon's two-week diplomatic tour of China (Feb 21-28) and the Soviet Union (May 22-30), Fischhoff and Beyth presented Israeli undergraduate subjects with a list of 15 possible outcomes:

- Nixon would meet Chairman Mao Zedong
- The U.S. would establish a permanent diplomatic mission in Peking
- The U.S. and China would issue a joint communiqué
- Nixon would announce a U.S. policy of two-Chinas (recognizing both Taipei and Peking)
- A group of American POWs from Vietnam would be released
- ... (10 more)

Subjects estimated the probability of each event, on a 0-100% scale. The trips then occurred. Some events happened (Nixon-Mao meeting, joint communiqué), others did not (no permanent mission established, no two-Chinas announcement, no POW release).

Then, two weeks, two months, and four months after the trips, Fischhoff asked the same subjects to *recall* their original probability estimates. He compared the recalled estimates with the actual original responses.

The findings, in Fischhoff and Beyth's own words:

> "Subjects' memory for the probabilities they had originally assigned was systematically biased in the direction of the actual outcome. For events that had occurred, subjects recalled having predicted higher probabilities than they actually had recorded. For events that had not occurred, they recalled lower probabilities than they had recorded. The mean absolute error in recall was 9.4 percentage points at two weeks, rising to 11.5 percentage points at four months. The direction of the shift was consistent with hindsight bias in 70% to 85% of cases, depending on the event and the time delay."
>
> — Fischhoff & Beyth (1975), p. 8.

The effect was not eliminated by:
- High confidence in memory (subjects who were *most* sure they remembered correctly were just as biased).
- Interest in the political subject matter (engaged subjects were biased just as much as uninterested ones).
- A short time delay (the bias was already substantial at two weeks).

In a companion study, Fischhoff's 1975 *JEP:HPP* paper used the British-Gurkha War of 1814 — a historical event most subjects had no prior knowledge of. He gave subjects a 150-word description of the strategic situation and asked them to estimate the probability of four possible outcomes: British victory, Gurkha victory, stalemate, no military resolution. Critically, different groups of subjects were told different outcomes had actually occurred before being asked for their probability estimates. The instruction was explicit: "Estimate the probabilities *as if you did not know which outcome occurred*."

Fischhoff's finding:

> "Subjects told that the British had won assigned the British victory a mean probability of 57.2%. Subjects told that the Gurkhas had won assigned a Gurkha victory a mean probability of 38.4% — substantially higher than the 21.3% assigned by subjects told there had been no military resolution. The mere knowledge of the outcome shifted estimated probabilities upward by 15 to 25 percentage points, *despite explicit instructions to ignore that knowledge*. Subjects were unable to disregard outcome information when reconstructing how probable the outcome 'should have looked' beforehand."
>
> — Fischhoff (1975), p. 293.

This was the breakthrough finding: the bias is not in deliberate self-deception, nor in motivated reasoning, nor in failure of effort. It is in the cognitive impossibility of reconstructing a prior epistemic state that has been overwritten by subsequent information. The mind cannot un-know what it knows.

The implications were operationally massive:

**Post-mortem unfairness.** Every post-disaster analysis (investment loss, business failure, military defeat, medical misdiagnosis, engineering accident) is conducted by people who know the outcome. Their reconstruction of "what should have been obvious" is systematically biased toward making the actual outcome seem more predictable than it was. Decision-makers are routinely judged as negligent for failing to foresee outcomes that, ex ante, were genuinely uncertain.

**Legal liability.** Tort law often hinges on whether a defendant "should have known" of a risk. Hindsight bias systematically inflates jurors' assessments of foreseeability. Empirical studies (Kamin & Rachlinski 1995, *Law and Human Behavior* 19(1)) show that mock jurors evaluate the same precautionary decision as negligent at much higher rates when they know an accident occurred than when they evaluate the decision ex ante.

**Investment evaluation.** Returns are visible; the decision process is not. A fund manager who took a 30%-probability bet that paid off looks like a genius; one who took the same bet and lost looks like a fool. Both decisions had identical expected value. Hindsight bias rewards lucky decisions and punishes unlucky ones, generating systematic miscalibration in portfolio assessment.

**Strategic planning.** "We should have predicted the financial crisis / the pandemic / the rise of X / the fall of Y" — these claims are almost always hindsight-biased. The information available before the event would, in honest reconstruction, support a much lower probability estimate than the post-event narrative suggests.

The follow-up literature established the bias as universal and structural:

**Slovic & Fischhoff (1977).** *JEP:HPP* 3(4). Showed the bias persists when subjects are explicitly trained in it and warned about it. Self-vigilance is weakly effective.

**Christensen-Szalanski & Willham (1991).** *OBHDP* 48(1). A meta-analysis of 122 studies confirmed the bias is robust across populations, domains, and methodologies. Effect size: Cohen's d ≈ 0.39, considered moderate-to-large in social psychology.

**Roese & Vohs (2012).** *Perspectives on Psychological Science* 7(5), 411-426. The canonical review. Decomposed the bias into the three components (memory, inevitability, foreseeability) and reviewed evidence that each has distinct underlying mechanisms and distinct countermeasures.

**Tetlock (2015).** *Superforecasting.* Crown. ISBN 978-0804136693. The Good Judgment Project's calibration-training methodology is, in operational terms, an industrial-scale antidote to hindsight bias: explicit pre-commitment of probability estimates, then scoring against outcomes. Forecasters trained this way reduced hindsight bias by ~40% compared to controls (Mellers et al. 2014, *Psychological Science* 25(5)).

The framework has reshaped multiple operational disciplines:

**Aviation accident investigation.** The NTSB's investigation protocol explicitly warns against hindsight bias and requires investigators to reconstruct the cockpit information environment *as the pilots experienced it*, before introducing outcome data. The investigation is conducted in two phases (facts first, then analysis) to bound the bias.

**Medical M&M (Morbidity & Mortality) conferences.** Modern protocols require discussion of the diagnostic reasoning available at each decision point, with outcome data introduced only after the process review. The bias is bounded structurally because the post-mortem is split temporally.

**Software engineering blameless post-mortems.** Pioneered at Etsy and Google, the practice (described in Allspaw 2012, "Blameless PostMortems") explicitly trains responders to reconstruct the engineer's information state at the time of action. Outcome-driven blame is institutionally banned. The goal is to learn about the system, not to punish foreseeability.

**Investment decision journals.** Adopted by Bridgewater (Dalio 2017), Ray Dalio's "issue log," and many systematic investors. Predictions and reasoning are logged before outcomes. Quarterly reviews compare logged reasoning against outcomes, distinguishing process error from outcome variance.

**Intelligence analysis.** The CIA's structured analytic techniques (Heuer & Pherson 2010) include "What If? Analysis" and "Devil's Advocacy," both designed to make plausible alternative outcomes salient and to bound the "anyone should have seen it coming" component of hindsight bias.

Three operational lessons from Fischhoff:

**First, the bias is invisible to introspection.** Subjects who were *most confident* in their memory of prior judgments were just as biased. The corrective must be structural — contemporaneous records — not vigilance-based.

**Second, the bias systematically transfers blame from the outcome to the decision-maker.** "He should have known" is the canonical phrase. In the absence of pre-commitment documentation, the bias produces unfair retrospective judgments at scale.

**Third, the bias is amplified by emotion and stakes.** Studies of medical, legal, and military post-incident reviews show the bias is *larger* for high-stakes outcomes (Hawkins & Hastie 1990, *Psychological Bulletin* 107(3)). When the outcome was catastrophic, the certainty that "we should have predicted it" is correspondingly inflated — exactly when the institutional consequences of unfair retrospective judgment are highest.
