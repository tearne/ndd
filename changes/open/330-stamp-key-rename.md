# Stamp key rename

## Intent

Consider whether a node's `approvals:` key should become `signers:`, so the key matches the sign-off terminology the map now uses.

## Context

Raised as an aside on 2026-11-19 during 320. The sign-off terminology change (archived 2026-11-17) renamed approval to sign-off throughout but kept the `approvals:` key unchanged; a rename would touch every stamped map, the fingerprint helper, the viewer and their tests.
