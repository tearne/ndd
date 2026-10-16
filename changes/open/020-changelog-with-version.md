# Changelog with version

**Change Style:** Formal

## Intent

Present versioning consistently, from one node the others link to, so Build, Archiving, Release Steps and the standards stop disagreeing on when a version exists: a project with a changelog is versioned, in semver. Support a release gathering several changes across sessions without presenting interim versions as releasable, and report what awaits release.

Raised as an aside (2026-10-14).

## Change Specification

Targets: whole-map copies at `020-changelog-with-version/ndd.map.md` and `020-changelog-with-version/map.md`.

## Implementation Plan

Re-agreed mid-Build on 2026-10-16 with the lock kept. Build ran on scope recorded only in an invented *Status* section, and landed non-map edits without surfacing them. Nothing is reverted up front; each item is surfaced as a diff with its count and settled on approval, one at a time, in this order:

1. Replace *Status* with a *Log* entry recording the deviation and what a resuming session needs.
2. Release Steps in `map.md`: approve and stamp.
3. 020's version bump: agree the kind; 020 claims its version.
4. AGENT-RULES rule 1: approve the wording.
5. AGENT-RULES rule 19: approve the wording.
6. Remove `standards/VERSIONING.md`, settling Held item 3: drop its row from Standards, and decide whether "prefer patch when in doubt" moves to Versioning.
7. `standards/CHANGELOG.md`: approve, with its references to `VERSIONING.md` redirected and the dated format dropped.
8. Versioning: say a project is versioned when it keeps a changelog, in semver; the nodes that say "versioned" already link there.
9. Standards: the changelog row drops "dated or semver".
10. `install.py`: list `standards/VERSIONING.md` in `RETIRED_FILES`, so upgrades remove it.

A rejected item is redrafted or reverted, as the user chooses. Build hands back once all ten are settled.

## Log

- 2026-10-16: Build entered on approval, on a plan summary read from an invented *Status* section, not from plan parts. No drift from baseline; both targets promoted in bulk. Landed: the `CHANGELOG.md` simulation (approved in planning), AGENT-RULES rules 1 and 19 and both standards (never surfaced). Release Steps settled in planning but unstamped. Distribution was checked in planning and needs no edit. The Implementation Plan was re-agreed to settle each of these.

- 2026-10-16: Implementation Plan 1 of 7 settled: *Status* replaced by this Log.

- 2026-10-16: 2 of 7 settled: Release Steps approved, stamped `adc6d0a5`.

- 2026-10-16: 3 of 7 settled: minor bump agreed; 020 claims `2.5.0-dev`.

- 2026-10-16: 4 of 7 settled: AGENT-RULES rule 1 approved as landed (552 characters).

- 2026-10-16: 5 of 7 settled: AGENT-RULES rule 19 approved with "one review" reworded to name the Map Review and its scopes (837 characters, over ~800); simplification parked as 070.

- 2026-10-16: Implementation Plan items 6 and 7 re-agreed: `VERSIONING.md` is removed rather than approved, since semver and Versioning now carry it.

- 2026-10-16: 6 of 7, part 1: Standards row for `VERSIONING.md` removed, stamped `fe979c88`.

- 2026-10-16: 6 of 7, part 2: "prefer patch" moved to Versioning's Detail, re-stamped `7f14bb96` (895 characters, over ~800).

- 2026-10-16: 6 of 7 settled: `standards/VERSIONING.md` deleted; Held item 3 settled with it.

- 2026-10-16: Intent revised during item 7: a project with a changelog is versioned, in semver; the dated changelog format goes.

- 2026-10-16: Implementation Plan re-agreed with items 8 and 9 added.

- 2026-10-16: 7 of 9 settled: `standards/CHANGELOG.md` rewritten semver-only, references redirected to Versioning.

- 2026-10-16: 8 of 9 settled: Versioning defines a versioned project, suffixes `-dev` from build start, folds Detail into the hand-back bullet and drops "prefer patch" (undoing 6 part 2); re-stamped `b89f3dcc`, 826 characters.

- 2026-10-16: 9 of 9 settled: Standards changelog row drops "dated or semver", re-stamped `af27ef94`.

- 2026-10-16: Surprise: deleting `standards/VERSIONING.md` breaks the install test until the deletion is staged (installer ships `git ls-files`), and existing installs keep the file unless `install.py`'s `RETIRED_FILES` lists it. Not in the plan.

- 2026-10-16: Implementation Plan re-agreed with item 10; 10 of 10 settled: `RETIRED_FILES` lists `standards/VERSIONING.md`. Tests pass. Pruning unshipped files parked as 080.

## Conclude

Build entered on a plan summary from an invented *Status* section, and AGENT-RULES rules 1 and 19 and both standards landed unsurfaced; the Implementation Plan was re-agreed mid-Build to settle each. Deviations: the Intent now makes a project with a changelog versioned, in semver, so the dated format went; `standards/VERSIONING.md` was deleted, not updated, and `install.py` retires it; `-dev` applies from build start; Release Steps gained its stamp. Parked: 060, 070, 080.
