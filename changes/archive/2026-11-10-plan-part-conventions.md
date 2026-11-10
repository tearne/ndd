# Plan part conventions

**Change Style:** Vibe

## Intent

An Intent should state what the change should achieve in modal language, such as "A change should hold…", rather than in the present tense, which reads as a description of what already exists. A Vibe change's Bounds should have a cap of about 500 characters, up from about 200. Every cap should read as a ceiling, never a target: a part that can be said in half the space should be.

## Bounds

Only *Intent*, *Caps* and the *Caps* rule change; *Bounds* keeps its warning against wordiness. The reworded *Caps* rule is A/B tested before it ships.

## Context

Both raised as asides on 2026-11-10: the modal voice during 106's Intent trim, whose draft opened "A change holds on disk…"; the Bounds cap while drafting 107's Bounds.

## Log

- 2026-11-10: Plan approved; Build Lock taken.
- 2026-11-10: Minor bump agreed, claiming 3.4.0-dev.
- 2026-11-10: Error in the Intent's wording: "modal language" was jargon the user could not read when approving; corrected in Build to "the voice of a requirement", with "the application should…" and "update the…" as examples.
- 2026-11-10: *Intent* node updated and stamped (2df60ca2); 783 characters.
- 2026-11-10: *Caps* updated and stamped (fcfadc36): caps are ceilings, not targets; Bounds ~500.
- 2026-11-10: *Caps* rule rewording approved; A/B test running before it lands.
- 2026-11-10: Caps rule A/B test: with Bounds at ~500, a Bounds draft with real content ran 309 against 177 under ~200, same four bounds; the ceiling line shortened an Intent slightly (305 against 349); trivial Bounds alike (113, 94). Deviation agreed with the user: Bounds stays ~200, the ceiling line kept. *Caps* table reverted and re-stamped (cc37c7ca).
- 2026-11-10: *Caps* rule landed in `method/AGENT-RULES.md` with the ceiling sentence only; Bounds stays ~200. Not re-tested: the tested wording differed only in the cap, and the sentence alone shortened the Intent.

## Conclude

Built within Bounds, touching `method/ndd.map.md` and `method/AGENT-RULES.md`. Two departures from the Intent: its "modal language" was jargon, so *Intent* now asks for the voice of a requirement; and the A/B test showed a ~500 Bounds cap invites padding, so Bounds stays at ~200, with only the ceiling sentence landed.
