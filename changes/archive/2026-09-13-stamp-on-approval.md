# Stamp on approval

**Cadence:** Formal

## Intent

The agent knows the **current user's handle**: the name a stamp is written under. It is resolved once per session, from a handle already stamped in the map for this person, else from git's `user.name`, else by asking. With the handle known, a user's approval of a node edit also writes their stamp into the node, rather than a stamp waiting for a separate request.

### Context

- Raised during the Map Review of 2026-09-13, where three nodes were stamped for tearne by explicit request after each approval.
- Sign-off today says the agent never adds a stamp unprompted; the Approach must reconcile that with an approval under the Engagement Rule counting as the prompt.
- Change 040 depends on this one for the notion of the current user.

## Approach

_(Approved 2026-09-13.)_

**A node for approver identity.** A new node, *Approver*, under Sign-off, holds the concept: the handle a stamp is written under, how it is resolved, and how it is overridden. Neither Approval Stamp, which describes the record, nor Sign-off, which reads it, is the right home for who is approving.

**Stamping is opt-in.** A map gains its first stamp only when the user asks for one. From then on the map carries a stamp, and every approval of a node edit stamps. A solo developer who never asks keeps a stamp-free map, and "a map with no stamps shows nothing" stays true.

**Resolution is lazy and reported.** The handle is resolved the first time a stamp is needed, not at the Startup Scan. Git's `user.name` is the source, confirmed against handles already stamped in the map. If git has none, or the map's handles do not include it, the agent asks rather than guessing. Whichever way it resolves, the agent says the handle the first time it uses it.

**Overrides are understood, not pattern-matched.** The user can say in any words that this one approval, or the rest of the session, is for another person, as when pairing. The agent confirms the reading in a line before stamping, so a misread costs one exchange. A one-off override lasts one stamp; the handle then returns to the session default. A session override shows in the status line while a set is in progress.

**Approval of an edit is approval of the node.** The Engagement Rule surfaces the whole node text, so the approver has seen it. Sign-off's "never adds one unprompted" becomes "never adds one without an approval": the stamp records what was just approved, with its hash reported beside the count. This is the one meaning change to an existing node.

**Corrections do not stamp.** A Tidy fix moves the fingerprint and the node becomes due again for everyone, which is correct since nobody has seen the result. Sign-off already implies this.

**Agent rules.** Rule 6, Map Edit Order, gains the stamp step, since it applies in nearly every session and the reported hash is the trace of compliance. No new rule.

## Worklist

- [x] Add the *Approver* node as a child of Sign-off: the handle, its resolution from git and the map's stamps, asking when unsure, the two override scopes, and the confirming line.
- [x] Edit Sign-off: "never adds one unprompted" becomes the opt-in rule, first stamp on request, then every approval of an edit stamps; link to Approver.
- [x] Edit the Engagement Rule: settling an approved edit writes the approver's stamp and reports its hash beside the count.
- [x] ~~Edit Thought Management: a session override shows in the status line, with the *Detail* example extended.~~ Dropped.
- [x] Edit AGENT-RULES rule 6 to carry the stamp step.
- [x] Add the Approver node to the Contents overview and Sign-off's child links.

## Log

- 2026-09-13: User rewrote the Engagement Rule's edit order as a numbered list and replaced the stamp sentence with "approval also counts as sign-off", dropping the reported hash from the map. The reporting moves to AGENT-RULES rule 6 (item 5) rather than the node.
- 2026-09-13: Item 4 dropped by the user: the agent naming the handle before each stamp is enough, no status line change. Approver's status-line clause removed accordingly and the node re-stamped.

## Conclude

Rule 6's closer reworded to "With nobody to approve, wait", outside the plan. Four nodes stamped for tearne on the way, the first stamps written under the new rule.
