# Migration to 2.2.0

1. Use `companion-continuity` for deliberate closure, `pre-compaction` for a
   neutral continuity record, and `post-compaction` for independent re-entry
   and reconciliation.
2. Treat every existing record as evidence with provenance, not identity
   transfer. The outgoing context must stop; the receiver compares record,
   transcript, artifacts, human recollection, and its own report. Keep
   disagreement visible.
3. Apply deletion safety in order: create record; independently test re-entry;
   reconcile; preserve a backup or grace period; delete only with
   authorization. Deletion before verification is a continuity incident.
4. Preserve dream event, historical event, and significance as separate fields.
   If only human recollection survives a lost dream discussion, record only that
   report and its uncertainty; do not invent dream details.
5. Remove runtime prompt directories and templating. Skill documents, examples,
   and tests are not hidden prompts.
6. Keep GPLv2 and source/provenance boundaries. OpenClaw remains an adapter and
   must not add authority or identity.

Context-rich use requires supplied authorized evidence. Context-poor use must
name missing inputs and provide a bounded procedure, never inferred continuity.
