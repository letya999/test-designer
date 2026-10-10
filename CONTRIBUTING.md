# Contributing

## Branches and pull requests

Use `feature/<name>` or `fix/<name>` branches from `dev` and open PRs into `dev`.
Keep changes focused and explain the behavior or design decision they improve.
The default branch is `dev`; `main` is the reviewed distribution branch.

Release promotion uses a PR from **this repository's `dev` to `main`**. The trusted
promotion workflow rejects other source branches and forks. Protected `main` requires
that status, validation/secret scanning, an up-to-date branch, and resolved review
conversations, including for administrators. Direct push, force push and deletion
are disabled. No approval count is required, so the maintainer can promote their
own changes; substantive review is still encouraged.

Use a merge commit for `dev -> main` to preserve ancestry. Keep both long-lived
branches; automatic branch deletion is disabled. Synchronize `dev` with `main` as
needed before the next promotion. Never disable a failing gate to merge.

## Local checks

Python 3.10+ is required only for authoring helpers, not skill use. In an isolated
environment, install `requirements-dev.txt`, then run:

```bash
python scripts/validate.py --package
python -m unittest discover -s scripts -p "test_*.py" -v
gitleaks git --redact --exit-code 1
git diff --check
```

CI runs equivalent checks without depending on a maintainer's local skill installation.
Do not commit `dist/`, `.repo-safety/`, temporary evaluations, credentials or test-project
data. The package includes SKILL, LICENSE and references only; it excludes authoring
helpers and repository guidance. Installation through the skills CLI follows that
tool's own copy behavior; the minimal archive is built by the authoring helper.

## Instruction changes

Read AGENTS and the relevant references before editing. Preserve the designer's
scope and the writer/critic/execution boundaries. Update routing and relevant
synthetic evals when behavior changes, with evidence limits recorded honestly.
Align English and Russian README guidance. Runtime instructions remain English.

Structural checks do not establish automatic triggering or model quality. Use
[the behavioral protocol](evals/protocol.md) for comparative claims. Do not relabel
historical runs as results of new instructions or translated prompts.

## Attribution and conduct

Contributions are submitted under the repository's MIT license. Preserve attribution
for original ideas and check source terms before verbatim reuse. Be respectful,
provide reproducible examples without private data, and discuss actionable behavior.
Report vulnerabilities privately following [SECURITY.md](SECURITY.md).
