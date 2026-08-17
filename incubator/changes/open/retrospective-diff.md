# Retrospective diff

## Intent

An optional aid on the approval axis: show a stakeholder "what changed in this node since *your* last approval." It is *derived, never stored* — at display time, resolve their approval timestamp to the commit that last touched the node at or before then, fetch that version, and diff it against current. Distinct from any global proposal diff, because each stakeholder's baseline differs.

Kept separate from `approval-mechanics` because it is fundamentally a **display-time git operation with a real tooling component**, sitting between the approval stamps it consumes and the viewer that would render it. Git is load-bearing here — and only here on the approval axis — so it degrades gracefully: with no git there is no retrospective diff, while stamps, drift, and the due-queue all still work.

Decomposition item 4 (keystone sequence in `enhancement-discussion.md`). Depends on `approval-mechanics`; relates to `tooling-development` for the rendering surface.
