# Node reference by heading name

## Intent

Agents cite map nodes by yaml id (sp1, s7q, fb9) alongside or instead of the heading name. The id is an agent-side fingerprint construct; the heading is navigable — a user can scan the map by eye and jump to it, while an id has to be searched. User-facing citations — chat, change files, status lines, commits, PR text — should use the heading name alone, with ids mentioned only when the yaml block itself is what's being edited. Opened as an aside 2026-10-07 while walking change 070's Change Specification; overlaps with change 080.
