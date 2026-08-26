# Enhancement discussion

Working notes for a discussion about potential enhancements to the COD process. Not yet a change proposal — capturing points, analysis, and open questions as we go. Radical changes and a possible new-repo spin-out are on the table.

> **Resume here (2026-08-03):** Discussion-only, no active change, nothing building. Five points captured (P1–P5). Synthesis reached a *keystone hypothesis*: give the map a node lifecycle (proposed → built → approved + drift). The **design fork is resolved** into a settled hybrid model — see "Resolved model — the hybrid". The three previously-open items are now **decided** (see "Resolved directions" at the bottom): **incubate here, spin out to a new repo later** (new name TBD); **stable node IDs are in** (needs a node-structure definition); **a plan is next, with graceful degradation for simple projects as a first-class concern**. Next step: shape that plan. User prefers conversational options over multiple-choice dialogs.

## Points raised

### P1 — Map has an all-or-nothing starting cost

**Friction:** Starting a map feels like you must map the *entire* system before it's valid, so the task gets deferred indefinitely. Blank-page problem.

**Analysis:** The current guidance describes a finished tree (root + children, TODO markers, tree overview) but doesn't strongly bless a partial, one-node start as a legitimate first state. `MAP-GUIDANCE.md` mentions `(TODO)` for unmapped nodes, which *technically* supports incremental growth, but the framing throughout implies a complete decomposition. Nothing tells a user "map the one node you're touching today and stop." The perceived unit of work is the tree, not the node.

**Possible directions:** (a) an explicit "seed the map" ritual — first map action is a single node for the area in hand; (b) reframe the map as grown edge-first from wherever work happens, TODO stubs everywhere else; (c) a startup nudge that offers to seed a map from the current change rather than demanding a whole one.

### P2 — Stakeholder engagement and per-node sign-off

**Friction:** Getting stakeholders to engage and formally sign off is hard. Idea: walk them through just one or two nodes during routine meetings rather than a big-bang review. But that needs bookkeeping — which nodes a stakeholder has approved, and which have changed since they last looked.

**Analysis:** COD today treats the *user* as the map's owner/maintainer, with the agent flagging inconsistencies. It has no notion of external stakeholders, approval state, or drift-since-review. This is a genuinely new axis: per-node review metadata (who, when, at what version) plus change detection against that baseline. Sits naturally with the map's node granularity — approval is per-node, matching the "one node at a time" engagement rule already in MAP-GUIDANCE.

**Tensions / questions to hold:** where does approval state live (in the node? a sidecar ledger? git?); how is "changed since last approval" computed (git blame/hash of node region vs a stored snapshot); does this stay lightweight or become a heavyweight review system; multiple stakeholders each with their own approval frontier.

### P3 — Browser-based viewer to maximise stakeholder engagement

**Friction:** The map is the primary documentation/specification artefact, and maximising stakeholder engagement with it matters. Markdown is pleasant for devs but a hard sell for non-devs to read. Imagining a simple browser-based viewer: eases navigation, renders views of node contents, lets stakeholders flag nodes as inaccurate or leave comments for later review. Counter-pressure: must not add friction for devs working primarily in a terminal (multiplexer + editor).

**Analysis:** This is the delivery surface for P2's engagement/sign-off. Key design constraint: the markdown files stay the source of truth; the viewer is a *read-optimised projection* plus a feedback capture channel — it must not fork the artefact or force devs off the CLI. The node/link format (H1 + Up/Down anchors) is already a clean tree the tool can parse and render as navigable UI. Flags/comments are the same data as P2's review metadata, so P2 and P3 likely share one substrate (per-node annotations living beside the markdown, mergeable via git).

**Tensions / questions to hold:** viewer as pure read + annotate vs. edit; where annotations persist so both CLI and browser see them; whether this pulls COD from "a methodology + markdown convention" toward "a methodology + tooling", which is a bigger scope shift (and a candidate reason to spin out a new repo/tool); keeping the tool optional so CLI-only teams lose nothing.

### P4 — Is COD two separable things intertwined?

**Observation:** COD may actually be two core things: (1) a **change-management process** for developing code with agents (plan/build modes, gates, change documents, modes, changelog), and (2) a **hierarchical approach to specification and documentation** (the map — nodes, links, sizing, sync/engagement rules). Question: is it right that they are so intertwined?

**Analysis:** These two do largely live in separate files already — `PROCESS.md` + `KEYWORDS.md` for the process, `MAP-GUIDANCE.md` for the map — but they're coupled at the seams: the process repeatedly defers to the map as "primary frame of reference", Build's map-catch-up, Approach reads the map, Conclusion flags map impact. The map is usable without the change process (just a doc convention); the change process references the map but could run against any documentation. So they're separable in principle, coupled by convention in practice.

**Why it matters for this discussion:** P1 (starting the map) is purely a *map* concern. P2/P3 (stakeholder sign-off + viewer) are *map* concerns too — they attach to the specification artefact, not the change process. So three of four points so far live on the **map/specification** side. That's evidence the map is the part with the most untapped potential, and a candidate to become its own thing (own repo, own tool, own vocabulary) with the change-management process as a separate, optional consumer of it.

**Tensions / questions to hold:** if split, what's the clean interface between them (the process needs to *reference* map nodes and know when they're stale); does splitting lose the "maintaining the map is the thinking" thesis that currently binds them; two repos vs one repo two modules; naming.

### P5 — Fold intent/approach into the map instead of archived change docs

**Observation:** The effort spent capturing Intent and Approach in change documents feels under-repaid — they get archived and rarely re-read. Alternative: express intent and approach *as map updates directly*, doing change-planning and map-documentation in one act. The map becomes a tool for both **specifying intent** (what we want) and **documenting reality** (what we have). No obvious low-complexity way to do this in plain markdown; may require moving beyond simple markdown, at which point the viewing tools (browser + CLI) become critical rather than optional.

**Analysis:** This directly collides with two current pillars:
- The **Sync rule** in MAP-GUIDANCE: "the map describes what exists, not what is proposed" — map edits describing pending work defer to Build. P5 wants the map to hold *proposed* state too. So it needs a way to mark a node (or a node-delta) as "intended, not yet built", i.e. a temporal/status dimension the map currently forbids.
- The change document as the home of Intent/Approach. P5 relocates that content onto/beside the node it concerns, so it lives where it's discoverable later instead of in an archive.

**Relationship to P4:** Not actually opposite so much as orthogonal. P4 asks "are process and map separable?" P5 asks "should the *artefacts* of the process live in the map?" You can have a separated map tool that natively models proposed-vs-actual node state (P5), consumed by a thin change process (P4). The map gaining a proposed/actual axis is what would let intent live in it without turning into mush.

**Tensions / questions to hold:** how to represent proposed vs actual without the map becoming a tangle (per-node status? a diff/overlay layer? draft nodes?); does folding intent into nodes lose the narrative "why" that Approach captures across several nodes at once; if intent lives in the map, what (if anything) is left of the change document; this is the strongest driver yet toward richer-than-markdown storage + real tooling.

### P6 — Optional post-change checklist at Conclude

**Observation:** A change lifecycle could support an *optional* project-supplied checklist (e.g. `changes/CHECKLIST.md`) that the agent walks at the Completing/Conclude stage — run the tests, update the changelog, verify a project invariant. If the file exists the agent runs it and reports; if not, nothing happens. A pointer that may or may not exist, degrading silently — in keeping with graceful degradation for simple projects.

**Provenance:** Surfaced while planning 125 (suggested standards), as a way to make "run the installer test" unforgettable. Judged out of proportion to that single risk, so parked here rather than built. Revisit only if a real recurring need appears.

## Open questions

These are the decisions that will shape any plan. Deferred from the per-point discussion:

- **The keystone question:** do we introduce a proposed-vs-actual (lifecycle) axis to the map? Nearly every point leans on it. If yes, the Sync rule is generalised/retired and plain markdown is likely outgrown.
- **Split or fuse?** P4 (separate map from process) vs P5 (fold process artefacts into map). Resolved provisionally as *orthogonal*: a richer standalone map artefact can serve a thin change process. Needs confirming.
- **How far past markdown?** Stay markdown + sidecar metadata, or move to a structured store with markdown as a projection? Determines whether tooling (P3 viewer, CLI) is optional or load-bearing.
- **Same repo or new repo?** A lifecycle-aware map + viewer is arguably a different product from "COD the agent methodology". Spin-out vs evolve-in-place.
- **Does the founding thesis survive?** "Maintaining the map is the structural thinking." A tool-heavy, lifecycle-aware map risks turning map-tending into data-entry. Must be actively protected whichever way we go.

## Emerging directions

**One keystone hypothesis:** the five points reduce largely to one capability — give the map a **node lifecycle** (proposed → built → approved, plus drift-since-approval). With that:

- P1 (starting) — a node can exist in a lightweight "proposed/stub" state, lowering the cost of the first node.
- P2 (sign-off) — approval is a lifecycle state per node per stakeholder; drift is computed against the approved baseline.
- P3 (viewer) — the browser/CLI tools exist to render and act on lifecycle state (navigate, approve, flag, comment).
- P5 (intent in the map) — "intent" is just the proposed state of a node; "documentation" is its actual state. Change docs shrink or dissolve.
- P4 (separation) — the lifecycle-aware map becomes a standalone artefact/tool; the agent change-process becomes a thin consumer that references nodes and reads their state.

**Candidate shape:** a new artefact — a lifecycle-aware conceptual map (structured store, markdown as one projection) with browser + CLI viewers — likely its own repo, of which the current COD change-process is one client. Current COD continues to exist for the plan/build cadence, slimmed to lean on the new map rather than re-implement documentation.

**What to protect:** the comprehension thesis — tooling must keep map-tending a thinking act, not form-filling.

## Design fork — where does lifecycle state live?

Two candidate models for representing proposed/actual/approved (raised by user; tooling ease is a stated deciding factor):

**Option A — per-node lifecycle.** Each node carries its own state (proposed → built → approved) and its own drift/approval metadata. Fine-grained.

- *Strengths:* matches the existing "one node at a time" engagement + sign-off rhythm (P2); a stakeholder approves nodes independently; drift is localised; partial maps are natural (P1) since a lone proposed node is just a node in one state.
- *Weaknesses:* many small states to track and render; "what does the whole thing look like as-proposed vs as-built" requires assembling per-node states; intent that spans several nodes (an Approach's cross-cutting "why") has no single home.
- *TUI/GUI:* viewer is a tree where each node shows a status badge; approve/flag acts on the focused node. Straightforward to render; the hard part is surfacing *cross-node* proposed changes coherently.

**Option B — whole-map versions.** The map as a whole has versions/snapshots; a proposed change is a new version of the (relevant part of the) map, reviewed and approved as a unit, then becomes the actual.

- *Strengths:* a coherent "here is the world as proposed" vs "as it is" — a single diff between two whole-map versions captures intent as an Approach naturally would (P5); approval of a version is a clean gate; matches how change docs currently bundle an intent.
- *Weaknesses:* coarse — stakeholders may want to approve one node, not a whole version; drift/approval frontier per stakeholder is awkward if approval is version-global; large maps make whole-version review heavy (re-introduces the P1/P2 all-at-once problem this discussion is trying to escape).
- *TUI/GUI:* viewer is a version switcher + diff view (proposed version vs current). Diffing two trees is a well-trodden UI (like a PR). Arguably the *easiest* compelling GUI to build, because "review this diff" is a familiar interaction.

**Hybrid worth considering:** whole-map (or subtree) *versions* as the unit of proposal and diff (Option B's clean intent + PR-like review), but *approval recorded per node* within that version (Option A's per-node sign-off frontier). Intent lives as a version-diff; sign-off and drift live per node. This may be the sweet spot for both P2 and P5, at the cost of more model complexity.

**Deciding factor to resolve:** which model yields the more effective, buildable TUI/GUI — a per-node status tree (A) vs a version/diff review surface (B). Leaning: B's diff-review is the more familiar and compelling GUI, but A's per-node approval is what stakeholder sign-off (P2) actually wants. Hybrid reconciles them.

> **Resolved (2026-07-31):** The fork settled on the hybrid, developed in detail below. The key realisation was that build-state and approval-state are *two orthogonal axes*, not one lifecycle — which lets B's diff-review serve proposals while A's per-node sign-off serves stakeholders, with no conflict.

## Resolved model — the hybrid

The five points reduce to giving the map two orthogonal axes: a **build-state** axis (is this node reality yet?) and an **approval-state** axis (has a stakeholder signed off, and has it drifted since?). Keeping them separate is what makes the hybrid coherent — the earlier A-vs-B tension came from treating "lifecycle" as a single dimension.

### Build-state is *location*, not a status field

The main map is **reality-only**: every node in it is built. There is no `proposed`/`accepted` status stamped on nodes, because those states are expressed by *where the node lives*, not by metadata:

- `proposed` — the node exists only in a **proposal artefact** (a branch, or a proposals dir), still under discussion.
- `accepted` — the proposal is approved but not yet merged (code pending).
- `built` — merged into the main map.

The Sync rule ("the map describes what exists, not what is proposed") is thus enforced *structurally*: the main map physically cannot hold un-built content because un-built content isn't in it. This keeps the main map — and proposals — as **plain markdown**; the difference between them is just a diff. The "richer than markdown" pressure drops away for this axis entirely.

A **proposal artefact** is, at minimum, an **intent document + a proposed map** (the changed subtree). It fuses today's change document with the map-slice it proposes. On merge, the node-deltas land in main; the cross-cutting intent/approach prose is what gets archived or distilled into nodes — which is where P5's "intent lives in the map" resolves *without* smearing narrative across nodes, because the narrative lives on the changeset, not the nodes.

This gives the dev/agent review surface for free: reviewing a proposal **is a PR-like diff** (map-as-it-reads-now vs as-it-would-read). That was Option B's most compelling GUI, kept without B's coarseness.

### Approval-state is an in-node per-approver stamp

Stakeholder sign-off (P2) is a *separate* axis acting on the **main map**, asynchronously, a few nodes at a time in routine meetings — never via the proposal PR-diff. It lives as a small **in-node metadata block**: a list of `person + timestamp` stamps (agent-maintained scaffolding, like the nav links — kept out of the user's prose; the viewer can collapse it).

- **A list gives independent per-stakeholder frontiers.** Each entry is one person's own last-approved point, so drift and the "what changed" diff are computed per-person against their own baseline. Single-frontier is just the degenerate one-entry case.
- **No separate ledger.** Because the stamps live *in the node*, there's no sidecar artefact to maintain — and moving/renaming a node carries its approval state along automatically (the sidecar would have lost that thread).

### Drift is computed; "what changed" is derived via optional git

- **Drift** is *computed on demand*, never stored: a node reads as due for a stakeholder when its current content differs from what they approved. Archiving/merging **writes nothing** to approval state — it simply changes node content, which automatically makes the node fall into the due-queues of everyone whose stamp predates the change. Merge-to-main is what passively dirties the approval frontier; the two mechanisms meet at that one clean seam.

- **The stakeholder surface is a due-queue, not a diff.** They read each due node *as it is now* and re-approve; "yes, that's right" updates their timestamp to current. A per-node, *personal* retrospective diff ("what changed in this node since **your** last approval") is an optional aid — distinct from the global proposal PR-diff, since each stakeholder's baseline differs.

- **The retrospective diff is derived, not stored.** At display time the GUI resolves a stakeholder's approval **timestamp → the commit that last touched the node at/before then**, fetches that version, and diffs against current. Nothing is written at invalidation; the fetch-point is an ephemeral git query keyed off the stored timestamp. (Store a full timestamp, not just a date, so a same-day edit is unambiguous.)

- **Git is load-bearing in exactly one place** — resolving "last approved version" for the retrospective diff — and it degrades gracefully: no git → no retrospective diff, everything else (build-state-as-location, drift detection, due-queues) still works. If date→commit resolution ever feels too fuzzy, the fallback is to store the commit at approval time (one extra token), deferrable for now.

### Why the node-sizing rule matters here

Per-node re-approval is only humane because nodes are already capped small (~800 chars): a "due" node is a re-read of one short node, not a document review. The P2 sign-off rhythm and the existing node-sizing discipline reinforce each other.

### Model summary

- **build-state = location** (main map vs proposal artefact)
- **approval-state = an in-node list of `person + timestamp` stamps** (independent frontiers, no separate ledger)
- **drift = computed** (current content vs the version at the approval timestamp)
- **"what changed" diff = derived via optional git** at display time

### Resolved directions (2026-08-03)

- **Incubate here, spin out later.** This is an evolution of COD, so it grows in this repo for now. It is expected to become its own repo once the shape settles, and will need a **new name** at that point. Treat "COD" as the working name only.
- **Stable node IDs are in.** Nodes will carry a stable identity so approval stamps and drift baselines survive renames — accepting the small step past plain markdown. This requires **defining a node structure** (identity + the in-node scaffolding blocks the model already needs). That definition is now a work item, not an open question.
- **A plan is needed next**, and it must treat **graceful degradation** as a first-class concern: a simpler project must be able to adopt this without heavy boilerplate. The lifecycle/approval/ID machinery should be opt-in and near-invisible until wanted, so small maps stay plain markdown.

### Still open

- **The new name** — deferred until the shape settles.
- **Node structure specifics** — exact form of the stable ID and in-node metadata blocks. To be settled while shaping the plan.

## Proposed decomposition

The keystone (a lifecycle-aware map) breaks into a dependency-ordered sequence of changes. Node structure is the foundation everything else stamps onto, so it comes first; the viewer consumes everything, so it comes last. **Graceful degradation is a cross-cutting constraint on every change**, not a change of its own — each piece must stay invisible on a plain map that doesn't want it.

1. **Node structure & identity** — define the node: what gives it durable identity (stable ID) and what scaffolding blocks it can carry, with the degenerate no-ID case staying plain markdown. Foundation for all that follows.

2. **Build-state as location** — the proposal artefact (intent + proposed map subtree), the reality-only main map, and the merge seam. Establishes how proposed vs built is expressed structurally.

3. **Approval mechanics** — per-node approval stamps, computed drift, and the per-stakeholder due-queue. Depends on node structure.

4. **Retrospective diff (git-backed)** — the optional "what changed since your last approval" aid. Depends on approval stamps; degrades to nothing without git.

5. **Viewer (browser + CLI)** — renders lifecycle state and drives navigate/approve/flag. Consumes everything above; a separate, later effort.

First change to shape: **Node structure & identity** (`node-structure.md`).
