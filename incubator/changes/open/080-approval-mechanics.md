# Approval mechanics

## Intent

Give the map a stakeholder sign-off axis, orthogonal to build-state, so non-authors can approve the map a few nodes at a time in routine meetings rather than via a big-bang review. Each node carries per-approver **approval stamps** (person + timestamp) in its scaffolding block — approval is per-node and independent per stakeholder, matching the one-node-at-a-time engagement rhythm. No sidecar ledger: stamps live in the node, so they survive rename and move via the stable id.

**Drift is computed, never stored.** A node reads as *due* for a stakeholder when its current content differs from what they last approved; merging new content into the map passively dirties the frontier of everyone whose stamp predates it. The stakeholder surface is a **due-queue** — read each due node as it is now and re-approve, updating the timestamp to current.

Graceful degradation is first-class: a map with no stamps shows nothing, and the machinery stays invisible until a project reaches for it.

Decomposition item 3 (keystone sequence in `enhancement-discussion.md`, which holds the full P2 rationale). Depends on node structure and identity, which is already built.

## Unresolved

- **Do node ids earn their place?** (folded from 240, 2026-09-10). Change 220 settled that nodes are cited outside the map by name alone, so the `id` has no consumer today: links resolve by name, citations do too, and the scaffolding block, the id rules in Node Identity and the review step that adds missing ids carry no weight. This change needs the block for its stamps but not the id; the id's one prospective consumer is 90, which resolves a node's history through git across renames. The Approach states whether the id stays for 90 or is dropped.
