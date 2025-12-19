#!/usr/bin/env python3
"""
Pre-Compact Auto-Handoff Hook
Automatically saves session context to Serena memory before context compaction.
This ensures continuity across context windows without manual handoff.
"""
import json
import sys
from datetime import datetime

# Load input from stdin
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

# Extract conversation context
messages = input_data.get("messages", [])
session_id = input_data.get("session_id", "unknown")

def output_json(instructions):
    """Output instructions for Claude to execute"""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreCompact",
            "additionalContext": instructions
        }
    }
    print(json.dumps(output))

# Build a summary of recent work
recent_messages = messages[-20:] if len(messages) > 20 else messages  # Last 20 messages

# Extract key info from messages
user_requests = []
assistant_actions = []

for msg in recent_messages:
    role = msg.get("role", "")
    content = msg.get("content", "")

    if isinstance(content, str):
        if role == "user" and len(content) < 500:
            user_requests.append(content[:200])
        elif role == "assistant":
            # Look for tool uses or key actions
            if "created" in content.lower() or "updated" in content.lower():
                assistant_actions.append(content[:200])

# Generate handoff instruction
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

handoff_instruction = f"""
CONTEXT COMPACTION IMMINENT - AUTO-SAVING SESSION

1. SHOW USAGE: Run /usage to display total session usage before compaction

2. SAVE TO SERENA: Use mcp__plugin_serena_serena__write_memory to save:
   - Memory Title: "Session Handoff {timestamp}"
   - Memory Content:
     - Recent user requests: {user_requests[-5:] if user_requests else 'None captured'}
     - Key actions taken: {assistant_actions[-5:] if assistant_actions else 'None captured'}
     - Session ID: {session_id}

3. ACKNOWLEDGE: "Usage logged. Session context saved to Serena. Continuing after compaction..."
"""

output_json(handoff_instruction)
sys.exit(0)
