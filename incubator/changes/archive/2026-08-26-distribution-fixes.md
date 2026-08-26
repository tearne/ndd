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

### The method's version lives in its changelog, not a hidden marker

The method ships its own **`CHANGELOG.md`**, fetched into `ndd/CHANGELOG.md` — inside the vendored method directory, namespaced away from the consumer's own `changes/` tree so the two change-management stories never blur. Its top heading (`## X.Y.Z — date`) *is* the version: a human semver a colleague can read off with `head`, answering "which version are you running?" without an embedded `<!-- ndd-version -->` comment to hunt for. A versioned filename was rejected too — `main` is a versionless source, and a versioned name would churn every stable reference each release. The changelog is both the version label and the human migration narrative.

### Migration keeps the prev-map diff as the agent's fallback; the installer is idempotent

`install.sh` backs up the prior map as `ndd.prev.md` — but only when the fetched map actually differs, so a redundant re-run is a no-op that preserves the last real backup. The changelog is the human "what changed"; the prev-map diff is what the agent reads for precise, mechanical migration reasoning.

### One shipped BOOTSTRAP; the repo's dev instruction lives in `CLAUDE.md`

`BOOTSTRAP.md` is authored purely for consumers (references `ndd.md`) and the installer ships it verbatim into `ndd/`. The repo's own operating instruction — read `map.md`, run the Startup Scan, no writes without an active change — is short, so it lives inline in the repo's `CLAUDE.md` rather than in a parallel bootstrap file. That keeps exactly one bootstrap *document* (the shipped one) and treats the repo's rules as ordinary project config, not a second variant to keep in sync.

## Plan

- [x] Point `install.sh`'s `NDD_BASE_URL` default at `raw.githubusercontent.com/tearne/ndd/main`.
- [x] Have `install.sh` also fetch `CHANGELOG.md` into `ndd/CHANGELOG.md`.
- [x] Make `install.sh` idempotent: fetch `ndd.md` beside the old copy and rotate to `ndd.prev.md` only when it changed.
- [x] Add repo-root `CHANGELOG.md` with an initial `1.0.0` entry noting NDD's succession from COD; its top heading is the version (no embedded marker).
- [x] Rewrite `BOOTSTRAP.md` to consumer paths (`ndd.md`) with a migration story keyed on the `CHANGELOG.md` heading, noting the agent may diff `ndd.prev.md` for precision.
- [x] Inline the repo's own dev bootstrap directly into `CLAUDE.md` (no separate bootstrap file), leaving `BOOTSTRAP.md` as the single shipped bootstrap document.
- [x] Re-test the installer against a local mock: fresh install, upgrade, redundant re-run (backup preserved), foreign-content refusal.

## Log

- The old `BOOTSTRAP.md` was serving double duty and had drifted inconsistent — it named `map.md` for the "map is authoritative" step but `ndd/ndd.md` in the update section. The consumer/internal split resolved this: `BOOTSTRAP.md` is now uniformly consumer (`ndd.md`), `INTERNAL_BOOTSTRAP.md` uniformly repo (`map.md`).
- Installer re-tested via a `file://` mock across fresh install, upgrade (prev-backup + changelog), and foreign-content refusal — all pass.
- On review, the consumer/internal *split into two bootstrap files* felt uncomfortable; reworked so the repo's dev instruction is inlined into `CLAUDE.md` and only `BOOTSTRAP.md` remains as a bootstrap document. Added an NDD-succeeds-COD note to the `1.0.0` changelog entry.
- On review the `<!-- ndd-version -->` marker was dropped entirely: the version already lives human-visibly as the top heading of `CHANGELOG.md`, so a hidden HTML marker (and a versioned filename) were both redundant. `map.md` no longer carries a marker.
- A backup idempotency flaw surfaced during the map catch-up: the installer backed up unconditionally, so a redundant re-run clobbered `ndd.prev.md` with a copy of the current map. Fixed to rotate only on change; verified by a triple-run test.
- Map catch-up done alongside (per-node, negotiated): the installer/distribution was entirely unmapped. Added a `Distribution` node under META, with META's child links + description and the Contents tree updated to match.

## Conclusion

Plan shifted during review, all folded in: the version marker was dropped in favour of the `CHANGELOG.md` top heading; the bootstrap split landed as one shipped `BOOTSTRAP.md` plus the repo's dev instruction inlined into `CLAUDE.md`, not a separate file; and an installer idempotency flaw — redundant runs clobbered `ndd.prev.md` — was found and fixed. Map catch-up added a `Distribution` node under META. No separate changelog entry: this work is part of the initial `1.0.0` release the changelog already records.
