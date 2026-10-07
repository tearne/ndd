# Agent rules rendering review

## Intent

Improve the rendering of the method map into AGENT-RULES.md and the agent's handling of rules in user interaction, and add map-level guidance on how rendering should be done. Rendering should keep AGENT-RULES in step with the map at user-facing moments without duplicating what belongs on the map side.

## Context

Concrete gaps seen so far:

- Agents cite rules by number in user conversation; should be heading name. (The floating rules-by-number fix.)
- Agents cite map nodes by yaml id in output; should be heading name, since the id is an agent-side fingerprint construct and the heading is user-navigable. (From the folded aside previously parked as 090.)
- Orientation preamble doesn't distinguish *reasoning* reads from *flow* reads; flow reads should happen at lifecycle hinges (Discussion → change, between plan parts, Build → Conclude, Conclude → archive). (From the folded gap previously parked as 060, noticed when the agent skipped Discussion Conclude 2026-10-06.)
- Rule 16 Archiving omits *Formal Conclude*'s disposable-whole-map-copy clause.
- Rule 13 Follow-the-Plan paraphrases *Formal Build*'s current wording rather than tracking the source.
- No rule renders *Formal Build*'s closing-act map promotion step.
- Per-node approval rules are buried in map prose rather than surfaced where the user needs them.

Design decisions deferred to the preparation section: what AGENT-RULES carries vs what stays map-side; whether rendering is hand-maintained or mechanically derivable; when render drift blocks vs parks.


## Change Specification

Target is a whole-map copy at [`080-agent-rules-rendering-review/ndd.map.md`](080-agent-rules-rendering-review/ndd.map.md), starting as a verbatim copy of `ndd.map.md`. Proposed node edits are made directly in that copy and walked per-node under the Engagement Rule. Approval stamps land in the copy's per-node yaml blocks and transfer to the live map at the closing act of Build.

Walk order not yet set — proposing after check-in of the baseline.
