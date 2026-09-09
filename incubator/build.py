#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

# NDD build step. Renders the shippable method into ./dist/, which is exactly
# what install.py copies into a consumer's ./ndd/. Sources stay where they are
# edited — map.md, CHANGELOG.md and standards/ at the root — and are copied in
# here, the map under its shipped name ndd.md. dist/AGENT-RULES.md is not
# generated: it is hand-maintained in place, since its links target ndd.md.
#
# Run after any edit to a source file, before committing. `--check` reports
# what is stale without writing, exiting non-zero if anything is; install.py
# uses the same check to refuse to ship a stale dist.

import argparse
import sys
from pathlib import Path

from rich.console import Console

console = Console()

SOURCE = Path(__file__).parent
DIST = SOURCE / "dist"


# Every (source, dist) pair the build maintains. The map is the one rename.
def rendered_pairs() -> list[tuple[Path, Path]]:
    pairs = [
        (SOURCE / "map.md", DIST / "ndd.md"),
        (SOURCE / "CHANGELOG.md", DIST / "CHANGELOG.md"),
    ]
    for guide in sorted((SOURCE / "standards").iterdir()):
        if guide.is_file():
            pairs.append((guide, DIST / "standards" / guide.name))
    return pairs


# Deploy files whose content differs from their source, or are missing.
def stale_files() -> list[Path]:
    return [dest for src, dest in rendered_pairs()
            if not dest.exists() or dest.read_text() != src.read_text()]


def build() -> None:
    console.print(f"Rendering NDD into [bold]{DIST}[/bold]\n")
    for src, dest in rendered_pairs():
        write_asset(dest, src.read_text())
    console.print("\n[bold green]Done.[/bold green]")


def check() -> None:
    stale = stale_files()
    if not stale:
        console.print("[green]dist/ is up to date.[/green]")
        return
    console.print("[bold red]dist/ is stale[/bold red] — run ./build.py:")
    for path in stale:
        console.print(f"  {path}")
    sys.exit(1)


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


def report(status: str, path: Path) -> None:
    colours = {"created": "green", "updated": "cyan", "already present": "dim"}
    label = f"[{colours.get(status, 'white')}]{status:<15}[/{colours.get(status, 'white')}]"
    console.print(f"  {label} {path.relative_to(SOURCE)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the NDD method into ./dist/.")
    parser.add_argument("--check", action="store_true",
                        help="report stale files without writing; exit 1 if any")
    args = parser.parse_args()
    check() if args.check else build()


if __name__ == "__main__":
    main()
