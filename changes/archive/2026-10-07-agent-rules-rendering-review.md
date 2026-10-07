# Agent rules rendering review

## Intent

Improve the rendering of the method map into AGENT-RULES.md and the agent's handling of rules in user interaction.

## Context

Concrete gaps seen so far:

- Agents cite rules by number in user conversation; should be heading name. (The floating rules-by-number fix.)
- Agents cite map nodes by yaml id in output; should be heading name, since the id is an agent-side fingerprint construct and the heading is user-navigable. (From the folded aside previously parked as 090.)
- Orientation preamble doesn't distinguish *reasoning* reads from *flow* reads; flow reads should happen at lifecycle hinges (Discussion → change, between plan parts, Build → Conclude, Conclude → archive). (From the folded gap previously parked as 060, noticed when the agent skipped Discussion Conclude 2026-10-06.)
- Rule 16 Archiving omits *Formal Conclude*'s disposable-whole-map-copy clause.
- Rule 13 Follow-the-Plan paraphrases *Formal Build*'s current wording rather than tracking the source.
- No rule renders *Formal Build*'s closing-act map promotion step.

Design decisions deferred to the preparation section: what AGENT-RULES carries vs what stays map-side; whether rendering is hand-maintained or mechanically derivable; when render drift blocks vs parks.


## Change Specification

Targets are whole-map copies of both NDD maps:

- [`080-agent-rules-rendering-review/ndd.map.md`](080-agent-rules-rendering-review/ndd.map.md) — baseline of `ndd.map.md`.
- [`080-agent-rules-rendering-review/map.md`](080-agent-rules-rendering-review/map.md) — baseline of `map.md`.

Proposed node edits are made directly in the copies and walked per-node under the Engagement Rule. Approval stamps land in each copy's per-node yaml blocks and transfer to the live maps at the closing act of Build.

Walk order:

1. [`map.md`] *Agent Rules* — restructure body/Detail; carry references-to-source-node principle; drift-on-sight clause. **Settled, stamped.**
2. [`map.md`] *Rule Form* — lead bullet 2 with "Each rule is trigger-centred:" to lift the trigger-centred design intent. **Settled, stamped.**
3. [`ndd.map.md`] *Node Identity* — agent output names the heading, not the id. **Settled, stamped.**
4. [`ndd.map.md`] New *Lifecycle Flow Reads* under *Change Lifecycle*, as first child — flow reads at lifecycle hinges, distinct from reasoning reads. **Settled, stamped.**
5. ~~*Engagement Rule* or *Approval* — surface per-node approval discipline~~ **Dropped on walk-time scrutiny**: current coverage in *Engagement Rule* and AGENT-RULES Rule 6 is adequate; the audit "buried in prose" observation didn't survive re-reading.


## Implementation Plan

The AGENT-RULES.md render is treated as a planning artefact so the user reviews before committing to Build. Baseline copy at [`080-agent-rules-rendering-review/AGENT-RULES.md`](080-agent-rules-rendering-review/AGENT-RULES.md), starting as a verbatim copy of `AGENT-RULES.md`. Proposed render edits are made in that copy and walked under the Engagement Rule's correction-aware form (AGENT-RULES.md is not a map, so stamps don't apply; approval is per edit).

Render edits to walk:

1. Rule 13 (Follow the Plan) — rewrite to track *Formal Build*'s current wording for Build-time re-agreement under Lock.
2. Rule 16 (Archiving) — extend to render *Formal Conclude*'s disposable-whole-map-copy clause.
3. New rule — render *Formal Build*'s closing-act map promotion step.
4. New rule — render *Lifecycle Flow Reads* (flow reads at lifecycle hinges).
5. Orientation preamble — update to reflect *Agent Rules*' route-into-map framing (the rendering is a route, not a destination; references name source nodes).
6. Rule 12 Caps or preamble — surface the heading-name output convention from *Node Identity* (if a rule-shaped placement fits).
7. Any rule-citation audit — ensure existing rules cite their sources by node name, consistent with the new convention.

Walk order: 1 → 7 in sequence; each surfaced and approved before the next.


## Conclude

Deltas:

- *Rule Division* drafted and dropped; redundant with *Rule Selection*.
- *Agent Rules* body/Detail restructure under cap pressure.
- *Rule Form* bullet 2 lifted with "Each rule is trigger-centred:" lead.
- *Lifecycle Flow Reads* reordered to first child of *Change Lifecycle*.
- *Formal Build* re-opened mid-walk for per-node promotion conditional.
- Walk shrunk 7→5; "per-node approval surfacing" dropped on scrutiny.
- Implementation Plan added for AGENT-RULES render review.
- 7 render edits: preamble, 2 new rules, 2 reworded, 1 citation audit.
