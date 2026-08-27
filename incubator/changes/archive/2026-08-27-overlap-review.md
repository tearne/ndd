# Review overlap between Style, map guidance, and Bootstrap

**Mode:** Explore

## Intent

Three artefacts now carry writing/coding guidance that may overlap or contradict: the `standards/STYLE.md` guide (suggested code style), the map's own **Writing Style** guidance (how map *nodes* are written), and `BOOTSTRAP.md` (how an agent orients and what rules bind it). Before go-live these should be reconciled so a consumer meets one clear account, not three partly-redundant ones.

Review the three, identify genuine overlap versus legitimately-distinct concerns (code style vs map-node prose style vs orientation rules), and decide what — if anything — to deduplicate, cross-reference, or move. The outcome may be no change, targeted edits, or a pointer between artefacts; the point is a deliberate decision rather than drift.

Precursor to go-live (130): fold into the pre-retirement pass alongside 125.

## Approach

### Treat the three as distinct by target, not candidates to merge

`STYLE.md` governs the code agents write on user projects, the map's *Writing Style* subtree governs map-node prose, and `BOOTSTRAP.md` governs agent orientation. They serve different audiences and lifecycles, so reconciliation means removing redundancy at the seams — not consolidating three concerns into one account.

### Drop `BOOTSTRAP.md` from the style reconciliation

It carries orientation and binding rules, no writing or coding guidance. It was named in the Intent as a precaution; the review confirms no style overlap, so it leaves this pass (bar being a possible home for a pointer).

### Outcome is a consistency check, not edits

The overlaps found are narrow and legitimate. The soft-wrap rule in `STYLE.md` #6 and map *Formatting* serves two different audiences (project code vs map prose), so stating it in both is acceptable local duplication, not redundancy to remove. The `STYLE.md` #4 vs *Conceptual Writing* domain-language echo is too loose to link. So the deliverable is confirmation that the three don't *contradict* each other — an edit lands only if an actual contradiction surfaces.

## Plan

**Topics**

- Cross-read `STYLE.md` against the map's *Writing Style* subtree (*Conceptual Writing*, *Formatting*) for any direct contradiction, not just overlap.

- Confirm `BOOTSTRAP.md` carries no writing/coding guidance that could conflict.

**Done when** the three are confirmed mutually non-contradictory; any genuine contradiction found is either corrected in place or, if it needs a decision, logged for the user.

## Log

- Review completed with no edits. Cross-read confirmed the soft-wrap rule (`STYLE.md` #6 vs map *Formatting*) states the same direction — acceptable two-audience duplication, not a contradiction. `STYLE.md` #4 and *Conceptual Writing* agree in spirit on domain language. `BOOTSTRAP.md` carries no writing/coding guidance. Three artefacts confirmed mutually non-contradictory.

## Conclusion

Completed with no edits. `STYLE.md`, the map's *Writing Style* subtree, and `BOOTSTRAP.md` were confirmed mutually non-contradictory; the sole overlap (the soft-wrap rule) is intentional two-audience duplication, kept as-is. No map catch-up, no changelog entry, no version bump.
