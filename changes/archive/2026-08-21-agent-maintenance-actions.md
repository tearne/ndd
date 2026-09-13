# Agent maintenance actions

**Mode:** Explore

## Intent

The agent performs a growing set of recurring upkeep actions on the map that the user does not — keeping the tree overview in step with the nav links, keeping scaffolding ids and links consistent, flagging oversize nodes, enforcing writing style, watching child ordering. Each is currently stated inline in the node it concerns, so the agent's standing obligations are nowhere visible as a set. Gather them so the agent's recurring responsibilities are named in one place, without hollowing out the home nodes a reader relies on.

## Approach

### Map Maintenance becomes the parent for both faces of upkeep

Map Maintenance is reworked from a flat node into the home for keeping the map healthy, which has two faces: conceptual (does the structure still fit the user's model) and mechanical (is the artefact internally consistent). It gains children rather than absorbing everything into one body.

### Two children: drift signals and consistency upkeep

The existing restructuring signals (node wants splitting, grown verbose, homeless concept, boxes mismatch the model) move into a child for conceptual drift. A second child, **Consistency Upkeep**, gathers the agent's standing mechanical obligations. The parent keeps only the short framing that names the two faces.

### Consistency upkeep indexes, it doesn't rehome

The upkeep child lists each standing obligation as a bullet that cross-links to the node defining the thing, rather than moving that node's detail. Home nodes keep their locally-sufficient detail; each gains a See also back to the upkeep node. This keeps a reader of, say, Node Sizing fully served in place while making the agent's obligations visible as a set.

### Child ordering joins as a named upkeep obligation

Child order under a node may carry a natural reading sequence — a lightweight, parent's-discretion notion, not a formal rule. The convention itself is stated in Navigation Links, alongside the child links it governs; Consistency Upkeep lists watching child order as one of its obligations. The concrete first application rides along in this change: reorder Change-Management's children so Change Lifecycle precedes Cadences (keeping the tree overview in step).

## Plan

**Topics**

- Rework Map Maintenance into a framing parent naming the two faces of upkeep; give it a scaffolding id and child links.

- Add the drift-signals child holding the existing restructuring signals lifted from the old Map Maintenance body.

- Add the Consistency Upkeep child: one bullet per standing obligation (tree-overview sync, id/nav-link consistency, oversize-node flagging, writing-style enforcement, child-order watch), each cross-linking to its home node.

- Add a See-also backlink to Consistency Upkeep from each home node it indexes.

- State the child-ordering convention in Navigation Links.

- Reorder Change-Management's children (Change Lifecycle before Cadences) in both the child links and the Contents tree overview.

**Done when** Map Maintenance reads as a two-child parent, Consistency Upkeep indexes every standing obligation with working cross-links backed by See-also returns, Navigation Links carries the ordering convention, and Change-Management's children are reordered consistently in node and overview.

## Log

- Parent prose trimmed on user feedback: "keeping the map useful is constant engagement" was principle-content (Comprehension is an Activity), so the parent now just frames the two faces as bullets.

## Conclusion

Completed as planned. Map Maintenance became a two-child parent (Conceptual Drift, Consistency Upkeep) with the upkeep child indexing five standing obligations via cross-links, each home node gaining a See-also return. The child-ordering convention landed in Navigation Links and was exercised by reordering Change-Management. The only deviation was trimming principle-content from the parent's framing (see Log).
