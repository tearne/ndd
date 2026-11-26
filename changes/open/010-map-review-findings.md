# Map Review findings

## Intent

Settle each remaining finding of the 2026-11-25 full Map Review: fixed, rejected or deferred to its own change.

## Context

Parked 2026-11-26 from 100 Release preparation, which fixed the most pressing findings so 3.12.0 could ship. Findings other than R1 were not individually verified. Also known and not listed as findings, nodes over ~800 characters: nodes over ~800 characters. Project map: *Installer*, *Rule Layout*, *Rule Selection*, *Map Viewer* (883), *Sign-off Button*, *Write Checks*; testing map: *Testing*, *Fingerprint Check*, *Map Viewer Browser Check*, *Map Viewer Due Check* (864). Method map: *Contents* (1712), *Conceptual Writing* (1172), *Map Files* (905), *NDD*, *Navigation Links*, *Node Sizing*, *Economy*, *Gates and Permissions*, *Drafts*, *Thought Management*, *Discussion Records*, *Unresolved*, *Sign-off*, *Installation*. Counts are rough.

Nodes taken further over the cap by 100, with a suggested trim: *Gates and Permissions* (862), *Sign-off Button* (892; P8 moves the red light out), project *Map Viewer* (887), *Fingerprint Check* (~885).

## Findings

Overlaps between reviewers are noted with "see". Already fixed in 100, and dropped here: R1, R4, R8, P1, M3. None below is settled.

### Rendering: project map against code (R)

- R2 *Map Viewer* *Tree* bullet omits that map files linked only in prose get their own tree beneath (`map_viewer.py:1275-1285`, `maps_linked_beyond` 1329-1334).
- R3 *Navigation*: the tree is replaced when the map's shape on disk changes, losing folds (`map_viewer.py:686-691`); following a link opens the destination's ancestor branches (709-713). *Map Viewer Browser Check* says "never redrawn".
- R5 *Contents* is special in three places unmentioned except in *Write Checks*: no *Sign off* button (`map_viewer.py:239-240`), no pick box in the request bar (1363), sign-off refused (1077-1078).
- R6 *Write Checks* *Partial write* "nothing is" reads as atomic across files; swaps are per file and not rolled back (`map_viewer.py:1098-1099`, 1152-1153).
- R7 *Write Checks*: "for a request no scaffolding block" — a sign-off is also refused without one (`map_viewer.py:1086-1087`); a withdrawal skips such a node (1122-1124).
- R9 *Rule Layout* "Each rule sits under a short level-3 heading": `AGENT-RULES.md` *Orientation* has three bullet rules under a level-2 heading.
- R10 *Fingerprint Check* *Detail* omits the *Contents*-never-due case (`tests/fingerprint_test.py`, `contents_never_due`).

### Project maps: node standard, shape, consistency (P)

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
