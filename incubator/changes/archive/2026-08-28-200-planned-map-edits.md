# Planned map edits during build

## Intent

*Build (u6k)* tells the agent to work through an approved plan without pausing step by step; the *Engagement Rule (n3g)* forbids map edits made in bulk and demands per-node negotiation. Any worklist carrying a map edit sets the two against each other — a restructuring change in an ordinary project as much as this repo, where the map is the product and every task is a map edit. The method should say which governs, and when.

Cadence: Formal.

### Context

Surfaced during change 180's build: six nodes were edited in one pass on the strength of an approved worklist naming each. The user noticed the missing per-node negotiation and declined a replay, but the rule conflict stands.

Where a change only touches code, the *Sync Rule (s5y)* keeps the two apart: map catch-up waits for Conclude and runs as its own per-node negotiation. The conflict appears as soon as map edits are planned work rather than catch-up — occasionally in an ordinary project, on every change in this one.

## Approach

- **The Engagement Rule wins: a task that edits the map is still negotiated node by node.** Build's "without pausing step by step" is about not seeking permission for routine execution, not a licence to bypass a rule stated elsewhere; saying so in one sentence in [Build](#build) resolves the conflict without new machinery.

- **Suggest [Explore](#cadences) for changes that touch nodes.** A task checklist invites a march through it, while topics with a *done-when* are shaped for working an area with the user — which is what per-node negotiation is. Guidance, not a constraint: a small mechanical map change is still fine as Formal.

- **No marking scheme, no per-task exemptions.** The alternative — labelling which tasks need a comprehension check — grows the worklist and re-litigates each task's weight at plan time, buying little over the rule simply applying.

## Worklist

- [x] State in [Build](#build) that a task editing the map is negotiated per node under the [Engagement Rule](#engagement-rule), which the no-pausing instruction does not override.
- [x] Add guidance to [Cadences](#cadences) that a change touching map nodes suits [Explore](#cadences).
- [x] Trim [Build](#build) back under its growth, dropping the **Feedback** block in favour of the [Log](#build) recording a reopened plan.
- [x] Retarget [Startup Scan](#startup-scan)'s hand-back recognition from Feedback to the Log.
- [x] Cut duplication from [Startup Scan](#startup-scan) and [Cadences](#cadences) already carried by [Plan](#plan) and [Build](#build).

## Log

- The Build sentence folded into the existing "interrupts only when something warrants it" list rather than standing alone, at the user's suggestion.
- Node counts after the edits: Build 1448 (was 1364), Cadences 1156 (was 1031) — both already on the 190 backlog, flagged not trimmed.
- Scope grew at the user's request: Build's size was dealt with here rather than left to 190. The user proposed the trim directly; Feedback went with it as needless machinery, taking Build from 1448 to 1093.
- Dropped with it: the explicit stop-and-record-the-blocker instruction, judged still implied by "follows the plan rather than improvising".
- Trimming spread from Build to its neighbours: Startup Scan 1038 to 902 (the Plan degrees it restated), Cadences 1156 to 916 (mid-flight cadence change and Wander renaming, both covered elsewhere).

## Conclusion

[Build](#build) now names a map-editing task among the things that interrupt it, negotiated per node under the [Engagement Rule](#engagement-rule), and [Cadences](#cadences) points map-node work at Explore. The **Feedback** block went as needless machinery: a reopened plan is recorded in the Log and rewritten, which [Startup Scan](#startup-scan) now reads instead. Trimming spread with it — Build 1448 to 1093, Startup Scan to 902, Cadences to 916, all by cutting what neighbouring nodes already said.
