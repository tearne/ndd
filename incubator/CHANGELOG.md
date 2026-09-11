# Changelog

Notable changes to the NDD method. The current version is the topmost heading below; re-running the installer refreshes an install to the latest. Newest first.

## Unreleased

- Thought Management: a stray thought is answered, taken as a digression, held or parked, and every message during a set ends with a status line such as `map edits 3 of 7 > aside`.
- The installer ships the sources: `map.md`, `ndd.map.md`, `CHANGELOG.md`, `AGENT-RULES.md` and `standards/` are copied as they are, with no build step. A client's `ndd/` now holds NDD's project map above the method branch.
- Maintenance simplified to three reviews: a Map Review offered after an archive and, in full scope, before a release; a Backlog Review at the Startup Scan; and Sign-off. Tidy runs on hand-back or before an archive and reports every fix. The named checks remain askable by name.
- Map files: a map may span several `.map.md` files, each a branch hanging from a node in `map.md`; the parent link reads `[↑ Parent]`, each file has a Contents node holding a linked overview, and META is retired. The method ships as `ndd/ndd.map.md`, backed up on upgrade as `ndd.prev.map.md`.
- Stakeholder sign-off: a node's scaffolding block can carry per-person approval stamps, each a timestamp and a fingerprint of the text approved; the Sign-off check lists what is due for a named person by comparing fingerprints. Maps without stamps are unaffected.
- Map Maintenance becomes a top-level Maintenance box: six named checks (Tidy, Shape, Prose, Consistency, Rendering, Backlog) in a table with triggers, offered after archival, at the Startup Scan, or before release.
- Agent rules rendered from the map replace `BOOTSTRAP.md`; the method ships from a checked-in `dist/` via `install.py`, formerly `opt-in.py`.

## 1.0.0 — 2026-08-26

First release under the NDD name — successor to COD (Comprehension-Oriented Design). Marks the method's move from incubation to a standalone, installable form.
