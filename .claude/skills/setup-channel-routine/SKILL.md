---
name: setup-channel-routine
description: "Create or update the daily CLOUD routine (scheduled Claude Code agent) that runs a content-factory channel's growth agent on a cron schedule. Reusable across channels — LinkedIn, X, Instagram Reels, and any future channel. Bakes in the canonical config (environment, the FORK repo the routine clones, allowed tools, no MCP connectors, push notifications, commit+PR after the run) and the per-channel prompt template, so every channel's routine is set up identically. Use when the user says /setup-channel-routine, 'set up the routine for X', 'schedule the <channel> agent', 'create a daily runner for <channel>', or 'make a routine like LinkedIn for <channel>'. Always trigger this skill for channel routine setup."
trigger: /setup-channel-routine
---

# /setup-channel-routine

Stands up (or updates) the **daily cloud routine** for a content-factory channel — a scheduled Claude Code agent that runs in Anthropic's cloud, clones the repo, runs the channel's growth-agent skill, commits, and opens a PR. One reusable recipe so every channel's routine matches the LinkedIn original.

**Argument:** the channel — `linkedin` | `x` | `instagram` (default: ask if missing).

---

## Critical context: the fork the routine clones

Cloud routines do **not** read your local working copy. They clone **`altaf-shaikh-cs/content-factory`** (a FORK of the upstream `altafshaikh/content-factory`, which is your local `origin`). A routine runs whatever is on the **fork's `main`**.

So before/after creating a routine, the channel's skill files MUST already be on the fork:
1. Push the channel skill + folder to upstream `main` (`git push origin main`).
2. Sync the fork: `bash scripts/sync-fork.sh`.

If the channel skill isn't on the fork, the routine will fail or run stale. **Always verify deployment** (see Step 4).

---

## Canonical routine config (identical for every channel)

| Field | Value |
|-------|-------|
| `environment_id` | `env_01Vofgnx2PoR7qURGVMb4HcN` (personal) |
| source repo (cloned) | `https://github.com/altaf-shaikh-cs/content-factory` (the FORK) |
| `allowed_tools` | `["Bash","Read","Write","Edit","Glob","Grep","WebFetch","WebSearch"]` |
| `mcp_connections` | **none** — clear them after create (the API auto-attaches all connected ones) |
| notifications | push on (the API default) |
| `enabled` | `true` |
| schedule | per-channel cron below, in **UTC** (user TZ is Asia/Calcutta = UTC+5:30) |

---

## Channel registry (agent + default schedule)

Schedules are staggered so the daily runs don't collide.

| Channel | Growth-agent invocation | Default time (IST) | Cron (UTC) |
|---------|-------------------------|--------------------|------------|
| `linkedin` | `/linkedin-growth-agent with N=3` | 8:30 PM | `0 15 * * *` |
| `instagram` | `/instagram-reels-agent` | 9:00 PM | `30 15 * * *` |
| `x` | `/x-growth-agent` | 10:00 AM | `30 4 * * *` |

If the user names a different time, convert IST → UTC (subtract 5:30) and **confirm the conversion** before creating.

---

## Prompt template (per run)

The cloud agent starts with zero context, so the prompt must be self-contained:

```
Run <AGENT INVOCATION>.

<one-paragraph channel summary: what this channel does and where it writes — pull it from the channel's CLAUDE.md so the cloud agent has context>. Follow .claude/skills/<channel-skill>/SKILL.md and ./<channel-folder>/CLAUDE.md exactly. ./raw-ideas/ is immutable — never move, rename, or delete files there. Only write inside ./<channel-folder>/; cross-channel reads are read-only. Update the channel's TODO.md.

After the run, commit the changes and open a PR.
```

---

## Procedure

1. **Resolve the channel** from the argument. If absent, ask which channel. Look it up in the registry for the agent invocation, default cron, and folder.
2. **Load the API tool:** `ToolSearch` with `select:RemoteTrigger`. (Auth is in-process — never use curl.)
3. **Check for an existing routine:** `RemoteTrigger {action:"list"}`. If one already exists for this channel (match by name, e.g. "Daily X Post Creator"), ask whether to **update** it (`action:"update"`, partial body) instead of creating a duplicate.
4. **Verify the channel skill is deployed to the fork** (so the routine won't run stale):
   - Confirm the channel's `SKILL.md` + folder are committed on upstream `main`.
   - `gh api repos/altaf-shaikh-cs/content-factory/contents --jq '.[].name'` and check the channel folder is present. If not, push to origin/main and run `bash scripts/sync-fork.sh` first.
5. **Build the create body** (generate a fresh lowercase v4 UUID for `events[].data.uuid`):
   ```json
   {
     "name": "Daily <Channel> <Post|Reel> Creator",
     "cron_expression": "<cron from registry or user>",
     "enabled": true,
     "job_config": { "ccr": {
       "environment_id": "env_01Vofgnx2PoR7qURGVMb4HcN",
       "session_context": {
         "sources": [{"git_repository": {"url": "https://github.com/altaf-shaikh-cs/content-factory"}}],
         "allowed_tools": ["Bash","Read","Write","Edit","Glob","Grep","WebFetch","WebSearch"]
       },
       "events": [{"data": {
         "uuid": "<fresh uuid>", "session_id": "", "type": "user", "parent_tool_use_id": null,
         "message": {"role": "user", "content": "<filled prompt template>"}
       }}]
     }}
   }
   ```
6. **Create:** `RemoteTrigger {action:"create", body:<above>}`.
7. **Strip auto-attached connectors:** the create response usually lists every connected MCP connector. Immediately `RemoteTrigger {action:"update", trigger_id:"<id>", body:{"clear_mcp_connections": true}}` so the routine matches the others (no connectors).
8. **Report:** print the routine id, the human-readable schedule (IST + UTC), `next_run_at`, and the management URL `https://claude.ai/code/routines/<id>`.
9. **Offer a test run:** ask whether to `RemoteTrigger {action:"run", trigger_id:"<id>"}` now to validate end-to-end before the first scheduled fire.

---

## Notes

- Routines can be listed/updated/run but **not deleted** here — to delete, direct the user to https://claude.ai/code/routines.
- Min cron interval is 1 hour.
- Keep schedules staggered; check the existing routines' times before picking a new one.
- This skill only configures the cloud routine. The channel's generation logic lives in its own growth-agent skill — this skill just schedules it.
- After ANY repo change that the routine depends on, re-deploy: push to origin/main, then `bash scripts/sync-fork.sh`.
