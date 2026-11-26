# Release preparation

**Change Style:** Trivial

## Intent

The maps should pass the full Map Review before release, each finding below settled: fixed, rejected or deferred to its own change.

## Context

Opened 2026-11-25 during the release steps in *Release Steps* (`map.md`), at step 1 of 3. Tidy ran over `map.md`, `testing.map.md` and `method/ndd.map.md` with nothing to fix; the user then asked for the full Map Review. Four read-only reviewers produced the findings below, which have not yet been individually verified except R1. Steps 2 (run every test) and 3 (fold the dev headings in `CHANGELOG.md`) wait on this change. The user declined a changelog entry for 150 Map viewer design in map.

Known and left out of the findings: nodes over ~800 characters. Project map: *Installer*, *Rule Layout*, *Rule Selection*, *Map Viewer* (883), *Sign-off Button*, *Write Checks*; testing map: *Testing*, *Fingerprint Check*, *Map Viewer Browser Check*, *Map Viewer Due Check* (864). Method map: *Contents* (1712), *Conceptual Writing* (1172), *Map Files* (905), *NDD*, *Navigation Links*, *Node Sizing*, *Economy*, *Gates and Permissions*, *Drafts*, *Thought Management*, *Discussion Records*, *Unresolved*, *Sign-off*, *Installation*. Counts are rough.

## Findings

Overlaps between reviewers are noted with "see". None is settled yet.

### Rendering: project map against code (R)

- R1 **Node split differs (verified).** `map_viewer.py:1025` splits nodes only at `# `; `fingerprint.py:23` and `tests/fingerprint_test.py:66` split at `#{1,6}`. A node with a `##` subheading fingerprints differently in each. The test can't catch it: `viewer_agrees` feeds the viewer nodes pre-split by the reference. *Fingerprint* (method map) says only "the next heading". No map has `##` today. Code fix plus map clarification.
- R2 *Map Viewer* *Tree* bullet omits that map files linked only in prose get their own tree beneath (`map_viewer.py:1275-1285`, `maps_linked_beyond` 1329-1334).
- R3 *Navigation*: the tree is replaced when the map's shape on disk changes, losing folds (`map_viewer.py:686-691`); following a link opens the destination's ancestor branches (709-713). *Map Viewer Browser Check* says "never redrawn".
- R4 *Sign-off Button* "nothing else is written": writes also rename `approvals:` to `signers:` (`map_viewer.py:1202`) and add a missing `signers:` line (1210-1213). See P1.
- R5 *Contents* is special in three places unmentioned except in *Write Checks*: no *Sign off* button (`map_viewer.py:239-240`), no pick box in the request bar (1363), sign-off refused (1077-1078).
- R6 *Write Checks* *Partial write* "nothing is" reads as atomic across files; swaps are per file and not rolled back (`map_viewer.py:1098-1099`, 1152-1153).
- R7 *Write Checks*: "for a request no scaffolding block" — a sign-off is also refused without one (`map_viewer.py:1086-1087`); a withdrawal skips such a node (1122-1124).
- R8 *Map Viewer* "writes nothing but sign-offs and requests": withdrawals delete stamp lines (`unstamp`, `map_viewer.py:1175-1181`). The method map's *Map Viewer* node ("it edits nothing else") predates requests and withdrawals. See P1.
- R9 *Rule Layout* "Each rule sits under a short level-3 heading": `AGENT-RULES.md` *Orientation* has three bullet rules under a level-2 heading.
- R10 *Fingerprint Check* *Detail* omits the *Contents*-never-due case (`tests/fingerprint_test.py`, `contents_never_due`).

### Project maps: node standard, shape, consistency (P)

- P1 *Sign-off Button* "nothing else is written" contradicts *Map Viewer Write Check* "renaming an older `approvals:` key". See R4, R8.
- P2 *Install Check* tests "a run over the flat layout from before 3.0.0", which *Installer* never describes.
- P3 *Map Viewer Due Check* and *Map Viewer Browser Check* are siblings describing the same script `tests/map_viewer/browser_test.py`; merge, or make Due Check a child. Due Check re-covers the *Sign off* drop-down.
- P4 *Rule Selection*: "this map" is ambiguous (project or method map), and "at rendering time" doesn't fit a hand-maintained file.
- P5 *Distribution* "Nothing is rendered on the way" vs *Agent Rules* "`AGENT-RULES.md` is a rendering": two senses of "render".
- P6 *Agent Rules* defers to *Installation* then restates it; "read on demand rather than preemptively at start" sits awkwardly with Startup Scan.
- P7 *Map Viewer* child order: suggest *Navigation*, *Sign-off Button*, *Due Nodes*, *Request Bar*, then *Request Guards*, *Write Checks*. Its bullets don't mention *Split* or *Navigation*.
- P8 *Sign-off Button*: the red uncommitted light is page-wide and belongs in *Map Viewer*.
- P9 *Sign-off Button*: how a name is added is never said; "which alone are removable" is hard to parse.
- P10 *Due Nodes* and *Request Bar* both state that the bars exclude each other; *Request Bar* leaves "Sign off's" and "the Due for bar" unitalicised.
- P11 *Map Viewer Write Check*: "a `request` key" is defined nowhere in the viewer's nodes.
- P12 *Map Viewer Check* and *Map Viewer Write Check* each say the same "on a copy of the demo map" sentence.
- P13 *Map Viewer Check* / *Test Setup*: "[Node](#test-setup)" for Node.js reads as the map's term; say "Node.js".
- P14 *Test Setup*: uv "fetches … Playwright" on first use vs Playwright "optional … pass with a note when it is missing" — unclear what can be missing.
- P15 *Agent Rules* child order: suggest Selection, Layout, Phrasing, Testing. Also: its *Detail* line only repeats a nav link; *Distribution* "this project map and the testing map stay here" duplicates *Shipped Assets*; *Shipped Assets*' wrapping bullets lack a blank line between.

### Method map: consistency (C)

- C1 *Sync Rule* ("never what is planned") vs *Map Structure* `(TODO)` nodes and *Bootstrapping* seeding a sketch under the map exemption, which *Edit Governance* defines as describing what exists.
- C2 *Gates and Permissions* write gate gives no permission for writes the method makes outside Build: stamps (*Sign-off*), Archiving's changelog and Tidy, Tidy fixes generally, *Formal Conclude* re-engagement.
- C3 "Parked": *Plan* (any degree of formation) vs *Pause Keyword* *Detail* (Intent-only); a change being planned or returned to planning is "not building", so Backlog Review would cover it.
- C4 "Release" and "hand-back for testing" have no home node (*Gates and Permissions*, *Archiving*, *Map Review*, *Versioning*); "the kind agreed then" doesn't say who agrees.
- C5 *Node Sizing*'s signer exemption for reviews rarely applies, since *Signer* resolves the handle only when a stamp is needed; same for *Shape*. Unclear whether Tidy counts as a review.
- C6 Changelog entry: *Caps* treats it as part of Conclude; *Archiving* and *Versioning* as a separate step.
- C7 Tidy corrections and renames change fingerprints, silently staling stamps; nothing says to report or re-stamp.
- C8 *Node Sizing* count leaves open heading, callouts, scaffolding and code blocks; *Caps* inherits.
- C9 *Maintenance* "each opens a list of findings" vs Sign-off's moment "On request" and its due-node worklist.
- C10 *Intent* trim "once the preparation section is approved" is ambiguous for Formal, with Change Specification and optional Implementation Plan.
- C11 *Formal Build* "promotion goes per node" where drifted implies bulk otherwise, against *Engagement Rule* "none in bulk".
- C12 "Due": *Edit Governance* (due for work, Maintenance) vs *Sign-off* (stamp stale or requested).
- C13 The plan-approval gate is stated in *Change Lifecycle*, *Build Lock* and *Gates and Permissions*. Also *Map Viewer* / *Map Viewer Access* 127.0.0.1; *Fingerprint Helper* / *Sign-off* "agent or map viewer writes a stamp" (see M2).
- C14 `AGENT-RULES.md` says what cited nodes don't: Edit Order "With nobody to approve, wait" and "hash beside the count"; Orientation's `method/` sources line and CHANGELOG version line (cites *Versioning*, owned by *Installation*); Approval "delivering a draft … is never approval" beyond *Approval* and *Drafts*.
- C-minor: *Build Lock* "changed code" vs non-code project files; *Change-Management* omits `changes/process-feedback.md`; *Lifecycle Flow Reads* names *Discussion* where *Discussion Conclude* owns promotion.

### Method map: shape and node standard (M)

- M1 *Node* names three standards, but only *Node Sections* is its child; *Node Sizing* and *Writing Style* are siblings under *Map*.
- M2 *Sign-off* (under *Maintenance*) restates *Sign-off Stamp*, *Stamp States*, *Fingerprint Helper*; the concept and its two tools are split across branches (*Tooling* holds only *Map Viewer*).
- M3 *Gates and Permissions* "a change returned to planning keeps the lock" restates, and unconditionally contradicts, *Build Lock* (only a build that changed code keeps it).
- M4 *Installation* second paragraph restates *Map Files*.
- M5 *Context* restates *Intent* and *Plan* on what Context holds.
- M6 Offer moment and yes-or-no form stated in *Maintenance* and again in *Map Review* and *Backlog Review*.
- M7 One-line confirm stated in *Keywords*, *Process Keyword* and *Aside Keyword*.
- M8 *Change Specification* opening repeats *Formal*.
- M9 *Emergent* second paragraph restates the first.
- M10 *Enjoyment*: clause after the colon restates the one before; "a binding constraint, not a bonus" repeats *Principles*.
- M11 Only one blank line before the titles *Fingerprint* and *Tooling*.
- M12 Bold for emphasis: *Node* "**one**", *Orient Then Focus* "**Attention dies under overwhelm.**", bolded links in *NDD* and *Change Lifecycle* bullets; *Node Identity* introduces **scaffolding block** in *Detail* after earlier uses.
- M13 *Engagement Rule* breaks one sentence across a numbered list, hard-wrapped.
- M14 *Consistency*: the ambiguity-test bullet should carry the inline link; its *Detail* is interpretation, not stoppable precision.
- M15 *Caps* sits under *Change Lifecycle* but caps discussion and Change Style parts; *Requirement Voice* sits between *Intent* and *Context* under *Plan* though it governs Change Style parts.
- M-minor: *Edit Governance* and *Sign-off Stamp* use *See also* where an inline link fits; *Map Viewer Access* restates 127.0.0.1 (see C13); *Bounds* says "brief" twice; *Discussion Conclude* paragraph order runs backwards; *Formal* "pays back many times over" is a flourish.

## Progress

- 2026-11-25: change opened to hold the full Map Review's findings; Intent drafted.
- 2026-11-25: Intent approved. Next: choose the Change Style, then work through the findings one at a time, starting with R1.
- 2026-11-26: Trivial style and plan approved; Build Lock taken. User wants a fast release: M3 first, then the changelog fold (release step 3), then other findings as time allows; the rest deferred to a new parked change.
- 2026-11-26: M3 fixed in *Gates and Permissions* (862, over cap; trim deferred). Stamped tearne 3ce7f1ec.
- 2026-11-26: Changelog fold (release step 3) approved: dev headings folded into 3.12.0 — 2026-11-26, regrouped, node brackets dropped. Release step 2 (tests) still to run.
- 2026-11-26: Release step 2: all four test scripts pass (Node absent, so the page-script parse check skipped; the browser test logged one server-side BrokenPipe and still passed).
- 2026-11-26: P1/R4 fixed in *Sign-off Button* (892, over cap; P8 trim deferred). Stamped tearne fe49cfea.
- 2026-11-26: R8 fixed in *Map Viewer* (project map; 887, over cap, trim deferred). Stamped tearne fc370aa0.
- 2026-11-26: R8 fixed in *Map Viewer* (method map; 715). Stamped tearne d375de8b. Viewer write-scope findings (P1, R4, R8) done.
- 2026-11-26: R1 code: fingerprint.py 1.3.1 and the test's reference split at level-1 headings only; new subheading_stays_in_node test splits with all three, fails on the old helper, passes now.
- 2026-11-26: R1 map: *Fingerprint* Detail says level-1 heading outside a code fence (777). Stamped tearne 1d5b37cd.
- 2026-11-26: R1 map: *Fingerprint Check* Detail names the subheading case (~885, over cap, trim deferred). Stamped tearne 5e9b8ba0. R1 done.
- 2026-11-26: Remaining findings parked as 010 Map Review findings; no open items left.

## Conclude

Fixed M3, P1/R4/R8 and R1; the other findings are parked unsettled as 010 Map Review findings. R1 went beyond the map: `fingerprint.py` 1.3.1 and its test split nodes at level-1 headings only, with a new case checking the reference, helper and viewer agree. Nodes edited: *Gates and Permissions*, *Map Viewer* and *Fingerprint* (method map), *Sign-off Button* and *Map Viewer* (project map), *Fingerprint Check* (testing map). Four were already over the cap and grew further; their trims are listed in 010.
