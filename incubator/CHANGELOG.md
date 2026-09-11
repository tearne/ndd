# Changelog

Notable changes to the NDD method. The current version is the topmost heading below; re-running the installer refreshes an install to the latest. Newest first.

## Unreleased

- Testing gains an Install Check: `tests/install_test.py` installs into a scratch project and asserts refusal of the checkout itself, the shipped set, pointer entry files, executable scripts, resolving links, and the upgrade path. Release Steps is now bump, then run every test.
- Testing: the project map gains a Testing branch, `testing.map.md`, whose Fingerprint Check pins the Fingerprint rule with a reference test and fixtures under `tests/`. A Sign-off helper, `util/fingerprint.py`, prints node fingerprints and lists what is due for a person; the new Fingerprint Helper node specifies it. Release Steps now run every test under Testing.
- The installer ships every file git tracks except `CLAUDE.md` and `AGENTS.md`, keeping scripts executable, so a new file ships once it is committed and there is no list to maintain.
- Thought Management: a stray thought is answered, taken as a digression, held or parked, and every message during a set ends with a status line such as `map edits 3 of 7 > aside`.
- The installer ships the sources: they are copied as they are, with no build step. A client's `ndd/` now holds NDD's project map above the method branch.
- Maintenance simplified to three reviews: a Map Review offered after an archive and, in full scope, before a release; a Backlog Review at the Startup Scan; and Sign-off. Tidy runs on hand-back or before an archive and reports every fix. The named checks remain askable by name.
- Map files: a map may span several `.map.md` files, each a branch hanging from a node in `map.md`; the parent link reads `[↑ Parent]`, each file has a Contents node holding a linked overview, and META is retired. The method ships as `ndd/ndd.map.md`, backed up on upgrade as `ndd.prev.map.md`.
- Stakeholder sign-off: a node's scaffolding block can carry per-person approval stamps, each a timestamp and a fingerprint of the text approved; the Sign-off check lists what is due for a named person by comparing fingerprints. Maps without stamps are unaffected.
- Map Maintenance becomes a top-level Maintenance box: six named checks (Tidy, Shape, Prose, Consistency, Rendering, Backlog) in a table with triggers, offered after archival, at the Startup Scan, or before release.
- Agent rules rendered from the map replace `BOOTSTRAP.md`; the method ships from a checked-in `dist/` via `install.py`, formerly `opt-in.py`.

## 1.0.0 — 2026-08-26

First release under the NDD name — successor to COD (Comprehension-Oriented Design). Marks the method's move from incubation to a standalone, installable form.
