#!/usr/bin/env bash
#
# daily-content-sync.sh — the 11:00 AM cron job (run by launchd).
#
# Order matters:
#   1) DOWN-sync: fast-forward the fork's main from personal main. This pulls in
#      any content PRs you MERGED since the last run, so the fork is realigned
#      and the cloud routines clone current code (no stale TODO.md / reel-map.md).
#   2) UP-open:   open a PR per NEW routine-generated `claude/*` branch on the
#      fork, into personal main, for your review.
#
# PRs you haven't reviewed stay OPEN — open-content-prs.sh skips branches that
# already have a PR, so nothing is duplicated and nothing is forced into the fork
# until you actually merge. Unmerged content simply isn't in the fork yet; the
# next time you merge its PR, the following day's down-sync pulls it in.
#
# Run by launchd daily at 11:00 AM IST; also safe to run by hand anytime:
#   bash scripts/daily-content-sync.sh

set -uo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] daily-content-sync START"

echo "--- step 1/2: down-sync fork from personal main (picks up merged PRs) ---"
bash "$DIR/sync-fork.sh" || echo "WARNING: down-sync failed (continuing)"

echo "--- step 2/2: open PRs for new fork content branches ---"
bash "$DIR/open-content-prs.sh" || echo "WARNING: open-content-prs failed"

echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] daily-content-sync DONE"
