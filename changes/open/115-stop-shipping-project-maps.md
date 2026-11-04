# Stop shipping the project maps

**Change Style:** Formal

## Intent

Stop shipping the main map, `map.md`, and the tests map, `testing.map.md`, which a client doesn't need. In a client's `ndd/`, `ndd.map.md` stands as its own root.

## Context

Raised during 105 (2026-11-03). The shipped `testing.map.md` described tests that 095 had stopped shipping, and the shipped `map.md` carries maintainer-only nodes such as *Release Steps*. Both ship today only because `ndd.map.md`'s root links up to *NDD Project* in `map.md`, the agent rules cite *Distribution* there, and `map.md` links into `testing.map.md`.

## Unresolved

- Agent rules' *Orientation* bullets cite *Distribution*, *Installer* and *Agent Rules* in `map.md`, which a client will not have: where does the client-facing fact they render live?
- `ndd.map.md`'s root links up to *NDD Project*: what does the tree look like in the checkout once *NDD* is a root in a client?
- *Fingerprint* points to *Fingerprint Check* in `testing.map.md` as the reference that pins the rule.
- `README.md` ships and links to `map.md`.
- *Distribution* says a client's `ndd/map.md` is this project map.
