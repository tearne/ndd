# Where the rules live

## Intent

The map cannot enforce the rules it states: it is read when the agent chooses to read it, while `BOOTSTRAP.md` is loaded every session unconditionally. Rules that must fire at a particular moment — the edit order, what an approval covers, what a batch may contain — therefore live in the artefact least able to trigger them. Split the carriers: the map explains the method, the always-loaded file carries the short imperative form.

## Context

Evidence from change 210, which fixed the map's unenforceable wording and then watched the same defect recur one level up. Two failures in one session, both after the fix had landed:

- Several edits were batched into one script and applied without being surfaced. One item in the batch was a legitimately mechanical correction, and the whole batch inherited that fast path — the exemption added minutes earlier was the hole it fell through.
- "Agreed, archiving node" was read as approving prose that did not yet exist. Approval of a decision is not approval of its wording, and the edit order does not say so.

The rule that never slipped all session was the character count, because it emits something visible in the agent's message that the user notices missing. Compliance that leaves no trace failed repeatedly; compliance that produces an artefact held. That asymmetry is the thread to pull.

### Research findings (2026-09-04)

A web search of vendor documentation and published experiments, prompted by the question of what actually maximises compliance. The full trail is recoverable from the sources named here.

- **Instruction count is the dominant variable.** Adherence degrades as the number of instructions rises, and degrades roughly *uniformly across all rules* rather than dropping the newest — so every non-essential rule taxes the essential ones. IFScale (arXiv:2507.11538) measures 68% accuracy at 500 instructions; ManyIFEval (arXiv:2509.21051) reproduces the trend at ≤10. IBM (arXiv:2510.14842) attributes much of it to conflict between instructions.
- **Vendors converge on brevity**: Anthropic targets under 200 lines and states "longer files consume more context and reduce adherence"; GitHub says two pages; Cursor 500 lines. No published experiment isolates file length itself — the length advice is vendor assertion resting on the instruction-count evidence.
- **Such files are context, not enforcement.** Anthropic: "there's no guarantee of strict compliance", and anything that must fire at a lifecycle point should be a hook, which runs regardless of what the agent decides.
- **Bare prohibitions are a poor tool.** Negated prompts show inverse scaling with model size (arXiv:2209.12711), and naming a forbidden thing raises its salience (arXiv:2511.12381). Anthropic advises saying what to do instead, with the reason attached, since the model generalises from the explanation.
- **Unconditional absolutes induce fabricated compliance** (OpenAI GPT-4.1 guide): "you must always X" without an escape clause produces invented X. The fix is an explicit "if you can't, stop and ask".
- **Concrete beats conceptual.** Anthropic's own examples: "Run `npm test` before committing", not "test your changes". The method's count-and-report rule is already this shape, which is consistent with it being the one rule that never slipped.
- **Prefer pointers to copies**, and re-injection beats a single early read — harnesses re-read their instruction file after compaction, and repetition is what sustains suppression of an unwanted behaviour.
- **Position matters**: instructions at the beginning and end of long context outperform the middle (arXiv:2307.03172).
- Weakly evidenced, and to be treated as hypotheses rather than findings: trigger-shaped phrasing, proof-of-compliance tokens, restating rule numbers, and capitalised MUST/NEVER — no experiment found, and vendors disagree on capitals.

## Approach

- **The rendering is a selection, not a translation.** Rendering every rule that fires would degrade the rules that matter. The file carries the fewest imperatives that plausibly change behaviour; everything else stays in the map, reachable by address.

- **A rule earns its place by a three-part test**: it applies in essentially every session, it is concrete enough that a reader can tell whether it was followed, and getting it wrong is costly or has already gone wrong in practice. The bar is a starting position rather than a settled one — the first pass over the map is also the experiment that tells us whether it is too strict.

- **Each imperative says what to do, with its reason and its map address.** Bare prohibitions perform badly and raise the salience of what they forbid, so a rule that forbids names the required alternative instead. The address is *name (id)*, so a rule can be traced to its explanation and survives the node being renamed.

- **Every absolute carries an escape clause.** An unconditional "always" invites fabricated compliance; each rule that admits no exception ends by saying to stop and ask instead.

- **Favour rules that leave a trace.** The one rule that never slipped is the one whose compliance is visible in the agent's message — the character count. Rules whose observance produces something the user would notice missing are preferred over rules satisfied by silence, and this is a map principle, not a rendering trick.

- **The map gains a node for the rendering**, stating that it is derived, that the map wins on disagreement, and when the agent re-reads it. The re-read rule belongs in the map for the same reason as the rest: a rule living only in the rendering would have no source.

- **A rule that fails the test is a question about the rule.** Each one is then adapted until it is concrete enough to carry, or cut from the map as unenforceable — leaving it in place, unrendered, is the third option and needs a reason.

### Unresolved

*(empty)*

## Topics

- **Selection** — walk the map and settle each rule as carried, adapted, cut, or deliberately left unrendered, reporting the running count. The pass is also the test of the bar itself.

- **The rendering** — its shape, name (`ndd/AGENT-RULES.md`, agreed), the orientation that survives from `BOOTSTRAP.md`, and the installer change that follows the rename.

- **The map node** — the rendering described as derived, with re-reading and the falsifiability test attached; plus observability promoted as a principle, and *name (id)* restored as the addressing convention.

**Done when** the rendering holds only rules that pass the test, each stating an act with its reason and address, the map explains the arrangement without restating the imperatives, and the installer ships the renamed file.

## Log

- **Paused 2026-09-03 with the lock held.** No map or file edits have been made under this change — the map is untouched since 210 concluded. Topic 1 was mid-proposal.
- Resume at topic 1, the map's own rules, which splits into two independent items with no ordering between them:
  1. **Approval scope** — an approval covers what was surfaced; agreeing to a decision authorises drafting the prose that carries it, not writing it. Home is [Gates and Permissions](#gates-and-permissions), already 917 and over the bound before this change touched it. The open question at the pause: add the rule and leave the node at ~1049 for the 190 backlog, or split approval into its own child node (drafted at 317, leaving Gates at 724) as part of adding it. The node's own opening — "two kinds: approval and write permission" — argues for the split.
  2. **Batch boundary** — the mechanical fast path applies only when every item in hand is a correction that changes no meaning. Home is [Engagement Rule](#engagement-rule) at 780; the drafted wording lands it at 812, or 778 if ", a lighter confirmation otherwise" is cut from the preceding sentence as now-redundant.
- Then topics 2 and 3, untouched: the rendering itself (content, shape, name, surviving orientation) and the map node describing it as derived, with *name (id)* restored as its addressing convention.
- Topic 1 done. Approval scope landed in [Gates and Permissions](#gates-and-permissions) as one sentence rather than the node split, taking the smaller option while the node stays over the bound; the user then rewrote the opening as bullets and split the *Detail*'s two prohibitions, ending at 1005 from 917. The batch boundary landed in [Engagement Rule](#engagement-rule): the fast path now applies only if every item in hand is a meaningless correction, paid for by cutting the redundant "lighter confirmation otherwise" clause. 780 unchanged.
- Gates and Permissions is 205 over the bound and the split into an Approval child (drafted at 317, leaving 724) remains available for the 190 backlog.
- **Returned to planning 2026-09-04**, lock retained. Topic 1's map edits are built and stand. A research phase into agent instruction compliance arrived with evidence that the Approach's central move — rendering every rule that fires — is counterproductive, so the Approach is being rewritten around selection and verification. The Intent is unaffected. Findings recorded in Context.
- Plan approved 2026-09-04 after the rewrite; build resumes at the selection pass.
- Aside parked mid-build as `230-triggers-in-the-map.md`: the selection pass kept having to attach rules to whichever neighbouring rule already fired, because triggering moments are not first-class in a concept-organised map.

- **Paused 2026-09-04 with the lock held**, mid-topic-1. Approved but *not yet written* — three map edits, to be made first on resume:
  1. New **Approval** node (needs a fresh id), child of [Gates and Permissions](#gates-and-permissions), at 504: `Approval requires a clear affirmative given in response to the agent asking ("yes", "ok", "go ahead"). Silence, a tangent, or a reply that raises new questions is not approval. It only covers what was surfaced and no more: agreeing to draft prose is not approval of the prose.` / `How a draft is delivered is the user's choice — described in chat, or written into the file to be read in place. Delivery is never approval: however it arrives, the draft stands provisional until the user accepts or amends it.`
  2. [Gates and Permissions](#gates-and-permissions) loses that approval paragraph and gains a child link, falling 1005 to 724. Tree overview and Contents need the new node too.
  3. [Engagement Rule](#engagement-rule) drops "check the prose against Writing Style" from the edit order — it named no honest moment and sent the agent to another document mid-task. 778 to 732. Prose style keeps its real trigger in [Judgement Scan](#judgement-scan), which already lists it; nothing to add there.
- The second delivery rule came from a live observation: "write it and I'll review in situ" is a legitimate mode the old text had no room for, so the general rule is that delivery is never approval.
- **Selection pass settled at 17 imperatives**, all approved in principle: startup scan (with the bootstrap condition folded in), take the lock, project writes need an active change, no git writes, approval and its scope, the map-edit order, the whole-batch rule for meaningless corrections, count-and-report on node edits, describe only what exists, surface plan parts one at a time, count against the Intent/Approach/Conclude caps, follow the plan and log the unexpected, empty Held before Conclude, archive and release the lock and offer the maintenance checks, the two keywords, orient-then-focus for any set of points, and the typography rules inlined from [Formatting](#formatting).
- Deliberately unrendered, reachable by address: [Judgement Scan](#judgement-scan), [Consistency Upkeep](#consistency-upkeep), [Map Maintenance](#map-maintenance), [Bootstrapping](#bootstrapping), and the judgement half of the writing guide ([Conceptual Writing](#conceptual-writing)).
- Still to do after those edits: write `ndd/AGENT-RULES.md` itself from the 17, add the map node describing the rendering (derived, map wins, when it is re-read, falsifiability applies to it), promote observability to a principle, restore *name (id)* as the addressing convention, and update `opt-in.py` (`METHOD_FILES`, `CLAUDE_POINTER`, `AGENTS_INSTRUCTION`) for the rename from `BOOTSTRAP.md`.
- The three edits above were written on 2026-09-04 before the pause, exactly as approved: [Approval](#approval) created (`k4d`, 504), [Gates and Permissions](#gates-and-permissions) down to 722, [Engagement Rule](#engagement-rule) to 739. Tree overview updated.
