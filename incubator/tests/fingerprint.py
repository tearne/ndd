#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

# Reference implementation of the Fingerprint rule (ndd.map.md#fingerprint): the
# hash of what a reader sees in a node. Prints fingerprints for a map file, lists
# the nodes due for a person against their approval stamps, or with --check
# verifies itself against the fixtures beside it. See map.md#testing.

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

from rich.console import Console

VERSION = "1.0.0"
HERE = Path(__file__).parent
FIXTURE = HERE / "fixture.map.md"
FIXTURE_EDITED = HERE / "fixture-edited.map.md"
EXPECTED_STAMP = "expected"
DUE_IN_EDITED = {"Changed Prose", "Renamed Child", "Fixture"}
DUE_IN_ORIGINAL = {"Bare Heading"}  # no scaffolding block, so no stamp: due, as any unstamped node is

console = Console()

HEADING = re.compile(r"^#{1,6} (.+?)\s*$")
FENCE = re.compile(r"^```")
LINK_ONLY_LINE = re.compile(r"^\[[^\]]+\]\([^)]+\)\s*$")
STAMP = re.compile(r"^\s+(?:\"([^\"]+)\"|'([^']+)'|([^:\s]+)):\s*\{.*?\bhash:\s*([0-9a-f]{8})\b")


def main():
    args = parse_args()
    if args.check:
        sys.exit(0 if self_check_passes() else 1)
    if args.map is None:
        console.print("[bold red]Error:[/bold red] a map file is required unless --check is given.")
        sys.exit(2)
    nodes = parse_nodes(Path(args.map))
    if args.due:
        list_due(nodes, args.due)
    elif args.node:
        print_one(nodes, args.node)
    else:
        print_all(nodes)


# The rule, as the Fingerprint node states it: heading line to the line before
# the next heading, scaffolding block and navigation-link lines dropped whole,
# every whitespace character removed, first eight hex digits of SHA-256.
def fingerprint(node_lines: list[str]) -> str:
    seen = [node_lines[0]] + strip_scaffolding(node_lines[1:])
    text = "".join(seen)
    text = re.sub(r"\s+", "", text)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]


def strip_scaffolding(body: list[str]) -> list[str]:
    i = 0
    while i < len(body) and (body[i].strip() == "" or LINK_ONLY_LINE.match(body[i])):
        i += 1
    if i < len(body) and body[i].startswith("```yaml"):
        i = end_of_fence(body, i) + 1
    return body[i:]


def self_check_passes() -> bool:
    original = parse_nodes(FIXTURE)
    edited = parse_nodes(FIXTURE_EDITED)
    problems = []
    due = set(due_for(original, EXPECTED_STAMP))
    for name in sorted(due - DUE_IN_ORIGINAL):
        problems.append(f"{FIXTURE.name}: '{name}' is due but its stamp should match")
    for name in sorted(DUE_IN_ORIGINAL - due):
        problems.append(f"{FIXTURE.name}: '{name}' should be due, it has no stamp")
    due = set(due_for(edited, EXPECTED_STAMP))
    for name in sorted(due - DUE_IN_EDITED):
        problems.append(f"{FIXTURE_EDITED.name}: '{name}' is due, but its edits should not change the fingerprint")
    for name in sorted(DUE_IN_EDITED - due):
        problems.append(f"{FIXTURE_EDITED.name}: '{name}' should be due, its text changed")
    for problem in problems:
        console.print(f"  [red]FAIL[/red] {problem}")
    if problems:
        return False
    console.print(f"[bold green]OK[/bold green] {FIXTURE.name}: only {', '.join(sorted(DUE_IN_ORIGINAL))} is due, unstamped; "
                  f"{FIXTURE_EDITED.name}: only {', '.join(sorted(DUE_IN_EDITED))} are due.")
    return True


# A node is due for a person when it has no stamp for them or the stamp's hash
# is not the node's current fingerprint. Sign-off (ndd.map.md#sign-off).
def due_for(nodes: dict[str, list[str]], person: str) -> list[str]:
    return [name for name, lines in nodes.items() if stamps(lines).get(person) != fingerprint(lines)]


def stamps(node_lines: list[str]) -> dict[str, str]:
    found = {}
    for line in node_lines:
        m = STAMP.match(line)
        if m:
            person = m.group(1) or m.group(2) or m.group(3)
            found[person] = m.group(4)
    return found


def parse_nodes(path: Path) -> dict[str, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    nodes, current, in_fence = {}, None, False
    for line in lines:
        if FENCE.match(line):
            in_fence = not in_fence
        heading = None if in_fence else HEADING.match(line)
        if heading:
            current = heading.group(1)
            nodes[current] = []
        if current is not None:
            nodes[current].append(line)
    return nodes


def end_of_fence(lines: list[str], start: int) -> int:
    for i in range(start + 1, len(lines)):
        if FENCE.match(lines[i]):
            return i
    return len(lines) - 1


def print_one(nodes: dict[str, list[str]], name: str) -> None:
    if name not in nodes:
        console.print(f"[bold red]Error:[/bold red] no node named '{name}'.")
        sys.exit(1)
    print(fingerprint(nodes[name]))


def print_all(nodes: dict[str, list[str]]) -> None:
    for name, lines in nodes.items():
        print(f"{fingerprint(lines)}  {name}")


def list_due(nodes: dict[str, list[str]], person: str) -> None:
    for name in due_for(nodes, person):
        print(name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fingerprint map nodes, per the NDD Fingerprint rule.")
    parser.add_argument("map", nargs="?", help="a map file")
    parser.add_argument("node", nargs="?", help="a node name; omit to list every node")
    parser.add_argument("--due", metavar="PERSON", help="list the nodes due for this person instead")
    parser.add_argument("--check", action="store_true", help="verify this script against the fixtures beside it")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return parser.parse_args()


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("Error: no virtual environment detected. Run this script via './fingerprint.py' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    main()
