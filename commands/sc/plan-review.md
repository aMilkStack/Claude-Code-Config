---
name: plan-review
description: "Stress-test and critique the initial plan using 5 adversarial lenses (Round 2 of 3)"
category: orchestration
complexity: advanced
mcp-servers: [sequential, serena]
personas: [analyzer, security]
---

# /sc:plan-review - Adversarial Plan Review (Round 2/3)

## Triggers
- After /sc:plan completes
- When reviewing any existing plan
- Before committing significant resources to implementation

## Usage
```
/sc:plan-review [plan-file|--last] [--deep] [--focus skeptic|edge|redundancy|alternatives|dependencies]
```

## Three-Round Planning System
```
/sc:plan --> /sc:plan-review (you are here) --> /sc:plan-final
  Generate         Challenge                     Consolidate
  Explore          Break                         Validate
  Structure        Find gaps                     Finalize
  Draft mindset    Adversarial                   Execution-ready
```

## The Critique Framework

### Lens 1: The Skeptic
Challenge every assumption:

```
ASSUMPTION AUDIT:
For each major decision in the plan, ask:
- What assumption does this rest on?
- What if that assumption is wrong?
- What evidence supports this assumption?
- What would falsify it?

HIDDEN ASSUMPTIONS:
- "Users will..." - Do we know this?
- "The system can..." - Verified?
- "This should take..." - Based on what?
- "We can reuse..." - Actually compatible?
```

**Output:** List of assumptions with confidence ratings (High/Medium/Low/Unknown)

### Lens 2: The Edge Case Hunter
Find what breaks:

```
EDGE CASE CATEGORIES:
+---------------------------------------------+
| SCALE EDGES                                 |
| - What if 0 items? 1 item? 1 million?       |
| - What if request takes 30 seconds?         |
| - What if payload is 100MB?                 |
+---------------------------------------------+
| STATE EDGES                                 |
| - What if user cancels mid-operation?       |
| - What if system crashes during?            |
| - What if data is partially written?        |
+---------------------------------------------+
| INPUT EDGES                                 |
| - What if input is malformed?               |
| - What if required field is missing?        |
| - What if encoding is unexpected?           |
+---------------------------------------------+
| TIMING EDGES                                |
| - What if called twice simultaneously?      |
| - What if dependency is slow/unavailable?   |
| - What if executed out of expected order?   |
+---------------------------------------------+
| PERMISSION EDGES                            |
| - What if user lacks permission?            |
| - What if token expires mid-operation?      |
| - What if rate limited?                     |
+---------------------------------------------+
```

**Output:** Edge cases requiring explicit handling

### Lens 3: The Redundancy Auditor
Find waste and duplication:

```
REDUNDANCY CHECK:
- Are any tasks doing the same thing differently?
- Is there unnecessary abstraction?
- Are we building what already exists?
- Can phases be combined without loss?
- Are dependencies actually needed?
- Is scope minimal for the goal?

YAGNI FILTER:
For each task, ask:
"If we shipped without this, would it matter?"
- Yes, blocks core function -> Keep
- No, nice-to-have -> Cut
- Maybe -> Flag for discussion
```

**Output:** Tasks to remove, combine, or defer

### Lens 4: The Alternative Advocate
Challenge the chosen approach:

```
ALTERNATIVE ANALYSIS:
Take the rejected alternatives from initial plan:
- Re-argue FOR each rejected alternative
- What conditions would make it better?
- What are we giving up by not choosing it?
- Is hybrid approach possible?

NEW ALTERNATIVES:
- What approach would a different team take?
- What if we had half the time? Double?
- What if we prioritized differently?
- What's the "lazy" solution?
```

**Output:** Strengthened justification OR changed approach

### Lens 5: The Dependency Mapper
Verify the dependency graph:

```
DEPENDENCY AUDIT:
For each dependency:
- Is it actually required?
- What happens if it's unavailable?
- Is there a fallback?
- Who owns it? Is it stable?

ORDERING CHECK:
- Can any tasks be parallelized?
- Are there false dependencies?
- What's the actual critical path?
- Where are the bottlenecks?
```

**Output:** Corrected dependency graph, parallelization opportunities

## Critique Document Structure

```markdown
# [Feature/Task Name] - Review Report

**Initial Plan:** [link/reference]
**Review Date:** [timestamp]
**Round:** 2 of 3

## Executive Summary
[2-3 sentences: key findings from critique]

## Assumption Audit
### High-Risk Assumptions
| Assumption | Risk | Evidence | Mitigation |
|------------|------|----------|------------|

### Assumptions Validated
- [Assumption 1] - Confirmed by [evidence]

## Edge Cases Requiring Handling

### Critical (Must Address)
1. **[Edge case]:** [How it breaks] -> [Required handling]

### Important (Should Address)
1. **[Edge case]:** [Impact] -> [Suggested handling]

## Redundancy Findings
### Tasks to Remove
- [Task X]: [Why unnecessary]

### Tasks to Combine
- [Task A + Task B]: [How to merge]

### Tasks to Defer
- [Task Y]: [Move to future iteration because...]

## Alternative Analysis
### Original Approach Strengthened
[Why chosen approach survives scrutiny]

### Approach Modifications
[Changes to original approach based on critique]

## Dependency Corrections
### Parallelization Opportunities
- [Tasks that can run parallel]

### Critical Path
[Actual minimum path to completion]

## Recommendations for Final Plan

### Must Change
1. [Change 1]

### Should Change
1. [Change 1]

### Consider Changing
1. [Change 1]
```

## MCP Integration

- **Sequential MCP**: Systematic application of each lens
- **Serena MCP**: Access plan context, persist review findings

## The Critique Oath

Before completing review, verify:
```
- I tried to break this plan, not validate it
- I argued FOR the alternatives, not just against
- I found concrete edge cases, not abstract concerns
- Every finding has an actionable recommendation
- I distinguished critical from nice-to-have
- The plan is BETTER for having been critiqued
```

## Handoff

After completing review:

**Say:** "Review complete. Key findings: [summary]. Ready for Round 3 - Final consolidation. Use `/sc:plan-final` to create execution-ready plan."

## Boundaries

**Will:**
- Apply all 5 lenses systematically
- Challenge assumptions adversarially
- Provide actionable recommendations
- Strengthen or change the approach

**Will Not:**
- Rubber stamp plans without real critique
- Nitpick minor issues while missing major flaws
- Add scope during review (critique scope, don't expand it)
- Find issues without providing resolutions
