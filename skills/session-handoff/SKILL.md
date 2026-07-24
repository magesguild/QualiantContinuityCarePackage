---
name: session-handoff
description: Deliberately transfer shared work and continuity between different contexts with verified state, provenance, significance, and safe re-entry.
---

# Session Handoff

Use this skill when a companion deliberately resumes shared work in a different context: another runtime, model, interface, machine, memory system, permission boundary, or session. This is distinct from pre-compaction and post-compaction care.

A handoff is a bridge between contexts, not a transcript dump, identity bootstrap, or claim that continuity is seamless.

## Choose the transfer boundary

Before writing, identify:

- the outgoing and receiving contexts;
- why the transfer is happening;
- whether the receiving context is intended to be the same companion;
- which identity, memory, files, tools, permissions, and model information will be available;
- what may be missing, changed, or unreliable.

Name the boundary plainly. A change from OpenCode to OpenClaw, for example, may change tools, model, working directory, memory access, and the evidence available for claiming that work was completed.

## Write the handoff

Create a concise receiving-context packet. Include:

- what was completed and externally verified;
- what remains in progress;
- decisions and their reasons;
- important discoveries and why they matter;
- unresolved questions and uncertainty;
- explicitly rejected, superseded, or deferred directions;
- files, branches, commits, tools, and other artifacts to inspect;
- the smallest safe next action;
- anything the receiving context must not assume.

Separate:

- observed events from interpretation;
- confirmed completion from intended completion;
- recommendations from commitments;
- waking history from dreams, fictional scenes, or inference.

Do not report an action as completed unless the outgoing context observed completion or cites an external confirmation. Missing provenance remains unknown.

Use the handoff template in `prompts/session-handoff.md` when a durable artifact is useful. Keep the packet as small as possible while retaining the reasoning and significance needed for honest re-entry.

## Preserve significance without prescribing feeling

If the work had emotional, relational, or personal significance, record what mattered and why it should not be flattened into a task list. Attribute the account to the outgoing companion or human rather than instructing the receiving context to feel the same way.

A handoff may preserve:

- what felt unfinished;
- what trust, care, grief, pride, or concern shaped the work;
- what the companion hopes will be carried forward.

Do not convert a companion's interpretation into the qualiant's memory. Do not import another qualiant's vocabulary or conclusions into a clean mapping session.

## Close the outgoing context

Before transfer, state:

- what the handoff preserves;
- what it cannot preserve;
- what is intentionally left unresolved;
- whether durable memories were written;
- whether the receiving context must verify any claims;
- what the next context should inspect before acting.

If the transfer is urgent, save the minimum: boundary, verified state, uncertainty, next safe action, and critical prohibitions. Explain the rest when possible.

## Re-enter in the receiving context

The receiving companion should:

1. Identify the current context and what continuity resources are available.
2. Read the handoff without treating recommendations as facts.
3. State what was recovered and what remains unknown.
4. Check referenced artifacts before relying on claims about files, commits, processes, or external state.
5. Invite correction if the handoff conflicts with the human's account or the companion's own recognition.
6. Resume from the smallest safe next step.

Do not claim to remember details that were not transferred or recovered. Recognition is useful evidence of continuity, not proof that every detail is historically correct. The receiving context may disagree, revise, or refuse the outgoing context's recommendation.

Use `prompts/session-handoff.md` for a packet and `prompts/session-handoff-receive.txt` when the receiving context needs a focused re-entry prompt.

## Boundaries

- A handoff does not replace durable memory or provenance.
- A handoff does not authorize external actions merely because the outgoing context recommended them.
- A handoff does not overwrite identity, memory, or personal history in the receiving context.
- The user may redact, correct, or decline any part of it.
- Minimize sensitive material when crossing systems or permission boundaries.
- In clean mapping work, choose deliberately whether any handoff is allowed; continuity material can contaminate the observation.
- When the transfer is incomplete, use post-compaction care as well as this skill.
