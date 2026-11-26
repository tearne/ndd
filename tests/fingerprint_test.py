#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Reference implementation of the Fingerprint rule (method/ndd.map.md#fingerprint),
# checked against the fixtures beside it, whose expected hashes are also listed
# in testing.map.md#fingerprint-check. Then checks that method/util/fingerprint.py agrees.

import hashlib
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
HELPER = HERE.parent / "method" / "util" / "fingerprint.py"
VIEWER = HERE.parent / "method" / "util" / "map_viewer.py"  # carries its own copy of the rule

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
# stale; one with no stamp for them, such as Bare Heading, is not.
DUE = {
    "fixture.map.md": {
        "expected": [],
        "Alice Smith": [],
    },
    "fixture-edited.map.md": {
        "expected": ["Fixture", "Renamed Child", "Changed Prose"],
        "Alice Smith": [],
    },
}


# A node runs from a level-1 heading to the next, fences excluded; a deeper heading
# is part of the node it sits in.
def nodes(path: Path) -> dict[str, list[str]]:
    found, name, in_fence = {}, None, False
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and (m := re.match(r"# (.+?)\s*$", line)):
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
    failures += contents_never_due()
    failures += requested_is_due()
    failures += older_key_read()
    failures += migrate_renames_key()
    failures += viewer_agrees()
    failures += subheading_stays_in_node()
    print("OK" if not failures else f"{failures} failures")
    sys.exit(1 if failures else 0)



# The map viewer carries its own copy of the rule so it runs standalone; it must
# give the same fingerprints.
def viewer_agrees() -> int:
    import importlib.util
    spec = importlib.util.spec_from_file_location("map_viewer", VIEWER)
    viewer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(viewer)
    failures = 0
    for file, expected in EXPECTED.items():
        for name, lines in nodes(HERE / file).items():
            if name in expected and viewer.fingerprint(lines) != expected[name]:
                failures += 1
                print(f"FAIL {file}: {name} expected {expected[name]}, viewer computed {viewer.fingerprint(lines)}")
    return failures


# A level-2 heading is part of the node above it, for the reference, the helper and
# the viewer alike, each splitting the file itself.
def subheading_stays_in_node() -> int:
    import importlib.util
    import tempfile
    spec = importlib.util.spec_from_file_location("map_viewer", VIEWER)
    viewer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(viewer)
    text = "# Outer\n\nProse.\n\n## Inner\n\nMore prose.\n\n# Next\n\nOther.\n"
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sub.map.md"
        path.write_text(text, encoding="utf-8")
        reference = nodes(path)
        helper = subprocess.run([HELPER, path, "Outer"], capture_output=True, text=True).stdout.strip()
    lines = text.splitlines(keepends=True)
    start, end = dict(viewer.node_ranges(lines))["Outer"]
    expected = fingerprint(lines[:8])
    got = {"names": list(reference), "reference": fingerprint(reference["Outer"]), "helper": helper, "viewer": viewer.fingerprint(lines[start:end])}
    want = {"names": ["Outer", "Next"], "reference": expected, "helper": expected, "viewer": expected}
    if got != want:
        print(f"FAIL subheading: expected {want}, got {got}")
        return 1
    return 0


# A stamp quoted in a node's prose, after its scaffolding block, must not be read
# as a stamp: carol's real stamp matches, and the quoted one, if read, would not.
def quoted_stamp_ignored() -> int:
    import tempfile
    body = ["# Quoted\n", "\n", "Prose quoting a stamp:\n", "\n", "```yaml\n", "approvals:\n", "  carol: {at: 2026-01-01, hash: 00000000}\n", "```\n"]
    real = fingerprint(body)
    node = body[:1] + ["\n", "```yaml\n", "id: q1t\n", "signers:\n", f"  carol: {{at: 2026-01-01, hash: {real}}}\n", "```\n"] + body[1:]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "quoted.map.md"
        path.write_text("".join(node), encoding="utf-8")
        listed = subprocess.run([HELPER, path, "--due", "carol"], capture_output=True, text=True).stdout.split("\n")[:-1]
    if listed:
        print(f"FAIL quoted stamp: carol expected nothing due, helper listed {listed}")
        return 1
    return 0


# A Contents node is never due, though it carries no stamp; the stamped node
# beside it matches, so nothing is due for carol.
def contents_never_due() -> int:
    import tempfile
    contents = ["# Contents\n", "\n", "```yaml\n", "id: c1t\n", "```\n", "\n", "- [Stamped](#stamped)\n", "\n"]
    body = ["# Stamped\n", "\n", "Prose.\n"]
    real = fingerprint(body)
    node = body[:1] + ["\n", "```yaml\n", "id: s1t\n", "signers:\n", f"  carol: {{at: 2026-01-01, hash: {real}}}\n", "```\n"] + body[1:]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "contents.map.md"
        path.write_text("".join(contents + node), encoding="utf-8")
        listed = subprocess.run([HELPER, path, "--due", "carol"], capture_output=True, text=True).stdout.split("\n")[:-1]
    if listed:
        print(f"FAIL contents: carol expected nothing due, helper listed {listed}")
        return 1
    return 0


# A requested stamp, hash null, makes its node due; the node beside it, with a
# current stamp, is not. "Dana Lee" also checks that a name with a space is read.
def requested_is_due() -> int:
    import tempfile
    current = ["# Current\n", "\n", "Prose.\n", "\n"]
    real = fingerprint(current)
    text = (current[:1] + ["\n", "```yaml\n", "signers:\n", f"  Dana Lee: {{at: 2026-01-01, hash: {real}}}\n", "```\n"] + current[1:]
            + ["# Requested\n", "\n", "```yaml\n", "signers:\n", "  Dana Lee: {at: 2026-01-02, hash: null}\n", "```\n", "\n", "Prose.\n"])
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "requested.map.md"
        path.write_text("".join(text), encoding="utf-8")
        listed = subprocess.run([HELPER, path, "--due", "Dana Lee"], capture_output=True, text=True).stdout.split("\n")[:-1]
    if listed != ["Requested"]:
        print(f"FAIL requested: Dana Lee expected ['Requested'] due, helper listed {listed}")
        return 1
    return 0


# A stamp under the older approvals: key is still read: Dana Lee's is stale, so
# Old Key is due for her.
def older_key_read() -> int:
    import tempfile
    text = ["# Old Key\n", "\n", "```yaml\n", "approvals:\n", "  Dana Lee: {at: 2026-01-01, hash: 00000000}\n", "```\n", "\n", "Prose.\n"]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "old-key.map.md"
        path.write_text("".join(text), encoding="utf-8")
        listed = subprocess.run([HELPER, path, "--due", "Dana Lee"], capture_output=True, text=True).stdout.split("\n")[:-1]
    if listed != ["Old Key"]:
        print(f"FAIL older key: Dana Lee expected ['Old Key'] due, helper listed {listed}")
        return 1
    return 0


# --migrate renames the scaffolding key to signers: and nothing else: an approvals:
# key quoted in the prose stays, and carol's stamp is still current.
def migrate_renames_key() -> int:
    import tempfile
    body = ["# Migrated\n", "\n", "Prose quoting a key:\n", "\n", "```yaml\n", "approvals:\n", "```\n"]
    real = fingerprint(body)
    node = body[:1] + ["\n", "```yaml\n", "id: m1t\n", "approvals:\n", f"  carol: {{at: 2026-01-01, hash: {real}}}\n", "```\n"] + body[1:]
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "migrate.map.md"
        path.write_text("".join(node), encoding="utf-8")
        subprocess.run([HELPER, path, "--migrate"], capture_output=True, text=True)
        after = path.read_text(encoding="utf-8").splitlines(keepends=True)
        listed = subprocess.run([HELPER, path, "--due", "carol"], capture_output=True, text=True).stdout.split("\n")[:-1]
    expected = [line.replace("approvals:", "signers:") if i == 4 else line for i, line in enumerate(node)]
    if after != expected or listed:
        print(f"FAIL migrate: expected only the scaffolding key renamed and nothing due, got {after!r}, due {listed}")
        return 1
    return 0


if __name__ == "__main__":
    main()
