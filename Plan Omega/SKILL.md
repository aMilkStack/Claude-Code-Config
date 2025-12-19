---
name: plan-omega
description: Use after plan-critique to consolidate improvements, validate dependencies, and create the final execution-ready plan. Third and final stage of the three-round planning system. Always preceded by plan-alpha and plan-critique.
---

# Plan Omega: Final Optimisation

## Overview

Final round of the three-round planning system. Consolidates the alpha plan with critique findings into an execution-ready plan with validated assumptions, optimised ordering, and clear implementation handoff.

**Announce at start:** "Starting Plan Omega - Round 3 of 3. Consolidating into final execution-ready plan."

**This skill is part of a chain:**
1. **plan-alpha** → Initial comprehensive plan
2. **plan-critique** → Critique, edge cases, alternatives
3. **plan-omega** (you are here) → Final optimisation and execution prep

## When to Use

- After plan-critique completes
- When both alpha and critique documents exist
- Before implementation begins

**Prerequisites:**
- Alpha plan at `docs/plans/YYYY-MM-DD-[feature]-alpha.md`
- Critique at `docs/plans/YYYY-MM-DD-[feature]-critique.md`
- Or both provided in conversation

## The Consolidation Process

### Step 1: Merge Inputs

Systematically integrate critique findings:

```
CONSOLIDATION CHECKLIST:
□ Load alpha plan
□ Load critique report
□ For each "Must Change" → Apply to plan
□ For each "Should Change" → Apply or justify skip
□ For each "Consider" → Decide and document
□ Verify all critical edge cases handled
□ Verify high-risk assumptions mitigated
□ Apply redundancy removals
□ Update dependency graph
```

### Step 2: Assumption Validation

Every assumption must be resolved:

```
ASSUMPTION RESOLUTION:
For each assumption from critique:

Status: VALIDATED
├── Evidence: [What proves this]
└── Confidence: High

Status: MITIGATED
├── Risk: [What could go wrong]
├── Mitigation: [How we handle it]
└── Fallback: [If mitigation fails]

Status: ACCEPTED
├── Risk: [Acknowledged uncertainty]
├── Rationale: [Why we proceed anyway]
└── Review trigger: [When to revisit]

Status: REMOVED
└── Change: [How plan changed to eliminate assumption]
```

**No assumption remains "Unknown" in omega plan.**

### Step 3: Dependency Validation

Lock down the execution graph:

```
DEPENDENCY FINALISATION:
┌─────────────────────────────────────────────┐
│ HARD DEPENDENCIES (Blocking)                │
│ Task X CANNOT start until Task Y complete   │
│ - Verify: Is this actually true?            │
│ - If false: Remove dependency               │
├─────────────────────────────────────────────┤
│ SOFT DEPENDENCIES (Preferred)               │
│ Task X SHOULD wait for Task Y               │
│ - Verify: What's lost if we don't wait?     │
│ - Decision: Enforce or relax                │
├─────────────────────────────────────────────┤
│ PARALLEL OPPORTUNITIES                      │
│ Tasks that CAN run simultaneously           │
│ - Identify: All parallelisable work         │
│ - Resource: Can we actually parallelise?    │
├─────────────────────────────────────────────┤
│ CRITICAL PATH                               │
│ The minimum sequence to completion          │
│ - Calculate: Actual critical path           │
│ - Optimise: Any way to shorten?             │
└─────────────────────────────────────────────┘
```

### Step 4: Task Refinement

Transform tasks into implementation-ready form:

```
TASK REQUIREMENTS:
Each task MUST have:
□ Specific action (verb + object)
□ Clear done criteria
□ Estimated duration
□ Required inputs
□ Expected outputs
□ Verification method

GOOD: "Create UserAuth service with login/logout methods, unit tests, returns JWT on success"
BAD: "Implement authentication"

TASK SIZING:
- Ideal: 30 mins - 2 hours per task
- Too big: Break into subtasks
- Too small: Combine with related
```

### Step 5: Risk Finalisation

All risks from critique must be addressed:

```
RISK MATRIX (Final):
┌────────────────┬────────────┬────────────┬────────────┐
│                │ Low Impact │ Med Impact │ High Impact│
├────────────────┼────────────┼────────────┼────────────┤
│ High Likelihood│  Monitor   │  Mitigate  │  CRITICAL  │
│ Med Likelihood │  Accept    │  Mitigate  │  Mitigate  │
│ Low Likelihood │  Accept    │  Accept    │  Monitor   │
└────────────────┴────────────┴────────────┴────────────┘

For CRITICAL risks:
□ Mitigation is in the plan as explicit task
□ Fallback is defined if mitigation fails
□ Early warning indicators identified
```

### Step 6: Confidence Assessment

Rate the final plan:

```
PLAN CONFIDENCE SCORECARD:
                                    Score (1-5)
Goal clarity                        [  ]
Task specificity                    [  ]
Dependency accuracy                 [  ]
Risk coverage                       [  ]
Assumption validation               [  ]
Resource availability               [  ]
Timeline realism                    [  ]
                            Total:  [  ]/35

Interpretation:
30-35: High confidence, execute with minimal oversight
25-29: Good confidence, normal oversight
20-24: Moderate confidence, closer monitoring
<20:   Low confidence, consider another critique round
```

## Omega Plan Document Structure

```markdown
# [Feature/Task Name] - Omega Plan (Final)

**Status:** APPROVED FOR EXECUTION
**Created:** [timestamp]
**Rounds Completed:** 3 of 3
**Confidence Score:** [X]/35

> **For Implementation:** Use superpowers:writing-plans to generate implementation tasks, OR superpowers:executing-plans if detailed tasks below are sufficient.

---

## Goal
[Crystal clear, measurable success criteria]

## Approach (Final)
[Chosen approach after critique refinement]

**Key Design Decisions:**
1. [Decision 1] - Because [rationale]
2. [Decision 2] - Because [rationale]

---

## Execution Plan

### Phase 1: [Name] - [Duration Estimate]

**Objective:** [What this achieves]
**Parallel Opportunities:** [What can run alongside]

| # | Task | Duration | Depends On | Verification |
|---|------|----------|------------|--------------|
| 1.1 | [Specific action] | [time] | - | [How to verify done] |
| 1.2 | [Specific action] | [time] | 1.1 | [How to verify done] |

**Phase Exit Criteria:**
- [ ] [Measurable criterion]
- [ ] [Measurable criterion]

### Phase 2: [Name] - [Duration Estimate]
[Same structure...]

---

## Critical Path

```
[Task 1.1] → [Task 1.3] → [Task 2.1] → [Task 2.4] → [Done]
     ↘ [Task 1.2] ↗           ↘ [Task 2.2] ↗
                               ↘ [Task 2.3] ↗
```

**Minimum Duration:** [calculated from critical path]

---

## Risk Register (Final)

| Risk | Likelihood | Impact | Mitigation | Fallback | Owner |
|------|------------|--------|------------|----------|-------|
| [Risk] | H/M/L | H/M/L | [Strategy] | [If fails] | [Who] |

---

## Assumptions (Validated)

| Assumption | Status | Evidence/Mitigation |
|------------|--------|---------------------|
| [Assumption] | ✅ Validated | [Evidence] |
| [Assumption] | ⚠️ Mitigated | [Mitigation in place] |
| [Assumption] | 🤝 Accepted | [Rationale for proceeding] |

---

## Edge Cases Handled

| Edge Case | Handling | Task Reference |
|-----------|----------|----------------|
| [Edge case] | [How handled] | Task X.Y |

---

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| [Metric] | [Value] | [How measured] |

---

## Rollback Plan

If implementation fails:
1. [Rollback step 1]
2. [Rollback step 2]
3. [Communication/escalation]

---

## Sign-off

- [ ] Plan reviewed against original requirements
- [ ] All critique items addressed
- [ ] Dependencies validated
- [ ] Risks mitigated or accepted
- [ ] Ready for implementation
```

## Output Location

Save omega plan to: `docs/plans/YYYY-MM-DD-[feature]-omega.md`

Optionally archive alpha/critique or keep for audit trail.

## Handoff to Implementation

After completing omega plan:

**Say:** "Omega plan complete. Confidence score: [X]/35. Ready for implementation."

**Offer implementation paths:**

1. **Detailed Implementation Plan**
   - **REQUIRED SKILL:** Use writing-plans to generate step-by-step implementation tasks
   - Best for: Complex features, team handoff, junior developers

2. **Direct Execution**
   - **REQUIRED SKILL:** Use executing-plans to implement from omega plan
   - Best for: Straightforward features, solo work, experienced developer

3. **Subagent Execution**
   - **REQUIRED SKILL:** Use subagent-driven-development for parallel task execution
   - Best for: Independent tasks, faster iteration

**Ask:** "Which implementation approach suits this work?"

## Integration with Other Skills

**Prerequisite skills:**
- **plan-alpha** - REQUIRED - initial plan
- **plan-critique** - REQUIRED - critique findings

**Handoff skills:**
- **writing-plans** - For detailed implementation tasks
- **executing-plans** - For direct execution
- **subagent-driven-development** - For parallel execution
- **using-git-worktrees** - For isolated implementation workspace

**Complementary skills:**
- **verification-before-completion** - Verify implementation matches plan
- **test-driven-development** - Implementation approach for tasks

## Key Principles

- **Consolidate, don't create** - Merge existing work, don't restart
- **Resolve, don't defer** - Every uncertainty gets a decision
- **Concrete over abstract** - Implementation-ready specificity
- **Confidence-rated** - Know how sure you are
- **Exit-ready** - Plan can be handed to any competent implementer

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Incomplete merge | Critique items ignored | Checklist each critique item |
| Over-engineering | Plan grew during omega | Omega consolidates, doesn't expand |
| Vague tasks | "Implement feature" style | Rewrite with specific actions |
| Unresolved assumptions | "TBD" or "Unknown" remains | Force decision or mitigation |
| False confidence | High score, low rigour | Honest self-assessment |

## The Three-Round Summary

```
┌─────────────────────────────────────────────────────────────┐
│  PLAN-ALPHA          PLAN-CRITIQUE        PLAN-OMEGA       │
│  ───────────         ─────────────        ──────────       │
│  Generate            Challenge            Consolidate       │
│  Explore             Break                Validate          │
│  Structure           Find gaps            Finalise          │
│  Draft mindset       Adversarial          Execution-ready   │
│                                                             │
│  Output:             Output:              Output:           │
│  Initial plan        Critique report      Final plan        │
│  with uncertainty    with findings        with confidence   │
└─────────────────────────────────────────────────────────────┘

Total time investment: 30-60 mins for significant features
ROI: Catches 60-80% of issues before implementation begins
```
