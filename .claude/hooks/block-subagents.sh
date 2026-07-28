# #!/usr/bin/env bash
# # Blocks subagent (Agent/Task) spawns to avoid premium per-agent seed cost.
# # Enable fan-out for a session with:  export CLAUDE_ALLOW_SUBAGENTS=1
# set -euo pipefail

# if [[ "${CLAUDE_ALLOW_SUBAGENTS:-0}" == "1" ]]; then
#   exit 0
# fi

# cat <<'JSON'
# {
#   "hookSpecificOutput": {
#     "hookEventName": "PreToolUse",
#     "permissionDecision": "deny",
#     "permissionDecisionReason": "Subagents are disabled in this project to control token cost (each agent inherits a premium context seed). Do the work inline in the main thread. If fan-out is truly needed, the user can run: export CLAUDE_ALLOW_SUBAGENTS=1"
#   }
# }
# JSON
