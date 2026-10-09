# Discover the test stack and environments

Use before choosing test placement, a runner, or an inspection tool in an unfamiliar
package. Reuse a current inventory rather than rediscovering it for every case.

## Contents

1. Scope the packages and follow the execution chain
2. Recognize framework and helper signals
3. Separate declaration, configuration, availability, and execution
4. Map environments and supporting tools
5. Produce a small usable inventory

## 1. Scope the packages and follow the execution chain

Start at the changed feature's owning package and the boundaries its cases cross.
In a monorepo, identify workspace roots and per-package manifests; a root `test`
script may select only one package or a different configuration. For a shared library,
inspect representative callers and contract tests, not every consuming application.

Follow this chain by reading files:

`project rule → wrapper/recipe → workspace script → runner config → setup/fixtures
→ test selection → CI job and services`

Use the required project search tools. Without a mandated order, file listing and
targeted literal search are enough for manifests/configs; semantic search helps find
feature tests named differently from production symbols. Do not dump giant lockfiles
or entire CI directories: inspect relevant package entries, imports, jobs and globs.

Read one representative adjacent test per candidate level. Record how it imports the
runner, assertions, fixtures and subject; where it places files; how it creates data;
and what it actually observes. A dependency name alone does not establish these facts.

### Follow configuration, not filenames alone

Check the effective package/working directory, inherited configs, include/exclude
patterns, project names, tags/markers, build conditions, setup hooks, and test filters.
Examples of design-changing details:

- `.tsx` component files excluded by a `.test.ts`-only pattern;
- API integration markers excluded by default options;
- browser project depending on an authentication setup project;
- Go build tags or separate modules selecting a different set of tests;
- test data reset occurring in a wrapper rather than in the individual fixture;
- a CI lane limited to manual/nightly runs or a subset of changed paths.

Read scripts before proposing them as later commands. Avoid invoking `--collect-only`,
`--list`, imports, setup projects or discovery plugins in this phase: they can execute
project code. Static discovery is sufficient for design; runtime enrollment remains
unverified until execution. Do not substitute a direct runner command for a required
`just`/Make/Gradle/build-system entrypoint.

## 2. Recognize framework and helper signals

This is a search aid, not an installation list or exhaustive registry. Confirm findings
against this repository and its resolved version before relying on version-specific APIs.

| Ecosystem | Start with | Distinguish and inspect |
|---|---|---|
| JS/TS | Workspace manifests, lockfiles, package scripts, Vitest/Jest/Playwright/Cypress configs, test imports | Runner vs assertion/UI helper; jsdom/happy-dom vs real browser; component vs browser projects; MSW/routes; setup files and `.tsx` selection |
| Python | `pyproject.toml`, pytest/tox/nox configs, `conftest.py`, test imports | pytest/unittest, async plugins, markers, fixture scope, real API client vs mocked transport, DB engine and migrations |
| Go | `go.mod`, `_test.go`, build tags, test helpers and recipes | Standard `testing`, helper libraries, `httptest`, integration packages, race/fuzz lanes, external service fixtures |
| JVM | Maven/Gradle modules, test source sets and imports | JUnit/TestNG, parameterized tests, mocks, Spring/test application context, Testcontainers, unit vs integration tasks |
| .NET | Solution/project files, package references, runsettings, test attributes | xUnit/NUnit/MSTest, test host, HTTP app factory, mocks, target frameworks and platform-specific lanes |
| Rust | `Cargo.toml`, workspace/features, `tests/`, `#[test]` and conditional attributes | Unit/integration/doc tests, feature-gated behavior, async runtime, property/fuzz targets, native dependencies |
| Native/hybrid mobile | Gradle/Xcode/Swift/Flutter/React Native files and existing test imports | Domain tests vs instrumentation/XCTest/UI tests; Robolectric/device differences; Detox/Maestro/Appium or project-specific driver; bridge behavior |
| Desktop/native | Build files, existing test harness and automation config | Native toolkit tests vs browser renderer tests; Electron/Tauri/native bridge; filesystem/process/OS tests; device/driver support |
| Other languages | Manifest/build file, test directories, imports, CI entrypoint | Identify the actual runner from evidence; use its versioned docs rather than translating another ecosystem's mechanics |

Search for supporting capabilities only when a chosen case needs them:

| Need | Useful existing evidence | Design consequence |
|---|---|---|
| User interaction | Testing Library/user-event or native UI helpers | Realistic events and semantic observations at that level |
| Controlled responses | MSW, HTTP stubs, route interception, recording transports | Identify what remains real and which guarantees are simulated |
| Data/services | Testcontainers, Compose, local emulators, test DB fixtures | Account for engine/version, migrations, seed/reset and lifecycle |
| Time/concurrency | Injected clocks, fake timers, barriers, deterministic schedulers | Reach the branch/overlap without sleeps or chance |
| Properties/fuzzing | Hypothesis, fast-check, proptest, native fuzz targets or equivalents | Reuse suitable generators/models; preserve replay and meaningful domains |
| Contracts | Schema validators, consumer/provider tests, protocol fixtures | State whether they cover shape, compatibility or domain semantics |
| Visual/a11y | Reviewed goldens, screenshot comparison, accessibility tooling | Separate capture from assertion; retain interaction checks |

Do not add dependencies because a table mentions them. When no existing seam/tool can
observe an important behavior, name the gap and the smallest proposed enabling change
for the implementation phase. Do not build it inside test design.

## 3. Separate evidence states

| State | Evidence needed | What it does not establish |
|---|---|---|
| Declared | Manifest or dependency constraint | Exact installed version, selected runner, working binary |
| Resolved version | Relevant lockfile entry for the owning package | Installation or successful startup |
| Configured | Effective script/config and setup for the owning package | Exact version without resolution evidence, tool access, valid credentials |
| Available for inspection | Tool exposed in this session and a usable permitted target | That the test suite includes or passes the case |
| Enrolled in a lane | CI/recipe selection includes the test's package/type | That the lane ran on this build |
| Observed execution | Matching existing log identifies build, command, cases and outcomes | That later changes pass, or unselected cases were exercised |

Do not probe secrets or credentials. Constraints like `^3.0.0` are not resolved
versions. Use available lock/config evidence; mark unknowns instead of guessing.
Existing logs narrow uncertainty, but you do not produce new test logs in design.

## 4. Map environments and supporting tools

For each selected level, identify only prerequisites that affect the case:

- **Runtime:** process/OS, simulated DOM vs browser, native device/emulator, build variant.
- **Dependencies:** actual engine/service vs double; network/queue/worker requirements.
- **Data:** isolated tenant/user/roles, seed state, clock, persistent artifacts, reset/cleanup.
- **Target:** documented dev/test origin or application; ownership and safe actions.
- **Execution route:** working directory, project/marker and recipe; CI lane and gating.

One app can use several environments. A component success with MSW is not a database
integration result. A browser installed in CI is not a browser MCP in this session.
Playwright as a Vitest browser provider, Playwright Test as a runner, and Playwright
MCP as exploration tools have different roles; discover the actual one.

Check exposed MCP/tool capabilities and local instructions, not remembered tool names.
Playwright/DevTools or an existing approved browser can help inspect web UI. Native
drivers and device/desktop tools may help inspect other clients. Do not install them,
declare them mandatory globally, or promise native coverage from browser emulation.
For unavailable tools, apply the required-vs-optional rule in project-context.md.

## 5. Produce a small usable inventory

Use a few sentences for one package; a table helps when multiple environments matter:

| Surface / level | Runner and useful helpers | Environment / real boundaries | Later command and selection | Evidence / gap |
|---|---|---|---|---|
| Web component | Existing Vitest, Testing Library, MSW | jsdom; HTTP simulated | Component recipe; `.tsx` glob verified | Config read; no run claimed |
| API integration | Existing pytest fixtures | Isolated PostgreSQL + worker | Dedicated integration recipe | Default lane excludes integration |

Give file references for claims. Unknown paths/commands stay unknown or explicitly
proposed. Do not list every library in the repo. The inventory is sufficient when
each planned case has an honest execution home or a specific feasibility gap.
