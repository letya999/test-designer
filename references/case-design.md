# Case design

Use the sections matching the behavior. A test case is an executable specification
of an observation; a list of techniques is not a test plan.

For deeper derivation use [design techniques](design-techniques.md); for contrasting
strong/weak candidates and reusable cards use [quality bank](quality-bank.md).

## Contents

- Derive candidates and select protection
- Ground the expected result
- Choose a faithful level
- Plan observations and mechanics
- Worked designs

## Derive candidates and select protection

Start from the behavior map in [case research](case-research.md). For each relevant
obligation, complete: **If this rule were broken by ___, this setup/action ___ would
produce observable ___ instead of required ___**. If those blanks cannot be filled,
research the contract or observation seam before promoting the idea to a case.

### Separate the path families

Use the main valid journey as the happy path. Side paths are valid alternatives with
different decisions or outcomes: saved versus new input, empty results, an existing
record, another supported role, user cancellation. Unhappy paths exercise documented
refusals or operational failures. Recovery follows the failure or interruption and
checks the subsequent usable state. A label is a navigation aid, not a quota.

Example contract: editors export tenant records, viewers cannot, an empty selection
produces a header-only CSV, storage failure offers retry and preserves the filter.

| Family | Concrete candidate | Observation that matters |
|---|---|---|
| Happy | Editor exports two matching rows among matching/nonmatching and foreign-tenant rows | Exact selected content, no foreign data, valid CSV |
| Alternative | Valid filter matches zero rows | Successful header-only download, not a generic error |
| Alternative | Select saved filter rather than manually entering it | Its actual values reach the operation; UI label alone is insufficient |
| Unhappy | Authenticated viewer submits otherwise valid request | Authorization refusal and no queued work |
| Unhappy + recovery | Storage fails after work starts, then the user retries | Failure shown, no partial download, same filter retained, eventual valid result |

Do not turn this example into mandatory export cases for unrelated features.

### Derive data and sequences

Partition by rules before picking values. For a maximum of 5,000 matched records,
4,999/5,000/5,001 distinguish the accepted boundary from rejection; a typical two-row
case additionally makes content mistakes legible. Use matched count if that is the
contract, not total database size. Partition invalid inputs by different handling,
not every spelling of invalidity. Check empty/missing/zero only where they can arrive.

For an AND authorization rule, vary one guard at a time while satisfying the others:

| Same tenant | Owns record | Required outcome |
|---|---|---|
| Yes | Yes | Allowed control |
| Yes | No | Ownership denial, record unchanged |
| No | Yes | Tenant denial, record unchanged |

The third row is feasible only if ownership and tenancy can differ in the domain.
Otherwise use a valid cross-tenant setup and explain the infeasible combination.
Both-false alone cannot distinguish a missing guard. Add other combinations only
for a distinct interaction, precedence rule, or threat. For OR rules, check each
independently sufficient condition and the neither-condition case.

For states, write **start → event(s) → next state + effects**. Include important
forbidden transitions and repeated events, not every pair of state names. Example:
queued/running → cancel → cancelled and no published artifact; ready → cancel →
rejected with the existing artifact preserved, if that is the contract. A race case
controls which event wins at the publish boundary; arbitrary delays prove little.

### Select without hiding omissions

First match each candidate to existing assertions: KEEP, UPDATE, ADD, or NO_NEW_TEST.
These classify the scenario plan. UPDATE specifies the planned observation/data change
for the writer; it is not a review verdict or an edit to authored test code.
Then order distinct gaps by consequence, likelihood/exposure, recent change, and
diagnostic value. Use the project's priorities; qualitative reasons usually suffice.
Security isolation, data loss, irreversible effects, and known regression witnesses
deserve explicit treatment even in a small change.

Group equivalent rows with shared mechanics. Merge duplicate protection, not distinct
failure causes. Prefer strengthening a weak case to adding a nearly identical case.
Keep a thin end-to-end wiring check where required while moving rule permutations to
faithful lower levels. A limited budget means a visible remaining risk, not fabricated
complete coverage. Name deferred cases, why they can wait, and what would require them.

Case card, adapted to the project's format:

> **UPDATE/ADD — scenario name or existing ID · family · priority reason**\
> Contract/source/status and credible fault; unresolved conflicting sources.\
> Concrete initial state and distinguishing data.\
> Action/sequence → required result and forbidden effects, observed at named boundary.\
> Level/location; real subject and allowed doubles; fixture/environment and
> completion/settling criteria, isolation and cleanup where needed. Unresolved prerequisite.

Do not repeat identical environment notes in every card or require every field for
a trivial case. A proposed test location must be labeled proposed, not discovered.

## Choose cases from the contract

Start with inputs, outputs, effects, denials, and state transitions. Prioritize by
consequence and credible likelihood using the project's scale. Do not invent numeric
risk scores or drop an important outcome because its implementation is small.

| Observed structure | Derive cases | Avoid |
|---|---|---|
| Classes with the same rule | One distinguishing representative per relevant equivalence class | Every value, or arbitrary null/negative inputs impossible at this boundary |
| Ordered threshold | Values just below, at, and above the meaningful boundary, using domain precision | A single far-away example; inventing milliseconds for date-only rules |
| Combined conditions / roles | A compact decision table with feasible combinations and distinct outcomes | All combinations by default; only administrator success |
| Stateful behavior | Starting state → event sequence → permitted or rejected transition → final state/effects | Testing methods separately while missing the sequence |
| Dependency failures | Inject failure at the actual dependency seam; check propagation, retry/cancel, rollback, and residual effects promised by contract | Treating invalid user input as coverage of disk/network/provider failure |
| Retry / concurrency | Control the relevant overlap or response loss; observe uniqueness, ordering, or conservation | Sleeps, probabilistic races, or assuming sequential replay proves contention safety |
| Large valid input domain | Contract-derived properties or a separately justified reference model; generators reach relevant classes and boundaries | A property true for constant/empty output; filters that discard every useful input |
| Configuration/platform matrix | Supported factors, feasible combinations, known interactions, representative coverage | Full Cartesian products or claiming pairwise catches higher-order faults |

Retain known regression witnesses even when a generative or combinatorial approach
is chosen. For parsers or hostile inputs, distinguish documented rejection from crash,
resource exhaustion, or unsafe acceptance. For performance requirements, name the
workload, environment, measured quantity, and existing budget; do not invent an SLO.

## Ground the expected result

An oracle is the source that tells the test what result is correct. Cite it at the
precision needed to implement the case. Hand-worked domain examples, accepted
protocol vectors, and independent models can supply exact values. Shared IDs or
builders are fine; computing expected via the tested implementation is not independent.

For uncertain behavior, separate a characterization case (preserve observed behavior)
from an acceptance case (satisfy an agreed requirement). A bug-fix case may properly
fail on today's implementation. Do not adjust expectations merely to make it green.

Metamorphic relations and round trips need domain justification: two components can
share a bug. Combine a relation with a known independent example when that exposes
the relevant shared error. A no-crash check can be appropriate for robustness, and a
presence or mock-call check can be appropriate when existence or dispatch is the
contract. Judge the promised behavior, not the assertion's length or spelling.

## Choose a faithful level

Use the narrowest existing boundary that contains the fault and permits observing
its consequence. Low cost is useful only after fidelity is established.

| Risk | Typical useful boundary | Evidence it cannot replace |
|---|---|---|
| Pure policy or calculation | Unit/domain test through stable interface | Actual authentication wiring or storage enforcement |
| Component interaction/state | Component or in-process integration | Native OS behavior or real browser layout |
| Serialization/API protocol | Request/response or consumer/provider contract | Business rules absent from schema; deployed wiring |
| Persistence, transaction, query semantics | Integration with relevant real engine/schema | A mock repository or a different engine cannot prove these semantics |
| Browser routing/focus/rendering | Real browser scenario | A DOM simulator cannot establish layout or native browser behavior |
| Mobile lifecycle/permissions | Device/emulator boundary matching the feature | A responsive browser is not a native mobile app |
| Desktop OS/file/process integration | Appropriate native application/OS boundary | A webview screenshot cannot establish IPC or filesystem safety |
| Critical user journey | Thin system/E2E scenario with actual relevant wiring | Repeating the entire domain rule table through UI adds cost without the same diagnostic value |

Similar rules at two levels can be justified by distinct faults: policy logic at
one, wiring at another. Name that difference. Preserve established smoke, contract,
and security checks; coverage overlap alone does not justify replacing them.

## Plan observations and mechanics

Make data distinguish the intended path: different valid source/destination IDs,
non-default amounts, meaningful initial state. Keep other guards valid when testing
one denial. Name the error class or observable refusal rather than accepting any
error. Plan both allowed and denied controls where a broken setup could mimic denial.

Observe persistence via a fresh read through an appropriate independent path, not
the object just returned by a fake. Observe prohibited effects at the actual boundary
and after the operation's meaningful completion point. A zero counter on a different
address, an empty result loop, or a premature observation proves little.

Specify which boundary may be doubled and what remains real. A recording double is
useful for checking exact outgoing fields and failure handling. Identify any separate
integration/contract case needed to establish the double's fidelity. Reuse fixtures;
do not design a new mocking framework or demand removal of all mocks.

Use a controllable clock/scheduler or condition/event-based synchronization for time
and async behavior. Define isolated records/files and cleanup after success or failure.
For long-running work, identify cancellation and partial completion only when they
affect the contract. Use existing tooling; name an unobservable seam as a testability
gap rather than silently refactoring production code.

Follow nearby naming, placement, parameterization, and fixture conventions. One case
should explain one behavioral outcome; it may need several assertions. Group rows
with the same setup/action and different meaningful input partitions without hiding
which row failed. Do not prescribe Python, Go, React, or any runner to an unknown stack.

## Worked designs (illustrative contracts)

**Invitation expiry.** Contract: invalid at `now >= expires_at`. Use a valid actor,
valid invitation, fixed deadline, and the same permitted operation just before and
at expiry. Assert denial at equality and no membership/event if promised. Detects
incorrectly accepting equality; unit policy plus an API wiring case may serve different
risks. Never call the outcome experimentally confirmed before execution.

**Idempotent action.** Contract: retries of one operation reuse a valid key; independent
operations receive distinct keys. UPDATE the existing retry case to assert presence,
valid format, and equality. ADD a distinct-operation case if absent. An integration
case separately checks one durable effect after a lost response and retry. Equality
alone admits two absent keys; a constant key admits accidental cross-operation reuse.

**Authoritative account ID.** Contract: the API result, not a stale client cache,
chooses the account. Use cache ID A and API ID B, both valid. Assert B reaches the
observable result. A recorded API call without this distinction admits code that
performs the call but ignores its result.

**Public bucket protection.** Contract: required access-block flags must be sent.
Record all relevant outgoing flags, not merely the bucket name. If the claim also
includes changing a previously public bucket, design that initial state and an
appropriate integration observation; a recording fake alone proves only dispatch.
