# Approved nodes exempt from size flag

## Intent

Stop flagging a node as oversize when it carries the current user's approval stamp for the text as it stands. Tidy's size count and the Shape check skip such nodes, since the size judgement has already been made; the flag returns only if the node's fingerprint no longer matches the stamp.

### Context

- Parked from the Map Review of 2026-09-13, where all 16 oversize nodes were judged to stay and Conceptual Writing was stamped for tearne. Without this, every review re-raises the same 16.
- Depends on change 050, which settles how the agent knows the current user's handle. Parked until that is built.
