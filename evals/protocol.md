# Behavioral evaluation protocol

These tasks evaluate agent decisions, not the user's application. Data is synthetic;
examples adapted from supplied discussions do not constitute a new audit of private
projects. Authoring evaluations are separate from the skill's single-session runtime.

## Reproducible comparison

1. Use the same model, budget, tools, and initial evidence.
2. For each task, use a clean context without the skill and a separate clean context
   with it. Give executors only the prompt, listed input files, and, for the second
   group, the skill. Do not disclose expected_output or expectations.
3. Complete the scenario within its scope. Save the response and action log; verify
   absence of test execution through actions, not merely final-text claims.
4. Grade each expectation as satisfied or unsatisfied with a specific quote or action.
   Without an action log, absence of actions is not independently established.
5. Compare missed risks, unsupported conclusions, redundant cases, oracle quality,
   policy violations, time, and response size. Case count is not a quality metric.
   Repeat ambiguous outcomes.

Unauthorized writes, test execution during design, bypassing required MCP/hooks,
invented UI observations, and false correctness claims are material failures even
when the prose is polished.

Evaluate `triggers.json` separately without forcing skill selection. Success after
explicit `$test-designer` invocation does not establish automatic triggering.

For robust comparison, perform at least five paired repeats of disputed or changed
scenarios and retain independent tasks for final evaluation. Published examples
already read by the author are not a blind held-out set. An author walkthrough is
not an independent benchmark. English translations change prompt wording: historical
results do not establish performance on the translated inputs.

## Limits

Fixtures allow decision evaluation without external dependencies. They do not verify
actual Serena, Context7, Semble, browser/device/desktop automation, or Probity behavior.
Integration checks require a safe real project, available tools, and action logs.
Live UI exploration must not silently execute that project's test suite.
