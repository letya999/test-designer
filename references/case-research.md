# Research behavior before selecting cases

Use for an unfamiliar feature, incomplete requirements, broad planning, or a regression
whose neighboring failure modes are unclear. For a narrow known behavior, use the
same questions briefly instead of performing a full product investigation.

## Contents

1. Define the scope and gather evidence
2. Trace a behavior and its obligations
3. Investigate happy, alternative, unhappy and recovery paths
4. Compare with existing protection
5. Resolve uncertainty and stop researching

## 1. Define the scope and gather evidence

Identify the actor's goal, changed behavior, entrypoints, affected consumers and
important assets. Use business wording: “export only this tenant's filtered orders,”
not “test ExportService.” Determine whether this is new behavior, bug regression,
unchanged behavior during refactoring, or deliberate characterization of legacy code.

State exclusions already established by the user or project. Do not turn one feature
into a full security/performance/accessibility audit, but include those risks where
this feature crosses their boundaries. A small implementation can have a large impact.

### Evidence sources and the next useful read

| Source | Extract | Follow up when |
|---|---|---|
| Task, acceptance examples, active specs, accepted decisions | Promised outcomes, constraints, supported actors/states | Terms or outcomes disagree; exact boundary is undefined |
| Product flows, designs, supplied screenshots | User goal, alternate entrypoints, visible state and recovery intent | Behavior depends on navigation, focus, persistence or a state not shown |
| Real entrypoint and callers | Reachable inputs, transformations, permissions and validation order | An assumed bad input is already impossible, or a caller bypasses a guard |
| Domain logic and dependencies | Decisions, transitions, side effects, partial completion points | Failure can happen after one effect but before another |
| Existing tests/fixtures/helpers/config | Actual assertions/data, doubles, selection | Test name promises more than observed result; setup hides the branch |
| In-scope bug/support report or approved history | Reproduction, impact, related failure class | Root cause can recur at another entrypoint/state; report lacks reproduction |
| Existing logs/traces | Observed sequence/environment and build identity | Timeout is mistaken for rejection, or “passed” excludes a lane |
| External docs/standards | Version-specific semantics or normative protocol expectations | Local evidence cannot resolve a technical question affecting design |

Access issues, history and external systems within the user's scope and project rules.
Search the web to answer a specific unresolved technical question, not to import a
generic “top 100 test cases” list. External examples are ideas until grounded in this
product. Avoid sending private source/data to external search or documentation tools.

Use targeted searches for domain terms, entrypoints, callers, effect-producing methods,
error classes and assertions. Read surrounding code after a hit; snippets can miss
guards, cleanup, and failure handling. Keep material evidence as short source notes
in the design, not a second permanent knowledge base.

## 2. Trace a behavior and its obligations

Build a small internal map; show it only if it helps the reader:

`actor + starting state → entry/action → decisions → dependency/effect → final observation`

For a long-running flow, map intermediate states too. Inspect both success and points
where the outcome diverges. Questions that change case selection:

- Who may do this, to whose object, at which tenant/ownership boundary?
- Which inputs select different rules? Which are transformed/defaulted before use?
- What state or previous action changes whether this operation is valid?
- What must be returned, persisted, emitted, rendered or explicitly *not* done?
- Where can acknowledgement be lost, work partially complete, or another actor intervene?
- What must remain usable/preserved after rejection, cancellation or retry?
- Which client/runtime differences affect the outcome rather than merely appearance?

Turn each distinct obligation into a candidate before consulting coverage totals.
This prevents the existing suite from defining the entire search space. Then inspect
existing checks to remove redundant candidates, not retrofit requirements to tests.

### Look beyond the happy-path implementation

Read sibling branches, public callers and dependent effects in the touched flow.
For a bug, retain its exact witness and look for the same mistaken assumption at a
nearby boundary: empty vs absent, retry vs independent action, same vs foreign tenant,
before vs at a deadline, memory vs durable storage. Extend only where that root cause
or contract applies; avoid inventing unrelated “edge cases.”

Without implementation, derive acceptance obligations from the contract and intended
integration boundaries. Mark placement/seams proposed; do not pretend call-chain research
happened. Without a contract, identify characterization scope or ask for the missing
behavior before assigning a correctness oracle.

## 3. Investigate scenario families

Family labels aid thinking; they are not a quota or severity scale. Use one primary
label per case and a boundary/sequence tag only when helpful.

| Family | Research question | Example | Usual observation |
|---|---|---|---|
| **Happy** | What is the representative intended success? | Editor exports ordinary matching orders | Correct output, durable effects, relevant user feedback |
| **Alternative (side)** | What supported route or valid state changes the flow? | Saved filter; zero matching orders; cancel by choice | Equivalent result or a different explicitly valid final state |
| **Unhappy** | What denial, invalid request, dependency failure or interruption needs handling? | Viewer export; invalid range; storage failure | Specific refusal/error and preserved/absent effects |
| **Recovery** | After failure/interruption, how does work safely proceed? | Retry after lost acknowledgement; resume draft | No duplication/loss, consistent state and usable next action |

Separate a valid empty state from an error. Distinguish cancellation from dependency
failure even if both show “no download.” A valid alternate path is not less important
merely because it is uncommon. A happy path is not automatically already covered.
Recovery can follow an unhappy or alternative path.

### Search prompts for each family

**Happy:** choose realistic non-default inputs and the intended actor/state. What
complete outcome matters beyond HTTP success or button visibility? Is required data
preserved and routed to the correct destination?

**Alternative:** inspect optional fields, existing vs new data, saved/default/manual
choices, empty results, alternate entrypoints, allowed roles, edit/back/cancel,
refresh/reopen, localization or device differences *actually supported*. Select a
variant only for a distinct rule, path, state transition or platform risk.

**Unhappy:** separate invalid input, domain rejection, authentication/authorization,
dependency errors, resource/limit boundaries, and interruptions. Trace where each
is detected and what may already have happened. For each denial keep other guards
valid; otherwise the test can pass without reaching the intended rule.

**Recovery:** inspect what survives timeout, retry, navigation, process recreation,
rollback or reconnect. “Retry succeeds” is incomplete if the first attempt committed
and retry duplicates an effect. Use a sequence and identify its settling point.
Design it when the product promises or relies on recovery.

Do not stop at “add errors and edge cases.” Turn relevant prompts into concrete
input/state/action and expected observation, or identify the missing decision.

## 4. Compare candidates with existing protection

Read assertions and data at the actual boundary. Classify current protection as adequate,
weak, absent, or unknown. These are source-based design judgments unless matching
execution evidence exists; they are not mutation-test results.
They inform scenario selection, not ACCEPT/REVISE verdicts on authored tests or
claims of proven stability/sensitivity. UPDATE here changes the plan for the writer.

| Question | Effect on the plan |
|---|---|
| Could the existing test pass while this obligation is violated? | Name the witness; strengthen data/assertion or add the distinct case |
| Does a caller-level assertion already observe the change? | Keep it; absence of direct helper tests alone is not a gap |
| Is the boundary named in the claim mocked? | Preserve narrower value; identify the integration guarantee still missing |
| Is the case unselected in the relevant lane? | Record enrollment/execution gap instead of duplicating the case |
| Do two levels detect different faults? | Keep both with separate rationale, e.g. policy vs wiring |
| Would one new parameter row add the distinction? | UPDATE the existing table instead of adding an abstraction |

## 5. Resolve uncertainty and stop researching

For a material unknown, state: evidence → unresolved choice → affected cases → the
smallest question/artifact that resolves it. Continue independent cases. Example:
support reports filters disappear on reopening, while the spec says “retain for retry.”
Confirm whether retry includes reopening before declaring that acceptance result;
still design in-place retry preservation now.

Stop when selected behavior has traceable expectations, relevant scenario families
have been considered, important current protection is accounted for, and each proposed
case has a usable level/environment or named blocker. Disclose remaining unknowns
instead of certifying completeness or researching indefinitely.

Hand candidate obligations and sources to case-design.md. The deliverable is a design,
not the research chronology, copied specification, or list of every technique considered.
