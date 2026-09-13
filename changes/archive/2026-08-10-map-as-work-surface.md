# Map as work surface

**Mode:** Explore

## Intent

Capturing future intent should be frictionless and belong to the map's world — TODOs and ideas seen in the context of the concept they touch, not parked in a disconnected side-doc. Today such thoughts break flow or go to `aside:`, detached from the map. This change makes capture map-native: a passing thought lands anchored to the map node it concerns and surfaces there, so the map is the primary artefact getting primary engagement. Captured intent comes in kinds — concrete TODOs versus ideas to weigh later — and capture respects that distinction.

## Approach

### Seeds are anchored to nodes, stored with change-management, not inline on the map

A captured thought becomes a **seed** — kind, an anchor to a map node's stable ID, and text — held in the change-management store, not written into `map.md`. Inline markers would pile non-reality onto the reality-only main map; since every open proposal carries a copy of the subtree it builds toward, on-map markers would drift from those copies and reconcile as noise at merge. Storing seeds beside change-management keeps the main map a clean diff against any proposal.

### A seed is the embryonic head of a change document

A seed is one file in the change store — the minimal head of a change document: kind, an anchor, and a line of text. It matures **in place**, growing to carry the intent and the copied map nodes that form the change's spec (build-state-as-location's proposed subtree). No separate seed store, no move: capture and proposal are one lineage, so there is one funnel and one place to look. The single source of change management is the change store; the map surfaces what is anchored to it.

### Surfaced through the map, in context

Because the anchor is a node ID, the startup scan and a future viewer report a node's pending seeds when you navigate there — contextual, map-native engagement even though the bytes sit in the change store. Anchoring by ID rather than name keeps a seed bound across renames and moves.

### Kinds are a field, not a node type

`kind: todo | idea` on the seed — concrete work versus backlog to weigh later. No new node types, no map markers. Priority is left out of this cut.

### Capture reuses `aside:`

`aside:` creates a seed anchored to the nearest relevant node; the agent proposes the anchor from active context and the user confirms in a line. When no home is obvious, the anchor falls back to the nearest existing ancestor, else the root. `process:` stays separate.

### Documentation is the incubator's own edited copies of COD's core docs

For the method to stand alone once the incubator is adopted without COD scaffolding, the docs the agent relies on are brought into the incubator as first-class **edited copies** — an agent-instructions doc plus `PROCESS`, `KEYWORDS`, and `MAP-GUIDANCE` — rather than bespoke files that reference the pinned snapshot. Seeds are woven through them: capture into `KEYWORDS`, maturation into `PROCESS`, anchoring and placement into `MAP-GUIDANCE`, the seed-aware scan into the agent-instructions doc. `MAP-GUIDANCE` absorbs the incubator's evolved node format (identity, scaffolding block, degradation) as a single map doc — no separate node-format file. `CLAUDE.md` is repointed from the pinned snapshot to `AGENT.md`, so the incubator now runs on its own method (dogfooding).

## Plan

**Topics**

- **Seed anatomy and maturation** — the seed's fields (kind `todo|idea`, a node-ID anchor, text), its identity as the minimal head of a change document in `changes/open/`, and its in-place growth into a full change (intent + copied spec nodes). Lands in `PROCESS`.

- **Capture via `aside:`** — the gesture producing a seed: anchor proposed from active context, confirmed in a line, with the ancestor→root fallback; the in-proposal-aside branch and `process:` preserved. Lands in `KEYWORDS`.

- **Anchoring, placement, and degradation** — node-ID anchor, nearest-node placement, invisible on a plain map, and graceful fallback when a node has no ID. Lands in `MAP-GUIDANCE`.

- **Seed-aware startup scan** — anchored seeds surfaced in context alongside open changes, grouped by the node they hang off. Lands in the agent-instructions doc.

- **Bring in and reconcile the core docs** — `PROCESS`, `KEYWORDS`, `MAP-GUIDANCE`, and the agent-instructions doc established as self-standing edited incubator copies; `MAP-GUIDANCE` absorbs the evolved node format as a single map doc (no separate node-format file); the two bespoke files (`AGENT.md` scan-only, `SEED-GUIDANCE.md`) folded into their homes and `SEED-GUIDANCE.md` removed.

**Done when** the incubator carries `PROCESS`, `KEYWORDS`, `MAP-GUIDANCE`, and an agent-instructions doc as self-standing edited copies with seeds woven through, no references to the pinned snapshot, `MAP-GUIDANCE` carrying the node format as a single map doc, `SEED-GUIDANCE.md` folded away — with the live `agent/` tree and pinned snapshot untouched.

## Log

- Cross-referencing against the pinned `KEYWORDS.md` caught that `aside:` has two branches (new proposal / in-proposal aside); the seed model replaces only the new-proposal branch, so the in-proposal aside is preserved rather than dropped.
- Seeds live in `changes/open/` as embryonic change documents, so the seed-aware scan finds them where the pinned scan already looks; maturation is in-place growth with no move.
- Review feedback: reframed both docs to stand on their own rather than as a delta over the pinned snapshot, since the incubator will be adopted without that scaffolding. AGENT.md now specifies the full startup scan self-contained; the pinned snapshot was used only as a completeness check during authoring.
- Scope grew (user-approved): brought PROCESS/KEYWORDS/MAP-GUIDANCE into the incubator as self-standing edited copies and promoted AGENT.md to the full agent-instructions doc; SEED-GUIDANCE.md dissolved into their proper homes (capture→KEYWORDS, maturation→PROCESS, anchoring/placement/degradation→MAP-GUIDANCE, scan→AGENT).
- MAP-GUIDANCE reconciled with NODE-FORMAT: node-format example now carries the scaffolding `id` block (four-backtick outer fence) and defers anatomy to NODE-FORMAT.md.
- PROCESS deliberately does NOT import build-state-as-location (that's a later change); seed maturation is described as growing into a normal change document, with the anchor keeping it located — keeping PROCESS self-consistent.
- STYLE.md not brought in (not needed for seeds); CLAUDE.md left pointing at the pinned snapshot (dogfooding is a separate change). AGENT.md @-imports PROCESS/MAP-GUIDANCE/KEYWORDS/NODE-FORMAT, ready to wire when dogfooded.
- Review feedback: dropped the "incubator method" framing and the "not switched on yet" callout from AGENT.md — the docs are written as live, definitive agent guidance. Incubation/dogfooding status lives in this change doc, not in the guidance itself.
- Dogfooding folded into this change (user-directed): repointed CLAUDE.md from the pinned snapshot README to @AGENT.md, so the incubator now loads its own method (AGENT.md → PROCESS/MAP-GUIDANCE/KEYWORDS/NODE-FORMAT). STYLE.md is not imported (not brought in), so coding-style guidance is not loaded — acceptable for a docs method repo, revisit if needed.
- Consolidated (user-directed): NODE-FORMAT.md's overlap with MAP-GUIDANCE was too much for two docs; merged its anatomy, identity, navigation, and degradation into MAP-GUIDANCE as a single map doc and deleted NODE-FORMAT.md. Dropped @NODE-FORMAT from AGENT.md's imports; repointed map.md's Node See-also at MAP-GUIDANCE.md.

## Conclusion

The method now stands on its own: the incubator carries edited `AGENT`, `PROCESS`, `KEYWORDS`, and `MAP-GUIDANCE` copies with seeds woven through, `CLAUDE.md` loads `@AGENT.md`, and the pinned snapshot is history rather than scaffolding.

Two deviations from the plan, both user-directed and logged: dogfooding (the `CLAUDE.md` repoint) was folded in, and `NODE-FORMAT.md` was dissolved into `MAP-GUIDANCE.md` so the map format lives in one doc.

Deferred: `map.md` is thoroughly stale against the new method — the Change-Management node and the node-format nodes no longer match the docs. Rather than a piecemeal catch-up, this is handed to a successor change that explores expressing the method predominantly in the map, leaving a minimal markdown shell that directs the agent to read it — true dogfooding.

(No changelog in the incubator, so no entry.)
