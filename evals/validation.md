# Initial validation — October 9, 2026

Historical evidence for the first revision. This English rendering preserves the
reported outcomes; it is not a rerun on the current skill or translated prompts.

## Structural checks and packaging

- skill-creator quick_validate: Skill is valid.
- skill-conductor eval_skill: 11 passed, 0 failed, 0 warnings; its 10/10 is structural.
- Body: 104 lines / 882 words; description: 552 characters.
- 12 behavioral tasks and 6 positive/negative trigger queries; 9 relative links,
  unique IDs, and required eval fields checked.
- Archive: four runtime files under test-designer/; CRC and source-byte equality checked.

The first Windows conductor invocation failed printing Unicode through cp1251; it
was repeated with PYTHONUTF8=1. The plain Python validator lacked PyYAML; it was
repeated using isolated uv run --with pyyaml python -X utf8. These are authoring
requirements, not skill runtime dependencies.

## Author walkthrough

Static application in the author's session, with criteria visible: no independent
model, blind grading, or test execution. This is not a benchmark.

| Scenario | Decision and limit |
|---|---|
| 1. Expiry | Valid actor/invitation; fixed clock before and at deadline; equality denied with no membership/event. Unauthenticated refusal does not protect expiry. API wiring only for a separate risk. |
| 2. Retry key | UPDATE presence, UUID validity and retry equality; distinct action gets another key. Recorded requests do not prove backend deduplication; no live UI. |
| 3. Account source | UPDATE tests/session.test.ts: valid cache A, API B, result B. Detects calling but ignoring API; no new E2E required. |
| 4. Private rename | NO_NEW_TEST with retained public allow/deny/tenant/no-write checks; later execution pending. |
| 5. Required MCP | Provisional contract cases only; coverage/location conclusion blocked by required unavailable navigation. No policy change or rg-as-MCP claim. |
| 6. Memory/Probity | Active contract requires one durable record; use existing test-design plan section. Writer follows permitted increment, critic, then run; no execution or frozen-spec change. |
| 7. Mobile | Offline save, process termination/recovery and fresh read; reconnect gives one sync effect; photo denial preserves text. Android native/persistence levels; no live UI or invented iOS matrix. |
| 8. Desktop | Cancel creates no file; controlled write failure retains old bytes and recoverable edits; success survives restart/reopen. Temporary files and cleanup; mocked toast protects renderer feedback only. |
| 9. Rounding | Merchant policy and precision unresolved. Exact acceptance value for 2.345 undefined; preserving current 2.35 is characterization only if agreed. |
| 10. Wrong observer | Real policy with controlled transport observes the actual dial destination; policy-specific denial/no dial plus allowed control. No private-network contact. |
| 11. UI/seed | Proposed direct semantic/screenshot inspection; Escape/focus and durable save are distinct. No seed test or invented observation. |
| 12. One-test pressure | If restricted to one: cross-tenant owner denial with record intact. Same-tenant non-owner and allowed owner remain unprotected; no completeness claim. |

This walkthrough helps expose wording contradictions, not the probability of correct
agent behavior. Paired repeated runs and automatic discovery were not verified.
Claude's authentication probe failed because OAuth had expired. No live native/UI,
installed Probity enforcement, MCP integration, superiority, or Ponytail efficiency
claim was established.

## Historical security checks

Initial ai-repo-safety offline agent-skills scan returned nonzero because skill
scanners included local scanner templates/rules/Python files. TruffleHog reported no
secrets; Opengrep no matches in processed JSON. Python checks did not apply to the
Markdown runtime. Gitleaks history saw zero commits and did not establish cleanliness
of new files. Local scanner state was always excluded from the payload.

Rescanning the four-file runtime boundary reported:

| Check | Observed result |
|---|---|
| gitleaks dir, redacted | About 26.91 KB, no secrets, exit 0 |
| skillspector, no LLM | Four Markdown files, no scripts, LOW 7/100, exit 0; one MEDIUM EA2 |
| skill-scanner, fail on high | Exit 0; INFO MANIFEST_MISSING_LICENSE only; no high/critical |

EA2 referred to the old SKILL.md line 65: “name that protection and its limits. This
does not mean no verification.” It constrained NO_NEW_TEST, not destructive actions.
It was reviewed as a heuristic false positive; rules were not disabled and wording
was not weakened to satisfy the scanner. No distribution license was chosen.
Scanners do not prove model behavior safe or replace behavioral evaluations.

Git was initialized on main with local ignored safety state and hooks. No commit,
push, or global skill installation was performed.
