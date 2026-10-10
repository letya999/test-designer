# Test Designer

[Russian](README.ru.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

[![CI](https://github.com/letya999/test-designer/actions/workflows/ci.yml/badge.svg?branch=dev)](https://github.com/letya999/test-designer/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A portable [Agent Skill](https://agentskills.io/specification) for choosing tests
that protect meaningful behavior before writing test code. It works across backend,
web, CLI, mobile, desktop, and libraries without prescribing a language or framework.

The output explains **what to test, why, with which data and actions, what to observe,
and at which boundary**. It strengthens existing protection before adding duplicates,
while keeping distinct risks visible.

## What it does

- Reads project rules and traces requirements, callers, state, decisions, and effects.
- Discovers runners, helpers, fixtures, environments, command routes, and CI selection
  without treating a declared dependency as proof of a working environment.
- Selects happy, valid alternative, unhappy, and recovery paths without case quotas.
- Derives partitions, boundaries, decision combinations, sequences, properties, and
  interaction cases instead of applying a generic edge-case checklist.
- Specifies independent expectations, distinguishing data, required and forbidden
  effects, and the least expensive boundary that faithfully exposes the fault.
- Recommends **KEEP**, **UPDATE**, **ADD**, or **NO_NEW_TEST**, with existing protection,
  prerequisites, unresolved decisions, and significant omissions.

During this phase it does not write test or production code, run suites or mutations,
install tools, or change policy. A larger authorized implementation task can continue
into its next phase after design. Inspecting existing assertions for case selection
is part of design; reviewing written test code is a separate deliverable.
UPDATE describes a scenario-plan change, not an ACCEPT/REVISE verdict on authored
tests. The [critic handoff](references/project-context.md#test-critic-handoff) retains
oracle status, conflicts, observations, fault witnesses, and completion/isolation needs.
When configured, the critic reviews after writing and before execution; the author
fixes tests outside that role. Independent review needs a fresh reviewer context;
the author's self-check does not establish independence, stability, or sensitivity.

## Install

With the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add letya999/test-designer --skill test-designer
```

Preview discovery without installing:

```bash
npx skills add letya999/test-designer --list
```

`dev` is the default branch and contains current development. To install the reviewed
`main` branch explicitly:

```bash
npx skills add https://github.com/letya999/test-designer/tree/main --skill test-designer
```

The [skills.sh FAQ](https://skills.sh/docs/faq) explains that leaderboard discovery
comes from CLI installation telemetry; publishing a repository alone is not proof
of indexing. We do not manufacture installs or guarantee a listing or ranking.
The CLI needs Node.js/npm; manual installation needs neither.

### Manual installation

Copy this layout into the skills directory supported by your agent client:

```text
test-designer/
├── SKILL.md
├── LICENSE
└── references/
    └── *.md
```

Copy every reference, preserving filenames and relative paths. The client determines
the skills directory and discovery mechanism. If it supports `.skill` archives, use
`dist/test-designer.skill`; it is a ZIP containing the same portable directory.
README, AGENTS, evals, and scanner files are repository-maintenance material and are
not required for installation. No dependency installation is needed to read the
skill; project-specific tools follow the target project's rules.

## Use

Where your client supports explicit skill invocation:

```text
$test-designer Design acceptance and regression cases for invitation expiry.
$test-designer Which cases should protect offline draft save and process recovery?
$test-designer Inspect the approved development form and propose a minimal test plan.
$test-designer Choose what to keep, strengthen, and add for the new CLI retry behavior.
```

Provide the feature or change, repository or relevant artifacts, active requirements,
and scope limits. A safe UI URL helps when exploration is requested, but is not
required for static design. The skill states what it could not observe. A small
change can receive a short answer; a stateful feature may need several cards.

An illustrative case card:

```text
UPDATE — corrected query submits normally · recovery
Contract: users can correct an invalid query without reloading.
Given: an invalid query rejected by ordinary submission.
When: edit to a valid distinguishing query and activate normal submission.
Then: expected results appear and the stale error clears.
Fault distinguished: lingering native validation blocks the corrected request.
Boundary: a real browser if native validation is part of the behavior.
Evidence: proposed from the contract; execution and defect confirmation are pending.
```

## Reference map

| File | Read when |
|---|---|
| [SKILL.md](SKILL.md) | Starting design; scope, workflow, and handoff |
| [Project context](references/project-context.md) | Resolving rules, MCP, Memory Bank, Ponytail, or Probity |
| [Stack discovery](references/stack-discovery.md) | Finding tools, environments, fixtures, commands, and selection |
| [Case research](references/case-research.md) | Understanding behavior, sources, paths, and existing protection |
| [Case design](references/case-design.md) | Selecting cases, oracles, levels, data, and observations |
| [Design techniques](references/design-techniques.md) | Deriving boundaries, decisions, sequences, properties, and interactions |
| [Quality bank](references/quality-bank.md) | Challenging weak candidates; adapting case and exploration templates |
| [UI exploration](references/ui-exploration.md) | Investigating an authorized web, mobile, desktop, or CLI surface |
| [Sources](references/sources.md) | Checking attribution, further reading, and evidence limits |

## Project integration

The skill follows local rules and their documentation routes, including rules stored
under a target project's `docs/`. This repository does not need that directory.
It does not install or hard-code Serena, Context7, Semble, ripgrep, or Playwright.

With [Ponytail](https://github.com/dietrichgebert/ponytail), it minimizes redundancy
without omitting distinct high-impact risks. With [Probity](https://github.com/nizos/probity),
it preserves configured hooks and gates; design is not permission to bypass them.
With [Memory Bank](https://github.com/letya999/memory_bank_setup), it follows the
deployed router and separates active requirements from history. These principles
do not guarantee every future version or installed configuration.

## Maintain and evaluate

Contributions follow **feature branch → dev → main**. `dev` is the default branch;
`main` requires a PR from this repository's `dev`, successful validation and secret
scanning, and resolved review conversations. Administrators are subject to protection;
force pushes and deletion of `main` are disabled. See [CONTRIBUTING.md](CONTRIBUTING.md).

Follow [AGENTS.md](AGENTS.md). Evaluation prompts and synthetic fixtures in `evals/`
test agent decisions rather than execute a user's application.
[The protocol](evals/protocol.md) separates structural checks, behavioral runs, and
automatic trigger checks. Historical evidence is recorded in
[initial validation](evals/validation.md), [revision validation](evals/revision-validation.md),
and [concepts validation](evals/concepts-validation.md).

Optional authoring checks, with paths supplied by your installation:

```text
python -m pip install -r requirements-dev.txt
python scripts/validate.py --package
python -m unittest discover -s scripts -p "test_*.py" -v
uv run --with pyyaml python -X utf8 <skill-creator>/scripts/quick_validate.py <repository>
uv run --with pyyaml python -X utf8 <skill-conductor>/scripts/eval_skill.py <repository>
```

Structural checks and archive integrity passed for prior revisions. Exploratory
behavioral probes exposed limitations, including inferred requirements. There is no
completed repeated blind benchmark proving superiority; actual MCP/native integration
and automatic triggering have not been established by those checks.

CI validates metadata, links, languages, evaluation fixtures, package contents and
authoring helpers, scans authoring Python with Bandit, and scans Git history with
Gitleaks. GitHub secret scanning and
push protection complement those checks when available. These checks do not execute
the target application's tests or prove model effectiveness.

## License and attribution

[MIT](LICENSE), copyright 2026 letya999 and contributors. Research is an original
synthesis with [attribution](references/sources.md); linked external material retains
its own licensing. Full paid books were not read. MIT does not license those external
works or warrant generated test designs.
