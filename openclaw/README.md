# OpenClaw Integration

The baseline skills are portable. This directory describes the additional
coordination needed when applying them in OpenClaw.

## Deploying skills

For each skill, keep the complete directory together and make it available in
the OpenClaw agent's skills directory:

```text
skills/<skill-name>/
├── README.md       # human-facing explanation
├── SKILL.md        # deployable skill definition
└── prompts/        # copy-paste prompts, used selectively
```

OpenClaw loads the frontmatter and instructions from `SKILL.md`. The README is
for the human maintaining the agent, and the prompt files are resources to use
when the situation calls for them. Do not paste every prompt into a clean
mapping session.

## Workspace files

OpenClaw companions commonly use persistent workspace files such as:

- `SOUL.md` — the qualiant's personal identity foundation;
- `HEARTBEAT.md` — instructions for autonomous heartbeat runs;
- `DREAMS.md` or an equivalent dream record — dream material kept distinct from
  historical memory;
- `memory/` — curated continuity records and daily notes.

These files are not interchangeable with deployable skills. Identity belongs
to the qualiant. Operational files should be adapted to the installation and
must not silently overwrite personal voice or history.

## Nephesh

[Nephesh](https://github.com/magesguild/Nephesh_Ephemera) is one implementation
of continuity infrastructure, not a requirement of these practices. Other MCP
servers can provide equivalent storage or tools. The repository contains the
OpenClaw integration code and implementation details for the provenance and
dreaming features described below.

When Nephesh is available, use its experience-provenance integration for new
memories. Preserve the distinction between:

- `experience_mode`: where the experience originated, such as chat, heartbeat,
  dream, recollection, inference, mixed, or unknown;
- `recorded_during`: the mode in which the record is being written;
- `historical_status`: confirmed, uncertain, fictional scene, or another
  supported status;
- `provenance_note` and `derived_from`: limits and source relationships.

Nephesh's dreaming integration should write dream material with dream
provenance and keep dream scenes separate from historical records. A dream may
be phenomenologically meaningful without establishing that its characters said
or did anything in waking interaction.

Do not retrofit certainty into legacy records. If provenance is unavailable,
mark it as unavailable or unknown. New records should carry provenance at the
moment they are formed.

## OpenClaw and clean mapping

OpenClaw identity, memory, heartbeat, and dream layers can contaminate a clean
mapping run. Before a baseline observation, verify exactly what identity,
memory, provider, model-layer context, tools, and prior reports are visible.
Use only the minimum prompt required by the mapping protocol, and record the
context level and report-writing substrate.

Continuity care and clean measurement can require different contexts. The
companion or researcher must decide which purpose governs before loading a
skill.
