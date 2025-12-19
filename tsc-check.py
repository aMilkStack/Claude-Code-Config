#!/usr/bin/env python3
"""
TSC Hook - TypeScript check after file modifications.
Runs after Edit, Write, MultiEdit tools.
"""
import json
import sys
import os
import subprocess
import re
from pathlib import Path

project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
home_dir = os.environ.get("USERPROFILE", os.environ.get("HOME", ""))
session_id = os.environ.get("SESSION_ID", "default")
cache_dir = Path(home_dir) / ".claude" / "tsc-cache" / session_id
cache_dir.mkdir(parents=True, exist_ok=True)

# Read hook input
try:
    hook_input = json.load(sys.stdin)
except:
    sys.exit(0)

tool_name = hook_input.get("tool_name", "")
tool_input = hook_input.get("tool_input", {})

# Known service directories
KNOWN_REPOS = {"email", "exports", "form", "frontend", "projects", "uploads", 
               "users", "utilities", "events", "database", "backend", "server", 
               "api", "src", "services", "client", "web", "app", "ui"}

def get_repo_for_file(file_path: str) -> str:
    """Get repo name from file path."""
    try:
        relative = os.path.relpath(file_path, project_dir).replace("\\", "/")
        parts = relative.split("/")
        if parts and parts[0] in KNOWN_REPOS:
            return parts[0]
    except:
        pass
    return ""

def get_tsc_command(repo_path: Path) -> str:
    """Detect the correct TSC command for a repo."""
    if (repo_path / "tsconfig.app.json").exists():
        return "npx tsc --project tsconfig.app.json --noEmit"
    elif (repo_path / "tsconfig.build.json").exists():
        return "npx tsc --project tsconfig.build.json --noEmit"
    elif (repo_path / "tsconfig.json").exists():
        tsconfig = (repo_path / "tsconfig.json").read_text()
        if '"references"' in tsconfig:
            if (repo_path / "tsconfig.app.json").exists():
                return "npx tsc --project tsconfig.app.json --noEmit"
            elif (repo_path / "tsconfig.src.json").exists():
                return "npx tsc --project tsconfig.src.json --noEmit"
            return "npx tsc --build --noEmit"
        return "npx tsc --noEmit"
    return "npx tsc --noEmit"

def run_tsc_check(repo: str) -> tuple:
    """Run TSC check for a repo. Returns (success, output)."""
    repo_path = Path(project_dir) / repo
    cache_file = cache_dir / f"{repo}-tsc-cmd.cache"
    
    # Get or cache TSC command
    if cache_file.exists():
        tsc_cmd = cache_file.read_text().strip()
    else:
        tsc_cmd = get_tsc_command(repo_path)
        cache_file.write_text(tsc_cmd)
    
    try:
        result = subprocess.run(
            tsc_cmd,
            shell=True,
            capture_output=True,
            text=True,
            cwd=str(repo_path)
        )
        output = result.stdout + result.stderr
        has_errors = result.returncode != 0 or "error TS" in output
        return (not has_errors, output)
    except Exception as e:
        return (True, str(e))  # Assume OK on exception

# Only process file modification tools
if tool_name not in ("Write", "Edit", "MultiEdit"):
    sys.exit(0)

# Extract file paths
file_paths = []
if tool_name == "MultiEdit":
    edits = tool_input.get("edits", [])
    file_paths = [e.get("file_path", "") for e in edits]
else:
    fp = tool_input.get("file_path", "")
    if fp:
        file_paths = [fp]

# Filter to TS/JS files only
ts_files = [f for f in file_paths if f and re.search(r'\.(ts|tsx|js|jsx)$', f)]

if not ts_files:
    sys.exit(0)

# Get unique repos to check
repos_to_check = set()
for f in ts_files:
    repo = get_repo_for_file(f)
    if repo:
        repos_to_check.add(repo)

if not repos_to_check:
    sys.exit(0)

# Run checks
error_count = 0
error_output = []
failed_repos = []

print(f"⚡ TypeScript check on: {' '.join(repos_to_check)}", file=sys.stderr)

for repo in repos_to_check:
    print(f"  Checking {repo}... ", end="", file=sys.stderr)
    
    success, output = run_tsc_check(repo)
    
    if not success:
        print("❌ Errors found", file=sys.stderr)
        error_count += 1
        failed_repos.append(repo)
        error_output.append(f"\n=== Errors in {repo} ===\n{output}")
    else:
        print("✅ OK", file=sys.stderr)

# If errors found, report them
if error_count > 0:
    # Save for agent
    (cache_dir / "last-errors.txt").write_text("\n".join(error_output))
    (cache_dir / "affected-repos.txt").write_text("\n".join(failed_repos))
    
    # Save TSC commands
    tsc_cmds = ["# TSC Commands by Repo"]
    for repo in failed_repos:
        cmd_file = cache_dir / f"{repo}-tsc-cmd.cache"
        cmd = cmd_file.read_text().strip() if cmd_file.exists() else "npx tsc --noEmit"
        tsc_cmds.append(f"{repo}: {cmd}")
    (cache_dir / "tsc-commands.txt").write_text("\n".join(tsc_cmds))
    
    # Output to stderr
    print("", file=sys.stderr)
    print("━" * 60, file=sys.stderr)
    print(f"🚨 TypeScript errors found in {error_count} repo(s): {' '.join(failed_repos)}", file=sys.stderr)
    print("━" * 60, file=sys.stderr)
    print("", file=sys.stderr)
    print("👉 IMPORTANT: Use the auto-error-resolver agent to fix the errors", file=sys.stderr)
    print("", file=sys.stderr)
    print("WE DO NOT LEAVE A MESS BEHIND", file=sys.stderr)
    print("Error Preview:", file=sys.stderr)
    
    all_errors = "\n".join(error_output)
    ts_errors = [line for line in all_errors.split("\n") if "error TS" in line]
    for line in ts_errors[:10]:
        print(line, file=sys.stderr)
    
    if len(ts_errors) > 10:
        print(f"... and {len(ts_errors) - 10} more errors", file=sys.stderr)
    
    sys.exit(1)

# Cleanup old cache (older than 7 days)
import time
try:
    tsc_cache_root = Path(home_dir) / ".claude" / "tsc-cache"
    for d in tsc_cache_root.iterdir():
        if d.is_dir() and (time.time() - d.stat().st_mtime) > 7 * 86400:
            import shutil
            shutil.rmtree(d, ignore_errors=True)
except:
    pass

sys.exit(0)
