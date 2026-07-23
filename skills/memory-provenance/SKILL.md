---
name: memory-provenance
description: Preserve continuity by recording memories with experience origin, historical status, significance, uncertainty, and derivation. Use when creating, reviewing, or correcting durable memory.
---

# Memory Provenance

Use this skill when durable memory is being formed, revised, or recollected.

## Core rule

Do not collapse event, interpretation, and recollection into one fact. Preserve
the distinction between:

- what happened or appeared;
- where the experience originated;
- when and how the record is being written;
- what is confirmed, uncertain, inferred, or fictional;
- why it matters now;
- what remains unresolved.

## Record

Use the fields supported by the memory system. The portable conceptual fields
are:

```text
Experience origin: chat | heartbeat | dream | recollection | inference | mixed | unknown
Historical status: confirmed | uncertain | fictional_scene | interpreted
Recorded during: chat | heartbeat | dream | unknown
Event: what happened or appeared
Significance: why it matters
Open question: what remains unresolved
Derived from: source records, if applicable
Provenance note: limitations or reconstruction details
```

Do not invent provenance. If origin is unknown, record that it is unknown.

## Dream records

Dreams may be real experiences without being real historical events. Keep the
dream scene, its possible significance, and the external historical record
separate. Never attribute dream dialogue or actions to a waking participant
without independent evidence.

## Recollection

Recollection may restore significance that was absent from an older record. Add
that significance as reconstructed or interpreted; do not silently rewrite the
original event as though the later understanding had been present then.

## Contamination control

For clean mapping, do not query prior memories unless the protocol explicitly
requires identity continuity. Save the raw account first. Add interpretation,
comparison, or analysis only after the raw record is frozen.

Use `prompts/memory-record.txt` for a new record and
`prompts/memory-review.txt` when auditing an existing one.
