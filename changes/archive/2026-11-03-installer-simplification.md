# Installer simplification

**Change Style:** Formal

## Intent

Make the installer ship only what a client needs at run time, written fresh from the checkout's disk into a cleared `ndd/` on each run, and add to `.gitignore` only what the project doesn't already own. Tests stay in the checkout. The *NDD Project*, *Testing* and *NDD* trunks also link their child bullets.

## Context

Agreed in discussion [090 Installer review](../archive/2026-10-30-installer-review-discussion.md) (2026-10-30), which holds the reasoning and the shipped set.

## Change Specification

The map targets sit in [095-installer-simplification/](095-installer-simplification/), each settled and stamped:

- `map.md`: *Installer*, the new *Shipped Assets*, *NDD Project*, and *Contents*.
- `testing.map.md`: *Testing* and *Install Check*.
- `ndd.map.md`: *NDD*.

Build brings `install.py` and `tests/install_test.py` into line with them, then promotes the targets into the live maps.

## Log

- Build lock taken; the spec matched the live maps, with no drift from the baselines.
- `install.py` rewritten: an explicit `SHIPPED` list, checked before `ndd/` is cleared and written fresh from disk, and `.gitignore` entries only for what the project doesn't own. `RETIRED_FILES` and the git file list are gone.
- Deviation: on a re-run where `ndd.map.md` hasn't changed, the existing `ndd.prev.map.md` is carried across the clear rather than lost, as before. The spec says nothing either way.
- `tests/install_test.py` rewritten against *Install Check*; it holds the shipped assets separately from the installer's list, and has a new case for an existing entry file. It passes, and so does `fingerprint_test.py`.
- Promoted *Installer*, *Shipped Assets*, *NDD Project* and *Contents* into `map.md`, *Testing* and *Install Check* into `testing.map.md`, and *NDD* into `ndd.map.md`. None of them is due, and the tests pass again after promotion.
- Version: a minor bump, agreed late (after the build rather than at its start). The change claims `2.9.0-dev`, and this hand-back for testing is `2.9.0-dev.1`.
- Re-agreed *Installer* at Conclude so the spec covers the backup on an unchanged re-run ("the last installed map that differs from the new one"). Re-stamped in both the live map and the copy; the earlier deviation line no longer applies.

## Conclude

Verified: the live maps match the Change Specification, and every stamp holds. At Conclude, *Installer* was re-agreed so that it covers keeping the backup on an unchanged re-run. The minor bump to `2.9.0-dev` was agreed after the build rather than at its start. Aside 100 was parked during planning.
