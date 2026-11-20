# Target nodes file

**Change Style:** Formal \
**Version:** 3.9.1-dev

## Intent

*Change Specification* should have every map target written as a whole node in the companion folder, offering a `targets.md` of them beside the sub-map and whole-map copy.

## Context

Raised 2026-11-20 during 330, which trials it: its targets were first written as body text without stamps, then as full nodes inside the change, which interrupted the change's flow, then moved to `archive/2026-11-20-stamp-key-rename/targets.md`, where `fingerprint.py` checks their stamps. 330 concluded the same day: review of whole nodes was easier than of described changes, each target was promoted by replacing its live node whole, and one miscount surfaced only at Tidy, as the example block in a node had been left out of its count. Likely touches *Change Specification* and perhaps *Companion Folder*. For a few nodes spread across maps, a copy is heavy and diffs against it add little.

## Change Specification

Planned edits, each target node written whole and stamped on approval, in this order, in `targets.md` (dropped at Archiving, the nodes being live as approved); promoted in Build:

1. *Change Specification* (method map): map targets always whole nodes in the companion folder, on a copy or a `targets.md`.
2. *Companion Folder* (method map): its contents name the drafted nodes rather than the map copy.

## Progress

- 2026-11-20: Intent approved; Formal. 1 drafted (~831, flagged; cut of "Once built the live map must describe the completed result." proposed, −60, not yet taken), written to `targets.md` between draft markers for the user's review.
- Cut taken in the draft at the user's request, ~771.
- Draft recast with the two options as bullets, at the user's request, ~770.
- 1 approved as edited by the user, with "later diffs against it show only the planned edits"; ~751, stamped e9439d8b.
- 2 approved: "the nodes a Formal change drafts as its specification", replacing a chain of ors; ~490, stamped 49a2a34c. Change Specification complete; next the Intent trim, then plan approval.
- Intent trimmed, ~110, approved; its reason moved to Context. (The approved Intent had read "for a change touches", a slip from applying it.)
- 1 reopened before plan approval: map targets are always whole nodes in the companion folder, inline kept for non-map assets only; stamp removed, draft written to `targets.md` for the user's review.
- 1 re-approved: whole map nodes in the companion folder, non-map assets moved to the last paragraph; ~708, stamped 0ab47ae9.
- Intent widened to match the reopened edit 1, ~165, approved.
- Plan approved 2026-11-20.

## Log

- 2026-11-20, Build Lock taken. Change Specification reconciled: both live nodes unchanged since the targets were drafted today.
- Version 3.9.1-dev claimed, a patch bump.
- Promoted into the method map, per node, no drift: *Change Specification*, *Companion Folder*.
- No other node, nor *Agent rules*, repeats the old copy wording. Fingerprint and install tests pass.

## Conclude

Completed.
