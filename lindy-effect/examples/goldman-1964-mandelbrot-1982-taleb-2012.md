# Method in Action: Goldman 1964, Mandelbrot 1982, Taleb 2012

> *Example for the [lindy-effect](../SKILL.md) skill.*

The principle has three formal moments.

The first is **Albert Goldman's 1964 New Republic essay**, which named the principle after Lindy's Deli on Broadway, where television comedians ate and gossiped about each other's career prospects. Goldman wrote:

> "The notion is that the future life expectancy of a non-perishable item is proportional to its current age. The lifetime of a television comedian is proportional to the total amount of his exposure on the medium. The comedian who has been on for ten years has, on average, ten more years ahead of him in the business. The comedian who has been on for ten weeks will be off within ten weeks. The math is rough, the empirical correlation is striking."
>
> — Goldman (1964), as cited in Taleb (2012), p. 318.

Goldman's observation predated the formal mathematics but captured the structural principle. Subsequent empirical studies in show-business career durations have confirmed the pattern.

The second formal moment is **Benoit Mandelbrot's 1982 mathematical formalization** in *The Fractal Geometry of Nature*. Mandelbrot connected the Lindy-style observation to power-law (Pareto) distributions, which had been extensively studied in the context of city sizes, wealth distributions, and earthquake magnitudes. The mathematical insight: for any distribution where the probability of survival to age T+t given survival to age T is a function of t/T alone (rather than depending on T as an absolute), the distribution is power-law. This is "self-similarity" in time — and is the structural reason why the Lindy effect operates.

The third formal moment is **Nassim Taleb's 2012-2018 operational extension** in *Antifragile* and *Skin in the Game*. Taleb's contribution:

> "What stays in print stays in print. The Iliad has survived three thousand years, so we can expect another three thousand years. A new book released this year is likely to be forgotten within a year. The relevant time-horizons are not symmetric: an idea that has survived two thousand years has been tested by every century of those two thousand years; an idea that emerged five years ago has been tested by half a decade. The two are not in the same league of empirical robustness. ...
>
> The reverse logic also holds: anything that *needs* the new to validate itself is structurally weak. The book that requires a 2024 interpretation of a 2024 trend to be relevant is unlikely to remain relevant when the trend passes. The book that has remained relevant across multiple paradigm shifts has, by survival evidence alone, met a higher bar."
>
> — Taleb, N. N. (2012). *Antifragile.* Random House, pp. 318-322.

Taleb's *Skin in the Game* (2018) extended the principle to practices and information sources:

> "When you eat a dish that has been cooked the same way for 400 years by 30 generations of people in a particular village, you are eating the safest meal in human history. The dish has been eaten by hundreds of thousands of people; the toxic ingredients have been weeded out; the cooks who made you sick have not had their recipes passed down. Compare this to a new "molecular gastronomy" technique, which has been tested by a small number of people for a short time. The Lindy effect on traditional cooking is the strongest food-safety endorsement that exists, far stronger than any FDA approval based on short-term study."
>
> — Taleb, N. N. (2018). *Skin in the Game.* Random House, pp. 184-186.

The empirical literature on the Lindy effect is large:

**Mandelbrot, B. (1982).** *The Fractal Geometry of Nature.* W. H. Freeman. The mathematical foundation.

**Eliazar, I., & Sokolov, I. M. (2010).** "Self-similar laws and the persistence of records." *Physica A: Statistical Mechanics and its Applications*, 389(20), 4329-4334. The statistical-physics treatment of Lindy-style scaling laws in record-survival data.

**Taleb, N. N. (2007).** *The Black Swan.* Random House. ISBN 978-1400063512. Where the Lindy idea is first informally discussed.

**Taleb, N. N. (2012).** *Antifragile: Things That Gain from Disorder.* Random House. ISBN 978-1400067824. Chapter 20 "Time and Fragility" develops the operational consequences.

**Taleb, N. N. (2018).** *Skin in the Game.* Random House. ISBN 978-0425284629. Chapter 11 extends to practices and information sources.

**Iturriza, M. (2019).** "Lindy effect in machine learning algorithm survival." *ACM Computing Surveys*, 52(4). An empirical study of which ML algorithms have survived and which have been replaced, broadly consistent with Lindy predictions.

**Cirillo, P., & Taleb, N. N. (2019).** "The Lindy effect for the longevity of statistical claims." *Significance*, 16(5), 22-27. Specifically about scientific findings: claims that have survived many replication attempts are statistically more likely to continue surviving.

The framework has operational implications across multiple domains:

**Software engineering / technology choice.** Foundational systems (programming languages, databases, operating systems) should be chosen by Lindy when switching cost is high. C (1972) and SQL (1974) are Lindy-stronger than recently-introduced alternatives. The argument is not that newer is bad — it is that the *prior* on a 50-year-old foundation continuing to work is much higher than for a 5-year-old foundation.

**Reading / information consumption.** The 30-year-old book that is still in print has earned its place; the new book from this month may be excellent or noise — Lindy is silent. Allocating reading time toward older books (with established Lindy track records) and recent books only when there is a strong reason produces a different reading list than newest-first allocation. Many serious readers (Buffett, Munger, Naval Ravikant) have explicitly endorsed Lindy-weighted reading.

**Institutional partnerships.** A 200-year-old institution (a bank, university, court system) has a strong Lindy prior for continuing to exist in another 200 years. A 5-year-old startup does not. For partnerships requiring multi-decade reliability (pension management, custodial services, infrastructure operation), Lindy is operationally important.

**Cultural practices.** Cuisines, agricultural rotations, religious practices, marriage and family structures that have persisted across many generations of changing conditions carry Lindy-evidence of fitness for human needs. This does not mean they should never be reformed — but the prior on continuation is strong.

**Scientific claims.** A scientific claim that has survived 50 years of attempted falsification is much more likely to continue surviving than a newly-published claim. The replication crisis (2011+ in psychology, expanding to other fields) has reinforced this: claims published recently have a much higher rate of failed replication than claims that have been replicated for decades.

**Investment strategy.** Investment principles that have produced returns across multiple market regimes (value investing since Graham 1934; index investing since Bogle 1975) have Lindy-stronger evidence than recent specialized strategies (factor investing, momentum strategies optimized on recent data).

Three operational lessons from Goldman, Mandelbrot, and Taleb:

**First, for foundational decisions, the Lindy prior is the right default.** When you don't have specific reason to prefer the new, prefer the old — it has the survival evidence the new does not. This is not nostalgia or conservatism; it is statistical inference.

**Second, "this time is different" is the most-falsified claim in history.** Carmen Reinhart and Kenneth Rogoff's *This Time Is Different* (2009) is essentially 800 years of evidence that "this time is different" was reliably wrong. The default should be that conditions have not changed enough to invalidate the Lindy prior; the change-claim bears the burden of proof.

**Third, Lindy is statistical, not deterministic.** Old things do die; new things do survive. The principle is about populations of similar items, not about any single item. The right operational use is to set priors and to filter, not to predict specific outcomes.
