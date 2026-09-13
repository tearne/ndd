# Packaging, distribution and upgrade

## Intent

An adopting project needs to pull later improvements to the method, or it ossifies at the version it first installed — and the old file-copying model was built for the document-based method, so there's no distribution story yet. The move: a `curl … | bash` installer that downloads the latest released method — a clean `ndd/ndd.md` plus a `ndd/BOOTSTRAP.md` carrying orientation and update logic — wires up `CLAUDE.md`, and can be re-run to upgrade in place. Flagged **critical before public go-live**; does not gate the incubator's own internal go-live.

## Approach

### The map stays pure; BOOTSTRAP.md stays separate

The method ships as two files, not one folded file: `ndd/ndd.md` holds the conceptual method untouched, and `ndd/BOOTSTRAP.md` holds the operational layer — prohibited actions, the pointer to the Startup Scan, and the update logic. Keeping them apart respects the split between what the method *is* (conceptual, the map) and how an agent *acts on it* (operational, the bootstrap); folding the bootstrap into the map would pollute it to buy a single-file convenience the installer already provides. This also means the change barely touches `map.md`.

### Installed under a namespaced `ndd/` directory

The method files land in a dedicated `ndd/` directory so the method's map can't collide with the consumer's own root `map.md`, and so the vendored files read as "don't hand-edit". `CLAUDE.md` at the root points at `@ndd/BOOTSTRAP.md`; the consumer's own `map.md` and `changes/` live at the project root. The `changes/open`, `changes/archive`, and `active.md` structure the method already describes is the consumer's, at their root.

### Curl-bash installer, dated releases, clean-replace upgrade

A `curl … | bash` one-liner fetches a small installer that downloads the latest dated release of the `ndd/` files from a stable GitHub latest-release URL, creates or updates the root entry files, and ensures `.gitignore`. It replaces `opt-in.py` and its uv/document-based machinery. Releases are dated on the existing `YYYY-MM-DD[.N]` scheme; the filename stays stable (`ndd/ndd.md`) with the version recorded in an embedded marker rather than in the filename.

### Root entry files: CLAUDE.md and AGENTS.md, both to the bootstrap

The installer writes both `CLAUDE.md` (Claude-specific) and `AGENTS.md` (the cross-agent convention) at the project root, so the method bootstraps whatever agent a consumer runs. `CLAUDE.md` uses the `@ndd/BOOTSTRAP.md` import; `AGENTS.md` carries a plain "read `ndd/BOOTSTRAP.md`" instruction, since the `@` import is Claude-specific. The installer owns both — writes if absent, upgrades its own pointer in place, refuses foreign content and warns to add the pointer manually.

### Ambient, gitignored install — git-free migration via a .prev backup

The whole install is treated as ambient dev tooling, like `node_modules`: `ndd/`, `CLAUDE.md`, `AGENTS.md`, and `.claude/` are gitignored and re-materialised by re-running the installer on a fresh checkout. On upgrade, the installer renames the existing `ndd/ndd.md` to `ndd/ndd.prev.md` before writing the new one, so the standing instruction in `BOOTSTRAP.md` can diff current against prior — two files on disk, no git coupling. The tradeoff: the method version isn't pinned to project history, exactly as dependency tooling already behaves.

### Build scope: everything in-repo now, publishing at go-live

This change builds what is self-contained to the repo — the augmented `BOOTSTRAP.md` with update logic, the version marker, the installer script written against the eventual `ndd` repo path — and defers only cutting the first public dated release and the repo rename, which can't be exercised until the repo is `ndd` and public. The incubator itself stays the source of truth at its root (`map.md`, `BOOTSTRAP.md`); it does not vendor itself into an `ndd/` directory.

### The version marker lives in the map

The embedded `YYYY-MM-DD[.N]` marker sits in `ndd/ndd.md` itself, co-located with the content the migration diff examines, so a `.prev` backup carries its own version and the diff is fully self-describing. This is the one spot the otherwise-pure map file carries operational metadata.

## Plan

**Topics**

- Write the `curl … | bash` installer targeting the `ndd` repo: fetch `ndd/ndd.md` and `ndd/BOOTSTRAP.md` from the stable latest-release URL into a local `ndd/` directory; on an existing install, back up `ndd/ndd.md` to `ndd/ndd.prev.md` before overwriting.

- Have the installer write and own the root entry files — `CLAUDE.md` (`@ndd/BOOTSTRAP.md` import) and `AGENTS.md` (plain "read `ndd/BOOTSTRAP.md`" instruction) — creating or upgrading its own pointer, refusing foreign content with a warning.

- Have the installer ensure `.gitignore` covers `ndd/`, `CLAUDE.md`, `AGENTS.md`, and `.claude/`.

- Add the standing update-and-migration instruction to `BOOTSTRAP.md`: compare the embedded version marker to the latest release and, when newer, diff `ndd/ndd.md` against `ndd/ndd.prev.md` and surface whether the project's own `map.md` or open changes need adjusting.

- Embed the dated version marker in the method map, sourced from the release.

**Done when** a fresh install and a re-run upgrade both succeed against a local mock release — producing the `ndd/` layout, both owned entry files, the `.gitignore` entries, and a `.prev` backup on upgrade — and `BOOTSTRAP.md` carries the migration instruction. Cutting the first public release and settling the in-repo release path remain for go-live.

## Log

- Installer written as `install.sh` at the incubator root, with `NDD_BASE_URL` overridable (defaulting to the `tearne/ndd` latest-release URL) so it can be exercised against a `file://` mock. Entry-file ownership is idempotent via a content compare; foreign content is refused with a warning naming the pointer to add.
- The staying-up-to-date section in `BOOTSTRAP.md` points its `curl … | bash` one-liner at `raw.githubusercontent.com/tearne/ndd/main/install.sh`; that exact path is provisional until the repo rename and release path settle at go-live.
- Tested against a local mock release: fresh install produced the `ndd/` layout, both owned entry files and the four `.gitignore` entries (no `.prev`); a re-run upgrade produced `ndd/ndd.prev.md` holding the old version and `ndd/ndd.md` the new, with no duplicate gitignore lines; foreign `CLAUDE.md` was left untouched with a warning.
- **Naming tension for review:** `BOOTSTRAP.md`'s existing "the `map.md` alongside this file is authoritative" line addresses the dev-repo layout, but the new update instruction it now sits beside references the consumer layout (`ndd/ndd.md`, `ndd/ndd.prev.md`). One shared BOOTSTRAP can't cleanly address both dev repo and consumer at once. Left as-is rather than redesigned mid-build — needs a deliberate decision (likely resolved by the go-live reorg, when the incubator becomes the `ndd` repo and BOOTSTRAP addresses consumer paths with the dev repo as the exception).

## Conclusion

Built as planned: `install.sh`, the BOOTSTRAP update/migration section, and the map version marker, all tested against a local mock release.

Two extensions were raised and declined during build. Seeding `.claude/settings.local.json` was rejected as opinionated, security-sensitive, and Claude-specific against the cross-agent stance. Renaming the incubator's own `map.md` to `ndd.md` was declined too: BOOTSTRAP ships verbatim to consumers, so a single file can't address both layouts literally, and this repo already treats itself as a special case (per the README's dev-repo-vs-consumer split) — the clean separation of the incubator's own operating instructions from the shippable consumer BOOTSTRAP is a go-live reorg decision, left flagged in the Log.

No map concepts touched beyond the operational version marker.
