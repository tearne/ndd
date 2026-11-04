#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

# NDD installer. Copies the shipped assets out of this checkout into a fresh
# ./ndd/ in the current project, as they are on disk, and wires up the agent
# entry files. Re-run at any time to upgrade in place (git pull this repo first); the
# prior method map is kept as ndd/method/ndd.prev.map.md so migration can be
# reasoned about.
#
# Nothing is rendered: what ships is the files in SHIPPED, uncommitted edits
# included, and nothing else of the checkout. The NDD repository reads its own files
# directly and is never installed into itself. Clone the repo wherever
# you like and run this from the project you want to opt in, e.g.
#   cd my-project && path/to/ndd/install.py

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from rich.console import Console

console = Console()

SOURCE = Path(__file__).parent
# What the agent and user need at run time, as map.md#shipped-assets lists it:
# the method directory whole, and the root files that describe the release. The
# install test's link check catches a shipped link leaving what ships.
SHIPPED = ["method", "CHANGELOG.md", "README.md", "LICENSE"]

RULES = "ndd/method/AGENT-RULES.md"
CLAUDE_POINTER = f"@{RULES}"
AGENTS_INSTRUCTION = (
    "# Agent instructions\n\n"
    f"Read `{RULES}` and follow it before doing anything else."
)


def main():
    parse_args()
    project = Path.cwd()
    ndd = project / "ndd"
    refuse_own_checkout(project)
    console.print(f"Installing NDD into [bold]{project}[/bold]\n")

    copy_method(ndd)
    created = [path.name for path, desired in ((project / "CLAUDE.md", CLAUDE_POINTER), (project / "AGENTS.md", AGENTS_INSTRUCTION))
               if own_entry_file(path, desired)]
    ensure_gitignore(project / ".gitignore", ignored_entries(project, created))

    console.print("\n[bold green]Done.[/bold green] NDD installed into ./ndd/")


# Write ndd/ fresh, so nothing an earlier version shipped lingers. Every
# shipped file is checked first, so a broken checkout leaves ndd/ untouched.
def copy_method(ndd: Path) -> None:
    sources = shipped_files()
    previous = previous_map(ndd)
    if ndd.exists():
        shutil.rmtree(ndd)
        report("cleared", ndd)
    for src in sources:
        copy_asset(src, ndd / src.relative_to(SOURCE))
    if previous:
        (ndd / "method" / "ndd.prev.map.md").write_text(previous)
        report("backed up", ndd / "method" / "ndd.prev.map.md", "previous map")


def shipped_files() -> list[Path]:
    missing = [name for name in SHIPPED if not (SOURCE / name).exists()]
    if missing:
        console.print(f"[bold red]Error:[/bold red] shipped assets missing from the checkout: {', '.join(missing)}")
        sys.exit(1)
    files = []
    for name in SHIPPED:
        path = SOURCE / name
        files += sorted(p for p in path.rglob("*") if p.is_file()) if path.is_dir() else [path]
    return files


# The map to keep as ndd.prev.map.md: the old one if the new differs, else the
# existing backup — so a redundant re-run preserves the last real one. Each is
# looked for under method/ first, then where the flat layout before 3.0.0 kept it.
def previous_map(ndd: Path) -> str | None:
    old, backup = installed(ndd, "ndd.map.md"), installed(ndd, "ndd.prev.map.md")
    if old and old.read_text() != (SOURCE / "method" / "ndd.map.md").read_text():
        return old.read_text()
    return backup.read_text() if backup else None


def installed(ndd: Path, name: str) -> Path | None:
    return next((p for p in (ndd / "method" / name, ndd / name) if p.exists()), None)


# An entry file whose whole content is a pointer into ndd/ is installer
# boilerplate from some version, and fair game to rewrite; anything more is the
# consumer's own and is never overwritten. Returns whether it was created.
def own_entry_file(path: Path, desired: str) -> bool:
    if path.exists():
        current = path.read_text().rstrip("\n")
        if current == desired:
            report("already present", path)
            return False
        if not is_installer_pointer(current, desired):
            report("conflict", path, f"exists with other content — add '{desired}' yourself")
            return False
        path.write_text(desired + "\n")
        report("updated", path, "pointer refreshed")
        return False
    path.write_text(desired + "\n")
    report("created", path)
    return True


def is_installer_pointer(current: str, desired: str) -> bool:
    shape = re.escape(desired).replace(re.escape(RULES), r"ndd/[^\s`]+")
    return re.fullmatch(shape, current) is not None


# Ignore only what the project doesn't already own: an entry file it had
# before is its own, and so is a .claude/ with files checked in.
def ignored_entries(project: Path, created: list[str]) -> list[str]:
    entries = ["ndd/", *created]
    if not tracks_files_under(project, ".claude"):
        entries.append(".claude/")
    return entries


def tracks_files_under(project: Path, directory: str) -> bool:
    # A silent probe, so not echoed through a run() helper; a missing git exits non-zero.
    result = subprocess.run(f"git ls-files -- {directory}", shell=True, cwd=project, capture_output=True, text=True)
    return result.returncode == 0 and bool(result.stdout.strip())


def ensure_gitignore(path: Path, entries: list[str]) -> None:
    content = path.read_text() if path.exists() else ""
    lines = content.splitlines()
    to_add = [e for e in entries if e not in lines]
    if not to_add:
        report("already present", path)
        return
    separator = "\n" if content and not content.endswith("\n") else ""
    with path.open("a") as f:
        f.write(separator + "\n".join(to_add) + "\n")
    report("updated", path, f"added: {', '.join(to_add)}")


# Shipped scripts must stay runnable, so the mode travels with the text.
def copy_asset(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    shutil.copymode(src, dest)
    report("copied", dest)


# The NDD repository reads its own sources — method/ and the maps at its root —
# so installing it into itself would only make a copy that lags.
def refuse_own_checkout(project: Path) -> None:
    if project.resolve() == SOURCE.resolve():
        console.print(
            "[bold red]Error:[/bold red] refusing to run — this is the NDD checkout, which reads its sources directly.\n"
            "Run install.py from the project you want to opt in."
        )
        sys.exit(1)


def parse_args() -> None:
    parser = argparse.ArgumentParser(description="Opt a project in to the NDD method.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {read_version()}")
    parser.parse_args()


# Single source of truth: the top CHANGELOG heading, so there is no separate
# constant to forget to bump.
def read_version() -> str:
    for line in (SOURCE / "CHANGELOG.md").read_text().splitlines():
        if line.startswith("## "):
            return line[3:].split("—")[0].strip()
    return "unknown"


def report(status: str, path: Path, note: str = "") -> None:
    colours = {"created": "green", "copied": "green", "updated": "cyan", "backed up": "cyan",
               "already present": "dim", "conflict": "yellow", "cleared": "magenta"}
    colour = colours.get(status, "white")
    label = f"[{colour}]{status:<15}[/{colour}]"
    detail = f"  [dim]{note}[/dim]" if note else ""
    console.print(f"  {label} {path}{detail}")


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("Error: no virtual environment detected. Run this script via './install.py' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    main()
