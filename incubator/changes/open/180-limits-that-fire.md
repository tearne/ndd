# Limits that actually fire

## Intent

The method's numeric limits do not fire in practice. Two consecutive changes ran their [Approach](#approach) at roughly 3× the ~1000-character trigger unnoticed, and ten map nodes now sit over the ~800 bound in [Node Sizing](#node-sizing) despite [Consistency Upkeep](#consistency-upkeep) obliging the agent to flag exactly that. Same defect on both surfaces: a limit nobody measures.

Also to settle: whether the numbers are right. A ~1000-character Approach covering six decisions-with-reasons may simply be too tight, in which case the limits rise rather than the discipline tightening. The build should include a sweep of the nodes currently over.

Contributing causes observed: the limits live in **Detail**, read once at navigation rather than at use; they are phrased as outcomes ("a soft trigger flags borderline material") with no actor or verb; a character count cannot be eyeballed, so a rule honoured only by measuring must say to measure; and the check assumes a single "before surfacing" moment, which incremental drafting — a part growing turn by turn as items fold in — never reaches.

Parked via aside during change 170's planning (2026-08-28), prompted by the user asking whether that change was within its limits; widened at its conclusion to cover node sizing.
