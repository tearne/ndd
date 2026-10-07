# Formal Specification as map content

## Intent

Narrow *Change Specification* to map content and move map promotion to *Formal Build*'s closing act, under a new NDD-level assumption that specifications are expressible as maps. Resolves [`2026-10-06-formal-specification-pacing-discussion`](../archive/2026-10-06-formal-specification-pacing-discussion.md).

## Context

Grounded in the archived discussion [`2026-10-06-formal-specification-pacing-discussion`](../archive/2026-10-06-formal-specification-pacing-discussion.md), where the working position was agreed.

**Planning state (paused 2026-10-06):**

- Change Style: **Formal**, confirmed.
- Intent: approved (revised version above — the earlier version named *Sync Rule* and *Plan* as targets; re-reading the map showed per-node approval was already in *Change Specification*, so the deltas narrowed).
- Next plan part: **Change Specification** — walk the proposed/updated map nodes per-node under the *Engagement Rule*. Candidate scope: updated *Change Specification* node (narrow format to map-only), updated *Formal Build* node (map promotion as the closing act of Build, non-map assets in place), and placement of a new NDD-level assumption. A candidate home for the assumption is a new principle under *Principles*, since the root *NDD* node already asserts the map is the primary specification; alternative is folding into the *Map* node itself.

**Related:**

- [`060-flow-reads-at-lifecycle-hinges`](060-flow-reads-at-lifecycle-hinges.md) and [`080-agent-rules-rendering-review`](080-agent-rules-rendering-review.md) are sibling AGENT-RULES rendering fixes surfaced during this session; not required for `070`.
- An earlier approval to cite rules by map-node name (not number) is still floating uncaptured; may be absorbed into `080`.


## Change Specification

Target is a whole-map copy at [`070-formal-specification-as-map-content/ndd.map.md`](070-formal-specification-as-map-content/ndd.map.md), starting as a verbatim copy of `ndd.map.md`. Proposed node edits are made directly in that copy and walked per-node under the Engagement Rule. Approval stamps land in the copy's per-node yaml blocks and transfer to the live map at the closing act of Build.

Nodes in scope (walk order):

1. *Map* — reframe primacy as an NDD-level assumption. **Settled, stamped.**
2. *Formal Build* — anchor narrowed to Build-only; add map promotion as Build's closing act, before Conclude. **Settled, stamped.**
3. *Formal Conclude* — new node, factored out of *Formal Build*; carries Conclude and Archiving paragraphs plus the disposable-whole-map-copy clause. **Settled, stamped.**
4. *Formal* — add child nav links to its four children. **Settled** (nav links don't affect fingerprint; existing stamp still valid).
5. *Change Specification* — narrow format to map-only; drop prose/table/diagram alternatives. Fold in change 100 (prompt for whole-map copy at Formal start) as one sentence. **Settled, stamped.**
6. *NDD* (root) — update the Contents one-liner for *Map* to track the Map node's new wording. **Settled, stamped.**

Change 100 (`100-prompt-for-whole-map-copy-at-formal-start`) folds into node 5 and archives alongside 070 at Conclude.
