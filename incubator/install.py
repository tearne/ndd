#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

# NDD installer. Copies the method's source files out of this checkout into
# ./ndd/ in the current project, as they are, and wires up the agent entry
# files. Re-run at any time to upgrade in place (git pull this repo first); the
# prior method map is kept as ndd/ndd.prev.map.md so migration can be reasoned
# about.
#
# Nothing is rendered: what ships is the checkout's own map.md, ndd.map.md,
# CHANGELOG.md, AGENT-RULES.md and standards/. The NDD repository reads those
# files directly and is never installed into itself. Clone the repo wherever
# you like and run this from the project you want to opt in, e.g.
#   cd my-project && path/to/ndd/install.py

import argparse
import os
import re
import sys
from pathlib import Path

from rich.console import Console

console = Console()

SOURCE = Path(__file__).parent
SHIPPED = ["map.md", "ndd.map.md", "CHANGELOG.md", "AGENT-RULES.md", "standards"]
RETIRED_FILES = ["BOOTSTRAP.md", "ndd.md", "ndd.prev.md"]  # shipped by earlier versions; removed on upgrade

CLAUDE_POINTER = "@ndd/AGENT-RULES.md"
AGENTS_INSTRUCTION = (
    "# Agent instructions\n\n"
    "Read `ndd/AGENT-RULES.md` and follow it before doing anything else."
)
GITIGNORE_ENTRIES = ["ndd/", "CLAUDE.md", "AGENTS.md", ".claude/"]


def main():
    parse_args()
    project = Path.cwd()
    ndd = project / "ndd"
    refuse_own_checkout(project)
    console.print(f"Installing NDD into [bold]{project}[/bold]\n")

    copy_method(ndd)
    own_entry_file(project / "CLAUDE.md", CLAUDE_POINTER)
    own_entry_file(project / "AGENTS.md", AGENTS_INSTRUCTION)
    ensure_gitignore(project / ".gitignore")

    console.print("\n[bold green]Done.[/bold green] NDD installed into ./ndd/")


# Copy the shipped files into ndd/ as they are. Files retired from the method
# are removed on upgrade.
def copy_method(ndd: Path) -> None:
    ndd.mkdir(parents=True, exist_ok=True)
    for name in SHIPPED:
        root = SOURCE / name
        files = sorted(p for p in root.rglob("*") if p.is_file()) if root.is_dir() else [root]
        for src in files:
            dest = ndd / src.relative_to(SOURCE)
            if dest.name == "ndd.map.md":
                back_up_map(dest, src.read_text())
            copy_asset(src, dest)
    for name in RETIRED_FILES:
        retired = ndd / name
        if retired.exists():
            retired.unlink()
            report("removed", retired, "no longer part of the method")


# Keep the old map as ndd.prev.map.md only when it actually changed — so a
# redundant re-run preserves the last real backup.
def back_up_map(dest: Path, content: str) -> None:
    if dest.exists() and dest.read_text() != content:
        backup = dest.parent / "ndd.prev.map.md"
        backup.write_text(dest.read_text())
        report("backed up", backup, "previous map")


# An entry file whose whole content is a pointer into ndd/ is installer
# boilerplate from some version, and fair game to rewrite; anything more is the
# consumer's own and is never overwritten.
def own_entry_file(path: Path, desired: str) -> None:
    if path.exists():
        current = path.read_text().rstrip("\n")
        if current == desired:
            report("already present", path)
            return
        if not is_installer_pointer(current, desired):
            report("conflict", path, f"exists with other content — add '{desired}' yourself")
            return
        path.write_text(desired + "\n")
        report("updated", path, "pointer refreshed")
        return
    path.write_text(desired + "\n")
    report("created", path)


def is_installer_pointer(current: str, desired: str) -> bool:
    shape = re.escape(desired).replace(re.escape("ndd/AGENT-RULES.md"), r"ndd/[^\s`]+")
    return re.fullmatch(shape, current) is not None


def ensure_gitignore(path: Path) -> None:
    content = path.read_text() if path.exists() else ""
    lines = content.splitlines()
    to_add = [e for e in GITIGNORE_ENTRIES if e not in lines]
    if not to_add:
        report("already present", path)
        return
    separator = "\n" if content and not content.endswith("\n") else ""
    with path.open("a") as f:
        f.write(separator + "\n".join(to_add) + "\n")
    report("updated", path, f"added: {', '.join(to_add)}")


def copy_asset(src: Path, dest: Path) -> None:
    write_asset(dest, src.read_text())


def write_asset(dest: Path, content: str) -> None:
    if dest.exists():
        if dest.read_text() == content:
            report("already present", dest)
            return
        dest.write_text(content)
        report("updated", dest)
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content)
    report("created", dest)


# The NDD repository reads its own sources — AGENT-RULES.md and the maps at
# its root — so installing it into itself would only make a copy that lags.
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
    colours = {"created": "green", "updated": "cyan", "backed up": "cyan",
               "already present": "dim", "conflict": "yellow", "removed": "magenta"}
    colour = colours.get(status, "white")
    label = f"[{colour}]{status:<15}[/{colour}]"
    detail = f"  [dim]{note}[/dim]" if note else ""
    console.print(f"  {label} {path}{detail}")


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("Error: no virtual environment detected. Run this script via './install.py' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    main()
