# Go-live reorg

**Mode:** Formal

## Intent

_(Approved 2026-08-28. Cadence: Formal. **Paused** to plan+build 140-map-bootstrapping first — no point shipping go-live if a project can't acquire its first map. Resume at Approach once 140 lands.)_

Flip the repo from incubation to the live method, so the repository itself *is* NDD rather than a framework incubated inside it. Today the live method lives in `incubator/` while the repo root still holds the superseded COD framework (`agent/`, the old root `opt-in.py`, `PRINCIPLES.md`, old root `README`/`CHANGELOG`, `CLAUDE.md.bk`, and the old root `changes/`). Go-live lifts `incubator/`'s contents to the root and retires the old framework, then renames the GitHub repo to `ndd`, makes it public, and proves the clone-and-run `opt-in.py` install end-to-end against the live repo. The blocking work has landed: distribution fixes (120), standards migration (125, now `standards/`), and the installer switch (128, which retired `install.sh` for `opt-in.py`) — so the install proof is the local-clone flow, not `curl … | bash`.

Note: repo rename, visibility change, and any branch/merge/push are user-performed — the agent never runs git-write or GitHub-admin operations on its own initiative.

<!-- ============================================================= -->
<!-- SCRATCH / WIP — parity check DONE. §C orphans all resolved.   -->
<!-- Resume point: get Intent approval, then propose Cadence,       -->
<!-- write Approach + worklist.                                     -->
<!-- ============================================================= -->

## Planning notes (WIP)

**Lifecycle status:** 130 is in Plan. Intent has been **revised to current reality** (above) and is **awaiting approval**. §A/§B/§C parity all settled (§C orphans resolved this session). No Cadence proposed yet. No active lock. Next: Intent approval → Cadence → Approach → worklist.

### User decisions taken this session

- **Keep COD changelog history.** NDD is COD's continuation, so present one lineage: NDD semver entries on top, COD's dated history preserved below (e.g. under a "Predecessor: COD" heading). **Open sub-decision:** does NDD 1.0.0 stay as-is or re-anchor onto COD's version line? Touches the VERSIONING standard — resolve in Approach.
- **Keep the old `changes/archive/`** (37 COD change records) — the method's development record. Lift into the unified `changes/archive/` (or a marked `archive/cod/`), don't drop.

### A. Cleanly replaced — safe to delete on go-live

- `agent/ADDITIONAL/{POS,RUST,VERSIONING}.md`, `agent/STYLE.md` → **identical** in `incubator/standards/`.
- `agent/ADDITIONAL/CHANGELOG.md` → `incubator/standards/CHANGELOG.md`; loading semantics (`ADDITIONAL/README.md`) → map **Standards (s9d)**.
- old root `opt-in.py` → `incubator/opt-in.py` (128).
- `agent/MAP-GUIDANCE.md` → **fully covered** by map Specification subtree (24/24 rules mapped: Node, Navigation Links, Map Structure, Node Sizing, Conceptual Writing, Formatting, Node Sections, Callouts, Sync Rule, Engagement Rule, Edit Governance, Conceptual Drift, etc.).
- `agent/KEYWORDS.md` → **fully covered** by map **Process Keyword** + **Aside Keyword**.
- `agent/PROCESS.md` → ~28/32 covered by Change-Management subtree; residual gaps in §C.
- `agent/README.md` → Startup Scan / Gates / Cadences cover it; its "version-upgrade procedure" is **covered in `BOOTSTRAP.md` → Staying up to date** (agent missed this — verified present, line 31). Not an orphan.
- `CLAUDE.md.bk` (`@README.md` + `@agent/README.md`) → obsolete; new entry is `incubator/CLAUDE.md` → `@ndd/BOOTSTRAP.md`.
- `changes/process-feedback.md` → empty (header only), nothing to preserve.
- `incubator/changes/agent/2026-06-10/` → legacy pre-128 snapshot of the `agent/` files; superseded by `ndd/` vendoring (128 log deferred its cleanup to 130).

### B. History (decided: keep — see user decisions)

- root `CHANGELOG.md` (124 lines, COD method history) — absorb into NDD changelog.
- root `changes/archive/` (37 records) — lift/keep.

### C. TRUE ORPHANS — need disposition before deleting source (RESUME HERE)

Each: decide fold-into-map vs. preserve-doc vs. accept-loss.

1. **PRINCIPLES.md rationale depth.** ✅ **RESOLVED — accept-loss on all four sub-threads.** (b) unbundling diagnosis is covered by Non-Dead Design root ("three deaths") + Principles overview; (c) peak-tree urgency is already in **Trees over Graphs (g6t)**; (d) the "three binding constraints" framing is carried implicitly (the principles *are* the binding constraints). (a) the paradigm-progression analogy (type systems → FP → ownership/borrow → conceptual maintainability) is **deliberately dropped**: the analogy leans on *deterministic, sound enforcement* — a decision procedure that makes the violation structurally unexpressible — whereas NDD's agent is a stochastic translator that guarantees nothing, and its real safeguard is an *activity* (map maintenance) plus a *statistical* cross-check (cross-agent falsifiability). Importing it would smuggle an overclaim into a deliberately terse node and needs too much hedging to earn its place. Original sub-thread text preserved in git history if ever revisited.
2. **Wander Conclusion length exception.** ✅ **RESOLVED — accept universal 500.** The map already routes retrospective detail to the Build **Log**, not Conclude ("its Build Log already carries what happened, so Conclude still just names the landing point"), so the old 1000-for-Wander exception is obsolete. No map edit; the exception simply lapses.
3. **`**Mode:**` line convention.** ✅ **RESOLVED — document it, renaming the label to Cadence.** The convention is real (128/129/130 all carry it) but "Mode" clashes with the map's own word. Fold a one-line mention into **Cadences (e3n)**, and standardise the change-doc title line to `**Cadence:** <name>` to match map vocabulary. (Go-live's own doc line, currently `**Mode:**`, updates too.)
4. **"Read the codebase" in Approach + no-map projects.** ✅ **RESOLVED — split: fold (i), park (ii).**
   - (i) *Research instruction* — fold one line into **Approach (a2r)**: the agent first researches the relevant map nodes (and the code where reality must be verified) to ground its decisions and surface coverage gaps. The map today only asserts research *happens* (Plan, v3d) without instructing the gap-finding, which is arguably more central to NDD than to COD.
   - (ii) *No-map degradation* — accept-loss in go-live; parked as a fresh standalone Intent (`140-map-bootstrapping.md`). This is the adoption/bootstrapping question (Distribution installs the method but the consumer's map starts empty), substantive and orthogonal to go-live's repo-flip purpose — not an Approach one-liner.

### Also fold into 130 scope (already noted)

- `incubator/README.md` has stale lower sections ("Boundary", "Self-contained COD project") referencing the old `agent/` model — clean during go-live, not just lift.
- Git-write / GitHub-admin steps (branch, merge, repo rename, make public, install proof) are **user-performed**.
