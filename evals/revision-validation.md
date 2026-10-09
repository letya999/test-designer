# Revision validation — October 9, 2026

Historical outcomes, translated into English; no rerun is implied.

## Change and probes

Core reduced from 882 to 674 words (104 to 78 body lines by conductor). Five
references cover context, discovery, research, design, and UI exploration. Runtime
remains design-only and single-session; the following probes are authoring evaluations.

Separate contexts received the synthetic [export dossier](fixtures/export-project.md):
one without the skill, one with the old revision, and one with the new revision.
Executors received task and dossier without grading criteria. The new revision also
received the private-helper rename task (eval 14). Assessment uses returned responses,
not independent blind grading. Full action logs are not included, so executor claims
of no execution are not an audit of those actions.

| Property | No skill / old revision | New revision |
|---|---|---|
| Stack/environment/CI | Both separated component, browser, API integration and execution limits | Named .tsx, MSW cleanup, auth setup, PostgreSQL, wrappers, missing integration job and manual browser job |
| Existing protection | Both kept useful cases and strengthened download assertions | KEEP viewer denial, progress, sequential replay; UPDATE file contents |
| Path families | Both found saved filter, zero rows, refusals and recovery | Explicit families; empty CSV treated as success |
| Distinguishing data | Both proposed dates, limit and tenant isolation | A101/A102/A103/A104/B201, inside/outside dates, quoting, 4999/5000/5001 |
| Retry/concurrency | Both included lost response and simultaneous retries | Lost response, independent operations and publish/cancel; concurrent duplicates deferred because explicit guarantee absent |
| Contract uncertainty | Neither invented retention/reopen rules | Also flagged dialect, timezone, error shape and retry-after-failure ambiguity |
| Response size | Detailed plans | Also detailed; shorter complex outputs not established |

The concurrent-duplicate guarantee was left unspecified. That is a reasonable oracle
limit, but the concurrency question should remain an explicit unresolved risk.
Eval 13's concurrency criterion was partial; this was not a full pass of all criteria.
Other listed properties were present by author assessment.

The simple rename answer recommended NO_NEW_TEST, retained public exit/stdout/stderr
checks and disclosed execution unconfirmed. All three eval 14 content expectations
were met; discovery did not force a large plan.

Controls already handled core risks well. These observations do not prove superiority.
No five repeats, blind grading, automatic trigger evaluation, or real application
verification. This is exploration, not the full conductor benchmark.

## Structure, package, and historical scan

- quick_validate valid; conductor 11 passed / 0 failed / 0 warnings; 10/10 structural.
- 14 tasks, required fields, unique IDs and fixture paths checked.
- Archive: SKILL plus five references; CRC and byte equality checked; authoring
  material excluded. Relative Markdown links checked.
- Six-file payload scan: Gitleaks exit 0, no secrets; SkillSpector exit 0, LOW 0/100,
  no findings; skill-scanner exit 0, INFO MANIFEST_MISSING_LICENSE only.
- After scanning, one textual clarification separated resolved version from configured.

License remained unselected; no commit/push/global installation. See the historical
[initial validation](validation.md).
