# Method in Action: Galton 1886 + Kahneman 2011 Chapter 17 Israeli Air Force

> *Example for the [regression-to-the-mean](../SKILL.md) skill.*

**Francis Galton** (1822–1911) was a Victorian polymath: cousin of Charles Darwin, founder of the field of biometrics, and (less savorily) the founder of eugenics. His 1886 paper documenting the regression phenomenon was a methodological breakthrough. He had collected height data on 928 adult children and 205 sets of parents at the International Health Exhibition in London (1884) — a dataset that was, for its time, extraordinarily large and well-controlled.

Galton's empirical finding was the contraction toward the mean across generations. Tall parents had children averaging shorter than themselves but still taller than the population mean. The contraction was systematic. Galton's framing — "regression towards mediocrity" — has stuck, though his interpretation (that a "force" was pulling toward mediocrity) is now understood to be wrong.

> "The law of Regression towards Mediocrity that I have proposed is precisely this: Every peculiarity in a man is shared by his kindred, but on the average in a less degree. ... I find that the height of an adult offspring deviates from the mid-parent height by a fraction (about two-thirds) of the deviation of the mid-parents from the average."
>
> — Galton (1886), pp. 247, 252.

The correct interpretation, developed in the 20th century, is that any noisy measurement of a stable underlying signal will produce extreme observations partly via lucky/unlucky noise. Retest will not repeat the noise; the underlying signal is preserved but the noise component regresses.

**Kahneman's Israeli Air Force example (2011, chapter 17).** This is the most influential operational illustration of the regression artifact. Kahneman was teaching Israeli Air Force flight instructors about behavioral psychology. He emphasized that positive reinforcement (praise) is more effective than punishment in training, citing established psychological research.

An instructor (whom Kahneman described as senior and respected) pushed back:

> "On many occasions I have praised flight cadets for clean execution of some aerobatic maneuver. The next time they try the same maneuver they usually do worse. On the other hand, I have often screamed into a cadet's earphone for bad execution, and in general he does better on his next try. So please don't tell us that reinforcement works and punishment does not, because the opposite is the case."
>
> — quoted in Kahneman (2011), p. 175.

Kahneman's response was the breakthrough: the instructor was observing regression to the mean, mistaken for a causal effect of praise/criticism.

When a cadet executes a maneuver exceptionally well, that performance includes a positive noise component (lucky day, favorable winds, instructor's attention, etc.). On the next attempt, the noise component will be different (likely less favorable); the underlying skill is the same; the next performance is statistically expected to be worse — regardless of whether the instructor praised or did nothing.

When a cadet executes badly, the performance includes a negative noise component. On the next attempt, the noise is different; the next performance is statistically expected to be better — regardless of whether the instructor screamed or did nothing.

The instructor was reading: praise → worse performance, criticism → better performance. The truth was: extreme observations → regression to the mean. The instructor's causal inference was driven by a statistical artifact.

Kahneman's framing:

> "Because we tend to reward others when they do well and punish them when they do badly, and because there is regression to the mean, it is part of the human condition that we are statistically punished for rewarding others and rewarded for punishing them."
>
> — Kahneman (2011), p. 175.

This is generalizable. Many domains exhibit the same pattern:

**Sales performance.** A salesperson who blew out a quarter gets a bonus. Next quarter they perform less well; manager wonders if the bonus de-motivated them. A salesperson who had a terrible quarter gets a stern talk. Next quarter they perform better; manager thinks the talk worked. Both inferences are likely regression.

**Sports coaching.** A breakout rookie season gets praise; sophomore year is worse — coaches wonder what went wrong. A struggling player gets benched; on return they perform better — coaches credit the benching. Both partly regression.

**Investment fund manager evaluation.** A fund manager who beat the market gets capital inflows; next period they underperform — LPs feel duped. A fund manager who underperformed gets fired; the replacement does better — board credits the replacement. Both partly regression.

**Acquisition targets.** Companies are typically acquired near peak performance. Post-acquisition, performance regresses. The acquirer is disappointed; narrative blames integration. Often: partly regression.

**Patient improvement after medical intervention.** Patients seek treatment when symptoms are most extreme. Symptoms regress regardless of treatment. The patient credits the treatment.

**Customer satisfaction interventions.** A team with low satisfaction gets training; satisfaction improves. Without a control, the improvement could be mostly regression.

Three operational lessons:

**First, use control groups or baseline regression estimates.** When evaluating interventions, the question is not "did the metric change?" but "did the metric change more than it would have changed by regression alone?" The control group reveals the regression baseline.

**Second, watch for "praise reduces performance, criticism improves it" patterns.** When you find yourself thinking that punishment works and praise doesn't, you are almost certainly observing regression artifact. Update your hiring, management, and intervention conclusions accordingly.

**Third, beware celebrating or punishing single-period extreme performance.** A single-quarter top performer is partly noise; promoting them based on one quarter will partly regret. A single-quarter struggler is partly noise; firing them based on one quarter will partly regret. Use longer windows to reduce noise.
