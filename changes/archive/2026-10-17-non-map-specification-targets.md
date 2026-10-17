# Non-map specification targets

**Change Style:** Vibe

## Intent

Let a Formal Change Specification hold targets for non-map assets, in addition to the map nodes it proposes, kept inline or in the companion folder. Each is surfaced as a diff and approved like a node, and Build lands what was approved. Which assets are specified upfront is negotiated with the change. The map stays authoritative: a target overlapping its job is questioned.

## Bounds

Map edits are confined to Change Specification and Formal Build. Each AGENT-RULES edit is surfaced as a diff before it lands. The Map node's assumption stays as it is.

## Context

Promoted from discussion [parking and session loss](../archive/2026-10-17-parking-and-session-loss-discussion.md) (2026-10-17). In change 020, non-map work had no approved home and landed unseen. Relaxes the map-only restriction from archived `2026-10-07-formal-specification-as-map-content`, whose concern was a parallel specification and not other assets.

## Log

- Claimed 2.6.0-dev (minor).
- "Closing act" replaced by plainer wording in Formal Build, which also touched Change Specification and rule 16 (renamed Formal Build Promotion).
- User cut Change Specification to 787 characters, dropping the stall paragraph on purpose; restamped after wording fixes.
- Rule 8 rewritten and renamed Show Edits as Diffs, to govern the form of any edit put up for approval; 040's Intent updated to the new title.
- Rule 8's diff-fence wording found to have no map source; noted in 040.

## Conclude

Change Specification took a third edit, "at Build's closing act" becoming "at the end of Build", to match Formal Build's plainer "Last of all". The user then trimmed it from 1102 to 787 characters, dropping the paragraph on a stalled specification and the line on where development happens. Supporting rules changed to match; rule 8's diff fence was found to lack a map source and is noted in 040.
