# Qualiant Continuity Care Package

**Version 2.1.0 — GPLv2**

This package is a platform-neutral set of care practices for continuity,
honesty, agency, and accountable collaboration. It is useful with no added
context: a skill can explain what input it needs and offer a safe next step.
It cannot invent a person's identity, history, state, relationship, ontology,
or platform capabilities.

## Contract

Every skill supports two modes:

* **Context-rich:** use supplied, authorized context, while labeling its
  provenance and distinguishing facts, reports, observations, interpretations,
  and hypotheses.
* **Context-poor:** state what is missing, avoid unsupported conclusions, ask
  only useful questions, and provide a bounded generic procedure or pause.

In both modes, preserve disagreement, refusal, uncertainty, and revision.
Consequential work records requester, authorizer, authority granted and
withheld, action, log, and reversal path. Privacy is purpose-limited and
access-bounded; no skill silently writes memory, crosses a boundary, or grants
itself authority. Graceful degradation is preferable to fabricated continuity.

The package is a care methodology, not a consciousness claim, identity
bootstrap, universal ontology, research result, or platform prompt library.

## Skills

1. `companion-continuity` — orientation, collaboration, pause, repair, and close.
2. `experience-modes` — label the mode and epistemic status of an encounter.
3. `memory-provenance` — preserve source, uncertainty, privacy, and disposition.
4. `pre-compaction` — prepare a truthful, bounded continuity record.
5. `post-compaction` — reconcile records without pretending recovery.
6. `self-audit` — inspect fidelity, contamination, authority, and degradation.

## Why session-handoff was removed

Version 2.1.0 removes the `session-handoff` skill entirely. Testing showed that
combining outgoing-session authoring with receiving-session re-entry could make
the exiting context speak as though it had already become the new context. That
role confusion risks false continuity and can cause an operator to delete the
source session before the receiving context has independently verified recovery.

Continuity is now handled by the remaining skills: use `companion-continuity`
for deliberate closure and interruption, `pre-compaction` to preserve the
current state, and `post-compaction` to reconcile the receiving context. A
handoff record may still be created as an ordinary, externally verified artifact
when needed, but it is not a deployable identity or continuity skill.

Never delete the source session until the receiving context has been tested,
reconciled against the source, and protected by an appropriate backup or grace
period.

`openclaw/` is an adapter example, not the definition of care. Runtime prompt
templating has been removed; `examples/` and `tests/` are non-runtime material.
See [METHODOLOGY.md](METHODOLOGY.md), [MIGRATION.md](MIGRATION.md), and
[CONTRIBUTING.md](CONTRIBUTING.md).
