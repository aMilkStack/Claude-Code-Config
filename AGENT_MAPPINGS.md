# Skill → Agent Mappings

When these skills are triggered, dispatch the corresponding agents using the Task tool.

**ALWAYS use `model: "opus"` for all agent dispatches.**

---

## Review Skills

| Skill | Agent(s) | subagent_type |
|-------|----------|---------------|
| `code-review-excellence` | Code Reviewer | `pr-review-toolkit:code-reviewer` |
| | Test Analyzer | `pr-review-toolkit:pr-test-analyzer` |
| | Silent Failure Hunter | `pr-review-toolkit:silent-failure-hunter` |
| | Type Design Analyzer | `pr-review-toolkit:type-design-analyzer` |
| `requesting-code-review` | Code Reviewer | `pr-review-toolkit:code-reviewer` |

## Debugging Skills

| Skill | Agent(s) | subagent_type |
|-------|----------|---------------|
| `debugging-strategies` | Root Cause Analyst | `root-cause-analyst` |
| | Silent Failure Hunter | `pr-review-toolkit:silent-failure-hunter` |
| `root-cause-tracing` | Root Cause Analyst | `root-cause-analyst` |
| `systematic-debugging` | Root Cause Analyst | `root-cause-analyst` |

## Architecture Skills

| Skill | Agent(s) | subagent_type |
|-------|----------|---------------|
| `backend-dev-guidelines` | Backend Architect | `backend-architect` |
| `frontend-dev-guidelines` | Frontend Architect | `frontend-architect` |

## Documentation Skills

| Skill | Agent(s) | subagent_type |
|-------|----------|---------------|
| `docs-write` | Documentation Architect | `documentation-architect` |
| `docs-review` | Technical Writer | `technical-writer` |

## Error Handling Skills

| Skill | Agent(s) | subagent_type |
|-------|----------|---------------|
| `error-handling-patterns` | Silent Failure Hunter | `pr-review-toolkit:silent-failure-hunter` |
| `error-tracking` | Silent Failure Hunter | `pr-review-toolkit:silent-failure-hunter` |

## Testing Skills

| Skill | Agent(s) | subagent_type |
|-------|----------|---------------|
| `test-driven-development` | Quality Engineer | `quality-engineer` |
| `testing-anti-patterns` | Quality Engineer | `quality-engineer` |

## Parallel Investigation

| Skill | Agent(s) | subagent_type |
|-------|----------|---------------|
| `dispatching-parallel-agents` | General Purpose (multiple) | `general-purpose` |

---

## NOT Using Agents (Different Workflows)

These use **built-in modes** instead of agents:

| Skill/Command | Uses | NOT Agent |
|---------------|------|-----------|
| `/sc:plan` | EnterPlanMode | Built-in plan mode |
| `/sc:plan-review` | Extended thinking | Built-in critique |
| `/sc:plan-final` | ExitPlanMode | Built-in finalization |
| `/sc:brainstorm` | Socratic dialogue | Interactive conversation |

---

## Usage Pattern

**ALWAYS specify `model: "opus"` for Opus 4.5!**

```
# Single agent - ALWAYS USE OPUS
Task tool:
  subagent_type: "root-cause-analyst"
  model: "opus"
  prompt: "Investigate [problem description]"

# Multiple agents in parallel (for comprehensive review)
Task tool (parallel):
  1. subagent_type: "pr-review-toolkit:code-reviewer"
     model: "opus"
  2. subagent_type: "pr-review-toolkit:pr-test-analyzer"
     model: "opus"
  3. subagent_type: "pr-review-toolkit:silent-failure-hunter"
     model: "opus"
```

## Enforcement

When dispatching ANY agent:
- ALWAYS include `model: "opus"` parameter
- NEVER use default model
- Opus 4.5 = best quality for specialized tasks
