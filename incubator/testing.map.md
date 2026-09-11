# Fingerprint Check

[↑ Testing](map.md#testing)
[Contents](#contents)

```yaml
id: c5m
```

Every agent must produce the same fingerprint for the same node text, or approval stamps cannot be compared. `tests/fingerprint_test.py` is the reference implementation of the [Fingerprint](ndd.map.md#fingerprint) rule, standard library only and short enough to read whole, run against two fixtures beside it: `fixture.map.md`, a small map exercising every node section, and `fixture-edited.map.md`, the same map after edits that must not move a fingerprint and two that must. It passes when every node's fingerprint is the one tabled in *Detail*. An agent about to trust any other implementation, its own included, runs that implementation over the fixtures and compares with the table.

**Detail**

| Node | Original | Edited | Edit made |
|---|---|---|---|
| Fixture | ab9e6f02 | 5fd5a260 | prose changed |
| Plain Prose | bcf6b47b | bcf6b47b | paragraph re-wrapped and indented |
| Full Sections | 3a096aaf | 3a096aaf | child link renamed |
| Child, then Renamed Child | 250ae92a | 103b2b33 | heading renamed |
| Bare Heading | 6bcce17f | 6bcce17f | scaffolding block and stamp added |
| Changed Prose | 275d67bd | 618c09de | one word added |


# Contents

[↑ Fingerprint Check](#fingerprint-check)

```yaml
id: ct7
```

- [Fingerprint Check](#fingerprint-check)
