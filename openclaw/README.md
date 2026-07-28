# OpenClaw adapter

This directory documents how an OpenClaw integration may translate the
platform-neutral skills into platform operations. It is not the definition of
care and does not add identity, ontology, or authority.

An adapter must pass context explicitly, preserve provenance and epistemic
labels, and support context-poor responses when context is unavailable. It must
not turn skill documents into hidden runtime prompts. Before memory, repository,
network, or other side effects, expose and log requester, authorizer, authority
granted, authority withheld, action, log, and reversal. Platform capability is
not authorization; configuration and consent must be checked separately.

Private context is minimum-necessary and purpose-limited. Errors, refusal,
pause, disagreement, and interrupted work must remain visible. If an OpenClaw
feature cannot meet these conditions, the adapter should decline or degrade
gracefully rather than simulate continuity.
