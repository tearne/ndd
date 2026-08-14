# Map build-out

**Mode:** Explore

## Intent

The method should describe itself in the map, not in the process docs beside it. `BOOTSTRAP.md` already hands the agent to the map as authoritative; now the map has to earn that — carrying the lifecycle, gates, seeds, and map conventions currently held in `AGENT.md`, `PROCESS.md`, `KEYWORDS.md`, and `MAP-GUIDANCE.md` as nodes. Only when the map holds the method can `CLAUDE.md` point at `BOOTSTRAP.md` and the incubator run on its own method for real — the dogfooding this whole line of work has been building toward. Two open questions ride along: where the method map lives so it doesn't collide with a client's own domain map, and how the map is split across files so agent traversal stays cheap.

## Approach

### Grow the existing three-concern tree

The docs map cleanly onto the tree already there: the **Specification** subtree absorbs the map conventions (`MAP-GUIDANCE`), the **Change-Management** subtree absorbs the process and keywords (`PROCESS`, `KEYWORDS`, and `AGENT`'s rules and startup scan), and **Tooling** stays minimal. No new top-level structure — the map already decomposes the way the method does.

### Concept in prose, precision in Detail, then delete the doc

Each node carries the concept in its prose and the mechanics in a **Detail** section; the source doc is deleted once its content fully lives in nodes. A single source is the whole point — leaving parallel docs recreates the drift this line of work exists to remove.

### Migration is a stale catch-up, done per node

Moving existing reality (the docs) into the map is a catch-up, not a proposal, so it is negotiated one node at a time and is exempt from the Build lifecycle. What this change enacts through the lifecycle is the surrounding mutation: deleting the docs and repointing `CLAUDE.md`.

### Stub the whole tree in one pass; author content one node at a time

The skeleton — every method node as a heading with a scaffolding `id`, nav links, and a `(TODO)` marker — is laid down in a single structural pass. Prose and Detail are then filled strictly per node, each negotiated. Structure is agent-maintained; content is the user's.

### Map stays at the project root; single file

`map.md` stays at the incubator root — here the method *is* the project, so there is no domain map to collide with (the consumer packaging under `changes/agent/` is a separate concern, not enacted here). It stays a single file until size forces a split, keeping agent traversal one read.

### Go live last

Once the map holds the method and the docs are gone, `CLAUDE.md` is repointed from `AGENT.md` to `BOOTSTRAP.md` — the incubator then runs on its own method.


## Plan

**Topics**

- Stub the method tree in one structural pass — every method node under Specification and Change-Management as a heading with a scaffolding `id`, nav links, and a `(TODO)` marker.

- Migrate the map conventions into the Specification subtree, one node at a time, concept in prose and mechanics in Detail.

- Migrate the process and keywords into the Change-Management subtree, one node at a time, concept in prose and mechanics in Detail.

- Delete each of `MAP-GUIDANCE.md`, `PROCESS.md`, `KEYWORDS.md`, and `AGENT.md` once its content lives in nodes.

- Repoint `CLAUDE.md` from `AGENT.md` to `BOOTSTRAP.md`.

**Done when** the map carries the method — map conventions, process, and keywords as nodes — the four process docs are deleted, and `CLAUDE.md` loads `BOOTSTRAP.md`, so the incubator runs on its own method.

## Log

- Incubator itself carries no changelog (only packaged consumer copies under `changes/agent/`), so no version bump on entering Build.
- Structural pass laid down: 23 stub nodes added to `map.md` (Specification and Change-Management subtrees plus a `Tooling` stub), each with a scaffolding `id`, nav links, and `(TODO)`. Existing authored nodes (root, Specification, Node, Change-Management) kept as-is; their child nav links and the root tree overview updated. `Change-Management` deliberately still carries no `id` (degradation demo preserved).
- Proceeded with proposed defaults for the three open decomposition questions (Seeds under Change-Management; version-update/changes-dirs folded into prose; granularity as proposed) — user approved the tree as a starting point, to refine while engaging.

- **Degradation node dropped.** While authoring the Specification subtree, the whole-map plain-markdown opt-out lost its rationale: the agent adds nav + scaffolding cheaply on review, so there's no user burden to protect against (the user need only supply tree structure, which the map requires anyway). Removed the `Degradation` stub (was `d2m`). The "user may omit while drafting, agent proposes on review" rule survives inside `Node Identity` (and will be echoed in `Navigation Links`). Ripples caught up: `Node` prose (dropped the identity paragraph now owned by `Node Identity`, reframed the superset line as a rendering/compat fact) and `Change-Management` (given `id: cm4`, dropped its no-scaffolding degradation-demo paragraph).
- Seed captured (`idea`, anchor `b3q`): nav links don't signal parent-vs-sibling at a glance — `nav-shows-hierarchy.md`.
- **Resume point (2026-08-12):** Build active (`active.md` → this change). Specification-subtree authoring in progress. Done: `Node Identity`, `Navigation Links`; caught up `Node` and `Change-Management` (gained `id: cm4`); removed the `Degradation` node. Next `(TODO)` nodes: `Node Sections` (+ `Callouts`), `Map Structure`, `Node Sizing`, `Content Principles`, `Map Maintenance`, then the whole Change-Management subtree. Node lengths healthy (root 1029 as overview; `Node Identity` 842 and `Navigation Links` 872 marginally over ~800 but single-concept, overage in skimmable Detail — left as-is). Docs not yet deleted; `CLAUDE.md` not yet repointed. Open seed: `nav-shows-hierarchy.md` (`idea`, anchor `b3q`).

- **Specification subtree complete (2026-08-13).** Authored `Node Sections` (`s8r`) + `Callouts` (`c5k`), `Map Structure` (`m6x`), `Node Sizing` (`z9p`), and `Map Maintenance` (`t7v`). `Content Principles` was split under our own Node-Sizing rule into a framing parent renamed **`Writing Style`** (`p4h`) with two children: `Conceptual Writing` (`h3v`) and `Formatting` (`f2n`); `Specification` child link and tree overview updated to match. Every Specification `(TODO)` is now cleared.

- **Writing conventions being accumulated.** New running seed `map-writing-conventions.md` (`todo`, anchor `f2n`) holds two settled preferences — flowing sentences over mid-sentence dash/parenthetical breaks; italics for section/element references, bold for term-of-art introduction — to distil into `Formatting` later and apply on a rescan.

- **Three seeds captured this session:** `quick-jump-to-tree.md` (`idea`, `m6x`) — stable name-independent anchor to reach the tree overview; `contents-and-rationale.md` (`idea`, `m6x`) — split the root into a `Contents` node (tree + jump target) and a `Rationale` sub-node; `agent-maintenance-actions.md` (`idea`, `t7v`) — gather recurring agent upkeep (box-drawing sync, metadata consistency, char counts, style) into a dedicated node, and consider rehoming inline upkeep detail (e.g. `Node Sizing`'s "agent flags it") there with a See-also left behind.

- **Resume point (2026-08-13, parked):** Build still active. Specification subtree done. Next up: the **Change-Management subtree** — draft `Modes` (`e3n`) first, then `Change Lifecycle` (`l5g`) + its five children (`Intent`, `Approach`, `Plan`, `Build`, `Conclusion`), `Seeds`, `Startup Scan`, `Gates and Permissions`, `Keywords` + `Process Keyword`/`Aside Keyword`. After the subtree: delete the four migrated docs and repoint `CLAUDE.md` from `AGENT.md` to `BOOTSTRAP.md`. Open seeds listed above.

- **Change-Management subtree in progress (2026-08-14).** Authored `Modes` (`e3n`), `Change Lifecycle` (`l5g`), and the stage nodes `Intent` (`i8b`), `Approach` (`a2r`), `Plan` (`p9d`), `Build` (`u6k`). Two seeds captured this session: `child-node-ordering.md` (`idea`, `m6x`) — whether child-listing order carries meaning, governed per-parent; and a formatting convention appended to `map-writing-conventions.md` (`f2n`) — two blank lines before a node title.
- **Stage nodes regrouped under two working postures.** User spotted that the five lifecycle stages aren't homogeneous — Intent/Approach/Plan/Conclusion are document sections, Build is an activity phase. Restructured (option b): `Change Lifecycle` now parents `Plan mode` (`v3d`, new) holding Intent/Approach/Plan, and `Build mode` (renamed from `Build`, kept id `u6k`) holding the execution content and parenting Conclusion. `Change Lifecycle`'s own prose left for a later trim pass — if it has little left to say once the two postures carry the content, fold them up into it.
- **Recurring slip:** stub-authoring edits kept swallowing the *next* node's `#` heading because `old_str` anchored on it (hit on Approach, Plan, Build). Fix going forward: don't include the following heading in edit anchors.

- **Seeds collapsed into a parked Intent; anchoring dropped (2026-08-14).** A method revision riding along on the transcription, decided with the user after stepping back to the big picture. Node anchoring added nothing toward the "change ≈ map maintenance" goal (that payoff belongs to the future *build-state-as-location* keystone), so seeds, the `Kind` (todo/idea) taxonomy, and anchoring are all dropped for now. A "seed" is now just a change captured at its [Intent](#intent) and parked in `changes/open/` until picked up — maturing is simply resuming the lifecycle. The `Intent` node gained a parked-change paragraph (an Intent may *optionally* reference nodes as *name (id)* — name to navigate, id to survive rename); the `Seeds` node (`s3w`) was deleted, dropping `Change-Management` to five children and updating its child links + the tree. `Node Identity` (`w9c`) needs no change — its "anything pointing to the node stays attached" is generic and the optional Intent reference is now its live example. Pending: `Aside Keyword` authored for the new model; existing files in `changes/open/` carry now-obsolete `Kind:`/`Anchor:` heads (backlog cleanup, deferred).

- **BOOTSTRAP startup pointer added early.** Though part of go-live, added a "First action each session" section to `BOOTSTRAP.md` pointing the agent straight at the `Startup Scan` node so it needn't traverse the whole map on cold start. Prose reference (name-coupled, breaks on rename of that node — cheap to fix).
