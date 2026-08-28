# Orient Then Focus as a core principle

**Mode:** Explore

## Intent

_(Approved 2026-08-28.)_

Elevate **"surface the whole set, then engage one item at a time"** from an incidental pattern to a first-class NDD principle. It already appears locally — the [Approach](#approach)'s Unresolved walkthrough, [Interaction Grain](#interaction-grain)'s one-node-at-a-time rule for map edits — but is nowhere named as the single underlying discipline, so it is easy to honour in one place and breach in another.

It protects a specific failure mode: **attention dies under overwhelm**. Showing the whole set preserves orientation; taking one item at a time preserves engagement, with the agent holding the rest; dumping everything at once destroys both.

## Approach

**The map is the deliverable.** This change adds and rewires map nodes only; no code, no installer, no standards. Its build is therefore a map-edit sequence under the ordinary one-node-at-a-time rule — which is the principle being named, so the change dogfoods itself.

**Weave by reference, not restatement.** Wherever the pattern already appears (Approach's Unresolved walkthrough, Interaction Grain's per-node rule) the existing prose stays and gains a pointer to the named principle; nothing is duplicated. Reason: artifact economy under **Enjoyment**, and the whole complaint in the Intent is that the discipline is scattered — a second home would repeat the fault.

**Widen and rename in place, no new node.** The principle lands as **Orient Then Focus**, a rename-and-rewrite of **Interaction Grain (p4c child, r5i)** rather than a sibling beside it. Reason: Interaction Grain already mashes two claims — *pace* (never outrun the user) and *negotiation* (the user decides each node rather than reviewing diffs) — which is why its name reads as opaque; what it lacks is the orienting half, surfacing the whole set first. A sibling would leave a near-duplicate pair and re-scatter the discipline this change exists to consolidate. Node identity `r5i` carries the rename, so nothing pointing at it is lost.

**The map-edit case is referenced, not restated.** **Engagement Rule (n3g)** already carries it — nodes "named up front and settled one by one" — so the widened principle points at it as the concrete instance instead of absorbing it. Reason: the general statement must visibly cover the case it grew from, but duplicating an existing node would breach the by-reference decision above.

**No spoon-feeding framing.** The name and prose put the burden on the agent — it holds the whole plan so the user holds one thing at a time — rather than describing the user as needing material fed to them.

**Scope is wide: every batched surface, not just map edits.** Orient Then Focus binds the agent's conduct wherever it presents a set — Unresolved lists, worklists, the Startup Scan's report of open changes, options offered in chat, and map-node proposals. Reason: the breach that prompted this change (three map nodes in one turn) and the existing instances (Unresolved walkthrough, per-node editing) fall on opposite sides of a narrow map-only line, so a narrow rule would not have prevented it. Wide scope is also what earns the node its place under **Principles** rather than in the spec subtree.

**The root's three deaths stand.** No fourth death is added to **Non-Dead Design (a3k)**. Reason: attention dying under overwhelm is a *mechanism* of the existing comprehension death ("understanding is sustained by engagement, not discipline"), not a peer of it; a fourth entry would put a cause alongside its effect and dilute the framing. Orient Then Focus names the mechanism in its own prose and points up at comprehension and **Enjoyment** instead.

## Topics

- **Rewrite Interaction Grain (r5i) as Orient Then Focus** — the widened principle: surface the whole set for orientation, then take one item at a time with the agent holding the rest. Keeps the pace and negotiation claims already there; adds the orienting half; names attention-under-overwhelm as the failure mode and points up at comprehension and **Enjoyment**.
- **Follow the rename through the tree** — child link in **Principles (p4c)** and the entry in **Contents (ct5)**.
- **Retarget Engagement Rule (n3g)** — its *See also* points at the renamed node, framed as the map-edit instance of the principle.
- **Point Approach (a2r) at it** — the Unresolved walkthrough gains a *See also* as the second existing instance.

**Done when:** the map holds one named principle covering every batched surface the agent produces, each existing instance points at it rather than restating it, and no `Interaction Grain` reference survives the rename.

## Log

- **Engagement Rule (n3g) trimmed, not just retargeted.** With the principle widened, the node's opening two sentences were the principle restated at map level. Cut to a pointer plus its own residue — the prompt-pitching guidance. Fold-into-parent was weighed and rejected: it would cost **Edit Governance** its what/how/when trio. Its *See also* went with the trim, the pointer now being the first line.
- **No version bump** — the method is unreleased, so the change carries no changelog entry.

## Conclude

Landed as a rename-and-widen of `Interaction Grain` into **Orient Then Focus (r5i)**, now covering every batched surface rather than map edits alone. `Engagement Rule (n3g)` was additionally trimmed — the widening left its opening as a restatement — and `Approach (a2r)` gained a pointer. Root's three deaths untouched. No changelog entry: the method is unreleased. Spun off change 170 (carried-forward block).
