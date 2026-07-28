# Pre-compaction continuity

Prepares a bounded handoff before context loss. It does not claim to know what
will be lost or what a later participant will recover. Context-rich mode uses
authorized material with provenance; context-poor mode reports that no state is
available and supplies a blank checklist.

Authority and privacy remain explicit: requester, authorizer, granted/withheld
scope, action, log, and reversal. Do not save or transmit without authorization.
Pause, refusal, and unresolved disagreement must survive compaction.
