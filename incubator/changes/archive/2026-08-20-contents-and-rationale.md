# Root split and Principles capture

## Intent

The root node does double duty: reader orientation (the tree overview and concern summary) and the method's founding rationale — which today lives only in an external `PRINCIPLES.md` the map can't even resolve. Split them. Give orientation its own **Contents** home, and bring COD's founding case into the map as **Principles** — comprehension as an activity, local sufficiency, trees over graphs, and the rest. Several of those principles are already enacted by existing nodes, so the same change points each such node at the principle it serves rather than repeating it, keeping the map true to its own artifact-economy discipline.

**Cadence:** Explore.

## Approach

### The root is the orientation home; no separate Contents node

Keep the tree box, the three-concern summary, the naming callout and the child links in the root and let that thin node *be* the Contents home. A standalone Contents node would be navigation-chrome, not a concept in the user's model, and orientation belongs where the reader lands.

### Principles enters as a new child subtree of the root

The founding case becomes a `Principles` parent alongside Specification, Change-Management and Tooling. Its prose carries the compressed motivation — agent-augmented development broke the bundle where producing code also built understanding; maintaining the map is the replacement activity; conceptual maintainability now has first-class standing alongside correctness. The seven-principle essay doesn't fit one node, so each principle becomes a terse child:

```
Principles
├ Comprehension is an Activity
├ Enjoyment
├ Local Sufficiency
│ └ Trees over Graphs
├ Cross-Agent Falsifiability
└ Interaction Grain
```

Two shaping calls: **Trees over Graphs** nests under **Local Sufficiency** because a tree is the mechanism that delivers local sufficiency, not a peer of it; and **conceptual maintainability** stays folded into the parent prose rather than becoming a node, since it is the meta-justification and nothing operational references it. The Enjoyment node carries the **artifact economy** corollary that the pruning and length disciplines lean on.

### Operational nodes reference their principle instead of repeating it

Where an existing node currently states a rationale a principle now owns, replace the repetition with a **See also** pointing at the principle. Expected pairings, confirmed per-node during Build: Node Sizing and Navigation Links → Local Sufficiency; Map Structure and Node → Trees over Graphs; Approach and Conclude → Enjoyment (artifact economy); Map Maintenance → Cross-Agent Falsifiability; Engagement Rule → Interaction Grain; Specification → Comprehension is an Activity.

### The external PRINCIPLES.md is left untouched

It belongs to the outer framework, and how the method reaches adopting projects is the separate `distribution-and-upgrade` change. This change brings the rationale into the incubator map only.

## Plan

The work is map editing, so node bodies are negotiated one at a time during Build per the Engagement Rule rather than pre-drafted here.

**Topics**

- Thin the root to its orientation role and extend the tree box with the Principles subtree.

- Author the `Principles` parent node with the compressed motivation prose.

- Author the six principle nodes, each terse and referenceable.

- Add **See also** references from the operational nodes to the principle each enacts, trimming any rationale the principle now owns.

**Done when** the map carries the Principles subtree, the root reads purely as orientation, and every operational node in the pairings above points at its principle rather than restating the reason.

## Log

- Build entered; `active.md` locks this change. Not versioned, so no bump.
- **Principles subtree written** in `map.md` (appended after Tooling): parent `Principles` (id `p4c`) plus six children — `Comprehension is an Activity` (`c8a`), `Enjoyment` (`j2e`, carries the artifact-economy corollary), `Local Sufficiency` (`s3l`) with child `Trees over Graphs` (`g6t`), `Cross-Agent Falsifiability` (`f9x`), `Interaction Grain` (`r5i`). All trimmed hard per user; no Detail blocks except where load-bearing.
- Cut during trimming, by agreement: the "two failed strategies" argument (dropped) and the conceptual-maintainability lineage (folded to a clause). Preserved: "map surfaces logic bugs before code" now sits in the Principles parent prose; "peak tree" in Trees over Graphs; ambiguity test in Cross-Agent Falsifiability.
- **Root reworked**: added `Principles` as first child link + tree-box subtree; reframed opening from meta ("what a map is") to product register ("what the method does"), leaning on Specification for the map definition and Principles for the why. Naming standardised — "the method" in prose, "Unified Map Method" only as heading/links/callout (fixed a stray "COD" in the Principles node).
- **REMAINING — final topic, the See also references.** Approved in principle, not yet applied. Nine nodes, each gains a `**See also**` entry (placed after any Detail block):
  - `Specification` (`sp1`) → Comprehension is an Activity. **Trim first**: drop the clause "Maintaining it is the comprehension-building activity;" from its prose (keep "Agents render it into code."), let the See also carry that reason.
  - `Node Sizing` (`z9p`) → Local Sufficiency — why nodes stay small.
  - `Navigation Links` (`b3q`) → Trees over Graphs — **re-pointed** from the originally-approved Local Sufficiency, because the node is about the one-parent tree.
  - `Map Structure` (`m6x`) → Trees over Graphs — why the sketched shape is a tree.
  - `Node` (`nd1`) → Trees over Graphs — nodes form a tree, complexity kept inside a node.
  - `Approach` (`a2r`) → Enjoyment — artifact economy: why the Approach is pruned to decisions-and-reasons.
  - `Conclude` (`o4j`) → Enjoyment — artifact economy: why Conclude is capped and never re-tells the journey.
  - `Map Maintenance` (`t7v`) → Cross-Agent Falsifiability. **Trim first**: shorten its Detail's re-explanation of the ambiguity test to just name the test and point, since the principle now owns it.
  - `Engagement Rule` (`n3g`) → Interaction Grain — why edits go one node at a time.
- User was mid-review of that See-also batch (had confirmed nothing yet in this turn) when they stopped. Resume by confirming the batch, then applying the nine edits. After that, all Plan topics are done → tell user, await confirmation, then Conclude.
- **See-also topic completed**, node by node per Engagement Rule. Deviations from the drafted plan, all user-approved in-flight:
  - `Specification`: also cut the redundant segue line "The map's unit is the **Node**." (child link already points at Node).
  - Enjoyment node prose tweaked: "a dialogic activity" → "a dialogic activity with the agent" (clarity, user request).
  - `Conclude`: extra Detail trim — dropped "The cap is deliberate pressure against re-telling the journey…" (repeated the node's own prose and the artifact-economy reason the See also now carries).
  - `Map Maintenance`: rendered as an **inline** pointer — "the *ambiguity test* (see [Cross-Agent Falsifiability])" — instead of a `**See also**` block, at user request; Detail's re-definition of the test trimmed.
- All Plan topics now done. Awaiting user confirmation to Conclude.

## Conclusion

Completed. The Principles subtree, root reorientation and nine principle-references all landed as planned; deviations are in the Log.

Two things worth surfacing beyond the Log:

- **Documentation impact:** the external `PRINCIPLES.md` was deliberately left untouched (its reconciliation belongs to the `distribution-and-upgrade` change). No other project docs affected.

- **Spun-off convention:** the inline-link-vs-See-also question raised during the See-also pass was captured as a new bullet in the `map-writing-conventions.md` TODO rather than resolved here, keeping this change focused. It awaits distillation into the `Formatting` node.
