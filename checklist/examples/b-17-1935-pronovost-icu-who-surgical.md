# Method in Action: B-17 1935 + Pronovost ICU + WHO Surgical

> *Example for the [checklist](../SKILL.md) skill.*

The **Boeing B-17 incident** of October 30, 1935, is the canonical aviation case. The B-17 prototype was being demonstrated to the U.S. Army Air Corps at Wright Field. The crew included Major Ployer Hill, an experienced test pilot. The aircraft took off and immediately began to climb steeply, stalled, and crashed. Two of five aboard died, including Hill.

Investigation: the aircraft was complex enough that pilots needed to release multiple control locks before takeoff. Hill, an experienced pilot of simpler aircraft, had not released the elevator gust lock. The aircraft was technically too complex to fly correctly by memory alone — even for an expert pilot. Boeing's response: institute a written pre-flight checklist that pilots must execute, every flight, regardless of experience. The B-17 went on to fly 1.8 million hours during WWII with negligible pilot-error accident rates in the items covered by the checklist.

The principle: even for experts, even for routine operations, written checklists prevent the omission of obvious-but-easily-forgotten steps.

**Peter Pronovost's ICU central-line checklist** (2001-2006) extended the principle to medicine. Pronovost, a Johns Hopkins anesthesiologist, observed that central-line bloodstream infections (CLABSI) were producing thousands of preventable deaths and tens of billions of dollars in healthcare costs in the U.S. annually. The five steps to prevent CLABSI were well-known and uncontroversial:

1. Wash hands with soap or alcohol
2. Clean the patient's skin with chlorhexidine
3. Drape the patient with sterile barriers
4. Wear sterile gloves, gown, and mask
5. Place a sterile dressing over the catheter site after insertion

Pronovost's intervention was to put these on a checklist that the inserting physician must run, and to give nurses the authority to stop the procedure if any step was skipped. The Michigan Keystone ICU project implemented this across ~100 ICUs from 2003-2005:

> "Within 18 months of implementation, the median rate of central-line bloodstream infections in participating Michigan ICUs dropped from 2.7 infections per 1000 catheter-days to 0. ... Estimated reduction: 1500+ lives saved over the study period, more than 65,000 prevented infections, and over $200 million in saved healthcare costs in Michigan alone."
>
> — Pronovost, P. et al. (2006). NEJM 355(26), p. 2731.

The intervention was almost free in monetary terms (a sheet of paper, a brief training, a cultural shift). The savings were enormous. The result has been called "the single largest QI success in U.S. healthcare history" by some commentators.

**Atul Gawande's WHO Surgical Safety Checklist** (2008-2009) replicated and extended the framework to global surgical practice. The 19-item checklist, developed by WHO and field-tested in 8 hospitals (Seattle, Toronto, London, New Delhi, Amman, Manila, Tanzania, Auckland) covering vastly different resource levels:

> "Implementation of the 19-item checklist was associated with the rate of any complication dropping from 11.0% to 7.0% (P<0.001), a 36% relative reduction. The rate of death dropped from 1.5% to 0.8% (P=0.003), a 47% relative reduction. The reductions were observed across all sites despite the wide differences in baseline complication rates and resource levels."
>
> — Haynes, A. B. et al. (2009). *New England Journal of Medicine*, 360(5), p. 495.

The 19 items include: confirm patient identity, mark surgical site, verify anesthesia readiness, anticipate critical events, confirm antibiotics, introduce all team members by name, etc. None of these are technically advanced; all are something every OR team already knew. The structural intervention: make consistent execution mandatory through checklist discipline.

The framework has been applied in many other domains:

**Investment management.** Mohnish Pabrai's published 80-item investment checklist; Charlie Munger's 20-25 question protocol; many value-investing firms now use formal checklists in due diligence.

**Software deployment.** Pre-deployment checklists at major engineering organizations (Google's Site Reliability Engineering manual, Amazon's pre-launch readiness reviews) prevent recurring outages.

**Construction.** Building codes and inspection checklists prevent structural failures. Modern construction project management treats checklists as load-bearing.

**Personal productivity.** David Allen's *Getting Things Done* (2001) explicitly recommends "trigger lists" — a form of checklist for capturing everything that should be addressed.

**Hiring.** Structured interview rubrics with explicit criteria function as hiring checklists, substantially improving prediction validity over unstructured interviews.

Three operational lessons:

**First, the checklist's power comes from the structural commitment, not the items themselves.** Every team Pronovost worked with already knew the 5 CLABSI steps. The checklist mattered because it made *consistent* execution structural. Without the cultural commitment (nurses authorized to stop procedures, leadership enforcing adherence), the checklist would have been ignored.

**Second, well-designed checklists are short.** 6-10 items is the empirical optimum. Longer lists get truncated or skipped. The discipline of cutting to the critical few is what makes the checklist work.

**Third, checklists supplement judgment, they don't replace it.** Each item still requires the operator to assess the specific situation. A checklist that runs without thinking ("checked, checked, checked") is a checklist that has failed culturally. The discipline is structured attention, not mechanical compliance.
