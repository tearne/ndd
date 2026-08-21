# Name the method

## Intent

The method still ships under the placeholder "Unified Map Method" — the root node's callout flags it as a working name only, with the real name left open. Before the new version goes live and adopting projects install under it, settle a real name. The root carries a stable id, so this is a rename that keeps the node's identity intact, but it touches the root heading, the callout, and every navigation link and prose reference that names the method — so it wants doing deliberately, once, ahead of distribution.

## Approach

### The name is Non-Dead Design (NDD)

The method takes the name **Non-Dead Design**, acronym **NDD**, slotting into the established `*DD` design-methodology family (TDD, DDD, BDD). The name carries the thesis directly: the spec-map is the primary specification, kept continuously alive rather than written once and abandoned as a dead document. The heading reads `# Non-Dead Design`; NDD is introduced in the root prose rather than carried in the title.

### The working-name callout is removed, not replaced

The root's `[!IMPORTANT]` callout exists only to flag the name as provisional and reassure that a later rename is safe via the stable id. With the name settled that job is done; the id-stability point is generic and already lives in Node Identity. Removing the callout rather than rewording it keeps the root prose-only.

### Root prose names the anti-dead-document thesis

The root's opening keeps describing the division of labour and the unification move, but gains a fuller sentence naming what the name reacts against: the long specification document nobody reads or maintains, which drifts into fiction. The spec-map earns "non-dead" by being small and navigable enough to stay read and maintained.

### The rename is a mechanical re-point plus one anchor change

The heading becomes `# Non-Dead Design`; the anchor shifts from `#unified-map-method` to `#non-dead-design`. Every navigation link and the Contents overview root label re-point to the new name. The id `a3k` is untouched, demonstrating the identity-survives-rename property the old callout described.

## Plan

- [x] Rename the root heading to `# Non-Dead Design` and remove the working-name callout.
- [x] Rewrite the root prose to introduce the NDD acronym and add the fuller anti-dead-document thesis sentence.
- [x] Re-point the six `[Unified Map Method](#unified-map-method)` navigation links to the new name and anchor.
- [x] Update the Contents overview root label to `Non-Dead Design`.
- [x] Verify all anchors resolve, no duplicate headings or ids, and blank-line spacing intact.

## Conclusion

Completed. The method is renamed **Non-Dead Design (NDD)** throughout the map (heading, six nav links, Contents overview; id `a3k` untouched). The root prose was reworked well beyond a mechanical rename: it now opens on three "deaths" the method prevents (dead specs, dead structural thinking, dead comprehension) with the map as the hub that keeps them alive. Principles-enrichment ideas surfaced during drafting were parked as `enrich-principles-from-hazards.md`.
