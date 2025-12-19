---
name: plan-final
description: "Consolidate initial plan with review findings into execution-ready plan (Round 3 of 3)"
category: orchestration
complexity: advanced
mcp-servers: [sequential, context7, serena]
personas: [architect, project-manager]
---

# /sc:plan-final - Final Plan Consolidation (Round 3/3)

## Triggers
- After /sc:plan-review completes
- When both initial plan and review exist
- Before implementation begins

## Usage
```
/sc:plan-final [plan-file] [review-file] [--execute] [--taskmaster]
```

## Three-Round Planning System
```
/sc:plan --> /sc:plan-review --> /sc:plan-final (you are here)
  Generate      Challenge           Consolidate
  Explore       Break               Validate
  Structure     Find gaps           Finalize
  Draft         Adversarial         Execution-ready
```

## The Consolidation Process

### Step 1: Merge Inputs
Systematically integrate review findings:

```
CONSOLIDATION CHECKLIST:
- Load initial plan
- Load review report
- For each "Must Change" -> Apply to plan
- For each "Should Change" -> Apply or justify skip
- For each "Consider" -> Decide and document
- Verify all critical edge cases handled
- Verify high-risk assumptions mitigated
- Apply redundancy removals
- Update dependency graph
```

### Step 2: Assumption Validation
Every assumption must be resolved:

```
ASSUMPTION RESOLUTION:
For each assumption from review:

Status: VALIDATED
  - Evidence: [What proves this]
  - Confidence: High

Status: MITIGATED
  - Risk: [What could go wrong]
  - Mitigation: [How we handle it]
  - Fallback: [If mitigation fails]

Status: ACCEPTED
  - Risk: [Acknowledged uncertainty]
  - Rationale: [Why we proceed anyway]
  - Review trigger: [When to revisit]

Status: REMOVED
  - Change: [How plan changed to eliminate assumption]
```

**No assumption remains "Unknown" in final plan.**

### Step 3: Dependency Validation
Lock down the execution graph:

```
DEPENDENCY FINALIZATION:
+---------------------------------------------+
| HARD DEPENDENCIES (Blocking)                |
| Task X CANNOT start until Task Y complete   |
| - Verify: Is this actually true?            |
| - If false: Remove dependency               |
+---------------------------------------------+
| SOFT DEPENDENCIES (Preferred)               |
| Task X SHOULD wait for Task Y               |
| - Verify: What's lost if we don't wait?     |
| - Decision: Enforce or relax                |
+---------------------------------------------+
| PARALLEL OPPORTUNITIES                      |
| Tasks that CAN run simultaneously           |
| - Identify: All parallelizable work         |
| - Resource: Can we actually parallelize?    |
+---------------------------------------------+
| CRITICAL PATH                               |
| The minimum sequence to completion          |
| - Calculate: Actual critical path           |
| - Optimize: Any way to shorten?             |
+---------------------------------------------+
```

### Step 4: Task Refinement
Transform tasks into implementation-ready form:

```
TASK REQUIREMENTS:
Each task MUST have:
- Specific action (verb + object)
- Clear done criteria
- Required inputs
- Expected outputs
- Verification method

GOOD: "Create UserAuth service with login/logout methods, unit tests, returns JWT"
BAD: "Implement authentication"

TASK SIZING:
- Ideal: 30 mins - 2 hours per task
- Too big: Break into subtasks
- Too small: Combine with related
```

### Step 5: Confidence Assessment
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
                            Total:  [  ]/30

Interpretation:
25-30: High confidence, execute with minimal oversight
20-24: Good confidence, normal oversight
15-19: Moderate confidence, closer monitoring
<15:   Low confidence, consider another review round
```

## Final Plan Document Structure

```markdown
# [Feature/Task Name] - Final Plan

**Status:** APPROVED FOR EXECUTION
**Created:** [timestamp]
**Rounds Completed:** 3 of 3
**Confidence Score:** [X]/30

---

## Goal
[Crystal clear, measurable success criteria]

## Approach (Final)
[Chosen approach after review refinement]

**Key Design Decisions:**
1. [Decision 1] - Because [rationale]
2. [Decision 2] - Because [rationale]

---

## Execution Plan

### Phase 1: [Name]

**Objective:** [What this achieves]
**Parallel Opportunities:** [What can run alongside]

| # | Task | Depends On | Verification |
|---|------|------------|--------------|
| 1.1 | [Specific action] | - | [How to verify] |
| 1.2 | [Specific action] | 1.1 | [How to verify] |

**Phase Exit Criteria:**
- [ ] [Measurable criterion]

### Phase 2: [Name]
[Same structure...]

---

## Critical Path
```
[Task 1.1] -> [Task 1.3] -> [Task 2.1] -> [Done]
```

---

## Risk Register (Final)

| Risk | L | I | Mitigation | Fallback |
|------|---|---|------------|----------|
| [Risk] | H/M/L | H/M/L | [Strategy] | [If fails] |

---

## Assumptions (Validated)

| Assumption | Status | Evidence/Mitigation |
|------------|--------|---------------------|
| [Assumption] | Validated | [Evidence] |
| [Assumption] | Mitigated | [Mitigation] |
| [Assumption] | Accepted | [Rationale] |

---

## Edge Cases Handled

| Edge Case | Handling | Task Ref |
|-----------|----------|----------|
| [Edge case] | [How handled] | Task X.Y |

---

## Rollback Plan

If implementation fails:
1. [Rollback step 1]
2. [Rollback step 2]

---

## Sign-off

- [ ] Plan reviewed against original requirements
- [ ] All review items addressed
- [ ] Dependencies validated
- [ ] Risks mitigated or accepted
- [ ] Ready for implementation
```

## MCP Integration

- **Sequential MCP**: Systematic consolidation and validation
- **Context7 MCP**: Implementation pattern verification
- **Serena MCP**: Persist final plan, cross-session tracking

## Implementation Paths

After completing final plan, offer:

1. **Direct Execution** - Use `executing-plans` skill for straightforward work
2. **Subagent Execution** - Use `subagent-driven-development` for parallel tasks
3. **TaskMaster Integration** - Export to TaskMaster MCP for task tracking
4. **Handoff** - Generate handoff document for team execution

## Handoff

After completing final plan:

**Say:** "Final plan complete. Confidence score: [X]/30. Ready for implementation."

**Ask:** "Which implementation approach? Direct execution, subagents, or TaskMaster integration?"

## Boundaries

**Will:**
- Consolidate all review findings into final plan
- Resolve every assumption (no "Unknown" allowed)
- Create implementation-ready task specifications
- Provide confidence score and rollback plan

**Will Not:**
- Ignore review findings without justification
- Expand scope during consolidation
- Leave tasks vague or unverifiable
- Skip confidence assessment

## Three-Round Summary

```
+-------------------------------------------------------------+
|  /sc:plan          /sc:plan-review    /sc:plan-final        |
|  Generate          Challenge          Consolidate           |
|  Explore           Break              Validate              |
|  Structure         Find gaps          Finalize              |
|  Draft mindset     Adversarial        Execution-ready       |
|                                                             |
|  Output:           Output:            Output:               |
|  Initial plan      Review report      Final plan            |
|  with uncertainty  with findings      with confidence       |
+-------------------------------------------------------------+

ROI: Catches 60-80% of issues before implementation begins
```
