# Frictionless map updates

## Intent

Make changes expressible so that updating the map is trivial — ideally a change *is* the map update, dissolving the separate "transcribe the outcome into the map" step this very build has been doing by hand. The goal is what matters; the mechanism is deliberately left open.

One candidate approach, worked in detail in `enhancement-discussion.md`, is **build-state as location**: a node's state (proposed / accepted / built) is expressed by *where it lives*, not by a status field. A proposal artefact is an intent document plus a proposed map subtree, reviewed as a PR-like diff (the map as it reads now vs as it would read) and merged into a reality-only main map. That would make the Sync Rule structural — the main map physically cannot hold unbuilt content — and fuse today's change document with the map slice it proposes.

But that is one route, not the committed solution; other ways to make "a change ≈ a map update" true remain open. Whatever the mechanism, graceful degradation is a first-class constraint: a simple project must be able to adopt it without heavy boilerplate.

Decomposition item 2 (of the keystone sequence in `enhancement-discussion.md`), which stays as the analysis archive.
