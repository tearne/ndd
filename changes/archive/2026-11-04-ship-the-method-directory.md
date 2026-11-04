# Ship the method directory

**Change Style:** Formal

## Intent

Stop shipping the main map, `map.md`, and the tests map, `testing.map.md`, which a client doesn't need, and gather what does ship into a `method/` directory. In a client's `ndd/`, `ndd.map.md` stands as its own root.

## Context

Raised during 105 (2026-11-03). The shipped `testing.map.md` described tests that 095 had stopped shipping, and the shipped `map.md` carries maintainer-only nodes such as *Release Steps*. Both ship today only because `ndd.map.md`'s root links up to *NDD Project* in `map.md`, the agent rules cite *Distribution* there, and `map.md` links into `testing.map.md`.

## Change Specification

Target copies in `115-ship-the-method-directory/`, laid out as the checkout will be:

- `map.md`: *NDD Project*, *Distribution*, *Installer*, *Shipped Assets* and *Agent Rules*; links into `method/`.
- `method/ndd.map.md`: new *Installation*; *NDD*, *Map Files*, *Fingerprint*, *Fingerprint Helper* and *Standards*.
- `method/AGENT-RULES.md`: *Orientation* bullets cite *Installation*.
- `testing.map.md`: *Install Check*; links into `method/`.
- `README.md`: method links into `method/`; `map.md` named as the source repository's map.

## Implementation Plan

- Move first, with plain `mv` so git sees renames: `AGENT-RULES.md`, `ndd.map.md`, `util/` and `standards/` into `method/`. Root `CLAUDE.md` and `AGENTS.md` then point at `method/AGENT-RULES.md`.
- `install.py` ships `method/` whole plus the three root files, and points entry files at `ndd/method/AGENT-RULES.md`. A first upgrade from the flat layout compares against the old `ndd/ndd.map.md`, so `ndd.prev.map.md` is still kept.
- The tests follow before anything promotes: `install_test.py`'s shipped list, pointers and backup paths, with its link check failing on a shipped link that leaves what ships; `fingerprint_test.py`'s path to the helper.
- *Orientation* bullets 1 and 2 are A/B tested against their old wording, as *Rule Testing* directs, before `method/AGENT-RULES.md` lands.
- The spec copies promote last, as *Formal Build* directs.

## Log

- Build Lock taken 2026-11-04.
- Claims 3.0.0-dev: client paths move from `ndd/` to `ndd/method/`.
- Moved `AGENT-RULES.md`, `ndd.map.md`, `util/` and `standards/` into `method/`; root `CLAUDE.md` and `AGENTS.md` point at `method/AGENT-RULES.md`.
- `install.py` ships `method/` plus the three root files, points entry files at `ndd/method/AGENT-RULES.md`, and finds the previous map under `method/` or the flat layout, backing it up as `ndd/method/ndd.prev.map.md`.
- Tests repathed; the install test's link check now fails a shipped link leaving `ndd/`. Fingerprint test passes; install test fails only on the unpromoted live links, as expected.
- Open: *Install Check* has no case for a first upgrade from the flat layout, so the backup path the plan names is untested.
- *Orientation* A/B, 2 arms × 2 scenarios: same edits and version file in both. Client: the new wording states the method map is not the project's spec, where the old only implied it. NDD repo: the new wording leaves open whether the method map is part of `map.md`.
- *Orientation* bullet 2 re-agreed: adds "a map separate from the repository's own"; A/B not re-run, as it adds a fact rather than rewording.
- Open item settled: *Install Check* and `install_test.py` gain the flat-layout upgrade case; it passes.
- No drift since the copies; promoted `map.md`, `testing.map.md`, `README.md`, `method/ndd.map.md` and `method/AGENT-RULES.md`. Both tests pass; no stale paths outside `changes/archive/`.

## Conclude

Verified: the live files match the specification. Two targets were re-agreed during Build: after the A/B test, *Orientation* bullet 2 now says the method map is separate from the repository's own; and *Install Check* and its test gained a flat-layout upgrade case. Links in *Release Steps*, *Rule Testing* and *Method Map Form* were repathed as corrections. Version 3.0.0-dev, since client paths move. Accepted over the bound: *NDD* (988), *Map Files* (893), *Installer* (828).
