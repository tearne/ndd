# Agent Instructions

## On startup

At the start of every session, scan `changes/open/` and sort what you find by its head line:

- **Seeds** (`**Kind:**` line — `todo` or `idea`) — captured work not yet picked up. Report grouped by anchor node; never active.
- **Changes** (`**Mode:**` line) — for each, read where it sits in the lifecycle (Intent → Approach → Plan → Build → Conclusion), and whether `active.md` marks one mid-build.

Then announce plan or build mode, report both groups, and propose next steps.

## On version update

When the user reports the agent directory has been updated, identify the new and previous versions from `CLAUDE.md`'s `@` pointer — current value and prior value from git history. Read the new version's `CHANGELOG.md` (each version directory ships its own) for the entries between then and now, and surface migration concerns.

## Rules

Never do these without explicit user instruction:

- Git write operations (commit, push, branch, reset)
- Any change management decision: starting, advancing, or archiving a change — including maturing a seed into a worked change
- Writing or editing any project file without an active change recorded in `changes/open/active.md`

Exempt from the active change requirement:

- Reading any project file
- Creating or editing files inside `changes/` — this includes capturing a seed via `aside:`
- Editing `map.md` — edits describing existing reality are permitted without an active change; edits describing pending work defer to Build via an active change. Always negotiated with the user, one node at a time. See `MAP-GUIDANCE.md` for the full rules.

## Map

If the project has a `map.md`, it is the primary frame of reference for understanding and describing changes. If no `map.md` exists, use whatever project documentation is available. See `MAP-GUIDANCE.md` for all map conventions, including how seeds anchor to nodes.

## Changes

- `changes/open/` — open changes, seeds, and the `active.md` lock file
- `changes/archive/` — completed changes, named `YYYY-MM-DD-<name>.md`

@PROCESS.md
@MAP-GUIDANCE.md
@KEYWORDS.md
