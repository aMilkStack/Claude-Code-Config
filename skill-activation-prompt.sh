#!/bin/bash
set -e

# Use global hooks directory
HOOKS_DIR="$HOME/.claude/hooks"
cd "$HOOKS_DIR"
cat | npx tsx skill-activation-prompt.ts
