# Stamp key rename

**Change Style:** Formal \
**Version:** 3.9.0-dev

## Intent

A node's stamps should sit under a `signers:` key rather than `approvals:`. A project already using NDD should be able to move its maps across in one step its agent takes after upgrading, with every stamp kept and still current.

## Context

Raised as an aside on 2026-11-19 during 320. The sign-off terminology change (archived 2026-11-17) renamed approval to sign-off throughout but kept the `approvals:` key unchanged; a rename would touch every stamped map, the fingerprint helper, the viewer and their tests. Discussed 2026-11-19: `signers:` chosen over `sign-offs:`, as each key is a signer in *Signer*'s sense, a requested stamp included. Suggested route: the helper and viewer read both keys for a while, a migrate command rewrites a map, and the changelog names it.

## Change Specification

Migration notes are left to the changelog: 330's entry carries a migration paragraph, as the changelog standard already provides, naming the migrate command (user, 2026-11-19; an installer-collected `MIGRATION.md` was declined for now).

Planned edits, each target node written whole and stamped on approval, in this order, in [targets.md](2026-11-20-stamp-key-rename/targets.md); promoted in Build (whole-map copies dropped at the user's request as too heavy for five small edits):

1. *Sign-off Stamp* (method map): stamps under `signers:`; an older `approvals:` key is still read, and renamed whenever a stamp is written.
2. *Fingerprint Helper* (method map): `--migrate` renames the key, one map file at a time.
3. *Sign-off Button* (project map): stamps written under `signers:`.
4. *Fingerprint Check* (testing map): the old key read, and migrate checked.
5. *Map Viewer Check* (testing map): a stamp under the old key shown, and renamed on sign-off.

Every stamp key in NDD's own maps is then rewritten in Build by the migrate command; fingerprints exclude the scaffolding block, so no stamp moves.

## Progress

- 1 drafted, ~765 characters, written in place between draft markers.
- 1 approved, ~765 characters, fingerprint cb1a7ae5; the stamp goes on at promotion.
- 2 drafted (~775 characters, ~822 counting the example block), surfaced, not yet approved; written above between draft markers on pause.
- 2026-11-19, paused. Next: approval of 2, then 3 *Sign-off Button*, 4 *Fingerprint Check*, 5 *Map Viewer Check*; then the Intent trim and plan approval. Build claims a version (minor, 3.9.0-dev, to confirm), and the changelog entry carries a migration paragraph naming `--migrate`.
- 2026-11-20, resumed. 2 approved as drafted (cut of "still read meanwhile" offered, not taken), ~800 characters prose, ~995 with example block (recount), fingerprint 02d8acfc; the stamp goes on at promotion.
- 2 reopened for size (~995 is the count; the example block is not excluded). Written whole above as a draft for the user to review and cut. Cuts offered: the example block (−208), the quoting sentence (−55), "so a map in several files…" (−50), "still read meanwhile" (−22), "no fingerprint moves" (−22). 3 *Sign-off Button* is surfaced (~834, flagged) and awaits approval; its draft adds to an existing `approvals:` key rather than renaming it.
- 2 approved as rewritten by the user, with three fixes (node-name bullet, dash, POS line), ~708 characters, fingerprint 9e1df54b; the stamp goes on at promotion.
- 1 reopened and approved: the old-key rule added (read as `signers:`, renamed whenever a stamp is written), the drift sentence cut; ~762 characters, fingerprint 6b3fa92c, superseding cb1a7ae5. 3 redrafted to say `signers:` only (~794), awaiting approval.
- 3 approved: `signers:` only, ~794 characters. Target is the live node with that one-word change; not yet written whole here. Fingerprint b562b2ef.
- Trial of full target nodes (user, 2026-11-20): first written whole inside the change, which interrupted its flow; moved to the companion file `targets.md`, where `fingerprint.py` checks the stamps. If it works, a candidate recommendation: full stamped targets in a companion file even for small edits, where a whole-map copy is too heavy.
- 4 approved with two cuts (opening sentence, "standard library only…"): old-key read and `--migrate` cases added; ~789 characters, fingerprint b7905cbd, written to `targets.md`.
- 350 *Target nodes file* opened, parked, to carry the targets.md recommendation into the method once this trial concludes.
- 5 approved with two cuts (`build_demo_map.py` clause, internet-access sentence, the latter noted in 160): old-key display and rename-on-write checked; ~775 characters, fingerprint 9affd6ea, written to `targets.md`. Change Specification complete; next the Intent trim, then plan approval.
- Edit list brought in line with the approved targets (1, 2, 5), approved.
- Intent trimmed (sign-off terminology clause cut, Context owns it), ~228 characters, approved.
- Plan approved 2026-11-20.

## Log

- 2026-11-20, Build Lock taken. Change Specification reconciled: targets drafted today from the live nodes, no drift.
- 2026-11-20, version 3.9.0-dev claimed, a minor bump.
- Helper: `--migrate` added (scaffolding key only), version 1.3.0. Viewer: writes under `signers:`, renaming an older key, version 0.6.0. Tests: older-key read and migrate cases in `fingerprint_test.py`, its inline stamps moved to `signers:`; demo map gains *Older Key* (builder 0.5.0) and a rename-on-sign-off check. All tests pass (fingerprint, viewer with page-script parse via the nodeenv Node, browser, install).
- Promoted into the live maps, per node, no drift: *Sign-off Stamp*, *Fingerprint Helper* (method map), *Sign-off Button* (project map), *Fingerprint Check*, *Map Viewer Check* (testing map).
- `--migrate` run over `map.md` (13), `method/ndd.map.md` (75), `testing.map.md` (4) and the two test fixtures (6, 5); no fingerprint moved, nothing due for tearne. Example `approvals:` blocks quoted in fixture prose left alone, as they are hashed. All tests pass again.
- The viewer's internal `approvals_html` renamed `stamps_html`; viewer and browser tests pass.
- `changes/resume.md` deleted: its only entry, this change's 2026-11-19 pause, was resumed (should have gone at resume).
- At Archiving, Tidy found *Sign-off Stamp* at ~875 with its example block (miscounted ~762 at approval). Trimmed with approval: "simply" and "and most maps never gain one" cut, example reduced to one stamp; ~799, restamped 097db66c. `targets.md` keeps the text as approved in plan.

## Conclude

Completed. Beyond the plan: the demo map gained an *Older Key* node, and the test fixtures and the reference test's inline stamps moved to `signers:`; the viewer's `approvals_html` became `stamps_html`. Targets were trialled as full stamped nodes in `targets.md`, parked as 350 for the method. *Map Viewer Check*'s internet-access sentence, cut for size, now waits in 160.
