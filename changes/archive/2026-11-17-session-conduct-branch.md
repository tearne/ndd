# Session conduct branch

**Change Style:** Formal \
**Version:** 3.7.3-dev

## Intent

Gather the nodes that govern how a session is conducted, rather than how a change evolves, into their own branch: *Startup Scan*, *Bootstrapping*, *Gates and Permissions*, *Keywords* and *Thought Management*. Then settle the child order of the branches the cut touches.

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

Node edits follow from it, made on a copy of `method/ndd.map.md` in a companion folder, promoted in Build and dropped at Archiving.

Planned node edits, in the copy:

1. *Session Conduct* (new).
2. *NDD*: child link, a bullet for the new branch, and *Change-Management*'s bullet no longer naming gates.
3. *Change-Management*: child links, the five moved out and *Discussion* first.
4. to 8. *Startup Scan*, *Bootstrapping*, *Gates and Permissions*, *Keywords*, *Thought Management*: up links to *Session Conduct*.
9. *Engagement Rule*: drops its *Diffs* child link.
10. *Approval*: gains it.
11. *Diffs*: up link to *Approval*.
12. *Contents*.
13. File order: the moved nodes' text placed in tree order.

Progress:

- 1 approved, stamped 06eead64.
- 2 approved at 1,058 characters, stamped cab28da0; a trim of its bullets to follow as 2a.
- 2a approved, *NDD* trimmed, stamped ea3f724d.
- 3 approved, child links only, stamp current.
- 4 approved, *Startup Scan* up link.
- 5 approved, *Bootstrapping* up link.
- 6 approved, *Gates and Permissions* up link.
- 7 approved, *Keywords* up link.
- 8 approved, *Thought Management* up link.
- 9 approved, *Engagement Rule* drops its *Diffs* child link.
- 10 approved, *Approval* gains *Diffs* as a child.
- 2026-11-17: the user gave permission to update all required navigation links without surfacing each.
- 11 *Diffs* up link to *Approval*, under that permission.
- 12 *Contents* rebuilt to the agreed tree, under that permission.
- 13 approved: nodes placed in tree order in the file, *Contents* kept after *NDD*; no fingerprint changed beyond the settled edits. A rule for file order parked as 180 Map file order.

## Conclude

*Diffs* moved under *Approval*, and *Discussion* to the head of *Change-Management*, with the tree. *NDD*, over its cap, had its branch glosses trimmed to 824 characters. The file was put in tree order, and a rule for that parked as 180 Map file order.

## Log

- 2026-11-17: Build Lock taken; version 3.7.3-dev claimed, a patch bump. Live method map unchanged since the baseline.
- 2026-11-17: promoted `method/ndd.map.md` whole from the copy. Fingerprint and install tests pass, and every link into the method map from the rules, readmes and maps resolves.
