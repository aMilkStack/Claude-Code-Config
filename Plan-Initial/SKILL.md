---
name: plan-alpha
description: Use when starting any significant task requiring planning - creates initial comprehensive plan using extended thinking and structured analysis. First stage of the three-round planning system. Always followed by plan-critique.
---

# Plan Alpha: Initial Planning

## Overview

First round of the three-round planning system. Creates a comprehensive initial plan using extended thinking (ultrathink) and structured Plan Mode analysis.

**Announce at start:** "Starting Plan Alpha - Round 1 of 3. Using extended thinking for initial plan generation."

**This skill is part of a chain:**
1. **plan-alpha** (you are here) → Initial comprehensive plan
2. **plan-critique** → Critique, edge cases, alternatives
3. **plan-omega** → Final optimisation and execution prep

## When to Use

- Starting any significant feature or project
- Complex problem requiring structured approach
- Before implementation work begins
- When brainstorming skill has completed design phase

**Do NOT use for:**
- Simple, obvious tasks (under 30 mins work)
- Bug fixes (use systematic-debugging instead)
- Tasks already planned elsewhere

## The Process

### Step 1: Context Gathering

Before planning, understand the landscape:

```
GATHER:
□ Project state (files, structure, recent changes)
□ Existing documentation (PRD, specs, designs)
□ Related code and patterns in codebase
□ Dependencies and constraints
□ Success criteria from stakeholder
```

**Ask if unclear:** "What does success look like for this?"

### Step 2: Ultrathink Analysis

Engage extended thinking mode for deep analysis:

```
ULTRATHINK FRAMEWORK:
┌─────────────────────────────────────────────┐
│ PROBLEM DECOMPOSITION                       │
│ - What are we actually trying to solve?     │
│ - What are the sub-problems?                │
│ - What's the dependency graph?              │
├─────────────────────────────────────────────┤
│ APPROACH EXPLORATION                        │
│ - What are 3+ different approaches?         │
│ - What are trade-offs of each?              │
│ - Which aligns best with constraints?       │
├─────────────────────────────────────────────┤
│ RISK IDENTIFICATION                         │
│ - What could go wrong?                      │
│ - What are the unknowns?                    │
│ - Where might estimates be wrong?           │
├─────────────────────────────────────────────┤
│ RESOURCE MAPPING                            │
│ - What existing code/patterns can we reuse? │
│ - What skills/tools are needed?             │
│ - What documentation exists?                │
└─────────────────────────────────────────────┘
```

### Step 3: Plan Mode Structure

Generate the plan using this structure:

```markdown
# [Feature/Task Name] - Alpha Plan

**Status:** Draft - Pending Critique
**Created:** [timestamp]
**Round:** 1 of 3

## Goal
[One sentence: what does done look like?]

## Context
[2-3 sentences: why this matters, what triggered it]

## Approach
[Chosen approach with brief justification]

### Alternatives Considered
1. [Alternative 1] - Rejected because [reason]
2. [Alternative 2] - Rejected because [reason]

## Task Breakdown

### Phase 1: [Name]
**Objective:** [What this phase achieves]

- [ ] Task 1.1: [Specific action]
- [ ] Task 1.2: [Specific action]
- [ ] Task 1.3: [Specific action]

**Verification:** [How to confirm phase complete]

### Phase 2: [Name]
[Same structure...]

## Dependencies
- [External dependency 1]
- [Internal dependency 1]

## Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |

## Open Questions
- [ ] [Question needing resolution]
- [ ] [Uncertainty to address]

## Estimated Effort
[Time estimate with confidence level]
```

### Step 4: Self-Assessment

Before handoff, assess the plan:

```
ALPHA PLAN SELF-CHECK:
□ Goal is specific and measurable
□ Tasks are concrete actions (not vague)
□ Dependencies identified
□ At least 2 alternatives were considered
□ Risks have mitigations
□ Open questions are flagged (not hidden)
□ Effort estimate has confidence qualifier
```

**Note weaknesses explicitly:** "Areas I'm uncertain about: [list]"

## Output Location

Save alpha plan to: `docs/plans/YYYY-MM-DD-[feature]-alpha.md`

## Handoff to Plan Critique

After completing alpha plan:

**Say:** "Alpha plan complete. Ready for Round 2 - Critique phase."

**REQUIRED NEXT SKILL:** Use plan-critique to:
- Challenge assumptions
- Find edge cases
- Identify redundancies
- Propose alternatives
- Stress-test the approach

**Do NOT proceed to implementation from alpha plan.** The critique round catches 60-80% of issues that would otherwise surface during implementation.

## Integration with Other Skills

**Prerequisite skills:**
- **brainstorming** - Often runs before plan-alpha for design exploration

**Chain skills:**
- **plan-critique** - REQUIRED next step
- **plan-omega** - Final round after critique

**Complementary skills:**
- **writing-plans** - Used in plan-omega for implementation-ready output
- **verification-before-completion** - Verify plan quality before handoff

## Key Principles

- **Ultrathink first** - Deep analysis before structure
- **Multiple approaches** - Never just one way
- **Flag uncertainty** - Don't hide what you don't know
- **Draft mindset** - This WILL be critiqued and improved
- **Concrete tasks** - Vague tasks = vague outcomes

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Surface planning | Tasks are vague verbs | Rewrite as specific actions |
| Single approach | No alternatives listed | Force 2+ alternatives |
| Hidden uncertainty | "Should work" language | Make unknowns explicit |
| Scope creep | Plan keeps growing | Apply YAGNI ruthlessly |
| Premature detail | Implementation specifics | Save for plan-omega |
