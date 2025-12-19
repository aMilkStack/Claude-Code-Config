#!/usr/bin/env python3
"""
Trigger Build Resolver Hook
Checks for git changes in service directories and triggers build-error-resolver.
"""
import json
import sys
import os
import subprocess
from pathlib import Path

# Debug log
debug_log = Path(os.environ.get("TEMP", "/tmp")) / "claude-hook-debug.log"

def log(msg):
    with open(debug_log, "a") as f:
        f.write(f"{msg}\n")

# Read stdin
try:
    stdin_data = sys.stdin.read()
    log(f"Hook triggered")
    log(f"Stdin: {stdin_data[:500]}")
except:
    stdin_data = ""

project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
log(f"CLAUDE_PROJECT_DIR: {project_dir}")

# Service directories to check
services_dirs = ["email", "exports", "form", "frontend", "projects", 
                 "uploads", "users", "utilities", "events", "database"]
services_with_changes = []

# Check each service directory for git changes
for service in services_dirs:
    service_path = Path(project_dir) / service
    git_dir = service_path / ".git"
    
    log(f"Checking service: {service} at {service_path}")
    
    if service_path.is_dir() and git_dir.is_dir():
        log(f"  -> Is a git repository")
        
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=str(service_path),
                capture_output=True,
                text=True
            )
            git_status = result.stdout.strip()
            
            if git_status:
                log(f"  -> Has changes:\n{git_status}")
                services_with_changes.append(service)
            else:
                log(f"  -> No changes")
        except Exception as e:
            log(f"  -> Error checking git: {e}")
    else:
        log(f"  -> Not a git repository or doesn't exist")

log(f"Services with changes: {services_with_changes}")

if services_with_changes:
    services_list = ", ".join(services_with_changes)
    msg = f"Changes detected in: {services_list} — triggering build-error-resolver..."
    log(msg)
    print(msg, file=sys.stderr)
    
    # Output JSON instruction for Claude
    output = {
        "hookSpecificOutput": {
            "hookEventName": "Stop",
            "additionalContext": f"""
BUILD CHECK TRIGGERED

Changes detected in: {services_list}

Please use the auto-error-resolver agent to build and fix any errors in these services:
- Task(subagent_type='auto-error-resolver', description='Fix build errors', prompt='Build and fix errors in: {services_list}')

Focus on these services in the monorepo structure. Each service has its own build process.
"""
        }
    }
    print(json.dumps(output))
else:
    log("No services with changes detected — skipping build-error-resolver.")
    print("No services with changes detected — skipping build-error-resolver.", file=sys.stderr)

log("=== END ===")
sys.exit(0)
