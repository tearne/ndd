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

## Log

- Topic 3 started. [Change-Management](#change-management) now introduces the `changes/` layout (finding 11): a change is one markdown file in `changes/open/`, archived to `changes/archive/` under an ISO date prefix, with `changes/open/active.md` named as the lock. Its *Detail* also settles change naming, which the map had never mentioned — two to five hyphenated words, an optional leading number for queue sequencing, both freely renameable while open and the number dropped on archiving.
- Two clauses were cut from that body en route: "updates the map as reality catches up" (the same standing catch-up prompt topic 2 deleted from Conclude) and "explicit user gates", which became **user-owned gates** to match [Gates and Permissions](#gates-and-permissions). The node now stands at 687, close to the bound.
- Six existing archive files still carry their numbers; left as they are by agreement rather than renamed.

- Topic 1 done. The map-edit permission is now a named **map exemption**, defined once in [Edit Governance](#edit-governance) and referenced by Change Lifecycle, Plan, Gates and Permissions and `BOOTSTRAP.md` — the restatements that let them drift are gone.
- Catch-up timing settled by deletion rather than reconciliation: Conclude lost its catch-up paragraph (the actual source of the routine prompting) and the Sync Rule shrank to its one essential sentence, 400 characters to 122. A bulleted draft was rejected en route for implying every change should plan map edits.
- Topic 2 done, and it grew a structural change rather than staying a wording pass: [Map Maintenance](#map-maintenance) now defines a single trigger — once a change is archived — and splits its children by cost. *Conceptual Drift* became [Judgement Scan](#judgement-scan) (id `d4p` kept), taking the two judgement bullets that were misfiled under Consistency Upkeep.
- The mechanical review is now an act, not a duty: it fixes and reports the tree overview and missing ids or links, reports a table of oversize nodes, and escalates what a fix can't settle. Seven stale *See also* and Detail pointers were repaired to match.
- Judgement Scan stands at 884, over the bound, with the user's explicit approval — the misc-bucket prohibition was judged worth the overage.
- Node counting gained a visible-text rule for inline links, so every count reported before this point in the session was inflated; the 190 backlog needs remeasuring.
- **Paused 2026-09-02 with the lock held.** Topics 1 and 2 are done and their map edits are in place; topic 3 (missing mechanics) is untouched. Findings 1-8 are resolved, 9-12 remain, plus finding 13 raised mid-build. Resume at topic 3, whose first item was mid-proposal: give [Change-Management](#change-management) a body sentence defining the `changes/` layout — one markdown file in `changes/open/` while in play, moved to `changes/archive/` on completion with a date prefix, and `changes/open/active.md` as the build lock — since `open/` and `archive/` are currently never introduced anywhere. Then the remaining three: the taking of the lock (finding 10), the `## Context` section defined against Held (9), and user-authored map edits arriving mid-build (12).
- Finding 10 (taking the lock) forced a split rather than a wording fix: [Build](#build)'s *Detail* had grown three unrelated topics and stood at 1141. The lock became its own child node, [Build Lock](#build-lock) (`b7n`), stating the act — write the change file name into `active.md` and report it, or stop if it already exists — plus release and the changed-code rule. Build fell to 809, at the bound; Build Lock is 470.
- Knock-ons: tree overview gained the node, and the Contents line for Change-Management now says "user-owned gates". [Gates and Permissions](#gates-and-permissions) and [Change-Management](#change-management) still name `active.md` bare and could link Build Lock instead — not yet done.
- Finding 12 (user edits mid-build) settled in [Engagement Rule](#engagement-rule) rather than Build: the rule binds the agent, not the user, and the agent's response to a user edit is the same act it owes for its own — re-read, recount, report knock-ons — logged only when it changes what the build must do. Node 270 to 564.
- Finding 9 done: the unnamed Intent subsection became [Context](#context) (`c7d`, 530), a section of the change document in its own right rather than nested inside the Intent, and the node states the distinction that was missing — Context is durable and travels to the archive, [Held](#held) is transient and must be empty by Conclude. Intent lost the vague sentence and sits at 1100, still well over the bound and left for the 190 backlog.
- Intent was over the bound at 1100 and came down to 539 in one pass: the Held pointer left its *Detail*, the cap paragraph was tightened without losing the count-and-report act, and the parked-Intent paragraph went entirely — parking is a property of a change at any degree of formation, which [Plan](#plan) already states, not an Intent feature. The optional *name (id)* node reference went with it, unused so far, taking a sentence of [Aside Keyword](#aside-keyword) too.
- "Parked Intent" became "parked change" in Conclude, Startup Scan, Gates and Permissions and Aside Keyword, following that reasoning.
- Plan's children reordered to reading order — Intent, Context, Held, Approach, Worklist — in the links, the document and the tree overview. Context took a brevity rule: the least that lets a later reader rediscover the detail, never a retelling.
- User rewrote [Plan](#plan) (812 to 627), prompting a real question: the parts list names Intent, Approach and Worklist but not the two new sections. Kept as is and made explicit instead — parts are the gated, cadence-governed sequence, while Context and Held are ungated sections named in a following sentence. Plan now 790.
- Finding 13 root-caused rather than noted: both symptoms — editing without waiting, and prose never checked against the guide — come from rules that describe a property of the output instead of a step in the agent's loop. [Engagement Rule](#engagement-rule) now states the order (draft, check against [Writing Style](#writing-style), surface with the count, write only on [approval](#gates-and-permissions)), which is the same shape [Node Sizing](#node-sizing) already uses. 564 to 679.
- Two follow-ups deliberately left open: whether change-document prose gets the same style check, and whether mechanical fixes under the map exemption deserve a lighter path than the full order.
- The edit order gained an exit for trivia: a correction that changes no meaning is applied and reported rather than surfaced, matching [Consistency Upkeep](#consistency-upkeep)'s fixed-then-reported split. Paid for by cutting the now-overlapping "batched confirmation when it's mechanical" clause. Engagement Rule 780.
- Declined deliberately: applying the same style check to change documents. The stage gates already surface every part for approval, so a second checking machine would be ceremony on top of a working gate.
- Held released and deleted — all 13 findings landed in the map, with outcomes recorded above.
- Final review pass found four leftovers of the same class. Judgement Scan's "should also apply the ambiguity test" became "also applies"; Bootstrapping stopped scaffolding vague "missing pieces" and names the `changes/` tree; the Engagement Rule's character count now links [Node Sizing](#node-sizing) rather than restating it.
- The fourth was an ownership error the user caught: Conclude pointing up at Change-Management for the archive convention, when the parent should give the shape and the child the mechanics. Fixing it exposed Conclude at 1254, so it split — the Wander paragraph went to [Cadences](#cadences) (which the user accepted at 1014, over the bound), the duplicated cap sentence folded into the body, and the post-approval machinery became [Archiving](#archiving) (`a9v`, 454). Conclude 750, Change-Management 504.
- Finding 13 recurred twice after its own fix landed — a batch applied without surfacing, and a decision-approval read as prose-approval. Root cause is one level out from this change: the map is consulted, `BOOTSTRAP.md` is always loaded, and the rules that must fire live in the former. Parked as `220-where-rules-live.md` rather than bolted on here.
- No changelog entry: the method is unreleased at 1.0.0, so no bump was agreed and the dated 1.0.0 section would be misstated by folding this in.

## Conclusion

Landed in `map.md`. Change-Management now defines the `changes/` layout and change naming; three nodes are new — Build Lock, Context and Archiving — and the Engagement Rule states an edit order in which waiting and the style check are acts. Intent fell 1100 to 539 and Conclude 1254 to 750 to pay for it.

Bootstrapping (1015) and Cadences (1014) are left over the bound for the 190 backlog. Finding 13 recurred during the pass and is parked as its own change on where enforceable instructions live.
