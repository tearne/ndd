#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Reference implementation of the Fingerprint rule (ndd.map.md#fingerprint),
# checked against the fixtures beside it, whose expected hashes are also listed
# in testing.map.md#fingerprint-check. Then checks that util/fingerprint.py agrees.

import hashlib
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
HELPER = HERE.parent / "util" / "fingerprint.py"

EXPECTED = {
    "fixture.map.md": {
        "Fixture": "11f6836e", "Plain Prose": "bcf6b47b", "Full Sections": "188f743f",
        "Child": "250ae92a", "Bare Heading": "6bcce17f", "Changed Prose": "275d67bd",
    },
    "fixture-edited.map.md": {
        "Fixture": "c332f293", "Plain Prose": "bcf6b47b", "Full Sections": "188f743f",
        "Renamed Child": "103b2b33", "Bare Heading": "6bcce17f", "Changed Prose": "618c09de",
    },
}


# The rule: from the heading line to the line before the next heading, drop the
# navigation-link lines and the scaffolding block whole, remove all whitespace,
# take the first eight hex digits of the SHA-256.
def fingerprint(node_lines: list[str]) -> str:
    heading, body = node_lines[0], node_lines[1:]
    i = 0
    while i < len(body) and (body[i].strip() == "" or re.fullmatch(r"\[[^\]]+\]\([^)]+\)\s*\\?\s*", body[i])):
        i += 1  # a navigation link is a line that is solely one link, with an optional trailing backslash
    if i < len(body) and body[i].startswith("```yaml"):
        i = next(j for j in range(i + 1, len(body)) if body[j].startswith("```")) + 1
    text = re.sub(r"\s+", "", heading + "".join(body[i:]))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]


# The helper's due listing, per person: a node is due when its stamp for them is
# missing or stale. "Alice Smith" checks that a name with a space is read.
DUE = {
    "fixture.map.md": {
        "expected": ["Bare Heading"],
        "Alice Smith": ["Fixture", "Child", "Bare Heading", "Changed Prose"],
    },
    "fixture-edited.map.md": {
        "expected": ["Fixture", "Renamed Child", "Changed Prose"],
        "Alice Smith": ["Fixture", "Renamed Child", "Bare Heading", "Changed Prose"],
    },
}


# A node runs from a heading to the next heading of any level, fences excluded.
def nodes(path: Path) -> dict[str, list[str]]:
    found, name, in_fence = {}, None, False
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and (m := re.match(r"#{1,6} (.+?)\s*$", line)):
            name = m.group(1)
            found[name] = []
        if name:
            found[name].append(line)
    return found


def main():
    failures = 0
    for file, expected in EXPECTED.items():
        actual = {name: fingerprint(lines) for name, lines in nodes(HERE / file).items()}
        helper = subprocess.run([HELPER, HERE / file], capture_output=True, text=True)
        helper_says = dict(line.split("  ", 1)[::-1] for line in helper.stdout.splitlines())
        for name, hash in expected.items():
            if actual.get(name) != hash:
                failures += 1
                print(f"FAIL {file}: {name} expected {hash}, computed {actual.get(name)}")
            if helper_says.get(name) != hash:
                failures += 1
                print(f"FAIL {file}: {name} expected {hash}, helper printed {helper_says.get(name)}")
    for file, people in DUE.items():
        for person, due in people.items():
            listed = subprocess.run([HELPER, HERE / file, "--due", person], capture_output=True, text=True).stdout.split("\n")[:-1]
            if listed != due:
                failures += 1
                print(f"FAIL {file}: due for {person} expected {due}, helper listed {listed}")
    failures += quoted_stamp_ignored()
    print("OK" if not failures else f"{failures} failures")
    sys.exit(1 if failures else 0)


# A stamp quoted in a node's prose, after its scaffolding block, must not be read
# as a stamp: carol's real stamp matches, and the quoted one, if read, would not.
def quoted_stamp_ignored() -> int:
    import tempfile
    body = ["# Quoted\n", "\n", "Prose quoting a stamp:\n", "\n", "```yaml\n", "approvals:\n", "  carol: {at: 2026-01-01, hash: 00000000}\n", "```\n"]
    real = fingerprint(body)
    node = body[:1] + ["\n", "```yaml\n", "id: q1t\n", "approvals:\n", f"  carol: {{at: 2026-01-01, hash: {real}}}\n", "```\n"] + body[1:]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "quoted.map.md"
        path.write_text("".join(node), encoding="utf-8")
        listed = subprocess.run([HELPER, path, "--due", "carol"], capture_output=True, text=True).stdout.split("\n")[:-1]
    if listed:
        print(f"FAIL quoted stamp: carol expected nothing due, helper listed {listed}")
        return 1
    return 0


if __name__ == "__main__":
    main()
