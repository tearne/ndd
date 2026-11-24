# Bulk request

**Change Style:** Formal

## Intent

The map viewer should take one request for sign-off from chosen people on several nodes, across map files.

## Context

Raised as an aside on 2026-11-19 during 320, as bulk requesting from the tree. Split on 2026-11-20: this change builds the back end as Formal; the tree UI, which needs iteration, is 360, Emergent, parked until this is built. A request is currently made one node at a time, from *Request* in a node's *Sign off* drop-down.

## Change Specification

The targets, drafted in a companion `targets.md` dropped at archiving once promoted, were *Request Guards*, *Write Checks* (new) and *Sign-off Button*, with link-only edits to *Map Viewer* and Contents.

## Implementation Plan

- **Endpoint** — a new POST `/request` takes the token, a list of nodes (file and name) and a list of names, with no fingerprint. The single-node *Request* button sends a list of one. `/signoff` serves sign-offs only and refuses a `request` key, so nothing sent as a request is written as a sign-off. Both keep the Host, Origin and token checks.

- **Writing across files** — under the write lock, every node is checked; then each changed file, carrying all its nodes' edits, is written to a temporary beside it, and each is swapped in. A failure during the swaps is not rolled back: each swap is whole, and the uncommitted changes show what landed.

- **Tests** — the map viewer tests cover `/request` on one node and on several across two files, the whole refusal, skipped names, and `/signoff` refusing a `request` key.

## Progress

- 2026-11-20: split from the tree UI (now 360); Intent and Formal style approved. Unresolved 1–3 resolved with the user.
- 2026-11-24: Unresolved 4 resolved: own `/request` endpoint. Unresolved 5 resolved: *Request Guards* sole target. Over size with the new bullets, so split: five targets in `340-bulk-request/targets.md` — *Request Guards*, *Write Checks* (new), *Map Viewer* link, Contents entry, *Sign-off Button* link, all approved and stamped. *Sign-off Button* trimmed to 802 characters. Change Specification approved; Intent trimmed.
- 2026-11-20, paused. Next: Unresolved 4 (shape: extend `/signoff` or a separate action) and 5 (map home while there is no UI), then the Change Specification targets in a companion `targets.md` (at least *Request Guards*), the Intent trim, and plan approval.
- 2026-11-24: Implementation Plan approved; Unresolved, all folded into the plan, deleted. Next: plan approval and Build.

## Log

- 2026-11-24: plan approved; Build Lock taken. Claims 3.10.0-dev (minor); map viewer 0.6.0 → 0.7.0.
- Endpoint: `/request` added; `/signoff` serves sign-offs only and refuses a `request` key; *Request* button posts to `/request`. Viewer 0.7.0.
- Writing across files: `request_signoffs` checks every node, then writes temporaries and swaps each in.
- Tests: three map viewer checks added (single, across files, refusals) and a `request` key refusal; map viewer and browser tests pass. The refusal check was seen to fail with the all-or-nothing check disabled.
- Deviation: *Map Viewer Check* (testing map) described the new checks only after a split: *Map Viewer Write Check* added as its child, with a Contents entry; both stamped.
- Promoted into `map.md`: *Request Guards*, *Write Checks*, *Sign-off Button*, and the *Map Viewer* and Contents links. Every stamp matches its live fingerprint; nothing due for tearne in either map.

## Conclude

Beyond the plan, the testing map had to describe the new checks. That took *Map Viewer Check* over size, so it was split, adding *Map Viewer Write Check* beneath it. *Sign-off Button* was trimmed to stay near its cap. A `/request` reply gives the number of stamps written, as `Requested N`.
