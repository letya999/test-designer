# Security policy

## Reporting a vulnerability

Use [GitHub private vulnerability reporting](https://github.com/letya999/test-designer/security/advisories/new).
Do not publish credentials, private logs, exploit payloads containing user data,
or confidential project content in issues or pull requests.

Describe affected instructions/files, a minimal sanitized reproduction, impact,
and relevant client/tool versions. Security reports include prompt-injection routes,
unexpected tool execution, scope bypasses, and exposure of project data, as well as
vulnerabilities in authoring helpers. No response-time guarantee is currently offered.

If a secret is exposed, revoke or rotate it first, then coordinate history cleanup.
Deleting a file does not revoke a credential or erase existing clones.

## Checks and support

The current `dev` and `main` revisions receive fixes; no older-version support
guarantee is offered. CI scans Git history with Gitleaks, validates the distributable,
and tests authoring helpers. GitHub secret scanning and push protection are enabled
when the hosting account supports them. Maintainer-local scanners may supplement CI.

This instruction skill cannot enforce permissions by itself. Follow your agent
host's access controls, project rules, and configured gates. A scanner pass or a
well-formed skill does not prove model behavior safe or a test design correct.
