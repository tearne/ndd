# Bootstrap

## Prohibited without explicit user instruction

- Git write operations (commit, push, branch, reset).
- Editing any project file while no change is active. The active change, if any, is recorded in `changes/open/active.md`. Reading is unrestricted; so is writing inside `changes/`.

## Two maps: the method and your project

Two maps are in play, and they must not be confused:

- The **method map** — `ndd.md`, alongside this file under `ndd/` — is the authoritative reference for *how NDD works*. It is read-only (see below); you read it to learn the method.
- The **project map** — `map.md` in the project root — is *the work itself*: the conceptual map of this project that you build and maintain with the user. In a fresh project it may not exist yet — the Startup Scan detects that and routes to bootstrapping.

Both are trees of nodes: each is a heading with a short description, a link to its parent, and links to its children. Start at the root node — the one with no parent link — and follow the child links to navigate. The method map explains its own conventions as you read; the project map follows those same conventions.

## The vendored method is read-only

Everything under `ndd/` is a snapshot that `opt-in.py` regenerates — treat it as read-only and never hand-edit it, or your changes vanish on the next install. Changing the method itself means editing its source and re-running the installer.

## First action each session

Begin with the **Startup Scan** — navigate to that node in `ndd.md` (under Change-Management) and follow it to orient from `changes/open/`. You need not read the whole map first; do the scan, then read further as the work requires.

## Staying up to date

The method is vendored under `ndd/` and is safe to refresh at any time. Update your NDD checkout and re-run the installer from your project:

```
git -C path/to/ndd pull
cd your-project && path/to/ndd/opt-in.py
```

The version you are running is the semver at the top of `ndd/CHANGELOG.md` — the value to compare when a colleague asks which version you are on. On upgrade the installer keeps the previous method map as `ndd/ndd.prev.md`. To see what changed, read the new entries at the top of `ndd/CHANGELOG.md`; for a precise, mechanical migration the agent may also diff `ndd/ndd.md` against `ndd/ndd.prev.md`. Then judge whether this project's own `map.md` or any open change in `changes/` needs adjusting to the changed conventions, and surface anything that does. This is the method's own migration step; nothing else pulls updates automatically.
