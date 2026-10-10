---
name: test-designer
license: MIT
description: >-
  Design test cases and expected results. Use for test plans, acceptance/regression
  scenarios, boundaries, error paths or "what to test", even within implementation
  tasks. Not for writing/reviewing/running tests, infrastructure or A/B experiments.
---

# Test Designer

Investigate the behavior, choose cases worth keeping, and make each case precise
enough to implement. Minimize redundant checks, not the distinct risks protected.
Work in the current session, without subagents or additional model calls. Use the
user's language and the project's terms.

## Scope

This phase reads artifacts and explores an authorized safe UI. It produces a design;
it does not write test/production code, run tests or mutations, install tools, or
change project policy. Save the design only when requested or required by the project.
Inspect existing assertions to select cases; reviewing written test code as a
deliverable remains a separate critic/review phase. Do not issue ACCEPT/REVISE
verdicts on authored tests. KEEP/UPDATE/ADD/NO_NEW_TEST are scenario-plan decisions;
UPDATE proposes changes to that plan, not a code review or permission to edit tests.
For a larger authorized task, finish this phase and continue that task without a new
approval gate. A configured critic belongs after test writing and before execution.

## Workflow and reference map

1. **Establish the local contract.** Read applicable `AGENTS.md` and its routes to
   requirements, testing rules, and quality gates. Follow
   [project context](references/project-context.md) for tool policy, Memory Bank,
   Ponytail, Probity, and conflicting or unavailable prerequisites.
2. **Discover the test stack.** Follow [stack discovery](references/stack-discovery.md)
   for each touched package: runner, helpers, config, runtime, data/services, command
   route, and CI selection. Reuse a current verified inventory. A declared dependency
   is not proof of an available tool, usable environment, or executed check.
3. **Research the cases.** Follow [case research](references/case-research.md): map
   actor/goal → inputs/state → decisions/dependencies → outputs/effects; inspect
   callers, existing assertions, and relevant product evidence. Explore a reachable
   UI using [UI exploration](references/ui-exploration.md). Label what was not seen.
4. **Select and specify.** Use [case design](references/case-design.md) to separate
   happy, alternative, unhappy, and recovery paths; derive meaningful boundaries and
   sequences; choose discriminating data, independent expectations, and a faithful
   level. Apply only techniques the behavior needs.
   For unfamiliar rules or interacting boundaries, consult
   [design techniques](references/design-techniques.md). Use the
   [quality bank and templates](references/quality-bank.md) to challenge candidates
   and structure the handoff; these are prompts, not mandatory case inventories.

5. **Hand off.** Return the smallest implementable set with its rationale, existing
   protection, environment needs, unresolved decisions, and excluded/deferred risks.

Source attribution and further reading are in [sources](references/sources.md).
Read that reference only when provenance or deeper research is relevant.

For a small change, each step may take one sentence. Read only relevant sections;
do not create five documents or a repository-wide audit to follow five steps.

## Decisions that matter

- Ground expectations in a requirement, agreed contract, domain rule, accepted example,
  or independently justified relation. Label preservation of current behavior as
  characterization. Code, an existing test, or a screenshot may contain the same bug.
- Consider each relevant scenario family; do not force one case per family or equal
  quotas. An empty successful result is an alternative path, not automatically an error.
- Compare candidates with actual existing assertions, including through callers.
  **KEEP** adequate checks, **UPDATE** a weak relevant case, **ADD** distinct protection,
  or choose **NO_NEW_TEST** with the existing protection/alternative check and its limits.
  Preserve mandatory gates and useful existing tests.
- Choose the least expensive boundary that contains the fault and exposes its result.
  Separate logic, wiring, persistence, and native-platform guarantees when necessary.
  One behavior may need several assertions; one-line security code may need several cases.
- Make wrong behavior distinguishable: different valid IDs/amounts, exact meaningful
  boundaries, valid other prerequisites, and observation of required/forbidden effects.
  Keep the subject real; a recorded mock call proves dispatch, not remote success.
- Resolve material ambiguities rather than inventing business rules. Ask the focused
  question and continue independent cases. Preserve unresolved requirement conflicts
  with their sources; do not choose a winner yourself. Mark affected cases conditional/blocked.

## Output

Lead with the recommendation and the few stack/environment facts affecting it.
For each ADD/UPDATE identify the scenario by name or the project's existing ID, family,
contract/risk, concrete setup and action/sequence, expected observations and their source
and status (accepted contract, characterization, or unknown), level/location, and
credible fault distinguished. Include unresolved conflicts, completion/settling criteria,
fixture/double, isolation/cleanup, and execution prerequisites where material. Follow
the [critic handoff](references/project-context.md#test-critic-handoff) when review is configured.

Use short case cards or a compact table; prefer the project's template. Do not squeeze
long sequences into unreadable cells. Cite existing protection once and briefly explain
significant omissions. No permanent risk registry or arbitrary case/assertion quota.

Before handoff, check: reachable setup; grounded oracle; observable result; discriminating
fault; useful added protection; feasible environment or explicit gap. Stop adding cases
when they add no relevant distinction. Do not silently drop a high-impact unresolved risk.

Close with decisions needed, unobserved surfaces, and the next phase. Distinguish source
evidence, live observations, assumptions, and unverified claims. State that tests were
not run in this design phase; never claim a passing suite, killed mutation, or proven
stability/sensitivity from a plan. An author's self-check is not independent review.
