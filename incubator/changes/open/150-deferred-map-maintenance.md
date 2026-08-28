# Deferred map maintenance / catch-up

## Intent

Does the method degrade nicely when the user chooses *not* to update the map after every change — e.g. during an emergency fix, or while focused on a larger-picture push — intending to pick map maintenance up later? Today the **Sync Rule** and **Engagement Rule** frame per-change map upkeep as the norm; the method should have an explicit, graceful account of *deferring* it: a way to mark that reality has moved ahead of the map (a known, acknowledged drift debt), keep working, and later reconcile — without the deferral being silent rot or a broken invariant.

Open questions when picked up: how deferred drift is recorded (a lightweight marker vs. an open change vs. nothing), how the **Startup Scan** surfaces outstanding catch-up, whether this is just "an open change that says map-catch-up pending," and how it interacts with **Conceptual Drift** and cross-agent falsifiability. Relates to Edit Governance (Sync/Engagement Rules), Map Maintenance, and Startup Scan.

Parked via `aside:` during change 140's build approval (2026-08-28).
