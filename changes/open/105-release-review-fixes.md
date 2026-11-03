# Release review fixes

**Change Style:** Emergent

## Intent

Settle every finding of the full Map Review run before the 2.10.1 release, across the three maps, the agent rules and the files they describe, so the release ships a map that holds together and matches what exists.

## Context

The review (2026-11-03) found about 55 items in six groups: A, introduced by this release; B, typos; C, facts duplicated across nodes; D, lifecycle ambiguities; E, shape; F, map against files. Findings are not stored, so this change's Log keeps track of them.

## Focus

Work the findings group by group, A first, then B to F. Each map edit is settled on its own; where the map is right and a file is wrong, the file is fixed. A finding that outgrows a quick fix is parked as its own change. Checkpoint: release once A and B are done, if time runs short.

## Log

- 2026-11-03: Build Lock taken; patch bump agreed, claiming 2.10.2-dev.
- A1: *Node* now holds the draft check's scope and trace clauses, and no longer contradicts *Node Sections* on which sections a node has.
- A2: agent rule renamed *Node*, closing on its one source link; the 2.10.0-dev changelog entry matched.
- B: seven typo and spelling corrections applied and reported; the seven stamped nodes they touched restamped on approval.
- C1: *Vibe* keeps the safeguard and its Build; *Bounds* owns its brevity and reason.
- C2: *Implementation Plan* states its trigger once; *Formal* no longer repeats it.
- C3: *Emergent* no longer repeats what *Focus* owns.
- C4: *Build* points to *Versioning* for the version step rather than restating it.
- C5: *Startup Scan* offers bootstrapping, pointing to *Bootstrapping* for the condition.
- C6: dismissed; *Maintenance*'s table names its reviews before they explain themselves.
- C7: *Aside Keyword* bullets its routes and points to *Thought Management* for current-change material.
- C8: style facts given one owner: *Trivial* (whole plan), *Change Style* (same Build and Conclude), *Formal* (default); "lightest" cut from *Trivial*.
- C9: *Three Deaths* links "engagement" to *Enjoyment*; "binding constraint" overlap dismissed.
- C10: *Log*'s restating last sentence cut; the parallel settle lists kept for local sufficiency.
- C11: *Cross-Agent Falsifiability* owns its relation to the two checks, now called lighter rather than everyday; *Consistency* and *Rendering* stop restating it.
- C12: *Agent Rules* leaves naming the source node to *Rule Layout*; still 842, over the bound, to settle with its group F finding.
- D1: return to planning given one shape: *Build* owns the user's return, *Formal Build* the in-place re-agreement; *Implementation Plan* points there, and the "abandoning Formal" clause is gone.
- D2: write permission keyed on phase in *Gates and Permissions*, which now names git writes as its third gate; the *Active Change* rule reworded to match and A/B tested (both arms declined; the old one only by reasoning past its rule).
- D3: *Drafts* and its orientation bullet exempt actions the method lets the agent take without asking; A/B tested, same behaviour, the conflict with the Build rule gone.
- D4: *Plan* defines a parked change; *Discussion Records* says where a record lives (tightened to 799); *Discussion Conclude* links there.
- D5: *Release Steps* opens with Tidy and the full Map Review offer; *Archiving* step 3 defers the companion folder to *Companion Folder*.
- E1, E2: parked as discussion `map-shape-session-conduct-discussion.md`; E3 settled with D2.
- Wording: *Navigation Links*, *Edit Governance*, *Callouts*, *Standards*, *Change Specification* and *Intent* settled; *Fingerprint Check* folded into F.
- F1: `util/fingerprint.py` reads stamps from the scaffolding block only; `tests/fingerprint_test.py` pins it with a quoted-stamp case (fails on the old helper, passes now), and its stale map anchor is fixed (F2).
- F3: *Fingerprint Check* names the test as an independent reference kept in the checkout, says what it checks in full, and moves fixture detail to *Detail*; shipping only the method parked as 115.
- F4, F5: *Rule Layout* lets a rule's inline read-link stand as its source link; the `AGENT-RULES.md` header says output cites the source node, not the rule heading.
- F6: *Drafts* holds the "even in reply to an ask for approval" clause, tightened to 809; its rule moved from *Orientation* to its own heading.
- F7: *Unresolved* rule fires per part as well as before the whole plan; A/B tested, same behaviour, now stated rather than inferred.
- F7a: *Plan* opens by defining the plan as the part of a change written before Build.
- F8: *Caps* rule's Focus line matches its node; A/B skipped on the user's say, as a one-clause conformance edit.
- F9: dismissed; the *Drafts* rule beside *Edit Order* already covers how a draft is written.
- F10: dismissed; "or reviewed" cues the agent to re-read for edits it was not told of.
