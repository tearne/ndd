# Surface the map-edit negotiation gate at point of use

**Mode:** Formal

## Intent

The map-edit negotiation gate — *Engagement Rule (n3g)*: every map edit is negotiated with the user, one node at a time, never silent, never in bulk — is invisible where map edits actually happen: during *Conclude (o4j)*'s map catch-up, and on any ad-hoc reality-sync edit. An agent navigating the *Change-Management* subtree never crosses into *Specification → Edit Governance*, so the rule isn't in front of it at edit time. Worse, *Edit Governance (e7m)*'s exemption wording ("map edits fall outside the active-change requirement... may happen at any time") reads as licence to edit freely — conflating the *what/when* exemption (*Sync Rule*) with the *how* (*Engagement Rule*, still binding). Surfaced by dogfooding 128: the agent caught up the *Distribution* node silently, mid-Conclude. Make the gate discoverable at point of use so a map edit can't be made silently or in bulk.

## Approach

### Reword the Edit Governance exemption to separate *what/when* from *how*

The misread traces to *Edit Governance (e7m)*: "these edits describe reality rather than intent, they fall outside the active-change requirement: no open change is needed, and they may happen at any time." Read at the moment of temptation this scans as blanket licence to edit freely. Reword so the exemption is explicitly scoped to the active-change requirement (the *what/when*) and states that the *Engagement Rule*'s per-node negotiation (the *how*) still binds every map edit. Fixes the conflation at its source rather than patching downstream.

### Signpost the gate at the point of use

An agent editing the map during *Conclude (o4j)*'s catch-up navigates the *Change-Management* subtree and never crosses into *Edit Governance*, so the gate isn't in front of it. Add an inline clause to *Conclude* stating that any map catch-up runs as its own per-node negotiation under the *Engagement Rule* — naming the rule in prose at the point of use, not merely a *See also* link, so it can't be skimmed past. Build is deliberately not signposted: the *Sync Rule* defers a code change's map catch-up to Conclude, so Build is not a legitimate map-edit site; the reworded exemption covers the remaining ad-hoc reality-sync edits that have no single node to signpost.

## Plan

- [x] Reword the *Edit Governance (e7m)* exemption so it scopes the exemption to the active-change requirement and states the *Engagement Rule*'s per-node negotiation still binds every map edit.
- [x] Add an inline clause to *Conclude (o4j)* stating that any map catch-up runs as its own per-node negotiation under the *Engagement Rule*.

## Conclusion

Landed in `map.md`. *Edit Governance (e7m)*'s exemption now states it lifts only the active-change constraint, with the Engagement Rule's per-node negotiation still applying to map updates; *Conclude (o4j)* gained an inline clause naming the Engagement Rule at the point of use, so map catch-up is never silently edited during conclusion. Both edits final-worded to the user's phrasing. No separate map catch-up — the change's deliverable is the map edit itself. Unreleased 1.0.0, no bump.
