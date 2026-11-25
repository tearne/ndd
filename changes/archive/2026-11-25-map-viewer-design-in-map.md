# Map viewer design in the map

**Change Style:** Vibe

## Intent

The project map should outline the map viewer's key UI features, so what it offers is not left to the code.

## Bounds

One new child of *Map Viewer*, *Navigation*, outlines moving through the tree and the second pane; *Map Viewer* gains only its link. The code's header stops calling the viewer a proof of concept.

## Context

Deferred by the user on 2026-11-16 from 002 Map viewer iteration, which left *Map Viewer* (`map.md`) near its size cap; a child node was suggested. Narrowed on 2026-11-17 to the aim alone: the earlier list (read-only and single file, page moves keeping the tree's folds, the second pane) had dated, as 140 made the viewer write sign-offs and 310 changes how the panes scroll.

## Progress

- 2026-11-25: check of the map against the code. Covered: tree, node, sign-off diff, Sign off, Due for, Request bar, guards, write checks, uncommitted light. Not in the map: tree navigation (page moves keep folds; the current node is marked and revealed; a branch's fold button folds or opens it and all below) and the second pane (*Split*, *Swap*, *Close*, back and forward per pane, each scrolling on its own, the node's links opening there once split). Suggested: one child node of *Map Viewer*, *Navigation*.
- 2026-11-25: Intent approved.
- 2026-11-25: Change Style Vibe confirmed (agreed with planning on that basis).
- 2026-11-25: Bounds approved; Intent re-read, nothing to trim.
- 2026-11-25: plan approved; Build Lock taken. Claims 3.12.1-dev (patch); map viewer stays 0.9.0.
- Header comment no longer calls the viewer a proof of concept.
- 2026-11-25: *Navigation* approved and written under *Map Viewer*, stamped 1f1dbdb3; *Map Viewer* gains its link and *Contents* its entry (navigation only, Map Viewer's stamp still current).

## Conclude

Completed. Out of Bounds and left alone: the root of `map.md` still calls the viewer "a prototype". That's now out of step with the code's header.
