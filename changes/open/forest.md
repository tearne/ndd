# Discussion forest

Superseded on 2026-09-27: Discussion documents replace this proposed forest; stable IDs are no longer required. Retained as reference only. The current direction and resumption point are in [the consolidated discussion](340-change-formality.md). Earlier agreements and open items below must be read in that light; W6D remains parked pending scope review.

Working forest for the discussion captured in [340-change-formality.md](340-change-formality.md). Created at the user's request to use the proposed process before implementing it. This representation is provisional; it does not amend the method or authorize Build. Existing unrelated changes have not been migrated.

The proposal is the reviewed baseline. These summaries hold conceptual context; plans and execution details belong in harvested change documents. The first harvest is [W6D: Forest-backed discussion](W6D_forest-backed-discussion.md), with an approved Intent and no Build authorization.

## Reading the forest

Each concept has a stable three-character ID. In the relationship list, `child parent broader-concept` describes current organization, `concept origin source` records provenance, and `concept linked other` records a symmetric association. Parent and origin are independent. Grouping follows the overview discussed with the user; implementation boundaries remain undecided.

## Conversation stack

Historical stack retired. Resume from [the consolidated discussion](340-change-formality.md#resume-here).

## Relationships

```text
d4s parent r8k
h6v parent r8k
a2p parent r8k
f7n parent r8k
c3u parent d4s
n5t parent d4s
s8b parent d4s
i6h parent h6v
v4r parent h6v
t9q parent a2p
v7e parent a2p
e3x parent a2p
f2m parent a2p
j5a parent f7n
d4s origin r8k
h6v origin r8k
a2p origin r8k
f7n origin r8k
c3u origin r8k
n5t origin r8k
s8b origin r8k
i6h origin r8k
v4r origin r8k
t9q origin r8k
v7e origin r8k
e3x origin r8k
f2m origin r8k
j5a origin r8k
s8b linked v4r
i6h linked a2p
n5t linked f7n
f2m linked j5a
q8u origin e3x
q8u linked f7n
q8u linked d4s
```

Origins record that these concepts were extracted from the same discussion, not that they were independently discussed under their present parents. Cross-links connect splitting to harvesting, Intent to approach selection, navigation to storage, and specification assets to archival. They express discussed connections, not new dependencies.

## r8k — Change lifecycle

Purpose: allow unfinished thinking to develop freely, then hand coherent work into user-reviewed changes with suitable approaches. The forest supports resumption after interruption, switching threads without losing context, and connections between emerging and earlier ideas.

Working agreement: capture -> review and harvest -> agree Intent -> develop work and agree an approach -> proceed on approval -> review and accept. Clear tasks can move quickly; discussion can finish without a build. Existing execution safeguards remain where they fit.

Source: [reviewed proposal](340-change-formality.md). Open: divide implementation after forest review. Writing this forest is authorized; implementing the method is not.

## d4s — Developing thoughts

Seeds remain in the forest until coherent work warrants a change document. Summaries preserve useful uncertainty, reasoning and agreements rather than transcripts. Thoughts need not become commitments; the agent guides gently without forcing progression.

## c3u — Capture and concept ownership

The agent maintains compact summaries automatically; the user owns concepts and relationships. Separate suggestions from agreements. Flag significant connections, overlaps and tensions; discuss uncertain or consequential associations before settling them. Preserve discarded directions only when their reasons constrain future choices.

Open: how to keep summaries fresh without losing unresolved material. The current file is a first working representation, not a settled schema.

## n5t — Conversation navigation

Maintain focus and return points across interruptions. Use judgment to offer tangents, parking or a return without pushing. No standing footer. `stack` displays only a terse numbered list, current topic first, with higher numbers showing deeper context.

Open: refine persisted stack behaviour through use, including what happens when a parked thread becomes independent.

## s8b — Splitting and connections

Split when work needs independence or substantial thinking needs its own space. Agree which part to pursue and preserve motivation. An outcome needing more than roughly 300 characters to explain prompts a scope check, not an automatic split. Do not make a change for every topic.

Connection: review may harvest several concepts together or several changes from one concept. Hierarchy need not dictate delivery boundaries.

## h6v — Turning thoughts into work

Review brings a coherent outcome forward into an Intent. Forest maintenance is administrative; the resulting change is a user-reviewed agreement. Readiness is distinct from priority and authorization.

## v4r — Reporting, review and harvesting

Show a short conceptual hierarchy, expanding selected concepts into agreements, rationale, boundaries, links and open questions. Show cross-links separately. Harvest primarily during review: recommend outcomes, explain readiness and consequential gaps, and let the user choose. Direct clear requests need not await a review meeting.

Retain source concepts, unresolved thinking and links to resulting work. A source is not automatically completed by harvesting.

Open: review invocation details. The first handoff is [W6D](W6D_forest-backed-discussion.md); remaining harvest candidates are unselected.

## i6h — Intent handover

Either party may propose work. The agent drafts a clear Intent for approval, with rationale in Context. The change must make sense without reading the forest. Document creation and approach selection need not coincide.

Open: exact content transfer and links; avoid duplicated authoritative accounts. Whether exploration later continues in place or produces another change remains undecided.

## a2p — Approaches

Trivial, Vibe, Exploratory and Formal replace the existing cadences. Recommend a fitting approach with a simple question as understanding develops; the user may accept or keep refining. These are opportunities to proceed, not a mandatory ladder. The agent proposes parameters rather than making the user anticipate every constraint.

Approved preparation sections after Intent:

| Approach | Sections |
|---|---|
| Trivial | None |
| Vibe | Bounds |
| Exploratory | Focus |
| Formal | Specification; optional Implementation Plan |

Build log and Conclude remain. These names replace the need for a generic Approach planning section in the proposed structure; method integration is not yet implemented.

## t9q — Trivial

Virtually no substantive ambiguity remains. The agent judges suitability and proposes it. Routine implementation choices remain delegated. Size alone is not decisive: a large mechanical edit can be Trivial, while a small bug may hide a design question.

The approved Intent is the whole plan; no separate planning sections or written check are required. The agent performs proportionate verification during the work and reports the result. Raise verification beforehand only where consequential uncertainty warrants it, potentially indicating another approach is needed. This supersedes the earlier suggestion to separately agree a check. Build still requires authorization.

Surface consequential ambiguity rather than silently expand discretion. A quick answer may preserve Trivial; substantial design decisions may require another approach. Intent alone is the plan, not the entire record: the Build log, Conclude, user acceptance and archival rules remain, as they do for Vibe.

Connection: Vibe deliberately delegates design decisions.

## v7e — Vibe

After Intent, agree Bounds: a short statement of delegated discretion, consequential boundaries and when to return for review. The agent uses judgment to propose these from context rather than burdening the user with inventing them or enumerating routine decisions. No detailed task checklist is implied by this agreement; exact integration with existing Plan sections remains open.

Continue while the agreement holds; return to discussion when it does not. A bounded spike can provide learning but does not automatically become an accepted implementation. Retain the Build log, Conclude, user acceptance and archival rules.

## e3x — Exploratory

After Intent, the agent proposes a conceptual focus and a useful point to take stock, such as comparing specification formats and reviewing whether a recommendation is possible. No predetermined answer is required. Record this agreement in Focus. Understanding, a decision or a handoff can be a complete outcome. A coded spike requires deliberate authorization.

Do not require an Exploratory change merely to maintain or discuss the forest: capture precedes choosing work and its approach.

## q8u — Discussion-only Explore instead of forest machinery?

User-raised alternative, unresolved and held for later: could an Explore change simply support talking things through and clarifying a vision, then archive like any other change? It might absorb some forest functions or replace the forest. Concern: the forest may introduce too much boilerplate. Examine whether ordinary discussion changes can preserve low-friction entry, resumability and useful connections with less administration. No decision to replace the forest or resume W6D.

## f2m — Formal specification

After Intent and choosing Formal, develop and approve Specification before authorizing Build and taking the lock. Keep specification work with the change and its assets; check against intervening project changes before Build.

Once the specification is agreed, the agent may propose an Implementation Plan section when consequential delivery choices or sequencing warrant it. Agree those choices before Build. If the specification suffices, no additional section is required; the agent still plans routine execution and obtains explicit Build authorization.

Use a map, sub-map, whole-map copy, table, flow diagram or prose. Independent agents should agree on required behaviours and constraints; delegated implementation details may differ. The approved target stays distinct from verified reality, and the project map ultimately describes the built result.

If specification stalls, propose conceptual exploration, a Vibe spike or smaller scope. Prefer a single change file; use a same-name asset folder when useful.

Open: specification approval granularity and verification into the live map. Specification inside a locked Build was explicitly superseded.

## f7n — Forest administration and method integration

Use stable IDs and parent/origin/linked relationships; preserve completed ancestry. Startup recovers current context and active work. Aside capture becomes a seed; review distinguishes seeds from defined changes. Process feedback stays unchanged. The implementation build lock and current-map truthfulness remain.

Open: settle representation after use, migrate existing records, and revise current rules for automatic capture and entry before Intent. Markdown with typed relationship pairs is the provisional choice used here.

## j5a — Identity and archival

Three-character alphanumeric IDs survive renaming, document creation and archival. Example: `k7m_change-formality.md` -> `2026-09-25_k7m_change-formality.md`. No extra prefix; forest ordering is separate from identity.

Require acceptance and account for outstanding threads before concluding. Seeds can conclude without waiting for descendants; retain motivation for later reconsideration. Review supporting assets at archival, keeping useful evidence and removing disposable experiments.

Open: allocation and migration, completed-seed treatment, asset cleanup details. Trying uppercase change identifiers: `W6D_forest-backed-discussion.md`. The legacy proposal filename and forest concept IDs are unchanged.

## Harvested work

[W6D: Forest-backed discussion](W6D_forest-backed-discussion.md) draws from d4s, h6v and f7n. Intent approved; further planning and implementation deferred at the user’s request. Its scope ends at Intent handover; approach and Formal redesign remain separate. Summaries must preserve only history needed to understand current thinking. Source concepts remain available for further development.

## Harvest candidates for review

These are agent suggestions, not selected changes or approved Intents.

| Candidate | Concepts | Readiness and remaining choice |
|---|---|---|
| Replace cadences with approaches | a2p | Distinctions are clear; exact Plan parts and the existing Approach section name need resolution. |
| Support specification before implementation | f2m | Sequence and safeguards are clear; approval and verification details need definition alongside Formal's Plan parts. |
| Preserve identity through archival | j5a | Filename convention is agreed; allocation, migration and completed-seed handling remain. |

Formal specification overlaps the approach candidate; combine them if that yields a more coherent change. Identity may belong with forest integration. Candidates do not require separate files until selected.
