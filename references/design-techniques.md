# Techniques for deriving meaningful cases

Read only sections matching the feature. These techniques expand the existing
behavior map; they do not authorize execution, new tools, or additional scope.
Examples below assume illustrative contracts, not universal product requirements.
See [sources](sources.md) for the foundations and reading limits behind these techniques.

## Contents

1. Rules, partitions, and boundaries
2. Decisions and combinations
3. States, sequences, and interruptions
4. Properties, models, and uncertain oracles
5. Exploration and coverage claims
6. Worked cross-platform example

## 1. Rules, partitions, and boundaries

Define a **test condition** (an obligation to investigate) before a concrete case.
For “at most 100 selected records,” the condition is inclusive selected-count
enforcement; cases supply counts and observable acceptance/refusal. Count cases,
conditions, branches, and risks separately: none is a substitute for the others.

An equivalence class groups values expected to receive the same treatment **for a
particular rule**. A valid identifier may still belong to different ownership
classes. One representative per input field does not cover combinations of fields.
Partition outputs and effects too: zero/one/many results, complete/partial work,
first/subsequent page, no/one/repeated notification, where these outcomes exist.

For ordered domains identify each actual boundary, inclusivity, and nearest
representable neighbors. With integers 1..100, consider 0/1/2 and 99/100/101 when
the corresponding faults matter. Interior values help expose content mistakes.
Do not claim exhaustive boundary coverage from whichever three values are handy.
Continuous values need the contract's precision and rounding; “epsilon” is not a
business unit. Compare the raw and normalized boundary when transformation matters.

### Boundary lenses: select relevant rows, then derive exact cases

| Lens | Questions that change the design | Useful distinction |
|---|---|---|
| Presence and cardinality | Is missing different from null, blank, zero or empty? Are they reachable? | Defaulting vs explicit clearing; zero vs one vs maximum supported items |
| Representation | Is length measured in bytes, code points, graphemes or records? Is normalization promised? | Same visible text with different encoding; limit before/after normalization |
| Numeric | What are unit, sign, precision, rounding and overflow rules? | Exact threshold; rounding crossover; valid large value vs overflow refusal |
| Time | Which clock, timezone and inclusive endpoint apply? Is this a date or instant? | Expiry equality; calendar change or DST only where local-calendar rules matter |
| Identity and authority | Which source controls identity, role or consent? Can cached state be stale? | Different valid IDs; revocation after initial permission check |
| Collections and navigation | What defines order, ties and snapshot membership? | Duplicate sort keys across pages; changed query with old cursor |
| Resources and lifecycle | Where can allocation, persistence, response or teardown fail? | Failure before commit vs commit followed by lost acknowledgement |
| Platforms and accessibility | Which native behavior does the requirement depend on? | Real keyboard/focus, OS permission, lifecycle event vs simulated handler |

“Edge case” means an unusual but relevant rule, state, representation, or interaction.
It does not mean a mandatory list of null, negative, Unicode and million-row inputs.
State the reason a chosen edge is plausible and the distinct wrong result it exposes.

## 2. Decisions and combinations

Use a decision table when several conditions determine outcomes. List conditions,
their feasible values, resulting actions, and constraints. Mark impossible rows
with a reason; do not create impossible fixtures to achieve a combinatorial count.
Treat an unknown condition as unknown, not automatically false.

For `owner AND active`, use allowed `(true,true)` and denials `(false,true)` and
`(true,false)` to expose either missing guard. `(false,false)` adds value only for
an interaction or error-precedence rule. For `owner OR delegated`, cover each
independently sufficient condition and neither. If error precedence matters, a
multiple-invalid case is appropriate **after** isolating individual rules.

For a safety-critical independence claim, condition influence may need more rigor
than these examples; follow the project's mandated criterion (such as MC/DC).
Branch execution alone does not prove the decision produced a correct effect.

### Pairwise and higher-order interaction selection

Use constrained combinatorial coverage for meaningful factors such as supported
client, role, authentication mode and transport. Define factor values as behavior
classes, not every raw value. Choose an interaction strength based on credible
faults and project obligations; pairwise is an economy technique, not a guarantee.

Example: permission depends on **role + tenant + document state**. That known
three-factor rule needs explicit cases even if a two-way platform matrix exists.
Keep known regression witnesses and boundary rows alongside generated combinations.
Name which combinations are covered and excluded; never call a manually chosen
small set “pairwise complete” without checking its actual feasible pair coverage.
Order-sensitive sequences need a sequence model, not an unordered covering array.

## 3. States, sequences, and interruptions

Model only relevant states, including hidden state with externally visible effects.
Write `pre-state + event + guards -> post-state + effects`. Distinguish state,
transition, transition-pair, and longer-sequence coverage. Visiting every state
does not cover every transition; covering each transition once does not establish
every sequence. Target the sequences suggested by history dependence and risk.

High-value patterns where supported:

- First use vs reuse; create -> edit -> save -> reload from an independent source.
- Invalid attempt -> correction -> normal retry -> successful durable result.
- Success -> next operation with changed input: no sticky role, cursor or consent.
- Start -> cancel -> completion arrives: late result cannot revive cancelled work.
- Disconnect/background/process restart -> resume: permitted recovery and residual data.
- Two consumers update the same version: conflict behavior and absence of lost writes.

For async behavior locate the **commit/publication boundary** and decide ordering.
Failure before an effect, after an effect, and after commit before acknowledgement
can require different recovery. Model duplicate delivery, stale/late responses and
out-of-order events when the protocol permits them. Sequential replay proves replay
behavior; it cannot establish safety of concurrent overlapping requests.

Design a controlled schedule using an existing event/barrier/clock seam. Observe
the completion relevant to the claim. For “no duplicate charge,” check durable
charges after both attempts settle, not just a client button or mock call count.
For eventual consistency, specify the promised convergence condition and deadline
source; distinguish legitimate intermediate states from prohibited states.

### Faithful actions are part of the case

A direct handler call, forced form submit, bypassed disabled control or mocked OS
permission can skip the guard responsible for the real behavior. Such a test can
prove handler logic if labeled accordingly. For a user journey, use normal actions
and a boundary that supports native behavior. A form recovery case must edit the
invalid value and activate normal submission: directly dispatching a submit event
can hide stale native validation. Do not prescribe a particular browser library.

## 4. Properties, models, and uncertain oracles

Choose exact examples when results can be independently specified. Use properties
for large domains only with a justified relation and useful generated inputs.

| Approach | Design obligations | Typical trap |
|---|---|---|
| Contract invariant | Define valid domain, invariant, observation point and assumptions | “Never throws” replaces required correctness |
| Property-based examples | Specify generator classes/boundaries, preconditions and replay/shrink needs | Constant output satisfies a weak property; all interesting inputs filtered out |
| Metamorphic relation | Define source input, transformation, relation and why it holds | Order assumed irrelevant although ranking depends on it |
| Reference model | Use a simpler independently justified model for selected behavior | Copying production algorithm, constants and errors into expected output |
| Differential comparison | Establish independence and explain how disagreements are adjudicated | Two implementations agree on the same bug; old version declared authoritative |
| Characterization | Label behavior preservation and its limits | A current defect is promoted into an accepted product rule |

For sorting, “output ordered” admits empty output. Combine ordering with multiset
preservation; use a known vector to challenge comparator semantics. For a set-valued
filter without order-sensitive semantics, permuting inputs should preserve selected
members. Applying the same relation to a ranked or paginated output may be invalid.
For serialization, round-trip equality needs canonicalization rules and independent
known vectors; encoder and decoder can share the same incorrect interpretation.

Include empty, singleton, repeated and nontrivial values only where they distinguish
faults. Preserve small known regression witnesses even when generators are used.
Specify replay information and failure reduction for later implementation using
existing tooling. Do not introduce a mandatory property-testing dependency.

When no exact oracle exists, propose justified partial checks and human evaluation
criteria. Label the remaining uncertainty. Do not invent an expected answer, use
another model's answer as ground truth, or claim that consistency proves correctness.

## 5. Exploration and coverage claims

Use exploration to learn missing behavior, not merely replay the happy path. A
focused charter names feature, uncertainty/risk, safe actions, observations, and a
stop condition. While exploring, adapt the next action to what was learned. Keep
observed facts separate from hypotheses; a screenshot establishes one observed
state, not correctness of every preceding step. Follow [UI exploration](ui-exploration.md).

Inspect product claims, inputs and transformations, state and dependencies, outputs
and artifacts, users and permissions, supported environments, and quality concerns
relevant to the feature. Vary one factor to diagnose a suspected cause; combine
factors when investigating an interaction. Reproduce a finding before describing
it as confirmed; if no live environment exists, return a proposed charter.

Coverage is always **of something**: rules, partitions, transitions, supported
configurations, branches or examples. Name the denominator and evidence available.
Source coverage can reveal unvisited code but cannot establish a correct oracle or
missing requirements. A mental mutation (“what if this guard vanished?”) challenges
the design; it is not an executed mutation or proof of detection.

Stop when relevant conditions have adequate existing/proposed protection, important
uncertainties are exposed, and additional rows add no useful distinction. Also stop
at the authorized exploration limit; record the residual risk rather than equating
a finished checklist with absence of defects.

## 6. Worked cross-platform example

Illustrative contract: users save a draft locally; retries preserve content; a
server rejection preserves edits; a save clears dirty state only when it successfully
saves the current edit revision.

1. Partition new/existing draft and unchanged/changed content. KEEP existing success
   checks if they already observe stored content, not only a success notification.
2. Derive `invalid -> error -> edit -> normal save -> reload`: UPDATE recovery
   coverage that bypasses ordinary submission. Observe actual revised content.
3. Derive save A then edit B before A completes. A's late success must not clear B's
   dirty state. Control responses; assert state and final stored content per contract.
4. Distinguish refusal before commit from lost acknowledgement after commit. Design
   retry expectations from the actual idempotency contract; do not assume one exists.
5. Use domain/component checks for state permutations, storage integration for
   persistence semantics, and a thin native-client journey for action/lifecycle wiring.

Web, CLI, mobile and desktop share the obligations, but their action and observation
boundaries differ. Background suspension belongs to a native lifecycle boundary;
a CLI process exit belongs to the process boundary. Similar logic is not evidence
that one client's test proves another client's wiring.
