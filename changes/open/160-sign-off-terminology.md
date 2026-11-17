# Sign-off terminology

**Change Style:** Formal

## Intent

The method's prose should call a person's recorded approval of a node's text a **sign-off**, keeping *approval* for the gating yes given in chat, so the two are never confused. The `approvals:` key in the scaffolding block stays as it is, noted once as where sign-offs are kept.

## Context

Raised by the user on 2026-11-16 while planning 140 Web UI approvals, which found the two senses of "approving" blurred: the yes that settles a draft (*Approval*) and the stamp recording who approved which text (*Approval Stamp*, *Sign-off*). Keeping the key avoids a migration for every stamped map. About 24 method-map nodes and *AGENT-RULES.md* use "stamp", "approved" or "approver", some in the gating sense, so each needs judging. 140 writes "sign-off" in the nodes it touches, a pattern for this change.

## Change Specification

Drafted on copies of `method/ndd.map.md` and `method/AGENT-RULES.md` in [160-sign-off-terminology/](160-sign-off-terminology/), taken 2026-11-17 before any edit.

Worklist, 2026-11-17: 33 method-map nodes use "approv…", "stamp" or "sign-off", and `AGENT-RULES.md` 39 times. Triage by sense:

- Gating sense only, likely unchanged, each to be confirmed: *Orient Then Focus*, *Gates and Permissions*, *Approval*, *Drafts*, *Diffs*, *Discussion Conclude*, *Change Lifecycle*, *Lifecycle Flow Reads*, *Plan*, *Intent*, *Unresolved*, *Build Lock*, *Archiving*, *Change Style*, *Trivial*, *Formal Build*, *Formal Conclude*, *Versioning*, *Standards*.
- Sign-off sense, to be edited: *NDD*, *Node Identity*, *Approval Stamp*, *Fingerprint*, *Fingerprint Helper*, *Node Sizing*, *Engagement Rule*, *Change Specification*, *Maintenance*, *Shape*, *Sign-off*, *Approver*, *Map Viewer*, then *Contents* for any rename.
- `AGENT-RULES.md`, a non-map target, re-rendered to match.
- The viewer's labels in `method/util/map_viewer.py` and the mentions in `method/util/fingerprint.py`, non-map targets.
- Project map *Map Viewer*, *Map Viewer Sign-off*; testing map *Map Viewer Check*, *Map Viewer Browser Check*, and its link to *Approval Stamp*.

## Unresolved

1. Settled: *Approval Stamp* is renamed *Sign-off Stamp*. Every link repoints, including one in `testing.map.md`, and the two mentions in `method/util/fingerprint.py`.
2. Settled: *Approver* is renamed *Signer*, chosen over "Sign-off Approver" since the `approvals:` key is untouched by any node name and "approver" was the blurred word. Its links repoint, two of them in `AGENT-RULES.md`.
3. Settled: folded in. The viewer's visible labels ("Approval Diff", "Approver", "Approved fingerprint", "the approved text") and the project and testing map nodes describing it (*Map Viewer*, *Map Viewer Sign-off*, *Map Viewer Check*, *Map Viewer Browser Check*) take the sign-off terms; the `/approval` route and code identifiers stay. Copies of `map.md` and `testing.map.md` added to the companion folder, identical to the live files.
