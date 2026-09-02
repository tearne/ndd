# Instructions that agents actually follow

## Intent

The method is written for an agent to act on, but too much of it can be satisfied by doing nothing: rules with no trigger, obligations with no observable act, and in places two nodes that say opposite things. Change 180 fixed this for the numeric limits; the same defect runs through the rest of the map. Every instruction should name who does what, when — or be dropped.

Cadence: Explore.

## Approach

- **Group the work by kind — contradictions, triggerless rules, missing mechanics — while still landing each node edit one at a time.** The twelve findings are three defects wearing different clothes, and a fix that reads well node-by-node can still leave a pair contradicting; the grouping is how the work is ordered, not a licence to edit in bulk.

- **Every obligation names an act the agent performs and something it says out loud.** Compliance that leaves no trace is indistinguishable from skipping it; this is the test each rewrite must pass.

- **Where a rule has no honest trigger, delete it rather than invent one.** "Used sparingly" and "asked freely" may be guidance a reader values and an agent cannot act on; adding a fake moment would be worse than dropping the line.

- **Settle the two contradictions by deciding which node is right, then cutting the loser's claim.** Restating a rule in a second node is how they drifted apart; the loser should point rather than repeat.

- **Keep the no-active-change exemption for reality-reflecting map edits, and make the stricter nodes defer to it.** The exemption is what stops routine upkeep needing ceremony; the contradiction is in the other nodes stating an absolute they don't mean.

- **Stop treating map catch-up as a routine part of Conclude.** A change that means to edit the map plans those edits; one that doesn't should not end with the agent hunting for map work, which is how Conclude turned into a standing prompt for it.

- **Include `BOOTSTRAP.md` in the map-edit contradiction.** It is the first thing an agent reads and currently states the stricter rule, so leaving it out would settle the map and not the behaviour.

- **Give the change document a `## Context` section of its own, after the Intent rather than nested inside it, and say what separates it from [Held](#held).** The Intent stays one quick paragraph, with background as a peer section rather than an overflow bin hanging off the part it dilutes. Both take material that isn't the Intent, so the distinction has to be stated: Context is durable and survives to the archive, Held is transient and must be empty by Conclude.

### Unresolved

*(empty)*

## Topics

- **Contradictions** — reconcile the map-edit permission across [Change Lifecycle](#change-lifecycle), [Plan](#plan), [Gates and Permissions](#gates-and-permissions), [Edit Governance](#edit-governance) and `BOOTSTRAP.md`; and settle map-catch-up timing between the [Sync Rule](#sync-rule) and [Conclude](#conclude).

- **Triggerless rules** — give a real trigger and a spoken act to [Node Sizing](#node-sizing), [Node Identity](#node-identity), [Conceptual Drift](#conceptual-drift) and the two soft bullets in [Consistency Upkeep](#consistency-upkeep); drop the unenforceable phrasing in [Cross-Agent Falsifiability](#cross-agent-falsifiability) and [Callouts](#callouts).

- **Missing mechanics** — introduce the `changes/` layout and the taking of the `active.md` lock; define the `## Context` section against [Held](#held); account for user-authored map edits arriving mid-build.

**Done when** every finding in Held is either fixed in the map or recorded as deliberately declined, and no instruction touched in the pass can be satisfied without the agent doing or saying something.

## Held

Review findings from a full pass over the map (2026-08-28), to be worked into the Approach:

**Contradictions**

1. Map edits during Plan: *Change Lifecycle*, *Plan* and *Gates and Permissions* say project files are untouchable without an active build, while *Edit Governance* says reality-reflecting map edits may happen at any time — and `map.md` is a project file. The vendored `BOOTSTRAP.md` sides with the stricter reading.
2. Map catch-up timing: the *Sync Rule* says it waits until the change is concluded, then follows; *Conclude* says it happens within Conclude.

**Rules with no trigger**

3. *Node Sizing* counts "whenever the agent touches a node" — reading is touching; it means edits.
4. *Node Identity* offers a missing id "when it next reviews the node" — same undefined trigger.
5. *Conceptual Drift* says "watch for the signals" with no moment and nothing to report; *Map Maintenance* promises to say when a node is due for work, and neither child does.
6. *Consistency Upkeep*'s "hold prose to the writing style conventions" and "watch child order" name no observable act, unlike the size bullet beside them.
7. *Cross-Agent Falsifiability*'s ambiguity test is "asked freely" — nothing obliges it anywhere.
8. *Callouts*' "used sparingly" is unfalsifiable.

**Underspecified mechanics**

9. The Intent history subsection has no name and no defined boundary; this session invented `### Context`.
10. Nothing instructs the agent to create `active.md` — *Build* only says to stop if it exists.
11. `changes/open/` and `changes/archive/` are never introduced; *Bootstrapping* scaffolds "the missing pieces" without naming them.
12. No account of user-authored map edits arriving mid-build: who counts them, whether the Engagement Rule applies to the user's own edits, whether they are logged.

**Raised mid-build, to settle before Conclude**

13. Agent conduct this session: edits applied without waiting for explicit approval, and prose written without checking it against the writing-style guide. Recurring rather than one-off — needs root-causing, since it is the same class of problem as the map's own unenforceable rules.

Not in scope as findings: the tree overview was verified in step with all 48 headings.

## Log

- Topic 1 done. The map-edit permission is now a named **map exemption**, defined once in [Edit Governance](#edit-governance) and referenced by Change Lifecycle, Plan, Gates and Permissions and `BOOTSTRAP.md` — the restatements that let them drift are gone.
- Catch-up timing settled by deletion rather than reconciliation: Conclude lost its catch-up paragraph (the actual source of the routine prompting) and the Sync Rule shrank to its one essential sentence, 400 characters to 122. A bulleted draft was rejected en route for implying every change should plan map edits.
- Topic 2 done, and it grew a structural change rather than staying a wording pass: [Map Maintenance](#map-maintenance) now defines a single trigger — once a change is archived — and splits its children by cost. *Conceptual Drift* became [Judgement Scan](#judgement-scan) (id `d4p` kept), taking the two judgement bullets that were misfiled under Consistency Upkeep.
- The mechanical review is now an act, not a duty: it fixes and reports the tree overview and missing ids or links, reports a table of oversize nodes, and escalates what a fix can't settle. Seven stale *See also* and Detail pointers were repaired to match.
- Judgement Scan stands at 884, over the bound, with the user's explicit approval — the misc-bucket prohibition was judged worth the overage.
- Node counting gained a visible-text rule for inline links, so every count reported before this point in the session was inflated; the 190 backlog needs remeasuring.
- **Paused 2026-09-02 with the lock held.** Topics 1 and 2 are done and their map edits are in place; topic 3 (missing mechanics) is untouched. Findings 1-8 are resolved, 9-12 remain, plus finding 13 raised mid-build. Resume at topic 3, whose first item was mid-proposal: give [Change-Management](#change-management) a body sentence defining the `changes/` layout — one markdown file in `changes/open/` while in play, moved to `changes/archive/` on completion with a date prefix, and `changes/open/active.md` as the build lock — since `open/` and `archive/` are currently never introduced anywhere. Then the remaining three: the taking of the lock (finding 10), the `## Context` section defined against Held (9), and user-authored map edits arriving mid-build (12).
