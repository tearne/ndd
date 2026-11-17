# NDD

Non-Dead Design: a method for keeping specification, structural thinking and comprehension alive in agentic software development. The system is described by a conceptual map, written in markdown and maintained with the agent, which serves as the hub for specification and change management. The reasoning is in the map itself, under [Principles](method/ndd.map.md#principles); the method starts at [NDD](method/ndd.map.md#ndd).

## Installation

Prerequisite: [`uv`](https://docs.astral.sh/uv/), which runs the installer.

Clone this repository, then run the installer from the project you want to adopt it:

```
git clone https://github.com/tearne/ndd
cd your-project && path/to/ndd/install.py
```

This vendors the method into `./ndd/` and points the agent entry files, `CLAUDE.md` and `AGENTS.md`, at it. To upgrade, `git pull` the checkout and re-run. Once installed, [`README.ndd.md`](README.ndd.md), shipped as `ndd/README.md`, is the starting point for working with it.

## Developing NDD

This repository is itself worked with NDD. Its own map, entered at [NDD Project](map.md#ndd-project), describes how the method is distributed and tested; `method/` holds the method's sources, `changes/` the repository's changes, and `tests/` the checks described under [Testing](testing.map.md#testing).
