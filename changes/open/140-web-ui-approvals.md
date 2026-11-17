# Web UI approvals

**Change Style:** Formal \
**Version:** 3.7.0-dev

## Intent

The map viewer should let whoever is at the screen record a named person's sign-off on the node shown, as well as through the agent. Settle how the signer is named when the viewer has no login, and what the viewer may write.

## Context

Raised as item 7 of 002 Map viewer iteration on 2026-11-16 and spun out at the user's request. Today an approval is a yes given in reply to the agent asking, and the agent writes the stamp. It reverses a decision: tooling development (archived 2026-11-10) first built an approve form, then re-agreed the viewer as read-only, for security and because review edits are better made through the agent. The viewer serves on 127.0.0.1 only, reached by port forwarding. The user's case: sharing the viewer in a meeting, talking stakeholders through the nodes, and recording each one's sign-off in front of them.

## Change Specification

The agreed nodes are in copies of the live maps in [140-web-ui-approvals/](140-web-ui-approvals/): `map.md`, `testing.map.md` and `method/ndd.map.md`, taken 2026-11-16 before any edit. Each node edit was approved and stamped in the copies:

1. *Sign-off* (method map): signs off, written by the agent or in the map viewer. Stamped 983960ae.
2. *Map Viewer* (method map): records sign-offs, refuses writes from other web pages. 774 characters, stamped 3e7b921e.
3. *Map Viewer* (project map): no longer read-only, writes nothing but sign-offs; child links to the two new nodes; a *Sign off* bullet. 669 characters after the user's edit, stamped 47a8585f.
4. *Map Viewer Sign-off* (project map, new): the button and its drop-down of names, the stamp written, and a red light while the repository has uncommitted changes; no commit from the browser. 777 characters, stamped 5db241d8.
5. *Map Viewer Security* (project map, new): forged form, DNS rebinding and stale page, each with its guard; Host 127.0.0.1 or localhost. 671 characters, stamped 7268bf69.
6. *Map Viewer Check* (testing map): sign-off checks, the stamp written and the file untouched on each guard's refusal; `viewer_demo.py` renamed `build_demo_map.py`, as it builds a demo map, folded in at the user's request though outside the Intent. 763 characters, stamped 8de533ff.
7. *Map Viewer Browser Check* (testing map): the *Sign off* button flow and the uncommitted-changes light. 783 characters, stamped 490f0ceb.
8. *Contents* (project map): entries for the two new nodes.

The rename is a `git mv` of `tests/map_viewer/viewer_demo.py`, updating its usage comment and the call in `map_viewer_test.py`. No Implementation Plan: no consequential delivery choices remain.

The demo map's *Linked Map* gains children, *Linked Branch* with *Linked Leaf* beneath it and *Second Child*, so its tree looks like a map; folded in at the user's request, outside the Intent.

## Log

- 2026-11-17: Build Lock taken.
- 2026-11-17: version 3.7.0-dev claimed, a minor bump.
- 2026-11-17: Change Specification re-agreed with the lock kept: method map *Map Viewer* trimmed to 774 characters, stamped 3e7b921e, the button's mechanics left to the project map's *Map Viewer Sign-off*.
- 2026-11-17: user edited the project map's *Map Viewer* in the copy (POS link, shorter shipping line, markdown-rendering sentence cut), now 669 characters; its stamp ef72c7b7 is stale, approved and re-stamped 47a8585f. Resolved.
- 2026-11-17: `viewer_demo.py` renamed `build_demo_map.py` by `git mv`; its usage comment, marker text and the call in `map_viewer_test.py` updated.
- 2026-11-17: demo *Linked Map* given *Linked Branch* (with *Linked Leaf*) and *Second Child*; both test suites pass.
- 2026-11-17: viewer 0.4.0: run token, Host check on every request and Origin on writes, sign-offs by POST only to `/signoff`, the receipt checked against disk, stamps written under `approvals:` (key added if absent, a name's earlier stamp replaced, a colon quoted) by atomic replace, the *Sign off* button and drop-down, the uncommitted-changes light; header comment and `--help` no longer say read-only.
- 2026-11-17: `map_viewer_test.py` gains sign-off checks on a copy (stamps written; refusals for a changed node, no or wrong token, GET, PUT, foreign or missing Origin, foreign Host, file untouched) and a foreign-Host page read refused; `browser_test.py` gains the *Sign off* flow and the light, committed away on the copy. All four test scripts pass; mutating out the Host and Origin checks fails five checks.
- 2026-11-17: surprise: the Host check as specified refuses `localhost:8080`, and a forward to a different local port (`ssh -L 9000:127.0.0.1:8080`), since the Host must be 127.0.0.1 at the viewer's own port. Raised with the user. Resolved: *Map Viewer Security* re-agreed with the lock kept, Host 127.0.0.1 or localhost at any port, Origin matching the Host; 671 characters, stamped 7268bf69. Viewer and tests updated; all four test scripts pass.
- 2026-11-17: promoted into the live map, whole files as the live maps had not drifted from the copies' baseline: `map.md` (*Map Viewer*, *Map Viewer Sign-off*, *Map Viewer Security*, *Contents*), `testing.map.md` (*Map Viewer Check*, *Map Viewer Browser Check*), `method/ndd.map.md` (*Sign-off*, *Map Viewer*). Each live fingerprint matches its stamp.
- 2026-11-17: handed back for testing as 3.7.0-dev.1.
