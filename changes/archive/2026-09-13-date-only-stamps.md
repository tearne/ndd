# Date-only stamps

**Cadence:** Wander

## Intent

A stamp's `at` becomes an ISO 8601 date, no time or offset. The hash identifies the text approved; the date only says when. Existing stamps in the map and the test fixtures are shortened to match.

### Context

- Raised 2026-09-13 after the first stamps under change 050 made the scaffolding block hard to glance at. Change 320's retrospective diff finds a version by hash, so the time was never load-bearing.

## Log

- 2026-09-13: Shortening every stamp in the test fixtures broke the fingerprint test: the Full Sections fixture node carries an example stamp inside its prose, which is fingerprinted content. That one example line restored in both fixtures; the test passes. The map's own in-prose example in Approval Stamp was changed deliberately as part of the node edit, so its fingerprint moved as expected.
- 2026-09-13: On the user's call the fixture example was shortened after all; Full Sections' pinned hash moved to 188f743f in the test, both fixtures and the Fingerprint Check table.

## Conclude

Completed. The Fingerprint Check table changed with the fixture, so the testing map was touched as well as the method map.
