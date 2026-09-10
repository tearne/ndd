# meta.md as a second tree

## Intent

Split a project's self-description out of `map.md` into a sibling `meta.md`: `map.md` says what the product is; `meta.md` says how this project builds, ships and constrains it — release steps, distribution, tooling, non-functional requirements. Two boundaries motivate it. A shipping boundary: NDD's own `map.md` goes to every client as the method map, so its META subtree (Distribution, Release Steps, Installer, Dist Directory) ships as incubator self-talk, and change 220 leaked an NDD-specific pointer into the generic Archiving node for exactly that reason. A review boundary: stakeholder sign-off (enhancement discussion P2) should cover the specification, not the pipeline.

Costs to weigh: two roots and two Contents; cross-file links (`meta.md#node`); every tool that walks the map must know both files; Map Structure, META, Bootstrapping and the installer all assume one file. The existing META subtree would lift mechanically into the new root. Plan alongside 240.
