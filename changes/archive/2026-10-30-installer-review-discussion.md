# Installer review

## Purpose

Review how the installer works as a whole, which may be more complex than is desirable. Raised during 040's build (2026-10-30), when the install test failed on an uncommitted deletion.

## Conclude

The installer is to ship only what a client needs at run time, from an explicit list, written fresh into a cleared `ndd/` from the checkout's disk; `.gitignore` entries become conditional. Promoted as [095 Installer simplification](../open/095-installer-simplification.md), which absorbs 080, discarded. Dropped: shipping from git, which only mattered while the file list came from git. Tests stop shipping, reversing the *Testing* entry; 095's build updates `map.md` to match.

## Agreements

- A client's `ndd/` holds only what the agent and user need at run time, not the repository as it stands (2026-10-30): `AGENT-RULES.md`, the three maps, `util/fingerprint.py`, `standards/`, `CHANGELOG.md`, `README.md` and `LICENSE`. `changes/`, `install.py`, `.gitignore` and `tests/` stop shipping. Tests are run only in the checkout, reversing the *Testing* entry's "shipped so clients have access to tests which matter"; `testing.map.md` still ships, its `tests/` mentions describing the checkout. The set is an explicit list in the installer; the install test's link check catches a linked file left off it.
- Each run clears `ndd/` and copies the listed files fresh from the checkout's disk, keeping the old `ndd.map.md` as `ndd.prev.map.md` if it changed (2026-10-30). Git is not involved: the crash came from mixing git's file list with disk contents, a clean checkout after `git pull` matches its commit anyway, and shipping uncommitted edits lets NDD development be tried in a client. `RETIRED_FILES` goes, and 080 is subsumed.
- `.gitignore` gains `ndd/` always; `CLAUDE.md` and `AGENTS.md` only when the installer creates them, since an existing one is the project's own; `.claude/` unless the project already has files under it checked in (2026-10-30).

## Observations

- The installer ships every git-tracked file except `CLAUDE.md` and `AGENTS.md`, so NDD's own `changes/` tree — open changes, archive, `process-feedback.md`, any `resume.md` — lands in every client's `ndd/`.
- It lists files from git's index but reads them from disk, so a deletion not yet committed crashes it with `FileNotFoundError` before the entry files are written.
- Retired files are removed only if named in `RETIRED_FILES`; 080 proposes pruning whatever isn't shipped instead.

## Open questions

None. Entry-file ownership and the guards (own checkout, virtual environment, `--version`) were reviewed and kept as they are.

## Related

- 080 Installer prunes unshipped: subsumed by the fresh-write update model, discarded as merged into 095.
- [095 Installer simplification](../open/095-installer-simplification.md): the change promoted from this discussion.
