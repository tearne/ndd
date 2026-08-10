# Node structure & identity

**Mode:** Explore

## Intent

The lifecycle-aware map needs each node to carry a durable identity and defined room for scaffolding. Today a node is just a heading, nav links, and prose — nothing survives a rename, and there is nowhere for approval stamps or build-state to live. Before any lifecycle mechanics can be built, the node itself must be pinned down: what gives it identity across renames, and what blocks it may carry.

Define enough to **start dogfooding now** — concrete enough to rewrite this project's own map in the new format and live with it.

It must not tax simple projects: a plain map stays plain markdown, with identity and scaffolding opt-in and invisible until wanted.

## Approach

### Markdown is the source of truth

Settled earlier. Nodes are authored as markdown prose because the comprehension thesis requires human authorship, and because proposal review depends on human-readable diffs. Any structured index for tooling is *derived* from the markdown, and is out of scope for this change.

### The format is a strict superset of today's node

A node with no ID and no scaffolding block is exactly a current plain-markdown node. This is the degradation guarantee, not a mode or flag: a simple project writes the map it writes today, and identity and scaffolding are purely additive on top. Everything below is opt-in.

### Identity is a stable ID decoupled from the node name

Rename-survival requires an identity that isn't the name. Each node may carry a stable, opaque short ID (e.g. `k7f`) — opaque rather than a readable slug so there is no temptation to "fix" it on rename, which would defeat its purpose. Navigation links keep using the node *name* as their anchor, exactly as today, so markdown navigators stay friendly; the ID is a parallel, machine-only identity, not a link target. Because links never resolve to it, the ID needs no anchor mechanism — it simply lives in the scaffolding block. Absent an ID, a node is just a name-anchored node as today — the degraded case.

### Scaffolding lives in one delimited per-node block

All machine-maintained metadata — the ID now, approval stamps later — sits in a single delimited block per node, kept out of the user's prose and agent-maintained like nav links are today. One block rather than scattered fields, so a viewer can collapse it and a reader can ignore it. The block is a **fenced YAML block** to start: markdown-native (no HTML), clearly delimited, trivially parseable, and easy to swap if dogfooding argues against it. Build-state stays *location* per the resolved model, so it is not an in-node field.

### This change fixes the container, not the lifecycle content

Approval stamps, drift, and proposal artefacts are later changes. Here we settle only the slots and syntax — where the ID lives, how the block is delimited, how references resolve — so later changes add fields into a known shape rather than reinventing the format.

### Dogfooding is the completion test

The format is done when this project's own map can be written in it and navigated. This change creates a real `map.md` for the incubator — kept to a small, honest starting subtree, not the whole product — so the format survives contact with real content (nav links, the ID block, and degradation all exercised). It is both the proof and the format's first real user; the map grows later.

## Plan

**Topics**

- **Node format specification** — the authoritative anatomy of a node in the new format: heading, name-anchored nav links, the fenced YAML scaffolding block and where it sits, and the existing prose/Detail/See-also sections. Authored as a format document in the incubator (the pinned COD snapshot under `changes/agent/` is not touched).

- **Stable ID scheme** — the opaque short-ID form, how an ID is generated and kept collision-free, and the assign-once / never-rewrite-on-rename rule; how the scaffolding block carries it.

- **Degradation spec** — the plain-node-is-valid superset rule, and how a reader or tool treats a node with no ID and no scaffolding block.

- **Incubator `map.md`** — a small starting subtree of the incubator's own map, authored in the new format: exercising IDs, name-anchored nav links, and at least one degraded plain node.

**Done when** the format is documented and the incubator's `map.md` exists as a small, navigable subtree written in it — at least one node carrying an ID scaffolding block, nav links resolving by name, and at least one plain (degraded) node.

## Log

- Authored `NODE-FORMAT.md` (spec) and created `map.md` with the root node `a3k` in the new format. Corrected an earlier overstatement: name-anchored nav links still need re-pointing on rename; the ID protects *identity* (approval/drift), not navigation.
- Dogfooding surfaced a concern: the root's `[!IMPORTANT]` callout is doing TODO/provisional duty, overloading one callout with two meanings. User chose organic process over literal scope — capturing "standardise a callout set (split provisional/TODO marker out of IMPORTANT)" as a `Callouts (TODO)` node under Node, for a later change, rather than solving it here.
- Authored the subtree: **Specification** (`sp1`) → **Node** (`nd1`) → **Callouts** (TODO), plus **Change-Management** as a plain degraded node (no scaffolding block). Done-when now met: format documented, map is a navigable subtree, three ID-bearing nodes, name-anchored nav links resolving, and one degraded plain node.

## Conclusion

Completed. The format (`NODE-FORMAT.md`) and a dogfooded `map.md` subtree exist, exercising IDs, name-anchored nav, and degradation.

Two deviations of note: (1) an earlier overstatement was corrected mid-build — name-anchored nav links still need re-pointing on rename; the ID protects identity, not navigation. (2) Dogfooding surfaced the overloaded `[!IMPORTANT]`-as-TODO smell; rather than expand scope, it's parked in the map as **Callouts (TODO)** under Node — the seed of the next change.

Docs created: `NODE-FORMAT.md`, `map.md`.
