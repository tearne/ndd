#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Checks install.py end to end, as testing.map.md#install-check describes: it
# refuses its own checkout, a fresh install ships exactly the shipped assets
# with scripts executable and every link resolving within what ships, an upgrade
# backs up a changed ndd.map.md and clears strays, from the flat layout too,
# an entry file the project already had stays out of .gitignore, and the shipped map
# viewer serves the project's map.

import re
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

CHECKOUT = Path(__file__).resolve().parent.parent
INSTALLER = CHECKOUT / "install.py"
# The shipped assets as map.md#shipped-assets lists them, held here
# independently of the installer's own list so the two are checked against each other.
SHIPPED_ASSETS = ["method", "CHANGELOG.md", "README.md", "LICENSE"]
RULES = "ndd/method/AGENT-RULES.md"
STRAY = "BOOTSTRAP.md"
failures = []


def main():
    refuses_own_checkout()
    with tempfile.TemporaryDirectory() as scratch:
        project = Path(scratch)
        install(project)
        ships_exactly_the_shipped_assets(project / "ndd")
        entry_files_point_into_ndd(project)
        scripts_are_executable(project / "ndd")
        every_link_resolves(project / "ndd")
        viewer_serves_the_project(project)
        upgrade_backs_up_and_clears_strays(project)
    with tempfile.TemporaryDirectory() as scratch:
        flat_layout_upgrade_backs_up_and_clears_strays(Path(scratch))
    with tempfile.TemporaryDirectory() as scratch:
        existing_entry_file_is_not_ignored(Path(scratch))
    for failure in failures:
        print(f"FAIL {failure}")
    print("OK" if not failures else f"{len(failures)} failures")
    sys.exit(1 if failures else 0)


def refuses_own_checkout():
    result = install(CHECKOUT, expect_success=False)
    check(result.returncode != 0, "installer ran inside its own checkout")
    check(not (CHECKOUT / "ndd").exists(), "installer wrote ndd/ into its own checkout")


def ships_exactly_the_shipped_assets(ndd: Path):
    expected = set()
    for name in SHIPPED_ASSETS:
        path = CHECKOUT / name
        found = [p for p in path.rglob("*") if p.is_file() and "__pycache__" not in p.parts] if path.is_dir() else [path]
        expected |= {p.relative_to(CHECKOUT) for p in found}
    shipped = {p.relative_to(ndd) for p in ndd.rglob("*") if p.is_file()}
    check(shipped == expected, f"shipped set differs: extra {sorted(map(str, shipped - expected))}, missing {sorted(map(str, expected - shipped))}")
    check(not any("__pycache__" in p.parts for p in shipped), "a bytecode cache was shipped")
    print("shipped:", *sorted(map(str, shipped)), sep="\n  ")


def entry_files_point_into_ndd(project: Path):
    check((project / "CLAUDE.md").read_text().strip() == f"@{RULES}", "CLAUDE.md is not the pointer")
    check(RULES in (project / "AGENTS.md").read_text(), f"AGENTS.md does not name {RULES}")
    ignored = (project / ".gitignore").read_text().splitlines()
    for entry in ["ndd/", "CLAUDE.md", "AGENTS.md", ".claude/"]:
        check(entry in ignored, f".gitignore lacks {entry}")


def scripts_are_executable(ndd: Path):
    for script in ndd.rglob("*.py"):
        check(script.stat().st_mode & 0o111, f"{script.relative_to(ndd)} is not executable")


def every_link_resolves(ndd: Path):
    for md in ndd.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", md.read_text()):
            if target.startswith("http"):
                continue
            file, _, anchor = target.partition("#")
            linked = (md if not file else md.parent / file).resolve()
            check(linked.is_relative_to(ndd.resolve()), f"{md.relative_to(ndd)} links outside what ships: {target}")
            check(linked.exists(), f"{md.relative_to(ndd)} links to missing {target}")
            if anchor and linked.exists():
                check(anchor in anchors(linked), f"{md.relative_to(ndd)} links to missing anchor {target}")


# The viewer ships with the method and, run from the project root, serves the project's map.
def viewer_serves_the_project(project: Path):
    viewer = project / "ndd" / "method" / "util" / "map_viewer.py"
    if not viewer.exists():
        return check(False, "the map viewer is not shipped")
    (project / "map.md").write_text("# Project\n\nA project's map.\n")
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    server = subprocess.Popen([str(viewer), "--port", str(port)], cwd=project,
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        page = ""
        for _ in range(100):  # uv may take a moment to start it
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/") as response:
                    page = response.read().decode("utf-8")
                break
            except OSError:
                time.sleep(0.1)
        check("<h1>Project</h1>" in page, "the shipped viewer did not serve the project's map")
    finally:
        server.terminate()
        server.wait()
        (project / "map.md").unlink()


def upgrade_backs_up_and_clears_strays(project: Path):
    ndd, method = project / "ndd", project / "ndd" / "method"
    changed = (method / "ndd.map.md").read_text() + "\nan edit from before the upgrade\n"
    (method / "ndd.map.md").write_text(changed)
    (ndd / STRAY).write_text("shipped by an earlier version\n")
    install(project)
    check((method / "ndd.prev.map.md").read_text() == changed, "changed ndd.map.md was not backed up as ndd.prev.map.md")
    check((method / "ndd.map.md").read_text() == (CHECKOUT / "method" / "ndd.map.md").read_text(), "ndd.map.md was not refreshed")
    check(not (ndd / STRAY).exists(), f"stray {STRAY} was not cleared")


# Before 3.0.0 the method sat flat in ndd/; the first upgrade still keeps its map.
def flat_layout_upgrade_backs_up_and_clears_strays(project: Path):
    ndd = project / "ndd"
    ndd.mkdir()
    old = (CHECKOUT / "method" / "ndd.map.md").read_text() + "\nthe map as the flat layout held it\n"
    (ndd / "ndd.map.md").write_text(old)
    (ndd / STRAY).write_text("shipped by an earlier version\n")
    install(project)
    check((ndd / "method" / "ndd.prev.map.md").read_text() == old, "flat-layout ndd.map.md was not backed up as method/ndd.prev.map.md")
    check(not (ndd / "ndd.map.md").exists() and not (ndd / STRAY).exists(), "flat-layout files were not cleared")


def existing_entry_file_is_not_ignored(project: Path):
    own = "# Our own agent notes\n"
    (project / "CLAUDE.md").write_text(own)
    install(project)
    check((project / "CLAUDE.md").read_text() == own, "the project's own CLAUDE.md was overwritten")
    check("CLAUDE.md" not in (project / ".gitignore").read_text().splitlines(), "the project's own CLAUDE.md was put in .gitignore")


def install(project: Path, expect_success: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run([INSTALLER], cwd=project, capture_output=True, text=True)
    if expect_success:
        check(result.returncode == 0, f"installer failed in {project}:\n{result.stdout}{result.stderr}")
    return result


def anchors(md: Path) -> set[str]:
    headings = re.findall(r"^#{1,6} (.+?)\s*$", md.read_text(), re.M)
    return {re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-") for h in headings}


def check(condition, failure: str):
    if not condition:
        failures.append(failure)


if __name__ == "__main__":
    main()
