# Method in Action: Abraham Wald and the Statistical Research Group, 1943

> *Example for the [survivorship-bias](../SKILL.md) skill.*

The canonical demonstration of survivorship bias is **Abraham Wald**'s wartime work at the **Statistical Research Group (SRG)** at Columbia University, 1942-1945. The SRG was the secret mathematical-statistics arm of the wartime US government, comparable in caliber to the Manhattan Project for statistics: it included Wald, Allen Wallis, Milton Friedman, Frederick Mosteller, and Jacob Wolfowitz, among others.

The bomber-armor problem was assigned to the SRG in 1943. The US Navy was losing aircraft over Europe and the Pacific in unsustainable numbers. The problem was to determine where to add additional armor on B-17 and B-24 bombers — adding armor everywhere would make the plane too heavy to fly its mission, so the armor had to be concentrated where it would do the most good. The Navy collected data on bullet holes and damage patterns in aircraft that returned from missions.

The pattern looked clear. Damage was concentrated in specific areas:

- **Wings:** many holes
- **Fuselage center:** many holes
- **Tail section:** many holes
- **Engine area:** few holes
- **Cockpit / pilot area:** few holes

The Navy's analyst recommended adding armor to the areas with the most damage — the wings, fuselage, and tail. Wald reviewed the data and recommended the *opposite*.

His reasoning, preserved in the SRG memorandum CRC 432, July 1943 (declassified 1980), opens with what may be the most famous selection-effect argument in 20th-century applied statistics:

> "The bullet holes are concentrated where the armor is not needed. The aircraft that we observe — the ones that returned — have damage on the wings, fuselage, and tail. The aircraft that did not return are not in our sample. They were shot down because they were hit where we observe little damage in the returnees: the engines and the cockpit. The damage we observe is the damage that planes can sustain and still fly home. The missing damage — the gaps in our pattern — is the lethal damage. Armor must go where the returners show no holes."
>
> — Wald, A. (1943). "A Method of Estimating Plane Vulnerability Based on Damage of Survivors." SRG Memorandum CRC 432, Statistical Research Group, Columbia University. Republished in 1980 as CNA Memorandum.

The recommendation was implemented. Modeled losses dropped substantially. Wald's analysis became foundational to the **selection-effects literature** in statistics, econometrics, and epidemiology.

The deeper lesson Wald drew: **the observed sample is conditional on survival**, and the conditional distribution can be the opposite of the unconditional distribution. The damage pattern in returning aircraft is *anti-correlated* with the damage pattern in shot-down aircraft, because the very planes that absorbed the most lethal hits are absent from the data.

Wald's framework was systematized. The post-war statistics literature developed:

**Heckman selection correction (1979).** James Heckman, building on Wald's logic, developed the formal mathematical framework for selection-corrected estimation. The "Heckman correction" is the standard treatment in modern econometrics; it won Heckman the 2000 Nobel Prize in Economics. See Heckman, J. J. (1979). "Sample selection bias as a specification error." *Econometrica*, 47(1), 153-161.

**Publication bias in scientific research.** Studies showing positive effects are more likely to be published than studies showing null effects. Ioannidis (2005) "Why most published research findings are false," *PLoS Medicine*, 2(8), e124, drew on this. Survivorship bias at the meta-research level: the published literature is the survivor sample of all conducted research.

**Funds and indices in finance.** Brown, Goetzmann, Ibbotson, and Ross (1992), "Survivorship Bias in Performance Studies," *Review of Financial Studies*, 5(4), 553-580, demonstrated that mutual fund returns reported in standard databases were systematically biased upward because failed funds had been dropped. The corrected estimates were 1-3 percentage points lower per year — a massive effect compounded over decades.

**Architecture and historical preservation.** When we say "they built things to last in the old days," we mean: the buildings that survived to be admired today are the ones built to last. The crumbling sheds, the collapsed houses, the burned-down tenements are not in the visible inventory. Modern buildings face the same survival filter; we just haven't done the filtering yet.

**Cultural products.** The "classics" of literature, music, and film are the survivors of centuries of evaluation. The forgotten 19th-century novels include masterpieces and unreadable hack work; the survivors are a biased sample. The same is true of folk traditions, religious texts (the documents that didn't get copied are gone), and historical figures.

The framework's most consequential modern application is in **startup and venture capital reasoning**. The base rate for startup failure is roughly 90% over 10 years; for venture-backed startups, roughly 75%. Most popular advice ("pivot quickly," "found in a garage," "raise from top-tier VCs") comes from the surviving 10-25%. The non-survivors include companies that did all the same things and failed. The advice may be correct, or it may be selection effect — the data alone cannot distinguish.

Peter Thiel articulated the survivorship-bias problem in startup wisdom in *Zero to One* (2014):

> "The most successful companies arrange every single piece of their business around a single insight — what they call a 'secret' — that other people don't share. The trouble is, we can only see this pattern in retrospect, among the companies that won. The companies that had a 'secret' that turned out to be wrong are dead, and we can't see them. So we cannot distinguish between 'successful companies all had a secret' (a causal claim) and 'companies with secrets had high variance, and we only see the upside tail.'"
>
> — Thiel, P. & Masters, B. (2014). *Zero to One: Notes on Startups, or How to Build the Future.* Crown Business. ISBN 978-0804139298, p. 95-97.

This is a remarkable concession from a venture capitalist whose business depends on identifying winners: the standard story of "what successful companies did" is structurally vulnerable to survivorship bias, and the available data cannot resolve it.

Three operational lessons from extensive application:

**First, the bias is invisible without explicit attention.** The survivor sample is what's *available* to study; the non-survivor sample is, by definition, hard to access. The default analysis silently ignores the missing data. Only deliberate questioning ("what would the non-survivors look like?") brings the bias into view.

**Second, the bias produces over-confident wrong conclusions, not random error.** Survivorship bias is directional — it always inflates the appearance of cause-effect in survivor traits. This makes it especially dangerous in advice and prediction: the wrong answer is confidently presented.

**Third, the only structural correction is access to non-survivor data.** When the non-survivor data is available (failed companies, dead patients, unpublished studies), corrected analysis is possible. When it's not, conclusions must be marked as conditional on the survivor sample.
