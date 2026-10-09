# UI exploration for test design

Read for web, mobile, desktop, terminal UI, or supplied screenshots. Explore only
the relevant journey and states; produce test cases, not a UI redesign or test run.

## Contents

- Establish the observable target and exploration charter
- Explore relevant behavior and record evidence
- Choose the surface that owns the risk
- Turn observations into implementable cases

## Establish what can be observed

Discover approved tools exposed in the current session: Playwright MCP or another
browser tool for web, a supported device/emulator tool for native mobile, and a native
automation/accessibility tool for desktop. Use the tool's actual documentation.
Do not treat Playwright, Appium, or any other product as a universal prerequisite.

Identify the target URL/application/build, environment, available test account, and
data reset route from project instructions. A safe dev/test target and permission
for the intended interactions must be established. Do not discover credentials in
secret files or reuse a personal authenticated session for destructive exploration.
If only production is available, stay within explicitly authorized safe observations;
do not submit purchases, send messages, delete records, or change access rights.

If the documented dev startup is authorized, does not run tests or migrations with
unapproved effects, and uses installed tools, it can prepare an inspection target.
Do not invoke a planner/generator/healer or a seed test that silently runs tests.
When setup requires a test runner, report that dependency for the next phase and
continue static design. Honor stronger local rules about environment startup.

Use [stack discovery](stack-discovery.md) to distinguish the installed test framework
from an interactive inspection tool. A Playwright dependency/configuration does not
provide a Playwright MCP session; a browser tool does not establish that the project's
Playwright suite is runnable. Verify capabilities before relying on network routing,
downloads, tracing, device controls, or accessibility inspection.

Write a short exploration charter: user goal, target/build, starting account/data,
questions to answer, permitted actions, and stopping point. Reuse a documented flow.
For example: determine how a saved export filter, empty result, and recoverable error
are presented on the provided test build; stop before operations outside that scope.
Do not explore every screen merely because the application is reachable.

## Explore the relevant behavior

1. Inspect the accessibility tree/DOM or native element hierarchy to identify actual
   roles, labels, state, and available actions. Derive locators from observed elements;
   a guessed selector must be labeled a candidate for later confirmation.
2. View a screenshot when layout, clipping, overlays, responsive behavior, or visual
   state matters. Pair visual evidence with semantic structure; neither supplies the
   other automatically. Record the platform/viewport and state relevant to the case.
3. Perform the authorized user action on test data. Observe its visible result and,
   where relevant and permitted, the matching network, storage, or OS boundary.
   Console errors and requests are clues; a quiet console is not proof of correctness.
4. Explore distinct contract-relevant states: initial/empty, loading, success, error,
   recovery, permission denial, or interrupted flow. Select only relevant states.
   If a state cannot be induced safely, design it from the contract and label unobserved.
5. Restore temporary test state with the established safe mechanism. Keep observations
   separate from expectations and avoid saving sensitive screenshots or payloads.

For a screenshot-only input, identify visible affordances and risks, but do not infer
hidden focus order, API behavior, persistence, or lifecycle behavior from pixels.
When tools or a target are unavailable, state the limitation and produce grounded
cases from source/spec/images; do not claim to have opened the app.

### Reach states deliberately

Trace one representative main journey first to discover actual entry points and
settling signals. Branch at decisions from the contract: an alternative input route,
a valid empty state, a refused operation, and recovery only where relevant. Inspect
an existing seeded fixture or documented test account before proposing new data.

Use already authorized simulation controls for deterministic network failure or
permission denial if available. Record exactly what was simulated and what stayed
real. Do not disconnect shared services, revoke a real user's rights, or change a
production account to manufacture a failure. Unreachable states become specified,
unobserved cases; inability to explore one does not eliminate its risk.

For asynchronous flows identify initiation, in-progress, completion, and interruption.
Wait on meaningful observed conditions instead of a fixed delay. Check whether input
remains editable, duplicate action is possible, or navigation loses work only when
these affect the contract. Do not infer persistence from a success toast or infer
server cancellation from a hidden progress indicator.

### Keep a compact observation record

For each useful observation record the source/build, starting state, action, observed
result, and design consequence. Store only evidence needed to justify a case.

| Evidence | What it establishes | What still needs another source |
|---|---|---|
| Semantic tree after failed submit | An alert and retry action currently exist | Correct business error and retained durable data |
| Request payload in an authorized trace | This interaction sent these fields | Server acceptance, authorization, and persisted effects |
| Download event | Download was initiated | Correct bytes, escaping, tenant selection, successful completion |
| Screenshot at a known viewport | Visible layout for this state | Keyboard order, native lifecycle, other viewport behavior |
| Reopen after a completed save | This target restored the observed state | Other users, devices, or failure points not exercised |

Observed behavior can expose a discrepancy with requirements; it does not silently
replace them. For example, a filter lost after reopening needs a product decision if
the contract only says it survives an in-place failed request.

## Choose the surface that owns the risk

| Surface | Inspect/design when relevant | Limit to preserve |
|---|---|---|
| Web | Form validation and submit outcome, keyboard/focus, routing/back/refresh, loading/error recovery, responsive obstruction | Component simulation does not prove real layout, download, browser storage, or navigation behavior. |
| Native mobile | Background/foreground, process recreation, offline/reconnect, permission grant/deny/revoke, deep links, keyboard/orientation, interrupted submission | Name actual supported OS/device class. Browser emulation cannot establish native lifecycle or permission behavior. |
| Desktop | Open/save/cancel, overwrite protection, disk permission failure, restart recovery, windows/focus/shortcuts, IPC and external-process boundaries | Separate renderer behavior from native host effects; use temporary files and controlled child processes. |
| Hybrid client | Shared UI logic plus the specific native bridge/lifecycle | Reuse shared cases; add platform cases for genuinely different outcomes. |
| Terminal/CLI | Arguments/stdin, exit status, stdout/stderr, filesystem effects, signal/cancel | Text output alone may miss data corruption or a wrong exit status. |

Accessibility cases should name an action and observation: keyboard reaches submit,
an error is associated with the field, focus returns after modal close, essential
controls remain usable at the relevant zoom or text size. An automated scan alone
does not establish full accessibility. Derive supported configurations from project
requirements and actual usage, not a universal browser/device matrix.

## Turn observations into cases

Prefer stable semantic locators or established test IDs. Use the real component and
handler for component cases, and the real relevant wiring for E2E cases. If network
responses are controlled, label the test's actual scope instead of calling it full
system coverage. A spinner disappearing does not by itself prove a save succeeded.

A useful case names the user goal, starting data/state, action, final observation,
failure it should catch, and level. Include wait/settling conditions and cleanup where
they affect repeatability; avoid sleeps and automatic baseline approval.

For a visual regression case, specify the meaningful region/state, a reviewed expected
baseline, stable rendering conditions, and the difference that matters. A screenshot
saved during exploration is evidence for design, not a passing visual assertion.
Keep behavioral assertions for outcomes a screenshot cannot establish.

Example handoff: **UPDATE export browser case**. An existing case observes only a
download event. Use an editor with two matching tenant rows, one nonmatching row, and
a foreign-tenant row; include a quoted/comma-containing field. Export and inspect
completed downloaded bytes for the contract's exact selection and CSV escaping.
Reuse the current authenticated browser fixture and temporary download cleanup.
This protects actual browser-to-service wiring and serialization. A component case
with a controlled response separately covers error presentation; it cannot establish
the exported dataset. Select these cases only if the export contract requires them.
