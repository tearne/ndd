# Change formality

## Status and purpose

Discussion proposal, not an approved implementation plan. The method remains unchanged and Build is not authorized.

Provide a common entry for developing thoughts, a clear handover into user-reviewed changes, and approaches ranging from unambiguous tasks to specification-led implementation.

## Discussion records

Discussion documents replace the proposed forest. They give unfinished thinking a durable home: discussions remain resumable, threads can change without losing ideas or return points, and partial thoughts can inform related concepts without becoming commitments.

A Discussion can begin with a provisional title and a thought, without a settled Intent or approach. It is not a special Exploratory mode or a fifth implementation approach. The agent maintains concise agreements, options, open questions, return points and essential reasoning. The user owns the concepts; flag meaningful connections and discuss uncertain or consequential relationships before settling them.

Discussion can conclude with understanding, a decision, or any number of change seeds, including none. Seeds carry enough context to develop their own Intent and link back to their source; the discussion need not remain open until resulting work finishes. Where seeds live without creating excessive stub files remains open.

Use ordinary links between discussions and resulting work. Split when a subject needs independent attention, preserving its motivation. Needing more than roughly 300 characters to explain an outcome prompts a scope check, not an automatic split. No explicit conceptual forest or stable-ID system is required.

The agent guides gently and tracks focus and return points. On `stack`, show only a terse numbered list, current topic first with higher numbers indicating deeper context. No standing footer.

## Review and handover

During review, summarize the discussion and recommend coherent work worth pursuing, explaining readiness and consequential gaps. The user selects what to take forward. Clear requests need not wait for a separate review.

Either party may propose a change. The agent drafts an Intent for user approval, with rationale in Context. Each change must be understandable without reconstructing its source discussion. Approach selection can happen earlier or emerge as the change develops. Readiness implies neither urgency nor authorization.

Discussion records organize thinking; change documents hold agreed Intents, plans and execution details. Avoid duplicating authoritative accounts. Ordinary links preserve origin when a discussion yields several changes or several discussions inform one change.

## Approaches

Approach replaces Cadence as the term for Trivial, Vibe, Exploratory and Formal. As understanding develops, the agent proposes a fitting approach with a simple question. The user can accept or keep refining; the approaches are not a mandatory ladder.

| Approach | Meaning and agreement |
|---|---|
| Trivial | Intent is the whole plan. Virtually no substantive ambiguity; routine implementation choices remain delegated. The agent verifies proportionately during work and reports results. Surface consequential ambiguity if it emerges. |
| Vibe | After Intent, agree Bounds: agent-proposed discretion, consequential boundaries and review points. |
| Exploratory | After Intent, agree Focus: the conceptual question and a useful point to take stock. Coding a spike requires separate authorization. |
| Formal | After Intent, agree Specification, then an optional Implementation Plan when consequential delivery decisions warrant it. |

The agent proposes parameters from context rather than requiring users to anticipate every constraint. Trivial selection and agreement may fit one short exchange. Readiness does not authorize work.

## Formal specification

Agree Intent -> choose Formal -> develop and approve the specification -> authorize Build and take the lock -> implement -> verify and conclude.

Once Specification is agreed, the agent may propose an Implementation Plan for consequential delivery choices or sequencing. If none is needed, no extra section is required. Build still needs explicit authorization.

Specification development stays with the change and its assets, without locking project assets. Before proposing Build, check it against current reality and surface revisions required by intervening work.

Use a map, sub-map, whole-map copy, table, flow diagram or prose as appropriate. Independent agents should be able to implement the same required behaviours and constraints; delegated implementation details may differ.

Keep the approved target separate from the current project map until verified. Whatever the specification format, the map must describe the completed result. Prefer one change file; use a same-name companion folder for supporting assets when warranted. At archival, retain useful evidence and rationale and remove disposable experiments.

If specification stalls, identify the uncertainty and propose conceptual exploration, a Vibe spike or smaller scope. A spike supplies learning, not automatic acceptance as the final implementation.

## Execution, completion and identity

Retain existing execution and completion rules where they suffice. Return to discussion when the agreement no longer fits, preserving completed work. Account for outstanding threads and require user acceptance before concluding, including Trivial work.

Discussions can conclude through understanding, decisions or handoff without waiting for resulting changes to finish. Preserve motivation for reconsideration if resulting work collapses or diverges.

Use readable filenames, for example `change-process-discussion.md` and `2026-09-27-change-process-discussion.md` after archival. Update links when renaming or archiving. The stable three-character ID requirement is dropped; existing files remain unchanged pending reconciliation. Build log and Conclude remain for every work approach, including Trivial.

## Integration and remaining decisions

Preserve substantive approval, the implementation build lock and current-map truthfulness. Adapt entry before Intent, approach definitions and Plan parts, capture permission, startup/review and archival for Discussion records. Process feedback remains unchanged. Approved section names are Bounds, Focus, Specification and optional Implementation Plan; Trivial has no second planning section.

Remaining decisions:

- Where spawned seeds live and how they develop into changes without excessive stub files.
- Minimal Discussion structure, completion/archival procedure, and startup, aside and review integration.
- Detailed target-specification approval, verification into the current map and supporting-asset cleanup.
- Reconcile W6D with the replacement direction before further work; its approved forest Intent is not silently rewritten.

## Resume here

Discussion documents replace the forest proposal; stable IDs are no longer required. The earlier [forest trial](forest.md) is retained as superseded reference, not the current organizational system. W6D remains parked pending scope review. Approach definitions and Formal can still proceed separately. No method implementation or Build is authorized, and no files have been renamed or archived.

### Handoff — 2026-09-29

Paused at the user's request. Read this document first: it is the current consolidated direction. The forest trial contains earlier, superseded proposals and must not be treated as current instructions. The live method in `ndd.map.md` and `AGENT-RULES.md` has not been edited; discussion approval is not implementation approval.

The last decision was to replace the forest with ordinary Discussion documents and drop stable IDs. Discussion is separate from Exploratory: it may begin before Intent and conclude by spawning zero or more seeds of any approach. Approach preparation is agreed: Trivial uses Intent alone; Vibe adds Bounds; Exploratory adds Focus; Formal adds Specification and optionally Implementation Plan. Build log and Conclude remain. Formal specification precedes Build authorization and its lock.

Suggested next discussion, not an agreed task: settle the smallest useful Discussion record and where its resulting seeds live. Then decide whether to revise or retire [W6D](W6D_forest-backed-discussion.md); do not restart its forest implementation. Approach/Formal work can be harvested separately once desired. No further implementation change has been created.

Return points:

3. Discussion records and seed handoff.
2. Review the relevance of parked W6D.
1. Harvest approach/Formal changes when ready.

Keep records concise, omitting non-critical history. Offer next steps gently; show the stack only on request. Existing files retain their names for now. The three discussion artifacts are this file, `forest.md` (superseded reference) and `W6D_forest-backed-discussion.md` (parked Intent); unrelated open changes are untouched.
