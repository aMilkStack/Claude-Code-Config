---
name: plan
description: "Generate initial comprehensive plan using extended thinking and structured analysis (Round 1 of 3)"
category: orchestration
complexity: advanced
mcp-servers: [sequential, context7, serena]
personas: [architect, analyzer]
---

# /sc:plan - Initial Plan Generation (Round 1/3)

## Triggers
- Starting any significant feature or project
- Complex problems requiring structured approach
- Before implementation work begins
- After brainstorming/ideation is complete

## Usage
```
/sc:plan [task-description] [--depth shallow|normal|deep] [--save]
```

## Three-Round Planning System
```
/sc:plan (you are here) --> /sc:plan-review --> /sc:plan-final
     Generate              Challenge          Consolidate
     Explore               Break              Validate
     Structure             Find gaps          Finalize
     Draft mindset         Adversarial        Execution-ready
```

## Behavioral Flow

### Step 1: Context Gathering
Before planning, understand the landscape:

```
GATHER:
- Project state (files, structure, recent changes)
- Existing documentation (PRD, specs, designs)
- Related code and patterns in codebase
- Dependencies and constraints
- Success criteria from stakeholder
```

**Use Serena MCP** to:
- Load project context and existing memories
- Search for related symbols and patterns
- Access cross-session planning history

**Ask if unclear:** "What does success look like for this?"

### Step 2: Ultrathink Analysis
Engage extended thinking (sequentialthinking MCP) for deep analysis:

```
ULTRATHINK FRAMEWORK:
+---------------------------------------------+
| PROBLEM DECOMPOSITION                       |
| - What are we actually trying to solve?     |
| - What are the sub-problems?                |
| - What's the dependency graph?              |
+---------------------------------------------+
| APPROACH EXPLORATION                        |
| - What are 3+ different approaches?         |
| - What are trade-offs of each?              |
| - Which aligns best with constraints?       |
+---------------------------------------------+
| RISK IDENTIFICATION                         |
| - What could go wrong?                      |
| - What are the unknowns?                    |
| - Where might estimates be wrong?           |
+---------------------------------------------+
| RESOURCE MAPPING                            |
| - What existing code/patterns can we reuse? |
| - What skills/tools are needed?             |
| - What documentation exists?                |
+---------------------------------------------+
```

### Step 3: Plan Structure
Generate the plan using this structure:

```markdown
# [Feature/Task Name] - Initial Plan

**Status:** Draft - Pending Review
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

**Verification:** [How to confirm phase complete]

### Phase 2: [Name]
[Same structure...]

## Dependencies
- [External dependency 1]
- [Internal dependency 1]

## Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | H/M/L | H/M/L | [Strategy] |

## Open Questions
- [ ] [Question needing resolution]
- [ ] [Uncertainty to address]
```

### Step 4: Self-Assessment
Before handoff, assess the plan:

```
PLAN SELF-CHECK:
- Goal is specific and measurable
- Tasks are concrete actions (not vague)
- Dependencies identified
- At least 2 alternatives were considered
- Risks have mitigations
- Open questions are flagged (not hidden)
```

**Note weaknesses explicitly:** "Areas I'm uncertain about: [list]"

## MCP Integration

- **Sequential MCP**: Deep multi-step reasoning for problem decomposition
- **Context7 MCP**: Framework-specific patterns and best practices
- **Serena MCP**: Project context, memory persistence, cross-session continuity

## Output

**Save plan to:** `docs/plans/YYYY-MM-DD-[feature]-plan.md`
**Or use Serena** to persist in project memory

## Handoff

After completing initial plan:

**Say:** "Initial plan complete. Ready for Round 2 - Review phase. Use `/sc:plan-review` to challenge assumptions and find gaps."

## Boundaries

**Will:**
- Generate comprehensive initial plans with proper structure
- Explore multiple approaches before committing
- Flag uncertainties and open questions
- Use extended thinking for complex problems

**Will Not:**
- Skip to implementation without review round
- Hide uncertainties or assume away risks
- Proceed with vague or generic tasks
- Generate plans for trivial tasks (under 30 min work)
