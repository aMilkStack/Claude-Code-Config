#!/usr/bin/env python3
"""
Status Line for Claude Code (PowerShell compatible)
Shows: Model | Dir | Style | Context% | Tokens
"""
import json
import sys

try:
    input_data = json.load(sys.stdin)
except:
    print("Claude Code | No data")
    sys.exit(0)

# Extract values
model = input_data.get("model", {}).get("display_name", "Claude")
cwd = input_data.get("workspace", {}).get("current_dir", "")
style = input_data.get("output_style", {}).get("name", "default")

# Get just the last folder name
if cwd:
    dir_name = cwd.replace("\\", "/").split("/")[-1] or cwd
else:
    dir_name = "~"

# Context usage
usage = input_data.get("context_window", {}).get("current_usage")
ctx_size = input_data.get("context_window", {}).get("context_window_size", 200000)

if usage:
    inp = usage.get("input_tokens", 0)
    out = usage.get("output_tokens", 0)
    cache = usage.get("cache_read_input_tokens", 0)
    cache_create = usage.get("cache_creation_input_tokens", 0)

    current = inp + cache + cache_create
    pct = int((current / ctx_size) * 100) if ctx_size else 0

    inp_k = inp // 1000
    out_k = out // 1000
    cache_k = cache // 1000

    print(f"{model} | {dir_name} | {style} | {pct}% ctx | In:{inp_k}k Out:{out_k}k Cache:{cache_k}k")
else:
    print(f"{model} | {dir_name} | {style} | Ready")
