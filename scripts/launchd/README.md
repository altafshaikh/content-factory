# launchd: daily content sync

`com.altaf.content-factory.open-content-prs.plist` runs `scripts/daily-content-sync.sh`
**every day at 11:00 AM local time (Asia/Calcutta)** on Altaf's Mac. That wrapper:
1. **down-syncs** the fork's `main` from personal (`sync-fork.sh`) — picks up any
   content PRs you merged since the last run, and
2. **opens PRs** (`open-content-prs.sh`) for any new routine-generated `claude/*`
   branches on the fork, into personal `main`, for your review.

(The routines also self-sync from upstream at generation time, so the fork being
briefly stale between runs doesn't cause bad content — this cron mainly keeps the
fork tidy and routes content up.)

Why 11:00 AM: the cloud routines fire at 10:00 AM (X), 8:30 PM (LinkedIn), and
9:00 PM (Instagram). An 11:00 AM local run catches the prior evening's LinkedIn +
Instagram and that morning's X (after it finishes).

**Caveat:** launchd only fires when the Mac is awake/logged in. If it's asleep at
11:00 AM, the run is skipped that day — just run `bash scripts/open-content-prs.sh`
manually, or it catches everything on the next fire (branches accumulate; nothing
is lost).

## Install / reload

```bash
cp scripts/launchd/com.altaf.content-factory.open-content-prs.plist ~/Library/LaunchAgents/
launchctl bootout  gui/$(id -u)/com.altaf.content-factory.open-content-prs 2>/dev/null
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.altaf.content-factory.open-content-prs.plist
```

## Test now / inspect / uninstall

```bash
launchctl kickstart -k gui/$(id -u)/com.altaf.content-factory.open-content-prs   # run immediately
launchctl print gui/$(id -u)/com.altaf.content-factory.open-content-prs          # status + next fire
cat ~/Library/Logs/content-factory-open-content-prs.log                          # output
launchctl bootout gui/$(id -u)/com.altaf.content-factory.open-content-prs        # stop/uninstall
```

To auto-merge instead of opening PRs for review, change `ProgramArguments` to pass
`--merge` as a third `<string>` to the script, then reload.
