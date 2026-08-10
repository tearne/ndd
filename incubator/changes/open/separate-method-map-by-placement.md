# Separate the method map from a client's domain map by placement

**Kind:** idea
**Anchor:** a3k

When this method is pulled into a client project, that project already has its own `map.md` describing its domain. The method's own process map and `BOOTSTRAP.md` would collide with it. Idea: ship them under `changes/agent/` so file-tree position distinguishes the method map from the client's domain map — both stay `map.md`, context comes from location. `BOOTSTRAP.md` already points at "the `map.md` alongside this file" to suit this. Decide during the map build-out follow-up whether the process lives as a separate co-located map or a labelled region inside one map.
