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
