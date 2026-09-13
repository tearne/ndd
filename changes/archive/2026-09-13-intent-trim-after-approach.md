# Intent trim after Approach

**Cadence:** Wander

## Intent

Two edits to the *Intent* node. First, reword its definition so it stops claiming "why": the Intent is what the change must achieve, in domain language, stated so the user can approve it; every "why" belongs to *Context*. Second, add one sentence: when the Approach is approved, the agent re-reads the Intent and cuts what the Approach now carries, surfacing the trimmed Intent with its count.

### Context

- Change 280's Intent grew Approach-level detail during planning and needed trimming once the Approach existed. The first draft of this change's own Intent carried history and provenance that belong in Context.
- Both leaks share a cause: the agent packs justification into the part it is surfacing for approval. Intent's definition, "why the change is needed", overlaps Context's "why the change exists" and invites that.
- Held is the intended route for material arriving before its part and stays unchanged. The leak is only visible once the Approach exists, so a check at that moment is the backstop.
- Source: process feedback entry, 2026-09-13, and this session's discussion.

## Log

- 2026-09-13: The first application of the approved Intent edit sliced from the Intent node to the Intent Memory node, deleting 536 lines. Caught by the diff stat, restored from git, reapplied bounded by the next heading. Final diff: two lines changed in the Intent node.

## Conclude

The *Intent* node now defines the Intent as what the change must achieve, sends every "why" to Context, and adds the re-read after Approach approval. One deviation, in the Log: the first application of the edit deleted 536 lines and was restored from git before reapplying. Held and AGENT-RULES untouched.
