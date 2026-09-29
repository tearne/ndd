# Introducing Discussion

**Cadence:** Formal

## Intent

Introduce Discussion as a new NDD artefact — a durable home for unfinished thinking that precedes an Intent — plus the mechanics to operate it alongside changes.

## Context

Split on 2026-09-29 from earlier `340-change-formality.md`. Approach rename and Formal specification moved to `030-approaches-discussion.md`; Unresolved at any stage built as change 010 (archived 2026-09-29). Direction was developed through prior discussion after retiring the forest proposal (see `changes/archive/2026-09-29-forest.md`). Sections below record the target state that fed the Approach.

## Approach

- **Add a Discussion subtree under Change-Management**, peer to Change Lifecycle. Discussion is a distinct work artefact with its own lifecycle — no plan parts, no Build lock — so giving it its own subtree keeps its rules from bleeding into change rules.

- **Three new nodes: Discussion, Discussion Records, Discussion Conclude.** Discussion for the concept and when to open one; Records for content rules (no imposed structure, prune freely, dead-end and resurfacing retention, Resume anchor on pause); Conclude for the either-party trigger, ~500-char capped prose, promote-or-drop of noted candidates, filename rename and archival.

- **Edit Aside Keyword** to describe content-routing: an aside becomes an append to an existing Discussion, a new parked change, or a new Discussion; overlap with an existing change is named but not attached. Placement confirmed in one line.

- **Edit Startup Scan** to read Discussions alongside changes, distinguish them by `-discussion.md` filename suffix, and announce "discussing" as a session mode co-existent with planning or building.

- **Edit Backlog Review** to walk Discussions and changes together, surfacing on a Discussion its current agreements, open questions and any inline candidates.

- **AGENT-RULES.md**: expand Rule 1 (Startup Scan) with the "discussing" mode; rewrite Rule 15 (Aside) for content routing.

- **No changes to Plan, Intent, Context, Held, Approach, Worklist, Build or Conclude on the change side** — Discussion runs alongside changes without altering their internal machinery.

## Worklist

- Add `Discussion` node under `Change-Management`.
- Add `Discussion Records` node under `Discussion`.
- Add `Discussion Conclude` node under `Discussion`.
- Update `Aside Keyword` node for content-based routing.
- Update `Startup Scan` node for Discussions and the discussing mode.
- Update `Backlog Review` node to walk Discussions and changes.
- Update the map's TOC and `Change-Management` nav to include the Discussion subtree.
- Update AGENT-RULES.md Rule 1 for the discussing mode.
- Update AGENT-RULES.md Rule 15 for aside content-routing.

## Conclude

Completed. Mid-build casing sweep normalised `discussion` to lowercase in prose (capitalised only as node names) across touched nodes. Three asides emerged and were parked: 040 (write ≠ approval discipline), 050 (present node edits as diffs), 060 (surface one thing at a time).

## Discussion records

Discussion documents replace the proposed forest (retired 2026-09-29). They give unfinished thinking a durable home: discussions remain resumable, threads can change without losing ideas or return points, and partial thoughts can inform related concepts without becoming commitments.

A Discussion can begin with a provisional title and a thought, without a settled Intent or approach. It is not a special Exploratory mode or a fifth implementation approach. The user owns the concepts; the agent flags meaningful connections and discusses uncertain or consequential relationships before settling them.

The record is kept concise. No fixed structure is imposed: the agent maintains a current-state record in whatever prose shape fits the topic. It prunes and rewrites freely; git history holds the deep archive, and past reasoning is retained only where its loss would risk revisiting a dead-end. On pause, a **Resume** anchor is left with return points and a pointer to current thinking; the anchor is trimmed on resumption.

Candidate changes noted in a Discussion live inline in the record. Each carries enough context to develop its own Intent and links back. Promotion is a distinct step: the user takes a candidate forward and it becomes a new parked change with an Intent only — no file exists at the noted stage. A Discussion is not concluded with candidates still open; at Conclude each is promoted or dropped, alongside any understanding or decision reached.

Use ordinary links between discussions and resulting work. Split when a subject needs independent attention, preserving its motivation. Needing more than roughly 300 characters to explain an outcome prompts a scope check, not an automatic split. No explicit conceptual forest or stable-ID system is required.

The agent guides gently and tracks focus and return points. On `stack`, show only a terse numbered list, current topic first with higher numbers indicating deeper context. No standing footer.

## Handover

Either party may propose a change. The agent drafts an Intent for user approval, with rationale in Context. Each change must be understandable without reconstructing its source discussion. Approach selection can happen earlier or emerge as the change develops. Readiness implies neither urgency nor authorization.

Discussion records organize thinking; change documents hold agreed Intents, plans and execution details. Avoid duplicating authoritative accounts. Ordinary links preserve origin when a discussion yields several changes or several discussions inform one change.

## Aside routing

`aside:` routes by content. The agent scans open Discussions and changes for overlap, then: appends to an existing Discussion when the aside continues that thread; otherwise opens a new parked change with Intent only if the aside is Intent-shaped; otherwise opens a new Discussion record. Placement is confirmed in one line. Overlap noticed with an existing change is named in the confirmation without attaching, so the change's owner can fold it in on resumption. The agent picks; capture is the priority and miscategorising is cheap.

## Discussion conclusion and archival

A Discussion's Conclude is triggered by either party: the agent detects nearing-conclusion and suggests, or the user indicates. The agent then drafts a short Conclude prose — capped at about 500 characters, counted and reported when surfaced — stating what the Discussion produced (understanding, decisions, and any promoted candidates with links to their new parked changes), what was dropped, and any ideas worth flagging for later resurfacing. The user approves the Conclude before archiving. Flagged resurfacing ideas survive any later pruning, alongside dead-end retentions.

Discussion filenames use a readable form ending in `-discussion.md`, for example `change-process-discussion.md`. On Conclude the file is prefixed with the ISO date and moved to the same `changes/archive/` folder used for concluded changes — for example `2026-09-27-change-process-discussion.md`. Links are updated on rename. Existing numbered Discussions in `changes/open/` keep their filenames pending reconciliation.

## Startup and review integration

The Startup Scan reads every file in `changes/open/`, distinguishing Discussions (filename ending `-discussion.md`) from changes on the file list before reading contents. For each Discussion it notes topic, any candidates pending inside, and whether the Discussion looks nearing-Conclude; for each change it places the lifecycle position as today. The scan announces the session's mode — planning, building or discussing — in any combination, since the Build Lock covers project files rather than attention.

Backlog Review walks Discussions and changes together, one at a time. On a Discussion, it surfaces current agreements, open questions and any noted candidates alongside their readiness for promotion. No separate Discussion Review is needed. Map Review is unchanged and applies only to changes touching the map, at their own Conclude.

## Integration

Preserve substantive approval, the implementation build lock and current-map truthfulness. Adapt entry before Intent, capture permission, startup/review and archival for Discussion records. Process feedback remains unchanged. The stable three-character ID requirement is dropped; existing numbered files remain unchanged pending reconciliation.

## Resume here

This is an active Discussion. Agreements above are settled but not yet in the live method. Related work: `010-unresolved-at-any-stage.md` (small change, Intent parked) and `030-approaches-discussion.md` (companion Discussion). The retired forest.md and its harvested W6D live in `changes/archive/` under 2026-09-29 dates.
