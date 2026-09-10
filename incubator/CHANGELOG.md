# Changelog

Notable changes to the NDD method. The current version is the topmost heading below; re-running the installer refreshes an install to the latest. Newest first.

## Unreleased

- Stakeholder sign-off: a node's scaffolding block can carry per-person approval stamps, each a timestamp and a fingerprint of the text approved; the Sign-off check lists what is due for a named person by comparing fingerprints. Maps without stamps are unaffected.
- Map Maintenance becomes a top-level Maintenance box: six named checks (Tidy, Shape, Prose, Consistency, Rendering, Backlog) in a table with triggers, offered after archival, at the Startup Scan, or before release.
- Agent rules rendered from the map replace `BOOTSTRAP.md`; the method ships from a checked-in `dist/` via `install.py`, formerly `opt-in.py`.

## 1.0.0 — 2026-08-26

First release under the NDD name — successor to COD (Comprehension-Oriented Design). Marks the method's move from incubation to a standalone, installable form.
