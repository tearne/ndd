# Proportionate engagement prompts

**Mode:** Formal

## Intent

The Engagement Rule tells the agent to phrase per-node map edits as comprehension checks, and offers "does that fit your mental model?" as the wording. In practice the agent hardens that example into a required incantation, stamping it on every edit — including trivial typographic swaps where nothing about the reader's mental picture is at stake and a plain yes/no is all that's wanted. The prompt should scale to what the edit actually changes: a genuine comprehension check when the edit reshapes understanding, a light confirmation (or a batched one) when it's mechanical. Refine the rule so it conveys that judgement rather than prescribing a single phrase.

## Approach

### Generalise the prompt sentence in place; don't add rules

The fix is one reworded sentence in the Engagement Rule node, not a new rule or node. Replace the wording that fixes on "does that fit your mental model?" with a statement that the prompt scales to what the edit changes — a comprehension check when it reshapes the picture, a lighter or batched confirmation when it's mechanical — keeping the mental-model phrasing as an example, not the mandate. Node stays roughly its current length; the point is to open room for agent judgement, not to legislate more of it.

## Plan

- [x] Reword the Engagement Rule node's prompt sentence so it scales to what the edit changes, mental-model wording kept as an example

## Conclusion

Completed. One sentence reworded in the Engagement Rule node; the "does that fit your mental model?" phrasing survives as an example rather than a mandate, and the old "not sign-off" tail was dropped as redundant once mechanical edits gained an explicit lighter prompt.
