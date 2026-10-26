# Map simplification

**Change Style:** Formal

## Intent

Simplify and harmonise the method map so each node carries less, says it once and sits within its size bound, and the agent rules follow.

## Change Specification

Targets: whole-map copy [`070-map-simplification/ndd.map.md`](070-map-simplification/ndd.map.md) and [`070-map-simplification/AGENT-RULES.md`](070-map-simplification/AGENT-RULES.md), and project-map copy [`070-map-simplification/map.md`](070-map-simplification/map.md). Review findings in [`070-map-simplification/findings.md`](070-map-simplification/findings.md).

## Context

Additive changes had left nodes over their size bound, prose overlapping, and rules rendering everything their nodes ask for at once; Archiving and the Startup Scan were the known hotspots. Raised during change 020 (2026-10-16); Startup Scan added during change 090 (2026-10-18).

The Change Specification is drafted finding by finding from the full Map Review in [`findings.md`](070-map-simplification/findings.md), each edit settled and stamped in the target copies. Steps:

1. Archiving cluster: one owner per step, Archiving a list of links. *Done 2026-10-20.*
2. Startup Scan report items: one owner per item. *Done 2026-10-22.* Along the way, pause notes became dated entries reviewed at Archiving; Startup Scan was split into picture and *Detail*, its interrupted-build text moving to Build Lock; Rule Form split into Rule Layout and Rule Phrasing; rule headings name their source node, unnumbered; rules with an occasional trigger point to their node (nine converted), the rest stay inline.
3. Preparation by style: style nodes and the Change Style table own it. *Done 2026-10-22.*
4. Wrong style returns to planning: Change Style owns it. *Done 2026-10-22.*
5. Stamped nodes exempt from size flags: Node Sizing owns it. *Done 2026-10-22.*
6. Tidy after a hand-back: Tidy owns its trigger. *Done 2026-10-22.*
7. Approval writes a stamp: Sign-off owns it, Engagement Rule links. *Done 2026-10-22.*
8. Cap counting and adjudication: new Caps node owns it. *Done 2026-10-22.*
9. Held and Context describing each other: Held owns its outcomes, Context and Conclude link. *Done 2026-10-22.* Parked change 100 (Held release language) folded in and closed: Held and Conclude now read as resolving each item, and the Held rule points to its node.
10. A change defined in two nodes: Change Lifecycle owns it. *Done 2026-10-22.*
11. Review moments stated in several places: Map Review's table owns its moments; Maintenance's table kept as the overview. *Done 2026-10-22.* Parked change 050 (Release map reality check) closed: its premise was mistaken, since Rendering, in the full scope, compares the map against the code.
12. Approver's handle announcement: at the first stamp and on any change. *Done 2026-10-22.*
13. Corrections, batched. *Done 2026-10-26.* Navigation Links and Thought Management were tightened under the bound along the way.
14. Unstamped nodes over the size bound. *Done 2026-10-26.* Bootstrapping, Map Structure, Orient Then Focus and Change Lifecycle were tightened under the bound and stamped; Thought Management was done in 13.
15. Rendering check. *Done 2026-10-26.* No new disagreements; 080 stays parked.
16. Re-check the inline agent rules against their nodes. *Done 2026-10-26.* Seven rules re-rendered; the diff-fence detail left to 040. Along the way the Engagement Rule now expects the agent to review and comment on user edits in one pass, and Drafts hands off to it.
17. Held folds into Unresolved, which is empty before Build; the Log carries Build's open items, resolved before Conclude. *In progress.* Raised by the user (2026-10-26): agents had been carrying Held into Build because its only deadline was Conclude.

## Held

- Reword "walk" across the map (about 10 places) in favour of plainer verbs such as "review".
- *Formatting*: when a link holds a step's detail, the wording says so, as in "as Pause Keyword directs".
- Map Review or Tidy: check each node keeps the picture in its body and implementation precision in *Detail*.
- "Hand back" carries three senses (build for testing, build to planning, user after editing a draft); settle or replace them.
