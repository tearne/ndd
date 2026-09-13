# Coding Style: Rust Addendum
*Applies to Rust projects only — ignore in other contexts.*

Rust-specific extensions to `STYLE.md`. The core principles apply; this addendum covers Rust's type system, ownership model, and idioms.

## 1. Module visibility as an API boundary *(extends STYLE §3)*
- Default to the most restrictive visibility — start private, widen only when needed
- Use `pub(crate)` for internal infrastructure, not public API
- Treat a module's `pub` surface as its contract; keep it minimal and stable
- No `pub` on everything to silence compiler warnings — that signals a missing abstraction boundary
- No `mod.rs` as a pass-through that re-exports everything from every submodule

## 2. Error types reflect domain, not implementation
- For libraries: define a custom error enum (e.g. `pub enum MyLibError { ... }`) with explicit variants in a dedicated `error.rs`; implement `std::error::Error` directly rather than using a derive macro
- For applications: use `color_eyre` for error aggregation and reporting
- Propagate with `?` freely — idiomatic and not an abstraction violation
- No `Box<dyn Error>` — erases information callers may need
- No single monolithic error enum spanning multiple unrelated modules
- No `unwrap()` or `expect()` in paths reachable at runtime; reserve for invariants that cannot fail by construction
- `unwrap()` is acceptable for hardcoded literal values that are obviously valid (e.g. `NaiveDate::from_ymd_opt(2016, 3, 1).unwrap()`) — the value itself is the documentation
- Prefer `expect("invariant description")` over `unwrap()` in all other cases — name the invariant, not the symptom

## 3. Ownership signals design
- Prefer owned types in structs that clearly own their data
- Use borrows (`&`, `&mut`) at function boundaries where the callee doesn't need ownership
- `Arc<Mutex<T>>` only when shared mutable ownership is genuinely required
- Widespread `clone()` calls are a code smell — investigate before accepting
- No `Arc<Mutex<T>>` to resolve borrow conflicts without first understanding why they exist
- Avoid lifetime annotations where a cheap clone or `.into()` removes the need — lifetimes add cognitive overhead and should only appear when the borrow reflects a real, meaningful constraint (e.g. a streaming reader holding a reference across calls). A single clone at a struct boundary or a `.into()` cast for a string literal is preferable to annotating an entire type with `'a`

## 4. Traits define behaviour, not convenience
- Define a trait when there are (or will be) multiple concrete implementations
- Default to generics (`impl Trait` / `fn foo<T: Trait>`) — zero-cost and keeps variant sets explicit
- `dyn Trait` only when the variant set is open — plugin systems, user-supplied callbacks, external inputs
- No trait for a concept with one implementation and no foreseeable variation
- No traits as a substitute for a module boundary
- "Chosen at runtime" is not sufficient justification for `dyn Trait` — a config-selected variant is still a closed set

## 5. Test support modules
- Group test-only exports in a single `#[cfg(test)] pub(crate) mod test_support { ... }` block per file
- Place alongside `mod tests` at the bottom of the file
- No individual `#[cfg(test)]` gates on items that need to be visible outside the file
- No test helpers mixed into the public API

## 6. Serde config conventions
- Use JSON as the config file format — not TOML, YAML, or properties files
- Write JSON keys in snake_case to match Rust field names — no `rename_all` or `rename` attributes needed on config structs
- Apply `#[serde(deny_unknown_fields)]` to all config structs — makes unrecognised keys an error rather than a silent no-op
- Use internally-tagged enums (`#[serde(tag = "...")]`) for config variants with associated parameters
- Name the tag field after the domain concept (e.g. `"model"`, `"strategy"`)
- No untagged or adjacently-tagged enums for config without specific reason

## 7. CSV reader pattern
When reading CSV input files, separate raw deserialisation from domain construction:
- Define a private `*Row` struct (e.g. `AnimalRow`) that derives `Deserialize` and mirrors the CSV columns exactly — column renaming via `#[serde(rename = "...")]` lives here
- Define a separate public domain struct (e.g. `CattleDetails`) that uses proper domain types (`LocationKey`, `TimeStep`, custom enums) — no raw `u32`/`String` primitives where a richer type exists
- Wrap `csv::Reader<File>` in a named `*Reader` struct; expose `new(path: &Path)` for construction
- Write custom serde deserialiser logic in small private submodules (`mod date_format`, `mod dam_flag`) within the same file, wired in via `#[serde(with = "...")]` on the `Row` struct — keeps the Row definition readable and the logic local

Two loading patterns depending on file size:

**Eager (`load()`)** — for small lookup tables that are needed throughout the run:
- Expose a consuming `load(...)` method that reads the whole file and returns the fully-typed collection
- Use for holdings, relationships, neighbours, abundance, seeding inputs

**Streaming (`take_day()`)** — for large chronologically-sorted files (e.g. ~300M row movement files):
- Keep the `csv::Reader` open inside the struct alongside a one-record lookahead buffer and the last-seen `TimeStep`
- Expose `take_day(&TimeStep) -> Result<Vec<Record>>` — drains all records for that timestep and buffers the next, so only one day is in memory at a time
- Use for cattle and sheep movement files

## 8. Imports
- Always import types and functions with `use` at the top of the file — do not write fully-qualified paths at call sites (e.g. `std::io::Error`, `std::process::Command`) where a `use` statement would serve
- Exception: `use std::fmt;` followed by `fmt::Formatter` / `fmt::Result` at call sites is idiomatic and preferred — importing `Result` directly would require `Result as FmtResult` to avoid a name clash with `std::result::Result`, which is more verbose and less readable

## 9. Runtime-to-static dispatch
Where a component is selected at runtime but the variant set is closed, bridge with a single startup `match`:

```rust
match config.model {
    Model::Seir => run::<SeirModel>(config),
    Model::Sir  => run::<SirModel>(config),
}
```

- Perform the dispatch `match` once at startup, outside the hot path
- No `Box<dyn Trait>` simply because selection happens at runtime
- No repeated dispatch matches — a single match at the boundary is the point
