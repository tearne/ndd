# Retrospective diff

## Intent

An optional aid on the approval axis: show a stakeholder "what changed in this node since *your* last approval." It is *derived, never stored* — at display time, resolve their approval timestamp to the commit that last touched the node at or before then, fetch that version, and diff it against current. Distinct from any global proposal diff, because each stakeholder's baseline differs.

Kept separate from `approval-mechanics` because it is fundamentally a **display-time git operation with a real tooling component**, sitting between the approval stamps it consumes and the viewer that would render it. Git is load-bearing here — and only here on the approval axis — so it degrades gracefully: with no git there is no retrospective diff, while stamps, drift, and the due-queue all still work.

Decomposition item 4 of the keystone sequence in the retired `enhancement-discussion.md`, kept in git history. Depends on approval mechanics (built, archived 2026-09-10); relates to change 330 (tooling development) for the rendering surface. Renumbered from 90 on 2026-09-10 to sit with the sign-off theme at the end of the backlog.
