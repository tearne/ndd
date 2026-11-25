# Bulk request in the tree

**Change Style:** Emergent

## Intent

The map viewer's tree should let a user request sign-off from chosen people on several nodes at once.

## Context

Split from 340 on 2026-11-20: the UI needs iteration, so it is worked here as Emergent, while 340 builds the back end as Formal. Parked until 340 is built. A request is currently made one node at a time, from *Request* in a node's *Sign off* drop-down.

## Focus

A *Request …* control above the tree, paired with *Due for …* under a shared *Review:* label, should let a user tick people, pick nodes in the tree singly or by branch, and send one request for them all.

## Progress

- 2026-11-24: 340 built; Intent approved.
- 2026-11-24: Focus approved, folding in the UI suggestion; Unresolved deleted. Intent trimmed.

## Log

- 2026-11-24: plan approved; Build Lock taken. Claims 3.11.0-dev (minor); map viewer 0.7.0 → 0.8.0.
- First cut, handed back as 3.11.0-dev.1: *Review:* row with *Due for …* and *Request …*; Request… opens an in-flow panel of names (shared with Sign off) and gives each tree node but Contents a box; picking a branch picks below it. One `/request` for all picked. Browser check `bulk_request` added; all tests pass. Panel first overlaid the tree, so it sits in flow.
- Second cut, 3.11.0-dev.2, from user feedback: Request… opens only a *Select children* option under the row (kept in the browser); picking a node picks it alone unless that is ticked. Names, count and Request/Cancel moved to a panel beneath the tree, sticky at the sidebar bottom. Browser check updated; all tests pass.
- Third cut, 3.11.0-dev.3, layout: boxes in a right-hand column; one request bar at the tree foot (count, *children* toggle, names drop-down showing who is ticked, Request, ✕). Surprise: the names drop-down, a `<details>` in the sidebar, was taken for a tree branch by the fold-button code and styles; both now scoped to the tree. Branch file tag moved clear of the boxes. All tests pass.
- Fourth cut, 3.11.0-dev.4, from user feedback: request bar moved to the top under the *Review:* row, sticky while the tree scrolls; *Request* relabelled *Apply*; names drop-down gains a ▾ and opens downward. All tests pass.
- Fifth cut, 3.11.0-dev.5, from user feedback: *Due for* gets the request bar's form (names drop-down with ▾, count, ✕), one bar open at a time; ✕ clears the marks, and open state and names are kept in the browser. *Apply* closes the request bar and opens *Due for* on the names asked. Surprise: a due branch row wrapped to a blank line, as the due highlight left no room for the fold button; narrowed for branch rows, so their badge sits a little left of the leaves'. All tests pass.
- Sixth cut, 3.11.0-dev.6: the *Review:* row's hairline runs full width like the bar beneath; *Due for …* and *Request …* share the row equally. All tests pass.
- Seventh cut, 3.11.0-dev.7: a branch's fold button now shows on hover pinned at the row's right end, inside any due badge or box, so due highlights on branches run full width and their badges line up with the leaves'. The branch file tag moved left to clear it. All tests pass.
- Eighth cut, 3.11.0-dev.8, from user feedback: the "due" badge dropped, the orange highlight alone marking a due node; *Due for …* turns the same orange while its bar is open. All tests pass.
- Ninth cut, 3.11.0-dev.9: in the request bar, the names drop-down, *Apply* and ✕ moved to the top row, matching the *Due for* bar; the count and *children* beneath. All tests pass.
- Tenth cut, 3.11.0-dev.10: the *children* checkbox centred on its label. All tests pass.
- Eleventh cut, 3.11.0-dev.11: colours in two families — the *Due for* bar orange (tint, borders, checkboxes) to match the due highlight and its button; the request bar blue to match *Request …*, *Apply* and *Sign off*. All tests pass.
- Twelfth cut, 3.11.0-dev.12: each file's name now always shown, just above its shading at the top right, the tree making room for it, rather than on hover inside the row. All tests pass.
- Thirteenth cut, 3.11.0-dev.13: both ✕ buttons dropped; *Due for …* and *Request …* toggle their bars closed, closing Request clearing the picks. All tests pass.
- Fourteenth cut, 3.11.0-dev.14: the map title above the sidebar dropped, the tree's top node naming the map; the *Review:* row now heads the sidebar. Surprise: the wrong-token checks were flaky (about 1 run in 64, when the random token ended in x, the "wrong" token was right), pre-existing; fixed in the test. All tests pass.
- 2026-11-24, paused. UI settled by the user at dev.14. Next: map edits, surfaced one at a time — (1) *Map Viewer*: Tree bullet drops "as a title" and gains file names; *Review due* bullet becomes *Due for* and a new *Request* bullet (draft at 890 characters, over ~800, to trim; its "writes nothing but sign-offs" is stale now requests are written — offer separately); (2) *Due Nodes*: the Due for bar (names drop-down, count, toggle, orange, opens after Apply); (3) new node for the request bar under *Map Viewer*, with its nav link and Contents entry; (4) *Map Viewer Due Check* (testing map): bars and the bulk request check. Then Conclude.
- 2026-11-25: map edit 1 settled — *Map Viewer* Tree, Due for and Request bullets; stamped de3676fc. Cut of its opening (ships sentence, stale write line) next.
- 2026-11-25: cut settled — *Map Viewer* opening drops the ships sentence, reads "Having no login" and "sign-offs and requests"; stamped f49760ac.
- 2026-11-25: map edit 2 settled — *Due Nodes* describes the Due for bar; stamped bfe029c1. Its dropped "closes on a click elsewhere" proved still true (map_viewer.py, click-outside handler), correction offered.
- 2026-11-25: *Due Nodes* correction settled — click-elsewhere closing restored; stamped c148157e.
- 2026-11-25: map edit 3 (*Request Bar* node, nav link, Contents entry) written in place as a draft at the user's *write*; awaiting review.
- 2026-11-25: map edit 3 settled — user reshaped the bar's contents as a list, tidied; *Request Bar* node, nav link and Contents entry in place, markers removed; stamped 80e0a80d.
- 2026-11-25: map edit 4 settled — *Map Viewer Due Check* covers the bars and the bulk request check; stamped f140a7b7. Map edits done; Conclude next.

## Conclude

Built over fourteen cuts to 3.11.0-dev.14, from user feedback. Beyond the Focus: the map title gave way to the tree's top node, each file's name now always shows, the due badge gave way to an orange highlight, and the ✕ buttons gave way to toggling. Surprises: a names drop-down was taken for a tree branch, so that code is now scoped to the tree; a flaky wrong-token check, there before this change, was fixed. Touched: map_viewer.py (0.8.0), both viewer tests, map.md, testing.map.md.
