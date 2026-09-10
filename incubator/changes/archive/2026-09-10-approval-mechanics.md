# Approval mechanics

**Cadence:** Explore

## Intent

_(Approved 2026-09-10.)_

Give the map a stakeholder sign-off axis, orthogonal to build-state, so non-authors can approve it a few nodes at a time in routine meetings rather than in one big review. Each node carries per-approver **approval stamps** (person + timestamp) in its scaffolding block. Drift is computed, never stored: a node is *due* for a stakeholder when its content differs from what they last approved, and their surface is a **due-queue** of nodes to re-read and re-stamp. A map with no stamps shows nothing until a project reaches for this.

## Context

Decomposition item 3 of the keystone sequence in `enhancement-discussion.md`, which holds the full P2 rationale and the hybrid model. Depends on node structure and identity, already built. Stamps live in the node rather than a sidecar ledger so they survive rename and move. Change 250 (meta.md as a second tree) asks to be planned alongside this one, since sign-off should cover the specification, not the pipeline. NDD's own map is unlikely to carry a stamp; the feature exists for client projects, so the no-stamps case is the one this repo will live in.

## Held

_(Empty. The due-node selection item was parked as change 310 on 2026-09-10.)_

## Approach

_(Approved 2026-09-10.)_

- **Stamps are a mapping in the scaffolding block**, `approvals:` keyed by a short person handle, each value holding a timezone-qualified timestamp and the fingerprint of the text that person approved. A mapping rather than a list because each person holds one frontier; re-approval overwrites. The timestamp is kept for change 90, which resolves it to a commit.

- **Drift compares fingerprints, not git.** The fingerprint is a short hash of the node's user-facing text — heading, prose, callouts, *Detail*, *See also* — excluding scaffolding and navigation links, whitespace normalised. This lets drift and the due-queue work without git, as the model promises, while a stamp stays a record of what was approved rather than a stored drift flag. Links are excluded because a child renamed or added changes nothing this node says; the child is itself due.

- **One new node, Sign-off, under Maintenance**, describing the axis, the due-queue and, in *Detail*, the stamp format. Maintenance is where the map's other "is this node due" checks live and Edit Governance already points there. Node Identity's "today just `id`" line gains a pointer.

- **The agent runs the due-queue on request**, walking the map for nodes whose fingerprint differs from a person's stamp and presenting them one at a time. No tooling; change 290 can render it later.

- **Stamping is a correction-class write.** Told that a person approved a node, the agent writes the stamp and reports it without per-node negotiation, since scaffolding carries no meaning for the reader.

- **Degradation is by absence.** No `approvals:` key means nothing shows; the agent never adds it unprompted and Tidy leaves it alone.

- **No restriction on which nodes take stamps.** Change 250 narrows the set by moving pipeline nodes out; this change stays independent of it.

- **No new agent rule**, since sign-off is not something almost every session touches.

- **Verification on a scratch copy**, since this map carries no stamps: stamp, edit, confirm the node falls due, re-stamp, confirm it clears.

- **Node id kept for change 90.** It has no consumer today, but removing a token from every node and restoring it for 90 is churn for no saving; if 90 is ever discarded the id goes with it (settled 2026-09-10).

## Topics

_(Approved 2026-09-10. Build started the same day.)_

1. **Sign-off node.** A new child of Maintenance: prose on the axis and the due-queue, *Detail* with the stamp format, fingerprint rule and a two-approver example, *See also* to Node Identity and Orient Then Focus. Maintenance gains the child link and its overview line; the Contents tree overview follows.
2. **Node Identity.** The *Detail* line saying the block holds "today just `id`" changes to name approval stamps with a link to Sign-off.
3. **Scratch trial.** On a copy of the map outside the project: stamp a node for two people, edit it, confirm it falls due for both, revert, confirm it clears for one, re-stamp the other. Confirm the real map is untouched.

**Done when:** both map edits are written and approved with counts reported, the tree overview and links are in step, the scratch trial has shown a node falling due and clearing, and the project map carries no stamp.

## Log

- 2026-09-10 — Sign-off drafted at 1235 characters, over the bound. User chose to split: **Approval Stamp** (child of Node, the stamp format) and **Fingerprint** (child of Approval Stamp, the hash rule) join Sign-off. Three new nodes instead of the Approach's one; topic 2's pointer goes to Approval Stamp.
- 2026-09-10 — Scratch trial passed on a copy of the map with a throwaway script implementing the Fingerprint rule: two stamps written, an edit made the node due for both, one re-stamp cleared one person, a revert cleared the other and re-dued the first. Writing a stamp, a whitespace-only edit and a child rename in the nav links all left the fingerprint unchanged. The project map carries no stamp. Script not kept; a shipped reference is change 275's question (numbered 300 at the time).

## Conclude

_(Approved 2026-09-10.)_

Landed as three nodes, not the one the Approach named: Sign-off under Maintenance, Approval Stamp under Node with Fingerprint beneath it. Node Identity and Maintenance gained pointers; the Contents overview follows. The due-queue's selection and ordering was left out deliberately and parked as change 310; a reference implementation of the fingerprint is change 275's question (numbered 300 at the time). No stamp exists in this map.
