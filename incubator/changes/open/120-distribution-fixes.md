# Distribution and bootstrap fixes

**Mode:** Formal

## Intent

Make the shipping machinery correct before go-live — all buildable in the current layout. Known things to fix:

- Point `install.sh` and the BOOTSTRAP one-liner at `raw.githubusercontent.com/tearne/ndd/main`, retiring the dated-release assumption.
- Give the method a human-facing semver and its own changelog, so a consumer can say which version they run and read what changed.
- Make `BOOTSTRAP.md` consumer-pure and give the repo its own `INTERNAL_BOOTSTRAP.md` to run off.

## Approach

### Distribution source: `main` is the latest

`install.sh` fetches from `raw.githubusercontent.com/tearne/ndd/main/…` (the `NDD_BASE_URL` default), matching the BOOTSTRAP one-liner; the dated-release model and its `releases/latest/download` URL are dropped. `main` is the single moving edge, with no release-cutting step to maintain.

### The method carries a human version and its own changelog

The `ndd-version` marker stays, but now holds a human-readable **semver** rather than a dated release or a commit SHA — it answers "which version are you running?" in a form a colleague can read off and compare. The version is a plain string in `map.md` that the installer ships verbatim, bumped as NDD dogfoods its own Build lifecycle; there is no separate release step and the installer needs no API call.

Alongside it the method ships its own **`CHANGELOG.md`**, fetched into `ndd/CHANGELOG.md` — inside the vendored method directory, namespaced away from the consumer's own `changes/` tree so the two change-management stories never blur. This is the human migration path: compare your old marker to the new, read the changelog entries between them.

### Migration keeps the prev-map diff as the agent's fallback

`install.sh` still backs up the prior map as `ndd.prev.md`. The changelog is the human "what changed"; the prev-map diff is what the agent reads for precise, mechanical migration reasoning. The two serve different readers and both stay.

### Shippable BOOTSTRAP is decoupled from the repo's own bootstrap

`BOOTSTRAP.md` is authored purely for consumers (references `ndd/ndd.md`) and the installer ships it verbatim into `ndd/`. The repo operates off a separate `INTERNAL_BOOTSTRAP.md` instead — a thin dev instruction pointing at the root `map.md` — which `CLAUDE.md` imports and the installer never ships. One shippable file stays clean for consumers while the repo keeps its own operating instructions.

## Plan

- [ ] Point `install.sh`'s `NDD_BASE_URL` default at `raw.githubusercontent.com/tearne/ndd/main`.
- [ ] Have `install.sh` also fetch `CHANGELOG.md` into `ndd/CHANGELOG.md`, retaining the `ndd.prev.md` backup step.
- [ ] Set `map.md`'s version marker to `1.0.0`.
- [ ] Add repo-root `CHANGELOG.md` with an initial `1.0.0` entry.
- [ ] Rewrite `BOOTSTRAP.md` to consumer paths (`ndd/ndd.md`) with a migration story keyed on the version marker and `ndd/CHANGELOG.md`, noting the agent may diff `ndd.prev.md` for precision.
- [ ] Add `INTERNAL_BOOTSTRAP.md` carrying the repo's own dev instruction, and repoint `CLAUDE.md` at it.
- [ ] Re-test the installer against a local mock: fresh install, upgrade with `.prev` backup plus changelog, foreign-content refusal.

## Unresolved

- Initial semver value for the first shipped marker — `0.1.0` (pre-go-live) or `1.0.0` (treat go-live as the 1.0)? This sets both the `map.md` marker and the first `CHANGELOG.md` entry.
