# Enrich Principles from the NDD hazards

## Intent

Naming the method Non-Dead Design (change 60) surfaced a sharper account of the hazards it exists to avoid, expressed as parallel "X dies when Y" failures. Three anchor the opening paragraph; the discussion around them raised further points that belong in the Principles subtree, not the root. Fold what's worth keeping into Principles so the founding rationale reflects the sharpened thinking, rather than losing it once change 60 archives.

Points to weigh, each against its candidate home:

- **Comprehension is sustained by enjoyment, not discipline** — the dev role staying architecturally fun is what keeps comprehension alive; you don't maintain understanding by willpower. Candidate home: the Enjoyment node. Check whether it already makes this causal claim or merely asserts enjoyment matters.

- **Comprehension debt compounds silently** — as agents generate more, the human's mental model goes stale unless something forces it current; nothing does so by default. Candidate home: Comprehension is an Activity.

- **Intent evaporates — code records *what*, never *why*** — the reasoning behind a shape lives only in someone's head until they leave. This idea has no clear home in Principles today; it may warrant its own principle, or a line in Local Sufficiency. The genuinely missing one.

- **Agents need a stable, shared frame of reference** — without one authoritative source each agent and session reinvents its understanding and they drift apart. Already owned by Cross-Agent Falsifiability (confirmed on reading); carried here only so it isn't re-proposed, not as an expected edit.

## Approach

### Enjoyment gains the causal claim

The Enjoyment node asserts that diff-review destroys engagement and that enjoyment is a binding constraint, but stops short of the mechanism the NDD framing sharpened: engagement is *what sustains comprehension*, not willpower. Add that causal link so the node explains why enjoyment is load-bearing rather than only asserting it is.

### Comprehension is an Activity is left untouched

The silent-staleness flip side was judged not to earn its words against Enjoyment's artifact-economy warning; the existing "as fast as agents produce code" already carries enough. No edit.

### Intent-evaporates becomes its own principle node

Code records *what*, never *why*; the reasoning behind a shape lives in someone's head until they leave, and the map is where it survives. No current principle owns this, and it's distinct enough to stand alone rather than fold into another node. Named **Intent Memory** — the map remembers the why that code forgets; a noun-style name matching principles like Enjoyment and Interaction Grain.

### The Principles intro node is left untouched

It frames the founding case adequately; the sharpened three-deaths framing stays confined to the child nodes.

### Cross-agent frame is left untouched

Confirmed on reading: Cross-Agent Falsifiability already owns "independent agents render from one authoritative source". No edit; carried in Intent only to prevent re-proposal.

## Plan

**Topics**

- Enrich the Enjoyment node with the causal claim that engagement sustains comprehension, not willpower.

- Add a new Intent Memory principle node (heading, id, parent link) stating that code records what while the map preserves why; register it as a child of Principles and in the Contents overview.

**Done when** Enjoyment carries the causal link, Intent Memory exists as a Principles child with working navigation and an overview entry, and the map passes anchor, duplicate, and spacing checks.

## Conclusion

Completed. Enjoyment gained the causal claim that engagement, not discipline, sustains comprehension. A new principle, Intent Memory (the map remembers the why that code forgets), was added as a child of Principles after Comprehension is an Activity. The silent-staleness point and any intro-node change were dropped as not earning their words; Cross-Agent Falsifiability was confirmed to already cover the shared-frame idea.
