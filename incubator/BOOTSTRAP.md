# Bootstrap

## Prohibited without explicit user instruction

- Git write operations (commit, push, branch, reset).
- Editing any project file while no change is active. The active change, if any, is recorded in `changes/open/active.md`. Reading is unrestricted; so is writing inside `changes/`.

## The map is authoritative

The `map.md` alongside this file is the authoritative reference. Read it before acting.

It is a tree of nodes. Each node is a heading with a short description, a link to its parent, and links to its children. Start at the root node — the one with no parent link — and follow the child links to navigate. The map explains its own conventions as you read.

## First action each session

Begin with the **Startup Scan** — navigate to that node in `map.md` (under Change-Management) and follow it to orient from `changes/open/`. You need not read the whole map first; do the scan, then read further as the work requires.

## Staying up to date

The method is vendored under `ndd/` and is safe to refresh at any time by re-running the installer:

```
curl -fsSL https://raw.githubusercontent.com/tearne/ndd/main/install.sh | bash
```

The installed version is recorded in the `<!-- ndd-version: … -->` marker at the top of `ndd/ndd.md`. On upgrade the installer keeps the previous method map as `ndd/ndd.prev.md`. Whenever that backup is present and differs, read the diff between `ndd/ndd.md` and `ndd/ndd.prev.md`, then judge whether this project's own `map.md` or any open change in `changes/` needs adjusting to the changed conventions, and surface anything that does. This is the method's own migration step; nothing else pulls updates automatically.
