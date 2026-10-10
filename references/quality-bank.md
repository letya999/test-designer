# Candidate quality bank and handoff templates

Use when selecting or sharpening cases. This is a design aid, not a test-code
critic, automatic rejection list, or mandatory checklist. “Red flag” means inspect
the claim and repair the mismatch; a narrow smoke/dispatch/characterization case
can legitimately use an observation insufficient for a broader claim.
The templates implement the selection and oracle principles in
[case design](case-design.md) and [design techniques](design-techniques.md).

## Contents

1. Green flags and red flags
2. Worked repairs
3. Reusable templates
4. Final challenge

## 1. Green flags and red flags

| Green flag: worth protecting | Red flag: weak for the stated claim | Repair or justified exception |
|---|---|---|
| A rule, affected actor and credible fault are explicit | Case chosen because a method exists or to hit a count | Trace obligation; KEEP existing adequate case or NO_NEW_TEST |
| Different valid data make wrong paths distinguishable | Cache and server IDs identical; all amounts zero | Distinct IDs, non-default values, control and decoy records |
| Correct result comes from an independent contract/example | Expected value calculated by the function under test | Hand-worked vector, accepted rule or independent relation |
| Boundary unit and equality are specified | Arbitrary negative number called “boundary coverage” | Nearest representable values at actual inclusive/exclusive edge |
| Denial has valid other guards and an allowed control | Any exception counts; missing fixture causes refusal | Intended error category plus reachable success and unchanged effects |
| Intended output and forbidden effects are observed | HTTP success, toast or mock call used to prove persistence | Read durable state at a faithful boundary; keep dispatch claim narrow |
| Recovery reaches normal usable state | Check error text and stop; force handler invocation afterward | Error -> correction -> normal retry -> actual result and cleared error |
| Relevant event order is controlled | Sleeps until an assumed race occurs | Existing event/barrier seam and final settled observations |
| Properties exclude useful wrong implementations | Round trip only; output length checked without contents | Independent vector, conservation/content and grounded relation |
| Negative observation happens after relevant completion | Assert “no event” before worker starts | Completion/settlement witness, correct effect boundary |
| At least one witness reaches the assertion | Empty loop, conditional return or broad skip yields green | Establish nonempty fixture/domain; explicit unavailable prerequisite |
| Real subject and necessary integration are identified | Stub returns the required answer; real operation never runs | Double dependency only; separate double-fidelity or integration claim |
| Ordinary user action reaches native guard/wiring | Forced click/submit proves real usability | Normal action in capable environment; label narrower handler check |
| Existing assertions are compared before adding | Reworded duplicate tests counted as new protection | UPDATE weak check or ADD a distinct fault; preserve useful gates |
| Scenario names describe meaningful outcomes | Names promise tenant isolation but assert only nonempty data | Foreign and allowed records, exact membership and forbidden data |
| Diagnostic failure explains contract and input row | One giant journey or unlabelled matrix obscures the failure | Separate distinct obligations; share mechanics, label rows |
| Platform matrix is justified by supported behavior | Every OS/browser/version combination or arbitrary pairwise claim | Feasible factors, known interactions and visible exclusions |
| Evidence claim matches completed work | Designed case called passing; compiler never included snippet | State design/static/runtime evidence separately; require real inclusion |

Do not reject snapshots, mocks, no-crash checks, private seams or large cases merely
by syntax. Ask whether they faithfully establish the promised behavior, with an
acceptable maintenance cost. A snapshot may protect a stable artifact contract;
presence may be the precise requirement; robustness may require only no crash.

## 2. Worked repairs

### Paginated search: “returns results” -> “preserves selection across pages”

Contract: stable ordering by timestamp then ID, cursor tied to query, no duplicates
within a stable dataset. Weak: page one is nonempty. Stronger: controlled records
include equal timestamps and nonmatching decoys; request small pages, establish a
nonnull cursor and actual second page, compare exact selected membership and order,
and separately reject old cursor with changed query. Do not assume concurrent-insert
snapshot semantics unless promised. Use database integration for ordering semantics.

### Permission refusal: “throws” -> “correct refusal before effect”

Contract: same-tenant editor can update; viewer and foreign tenant cannot. Weak:
all-invalid request throws. Stronger: valid record and payload, allowed editor
control, viewer with correct tenant, editor with foreign tenant; expected refusal
category and independently read unchanged record. Multiple-invalid rows only when
error precedence is a separate requirement.

### Recovery: “error shown” -> “normal retry succeeds”

Contract: invalid query can be corrected without reloading. Weak: error message,
then direct submit event invokes handler. Stronger: normal submit yields refusal;
edit to a valid distinguishing query; normal submit reaches search and produces the
expected results, stale error cleared. If native form validation is involved, use
a real browser where required. Keep a handler-only case labeled handler-only.

### Idempotency: “same token” -> “one effect for one operation”

Weak: equality of two tokens also passes for two missing values. Stronger: valid
nonempty key, same key on retry, distinct key for distinct operation. This targets
client key handling; a design does not prove its implementation. Server protection
needs a separate durable-effect observation
after lost response or controlled concurrent retry, with payload/key semantics
specified by contract. Never infer concurrent safety from sequential calls alone.

## 3. Reusable templates

Adapt the project's template first. Omit irrelevant fields; never invent values to
fill a template. A small known change can use one paragraph, not every template.

### Behavior and evidence map

```text
Goal / actor / entrypoint:
Obligation and source (accepted, characterized, or unresolved):
Inputs/state -> decisions -> output + durable/forbidden effects:
Existing assertion and fixture witness:
Gap or uncertainty -> next useful read/observation:
```

### Case card

```text
KEEP / UPDATE / ADD / NO_NEW_TEST — scenario name or existing ID; path family
Decision applies to the scenario plan, not an ACCEPT/REVISE verdict on test code.
Contract + risk / credible wrong behavior:
Given: reachable state, discriminating data, valid other guards
When: ordinary action or controlled event sequence
Then: exact required observations + forbidden effects
Oracle source + status: accepted contract / characterization / unknown
Conflicting sources and missing decision, without choosing a winner:
Why it distinguishes the fault / existing protection:
Boundary + proposed/existing location; real subject and dependency doubles:
Completion/settling criteria; environment, synchronization, isolation/cleanup if material:
Unresolved decision / unverified prerequisite:
```

### Boundary worksheet

```text
Rule | domain/unit | inclusive/exclusive endpoints | transformation
Classes and reachable representatives | nearest boundary neighbors
Expected outcome/source | effect observed | fault distinguished
Existing protection | selected additions | omitted rows and reason
```

### Decision or transition worksheet

```text
Decision: conditions + feasible values + constraints -> required actions
Row: values -> outcome/effects; guard/interaction distinguished

Transition: start + event + guards -> next state/effects
Sequence: ordered events + controlled overlap -> intermediate/final observations
Invalid transition/repetition: required refusal + state/effects preserved
Coverage target and intentionally excluded rows/sequences:
```

### Property or relation card

```text
Domain/preconditions and credible faulty implementations:
Generated classes/boundaries, without discarding useful witnesses:
Property OR source input -> transformation -> required relation:
Independent justification + known vector where shared errors matter:
Observation boundary; replay/reduction requirements using existing tooling:
Residual faults this relation cannot distinguish:
```

### Exploration charter and final selection

```text
Explore [surface] with [safe actions/data] to learn [risk/uncertainty].
Observe [result/effects] against [claim/source]; stop at [scope/condition].
Observed / inferred / unknown:
Finding -> minimal reproduction -> proposed case + faithful level:

Selected KEEP/UPDATE/ADD, each with distinct protection:
Deferred / excluded + reason + trigger for revisiting:
Decisions needed, environment gaps, next phase and evidence limits:
```

## 4. Final challenge

Mentally replace the implementation with a plausible defect: missing guard, wrong
identity source, off-by-one threshold, constant/empty output, dropped write, sticky
state, duplicate effect or late response. Would the proposed observation distinguish
it? This is a design challenge, not a claim that a mutation was run or killed.

For each case ask: can setup reach it, does the action preserve real semantics,
is the expectation grounded, is the observation made at the right time/boundary,
and does this add protection beyond existing assertions? Retain a case whose narrow
claim is valuable. Strengthen or discard one that promises more than it can prove.
