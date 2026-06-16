# Method in Action: Van Valen 1973 + Intel vs. AMD 1990–2010

> *Example for the [red-queen-effect](../SKILL.md) skill.*

**Leigh Van Valen** (1935–2010) was a University of Chicago evolutionary biologist and paleontologist. His 1973 paper "A New Evolutionary Law" was published in *Evolutionary Theory*, Volume 1 — a journal he founded himself after the mainstream evolutionary biology journals rejected the paper. The paper's central empirical finding was that the probability of extinction for a taxon was roughly constant across the lifespan of that taxon — well-adapted, long-surviving species did not have lower extinction rates than newly-evolved species.

The interpretation: in a co-evolutionary system, a species' environment is largely composed of other species. Every adaptation by one species changes the fitness landscape for others, which evolve counter-adaptations, which change the landscape back. The net result is a system where absolute fitness increases continuously but relative fitness — fitness *against the current field* — remains approximately constant. Van Valen named this dynamic after Lewis Carroll's Red Queen:

> "It takes all the running you can do, to keep in the same place."
>
> — Carroll, L. (1871). *Through the Looking-Glass.* Macmillan. Chapter 2.

The business application that best illustrates the Red Queen at industrial scale is the **Intel vs. AMD semiconductor arms race, 1990–2010**.

Both companies were bound by Moore's Law — the empirical regularity (not a physical law) that transistor density on integrated circuits roughly doubles every 18–24 months. Intel and AMD each invested massively to track Moore's Law: fabrication process improvements (from 800nm in 1990 to 32nm in 2010), microarchitecture redesigns, cache hierarchy innovations, instruction set extensions.

The results were extraordinary in absolute terms: a 2010 processor was roughly 1000× faster than a 1990 processor in single-thread performance. Both companies ran as fast as they could.

The competitive result: market share barely moved. Intel held 75–85% of the x86 desktop and server processor market throughout this period. AMD held 15–25%. The share distribution in 2010 looked almost identical to 1990, despite both companies having invested tens of billions of dollars in the race.

Where did the value go? To consumers — Moore's Law primarily produced consumer surplus: cheaper, faster personal computers that drove the internet era, the PC revolution, and ultimately mobile computing. The companies running the race were the mechanism through which technology value was transferred to buyers rather than retained as corporate profit.

The escape: neither Intel nor AMD escaped the Red Queen in this period. AMD eventually exited the manufacturing race (foundry to TSMC) and refocused on design — a partial vertical disintegration that reduced Red Queen exposure. Intel's escape vector came from a different direction: Xeon server processors for the cloud era, where switching costs (data center architecture lock-in) provided temporary protection. But the deeper Red Queen escape came from ARM architecture — not a company in the x86 race, but a fundamentally different instruction set that made the x86 Red Queen largely irrelevant in mobile, and increasingly in data centers (Apple M-series, AWS Graviton). ARM did not run faster in the x86 race. It changed the track entirely.

The operational lesson for founders and operators: identify whether you are in a race to win or a race to maintain. In many industries, the race is to maintain — every investment you make produces a temporary advantage that competitors replicate within 12–24 months, and the permanent outcome of all that running is that your starting position is roughly where you finished. Recognizing this early allows capital allocation toward escape vectors before the sunk-cost trap of the arms race becomes the primary organizing principle of the business.
