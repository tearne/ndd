# Bulk request

**Change Style:** Formal

## Intent

The map viewer should take one request for sign-off from chosen people on several nodes, across map files, under the same guards as a single request.

## Context

Raised as an aside on 2026-11-19 during 320, as bulk requesting from the tree. Split on 2026-11-20: this change builds the back end as Formal; the tree UI, which needs iteration, is 360, Emergent, parked until this is built. A request is currently made one node at a time, from *Request* in a node's *Sign off* drop-down.

## Unresolved

1. ~~Stale-page guard~~ — resolved: requests, single or bulk, carry no fingerprint receipt; sign-offs keep it. Safe because a request writes `hash: null`, never overwrites a stamp, and the token, Host and Origin guards stay. For the *Request Guards* target.
2. ~~Partial failure~~ — resolved: if any node cannot take the request (Contents, no scaffolding block, not found), the whole request is refused, naming each failing node and why, and nothing is written. Names already stamped on a node are skipped, as for a single request, not a failure; the reply gives the number written.
3. ~~Across files~~ — resolved: under the write lock, check every node, then write every changed file's temporary, then swap each in; no rollback.
4. Shape: extend `/signoff` with a list of nodes for a request, or a separate action?
5. Map home: with no UI until 360, which node describes the bulk request — *Request Guards*, *Sign-off Button*, or a new node under *Map Viewer*?

## Progress

- 2026-11-20: split from the tree UI (now 360); Intent and Formal style approved. Unresolved 1–3 resolved with the user.
- 2026-11-20, paused. Next: Unresolved 4 (shape: extend `/signoff` or a separate action) and 5 (map home while there is no UI), then the Change Specification targets in a companion `targets.md` (at least *Request Guards*), the Intent trim, and plan approval.
