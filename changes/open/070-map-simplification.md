# Map simplification

**Change Style:** Formal

## Intent

Additive changes have left the method map accumulating weight: nodes over their size bound, overlapping prose, and rules that render everything their nodes ask for at once. Simplify and harmonise across the map, driven by a full Map Review, so each node carries less and says it once, and the rules follow. Known hotspots are Archiving and the Startup Scan, whose rules (rules 19 and 1) read as too complex and whose nodes keep gaining items.

Raised during change 020 (2026-10-16).

Startup Scan added during change 090 (2026-10-18).

## Change Specification

Targets: whole-map copy [`070-map-simplification/ndd.map.md`](070-map-simplification/ndd.map.md) and [`070-map-simplification/AGENT-RULES.md`](070-map-simplification/AGENT-RULES.md), and project-map copy [`070-map-simplification/map.md`](070-map-simplification/map.md). Review findings in [`070-map-simplification/findings.md`](070-map-simplification/findings.md).

## Context

The Change Specification is drafted finding by finding from the full Map Review in [`findings.md`](070-map-simplification/findings.md), each edit settled and stamped in the target copies. Steps:

1. Archiving cluster: one owner per step, Archiving a list of links. *Done 2026-10-20.*
2. Startup Scan report items: one owner per item. *Done 2026-10-22.* Along the way, pause notes became dated entries reviewed at Archiving; Startup Scan was split into picture and *Detail*, its interrupted-build text moving to Build Lock; Rule Form split into Rule Layout and Rule Phrasing; rule headings name their source node, unnumbered; rules with an occasional trigger point to their node (nine converted), the rest stay inline.
3. Preparation by style: style nodes and the Change Style table own it. *Done 2026-10-22.*
4. Wrong style returns to planning. *In progress.*
5. Stamped nodes exempt from size flags.
6. Tidy after a hand-back.
7. Approval writes a stamp.
8. Cap counting and adjudication.
9. Held and Context describing each other.
10. A change defined in two nodes.
11. Review moments stated in several places.
12. Approver's handle announcement.
13. Corrections, batched.
14. Unstamped nodes over the size bound.
15. Rendering check.
16. Re-check the inline agent rules against their nodes.

## Held

- Reword "walk" across the map (about 10 places) in favour of plainer verbs such as "review".
- *Formatting*: when a link holds a step's detail, the wording says so, as in "as Pause Keyword directs".
- Map Review or Tidy: check each node keeps the picture in its body and implementation precision in *Detail*.
- "Hand back" carries three senses (build for testing, build to planning, user after editing a draft); settle or replace them.
