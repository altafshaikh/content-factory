#!/usr/bin/env bash
#
# sync-fork.sh — keep the routine's fork in sync with the upstream repo.
#
# WHY: cloud routines (LinkedIn / X / Instagram daily runners) clone code from the
# FORK `altaf-shaikh-cs/content-factory`, which is a fork of the upstream
# `altafshaikh/content-factory` (the local `origin`). A change only reaches a
# routine after it lands on upstream `main` AND the fork is synced from upstream.
#
# This script does the second half: fast-forwards the fork's main from upstream main.
# Run it after every push to origin/main.
#
# Usage:
#   bash scripts/sync-fork.sh            # sync now (manual)
#   bash scripts/sync-fork.sh --from-hook  # read a PostToolUse JSON on stdin; only
#                                            sync if the tool call was a git push touching main
#
# Requires: gh authenticated on the fork's account (altaf-shaikh-cs).

set -uo pipefail

UPSTREAM="altafshaikh/content-factory"
FORK="altaf-shaikh-cs/content-factory"
BRANCH="main"

# Hook mode: gate on the Bash command that just ran.
if [ "${1:-}" = "--from-hook" ]; then
  input="$(cat)"
  printf '%s' "$input" | grep -q "git push" || exit 0
  printf '%s' "$input" | grep -q "$BRANCH"   || exit 0
fi

if gh repo sync "$FORK" --source "$UPSTREAM" --branch "$BRANCH" 2>&1; then
  echo "Fork synced: $FORK $BRANCH <- $UPSTREAM $BRANCH"
else
  echo "WARNING: fork sync failed. Routines will run stale code until resolved." >&2
  echo "Fix: ensure gh is authed on the fork account, or sync manually at https://github.com/$FORK" >&2
  exit 0   # never block the surrounding workflow on a sync failure
fi
