---
name: plan-critique
description: Use after plan-alpha to critique, stress-test, and refine the initial plan - identifies edge cases, redundancies, and alternative approaches. Second stage of the three-round planning system. Always preceded by plan-alpha, followed by plan-omega.
---

# Plan Critique: Adversarial Refinement

## Overview

Second round of the three-round planning system. Takes the alpha plan and subjects it to rigorous critique - finding gaps, challenging assumptions, and strengthening the approach.

**Announce at start:** "Starting Plan Critique - Round 2 of 3. Engaging adversarial analysis mode."

**This skill is part of a chain:**
1. **plan-alpha** → Initial comprehensive plan
2. **plan-critique** (you are here) → Critique, edge cases, alternatives
3. **plan-omega** → Final optimisation and execution prep

## When to Use

- Immediately after plan-alpha completes
- When reviewing any existing plan
- Before committing significant resources to implementation

**Prerequisites:**
- Alpha plan exists at `docs/plans/YYYY-MM-DD-[feature]-alpha.md`
- Or plan content provided in conversation

## The Critique Framework

### Lens 1: The Skeptic

Challenge every assumption:

```
ASSUMPTION AUDIT:
For each major decision in the plan, ask:
□ What assumption does this rest on?
□ What if that assumption is wrong?
□ What evidence supports this assumption?
□ What would falsify it?

HIDDEN ASSUMPTIONS:
□ "Users will..." - Do we know this?
□ "The system can..." - Verified?
□ "This should take..." - Based on what?
□ "We can reuse..." - Actually compatible?
```

**Output:** List of assumptions with confidence ratings (High/Medium/Low/Unknown)

### Lens 2: The Edge Case Hunter

Find what breaks:

```
EDGE CASE CATEGORIES:
┌─────────────────────────────────────────────┐
│ SCALE EDGES                                 │
│ - What if 0 items? 1 item? 1 million?       │
│ - What if request takes 30 seconds?         │
│ - What if payload is 100MB?                 │
├─────────────────────────────────────────────┤
│ STATE EDGES                                 │
│ - What if user cancels mid-operation?       │
│ - What if system crashes during?            │
│ - What if data is partially written?        │
├─────────────────────────────────────────────┤
│ INPUT EDGES                                 │
│ - What if input is malformed?               │
│ - What if required field is missing?        │
│ - What if encoding is unexpected?           │
├─────────────────────────────────────────────┤
│ TIMING EDGES                                │
│ - What if called twice simultaneously?      │
│ - What if dependency is slow/unavailable?   │
│ - What if executed out of expected order?   │
├─────────────────────────────────────────────┤
│ PERMISSION EDGES                            │
│ - What if user lacks permission?            │
│ - What if token expires mid-operation?      │
│ - What if rate limited?                     │
└─────────────────────────────────────────────┘
```

**Output:** Edge cases requiring explicit handling in plan

### Lens 3: The Redundancy Auditor

Find waste and duplication:

```
REDUNDANCY CHECK:
□ Are any tasks doing the same thing differently?
□ Is there unnecessary abstraction?
□ Are we building what already exists?
□ Can phases be combined without loss?
□ Are dependencies actually needed?
□ Is scope minimal for the goal?

YAGNI FILTER:
For each task, ask:
"If we shipped without this, would it matter?"
- Yes, blocks core function → Keep
- No, nice-to-have → Cut
- Maybe → Flag for discussion
```

**Output:** Tasks to remove, combine, or defer

### Lens 4: The Alternative Advocate

Challenge the chosen approach:

```
ALTERNATIVE ANALYSIS:
Take the rejected alternatives from alpha plan:
□ Re-argue FOR each rejected alternative
□ What conditions would make it better?
□ What are we giving up by not choosing it?
□ Is hybrid approach possible?

NEW ALTERNATIVES:
□ What approach would a different team take?
□ What if we had half the time? Double?
□ What if we prioritised differently?
□ What's the "lazy" solution?
```

**Output:** Strengthened justification OR changed approach

### Lens 5: The Dependency Mapper

Verify the dependency graph:

```
DEPENDENCY AUDIT:
For each dependency:
□ Is it actually required?
□ What happens if it's unavailable?
□ Is there a fallback?
□ Who owns it? Is it stable?

ORDERING CHECK:
□ Can any tasks be parallelised?
□ Are there false dependencies?
□ What's the actual critical path?
□ Where are the bottlenecks?
```

**Output:** Corrected dependency graph, parallelisation opportunities

## Critique Document Structure

```markdown
# [Feature/Task Name] - Critique Report

**Alpha Plan:** [link to alpha plan]
**Critique Date:** [timestamp]
**Round:** 2 of 3

## Executive Summary
[2-3 sentences: key findings from critique]

## Assumption Audit

### High-Risk Assumptions
| Assumption | Risk | Evidence | Mitigation |
|------------|------|----------|------------|
| [Assumption] | [H/M/L] | [What we know] | [How to verify/handle] |

### Assumptions Validated
- [Assumption 1] - Confirmed by [evidence]

## Edge Cases Requiring Handling

### Critical (Must Address)
1. **[Edge case]:** [How it breaks] → [Required handling]

### Important (Should Address)
1. **[Edge case]:** [Impact] → [Suggested handling]

### Minor (Document Only)
1. **[Edge case]:** [Unlikely but noted]

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

### Rejected Alternatives Confirmed
[Why alternatives remain inferior]

## Dependency Corrections

### Parallelisation Opportunities
- [Tasks that can run parallel]

### Critical Path
[Actual minimum path to completion]

### New Dependencies Identified
- [Previously missed dependency]

## Recommendations for Omega Plan

### Must Change
1. [Change 1]
2. [Change 2]

### Should Change
1. [Change 1]

### Consider Changing
1. [Change 1]

## Open Questions Resolved
- [Question from alpha] → [Answer/decision]

## New Questions Raised
- [New question requiring resolution]
```

## Output Location

Save critique to: `docs/plans/YYYY-MM-DD-[feature]-critique.md`

## Handoff to Plan Omega

After completing critique:

**Say:** "Critique complete. Key findings: [summary]. Ready for Round 3 - Final Optimisation."

**REQUIRED NEXT SKILL:** Use plan-omega to:
- Consolidate critique improvements
- Validate all assumptions addressed
- Create execution-ready plan
- Prepare implementation handoff

## Integration with Other Skills

**Prerequisite skills:**
- **plan-alpha** - REQUIRED - provides the plan to critique

**Chain skills:**
- **plan-omega** - REQUIRED next step

**Complementary skills:**
- **systematic-debugging** - Similar analytical rigour
- **root-cause-tracing** - For deep assumption analysis

## Key Principles

- **Adversarial mindset** - Your job is to break the plan
- **Steel-man alternatives** - Argue FOR rejected options
- **Concrete edge cases** - Not abstract "what ifs"
- **Actionable findings** - Each critique has a resolution
- **Preserve what works** - Don't critique for its own sake

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Rubber stamping | "Looks good" without specifics | Apply each lens systematically |
| Nitpicking | Minor issues, no substance | Focus on plan-breakers first |
| Scope expansion | Adding features during critique | Critique scope, don't expand it |
| Analysis paralysis | Finding issues, no resolutions | Every critique needs recommendation |
| Missing the obvious | Complex critique, simple flaw missed | Start with "what's the dumbest way this fails?" |

## The Critique Oath

Before completing critique, verify:

```
□ I tried to break this plan, not validate it
□ I argued FOR the alternatives, not just against
□ I found concrete edge cases, not abstract concerns
□ Every finding has an actionable recommendation
□ I distinguished critical from nice-to-have
□ The plan is BETTER for having been critiqued
```
