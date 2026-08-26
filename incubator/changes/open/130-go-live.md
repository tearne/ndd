# Go-live reorg

**Mode:** _(to propose after Intent approval)_

## Intent

Flip the repo from incubation to the live method. Parked until we're actually ready to go live. Steps:

- Lift the incubator's contents to the repo root so the repo *is* the method (`map.md`, `BOOTSTRAP.md`, `install.sh`, `changes/`, `README.md`).
- Retire the superseded framework: `agent/`, `opt-in.py`, `PRINCIPLES.md` (after a final parity check against the map's Principles subtree), old root `README`/`CHANGELOG`, and the `changes/agent/` snapshot. `STYLE.md` and the `ADDITIONAL/*` guides are only retired once migrated by the standards change (125) — nothing valuable is dropped silently.
- Do the reorg via `git mv` on a dedicated branch, merged when ready.
- Rename the GitHub repo to `ndd`, make it public, and prove the `curl … | bash` installer end-to-end against the live URL.

Depends on the distribution fixes (120, done) and the standards migration (125) landing first.
