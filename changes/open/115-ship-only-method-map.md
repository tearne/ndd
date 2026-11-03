# Ship only the method map

## Intent

Ship only the method a client needs: `ndd.map.md` stands as its own root in a client's `ndd/`, and NDD's project map, `map.md` and `testing.map.md`, which describe how this repository builds, releases and tests itself, stay in the checkout.

## Context

Raised during 105 (2026-11-03). The shipped `testing.map.md` described tests that 095 had stopped shipping, and the shipped `map.md` carries maintainer-only nodes such as *Release Steps*. Both ship today only because `ndd.map.md`'s root links up to *NDD Project* in `map.md`, the agent rules cite *Distribution* there, and `map.md` links into `testing.map.md`.
