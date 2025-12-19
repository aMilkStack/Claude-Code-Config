#!/usr/bin/env python3
"""
Stop event hook that runs build checks and provides instructions for error resolution.
Runs when Claude Code finishes responding.
"""
import json
import sys
import os
import subprocess
import re
from pathlib import Path

# Read event information from stdin
try:
    event_info = json.load(sys.stdin)
except:
    sys.exit(0)

session_id = event_info.get("session_id", "default")
project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())

cache_dir = Path(project_dir) / ".claude" / "tsc-cache" / session_id

# Check if cache exists
if not cache_dir.exists():
    sys.exit(0)

affected_repos_file = cache_dir / "affected-repos.txt"
if not affected_repos_file.exists():
    sys.exit(0)

# Create results directory
results_dir = cache_dir / "results"
results_dir.mkdir(parents=True, exist_ok=True)

def count_tsc_errors(output: str) -> int:
    """Count TypeScript errors in output."""
    pattern = r'\.tsx?.*:.*error TS\d+:'
    return len(re.findall(pattern, output))

# Initialize error tracking
total_errors = 0
has_errors = False

# Clear previous error summary
error_summary_file = results_dir / "error-summary.txt"
error_summary_file.write_text("")

# Read commands file
commands_file = cache_dir / "commands.txt"
commands = {}
if commands_file.exists():
    for line in commands_file.read_text().strip().split("\n"):
        if line and ":tsc:" in line:
            parts = line.split(":tsc:", 1)
            if len(parts) == 2:
                commands[parts[0]] = parts[1]

# Read affected repos and run TSC checks
affected_repos = affected_repos_file.read_text().strip().split("\n")

for repo in affected_repos:
    repo = repo.strip()
    if not repo:
        continue
    
    tsc_cmd = commands.get(repo)
    if not tsc_cmd:
        continue
    
    # Run TSC
    try:
        result = subprocess.run(
            tsc_cmd,
            shell=True,
            capture_output=True,
            text=True,
            cwd=project_dir
        )
        output = result.stdout + result.stderr
        
        if result.returncode != 0:
            has_errors = True
            error_count = count_tsc_errors(output)
            total_errors += error_count
            
            # Save error output
            (results_dir / f"{repo}-errors.txt").write_text(output)
            with open(error_summary_file, "a") as f:
                f.write(f"{repo}:{error_count}\n")
        else:
            with open(error_summary_file, "a") as f:
                f.write(f"{repo}:0\n")
    except Exception as e:
        continue

# If we have errors, prepare for resolution
if has_errors:
    # Combine all errors into one file
    last_errors = cache_dir / "last-errors.txt"
    all_errors = []
    
    for error_file in results_dir.glob("*-errors.txt"):
        repo_name = error_file.stem.replace("-errors", "")
        all_errors.append(f"=== Errors in {repo_name} ===")
        all_errors.append(error_file.read_text())
        all_errors.append("")
    
    last_errors.write_text("\n".join(all_errors))
    
    # Copy TSC commands for the resolver
    if commands_file.exists():
        (cache_dir / "tsc-commands.txt").write_text(commands_file.read_text())
    
    # Output to stderr
    if total_errors >= 5:
        print("", file=sys.stderr)
        print("## TypeScript Build Errors Detected", file=sys.stderr)
        print("", file=sys.stderr)
        print(f"Found {total_errors} TypeScript errors across the following repos:", file=sys.stderr)
        
        for line in error_summary_file.read_text().strip().split("\n"):
            if ":" in line:
                r, c = line.rsplit(":", 1)
                if c.strip().isdigit() and int(c.strip()) > 0:
                    print(f"- {r}: {c} errors", file=sys.stderr)
        
        print("", file=sys.stderr)
        print("Please use the auto-error-resolver agent to fix these errors systematically.", file=sys.stderr)
        print("The error details have been cached for the resolver to use.", file=sys.stderr)
        sys.exit(2)
    else:
        print("", file=sys.stderr)
        print("## Minor TypeScript Errors", file=sys.stderr)
        print("", file=sys.stderr)
        print(f"Found {total_errors} TypeScript error(s). Here are the details:", file=sys.stderr)
        print("", file=sys.stderr)
        
        errors_text = last_errors.read_text()
        for line in errors_text.split("\n"):
            print(f"  {line}", file=sys.stderr)
        
        print("", file=sys.stderr)
        print("Please fix these errors directly in the affected files.", file=sys.stderr)
        sys.exit(2)
else:
    # Clean up session cache on success
    import shutil
    shutil.rmtree(cache_dir, ignore_errors=True)
    sys.exit(0)
