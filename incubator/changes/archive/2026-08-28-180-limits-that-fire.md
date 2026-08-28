# Limits that actually fire

## Intent

The method's numeric limits do not fire in practice. Change parts run well over their character triggers unnoticed, and map nodes sit over the ~800 bound in [Node Sizing](#node-sizing) despite [Consistency Upkeep](#consistency-upkeep) obliging the agent to flag exactly that. Same defect on both surfaces: a limit nobody measures.

Also to settle: whether the numbers are right. If a cap is simply too tight for what its part must carry, the limit rises rather than the discipline tightening.

Cadence: Formal.

## Approach

- **Phrase each limit as an instruction with an actor and a verb: the agent counts the characters and reports the count.** The present wording describes an outcome ("a soft trigger flags borderline material") that nothing obliges anyone to produce, and a character count cannot be eyeballed — a rule honoured only by measuring must say to measure.

- **Disclose the number in chat at every surfacing, not only when near the cap or at a final one.** A stated count is falsifiable, where silence makes "measured, fine" indistinguishable from "forgot to measure"; and a part that grows turn by turn as answers fold in never reaches a single last moment to check.

- **Move the cap from Detail into the node body.** Detail is read once at navigation, not at the moment of use.

- **Give node sizing the same treatment, indexed from Consistency Upkeep, triggered when a node is touched.** Nothing else prompts it, and a whole-map sweep on every session is not affordable.

- **Set the caps from observed practice: Intent ~500, Approach ~2000, Conclude ~500, node ~800.** A cap set below the norm fires constantly once it works, and the user learns to wave it through — which is how a limit dies. Across twenty archived changes only the Approach number was badly wrong.

- **Cap the Intent's opening prose only, and let history and context sit below it in a subsection.** What matters is that the opening scans in seconds and states the problem or the outcome; provenance and evidence are often worth keeping, just not above the thing they support. It mirrors a node's *Detail*, so nothing new has to be learnt, and gives the agent somewhere to put material a bare number would only tell it to delete.

- **Count a node's body and its *Detail*, excluding *See also* (as well as tables and diagrams).** Exempting Detail would make the bound gameable by pushing bulk downward, while counting a link list penalises a node for being well connected.

- **Land the rules only; park the nodes already over as their own Intent.** Seventeen nodes need split-versus-keep settled one at a time under the Engagement Rule — a body of work that would swamp the rule change carrying it.

- **Count with an ad-hoc shell command, adding no vendored tool.** The method rides generic tooling; a purpose-built counter belongs to change 110, not here.

## Worklist

- [x] Rewrite the cap in [Intent](#intent) as a body-level instruction to count and report, set at ~500 over the opening prose only.
- [x] Add the history/context subsection convention to [Intent](#intent), with the cap not applying below it.
- [x] Rewrite the cap in [Approach](#approach) as a body-level instruction to count and report, raised to ~2000.
- [x] Rewrite the cap in [Conclude](#conclude) as a body-level instruction to count and report, held at ~500.
- [x] State in [Node Sizing](#node-sizing) that the ~800 count covers body and *Detail* and excludes *See also*, and rewrite it as an instruction to measure and report when a node is touched.
- [x] Retarget the size bullet in [Consistency Upkeep](#consistency-upkeep) to measuring on touch rather than flagging.
- [x] Park an Intent for the map nodes now over the size bound.

## Log

- Conclude's cap moved into its body; the Detail sentence now only carves out the changelog entry from the count.
- Touched-node counts after the edits: Intent 1159, Approach 1282, Conclude 1509, Node Sizing 692, Consistency Upkeep 649 — three already over the bound and nudged further by this change's own additions. Flagged rather than trimmed; they head the backlog parked as 190.
- Backlog parked as `190-oversize-nodes.md`, dogfooding the new Intent shape: short opening, counts in a Context subsection.
- Deviation: the six node edits went in as one pass on the approved worklist rather than negotiated per node under the Engagement Rule. User declined a replay; the underlying rule conflict parked as 200.
- No version bump: staying on 1.0.0 until release, so no changelog entry.

## Conclusion

The method's caps are now instructions to count and report, stated in the node bodies and firing at every surfacing rather than at one final moment. Numbers settled: Intent ~500 over its opening prose only, Approach ~2000, Conclude ~500, node ~800 counting body and *Detail*. An Intent may now carry history below its opening. Two Intents parked: 190 for the seventeen oversize nodes, 200 for the Build/Engagement-Rule conflict this build exposed.
