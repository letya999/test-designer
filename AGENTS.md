# Repository instructions

This repository maintains one portable Agent Skill: `test-designer`. It researches
behavior and selects implementable test cases before test writing. All maintained
repository content is written in English except `README.ru.md`, the requested Russian
translation. Keep its installation, scope, and branch guidance aligned with README.
The skill may respond in the user's
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
- UPDATE means a scenario-plan change, not an ACCEPT/REVISE test-code verdict. Preserve
  oracle status, unresolved conflicts, observation/completion/isolation needs at handoff.
  Keep independent fresh-context review distinct from author self-review; corrections
  belong to the author outside the critic role. Never certify stability from design.

## Structure and writing

Keep `SKILL.md` a concise entrypoint. Put conditional depth, worked examples, and
templates in `references/`, with explicit routing and relative links. Reuse the
target project's output template. Templates are optional aids.
Do not create a `docs/` directory: user guidance belongs in README; runtime knowledge
and attribution belong in references; evaluation evidence belongs in evals.

Generalize lessons from concrete failures. Explain which decision a new instruction
changes. Avoid copied manuals, redundant rules, guessed business requirements, and
source-specific implementation recipes. Preserve attribution when moving material;
preserve the chosen MIT license and keep third-party source attribution accurate.

## Validation and packaging

For instruction changes, check frontmatter, relative links, English-only maintained
text, eval IDs/fixtures, and relevant behavioral scenarios. Use existing authoring
validators when available; their dependencies are not runtime requirements. A
structural score does not prove effectiveness or automatic triggering.

Record behavioral evidence and limitations in `evals/`. Do not rewrite historical
results as current results after changing prompts or translating evaluation material.
Keep controls and held-out evidence separate for comparative claims.

The distributable is `SKILL.md`, `LICENSE`, and required `references/*.md`, under a
`test-designer/` directory. Exclude README, AGENTS, evals, local scanner state, secrets,
and scratch files. Rebuild `dist/test-designer/` and `dist/test-designer.skill` after
runtime changes; verify entry names, CRC, and byte equality with source files.
Inspect the staged payload for stale files.

Run `python scripts/validate.py --package` and
`python -m unittest discover -s scripts -p "test_*.py" -v` for authoring changes.
Install authoring-only dependencies from `requirements-dev.txt` in an isolated
environment. These scripts validate this repository; they are not application test
execution and are not called by the runtime designer. Preserve CI's read-only
permissions except the trusted promotion workflow's narrowly scoped status write.

## Collaboration and publication

Work from `dev`, the default branch. Contributions use `feature/*` or `fix/*` branches
and PRs into `dev`. Promote `dev` to protected `main` through a PR from this repository's
`dev` only; do not push directly to `main`, force-push protected history, disable
checks, or bypass branch policy. See [CONTRIBUTING.md](CONTRIBUTING.md).
Preserve the long-lived `dev` branch when merging; merge release PRs with ancestry
intact so future promotions do not repeatedly include old commits.

Before public writes inspect the exact staged/tracked payload and scan it for secrets.
Local `.repo-safety/`, scratch state, downloaded tools, and credentials remain ignored.
Follow [SECURITY.md](SECURITY.md) for private vulnerability disclosure. Do not turn
structural CI results into claims of proven model quality or security.

Keep the public `SKILL.md` discoverable at repository root. Do not add fabricated
skills.sh install counts or claim catalog indexing before it is observed. Publication
and global installation require user task authorization; a README example grants neither.

Keep edits in this repository unless the user's task authorizes another project.
Editing the skill does not authorize global installation or changes to example projects.
