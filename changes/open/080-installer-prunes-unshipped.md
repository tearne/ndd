# Installer prunes unshipped files

## Intent

On upgrade the installer copies the checkout over the existing `ndd/` without clearing it, so a file deleted from NDD lingers in client installs unless someone remembers to name it in `RETIRED_FILES`. Have the installer remove whatever in `ndd/` it does not ship, keeping its own `ndd.prev.map.md` backup, so retiring a file needs no list.

Raised during change 020 (2026-10-16).
