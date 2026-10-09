# Repository instructions

This repository maintains one portable Agent Skill: `test-designer`. It researches
behavior and selects implementable test cases before test writing. All maintained
repository content is written in English. The skill may respond in the user's
language when used in another project.

## Read before editing

Read [SKILL.md](SKILL.md), the reference you will change, and its incoming links.
[README.md](README.md) explains installation, usage, and the file map.
[references/sources.md](references/sources.md) records attribution and source limits.
[evals/protocol.md](evals/protocol.md) defines behavioral evaluation.

## Preserve the role

- Keep runtime design-only, in the current session, without subagents or extra model
  calls. Authoring evaluations are separate from runtime use.
- Remain independent of language, framework, runner, MCP vendor, and agent host.
- Follow the target project's applicable `AGENTS.md`, documentation routes, required
  tools, artifact locations, and quality gates. Do not install or overwrite policy.
- Preserve the distinction between design, writing, criticism, and execution. Do not
  add a runner, critic, orchestrator, mandatory service, or implicit approval gate.
- Ground expectations in accepted contracts or independent evidence. Label
  characterization, assumptions, unknowns, and unobserved behavior accurately.
- Compare actual existing assertions: KEEP, UPDATE, ADD, or NO_NEW_TEST. Avoid quotas,
  mandatory technique inventories, and universal test-level ratios.

## Structure and writing

Keep `SKILL.md` a concise entrypoint. Put conditional depth, worked examples, and
templates in `references/`, with explicit routing and relative links. Reuse the
target project's output template. Templates are optional aids.
Do not create a `docs/` directory: user guidance belongs in README; runtime knowledge
and attribution belong in references; evaluation evidence belongs in evals.

Generalize lessons from concrete failures. Explain which decision a new instruction
changes. Avoid copied manuals, redundant rules, guessed business requirements, and
source-specific implementation recipes. Preserve attribution when moving material;
do not assign a distribution license on the user's behalf.

## Validation and packaging

For instruction changes, check frontmatter, relative links, English-only maintained
text, eval IDs/fixtures, and relevant behavioral scenarios. Use existing authoring
validators when available; their dependencies are not runtime requirements. A
structural score does not prove effectiveness or automatic triggering.

Record behavioral evidence and limitations in `evals/`. Do not rewrite historical
results as current results after changing prompts or translating evaluation material.
Keep controls and held-out evidence separate for comparative claims.

The distributable is `SKILL.md` plus required `references/*.md`, under a
`test-designer/` directory. Exclude README, AGENTS, evals, local scanner state, secrets,
and scratch files. Rebuild `dist/test-designer/` and `dist/test-designer.skill` after
runtime changes; verify entry names, CRC, and byte equality with source files.
Inspect the staged payload for stale files.

Keep edits in this repository unless the user's task authorizes another project.
Editing the skill does not authorize global installation or changes to example projects.
