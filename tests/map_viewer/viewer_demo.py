#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Builds a small demo map for trying the map viewer: a git repository whose last
# commit holds one version of the map and whose working tree holds a later one,
# with stamps chosen so every approval state and kind of diff appears. Run it, then
# point the viewer at the result:
#
#   tests/map_viewer/viewer_demo.py      # builds /tmp/map-viewer-demo
#   method/util/map_viewer.py /tmp/map-viewer-demo
#
# Each node says what it demonstrates. Stamps are computed with the viewer's own
# fingerprint, so "current" and "text changed since" are real.

import argparse
import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

VERSION = "0.3.0"

GREEN, YELLOW, RED, CYAN = "32", "33", "31", "36"  # ANSI colour codes

VIEWER = Path(__file__).resolve().parents[2] / "method" / "util" / "map_viewer.py"

# Each node: its file, its navigation links, its text as committed and as it stands
# now (None if absent), and who approved which version.
NODES = [
    dict(file="map.md", name="Demo",
         nav=["[Contents](#contents)", "[Approval States](#approval-states)", "[Changes](#changes)",
              "[Branch](branch.map.md#branch)", "[Rendering](#rendering)"],
         committed="A demo map for the viewer. Each child shows one thing: approval states, what changed since an approval, a branch in another file, and rendering. A [further map](linked.map.md#linked-map), linked only here in prose, still has its own tree beneath.",
         now="same", approved={"alice": "now"}),
    dict(file="map.md", name="Contents", nav=["[↑ Demo](#demo)"],
         committed="- [Demo](#demo)\n  - [Approval States](#approval-states)\n    - [Current](#current)\n    - [Stale](#stale)\n    - [Mixed](#mixed)\n    - [Unstamped](#unstamped)\n    - [Quoted Handle](#quoted-handle)\n    - [Renamed](#renamed)\n    - [Lost Approval](#lost-approval)\n  - [Changes](#changes)\n    - [Edited](#edited)\n  - [Branch](branch.map.md#branch)\n    - [Branch Leaf](branch.map.md#branch-leaf)\n  - [Rendering](#rendering)",
         now="same", approved={}),
    dict(file="map.md", name="Approval States",
         nav=["[↑ Demo](#demo)", "[Current](#current)", "[Stale](#stale)", "[Mixed](#mixed)",
              "[Unstamped](#unstamped)", "[Quoted Handle](#quoted-handle)", "[Renamed](#renamed)",
              "[Lost Approval](#lost-approval)"],
         committed="One node for each state a stamp can be in.", now="same", approved={"alice": "now", "bob": "now"}),
    dict(file="map.md", name="Current", nav=["[↑ Approval States](#approval-states)"],
         committed="Approved by alice and bob, and unchanged since: both stamps show as current.",
         now="same", approved={"alice": "now", "bob": "now"}),
    dict(file="map.md", name="Stale", nav=["[↑ Approval States](#approval-states)"],
         committed="Approved by alice, then edited: her stamp is for the old text.",
         now="Approved by alice, then edited after the commit: her stamp is for the old text, so it shows as changed since.",
         approved={"alice": "committed"}),
    dict(file="map.md", name="Mixed", nav=["[↑ Approval States](#approval-states)"],
         committed="Bob approved this wording.",
         now="Bob approved an earlier wording; alice approved this one. One stamp is current, the other is not.",
         approved={"alice": "now", "bob": "committed"}),
    dict(file="map.md", name="Unstamped", nav=["[↑ Approval States](#approval-states)"],
         committed="Nobody has approved this node.", now="same", approved={}),
    dict(file="map.md", name="Quoted Handle", nav=["[↑ Approval States](#approval-states)"],
         committed="Approved under a handle with a colon in it, which a stamp must quote.",
         now="same", approved={"carol: qa": "now"}),
    dict(file="map.md", name="Renamed", committed_name="Old Name", nav=["[↑ Approval States](#approval-states)"],
         committed="Approved by alice under its old name. The heading counts towards the fingerprint, so her stamp is stale, and the viewer still finds her version by the node's id.",
         now="same", approved={"alice": "committed"}),
    dict(file="map.md", name="Lost Approval", nav=["[↑ Approval States](#approval-states)"],
         committed="Bob's stamp is for text that was never committed, so the viewer can't show what changed since.",
         now="same", approved={"bob": "never committed"}),
    dict(file="map.md", name="Changes", nav=["[↑ Demo](#demo)", "[Edited](#edited)"],
         committed="What a stale approval's link shows: the passages changed since, then the whole node.", now="same", approved={}),
    dict(file="map.md", name="Edited", nav=["[↑ Changes](#changes)"],
         committed="Alice approved this node when its words were struck through where removed.\n\nThis paragraph stays the same.",
         now="Alice approved this node when its words were struck through where removed; now they are highlighted where added too.\n\nThis paragraph stays the same.\n\nThis paragraph is new.",
         approved={"alice": "committed"}),
    dict(file="map.md", name="Rendering", nav=["[↑ Demo](#demo)"],
         committed="Text in *italics* and **bold**, `inline code`, and a link to [Current](#current).\n\n- A bullet\n- Another, with a link to [Branch Leaf](branch.map.md#branch-leaf)\n  - A nested bullet\n    1. A numbered item, nested deeper\n    2. And a second\n\n3. A numbered list starting at three\n4. And four\n\n## A Heading\n\n### A Smaller Heading\n\n> A blockquote.\n\n> [!IMPORTANT]\n> An alert, as GitHub draws one.\n\n| Column | Value |\n|--------|-------|\n| one | 1 |\n| two | 2 |\n\n````markdown\n```python\nprint(\"a fence quoting a shorter one\")\n```\n````",
         now="same", approved={"alice": "now"}),
    dict(file="branch.map.md", name="Branch", nav=["[↑ Demo](map.md#demo)", "[Branch Leaf](#branch-leaf)"],
         committed="This node lives in another file, branch.map.md, and joins the tree through Demo's child link.",
         now="same", approved={"bob": "now"}),
    dict(file="branch.map.md", name="Branch Leaf", nav=["[↑ Branch](#branch)"],
         committed="A leaf in the branch file.", now="same", approved={}),
    dict(file="linked.map.md", name="Linked Map", nav=[],
         committed="A map of its own, reached from Demo's prose rather than a child link, so it is drawn as a tree of its own beneath the main one.",
         now="same", approved={}),
]

IDS = iter(f"d{i:02d}" for i in range(100))


def main():
    args = parse_args()
    target = Path(args.dir)
    if target.exists():
        if not (target / ".map-viewer-demo").exists():
            error(f"{target} exists and isn't a demo built by this script; choose another directory.")
            sys.exit(1)
        shutil.rmtree(target)
    target.mkdir(parents=True)
    (target / ".map-viewer-demo").write_text("Built by tests/map_viewer/viewer_demo.py; safe to delete.\n")
    viewer = load_viewer()
    ids = {node["name"]: next(IDS) for node in NODES}

    write_maps(target, "committed", ids, viewer)
    run(f"git -C {target} init -q && git -C {target} add -A && "
        f"git -C {target} -c user.name=demo -c user.email=demo@example.com commit -qm 'Demo map as committed'")
    write_maps(target, "now", ids, viewer)
    success(f"Demo map built in {target}")
    print(f"View it with: {VIEWER} {target}")


def write_maps(target: Path, version: str, ids: dict[str, str], viewer) -> None:
    files: dict[str, list[str]] = {}
    for node in NODES:
        text = text_of(node, version)
        if text is not None:
            files.setdefault(node["file"], []).append(node_markdown(node, text, ids[node["name"]], viewer, version))
    for file, nodes in files.items():
        (target / file).write_text("\n\n".join(nodes) + "\n", encoding="utf-8")


def text_of(node: dict, version: str) -> str | None:
    if version == "committed" or node["now"] == "same":
        return node["committed"]
    return node["now"]


def name_of(node: dict, version: str) -> str:
    return node.get("committed_name", node["name"]) if version == "committed" else node["name"]


def node_markdown(node: dict, text: str, node_id: str, viewer, version: str) -> str:
    nav = " \\\n".join(node["nav"])
    stamps = "".join(f"  {quoted(who)}: {{at: 2026-11-10, hash: {stamp_hash(node, which, viewer)}}}\n"
                     for who, which in node["approved"].items())
    yaml = f"```yaml\nid: {node_id}\n" + (f"approvals:\n{stamps}" if stamps else "") + "```"
    return f"# {name_of(node, version)}\n\n{nav}\n\n{yaml}\n\n{text}\n"


# A stamp's hash is the fingerprint of the text the approver saw.
def stamp_hash(node: dict, which: str, viewer) -> str:
    if which == "never committed":
        return viewer.fingerprint([f"# {node['name']}\n", "Some text nobody committed.\n"])
    text = text_of(node, which)
    lines = f"# {name_of(node, which)}\n\n{text}\n".splitlines(keepends=True)
    return viewer.fingerprint(lines)


def quoted(handle: str) -> str:
    return f'"{handle}"' if ":" in handle else handle


def load_viewer():
    spec = importlib.util.spec_from_file_location("map_viewer", VIEWER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(cmd: str, **kwargs) -> subprocess.CompletedProcess:
    echo_command(cmd)
    return subprocess.run(f"set -o pipefail && {cmd}", shell=True, executable="/bin/bash", check=True, **kwargs)


def echo_command(cmd: str, root: bool = False) -> None:
    print(styled(f"{'#' if root else '$'} {cmd}", CYAN, sys.stdout))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a demo map for trying the map viewer.")
    parser.add_argument("dir", nargs="?", default="/tmp/map-viewer-demo", help="where to build it (default: /tmp/map-viewer-demo)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return parser.parse_args()


def success(text: str) -> None:
    print(styled(f"✓ {text}", GREEN, sys.stdout))


def warn(text: str) -> None:
    print(styled(f"⚠ {text}", YELLOW, sys.stdout))


def error(text: str) -> None:
    print(styled(f"✗ {text}", RED, sys.stderr), file=sys.stderr)


def styled(text: str, code: str, stream) -> str:
    if stream.isatty() and "NO_COLOR" not in os.environ:
        return f"\033[{code}m{text}\033[0m"
    return text


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        error("No virtual environment detected. Run this script via './viewer_demo.py' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        warn("Aborted.")
        sys.exit(130)
