# Description revision — October 10, 2026

Applied skill-conductor's capability/trigger/exclusion pattern without putting the
workflow in discovery metadata. Description shortened from 522 to 245 characters
(2.13 times) and from 70 to 31 words (2.26 times). Skill body and role are unchanged.

The description names test plans, acceptance/regression scenarios, boundaries,
error paths and “what to test,” including case selection within implementation tasks.
It excludes writing/reviewing/running tests, infrastructure and A/B experiments.

Manual routing review of the existing six trigger queries: export cancellation,
native recovery planning and invoice-retry assertion intent match the capability;
written-test review, suite execution and statistical A/B sample size match exclusions.
This is an author inspection, not observed automatic selection by an agent host.

quick_validate passed; conductor structural checks: 11 passed, 0 failed, 0 warnings,
245-character description. Runtime links, English maintained text, nine-file archive
entry names/CRC/source bytes and git diff --check passed. Archive rebuilt.

No automated optimization loop, independent trigger run, repeated comparison,
commit or push was performed. Improved automatic triggering remains unmeasured.
