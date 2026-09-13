# META node for map-about-map nodes

**Mode:** Explore

## Intent

Introduce a conventional **META** node: a fixed home for nodes that describe the map or the product itself rather than a domain concept. Because such nodes carry conventional names, they double as stable jump targets regardless of the root node's name. Its first member, **Contents**, holds the tree overview — giving the fast jump to the tree that originally prompted this. Settle which further meta-nodes are conventional, and which are standard versus optional.

## Approach

### META sits apart from the domain tree and orients a new reader

META is a node listed first among the root's children, holding map-about-map nodes so they don't intermingle with the domain concepts. Its members have conventional fixed names, so each is a reliable symbol-picker jump target no matter what the root or domain nodes are called. META's own prose carries a very short orientation — that the document is a conceptual map, a tree of named nodes navigated by links — because in a product's map, unlike this method's own, the tree convention won't be self-evident to a reader.

### Contents is mandatory and holds the relocated tree overview

Every map has a **Contents** meta-node holding the tree overview. The overview moves out of the end of the root node into Contents — a single copy under a stable, jumpable name — and Contents is placed near the top of the file so the shape is reached as fast on opening as before. This supersedes the "overview lives at the end of the root" arrangement, so the Map Structure node is updated to match.

### Further members are optional

Beyond mandatory Contents, a map may adopt optional meta-nodes: product **Rationale** (why the product exists) and a domain **Glossary**. The notation-legend need is met by META's own orientation prose, so no separate Legend node.

## Plan

**Topics**

- Add the META node as the root's first child, with orientation prose and its child links; add META to the root's link block and the tree overview.
- Create the Contents node under META, relocate the tree overview into it, and position it near the top of the file.
- Update the Map Structure node so it describes the overview living in Contents rather than at the end of the root.
- State the convention: META is standard with mandatory Contents and optional Rationale/Glossary; record it in the appropriate Specification node(s).

**Done when** the map carries a META node whose Contents holds the sole tree overview jumpable by name, the root is prose-only, and the meta-node convention is documented.


## Conclusion

The change broadened from its original "jump straight to the tree overview" idea into a general META-node convention; Contents absorbs the jump-target need as a mandatory meta-node, with Rationale and Glossary as optional members.

The parked aside (should Principles move under META?) resolved as a **thin Rationale node** pointing to the Principles subtree — Principles stays first-class, and META still carries the conventional Rationale entry. This added one node beyond the approved plan.

Nodes touched in `map.md`: new META, Contents (holds the relocated sole tree overview), and Rationale; root reduced to prose-only with META as its first child; Map Structure repointed to Contents. A pure-pointer Rationale node was accepted as a deliberate convention instance despite brushing the only-child grain.
