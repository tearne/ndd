# Agent maintenance actions

**Kind:** idea
**Anchor:** t7v

We seem to be accumulating recurring upkeep actions the agent performs on the map rather than the user: keeping the tree box-drawing in step with the nodes, ensuring scaffolding metadata is consistent, watching node character counts, enforcing language and formatting style. Consider whether these belong gathered under a dedicated node (a **Maintenance** node, or folded into `Map Maintenance`) so the agent's standing obligations are named in one place.

When this lands, consider rehoming detail that currently states an upkeep action inline (e.g. `Node Sizing`'s "the agent flags it rather than silently trimming") into the maintenance node, leaving a **See also** in its place.

## Folded in: child-node ordering (was change 20)

Child order under a node may carry a natural reading sequence rather than being incidental — a lightweight, parent's-discretion notion, not a formal rule. It belongs among the standing things the agent watches, alongside language and formatting style. Concrete one-off application to carry out when this lands: reorder `Change-Management`'s children so `Change Lifecycle` precedes `Cadences`, the lifecycle reading more naturally first with cadences as a qualifier on it (remember to keep the root tree overview in step).
