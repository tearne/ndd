# Packaging, distribution and upgrade

## Intent

An adopting project needs to pull later improvements to the method, or it ossifies at the version it first installed — and the old file-copying model was built for the document-based method, so there's no distribution story yet. The move: a `curl … | bash` installer that downloads the latest released method — a clean `ndd/map.md` plus a `ndd/BOOTSTRAP.md` carrying orientation and update logic — wires up `CLAUDE.md`, and can be re-run to upgrade in place. Flagged **critical before public go-live**; does not gate the incubator's own internal go-live.

## Approach

### The map stays pure; BOOTSTRAP.md stays separate

The method ships as two files, not one folded file: `ndd/map.md` holds the conceptual method untouched, and `ndd/BOOTSTRAP.md` holds the operational layer — prohibited actions, the pointer to the Startup Scan, and the update logic. Keeping them apart respects the split between what the method *is* (conceptual, the map) and how an agent *acts on it* (operational, the bootstrap); folding the bootstrap into the map would pollute it to buy a single-file convenience the installer already provides. This also means the change barely touches `map.md`.

### Installed under a namespaced `ndd/` directory

The method files land in a dedicated `ndd/` directory so the method's map can't collide with the consumer's own root `map.md`, and so the vendored files read as "don't hand-edit". `CLAUDE.md` at the root points at `@ndd/BOOTSTRAP.md`; the consumer's own `map.md` and `changes/` live at the project root. The `changes/open`, `changes/archive`, and `active.md` structure the method already describes is the consumer's, at their root.

### Curl-bash installer, dated releases, clean-replace upgrade

A `curl … | bash` one-liner fetches a small installer that downloads the latest dated release of the two `ndd/` files, creates or updates `CLAUDE.md`, and ensures `.gitignore`. It replaces `opt-in.py` and its uv/document-based machinery. Releases are dated on the existing `YYYY-MM-DD[.N]` scheme. Because method files are never hand-edited — a project extends via its own `map.md`, not by touching `ndd/` — upgrade is a clean file-replace: re-run the installer, drop in the newer files, and a standing instruction in `BOOTSTRAP.md` has the agent read the latest, compare against the installed version, and surface whether the project's own `map.md` or open changes need adjusting.

### Build scope: everything in-repo now, publishing at go-live

This change builds what is self-contained to the repo — the `ndd/` layout, the augmented `BOOTSTRAP.md`, the installer script written against the eventual `ndd` repo path — and defers only cutting the first public dated release and the repo rename, which can't be exercised until the repo is `ndd` and public.

## Unresolved

- **Committed vs gitignored method files.** Whether the downloaded `ndd/` files are committed (pinning the method version in the project's history) or gitignored and re-fetched (as the old model did). Affects reproducibility versus repo noise.
- **Update-detection mechanism.** How the standing instruction spots a newer release — e.g. curl the latest file and compare a version marker embedded in it, versus checking a releases endpoint. Needs to work with nothing but `curl` available.
- **Installer's CLAUDE.md handling.** Whether it fully owns `CLAUDE.md` (as `opt-in.py` did, refusing foreign content) or appends its pointer alongside existing content, given consumers may already have a `CLAUDE.md`.
