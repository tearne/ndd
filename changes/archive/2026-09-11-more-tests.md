# More tests

**Cadence:** Explore

## Intent

_(Approved 2026-09-11.)_

Grow the Testing branch beyond the fingerprint. Two candidates already known: the installer refusing to run inside this repository, and an approval stamp for a person whose name has spaces, which the helper mis-read until fixed by hand and the fixtures do not cover. Each test is a node under Testing stating what must hold and how it is verified, with its runnable form under `tests/`, following the shape the Fingerprint Check set.

## Context

Parked from change 275's Held (2026-09-11), numbered to run right after it. On approving the Intent the user noted these may not be two tests, but are two items to think about.

## Approach

_(Approved 2026-09-11.)_

- **The spaced name joins Fingerprint Check's fixtures rather than becoming a test.** That check already runs the helper; it gains a stamp for "Alice Smith" and an assertion on `--due`. Hashes are unchanged, since stamps are scaffolding.

- **The installer gets a node, *Install Check*, and `tests/install_test.py`.** It installs into a temporary directory and asserts: refusal from its own checkout, the shipped file set, pointer entry files, executable scripts, every link resolving; then installs again over a changed `ndd.map.md` and a retired file, asserting the backup and the removal. It prints the shipped file list so a stray file is still seen.

- **Release Steps step 2 folds into "run every test"**, since the install test covers what it asked a person to check by eye.

- **The installer ships every file git tracks except `CLAUDE.md` and `AGENTS.md`.** _(Added in Build, 2026-09-11, on the user's call; supersedes 275's exclusion list.)_ No list to maintain, and a file ships once committed.

- **Standard library only**, like the reference, so the test reads whole and shares nothing with what it tests.

- **Testing's overview and the branch Contents follow; the method map is untouched** unless something falls out.

## Worklist

_(Approved 2026-09-11.)_

**Topics**

1. **Fingerprint fixtures.** A stamp for "Alice Smith" in both fixtures, and the reference test asserting the helper's `--due` output for her and for `expected`.

2. **Install test.** `tests/install_test.py`: fresh install into a temporary directory, the assertions in the Approach, then the upgrade pass, printing the shipped file list.

3. **Map.** The *Install Check* node in `testing.map.md`, negotiated; Testing's overview line, the branch Contents, and Release Steps losing step 2.

4. **Observation.** Anything the method map turns out to need, logged and carried to Conclude.

**Done when** both tests pass from a clean checkout and the map describes all of it.

## Log
- 2026-09-11 — Topic 1 done: "Alice Smith" stamped on Plain Prose and Full Sections in both fixtures; the reference test asserts the helper's `--due` listing for her and for `expected` in each file. Confirmed the assertion fails against the pre-fix helper (six due instead of four).
- 2026-09-11 — Topic 2 done: `tests/install_test.py` passes: refusal from own checkout, shipped set equals checkout minus residue (15 files, printed), pointer entry files, executable scripts, every link resolves, upgrade backs up `ndd.map.md` and removes a retired file. Observation for topic 4: the install test itself ships, but `install.py` does not, so in a client's `ndd/tests/` it cannot run; a test that only matters here is now in the shipped set. Raised with the user before the node is drafted.
- 2026-09-11 — User chose to exclude the install test by name: `tests/install_test.py` joins the residue list, the first file-level entry, so `is_residue` matches a whole path or a top-level name. Both tests pass; 14 files ship.
- 2026-09-11 — **Shipping rule changed on the user's call**, superseding the exclusion list from 275: the installer ships every file git tracks except `CLAUDE.md` and `AGENTS.md`, read from `git ls-files`. No residue list; `changes/`, `README.md`, `install.py` and `.gitignore` now ship; the install test needs no exclusion and can run in a client against `ndd/install.py`. New files ship once committed, so the untracked files of this change (the install test) do not ship until added, which is git's to do. The link check is scoped to markdown outside `changes/`, whose records cite the map by bare anchor. Install test passes: 58 files ship at present.
- 2026-09-11 — Install Check written (527) after the user cut a preamble that only restated the Sync Rule. Then, on the user's yes, the Testing node moved from `map.md` into `testing.map.md` as the branch's top node, Contents its first child, so the file has one top as Map Files expects; trunk link, Contents and Release Steps re-pointed. Tidy found the trunk root had never gained a child link to Testing (only the overview line): added. The Testing node's overview list gained an Install Check line during the move, which was ahead of its approval; surfaced.
- 2026-09-11 — Topic 3 done: Testing overview line, branch Contents, Release Steps down to two steps (519), Installer re-described for tracked files (814). Topic 4: nothing for the method map; Map Files' one-top-node-per-file shape held once Testing moved into its file, so the observation is that a branch file's top node is the hanging node's child, as the NDD branch already showed. Done-when: both tests pass; the install test is untracked and awaits `git add`, which is the user's.

## Conclude

_(Approved 2026-09-11.)_

Landed as one new node, Install Check, beside a widened Fingerprint Check, with Testing moved into `testing.map.md` as the branch's top node. The shipping rule changed on the way: every file git tracks ships except the two entry files, superseding the exclusion list from 275, so the install test and the change records ship too. Release Steps is two steps, bump and test. The install test is untracked until added, and ships once it is.
