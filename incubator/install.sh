#!/usr/bin/env bash
set -euo pipefail

# NDD installer. Fetches the method into ./ndd/ and wires up the agent entry
# files at the project root. Re-run at any time to upgrade in place; the prior
# method map is kept as ndd/ndd.prev.md so migration can be reasoned about.
#
# Source is the tip of the method's main branch by default; override NDD_BASE_URL
# (for example with a file:// URL) to install from an alternate location.

NDD_BASE_URL="${NDD_BASE_URL:-https://raw.githubusercontent.com/tearne/ndd/main}"

CLAUDE_POINTER='@ndd/BOOTSTRAP.md'
AGENTS_INSTRUCTION='# Agent instructions

Read `ndd/BOOTSTRAP.md` and follow it before doing anything else.'

GITIGNORE_ENTRIES=("ndd/" "CLAUDE.md" "AGENTS.md" ".claude/")

main() {
  download_method
  own_entry_file CLAUDE.md "$CLAUDE_POINTER"
  own_entry_file AGENTS.md "$AGENTS_INSTRUCTION"
  ensure_gitignore
  echo "NDD installed into ./ndd/"
}

download_method() {
  mkdir -p ndd
  refresh_map
  fetch BOOTSTRAP.md ndd/BOOTSTRAP.md
  fetch CHANGELOG.md ndd/CHANGELOG.md
}

# Fetch the new map beside the old, and keep the old as ndd.prev.md only when it
# actually changed — so a redundant re-run preserves the last real backup.
refresh_map() {
  fetch ndd.md ndd/ndd.md.new
  if [ -f ndd/ndd.md ] && ! cmp -s ndd/ndd.md.new ndd/ndd.md; then
    cp ndd/ndd.md ndd/ndd.prev.md
  fi
  mv ndd/ndd.md.new ndd/ndd.md
}

fetch() {
  curl -fsSL "$NDD_BASE_URL/$1" -o "$2"
}

own_entry_file() {
  local path="$1" desired="$2"
  if [ -f "$path" ]; then
    if [ "$(cat "$path")" = "$desired" ]; then
      return
    fi
    echo "warning: $path already exists with other content — left untouched; add '$CLAUDE_POINTER' yourself" >&2
    return
  fi
  printf '%s\n' "$desired" > "$path"
}

ensure_gitignore() {
  touch .gitignore
  local entry
  for entry in "${GITIGNORE_ENTRIES[@]}"; do
    if ! grep -qxF "$entry" .gitignore; then
      printf '%s\n' "$entry" >> .gitignore
    fi
  done
}

main "$@"
