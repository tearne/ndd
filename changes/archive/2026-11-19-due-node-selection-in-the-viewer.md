# Due node selection in the viewer

**Change Style:** Formal

## Intent

The map viewer should help a stakeholder step through the nodes due for their sign-off, signing each as they go. In a split page, each pane should scroll in a box of its own.

## Context

Parked from change 80's Held on 2026-09-10 as agent-side selection at Sign-off; refreshed on 2026-11-17 to use the map viewer, which now records sign-offs, and to fix the split page's scrolling. The old Intent's ordering candidates remain open: rank by how load-bearing a node is, lead with nodes where most stakeholders are out of sync, or orient around one stakeholder. The aid it named to accompany each node, change 320's retrospective diff, was delivered by tooling development (archived 2026-11-10) as the viewer's sign-off diff.

## Change Specification

Shape agreed 2026-11-17:

- A *Due for…* selector in the tree pane, listing the signers in the map's stamps (simplified at the user's request from also listing names added in the sign-off drop-down).
- With a person chosen, their due nodes marked in the tree, and a count such as "7 due for bob".
- *Next due* and *Previous due* step through them; after a sign-off the page moves on to the next due node.
- Order is tree order; ranking stays out of scope.
- In a split page each pane scrolls in its own box.
- Four sign-off states: *current*, a stamp matching the node; *stale*, a stamp not matching; *requested*, a stamp with `hash: null` and `at` the request date; *unsigned*, no stamp. Due means stale or requested; unsigned is never due.
- A *Request sign-off* button beside *Sign off* writes a request for each ticked name with no stamp on the node; a stale stamp is already due.

Planned edits, on copies in the companion folder (dropped at archiving) of `map.md`, `testing.map.md` and `method/ndd.map.md`, taken 2026-11-17 before any edit:

1. *Due Nodes* (project map, new, under *Map Viewer*): the selector, the marks and count, stepping, moving on after a sign-off, tree order.
2. *Map Viewer* (project map): child link and a bullet.
3. *Sign-off* (method map): due nodes can also be followed in the map viewer, and due is stale or requested, linking to *Stamp States*.
4. *Stamp States* (method map, new, under *Sign-off Stamp*): the four states.
5. *Sign-off Stamp* (method map): child link, and in *Detail* the requested form, `hash: null` with `at` the request date.
6. *Node Sizing* (method map): rely on a current stamp rather than on "not due".
7. *Fingerprint Helper* (method map): `--due` lists stale and requested; `null` accepted.
8. *Sign-off Button* (project map): the *Request sign-off* button.
9. *Map Viewer Browser Check* (testing map), or a new check beside it if over the bound: the due flow, requesting, and each pane scrolling on its own.
10. *Fingerprint Check* (testing map): a requested stamp is due, an unsigned node is not.
11. Contents entries for any new node.

The scrolling fix has no node to describe it: the second pane is not yet in the map, which is 150's aim.

Progress:

- 1 approved, 399 characters, stamped 0339c333.
- 2026-11-17: names agreed with the user, dropping the "Map Viewer" prefix from *Map Viewer*'s children: *Map Viewer Sign-off* becomes *Sign-off Button*, *Map Viewer Security* becomes *Request Guards*, and the new node *Due Nodes*. Headings and every link renamed in the copies, the three re-stamped. The testing map's check names stay.
- Map Viewer Check's link repointed, re-stamped as a correction. 
- 2 approved, 746 characters, stamped 0b89b316.
- 3 drafted, then reopened by the stale/absent item: whole-file draft in draft-method.md is superseded.
- 2026-11-18: stale/absent item folded in; shape and edit list revised (now 9 edits), approved. Next: redraft 3.
- 3 redrafted with the four states, 1009 characters, written in place in the copy between draft markers; a split into a new *Stamp States* node proposed, not yet agreed. The old draft-method.md is superseded.
- 2026-11-18: session lost and resumed. *Sign-off*'s first paragraph reworded ("is scaffolding" sentence), written in place between draft markers, awaiting approval alongside edit 3.
- 2026-11-18: *Sign-off*'s "requested" clause reworded in the draft region, awaiting approval. Open: *Sign-off Stamp* Detail should describe a requested stamp (`hash: null`, `at` the request date); not yet on the edit list.
- 2026-11-18: edit list revised to 11 and approved: the states split into a new *Stamp States* under *Sign-off Stamp*; *Sign-off Stamp* gains the requested form (closes the open item). Next: redraft 3 narrowed.
- 2026-11-18: 3 narrowed (states out to 4, last clause cut as *Engagement Rule* owns it), 820 characters, written in place between draft markers, awaiting approval. Link to *Stamp States* dangles until 4.
- 3 approved, 820 characters, stamped 0bc8d4fc.
- Open: requesting on a stale stamp writes `hash: null`, losing the old hash the viewer's sign-off diff uses to show what changed. Raise before edit 5 settles the requested form.
- 4 approved, 312 characters, stamped 803c0718; placed after *Fingerprint Helper*, in tree order. Next: the lost-hash item, then 5.
- 2026-11-18: lost-hash item closed: a request is written only where the person has no stamp, so no hash is overwritten; shape bullet revised, approved.
- 5 approved, 767 characters, stamped 749361bb; first sentence also reworded to cover a request.
- 6 approved, 795 characters, stamped 86d46184.
- 7 approved, 641 characters, stamped 442e03c4; "null accepted" left to edit 10's check.
- 8 approved, 880 characters (overrun accepted), stamped c47c4c54; link corrected to method/ndd.map.md#stamp-states.
- 9 split: 9a scrolling into *Map Viewer Browser Check*, 9b a new *Map Viewer Due Check*. 9a approved, 815 characters, stamped d3874e7b.
- 9b approved, 420 characters, stamped 0794c205. Next: 9c, *Testing*'s child link and bullet for it.
- 9c approved (*Testing* child link and bullet), 712 characters, stamped 748129d6.
- 10 approved, 940 characters, stamped e36b19ee. Open: trim offered (cut the checkout sentence).
- Fingerprint Check trimmed (checkout sentence cut, *Shipped Assets* owns it), ~840 characters, stamped 948fdd44.
- 11 approved: Contents entries for *Due Nodes*, *Map Viewer Due Check*, *Stamp States*. All 11 edits settled.
- User edit to *Sign-off Button* (reason clause cut), 791 characters, re-stamped a2cb36c6.
- 2026-11-18, paused. Next: decide whether to skip the Implementation Plan (agent recommends skip), then approve the plan whole, then Build Lock. Open: delete superseded draft-method.md; spacing correction, one blank line before *Signer* in the method map copy should be two.
- 2026-11-19: resumed. Superseded draft-method.md deleted (`git rm`); its mentions above are history. Spacing before *Signer* in the method map copy corrected to two blank lines. Next: Implementation Plan skip decision.
- 2026-11-19: Implementation Plan skipped, approved by the user. Next: Unresolved check, then plan approval.
- 2026-11-19: plan approved; Build Lock taken. Next: Intent trim, then Build.
- 2026-11-19: Intent trimmed, 174 characters, approved. Build begins.
- Build 1: fingerprint helper 1.2.0, `hash: null` read as requested; due is stale or requested, unsigned never. fingerprint_test.py updated (new requested case, Dana Lee covers the spaced name), passes; fails on the old helper.
- Build 2: viewer 0.5.0: requested stamps read and shown, Due for… selector with marks, count and Previous/Next due, moving on after a sign-off, Request sign-off (only names with no stamp), split panes each scrolling in their own box. Existing viewer and browser suites pass.
- Build 3: checks added: demo gains a Requested node (build_demo_map 0.4.0); server check shows it; browser checks for panes scrolling apart, due nodes, and requesting. All suites pass; the new browser checks fail on the old viewer.
- Build 4: copies promoted into the live map, whole files, as the live maps had not drifted from the baseline: map.md, testing.map.md, method/ndd.map.md. Nothing due for tearne.
- Page script parse check run with pyright's bundled node (~/.cache/pyright-python/nodeenv/bin) on PATH: passes.
- 2026-11-19: user feedback on the built viewer, before Conclude; the Change Specification is to be re-agreed with the Build Lock kept. Open, to settle one at a time:
  1. A clearer due mark in the tree.
  2. *Due for…* allows several people.
  3. *Previous due* / *Next due* removed (user not bothered), so the moving-on after a sign-off needs deciding.
  4. *Due for…* becomes a button, not full width, with the count to its right.
  5. The *Sign off* drop-down closes on a click elsewhere; its two buttons sit side by side.
  Spec nodes affected: *Due Nodes*, *Map Viewer*'s bullet, *Map Viewer Due Check*; 1, 4 and 5 are presentation, below the map.
- 2026-11-19: the five feedback items parked as their own change, [320 Due and sign-off UI tweaks](../open/320-due-and-sign-off-ui-tweaks.md), at the user's request; nothing open. Build confirmed done.

## Conclude

Completed. Two additions: the demo map gained a Requested node, so every stamp state shows. The page-script parse check needs Node on the PATH, which pyright's nodeenv supplies; setup is parked as 160. Feedback on the built interface is parked as 320.
