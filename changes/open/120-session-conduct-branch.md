# Session conduct branch

**Change Style:** Formal

## Intent

Gather the nodes that govern how a session is conducted, rather than how a change evolves, into their own branch: *Startup Scan*, *Bootstrapping*, *Gates and Permissions*, *Keywords* and *Thought Management*, and perhaps *Orient Then Focus* and *Diffs*. Then settle the child order of the branches the cut touches.

## Context

Promoted 2026-11-04 from the discussion *Map shape: session conduct*, opened in 105's pre-release Map Review. *Change-Management* says it covers how the project evolves through changes, yet these children apply equally to map edits and discussions. *Startup Scan* and *Bootstrapping* come first in time but sit after *Versioning*, and *Gates and Permissions* is referenced by *Plan* but sits second to last.

## Change Specification

Tree agreed 2026-11-17, from a before-and-after comparison of the contents tree shown at the user's request:

```text
- NDD
  - Principles (unchanged, Orient Then Focus kept there)
  - Map (Diffs leaves Engagement Rule)
  - Session Conduct (new)
    - Startup Scan
    - Bootstrapping
    - Gates and Permissions
      - Approval
        - Drafts
        - Diffs
    - Keywords
      - Process Keyword, Aside Keyword, Pause Keyword
    - Thought Management
  - Change-Management
    - Discussion
    - Change Lifecycle
    - Change Style
    - Versioning
  - Maintenance, Tooling, Standards, Installation (unchanged)
```

Node edits follow from it, on a copy of `method/ndd.map.md` in the companion folder.
