# Due node selection in the viewer

**Change Style:** Formal

## Intent

The map viewer should help a stakeholder sign off what is due for them: choose a person, see which nodes are due for them, and step through those nodes in a useful order, signing each off as they go. In a split page, each pane should scroll in a box of its own, with its scrollbar at its own edge.

## Context

Parked from change 80's Held on 2026-09-10 as agent-side selection at Sign-off; refreshed on 2026-11-17 to use the map viewer, which now records sign-offs, and to fix the split page's scrolling. The old Intent's ordering candidates remain open: rank by how load-bearing a node is, lead with nodes where most stakeholders are out of sync, or orient around one stakeholder. The aid it named to accompany each node, change 320's retrospective diff, was delivered by tooling development (archived 2026-11-10) as the viewer's sign-off diff.

## Change Specification

Shape agreed 2026-11-17:

- A *Due for…* selector in the tree pane, listing every signer in the map's stamps plus the names added in the sign-off drop-down.
- With a person chosen, their due nodes marked in the tree, and a count such as "7 due for bob".
- *Next due* and *Previous due* step through them; after a sign-off the page moves on to the next due node.
- Order is tree order; ranking stays out of scope.
- In a split page each pane scrolls in its own box.

Planned edits, on copies in [310-due-node-selection-in-the-viewer/](310-due-node-selection-in-the-viewer/) of `map.md`, `testing.map.md` and `method/ndd.map.md`, taken 2026-11-17 before any edit:

1. *Map Viewer Due* (project map, new, under *Map Viewer*): the selector, the marks and count, stepping, moving on after a sign-off, tree order.
2. *Map Viewer* (project map): child link and a bullet.
3. *Sign-off* (method map): due nodes can also be followed in the map viewer.
4. *Map Viewer Browser Check* (testing map), or a new check beside it if over the bound: the due flow, and each pane scrolling on its own.
5. Contents entries for any new node.

The scrolling fix has no node to describe it: the second pane is not yet in the map, which is 150's aim.
