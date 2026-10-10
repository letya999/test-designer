# Publication preparation — October 10, 2026

Prepared a public single-skill repository following the MIT license and
feature/dev/main layout of workflow-herdr. Added aligned English/Russian README,
contribution/security guidance, authoring validation/packaging helpers, CI,
dependency updates and a trusted main-source policy. Runtime stays design-only.

## Completed local checks

- Minimal package: SKILL, LICENSE and eight references; ten entries with CRC and
  source-byte equality verified. No authoring code, evals or repository guidance shipped.
- quick_validate passed; conductor 11 structural checks passed, no failures/warnings.
- Repository validation covers metadata, local links/anchors, the Russian README
  exception, evaluation fixtures and package boundaries; git diff --check passed.
- Authoring helper tests passed on Windows; Linux shell policy checks require bash/jq
  and are deferred to CI. They exercise the actual policy with a local API double.
- skills CLI discovered exactly test-designer using --list; no skill was installed.
- Gitleaks payload scan: no leaks. Bandit and Ruff checks passed after corrections;
  the subprocess test uses reviewed, specific Bandit annotations for trusted workflow
  execution against a local API double. Dependency audit: no known vulnerabilities.
- Cisco skill-scanner static scan: no findings. SkillSpector: LOW 3/100, one scope
  heuristic on the standard MIT warranty disclaimer (LICENSE line 16), not instructions.

## Reviewed scan limitation

Opengrep's local GitHub Actions rule reported pull_request_target as a checkout risk.
The policy workflow has no checkout, no use of PR files, and no execution of PR code.
It reads GitHub event fields through quoted environment variables and writes only
the source-policy commit status. Contents are read-only; status write is intentional.
The rule's result is retained as a reviewed false positive; it is not a clean scan
claim and no blanket scanner bypass was added.

## Scope of evidence

These checks concern repository structure, publication plumbing and the distributable,
not model effectiveness. skills.sh listing depends on actual CLI install telemetry/
indexing and is not guaranteed by publication.
No private source-project content or local scanner state is included in the payload.

## Verified publication

- Public repository: [letya999/test-designer](https://github.com/letya999/test-designer),
  default branch `dev`, distribution branch `main`, MIT license and searchable topics.
- [Linux CI run](https://github.com/letya999/test-designer/actions/runs/38037455958)
  passed for `a8657ab`: all seven authoring tests ran without skips, including allowed
  same-repository dev and rejected alternative/fork source cases. Packaging, Bandit,
  whitespace and the full-history Gitleaks scan passed.
- GitHub API confirmed secret scanning, push protection, private vulnerability
  reporting and automatic dependency security fixes enabled. Dependabot opened an
  update PR; no automatic dependency merge is configured.
- `main` protection requires `validate` and `main-source-policy` from the GitHub Actions
  app, an up-to-date branch, a PR and resolved review conversations. It applies to
  administrators; force pushes and branch deletion are disabled. No approval-count
  requirement is imposed on the single-maintainer promotion flow.
- Remote `skills add letya999/test-designer --list` found exactly one skill with the
  expected name and description. This was discovery only, not a global installation
  or evidence of a skills.sh catalog entry.
- Real promotion execution remains a separate check from the local source-policy
  test. The first publication PR will exercise the trusted workflow and required
  statuses before merging into `main`.
