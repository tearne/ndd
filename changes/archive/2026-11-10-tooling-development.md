# Tooling development

**Change Style:** Vibe

## Intent

Build a proof of concept of a map viewer: a POS script, run beside a map or pointed at a map.md, that serves it on port 8080 with no login. In a browser the user should be able to navigate the map node by node, see what changed in a node and who has approved it. The viewer only reads: approvals and edits are made through the agent in the same ssh session. The markdown stays the source of truth, and the tool stays optional.

## Bounds

No map edits. Listens on 127.0.0.1 only, reached by port forwarding. Serves no request that writes a file.

## Context

The wider aim, beyond the PoC: present a map in stakeholder meetings, record feedback on nodes, and add a cross-map index; never formally hosted.

Fuller notes and the design tensions are in the retired `enhancement-discussion.md` (P3), kept in git history. Renumbered from 290 on 2026-09-10 to close the sign-off theme.

## Log

- 2026-11-10: Plan approved; Build Lock taken. Script at `tools/map_viewer.py`, outside what ships.
- 2026-11-10: Patch bump agreed, claiming 3.5.1-dev.
- 2026-11-10: `tools/map_viewer.py` written: stdlib only, imports the shipped `fingerprint.py` for parsing, hashing and stamp reading. Pages: node (rendered, nav links, stamps with current/stale status, approve form), changes since last commit (word diff against `git show HEAD`), per-file index. Approve refuses if the node changed since the page was opened.
- 2026-11-10: Tested on a scratch git copy of the repo: cross-file navigation, tables, word diff, a stamp written and accepted by `fingerprint.py --due`, a quoted handle with a colon, stale refusal; a path outside the map directory and missing nodes now answer 403/404 rather than dropping the connection.
- 2026-11-10: Limits found: needs the NDD checkout's `method/util/fingerprint.py` beside it (not yet usable from a client install); minimal markdown rendering.
- 2026-11-10: Handed back for testing as 3.5.1-dev.1.
- 2026-11-10: Made self-contained at the user's request, to copy to another host: the fingerprint rule is carried in the viewer, and `tests/fingerprint_test.py` now checks it gives the same fingerprints as the reference. A name clash from the move broke node pages; caught by running the copy standalone, fixed. Every page answers from a lone copy in `/tmp`, with fingerprints matching `fingerprint.py`.
- 2026-11-10: Open: *Fingerprint Check* in `testing.map.md` doesn't mention the viewer check; left for after the PoC under the no-map-edits Bounds.
- 2026-11-10: Handed back for testing as 3.5.1-dev.2.
- 2026-11-10: Contents tree added on the left, at the user's request: followed from the entry map's root through child links, collapsible, current node in bold. A node outside it (the method map, linked from `map.md` only in prose) adds its own file's tree beneath. Map reads cached until the file changes; a method-map page with both trees renders in about 0.25 s.
- 2026-11-10: Handed back for testing as 3.5.1-dev.3.
- 2026-11-10: Contents special-cased at the user's request: its page says it is never stamped or due instead of showing an empty approver table and form, the index marks it "overview", and a posted approval for it writes nothing.
- 2026-11-10: Handed back for testing as 3.5.1-dev.4.
- 2026-11-10: Footer (fingerprint, stamps, approve) set in lighter grey, smaller, at the user's request. Each sidebar tree now headed by its file name, after the user found the two trees confusing.
- 2026-11-10: Bug, reported by the user: opening map.md's Contents drew map.md's tree a second time, since Contents was left out of the tree and so looked like a node outside it. Contents now appears in the tree where its root links to it, and a second tree is added only for a file the first doesn't cover. Checked on Contents in both maps, a method-map node and a testing-map node.
- 2026-11-10: Handed back for testing as 3.5.1-dev.5.
- 2026-11-10: Tree layout, at the user's request: the browser's disclosure triangle replaced by a fixed-width ▸/▾ marker, with a blank of the same width before leaves, so siblings align; the current node highlighted and scrolled into view. Checked in the HTML only; no browser here to see it rendered.
- 2026-11-10: Handed back for testing as 3.5.1-dev.6.
- 2026-11-10: Plan re-agreed with the user: the viewer is read-only, for security and because review edits are better made through the agent in the ssh session. Intent and Bounds revised.
- 2026-11-10: Made read-only to the revised plan: the approve form, POST handler and stamp writing removed. The stamp table (approver, date, hash, current or changed since) stays. Every page answers; a POST now gets 501 from the server itself. Fingerprint test passes.
- 2026-11-10: Handed back for testing as 3.5.1-dev.7.
- 2026-11-10: `tools/viewer_demo.py` added at the user's request: builds a demo git repo (default `/tmp/map-viewer-demo`, refusing any directory it didn't build) whose commit and working tree differ, with stamps computed by the viewer's fingerprint. Covers current, stale, mixed, unstamped and quoted-handle approvals; edited, added and unchanged nodes; a branch file; Contents; and rendering. Checked in the viewer, and against `fingerprint.py --due`, which agrees on every node.
- 2026-11-10: Handed back for testing as 3.5.1-dev.8.
- 2026-11-10: Cross-file branches tinted in the tree at the user's request: where the tree crosses into another file, that branch gets a pale background, one tint per file, with the file name on hover. Checked on the demo (Branch) and the scratch NDD copy (Testing).
- 2026-11-10: Handed back for testing as 3.5.1-dev.9.
- 2026-11-10: At the user's request, "changes since last commit" replaced: a stale approval's status is a link to what changed since that approval. The approved version is the newest commit of the file whose node, found by id or else by name, has the stamp's fingerprint; the page shows the changed passages with a line of context, then the whole node now, yaml included, with the same highlights. When no committed version matches, it says so.
- 2026-11-10: Tree level buttons (1, 2, 3, all) added at the user's request: they open the tree to that depth, remembered across pages, keeping the current node's branch open.
- 2026-11-10: Demo reworked to match: Edited now carries a stale approval; Added dropped; Renamed (approved under an old name, found by id) and Lost Approval (stamp for text never committed) added. All checked in the viewer; `fingerprint.py --due` agrees.
- 2026-11-10: Open: the stale-approval view is change 320's retrospective diff, built here for the viewer; 320's fate to settle before Conclude.
- 2026-11-10: Handed back for testing as 3.5.1-dev.10.
- 2026-11-10: The approval table added to the stale-approval view at the user's request, below the line saying where the approved text was found, including when it wasn't found; its stale links move between approvers' views.
- 2026-11-10: Handed back for testing as 3.5.1-dev.11.
- 2026-11-10: Level buttons replaced, at the user's request, by + and − beside each branch node, shown on hover: expand or fold everything below that node, leaving it open. The current node's branch still opens on load. Checked in the HTML only.
- 2026-11-10: Handed back for testing as 3.5.1-dev.12.
- 2026-11-10: User found + and − did nothing. Likely cause: the tree loads fully open, so + had nothing to open, and − folded only branches below, so on a node whose children are all leaves it had nothing to fold. Both now act on the node itself as well as everything below it. Still unverified in a browser.
- 2026-11-10: Handed back for testing as 3.5.1-dev.13.
- 2026-11-10: + and − merged into one toggle button per branch, at the user's request: it folds the branch and everything below when all of it is open, else opens it all, and its label follows the tree's state however that changed. Unverified in a browser.
- 2026-11-10: Handed back for testing as 3.5.1-dev.14.
- 2026-11-10: Diff view text revised with the user: titled *Approval Diff*, with a details list (Node, Approver, Approved with date, hash and commit, Current hash) in place of the sentence; sections renamed *Delta* and *Current*.
- 2026-11-10: Handed back for testing as 3.5.1-dev.15.
- 2026-11-10: *Approved* split: the stamp's date and hash, then *Found in* with the commit only, its date dropped.
- 2026-11-10: Handed back for testing as 3.5.1-dev.16.
- 2026-11-10: Diff view reordered at the user's request: Delta, then Current, then the details list and approval table in the grey footer. Title now names the node.
- 2026-11-10: Handed back for testing as 3.5.1-dev.17.
- 2026-11-10: Diff details moved beside the heading, on the right and smaller, at the user's request; the approval table stays in the footer. The Node line dropped, since the heading names it. Unverified in a browser.
- 2026-11-10: Handed back for testing as 3.5.1-dev.18.
- 2026-11-10: "back to" link moved under the diff view's heading, so the heading and details start at the top together.
- 2026-11-10: Handed back for testing as 3.5.1-dev.19.
- 2026-11-10: "back to" link dropped; the node name in the diff view's heading links back to the node instead.
- 2026-11-10: Handed back for testing as 3.5.1-dev.20.
- 2026-11-10: A tinted branch shows its file name at the tint's top right on hover, replacing the tooltip, at the user's request. Unverified in a browser.
- 2026-11-10: Handed back for testing as 3.5.1-dev.21.
- 2026-11-10: Labels made consistent with the user: "fingerprint" for every node hash (Current fingerprint, Approved fingerprint), "commit" only for git.
- 2026-11-10: Handed back for testing as 3.5.1-dev.22.
- 2026-11-10: In the approval table, the link to what changed moved from "stale" to the approved fingerprint, and a stale row is tinted pale orange, at the user's request.
- 2026-11-10: Handed back for testing as 3.5.1-dev.23.
- 2026-11-10: Diff details normalised with the user into an Approved vs Current table, the columns tinted orange and green: Fingerprint; Introduced (the oldest commit in the newest run holding that text, or "not yet committed" for current text the newest commit lacks); Stamped (approved only). Checked uncommitted and committed on the demo and a copy with its working tree committed.
- 2026-11-10: Handed back for testing as 3.5.1-dev.24.
- 2026-11-10: Diff view's title dropped at the user's request; the page opens with a bordered details panel: on the left, the node (linked), approver and map file; on the right, the Approved vs Current table. Unverified in a browser.
- 2026-11-10: Handed back for testing as 3.5.1-dev.25.
- 2026-11-10: Details panel split into two tables, left and right justified: *Approval Diff* (Node, Approver, Map file) and Approved vs Current.
- 2026-11-10: Handed back for testing as 3.5.1-dev.26.
- 2026-11-10: Labels revised with the user: File; Commit hash (hash only), Commit date and Stamp date in place of Introduced and Stamped.
- 2026-11-10: Handed back for testing as 3.5.1-dev.27.
- 2026-11-10: Rows settled with the user: Fingerprint, Stamp date, First committed (hash) and "on" (its date), making plain that a stamp records no commit and the viewer finds the first commit holding that text.
- 2026-11-10: Handed back for testing as 3.5.1-dev.28.
- 2026-11-10: Diff details panel set in a smaller font.
- 2026-11-10: Handed back for testing as 3.5.1-dev.29.
- 2026-11-10: *Delta* heading removed; *Current* renamed *Current Node*, in a smaller grey heading.
- 2026-11-10: Handed back for testing as 3.5.1-dev.30.
- 2026-11-10: File labels above the trees removed at the user's request: every file's part of the tree is now shaded with its name at the top right on hover, the shades alternating grey and green from file to file (map.md grey, a branch file green, a second tree grey). Unverified in a browser.
- 2026-11-10: Handed back for testing as 3.5.1-dev.31.
- 2026-11-10: Navigation links on node pages stacked one per line, as in the markdown, at the user's request; the index and map-root links moved to a smaller line beneath. Found and fixed on the way: links were read only from the node's first 11 lines, so a node with many children lost some.
- 2026-11-10: Handed back for testing as 3.5.1-dev.32.
- 2026-11-10: Links above the node removed at the user's request, the tree covering navigation; the per-file index page, now unreachable, removed with them.
- 2026-11-10: Handed back for testing as 3.5.1-dev.33.
- 2026-11-10: Code review with the user, then a tidy pass: CSS and script moved out of the f-string into plain constants, one rule per line, grouped; leftovers from removed features (stale comments, unused `stamps()` and `CYAN`, an unused `nav` rule) removed; every file read now goes through one guarded, cached reader, closing a gap where a map link like `../x.md#y` let the tree read outside the map's directory (shown before and after on a scratch map); stamp dates escaped. Every demo page renders the same as before, ignoring whitespace; CSS differs only in the removed rules; fingerprint test passes.
- 2026-11-10: Third-party libraries considered with the user: only a markdown renderer would earn its place, deferred to the next change, since it costs the script's run-anywhere quality.
- 2026-11-10: Handed back as 3.5.1-dev.34.
- 2026-11-10: Change 320 (*Retrospective diff*) closed by the user as delivered here: the approval diff finds the approved text in git by fingerprint and diffs it against current. Its parked file deleted; it remains in git history. Resolved.
- 2026-11-10: Deviation from the no-map-edits Bounds, at the user's request: *Map Viewer* added to `map.md` under *NDD Project*, describing the prototype, with a callout that it is a proof of concept; stamped (e6383ba4), 742 characters.
- 2026-11-10: *NDD Project* gains the *Map Viewer* child link and bullet, and its scope sentence the tooling prototyped beside the method; stamped (8f112952).
- 2026-11-10: *Contents* in `map.md` lists *Map Viewer*.
- 2026-11-10: *Fingerprint Check* now says the map viewer agrees on the fingerprints, linking to *Map Viewer*; stamped (80ee4e2f), 822 characters, accepted over the bound. Resolves the open item.

## Conclude

Re-agreed in Build as read-only, with edits and approvals left to the agent. Beyond the plan: self-contained, with a demo builder, and the approval diff, which delivered change 320, now closed. Against the Bounds, at the user's request, `map.md` gained *Map Viewer* and *Fingerprint Check* its check. Known limits for the next change: a minimal hand-rolled renderer, a git history walk on every diff, and no tests of the viewer beyond fingerprints.
