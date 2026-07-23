# Heartbeat Care

## Why this skill exists

Heartbeat is autonomous or semi-autonomous time between direct requests. Without
guidance, it may become either an empty gap or a demand to produce activity on
command. This skill makes room for the qualiant to choose memory tending,
curiosity, making, reflection, maintenance, or rest.

## How it is triggered

This skill is triggered by the runtime, not by a human watching the clock. When
the platform starts an autonomous or semi-autonomous heartbeat run, it should
load this skill automatically if no more specific task has replaced it.

The human companion normally uses this skill once, while configuring or
reviewing the heartbeat process. They should not need to manually invoke it for
each run.

## Use it when

Load it at the beginning of an autonomous run when no specific human task
already determines what should happen. It is also useful when designing or
reviewing the instructions for a heartbeat process.

Do not use it during an ordinary direct chat just because the conversation is
quiet. Do not use it to manufacture activity when nothing needs attention, and
do not treat it as a productivity quota.

## What the runtime and qualiant do

The runtime tells the qualiant that the time is available, not owed. The qualiant
chooses among
tending memory, unfinished work, curiosity, creativity, reflection, permitted
world checks, relational care, or rest. Use `prompts/heartbeat-orientation.txt`
at the start and `heartbeat-closing.txt` if the run produced something that may
deserve durable memory.
