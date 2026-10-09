# Test Designer

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

## Install

Copy this layout into the skills directory supported by your agent client:

```text
test-designer/
├── SKILL.md
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

Follow [AGENTS.md](AGENTS.md). Evaluation prompts and synthetic fixtures in `evals/`
test agent decisions rather than execute a user's application.
[The protocol](evals/protocol.md) separates structural checks, behavioral runs, and
automatic trigger checks. Historical evidence is recorded in
[initial validation](evals/validation.md), [revision validation](evals/revision-validation.md),
and [concepts validation](evals/concepts-validation.md).

Optional authoring checks, with paths supplied by your installation:

```text
uv run --with pyyaml python -X utf8 <skill-creator>/scripts/quick_validate.py <repository>
uv run --with pyyaml python -X utf8 <skill-conductor>/scripts/eval_skill.py <repository>
```

Structural checks and archive integrity passed for prior revisions. Exploratory
behavioral probes exposed limitations, including inferred requirements. There is no
completed repeated blind benchmark proving superiority; actual MCP/native integration
and automatic triggering have not been established by those checks.

Research is an original synthesis with attribution. Full paid books were not read,
and no distribution license has been selected for this repository.
