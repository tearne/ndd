# Incubator

Incubation space for the next evolution of COD — a lifecycle-aware conceptual map (build-state as location, per-node approval stamps, stable node IDs) with viewer tooling, and graceful degradation for simple projects. Expected to spin out into its own repository, under a new name, once the shape settles.

## Installation

Prerequisite: [`uv`](https://docs.astral.sh/uv/) (the installer runs as a `uv` script).

Clone this repo wherever you like, then run the installer from the project you want to opt in:

```
git clone https://github.com/tearne/ndd
cd your-project && path/to/ndd/opt-in.py
```

This vendors the method into `./ndd/` and wires up the agent entry files (`CLAUDE.md`/`AGENTS.md`). To upgrade later, `git pull` the checkout and re-run — the previous method map is kept as `ndd/ndd.prev.md`.

## Boundary

**Nothing in `incubator/` is live COD.** The framework that real consumers install is the tree under the repository's top-level `agent/` directory, shipped by `opt-in.py`. This folder is inert to both:

- **The installer** — `opt-in.py` copies only from `agent/`, so nothing here reaches any consumer project.
- **The running framework** — the root agent config loads only `agent/`; this folder does not change how COD behaves.

Incubation work does **not** modify `agent/`, `opt-in.py`, or the root docs. Those are live COD.

## Self-contained COD project

This directory is its own COD project via a subdirectory install of `opt-in.py`. It carries a pinned snapshot of the framework under `changes/agent/<version>/`, its own `CLAUDE.md`, and its own `changes/` tree with an independent `active.md` lock. It subscribes to a frozen COD version, decoupled from edits to the root `agent/`.
