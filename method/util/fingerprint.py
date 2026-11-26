#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Helper for Sign-off (ndd.map.md#sign-off): prints the fingerprints of a map's
# nodes, lists the nodes due for a person against their sign-off stamps, or
# migrates a map's stamps from the older approvals: key to signers:. The
# reference implementation of the rule is tests/fingerprint_test.py, which also
# checks that this helper agrees with it.

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

VERSION = "1.3.1"

GREEN, YELLOW, RED, CYAN = "32", "33", "31", "36"  # ANSI colour codes

# A node starts at a level-1 heading; a deeper one is part of the node it sits in.
HEADING = re.compile(r"^# (.+?)\s*$")
FENCE = re.compile(r"^```")
LINK_ONLY_LINE = re.compile(r"^\[[^\]]+\]\([^)]+\)\s*\\?\s*$")
# A key may hold spaces; one with a colon or leading punctuation is quoted, per
# the Sign-off Stamp node.
STAMP = re.compile(r"^\s+(?:\"([^\"]+)\"|'([^']+)'|([^\s\"'][^:]*?))\s*:\s*\{.*?\bhash:\s*([0-9a-f]{8}|null)\b")


def main():
    args = parse_args()
    if args.migrate:
        migrate(Path(args.map))
        return
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


def scaffolding_block(body: list[str]) -> list[str]:
    i = 0
    while i < len(body) and (body[i].strip() == "" or LINK_ONLY_LINE.match(body[i])):
        i += 1
    if i < len(body) and body[i].startswith("```yaml"):
        return body[i:end_of_fence(body, i) + 1]
    return []


def strip_scaffolding(body: list[str]) -> list[str]:
    i = 0
    while i < len(body) and (body[i].strip() == "" or LINK_ONLY_LINE.match(body[i])):
        i += 1
    if i < len(body) and body[i].startswith("```yaml"):
        i = end_of_fence(body, i) + 1
    return body[i:]


# A node is due for a person when their stamp is stale, its hash not the node's
# current fingerprint, or requested, its hash null. A node with no stamp for
# them is never due, nor is Contents. Stamp States (ndd.map.md#stamp-states).
def due_for(nodes: dict[str, list[str]], person: str) -> list[str]:
    due = []
    for name, lines in nodes.items():
        found = stamps(lines)
        if name != "Contents" and person in found and found[person] != fingerprint(lines):
            due.append(name)
    return due


# Stamps are read from the scaffolding block only, so an example stamp quoted
# later in the node is never taken for a real one. A requested stamp's hash is
# None. Sign-off Stamp (ndd.map.md#sign-off-stamp).
def stamps(node_lines: list[str]) -> dict[str, str | None]:
    found = {}
    for line in scaffolding_block(node_lines[1:]):
        m = STAMP.match(line)
        if m:
            person = m.group(1) or m.group(2) or m.group(3)
            found[person] = None if m.group(4) == "null" else m.group(4)
    return found


# Renames each node's older approvals: key to signers:, in the scaffolding block only, so a
# key quoted in a node's prose is left alone. Fingerprints skip the block, so none moves.
# Sign-off Stamp (ndd.map.md#sign-off-stamp).
def migrate(path: Path) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    renamed, in_fence = 0, False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            in_fence = not in_fence
        if not in_fence and HEADING.match(line):
            body = lines[i + 1:]
            block = scaffolding_block(body)
            if block:
                first = i + 1 + body.index(block[0])
                for j in range(first, first + len(block)):
                    if re.match(r"^approvals:\s*$", lines[j]):
                        lines[j] = lines[j].replace("approvals:", "signers:", 1)
                        renamed += 1
    if renamed:
        path.write_text("".join(lines), encoding="utf-8")
    print(f"{renamed} node{'' if renamed == 1 else 's'} migrated in {path}")


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
        error(f"No node named '{name}'.")
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
    parser.add_argument("map", help="a map file")
    parser.add_argument("node", nargs="?", help="a node name; omit to list every node")
    parser.add_argument("--due", metavar="PERSON", help="list the nodes due for this person instead")
    parser.add_argument("--migrate", action="store_true", help="rename an older approvals: stamp key to signers:")
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
        error("No virtual environment detected. Run this script via './fingerprint.py' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        warn("Aborted.")
        sys.exit(130)
