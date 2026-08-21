# Go-live reorg and first public release

**Mode:** _(to propose after Intent approval)_

## Intent

Shape the repo for public use and prove it ships. Known things to fix:

- Rename the repo to `ndd`; lift the incubator's contents to the repo root so the repo *is* the method.
- Settle the distribution source: treat `main` as latest via `raw.githubusercontent.com`, retiring the dated-release assumption — reconcile the installer's `NDD_BASE_URL` with the one-liner.
- Decide how the shippable consumer BOOTSTRAP is produced separately from this repo's own operating instructions (the dev-vs-consumer split change 70 flagged).
- Prove the `curl … | bash` installer end-to-end against the live URL.
