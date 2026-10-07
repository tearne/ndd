# Formal Specification pacing

## Status and purpose

Discussion to resolve a tension between *Change Specification* and the *Engagement Rule* when a Formal change's output is map content, or any structured content.

## The tension

Formal Change Specification is approved as one plan part. When the change's output is map content, a Specification tends to enumerate the nodes to be built — names, roles, build order. Approving the Specification approves the architectural shape of all those nodes in one dialogue.

The *Engagement Rule* exists to pace that: comprehension built one node at a time. Even if each node's text is drafted and surfaced one-by-one at Build, the shape was already settled in bulk.

Generalises beyond maps: any Formal change whose output is structured content likely has the same shape — the Specification pre-commits the structure the Build then types out.

## Working position: Specification is map content

NDD's premise is that the map is the specification. A Change Specification expressed as free-form prose is a parallel specification track — the thing NDD exists against. The working position:

- A Formal Change Specification *is* a slice of the map — either existing nodes it is reconciled against, or new or modified nodes drafted inside the change file, pending promotion to the real map.
- Other assets a Formal change produces or touches — configuration files, test data, code — can exist alongside, but the map slice is the spec work. The map is what *Formal Build* reconciles against.
- Because the Specification is map content, the *Engagement Rule* applies to its drafting by default: Specification becomes a one-at-a-time sequence of per-node shape settlements.
- Approval stamps on held Specification nodes carry through to the real map at promotion — stakeholder sign-off earned during planning is preserved, not reset. Stamps are a map device, and held nodes carry their stamps with them when they land.
- Map promotion is the closing act of *Formal Build*: code and other assets land in their project locations during Build; at Build's close the map is updated to match what actually landed, before Conclude. Conclude writes the delta from the plan but does not write the map. This gives any Build-time divergence a chance to surface in the map before archival, and keeps the *Sync Rule* clean — the map updates when reality is in place, not before and not after.
- The earlier candidate directions (narrower Specification, new map-seeding style, bulk-and-accept, Engagement-Rule pacing as a bolt-on) are superseded: they treated map-content as a special case within a broader Specification concept, where this position makes map-content *the* Specification concept.

## Open questions

- When a Formal change genuinely cannot be expressed as map work, is that a signal the change is wrongly scoped, or that NDD has a real gap? If NDD can answer "wrongly scoped" every time, the taxonomy tightens; if not, that is where NDD learns something about itself.
- Shape of the *Plan* node under Formal: the Specification plan-part is no longer a single approval moment. Does *Plan* still read as four discrete parts, or is Formal's Specification part now a sub-phase?
- How is a per-node-paced Specification counted and capped against the existing *Change Specification* sizing conventions?
- Does *Formal Build* still read coherently when the Specification was negotiated across many turns? The drift-check has a well-defined target (the agreed map slice), but the comprehension story is now spread across both Specification and Build.
- Does the "Specification is map content" principle bleed into *Exploratory*'s Focus and *Vibe*'s Bounds where they describe map regions, or is it a Formal-only commitment?

## Conclude

Working position: Formal's *Change Specification* is map content, drafted per-node under the *Engagement Rule* with stamps carried through; non-map assets land in place during Build; the map updates to match at Build's close, before Conclude. NDD assumption sharpened: Specifications are expressible as maps. Promoted [070-formal-specification-as-map-content](../open/070-formal-specification-as-map-content.md). Dropped: earlier candidate directions, the 'map-work gap' question (covered by the assumption), and 'bleed into other styles'.
