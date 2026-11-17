# Sign-off terminology

**Change Style:** Formal \
**Version:** 3.7.4-dev

## Intent

The method's prose, and the map viewer that ships with it, should call a person's recorded approval of a node's text a **sign-off**, keeping *approval* for the gating yes given in chat, so the two are never confused. The `approvals:` key in the scaffolding block stays as it is, noted once as where sign-offs are kept.

## Context

Raised by the user on 2026-11-16 while planning 140 Web UI approvals, which found the two senses of "approving" blurred: the yes that settles a draft (*Approval*) and the stamp recording who approved which text (*Approval Stamp*, *Sign-off*). Keeping the key avoids a migration for every stamped map. About 24 method-map nodes and *AGENT-RULES.md* use "stamp", "approved" or "approver", some in the gating sense, so each needs judging. 140 writes "sign-off" in the nodes it touches, a pattern for this change.

## Change Specification

Drafted on copies in a companion folder, of `method/ndd.map.md` and `method/AGENT-RULES.md` taken 2026-11-17 before any edit, then of `map.md`, `testing.map.md` and the two scripts; promoted in Build, and the folder dropped at Archiving.

Worklist, 2026-11-17: 33 method-map nodes use "approv…", "stamp" or "sign-off", and `AGENT-RULES.md` 39 times. Triage by sense:

- Gating sense only, likely unchanged, each to be confirmed: *Orient Then Focus*, *Gates and Permissions*, *Approval*, *Drafts*, *Diffs*, *Discussion Conclude*, *Change Lifecycle*, *Lifecycle Flow Reads*, *Plan*, *Intent*, *Unresolved*, *Build Lock*, *Archiving*, *Change Style*, *Trivial*, *Formal Build*, *Formal Conclude*, *Versioning*, *Standards*.
- Sign-off sense, to be edited: *NDD*, *Node Identity*, *Approval Stamp*, *Fingerprint*, *Fingerprint Helper*, *Node Sizing*, *Engagement Rule*, *Change Specification*, *Maintenance*, *Shape*, *Sign-off*, *Approver*, *Map Viewer*, then *Contents* for any rename.
- `AGENT-RULES.md`, a non-map target, re-rendered to match.
- The viewer's labels in `method/util/map_viewer.py` and the mentions in `method/util/fingerprint.py`, non-map targets.
- Project map *Map Viewer*, *Map Viewer Sign-off*; testing map *Map Viewer Check*, *Map Viewer Browser Check*, and its link to *Approval Stamp*.

Gating-sense nodes confirmed unchanged, 2026-11-17: all 19 above, plus *Engagement Rule*, whose "approval, which stamps the node" is the gating yes. *Formal Conclude*'s "per-node approved element" is also the gating sense.

Edits, in order:

1. *Sign-off Stamp*, renamed from *Approval Stamp*, with links to it repointed.
2. *Signer*, renamed from *Approver*, with links repointed.
3. *Sign-off*.
4. *Node Identity*.
5. *Fingerprint*.
6. *Fingerprint Helper*.
7. *Node Sizing*.
8. *Change Specification*.
9. *Maintenance*.
10. *Shape*.
11. *Map Viewer* (method map).
12. *Contents* (method map).
13. *Map Viewer* (project map).
14. *Map Viewer Sign-off* (project map).
15. *Map Viewer Check* (testing map), and *Fingerprint Check*, which says "approval stamps".
16. *Map Viewer Browser Check* (testing map).
17. `AGENT-RULES.md`.
18. `method/util/map_viewer.py` labels.
19. `method/util/fingerprint.py` mentions.

Progress, with Unresolved items 1 to 3 settled and folded in (*Sign-off Stamp*, *Signer*, the viewer's wording in scope):

- 1 approved, 684 characters, stamped 064255d3; nav links in *Node* and *Fingerprint* repointed.
- 2 approved, 665 characters, stamped daeff2c7; *Sign-off*'s child link repointed.
- 3 approved, 719 characters, stamped 13a3fa18.
- 4 approved, 679 characters, stamped e785da72.
- 5 approved, 748 characters, stamped 68af75d3.
- 6 approved, 773 characters, stamped a2b17a20; also no longer says only the agent writes stamps.
- 7 approved, 792 characters, stamped a17361fe.
- 8 approved, 785 characters, stamped 6393ee2f.
- 9 approved, stamped 76076420.
- 10 approved, 436 characters, stamped 80d2a65e.
- 11 approved, 768 characters, stamped 1cb0db0a.
- 2026-11-17: the user delegated approval of the remaining edits unless one seems subtle, which is to be surfaced.
- 12 approved under the delegation, *Contents* renamed entries.
- 13 to 16 approved under the delegation: project map *Map Viewer* (118b1d17, 669) and *Map Viewer Sign-off* (a51b491b, 776), the viewer's diff page now called "Sign-off diff"; testing map *Fingerprint Check* (8855620d, 832, over the bound as before), *Map Viewer Check* (7e9d1192, 763), *Map Viewer Browser Check* (a06ac3cc, 781).
- 18 and 19 approved under the delegation: copies of `map_viewer.py` and `fingerprint.py` in the companion folder. Viewer labels "Sign-off Diff", "Signer", "Signed-off fingerprint", "Signed off", "the signed-off text"; comments to match; `/approval` route and identifiers unchanged.
- 17 approved: `AGENT-RULES.md` *Engagement Rule: Edit Order* says "signer's stamp" and links *Signer*; exempted from *Rule Testing* by the user, as a term rename that changes no meaning.

## Conclude

The scope grew to the map viewer and NDD's own maps, the Intent amended to match. *Approval Stamp* became *Sign-off Stamp* and *Approver* *Signer*. *Fingerprint Helper* also lost its stale claim that only the agent writes stamps. The rules file's rename was exempted from Rule Testing.

## Log

- 2026-11-17: Build Lock taken; version 3.7.4-dev claimed, a patch bump. Live files unchanged since the baseline.
- 2026-11-17: promoted from the companion folder, whole files: `method/ndd.map.md`, `map.md`, `testing.map.md`, `method/AGENT-RULES.md`, `method/util/map_viewer.py`, `method/util/fingerprint.py`. Every stamp in the three maps is current, and all four test scripts pass.
