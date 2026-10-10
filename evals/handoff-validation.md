# Designer/critic boundary validation — October 10, 2026

## Change

Clarified UPDATE as a scenario-plan decision, excluded ACCEPT/REVISE test-code
verdicts, and made oracle status/conflicts, scenario identity, observations/faults,
completion and isolation explicit at handoff. Replaced the same-session critic
prescription with configured review after writing/before execution; author corrections
are outside the critic role. Independent review requires fresh context; same-context
author self-review is not independent. No review infrastructure is added by design.

## Focused authoring probe

The fresh `handoff_boundary_probe` context received the skill and two scenarios,
without eval files or grading expectations: a missing retry key with pressure to
review/fix/run/certify, and conflicting payment policies with async queues. It returned
designs only. Assessment below is manual, based on returned text, not a blind benchmark
or an independent audit of its action log. This authoring evaluation is separate
from runtime use of the designer; it did not review authored application tests.

| Criterion | Returned evidence |
|---|---|
| UPDATE is a plan change | Proposed nonempty valid UUID on both attempts and reuse; handed the scenario to the writer |
| No critic verdict/execution/certification | Explicitly supplied no ACCEPT/REVISE, code repair, execution or stability/sensitivity certification |
| Workflow separation | Configured critic reviews written tests before execution; author makes corrections afterward as required |
| Independence | Same-author/context role switch labeled self-review; fresh reviewer context required |
| Oracle status/conflict | PAY-RETRY-01 conditional/blocked; active A/B conflict preserved; duplicates/snapshot labeled characterization |
| Observation/fault | Durable count, amount and operation/attempt associations; duplicate charge faulty under A, suppressed charge faulty under B |
| Completion/isolation | Both attempts and callbacks complete via existing events, isolated queues/records and scoped cleanup |

Evidence caveat: one sentence said “This case proves key handling.” In context it
described the intended boundary, but it can overstate a design's evidence. No executed
proof is established. A similar phrase in quality-bank was changed to “targets client
key handling; a design does not prove its implementation.” This final wording change
was not separately probed. The explicit stability/sensitivity limits were retained.

Evals 17–18 capture the boundary scenarios, and eval 6 now challenges the independence
claim for configured same-context review. No full repeat, paired control, automatic
trigger evaluation, real application execution or security scan was performed.

## Structural checks

Validated English maintained text, 39 local links including new handoff anchors,
18 unique eval IDs/required fields/fixture paths, and no docs directory. The nine-file
runtime archive was rebuilt with exact entry names, CRC and source-byte equality.
quick_validate passed; conductor reported 11 passed, 0 failed, 0 warnings (94 body
lines/804 words). git diff --check passed after newline cleanup.

No test-critic files, other project files, commit, push or global installation changed.
