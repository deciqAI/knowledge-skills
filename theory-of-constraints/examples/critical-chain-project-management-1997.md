# Method in Action: Critical Chain Project Management (1997 → 2000s)

> *Example for the [theory-of-constraints](../SKILL.md) skill.*

Thirteen years after *The Goal* applied the Five Focusing Steps to a factory floor, Goldratt applied the same discipline to a domain with no machines at all: project pipelines. *Critical Chain* (1997) — again written as a novel — follows an executive MBA class whose students bring their employers' real project problems into the classroom. The central case is Genemodem, a modem manufacturer whose product life cycles are collapsing: by the time a development project ships, competitors have already moved.

The presenting symptoms are the project-world version of the busy-but-losing plant. Every task has a deadline and a padded estimate, every engineer is fully occupied — usually on several tasks at once — and yet every project is late. Adding engineers and starting projects earlier has not helped, because none of it touches the constraint.

**Step 1 — Identify.** In a single project, the constraint is not a machine but the *critical chain*: the longest sequence of tasks accounting for both task dependency **and** resource dependency (two tasks sharing the same engineer cannot run in parallel, even if the network diagram says they can — a dependency classic PERT/CPM ignores). In a multi-project organization, the constraint is typically one heavily shared, strategically loaded resource through which most projects must pass. Evidence of the constraint is the same as on a factory floor: work queues up in front of it while downstream tasks sit idle waiting.

**Step 2 — Exploit.** Goldratt's diagnosis of why projects are late despite generous estimates: safety is embedded in every task, then systematically wasted. He names the mechanisms — the *student syndrome* (safety in an estimate invites starting the task at the last moment, so the safety is consumed before work begins), *Parkinson's Law* (work expands to fill the time allotted; early finishes are rarely reported), and *bad multitasking* (splitting one person across several open tasks stretches every one of them). Exploiting the constraint costs nothing: cut per-task estimates to aggressive durations with no individual padding, forbid multitasking on critical-chain tasks, and adopt a relay-runner work ethic — when a critical-chain task arrives, drop everything, run it flat out, hand it off immediately.

**Step 3 — Subordinate.** The safety removed from individual tasks is not discarded; it is pooled and repositioned to protect the constraint. A single *project buffer* is placed at the end of the critical chain, and *feeding buffers* are placed wherever a non-critical path merges into it — so variability on non-constraint paths cannot starve the chain. In multi-project environments, subordination means staggering project releases to the pace of the constraint resource (the drum) instead of launching every approved project immediately. Task-level due dates and per-task efficiency tracking are retired; management attention shifts to a single signal, buffer consumption, which flags trouble while there is still time to act.

**Step 4 — Elevate.** Only after exploitation and subordination, if the strategic resource is still binding, add capacity there — hire into that skill, offload its non-critical work — the highest-ROI investment in the pipeline. Adding people anywhere else adds cost and work-in-process, not throughput.

**Step 5 — Repeat.** Once releases are staggered and buffers manage variability, the constraint moves — often to a different resource, or out of engineering entirely into decision-making or market demand. The Five Focusing Steps are re-run.

Buffer management is what makes the discipline self-correcting: buffer consumption compared against chain completion tells management, on one chart, whether the pooled safety is being burned faster than the work is progressing. Green means leave the team alone; deep incursion means intervene at the specific task consuming the buffer. This replaces the futile practice of chasing every task-level slip — most of which the buffers would have absorbed anyway.

The method became known as Critical Chain Project Management (CCPM). Leach (2004) gives the standard engineering treatment, and the practitioner chapters in Cox & Schleier's *Theory of Constraints Handbook* (2010) document implementations across defense, aerospace, R&D, and construction organizations, with the recurring reported pattern of shorter project durations and more projects completed with the same resources. The deeper point of the case: the Five Focusing Steps transferred intact from machines to knowledge work because the constraint logic never depended on machinery — only on dependency plus variability.

The mapped steps:
1. Identify: the critical chain (longest resource-and-task-dependent path); in multi-project settings, the shared strategic resource where work queues
2. Exploit: strip per-task safety padding; kill student syndrome, Parkinson's Law, and bad multitasking; relay-runner execution on the chain
3. Subordinate: pool safety into project and feeding buffers; stagger project releases to the constraint's pace; retire task-level due dates for buffer management
4. Elevate: add capacity at the strategic resource only, after cheaper steps are exhausted
5. Repeat: the constraint migrates — to another resource or to the market — so the analysis is re-run

Primary source: Goldratt, E. M. (1997). *Critical Chain.* North River Press. ISBN 978-0884271536. See also Leach, L. P. (2004). *Critical Chain Project Management* (2nd ed.). Artech House.
