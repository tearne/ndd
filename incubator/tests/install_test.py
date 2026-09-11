#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# ///

# Checks install.py end to end, as testing.map.md#install-check describes: it
# refuses its own checkout, a fresh install ships every tracked file but the
# entry files with scripts executable and every link resolving, and an upgrade
# backs up a changed ndd.map.md and removes retired files.

import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHECKOUT = Path(__file__).resolve().parent.parent
INSTALLER = CHECKOUT / "install.py"
NOT_SHIPPED = {"CLAUDE.md", "AGENTS.md"}
RETIRED = "BOOTSTRAP.md"
failures = []


def main():
    refuses_own_checkout()
    with tempfile.TemporaryDirectory() as scratch:
        project = Path(scratch)
        install(project)
        ships_the_checkout_minus_residue(project / "ndd")
        entry_files_point_into_ndd(project)
        scripts_are_executable(project / "ndd")
        every_link_resolves(project / "ndd")
        upgrade_backs_up_and_retires(project)
    for failure in failures:
        print(f"FAIL {failure}")
    print("OK" if not failures else f"{len(failures)} failures")
    sys.exit(1 if failures else 0)


def refuses_own_checkout():
    result = install(CHECKOUT, expect_success=False)
    check(result.returncode != 0, "installer ran inside its own checkout")
    check(not (CHECKOUT / "ndd").exists(), "installer wrote ndd/ into its own checkout")


def ships_the_checkout_minus_residue(ndd: Path):
    tracked = subprocess.run(["git", "ls-files"], cwd=CHECKOUT, capture_output=True, text=True, check=True).stdout.split()
    expected = {Path(name) for name in tracked if name not in NOT_SHIPPED}
    shipped = {p.relative_to(ndd) for p in ndd.rglob("*") if p.is_file()}
    check(shipped == expected, f"shipped set differs: extra {sorted(map(str, shipped - expected))}, missing {sorted(map(str, expected - shipped))}")
    print("shipped:", *sorted(map(str, shipped)), sep="\n  ")


def entry_files_point_into_ndd(project: Path):
    check((project / "CLAUDE.md").read_text().strip() == "@ndd/AGENT-RULES.md", "CLAUDE.md is not the pointer")
    check("ndd/AGENT-RULES.md" in (project / "AGENTS.md").read_text(), "AGENTS.md does not name ndd/AGENT-RULES.md")
    check("ndd/" in (project / ".gitignore").read_text().splitlines(), ".gitignore lacks ndd/")


def scripts_are_executable(ndd: Path):
    for script in ndd.rglob("*.py"):
        check(script.stat().st_mode & 0o111, f"{script.relative_to(ndd)} is not executable")


# Change records under changes/ cite the map by bare anchor and are not checked.
def every_link_resolves(ndd: Path):
    for md in ndd.rglob("*.md"):
        if md.relative_to(ndd).parts[0] == "changes":
            continue
        for target in re.findall(r"\]\(([^)]+)\)", md.read_text()):
            if target.startswith("http"):
                continue
            file, _, anchor = target.partition("#")
            linked = md if not file else md.parent / file
            check(linked.exists(), f"{md.relative_to(ndd)} links to missing {target}")
            if anchor and linked.exists():
                check(anchor in anchors(linked), f"{md.relative_to(ndd)} links to missing anchor {target}")


def upgrade_backs_up_and_retires(project: Path):
    ndd = project / "ndd"
    changed = (ndd / "ndd.map.md").read_text() + "\nan edit from before the upgrade\n"
    (ndd / "ndd.map.md").write_text(changed)
    (ndd / RETIRED).write_text("shipped by an earlier version\n")
    install(project)
    check((ndd / "ndd.prev.map.md").read_text() == changed, "changed ndd.map.md was not backed up as ndd.prev.map.md")
    check((ndd / "ndd.map.md").read_text() == (CHECKOUT / "ndd.map.md").read_text(), "ndd.map.md was not refreshed")
    check(not (ndd / RETIRED).exists(), f"retired {RETIRED} was not removed")


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
