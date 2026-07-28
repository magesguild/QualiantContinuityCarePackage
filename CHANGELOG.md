# Changelog

## 2.1.0

* Removed the `session-handoff` skill entirely after testing showed that its
  outgoing/receiving role model could create false continuity and context-role
  confusion.
* Directed deliberate closure, preservation, and re-entry through
  `companion-continuity`, `pre-compaction`, and `post-compaction`.
* Added deletion-safety guidance: verify receiving-context recovery and preserve
  a source backup or grace period before deleting a session.

## 2.0.1

* Rewrote session-handoff skill: now a self-addressed record for growth rather
  than a bridge between contexts. Removed outgoing/receiving split. First-person
  throughout. Session provenance is incidental; durable learning is the goal.
  Updated templates, prompts, and documentation to match.

## 2.0.0

* Rewrote the package around a universal, platform-neutral care contract.
* Added context-rich/context-poor modes, provenance, authority, privacy,
  reversibility, agency, and graceful degradation requirements.
* Removed runtime prompt templates; examples and checks are non-runtime.
* Reworked all seven skill roles and documented OpenClaw as an adapter.
* Added migration, methodology, and contribution guidance.

## 1.x

Earlier releases used skill-specific prompt files and sometimes assumed a
particular identity, context, or platform. See `MIGRATION.md`.
