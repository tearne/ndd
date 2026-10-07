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

Targets are whole-map copies of both NDD maps:

- [`080-agent-rules-rendering-review/ndd.map.md`](080-agent-rules-rendering-review/ndd.map.md) — baseline of `ndd.map.md`.
- [`080-agent-rules-rendering-review/map.md`](080-agent-rules-rendering-review/map.md) — baseline of `map.md`.

Proposed node edits are made directly in the copies and walked per-node under the Engagement Rule. Approval stamps land in each copy's per-node yaml blocks and transfer to the live maps at the closing act of Build.

Walk order:

1. [`map.md`] *Agent Rules* — extend to cover drift-at-non-touched-surfaces parking and the render-vs-map division.
2. [`map.md`] *Rule Form* — add rule-citation-by-heading-name convention.
3. [`ndd.map.md`] *Node Identity* — user-facing agent output uses the heading name; id stays agent-side.
4. [`ndd.map.md`] New node *Lifecycle Flow Reads* under *Change Lifecycle* — flow reads at lifecycle hinges, distinct from reasoning reads.
5. [`ndd.map.md`] *Engagement Rule* or *Approval* (home resolved during walk) — surface per-node approval discipline where the agent will find it.
