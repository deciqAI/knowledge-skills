# Method in Action: Hanlon's Submission, 1980; Heinlein's 1941 Articulation

> *Example for the [hanlons-razor](../SKILL.md) skill.*

The Hanlon's Razor formulation that spread across modern internet culture, business writing, and decision-theory literature was submitted by **Robert J. Hanlon** of Scranton, Pennsylvania, to the 1980 humor compendium *Murphy's Law Book Two: More Reasons Why Things Go Wrong*, edited by Arthur Bloch:

> "Never attribute to malice that which is adequately explained by stupidity."

— Hanlon, R. J. (1980). In Bloch, A. (Ed.). *Murphy's Law Book Two.* Price/Stern/Sloan. ISBN 978-0843105674.

The submission was one of dozens in a humorous compendium. Most have been forgotten. Hanlon's became one of the most-cited heuristics of the next 40 years — a fact that should itself give pause.

The deeper history runs back further. **Robert A. Heinlein**, in his 1941 novella "Logic of Empire" (published in *Astounding Science Fiction*, later collected in *The Past Through Tomorrow*, 1967), wrote a passage that historians of the saying believe Hanlon either independently re-discovered or consciously adapted:

> "You have attributed conditions to villainy that simply result from stupidity."

— Heinlein, R. A. (1941). "Logic of Empire." *The Past Through Tomorrow.* Putnam, 1967. ISBN 978-0399108211, p. 224.

The "Logic of Empire" context is instructive. Heinlein's protagonists are abolitionists who have come to believe the slavery system on Venus is being maintained by an evil conspiracy. The older character corrects them: the system persists not because of conspiracy but because of structural incompetence — bad information, misaligned incentives, individual short-term rationality producing collective long-term harm. The point: **systems that look like conspiracies are usually structures that have evolved to produce the same outcome without anyone planning it**. This is Hanlon's razor applied at the level of institutions, not individuals.

Even earlier, **Johann Wolfgang von Goethe** had written in *Sorrows of Young Werther* (1774):

> "Misunderstandings and lethargy perhaps produce more wrong in the world than deceit and malice do. At least the last two are certainly rarer."

— Goethe, J. W. (1774). *Die Leiden des jungen Werthers.* As discussed at https://quoteinvestigator.com/2016/12/30/not-malice/

The three formulations span 200+ years, three languages, and quite different cultural contexts — yet articulate the same calibration error. The fact that the observation keeps being independently re-derived suggests a robust underlying psychological fact: **humans systematically over-attribute malice.**

The empirical psychology supports the heuristic. The **fundamental attribution error** (Ross 1977) documents that humans attribute others' behavior to disposition (intent, character) while attributing their own similar behavior to situation (circumstance, pressure). When someone cuts us off in traffic, "they're a jerk" (disposition); when we cut someone off, "I had an emergency" (situation). Hanlon's razor is a corrective: extend the situation-attribution we apply to ourselves to others' behavior.

> "The tendency for people to over-emphasize personal characteristics and ignore situational factors in judging others' behavior. ... Because of the fundamental attribution error, we tend to believe that others do bad things because they are bad people."
>
> — Ross, L. (1977). "The intuitive psychologist and his shortcomings: Distortions in the attribution process." *Advances in Experimental Social Psychology*, 10, 173-220.

The framework has been adopted operationally:

**Software engineering.** Post-mortems of production failures routinely apply Hanlon's razor: the engineer who pushed the bad commit was not malicious, and the corrective is process/tooling, not punishment. Google's **blameless postmortem** practice is Hanlon's razor institutionalized.

**Corporate management.** Andy Grove, in *High Output Management*, applied the heuristic to performance management: a subordinate who keeps making the same mistake is most often not insubordinate — they are missing information, training, or context.

**International diplomacy.** The "rational actor" framework in international relations is an application at the state level: states act in their own (sometimes incompetent) interest rather than out of pure malice.

The framework also has documented failure modes:

**First, the razor can be weaponized.** People who have caused real harm can invoke Hanlon's razor to deflect accountability. The defense: the razor specifies a *starting prior*, not a final attribution. Repeated incompetence-causing-harm despite available information eventually becomes equivalent to malice in practical effect.

**Second, the razor can disable necessary protective response.** When the cost of being wrong about non-malice is catastrophic (abusive partner, predatory company, hostile state), the calibrated prior must shift toward defensive posture *before* malice is proven.

**Third, the razor doesn't excuse harm.** A bridge that collapses through incompetence has still collapsed. The point is *attribution*, not *accountability*. Once incompetence is identified, the corrective is competence-building, not blame-shifting.

Three operational lessons from extensive application:

**First, the conversation that follows from mistake-prior is almost always better than the one that follows from malice-prior — even when it later turns out to be malice.** Clarifying conversations produce information; accusatory ones produce defensiveness.

**Second, the malice attribution feels viscerally correct in real-time and almost always feels overconfident in retrospect.** This calibration error is robust.

**Third, the razor scales from individual to institutional.** Most "bad culture" / "broken system" complaints are about coordination failure, not coordinated malice.
