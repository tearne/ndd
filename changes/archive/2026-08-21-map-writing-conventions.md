# Map writing conventions

**Mode:** Formal

## Intent

Five writing conventions have accumulated as raw captures while authoring the map. Settle them: decide which survive, phrase each canonically, and give each a home in the Writing Style subtree — Conceptual Writing for what the prose says, Formatting for how it's typeset. Then bring the map and the other method documents into conformance, so each convention is both stated in one place and actually honoured everywhere.

## Approach

### Homes stay the two existing nodes; no new child nodes

The five conventions fold into *Conceptual Writing* and *Formatting* as bullets, not new nodes. The subtree's split (what the prose says vs how it's typeset) already covers them, and both nodes have headroom under the sizing limit. Watch for bloat as bullets land.

### Where each convention lands

- **Flowing sentences over mid-sentence breaks** → Conceptual Writing. It governs how a sentence is composed, not how it's typeset.
- **Italics for references, bold for term introduction** → Formatting. Pure typography.
- **Two blank lines before a node title** → Formatting. Pure typography.
- **Bullets for scannable enumerations** → the *decision to enumerate* is conceptual and rhymes with "name the boxes", so its when-to-bullet lands in Conceptual Writing; the how (blank line between bullets) already lives in Formatting and isn't duplicated.
- **Inline link vs See also** → Formatting. It's a cross-referencing convention about how a reference is presented on the page.

### Convention 1 settled by a case-by-case em-dash review

Rather than adopt convention 1 as a pre-written rule, its fate and phrasing emerge from a review during Build: walk the map's em-dash uses case by case, find where tolerance sits, then capture the resulting rule canonically. The convention isn't phrased up front because the phrasing is the review's output.

### Conformance is scoped to the map only

Only `map.md` is brought into conformance; `BOOTSTRAP.md` and `README.md` are out of scope for this change.

## Plan

- [x] Review the map's em-dash uses case by case, agree the tolerance, and settle convention 1's canonical rule
- [x] Add the surviving conceptual conventions (flowing sentences, when-to-bullet) to Conceptual Writing
- [x] Add the surviving formatting conventions (italics/bold, two blank lines before a title, inline link vs See also) to Formatting
- [x] Apply the agreed em-dash fixes across the map
- [x] Normalise node separation to two blank lines across the map
- [x] Bring italics/bold, bullet, and inline-vs-See-also usage into conformance across the map

## Log

- Convention 1 tolerance settled: term–gloss label dashes and single trailing dashes are fine; parenthetical em-dash pairs (`— … —`) are fine when the middle is one short clause, and fail only when the middle is both long and multi-part. Only two lines cross it — L461 (three-item Feedback list) and L420 (two-clause *name (id)* gloss) — to be reworked in the fixes task.
- Node-separation sweep: 29 nodes were on one blank line, 7 already on two; normalised all to two (root stays zero). Mechanical whitespace only.
- Italics/bold conformance: three in-prose references to *Detail*/*See also* were still bold or plain (Node, Node Sections, Map Maintenance) — italicised to match the exemplar. Bullet and inline-vs-See-also conventions found already honoured; the amended blank-line-between-bullets rule is permissive, so no forced changes.

## Source conventions

- **Flowing sentences over mid-sentence breaks.** Prefer structures that keep the sentence intact over ones that interrupt it with dashes or parentheticals. When a list of examples is needed, favour a trailing "such as ..." clause rather than an em-dash-bracketed insertion. Only break the sentence when that genuinely reads best.

- **Italics for references, bold for term introduction.** Use *italics* when a sentence refers to a section or named element (e.g. *Callouts*, *Detail*, *See also*). Reserve **bold** for introducing a term of art on first use (e.g. **scaffolding block**). This keeps inline references from reading like competing sub-headings.

- **Two blank lines before a node title.** Separate one node from the next with two blank lines ahead of its `#` heading, so node boundaries are visually distinct when scrolling a single-file map.

- **Bullets for enumerations the reader will scan.** When a node names a small set of parts, options, or questions, prefer a bulleted list over an in-sentence enumeration — it makes the set scannable and each item individually referenceable. (Applied in *Edit Governance*'s what/how/when framing.) Keep a blank line between bullets for readability.

- **Inline link vs See also.** Use an *inline* cross-reference link when a sentence already names another node in passing — the reference rides the prose (e.g. the *ambiguity test* pointing at *Cross-Agent Falsifiability*). Reserve a *See also* entry for a standalone pointer to a related node the prose doesn't already invoke, and give it an explicit "why this matters." Neither replaces the parent/child navigation links.

## Conclusion

All five conventions landed in the two existing Writing Style nodes; no new nodes were needed. Two things worth noting beyond the plan:

- The blank-line-between-bullets rule was made *permissive* mid-build ("only when they wrap"), narrower than the original capture, at the user's steer.
- Convention 1 became a *tolerance* rather than a hard rule: parenthetical em-dash pairs are fine unless the middle is both long and multi-part. Only two lines crossed it.

Map-only change, so no code or docs beyond `map.md` were touched.
