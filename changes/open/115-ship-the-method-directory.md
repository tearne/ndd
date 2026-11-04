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
