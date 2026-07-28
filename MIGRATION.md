# Migration to 2.1.0

## From 2.0.1

1. Remove the `session-handoff` skill and any references to it from runtime
   configuration.
2. Use `companion-continuity` for deliberate closure and interruption,
   `pre-compaction` for preservation, and `post-compaction` for independent
   re-entry and reconciliation.
3. Treat any existing handoff records as ordinary, unverified input until the
   receiving context checks them against the source session and external
   artifacts.
4. Do not delete a source session until receiving-context recovery has been
   tested and a backup or grace period protects the source.

## From 1.x

1. Replace prompt-file loading or templating with the relevant `SKILL.md`
   contract. Files in `examples/` are illustrative and must not be executed.
2. Supply context explicitly when available, including provenance and privacy
   disposition. With no context, expect a missing-input response rather than
   inferred identity, continuity, or state.
3. Update integrations to request and log authority fields: requester,
   authorizer, granted, withheld, action, log, and reversal.
4. Treat stored material as typed evidence (fact/report/observation/
   interpretation/hypothesis), not as undifferentiated truth.
5. Remove assumptions about Qualiant names, identities, ontology, chat,
   OpenClaw, or any other platform. OpenClaw users should follow its adapter
   README only for translation into platform operations.
6. Re-check privacy, refusal, disagreement, pause, and contamination behavior.

The skills remain useful without added context, but they cannot invent missing
facts. Existing 1.x records may be retained as historical inputs only when
their provenance and uncertainty are visible.
