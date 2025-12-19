#!/usr/bin/env python3
"""
Post-tool-use hook that tracks edited files and their repos.
Runs after Edit, MultiEdit, or Write tools complete successfully.
Python version for Windows compatibility.
"""
import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Read tool information from stdin
try:
    tool_info = json.load(sys.stdin)
except:
    sys.exit(0)

# Extract relevant data
tool_name = tool_info.get("tool_name", "")
file_path = tool_info.get("tool_input", {}).get("file_path", "")
session_id = tool_info.get("session_id", "default")

# Skip if not an edit tool or no file path
if tool_name not in ("Edit", "MultiEdit", "Write") or not file_path:
    sys.exit(0)

# Skip markdown files
if file_path.endswith((".md", ".markdown")):
    sys.exit(0)

# Get project directory
project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())

# Create cache directory
cache_dir = Path(project_dir) / ".claude" / "tsc-cache" / session_id
cache_dir.mkdir(parents=True, exist_ok=True)

def detect_repo(file_path: str) -> str:
    """Detect repo from file path."""
    try:
        relative_path = os.path.relpath(file_path, project_dir).replace("\\", "/")
    except ValueError:
        return "unknown"
    
    parts = relative_path.split("/")
    if not parts:
        return "unknown"
    
    repo = parts[0]
    
    # Common project directory patterns
    known_repos = {
        "frontend", "client", "web", "app", "ui",
        "backend", "server", "api", "src", "services",
        "database", "prisma", "migrations"
    }
    
    if repo in known_repos:
        return repo
    
    # Package/monorepo structure
    if repo == "packages" and len(parts) > 1:
        return f"packages/{parts[1]}"
    
    if repo == "examples" and len(parts) > 1:
        return f"examples/{parts[1]}"
    
    # Root file
    if "/" not in relative_path:
        return "root"
    
    return "unknown"

def get_build_command(repo: str) -> str:
    """Get build command for repo."""
    repo_path = Path(project_dir) / repo
    package_json = repo_path / "package.json"
    
    if package_json.exists():
        try:
            with open(package_json) as f:
                pkg = json.load(f)
            if "build" in pkg.get("scripts", {}):
                # Detect package manager
                if (repo_path / "pnpm-lock.yaml").exists():
                    return f"cd {repo_path} && pnpm build"
                elif (repo_path / "package-lock.json").exists():
                    return f"cd {repo_path} && npm run build"
                elif (repo_path / "yarn.lock").exists():
                    return f"cd {repo_path} && yarn build"
                else:
                    return f"cd {repo_path} && npm run build"
        except:
            pass
    
    # Prisma
    if repo in ("database", "prisma") or "prisma" in repo:
        if (repo_path / "schema.prisma").exists() or (repo_path / "prisma" / "schema.prisma").exists():
            return f"cd {repo_path} && npx prisma generate"
    
    return ""

def get_tsc_command(repo: str) -> str:
    """Get TSC command for repo."""
    repo_path = Path(project_dir) / repo
    
    if (repo_path / "tsconfig.json").exists():
        if (repo_path / "tsconfig.app.json").exists():
            return f"cd {repo_path} && npx tsc --project tsconfig.app.json --noEmit"
        return f"cd {repo_path} && npx tsc --noEmit"
    
    return ""

# Detect repo
repo = detect_repo(file_path)

# Skip if unknown
if repo == "unknown" or not repo:
    sys.exit(0)

# Log edited file
timestamp = int(datetime.now().timestamp())
with open(cache_dir / "edited-files.log", "a") as f:
    f.write(f"{timestamp}:{file_path}:{repo}\n")

# Update affected repos list
affected_repos_file = cache_dir / "affected-repos.txt"
existing_repos = set()
if affected_repos_file.exists():
    existing_repos = set(affected_repos_file.read_text().strip().split("\n"))

if repo not in existing_repos:
    with open(affected_repos_file, "a") as f:
        f.write(f"{repo}\n")

# Store build commands
commands_file = cache_dir / "commands.txt"
existing_commands = set()
if commands_file.exists():
    existing_commands = set(commands_file.read_text().strip().split("\n"))

build_cmd = get_build_command(repo)
tsc_cmd = get_tsc_command(repo)

if build_cmd:
    existing_commands.add(f"{repo}:build:{build_cmd}")
if tsc_cmd:
    existing_commands.add(f"{repo}:tsc:{tsc_cmd}")

# Write unique commands
with open(commands_file, "w") as f:
    f.write("\n".join(sorted(existing_commands)))

sys.exit(0)
