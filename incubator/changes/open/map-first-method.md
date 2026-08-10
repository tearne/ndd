# Map-first method

**Mode:** Explore

## Intent

The method should live in the map, not in prose beside it. Today `AGENT`, `PROCESS`, `KEYWORDS`, and `MAP-GUIDANCE` carry the process as markdown, and `map.md` describes the same concepts as nodes — the two have already drifted, with `map.md` badly stale. This change explores collapsing that duplication: express as much of the method as possible *as the map*, so the map is the primary artefact the agent reads to understand how to work, leaving only a minimal markdown shell that points the agent at the map and tells it to read and follow it. That is the true dogfooding test — the method describing itself in its own form.
