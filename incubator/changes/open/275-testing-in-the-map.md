# Testing in the map

**Cadence:** Explore

## Intent

_(Approved 2026-09-11.)_

Try testing in this project's own map before designing anything for the method. The Fingerprint rule is the candidate: every agent must produce the same hash for the same node, a property that wants a runnable check. Put that check where a project would naturally keep one, a branch of the project map stating what must hold and how it is run, with the script beside it, and read off what convention the method map then needs. Since branches already live in their own files, the answer may be nothing.

## Context

Parked via aside during change 80's build (2026-09-10); numbered 275 to run just before go-live. That build proved the Fingerprint rule with a throwaway script that was not kept. The original Intent asked for a method-level convention for specifying tests; on 2026-09-11 the user redirected it to trying testing in this project first, since map files already let a branch live in its own file.

## Approach

_(Approved 2026-09-11.)_

- **A *Testing* node hangs off the trunk, beside Distribution, with its branch in `testing.map.md`.** Testing is how this repository checks itself, trunk material like Distribution, and a branch in its own file is the mechanism the Intent wants to exercise.

- **`testing.map.md` ships, and so do the script and fixtures under `tests/`.** _(Revised in Build, 2026-09-11; originally the script stayed behind.)_ The project map already ships, so a child link into an unshipped file would dangle in a client's copy. The Fingerprint node forbids computing a hash by reasoning, so every client agent must run code, and a shipped reference is the direct way to have every agent get the same answer.

- **The map states the property and names the check; the script is not embedded.** Code in the map would be a second copy of the rule, and the map describes what exists rather than carrying it.

- **The check is a single POS-style Python file, `tests/fingerprint.py`.** POS is the project's standard for small scripts, and one file with a `uv` shebang runs anywhere. It prints the fingerprint of a named node in a map file, and with `--check` verifies itself.

- **Self-check runs against a frozen fixture, `tests/fixture.map.md`, whose cases and expected hashes are listed in the branch's *Detail*.** Live nodes change, so their hashes cannot be expected values. The fixture holds the cases the approval-mechanics trial covered, such as whitespace-only edits and renamed child links, and listing them in the map lets any agent test its understanding before writing a stamp, script or no script.

- **The same script is what an agent runs here at Sign-off.** A kept script replaces a throwaway per session, and using it for real tests whether the branch's description is enough.

- **Release Steps gains running the check as its third step.** A release that broke the script or its hashes would ship a wrong worked example. Edited once the script runs, since the map describes what exists.

- **The method map is touched only if what falls out demands it.** Conclude records the finding; any node in `ndd.map.md` is a negotiated edit proposed then, not planned now.

## Worklist

_(Approved 2026-09-11.)_

**Topics**

1. **Script and fixture.** `tests/fingerprint.py` in POS style, printing a named node's fingerprint from a map file and verifying itself with `--check`; `tests/fixture.map.md` holding the cases from the approval-mechanics trial, with expected hashes derived by running the script and cross-checked by a second, independent computation.

2. **Testing branch.** A *Testing* node on the trunk and its branch in `testing.map.md`, each node drafted, counted and negotiated in turn: what must hold, how it is checked, and the fixture cases with their hashes in *Detail*. Contents and the trunk's overview follow.

3. **Distribution follow-through.** `testing.map.md` added to the installer's shipped list, Release Steps gaining the check as step three, and a scratch install run to confirm every link resolves.

4. **Method pointer.** The Fingerprint node's *Detail* gains one sentence directing an agent to verify its implementation against the Testing cases before use, negotiated as a map edit once the branch exists. Anything else the method map turns out to need is noted in the Log and carried to Conclude.

**Done when** `./tests/fingerprint.py --check` passes, a scratch install resolves every link including the shipped branch, and the map describes all of it.

## Held

- Further checks for the Testing branch, e.g. that the installer refuses to install into this repository. Raised by the user 2026-09-11 while approving the Testing node.

## Log

- 2026-09-11 — Topic 1: two fixture files rather than the one the Approach named, `tests/fixture.map.md` and `tests/fixture-edited.map.md`, because headings must be unique within a file, so a "same node after a meaning-free edit" case needs a second file. Each fixture node carries a stamp for a person called `expected`, so `--check` is the Sign-off due-queue run against known answers: only the unstamped Bare Heading is due in the original; only Changed Prose, Renamed Child and the root Fixture (whose prose was edited to say it is the copy) are due in the edited copy. Hashes cross-checked by an independent awk/tr/sha256sum pipeline: they agree.
- 2026-09-11 — Topic 4 observations from writing the script. The Fingerprint rule left three things for the implementer to decide: (a) "next heading" is taken as any ATX heading of any level outside a fenced block, so a `#` inside a code block does not end a node; (b) a navigation-link line is a line that is solely one markdown link, and only such lines between the heading and the scaffolding block are dropped; (c) the scaffolding block is a `yaml` fence that follows the links directly, so a yaml example later in *Detail* is kept. None contradicts the node; whether any needs stating in the method map is for Conclude.
- 2026-09-11 — Approach decision 2 revised on the user's call while drafting the Testing node: the script and fixtures ship under `ndd/tests/`, not only the branch file. Reason: fingerprints only work if every agent computes the same one, and separate implementations would diverge on the interpretation choices logged above. Topic 3 adds `tests` to the shipped list alongside `testing.map.md`.
- 2026-09-11 — **Paused mid-build; lock kept.** State: topic 1 done (`tests/fingerprint.py`, `tests/fixture.map.md`, `tests/fixture-edited.map.md`, `--check` passes). Topic 2: the *Testing* node is approved and written at the end of `map.md`; its child link to `testing.map.md#fingerprint-check` does not resolve yet because the branch file is not written, and the root overview line and Contents entries were drafted but not approved. **Resume there:** surface the two trunk edits again (root node lands at 900 characters, user to say split or accept), then draft node 2 of 2, *Fingerprint Check*, in `testing.map.md` with the fixture cases and hashes in *Detail* (original: Fixture ab9e6f02, Plain Prose bcf6b47b, Full Sections 3a096aaf, Child 250ae92a, Bare Heading 6bcce17f, Changed Prose 275d67bd; edited: Fixture 5fd5a260, Renamed Child 103b2b33, Changed Prose 618c09de, others unchanged). Then topics 3 and 4. Nothing committed.
