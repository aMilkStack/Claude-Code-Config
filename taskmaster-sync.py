#!/usr/bin/env python3
"""
TaskMaster Sync Hook (PostToolUse)
Syncs TodoWrite operations to TaskMaster MCP for persistent task tracking.
"""
import json
import sys

# Load input from stdin
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    sys.exit(0)  # Fail silently

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
tool_output = input_data.get("tool_output", "")

def output_json(instructions):
    """Output instructions for Claude"""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": instructions
        }
    }
    print(json.dumps(output))

# Only trigger on TodoWrite
if tool_name != "TodoWrite":
    sys.exit(0)

# Extract todos from the tool input
todos = tool_input.get("todos", [])

if not todos:
    sys.exit(0)

# Build sync instruction
in_progress = [t for t in todos if t.get("status") == "in_progress"]
pending = [t for t in todos if t.get("status") == "pending"]
completed = [t for t in todos if t.get("status") == "completed"]

instruction = """
TASKMASTER SYNC (Optional):
To persist these todos across sessions, consider using TaskMaster MCP:
- mcp__taskmaster-ai__get_tasks - Check existing tasks
- mcp__taskmaster-ai__set_task_status - Update task status

Current todos:
"""

if in_progress:
    instruction += f"- In Progress: {len(in_progress)}\n"
if pending:
    instruction += f"- Pending: {len(pending)}\n"
if completed:
    instruction += f"- Completed: {len(completed)}\n"

# Only output if there are meaningful todos
if len(todos) > 2:
    output_json(instruction)

sys.exit(0)
