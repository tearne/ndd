# Due and sign-off UI tweaks

**Change Style:** Emergent

## Intent

The map viewer's due and sign-off controls should work as the user asked when trying them.

## Focus

The five requests in Context should be built and tried in the viewer one at a time, each adjusted until the user is happy with it; the map should follow where behaviour changes.

## Context

Feedback on 310 (due node selection) once built, 2026-11-19, taken as its own change so the interface can be tweaked freely. The items raised:

1. A clearer due mark in the tree.
2. *Due for…* allows several people.
3. *Previous due* / *Next due* removed; whether a sign-off still moves on to the next due node is undecided (310's agent suggested keeping it, the next node due for any person chosen).
4. *Due for…* a button rather than full width, with the count to its right.
5. The *Sign off* drop-down closes on a click elsewhere, its two buttons side by side.

Items 2 and 3 touch *Due Nodes*, *Map Viewer*'s bullet and *Map Viewer Due Check*; 1, 4 and 5 are presentation.

## Log

- 2026-11-19: plan approved, Build Lock taken, version 3.8.1-dev.
- 1 drafted: due mark now an amber tint with a left bar and a "due" badge, replacing the dot. Demo served on 8081 (8080 holds an older viewer from 09:31, left running).
- 1 revised: due bar runs nearly the row's width, badge at its right end.
- 1 revised: bar and badge orange lightened to #f2b54d, badge text dark brown.
- 1 done, user confirmed.
- 3 settled: no auto-advance after a sign-off, user's call; Previous/Next due go too. 2 and 4 built together with it, as one control.
- 2–4 built: Due for… is a button opening a tick list of signers, closing on a click elsewhere, count to its right; Previous/Next due and the move-on removed. Browser check reworked, passes.
- 2–4 revised: count shows only the number, "6 due".
- 6 added by the user: the project name as a title above the tree.
- 6 tried: the entry root's heading as a title above the tree, linking to the root; the root stays in the tree for now.
- 6 revised: the root dropped from the tree, which opens at its children, shaded as the root's file; the title carries the root's here and due marks. Fold-button check moved to *Linked Map*, as *Demo* is no longer a branch; tree comparison ignores the title's mark.
- Button renamed "Review due for …", at the user's request.
- One unexplained failure of map_viewer_test.py ("refused sign-off: the file untouched", 2 failures) on one run; eight reruns clean. Open: watch for it.
- 6 done, user confirmed. Next: 5.
- 5 built: Sign off drop-down closes on a click outside it; Sign off and Request sign-off side by side. Browser check gains the click-away; both suites pass.
- 5 revised: "Sign off ticked names" shortened to "Sign off", matching "Request sign-off".
- 5 revised: "Request sign-off" shortened to "Request".
- 5 revised: drop-down narrowed to 11rem.
- 5 revised: Request now left of Sign off.
- 5 done, user confirmed.
- 2026-11-19: map edits to follow the build, one at a time: (1) *Due Nodes*, (2) *Map Viewer*'s Tree and Due bullets, (3) *Sign-off Button*'s *Request*, (4) *Map Viewer Due Check*, (5) *Sign-off* (method map) "step them through".
- Map edit 1 approved, 340 characters, stamped e935ef24.
- Map edit 2 approved, 804 characters, stamped 0b001393. Offered: *Node* bullet's "current or stale" omits requested.
- Map edit 2b approved (*Node* bullet links stamp state), ~793 characters, stamped 047f2b94.
- Map edit 3 approved, 795 characters, stamped 8fe86aea.
- Map edit 4 approved, 377 characters, stamped 50bf848d.
- Map edit 5 approved, ~819 characters (over, as accepted in 310), stamped f87127a5. All map edits settled.
- 10 more server runs clean, browser and fingerprint suites pass; the one-off failure did not recur, closed as not reproduced.
- 2026-11-19, after the build was confirmed done: root restored as the tree's first item, at the user's request, so it is reviewed and marked due like any node; the title above stays, as a plain label. Tests pass. *Map Viewer*'s Tree bullet still holds.

## Conclude

Completed. Beyond the five requests: the map's root heading is shown as a title above the tree; the buttons were renamed *Review due for …*, *Sign off* and *Request*; the sign-off no longer moves on; *Map Viewer*'s Node bullet now links stamp states. Asides parked as 330 and 340.
