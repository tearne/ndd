# Parking and session state

## Intent

Let work be paused on request, by the `pause:` keyword or in plain words, and resumed without misreading its state. Pausing writes `changes/resume.md` naming what was in progress, where it sits and what is unapproved; the Startup Scan reports it with its date, and the first write after resuming deletes it. Detail stays in the discussion's Resume anchor or the build's Log. A draft written in place sits between `<!-- draft -->` and `<!-- /draft -->` until approved. Build logs each settled plan item.

## Context

Promoted from discussion [parking and session loss](../archive/2026-10-17-parking-and-session-loss-discussion.md) (2026-10-17), which records the reasoning and the 020 incident behind it. The Startup Scan is already weighty, so its additions stay minimal. Deletion waits for the first write so that a start-and-quit restart keeps the note.
