# Method in Action: Sally Clark Case (1999)

> *This example is part of the [bayesian-reasoning](../SKILL.md) skill.*

The Sally Clark case is one of the most consequential demonstrations of how violating Bayesian reasoning produces wrongful convictions — and one of the most cited examples in modern statistical literature.

In 1996, Sally Clark, a British solicitor, lost her first son to what appeared to be Sudden Infant Death Syndrome (SIDS) at 11 weeks of age. In 1998, she lost her second son under similar circumstances at 8 weeks. She was charged with murdering both children.

At her 1999 trial, the prosecution called Sir Roy Meadow, an eminent pediatrician, as expert witness. Meadow testified that the probability of two SIDS deaths in a single affluent, non-smoking family was **1 in 73 million**. He arrived at this number by taking the published probability of SIDS in such a family (~1 in 8,543) and squaring it: 8,543² ≈ 73 million. He stated: "It's the chance of backing that long-odds outsider at the Grand National four years running."

The jury convicted Clark of murdering both sons. She served three years in prison before her conviction was overturned in 2003. She was found dead in 2007 — a death the coroner attributed to alcohol poisoning, after years of psychiatric distress.

The Meadow calculation contained at least three load-bearing Bayesian errors:

**1. Squaring assumed independence that does not hold.** SIDS deaths in a single family are not independent events. There may be unknown genetic, environmental, or familial-circumstance factors that elevate risk in *some* families above the population baseline. If the first SIDS death in a family raises (Bayes-update style) our estimate of those underlying factors, the probability of a second SIDS in the same family is much higher than the unconditional probability squared. The Royal Statistical Society later estimated the actual conditional probability — *given* one SIDS death in the family — to be on the order of 1 in 100, not 1 in 8,543.

**2. The prosecutor's fallacy.** Meadow's calculation, even if it had been right, would have given P(two SIDS deaths | this family has no murderer) ≈ 1 in 73 million. The jury was invited to infer P(this family has a murderer | two infant deaths) ≈ "huge." But these are not the same probability. The correct Bayesian framing requires also computing the probability of *two infant murders by the same parent* in a similar family — itself a rare event. The Royal Statistical Society's analysis suggested the prior probability of double infanticide is also extremely small — actually smaller than the realistic prior for double SIDS. When you do the Bayes calculation properly, **double SIDS is more likely than double infanticide, even with the supposedly-shocking 1-in-73-million number.**

**3. Base rate of murder vs SIDS in the population was ignored.** SIDS, while rare in any single family, is the leading cause of post-neonatal infant death in developed countries. Double infant murder by a mother is *vastly rarer* than double SIDS, at any reasonable prior. The vivid story of murder was treated as more probable than the unromantic but statistically more likely story of two SIDS deaths in a vulnerable family.

The Royal Statistical Society wrote a formal letter to the Lord Chancellor in 2001, stating in part:

> "The case ... is one of several recent instances where statistical evidence has been seriously misused in the courts. The calculation leading to 1 in 73 million is invalid because it assumes the deaths to be statistically independent. The Society wishes to express its concern that the misuse of statistical methods in the courts is causing miscarriages of justice."

— Royal Statistical Society. (2001, October 23). *Letter to the Lord Chancellor regarding the use of statistical evidence in court cases.* Reproduced at https://web.archive.org/web/20120925034735/http://www.rss.org.uk/uploadedfiles/documentlibrary/744.pdf

The case became the canonical British illustration of the prosecutor's fallacy and base-rate neglect. It has been studied in statistical, legal, and Bayesian-reasoning curricula since.

The deeper lesson, stated formally by Bayesian reasoning:

> "When you compute the probability of evidence E given hypothesis H, you have computed P(E|H). You have *not* computed P(H|E). The two can differ by orders of magnitude. To get from one to the other you need P(E|not-H) and P(H). Without those, P(E|H) is rhetorically powerful and decision-theoretically useless."

— Adapted from Jaynes, E. T. (2003). *Probability Theory: The Logic of Science.* Cambridge University Press. ISBN 978-0521592710, pp. 86-90, and from Berger, J. O. (1985). *Statistical Decision Theory and Bayesian Analysis* (2nd ed.). Springer-Verlag.

Three operational lessons from the Clark case and similar miscarriages (Lucia de Berk in the Netherlands; multiple wrongful medical-malpractice and security-screening cases):

**First, the prior is the highest-leverage variable.** Whatever the evidence does, it operates by multiplying the prior. If the prior is off by 100x, no amount of evidence quality saves you.

**Second, "this is consistent with X" is not Bayesian reasoning.** It is half of Bayesian reasoning. The other half is "this is also consistent with not-X." Without both, the evidence has no diagnostic content.

**Third, when independence assumptions are wrong, the error compounds nonlinearly.** Two pieces of correlated evidence treated as independent can produce a posterior off by orders of magnitude — exactly the magnitude of the 1-in-73-million number that helped convict an innocent woman.
