# Distribution and bootstrap fixes

**Mode:** Formal

## Intent

Make the shipping machinery correct before go-live — all buildable in the current layout. Known things to fix:

- Point `install.sh` and the BOOTSTRAP one-liner at `raw.githubusercontent.com/tearne/ndd/main`, retiring the dated-release assumption.
- Drop the version marker; migration keys off the `ndd.prev.md` diff.
- Make `BOOTSTRAP.md` consumer-pure and give the repo its own `INTERNAL_BOOTSTRAP.md` to run off.

## Approach

### Distribution source: `main` is the latest

`install.sh` fetches from `raw.githubusercontent.com/tearne/ndd/main/…` (the `NDD_BASE_URL` default), matching the BOOTSTRAP one-liner; the dated-release model and its `releases/latest/download` URL are dropped. `main` is the single moving edge, with no release-cutting step to maintain. The embedded version marker loses its anchor and is dropped — migration keys off the `ndd.md` vs `ndd.prev.md` diff, which never needed it — and BOOTSTRAP's update instruction becomes "re-run the installer; if `ndd.prev.md` differs, diff and assess."

### Shippable BOOTSTRAP is decoupled from the repo's own bootstrap

`BOOTSTRAP.md` is authored purely for consumers (references `ndd/ndd.md`) and the installer ships it verbatim into `ndd/`. The repo operates off a separate `INTERNAL_BOOTSTRAP.md` instead — a thin dev instruction pointing at the root `map.md` — which `CLAUDE.md` imports and the installer never ships. One shippable file stays clean for consumers while the repo keeps its own operating instructions.

## Plan

- [ ] Point `install.sh`'s `NDD_BASE_URL` default at `raw.githubusercontent.com/tearne/ndd/main`.
- [ ] Remove the version marker from `map.md`.
- [ ] Rewrite `BOOTSTRAP.md` to consumer paths (`ndd/ndd.md`) and replace the version-marker update instruction with the `ndd.prev.md` diff.
- [ ] Add `INTERNAL_BOOTSTRAP.md` carrying the repo's own dev instruction, and repoint `CLAUDE.md` at it.
- [ ] Re-test the installer against a local mock: fresh install, upgrade with `.prev` backup, foreign-content refusal.
