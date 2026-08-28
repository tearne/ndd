# Within-change material held for its stage

**Mode:** Formal

## Intent

_(Approved 2026-08-28.)_

The `aside:` keyword dispatches two unlike things under one name: a genuinely **separate** proposal, parked as its own Intent, and material belonging to the **current** change but a later stage. In practice "aside" reads only as the former, so the latter is forgotten — both user and agent overlooked it while drafting change 160, hand-rolling a block instead. Split them: keep Asides for separate proposals, and give within-change material held for its stage a heading and name of its own, cap-exempt and settled as its stage arrives.

## Approach

**`aside:` becomes single-purpose** — always "park a separate proposal as its own Intent", losing the scope dispatch, the ask-if-unsure clause it required, and the Asides subsection it fed. Reason: a keyword meaning two things is remembered as whichever is commoner, which is how the within-change case went missing.

**Within-change material is called Held**, a `## Held` section in the change document. Reason: *parked* is already the method's word for the other half of the split, so reusing it would re-fuse the concepts; *held* implies custody with a release due.

**Held is a Detail paragraph in [Plan](#plan), not a node.** Reason: it is one section of one document, and `Plan` already owns the parts and their caps. Accepted cost: it sits a tier below [Aside Keyword](#aside-keyword), a sibling in spirit.

**It needs no keyword.** Reason: holding material is ordinary drafting by either party, continuous with the work, whereas a keyword implies a deliberate side-action.

**Released at each stage boundary; left-overs block completion.** Opening a new part, the agent folds in what now belongs; anything whose stage has passed surfaces in the pre-[Conclude](#conclude) sweep. Reason: material aimed at the Approach is worthless if it surfaces after the build, so an end-of-change sweep alone would defeat the purpose — it survives only as the net.

**[Intent](#intent) gains the consequence** — a clause saying it may stay high-level because early material now has a home. Reason: the cap reads today as a bare restriction, which is how bloated Intents keep happening.

## Worklist

- [x] Define **Held** as a Detail paragraph in [Plan](#plan): what it holds, cap-exempt, released at stage boundaries, left-overs blocking completion.
- [x] Narrow [Aside Keyword](#aside-keyword) to parking a separate proposal, dropping the scope dispatch, the ask-if-unsure clause, and the Asides subsection.
- [x] Update the [Keywords](#keywords) summary bullet for `aside:` to match.
- [x] Retarget [Conclude](#conclude)'s outstanding-aside check to Held.
- [x] Add the high-level-Intent clause to [Intent](#intent).

## Log

- **Held became its own node, reversing the Approach's Detail-in-Plan decision.** Adding the paragraph took `Plan` to 2,000 characters against a ~800 bound, and `Node Sizing`'s felt test — a node wanting sub-sections has outgrown one concept — applied plainly. Approved on that evidence.
- **Worklist was promoted to a node in the same move.** The parts were otherwise documented at two tiers: `Intent` and `Approach` as nodes, the worklist inline. `Plan`'s children are now exactly the parts of a change document, and `Plan` sits at 881.
- **Pre-existing tree defect fixed.** `Conclude` claimed `Build` as parent while `Change Lifecycle` and Contents both listed it as a child — two parents, breaking the one-parent rule. Repointed to `Change Lifecycle`, matching the lifecycle's own "three phases" prose.
- **Approach pruned mid-planning**, 3,322 → 1,593 characters, after the user asked whether the change was within its limits. The failure to notice was parked as change 180.

## Conclude

`Held` and `Worklist` landed as new nodes under `Plan`, whose children are now exactly the parts of a change document. `Aside Keyword` narrowed to separate proposals only, retiring the Asides subsection; `Conclude`, `Intent` and `Keywords` follow it. Two pre-existing defects were fixed en route: `Conclude` had two parents, and `part` was undefined. Held proved itself mid-change, holding two of the user's points until their part arrived. Spun off change 180.
