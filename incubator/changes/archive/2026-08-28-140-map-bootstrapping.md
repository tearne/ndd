# Map bootstrapping / no-map adoption path

**Mode:** Explore

## Intent

_(Approved 2026-08-28. Cadence: Explore.)_

NDD installs cleanly but leaves a project unable to *start*: a fresh opt-in produces no project map and no `changes/` tree, yet the **Startup Scan** assumes both, and **BOOTSTRAP** conflates the read-only *method* map (`ndd/ndd.md`) with the *project* map the user actually builds. Give NDD a defined bootstrapping path — from fresh install to a first project map worth maintaining — covering both greenfield and existing-codebase adoption, with the method/project map distinction made explicit. Graceful for simple projects; no heavy ceremony.

Parked from change 130 (go-live §C, orphan 4(ii)); activated ahead of 130 because go-live is pointless if a project can't acquire its first map.

## Approach

Decisions (each with its reason):

- **Project map lives at `map.md` in the project root.** Matches the convention BOOTSTRAP already implies ("this project's own `map.md`") and the self-hosting example (`incubator/map.md`), and keeps a clean split from the vendored method map at `ndd/ndd.md`.
- **Bootstrapping is the ordinary change lifecycle applied to an empty tree, not a parallel ceremony.** Keeps new machinery minimal and degrades gracefully; the only addition is an *entry ramp* that gets a fresh project to the point where the normal lifecycle can run.
- **Two entry modes share one ramp.** *Greenfield*: seed a root-only project map, then grow via normal changes. *Existing-codebase adoption*: the agent surveys the code and *proposes* initial nodes, negotiated one node at a time per **Interaction Grain** — never a bulk map dump. This reuses the codebase-research instruction folded into **Approach (a2r)** by 130 orphan 4(i).
- **BOOTSTRAP draws the method-map vs project-map distinction explicitly.** Rewrite its "The map is authoritative" section to name both: `ndd/ndd.md` = read-only method reference (how to work); `map.md` = the project map the user builds and maintains (the actual work).
- **The method map gains a Bootstrapping concept node**, so the path is documented in the method itself rather than living only in BOOTSTRAP prose. It sits under **Change-Management** as a sibling of **Startup Scan**, which links to it — bootstrapping is the entry into the lifecycle when no project map exists yet.
- **The installer stays pure method-vendoring; bootstrapping is agent-detected.** `opt-in.py` is unchanged (honouring Distribution's "leaves the consumer's own map and changes untouched"). Instead, **Startup Scan** gains a degradation: no `map.md` + no `changes/` tree ⇒ fresh project ⇒ the agent offers to bootstrap, keeping first-map creation a negotiated activity rather than a mechanical stub.
- **Greenfield seeds a root-only map.** The first project map is a single root node named for the project; everything else grows via the normal change lifecycle. Adoption instead surveys the code and proposes nodes one at a time.
- **140 owns all bootstrapping-related BOOTSTRAP and method-map edits; 130 keeps its go-live reorg + README cleanup.** 140 lands first, so 130 resumes and adapts on top — no simultaneous edits to the same sections.
- **Existing documentation is migrated by invitation, incrementally — never swallowed during bootstrap.** An adopted project often already has spec docs, READMEs, design notes. Rather than absorbing them wholesale into the initial map, the ramp seeds a minimal map from the code survey, then *invites the user to open a change* to consider migrating that existing documentation — in small, bite-sized changes at the pace they prefer. This keeps bootstrapping light, reinforces "bootstrapping is the ordinary lifecycle on an empty tree," and honours per-node negotiation (**Interaction Grain**).

## Topics

Areas to work (Explore — no fixed step list):

- **Method-map edits.** Add the **Bootstrapping** node (under Change-Management, sibling of Startup Scan); add the Startup-Scan fresh-project degradation; make the project-map-at-`map.md` convention explicit where the map references it. Per-node negotiation per the **Engagement Rule** during build.
- **BOOTSTRAP rewrite.** Draw the method-map (`ndd/ndd.md`, read-only) vs project-map (`map.md`, the work) distinction; point the agent at `map.md` as the thing it builds; describe the fresh-project entry ramp.
- **Entry ramp definition.** Specify the actual first-run flow and resolve its chicken-and-egg: the agent first creates the `changes/` tree (always writable), then runs a normal first change to seed `map.md`. Greenfield → root-only node; existing-codebase → survey and propose initial nodes one at a time per **Interaction Grain**. For adopted projects carrying existing documentation (spec docs, design notes, READMEs), the ramp closes by *inviting the user to open a change* to consider migrating that material into the map incrementally, in bite-sized changes at their chosen pace — not folding it in during bootstrap.
- **Fresh-project proof.** Validate end-to-end: run `opt-in.py` into an empty directory and into a small existing codebase, and confirm the agent can go from install → first maintained node without the Startup Scan breaking.

**Done when:** a fresh opt-in — both greenfield and existing-codebase — reaches a first maintained project map via a documented, graceful ramp: the Startup Scan no longer assumes a pre-existing map/changes tree, BOOTSTRAP distinguishes the two maps, the method map documents bootstrapping, and both an empty-dir and a small-codebase run have been proven to work.

## Log

- **Method-map edits topic — done.** Added **Bootstrapping** node (`b6t`) under Change-Management; added the fresh-project degradation to **Startup Scan** (`x7t`) as an early precondition branch; added the child nav link to **Change-Management** (`cm4`); updated the **Contents** tree (`ct5`). All negotiated one node at a time per Engagement Rule.
- **Two asides parked mid-build:** `150-deferred-map-maintenance` (graceful degradation when the user defers map upkeep) and `160-surface-then-one-at-a-time` (elevate "surface the set, then engage one at a time" to a core principle — a *fourth death*, attention/overwhelm). 160 was prompted by the agent breaching that discipline (proposing three nodes at once); noted for future adherence.
- Startup Scan tidy: converted a long em-dash parenthetical pair to commas per Conceptual Writing (`h3v`) — pre-existing text, fixed while in the node.
- **BOOTSTRAP rewrite topic — done.** Replaced "The map is authoritative" with "Two maps: the method and your project", distinguishing the read-only method map (`ndd/ndd.md`) from the project map (`map.md`); other sections already held up.
- **Fresh-project proof — done.** Ran `opt-in.py` into an empty dir and a small existing codebase (README + `src/`). Both: method vendored under `ndd/`, entry files + gitignore written, and — crucially — no `map.md` / no `changes/` tree, i.e. the exact condition the Startup Scan branch now detects to route to bootstrapping. Brownfield run left existing assets untouched, validating the agent-detect (not installer-scaffold) decision and Distribution's "leaves the consumer's own map and changes untouched". Vendored `ndd.md`/`BOOTSTRAP.md` confirmed to carry the new content. Note: the proof covers install→route machinery; literally seeding a first node needs an interactive agent+user session, which is inherent to the ramp, not automatable here.

## Conclusion

Landed the bootstrapping path across the method map and BOOTSTRAP. Added the **Bootstrapping** node (`b6t`), a fresh-project precondition branch in **Startup Scan**, its Change-Management nav link and Contents entry; rewrote BOOTSTRAP's map section into the two-map (method vs project) distinction. Proven by greenfield and brownfield `opt-in.py` runs. No version bump — 1.0.0 is unreleased, so this is part of it. Two asides parked (150, 160). Deviation: activated ahead of 130 (go-live) at the user's call.
