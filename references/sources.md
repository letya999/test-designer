# Sources and further reading

Use for attribution or deeper research; normal case selection does not require
reading this bibliography. The practical guidance is implemented in the other
references. This is an original synthesis, not a copied syllabus or certification
requirement. Sources were investigated on October 9–10, 2026; branch links can change.
No source's popularity or claimed benchmark establishes this skill's effectiveness.

## Test-design foundations

| Source | Applied idea and reading limit |
|---|---|
| [ISTQB CTFL 4.0.1, chapter 4](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) | Public technique definitions: partitions, boundary neighbors, decision tables, transitions, and explicit coverage criteria. Selected cases do not automatically mean complete coverage. |
| [James Bach — Heuristic Test Strategy Model, available PDF v6.0](https://www.developsense.com/resource/htsm.pdf) | Context, product dimensions, quality concerns, and adaptable techniques guide investigation. Heuristics are prompts, not a compulsory inventory. |
| [NIST SP 800-142 — Practical Combinatorial Testing](https://www.nist.gov/publications/practical-combinatorial-testing) | Official overview and publication link: meaningful factors, constraints, and interaction strength. No claim that pairwise detects every interaction fault. |
| [NIST — Beyond Pairwise](https://csrc.nist.gov/pubs/journal/2008/06/practical-combinatorial-testing-beyond-pairwise/final) | Higher-order interactions remain a distinct concern; known multi-condition rules need direct protection. |
| [Ham Vocke — The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) | Different boundaries protect different faults; faithful lower levels and thin wiring journeys. No universal enforced test ratio. |
| [Maurício Aniche — Effective Software Testing](https://www.manning.com/books/effective-software-testing) | Publisher description and available topics: systematic case derivation, contracts, invariants, and properties. The full paid book was not read. |
| [Elisabeth Hendrickson — Explore It!](https://pragprog.com/titles/ehxta/explore-it/) | Publisher description: focused exploration of risks informs candidate cases. The full paid book was not read. |
| [Kaner, Bach, Pettichord — Lessons Learned in Software Testing](https://uat.store.wiley.com/en-us/lessons-learned-in-software-testing-a-context-driven-approach-p-9780471081128) | Publisher description and further reading on context-driven testing; specific unseen chapters are not cited as evidence for rules. |
| [Aniche, Treude, Zaidman — How Developers Engineer Test Cases](https://arxiv.org/abs/2103.01783) | Abstract of an observational study of test-case reasoning; no numerical effectiveness claim is derived here. |
| [fast-check — What is Property-Based Testing?](https://fast-check.dev/docs/introduction/what-is-property-based-testing/) | Official explanation of properties, generation, and shrinking. These concepts do not require JavaScript or a new dependency. |
| [Hypothesis — What is property-based testing?](https://hypothesis.works/articles/what-is-property-based-testing/) | Author's discussion of the approach; Python APIs are not prescribed by this skill. |
| [Fu et al. — Test Adequacy for Metamorphic Testing](https://arxiv.org/abs/2412.20692) | Abstract: relation selection and source-input selection both matter. Merely defining a relation does not prove adequacy. |

## Existing skill approaches

| Source | Incorporated distinction; excluded scope |
|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | Portable SKILL.md and relative resources; no mandatory host-specific permissions or tools. Format alone does not enforce behavior. |
| [adewale — testing-best-practices](https://github.com/adewale/testing-best-practices/blob/main/testing-best-practices/SKILL.md) | Distinguishing data, independent expected results, boundaries, and faithful levels. Its writing/assessment/execution modes are not adopted. |
| [sjinks — test-design](https://github.com/sjinks/ai-skills/blob/master/skills/test-design/SKILL.md) | Compact contracts and observable outcomes. Its implementation/execution capability is outside this design phase. |
| [dotnet — test-gap-analysis](https://github.com/dotnet/skills/blob/main/plugins/dotnet-test/skills/test-gap-analysis/SKILL.md) | Inspect actual assertions before declaring a gap. No whole-repository mutation audit or execution-backed verdict without execution. |
| [jamestexas — test-fidelity](https://github.com/jamestexas/agents/blob/main/skills/test-fidelity/SKILL.md) | Wrong observers, fake subjects, unreachable setups, and vacuous guarantees. No additional runtime agents or specialized analysis engine. |
| [Trail of Bits — property-based-testing](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | Justified properties and useful generator domains. No mandatory PBT, universal property ranking, or production refactor. |
| [GitLab — collectors](https://gitlab.com/gitlab-org/ai/skills/-/blob/main/skills/bug-burndown/references/collectors.md) | Separate evidence from hypotheses. Its broader orchestration and mutation/coverage execution are excluded. |

## Integration sources

| Source | Local adaptation |
|---|---|
| [Ponytail](https://github.com/dietrichgebert/ponytail) | Simplicity after understanding affected code; reuse and preserve distinct valuable protection. No imported benchmark claims. |
| [Probity](https://github.com/nizos/probity) and [rules](https://github.com/nizos/probity/blob/main/docs/rules.md) | Preserve the deployed configuration and gates. External model calls made by that product are separate from this skill's runtime scope. |
| [Memory Bank](https://github.com/letya999/memory_bank_setup) and [AGENTS template](https://github.com/letya999/memory_bank_setup/blob/main/memory_bank/project_templates/AGENTS.md) | Follow the local router, distinguish current state/specifications/history/work, reuse existing work artifacts; no automatic template installation. |
| [Serena](https://github.com/oraios/serena) | Supported structural navigation in the correct initialized project. |
| [Context7](https://github.com/upstash/context7) | Appropriate library/version documentation; not a business-rule oracle. |
| [Semble integration](https://github.com/MinishLab/semble/blob/main/src/semble/installer/agents.py) | Semantic discovery followed by reading found code, respecting search mode and local policy. |

Required tools cannot silently be replaced by optional fallbacks. Compatibility
comes from reading current project policy and capabilities, not promising eternal
compatibility with remote versions. See [project context](project-context.md).

## Faithful observation and stack discovery

| Source | Applied distinction |
|---|---|
| [Testing Library principles](https://testing-library.com/docs/guiding-principles/) | User actions and observable behavior, rather than only implementation details. |
| [Playwright best practices](https://playwright.dev/docs/best-practices) | Ordinary actions, isolation, and relevant observations. Playwright is not mandatory. |
| [Playwright Test Agents](https://playwright.dev/docs/test-agents) | Planning and generation are distinct; running a seed test is still execution. |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Semantic inspection and screenshots complement each other; available tools do not prove a safe target is available. |
| [Playwright configuration](https://playwright.dev/docs/test-configuration) and [setup dependencies](https://playwright.dev/docs/test-global-setup-teardown) | Projects, setup, webServer and selection affect execution; setup can itself execute tests. |
| [Vitest environments](https://vitest.dev/guide/environment.html) | Simulated DOM and browser execution provide different evidence. |
| [pytest configuration](https://docs.pytest.org/en/stable/reference/customize.html) | Configuration and selection matter; a test file's presence does not prove inclusion. |
| [Android strategies](https://developer.android.com/training/testing/fundamentals/strategies) | Choose a boundary that contains native lifecycle and persistence effects. |
| [Appium introduction](https://appium.io/docs/en/latest/intro/) | Platform support depends on relevant drivers; a tool name alone proves little. |

## Research boundaries

The initial supplied texts informed the design/critic separation, independent
expectations, meaningful fault witnesses, UI exploration, existing-test comparison,
and project-rule precedence. Private messages and unavailable original exports were
not copied. References to unavailable archives or reports were not independently
verified. Synthetic evaluation examples are not fresh accusations about private projects.

GitHub/GitLab and official documentation informed the practical rules. skills.sh,
social discussions, translations, and community posts helped discover questions and
sources; they were not treated as technical proof or comparative measurements.
Targeted X and Internet Archive searches did not produce a usable verified source;
this does not establish an absence of relevant material on those platforms.

Repeated themes included oracle uncertainty, nondeterminism, data scale, isolation,
and the cost of execution-based sensitivity checks. Those ideas appear directly in
the case references. Mutation execution, a separate critic, additional agents,
mandatory tool installations, permanent risk registries, and fixed coverage quotas
remain outside this skill's runtime role.

No full paid books, reproduced research experiments, or repeated blind comparative
benchmark are claimed. Review source licenses before any future verbatim reuse.
