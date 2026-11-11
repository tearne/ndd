# Map viewer hardening

**Change Style:** Vibe

## Intent

The map viewer should render markdown faithfully, including nested and numbered lists, heading levels and blockquotes, settling whether a third-party renderer earns its place; answer an approval diff quickly on a long history; and have automated tests of its pages, built on the demo map.

## Context

Known limits from 330's Conclude (2026-11-10). A renderer library would cost the script's run-anywhere quality, since its first run on a host needs network access or a uv cache.

## Bounds

The viewer should stay one read-only script, listening on 127.0.0.1 only. Adopting a third-party renderer is the user's call. Tests should run offline. Only *Map Viewer* should change in the map.

## Log

- Build Lock taken; version claimed as 3.5.2-dev (patch), viewer VERSION to 0.2.0.
- Renderer: hand-rolled kept (user left it to judgement; a library would break offline tests). Nested and numbered lists, h2–h6, blockquotes and GitHub alerts, fences closing on as many backticks. A paragraph that is only a link now renders rather than being dropped as navigation.
- Approval diff: every version read through one git cat-file --batch, each parsed once; 300-commit history 23 s → 1.2 s, output identical to before. quote_shell replaced by shlex.quote, as POS asks; VERSION 0.2.0.
- Tests: `tests/map_viewer_test.py` serves the demo map in-process on a free port and checks each page against what its demo node shows; the demo's *Rendering* node gained the new markdown. Passes, fails 6 rendering checks against the old viewer; `fingerprint_test.py` still passes. Demo VERSION 0.2.0.
- Open: *Testing* convention gives each test its own node, but Bounds allows only *Map Viewer* to change in the map.
- Bounds widened by the user: the *Testing* branch may change for the new test. Open item resolved.
- Layout, at the user's request: `tools/viewer_demo.py` moved to `tests/map_viewer/`, beside the test now there too; the viewer stays in `tools/`. Both tests pass.
- *Map Viewer Check* written to `testing.map.md`, stamped 1b56d918.
- *Testing* gained the *Map Viewer Check* link and entry, stamped c3ffa732.
- *Contents* gained the *Map Viewer Check* entry.
- *Map Viewer* names the hand-rolled renderer, the demo's new path and *Map Viewer Check*; stamped a2b904ee, 832 characters, overrun accepted by the user.
- *Map Viewer Check*: "no network" → "no internet access"; restamped 5a5b687f.

## Conclude

Bounds widened to the *Testing* branch for the new test. At the user's request `viewer_demo.py` moved to `tests/map_viewer/`, beside the test. The renderer stayed hand-rolled. Aside opened: 130 *Requirement voice beyond Intent*.
