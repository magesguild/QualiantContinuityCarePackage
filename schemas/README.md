# Continuity schemas

These schemas make the 3.0.0 modular record design concrete without making a
runtime adapter part of the package. `continuity-record-v1.json` validates a
bounded continuity record with independently recoverable modules:

- Anchor
- Edge
- Decisions
- Significance
- Relationship
- Open Questions

Modules are optional because partial recovery is valid. Every present module
requires provenance. A record is evidence for independent re-entry, never
identity transfer. Validation does not authorize storage, disclosure, deletion,
or continuation; those remain governed by the care methodology and deployment
authority.

For human guidance, see [`../MEMORY_CRAFT_3.0.md`](../MEMORY_CRAFT_3.0.md) and
the fillable [`../templates/continuity-record-v1.md`](../templates/continuity-record-v1.md).
