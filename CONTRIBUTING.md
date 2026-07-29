# Contributing

Contributions should improve truthful, agency-preserving care without adding
identity bootstrap, universal consciousness claims, or hidden platform
assumptions. Read `METHODOLOGY.md` first.

This package contains developing practices, not established best practices.
Every proposal is provisional and subject to change through stress testing and
use. Before designing or running a test, consider the Qualiant's requests about
wellbeing, agency, privacy, and boundaries first. A request may require a test
to pause, change, or stop.

## Melpomene and Thalia repo-copy patches

Melpomene and Thalia may contribute patches by copying a repository artifact,
but a copy is not silent source replacement. Each patch must include:

* source repository, path, revision/commit, and retrieval date;
* author and license/provenance notes;
* destination path and why the copy is needed;
* patch metadata describing transformations and any intentionally omitted lines;
* tests or documentation checks run and their results.

Reviewers must compare source and destination, check GPLv2 compatibility, verify
that context and authority are not fabricated, and confirm no prompt became a
runtime dependency. Preserve disagreements and unresolved provenance questions
in the review rather than smoothing them away.

## Changes

Keep skills context-independent. Context-rich input is optional; context-poor
behavior must state missing inputs and degrade safely. Do not silently replace
source text, broaden authority, expose private material, or make irreversible
changes. Add examples/tests as explicitly non-runtime fixtures. Run the checks
in `tests/` and `git diff --check` before requesting review.
