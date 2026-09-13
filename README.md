# NDD

Non-Dead Design: a method for keeping specification, structural thinking and comprehension alive in agentic software development. The system is described by a conceptual map, written in markdown and maintained with the agent, which serves as the hub for specification and change management. The reasoning is in the map itself, under [Principles](ndd.map.md#principles); the method starts at [NDD](ndd.map.md#ndd) and this repository's own map at [map.md](map.md).

## Installation

Prerequisite: [`uv`](https://docs.astral.sh/uv/), which runs the installer.

Clone this repository, then run the installer from the project you want to adopt it:

```
git clone https://github.com/tearne/ndd
cd your-project && path/to/ndd/install.py
```

This vendors the method into `./ndd/` and points the agent entry files, `CLAUDE.md` and `AGENTS.md`, at it. To upgrade, `git pull` the checkout and re-run.
