# Installer review

## Purpose

Review how the installer works as a whole, which may be more complex than is desirable. Raised during 040's build (2026-10-30), when the install test failed on an uncommitted deletion.

## Observations

- The installer ships every git-tracked file except `CLAUDE.md` and `AGENTS.md`, so NDD's own `changes/` tree — open changes, archive, `process-feedback.md`, any `resume.md` — lands in every client's `ndd/`.
- It lists files from git's index but reads them from disk, so a deletion not yet committed crashes it with `FileNotFoundError` before the entry files are written.
- Retired files are removed only if named in `RETIRED_FILES`; 080 proposes pruning whatever isn't shipped instead.

## Open questions

- What should a client install contain, and should that be listed by inclusion rather than exclusion?
- Which of the installer's jobs — copying, map backup, entry-file ownership, retiring — earn their place?

## Related

- [080 Installer prunes unshipped](080-installer-prunes-unshipped.md): may fold into whatever this discussion concludes.
