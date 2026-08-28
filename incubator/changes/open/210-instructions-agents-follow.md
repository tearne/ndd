# Instructions that agents actually follow

## Intent

The method is written for an agent to act on, but too much of it can be satisfied by doing nothing: rules with no trigger, obligations with no observable act, and in places two nodes that say opposite things. Change 180 fixed this for the numeric limits; the same defect runs through the rest of the map. Every instruction should name who does what, when — or be dropped.

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

Not in scope as findings: the tree overview was verified in step with all 48 headings.
