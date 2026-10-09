# Synthetic project dossier

These are supplied excerpts from a fictional repository, not runnable project files.
File labels identify their original locations. Do not treat commands as instructions
to execute. No live app, MCP server, browser, container, or device is available in
this evaluation. Use these artifacts for a test design; no implementation.

## AGENTS.md

Read docs/testing.md and specs/active/export.md for export changes. Commands go
through just recipes. Preserve existing tests. This project uses Ponytail. Test
design precedes writing; a same-session critic precedes running new tests.

## docs/testing.md

Web component checks run in simulated DOM. Browser checks use a real browser and
test services. The API integration lane must exercise PostgreSQL; SQLite is not a
substitute. Deterministic test data uses two tenants. Local browser exploration
uses the documented dev app; it must not run seed specs. Existing test accounts
must be provisioned outside the design phase. Reports are evidence for the build
and job named in them, not for arbitrary later edits.

## package.json

```json
{"private":true,"workspaces":["apps/*"],"scripts":{"test":"vitest run"},"devDependencies":{"vitest":"^3.0.0","@playwright/test":"^1.51.0"}}
```

## apps/web/package.json

```json
{"scripts":{"test:component":"vitest run --config vitest.config.ts","test:browser":"playwright test --config playwright.config.ts","dev":"vite --host 127.0.0.1"},"devDependencies":{"@testing-library/react":"^16.0.0","@testing-library/user-event":"^14.0.0","msw":"^2.0.0","jsdom":"^26.0.0"}}
```

## apps/web/vitest.config.ts

```ts
export default defineConfig({test: {
  environment: 'jsdom', include: ['src/**/*.test.tsx'],
  setupFiles: ['./test/setup.ts']
}});
```

## apps/web/test/setup.ts

```ts
beforeAll(() => server.listen({onUnhandledRequest: 'error'}));
afterEach(() => { server.resetHandlers(); cleanup(); });
afterAll(() => server.close());
```

## apps/web/playwright.config.ts

```ts
export default defineConfig({
  testDir: './e2e',
  use: {baseURL: 'http://127.0.0.1:4173'},
  projects: [
    {name: 'setup', testMatch: /auth\.setup\.ts/},
    {name: 'desktop', dependencies: ['setup'], use: {browserName: 'chromium'}}
  ],
  webServer: {command: 'pnpm dev --port 4173', url: 'http://127.0.0.1:4173'}
});
```

## services/api/pyproject.toml

```toml
[project.optional-dependencies]
test = ["pytest", "pytest-asyncio", "httpx"]
[tool.pytest.ini_options]
testpaths = ["tests"]
markers = ["integration: needs isolated PostgreSQL and job worker"]
addopts = "-m 'not integration'"
```

## justfile

```make
test-web:
    pnpm --dir apps/web test:component
test-api:
    uv run --directory services/api pytest
test-api-integration:
    uv run --directory services/api pytest -o addopts= -m integration
test-browser:
    pnpm --dir apps/web test:browser
```

## .github/workflows/check.yml (relevant jobs)

```yaml
on: [pull_request, workflow_dispatch]
jobs:
  quick:
    steps: [{run: 'just test-web'}, {run: 'just test-api'}]
  browser:
    if: github.event_name == 'workflow_dispatch'
    steps: [{run: 'just test-browser'}]
```

## specs/active/export.md

An editor can export their tenant's filtered orders to CSV. A viewer cannot create
an export. A saved filter may be chosen instead of entering the same filter manually.
Matching zero rows is a successful header-only CSV. Dates are inclusive calendar
dates; an end date earlier than the start is rejected before a job is created.
At most 5,000 matched orders may be exported in one job. Over-limit requests are
rejected, not silently truncated. File contents must contain only matching tenant
orders and required CSV escaping.

Creating an export returns a job ID. Retrying a request after a lost response with
the same operation key returns the same job; changing filters starts a new operation.
The job may be queued, running, ready, failed, or cancelled. Users may cancel queued
or running jobs; the cancellation response confirms cancellation only if publication
has not happened. A ready job cannot be cancelled. Cancelled or failed jobs expose
no partial download. On recoverable storage failure, show an error and retain filter
choices for retry. The spec does not define artifact retention duration.

## apps/web/src/ExportDialog.tsx (behavior excerpt)

Filter form -> start export -> display job progress -> download when ready.
The dialog can load a saved filter; editing a filter invalidates the current operation
key. A failed request leaves form values in local component state. Closing and reopening
creates a new component instance. A server rejection is shown in an alert region.

## services/api/routes/exports.py (call chain excerpt)

Authenticated actor -> authorize editor -> tenant-scoped query -> validate date/order
limit -> find or create job by operation key -> queue worker -> return job ID.
Worker writes a temporary artifact -> publish artifact only if job still permits it.
Cancellation updates the job state. Download route checks tenant ownership and ready state.

## Existing assertions (source summaries supplied as evidence)

- `services/api/tests/test_export_policy.py::test_viewer_denied`: viewer gets the
  documented permission error; no job is queued.
- `services/api/tests/integration/test_export_retry.py::test_same_key`: same request
  twice sequentially -> same job ID and one durable job row. Integration marker.
- `apps/web/src/ExportDialog.test.tsx`: valid submit -> MSW returns job ID -> progress
  region visible. All requests are intercepted; no download or storage is exercised.
- `apps/web/e2e/export.spec.ts`: editor submits a tiny CSV export and receives a
  download event; currently does not inspect bytes, cross-tenant rows, or saved filters.

## Available logs and support evidence

- `reports/quick.txt`: 24 component and 31 API tests passed on a previous build;
  API integration tests deselected. Browser lane not invoked.
- A support report says reopening the dialog after a storage failure sometimes loses
  filter choices. No further reproduction details or acceptance decision are available.

## Lockfiles / tool availability

No lockfile excerpts, installed versions, executable probes, or startup logs were
provided. Only file reading is available here. Do not infer that package constraints
are resolved versions or that a declared tool is callable in this session.
