# Tooling development

**Change Style:** Vibe

## Intent

The method uses generic markdown tools today — see *Tooling* — but a purpose-built tool is worth pursuing: a browser-based viewer a developer runs on their dev box and reaches over port forwarding, to present a map in stakeholder meetings — showing it as navigable pages, recording feedback on nodes, and taking approvals as given — plus a cross-map index. It is never formally hosted, the markdown stays the source of truth, and it stays optional so CLI-only teams lose nothing.

## Bounds

Approval box lists handles from stamps already in the map, with new ones addable; on *Approve*, every ticked handle is stamped onto the current node via the shipped fingerprint script.

## Context

Fuller notes and the design tensions are in the retired `enhancement-discussion.md` (P3), kept in git history. Renumbered from 290 on 2026-09-10 to close the sign-off theme.
