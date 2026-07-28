# Migration from 1.x to 2.0.0

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
