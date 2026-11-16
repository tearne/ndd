# Web UI approvals

**Change Style:** Formal

## Intent

The map viewer should let whoever is at the screen record a named person's sign-off on the node shown, as well as through the agent. Settle how the signer is named when the viewer has no login, and what the viewer may write.

## Context

Raised as item 7 of 002 Map viewer iteration on 2026-11-16 and spun out at the user's request. Today an approval is a yes given in reply to the agent asking, and the agent writes the stamp. It reverses a decision: tooling development (archived 2026-11-10) first built an approve form, then re-agreed the viewer as read-only, for security and because review edits are better made through the agent. The viewer serves on 127.0.0.1 only, reached by port forwarding. The user's case: sharing the viewer in a meeting, talking stakeholders through the nodes, and recording each one's sign-off in front of them.

## Change Specification

Drafted on copies of the live maps in [140-web-ui-approvals/](140-web-ui-approvals/): `map.md`, `testing.map.md` and `method/ndd.map.md`, taken 2026-11-16 before any edit.

Progress, 2026-11-16, seven node edits in the copies:

1. *Sign-off* (method map): signs off, written by the agent or in the map viewer. Approved, stamped 983960ae.
2. *Map Viewer* (method map): records sign-offs, refuses writes from other web pages. Approved at 873 characters, stamped ab16b6ce.
3. *Map Viewer* (project map): no longer read-only, writes nothing but sign-offs; child links to the two new nodes; a *Sign off* bullet. Approved, 792 characters, stamped ef72c7b7.
4. *Map Viewer Sign-off* (project map, new): not yet surfaced. Draft text in [140-web-ui-approvals/draft-map-viewer-sign-off.md](140-web-ui-approvals/draft-map-viewer-sign-off.md), 929 characters, over the cap, so trim or split before surfacing. Folds in items 2 and 3.
5. *Map Viewer Security* (project map, new): the two attacks and their guards, as item 4 settled and explained, at the user's request.
6. *Map Viewer Check*: server-side sign-off checks (stamp written, receipt mismatch refused, token and Host checks).
7. *Map Viewer Browser Check*: the button and drop-down flow.

Then, before the plan goes up: method *Contents* and project map *Contents* entries for the new nodes; delete the settled *Unresolved* items once folded into their nodes; consider an Implementation Plan.

## Unresolved

1. Settled: no viewer approval; the viewer gains a sign-off facility, and *Approval* is not involved. Sent the Intent back for revision.
2. Settled: a *Sign off* button in the node's footer, beside its sign-offs; a drop-down of names, several tickable at once, listing every handle in the map's stamps plus names added in that browser, which stay until removed (only added names can be removed); the last ticked are ticked by default, remembered by the browser. Pressing writes one stamp per ticked name. No button on an approval diff.
3. Settled: the viewer writes only the signer's line under `approvals:` in the node's scaffolding block, adding the mapping if absent and overwriting that person's earlier sign-off; no other text, file or git write. The page carries the fingerprint the server computed when rendering it, sent back on sign-off as a receipt; the server recomputes from disk and refuses if they differ, so a sign-off never covers text the signer was not shown.
4. Settled: a random token per run, carried by the viewer's own pages and required on every sign-off, stops a forged cross-site form, since other sites cannot read the pages; a Host check on every request (and Origin on writes) refusing anything but 127.0.0.1:<port> stops DNS rebinding, which would otherwise also let a site read the map, a gap open today; writes by POST only. The specification should give these, with the attacks they stop, a security node under the project map's *Map Viewer*, at the user's request.
5. Settled: parked as 160 Sign-off terminology, prose only, the `approvals:` key kept; 140 writes "sign-off" in the nodes it touches.
