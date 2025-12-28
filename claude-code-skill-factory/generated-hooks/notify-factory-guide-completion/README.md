# notify-factory-guide-completion

## Overview
Sends a macOS notification with a ping sound when the factory-guide agent completes a task.

**Event Type:** `SubagentStop`
**Platform:** macOS only
**Complexity:** intermediate

## How It Works

1. **Trigger:** Runs when any subagent completes its task
2. **Check:** Looks for "factory-guide" in recent transcript activity
3. **Notify:** If found, plays ping sound and shows notification
4. **Log:** Records completion time to log file

### Workflow
```
Subagent Completes
    ↓
Check if macOS
    ↓
Read transcript
    ↓
Search for "factory-guide"
    ↓
[If found]
    ↓
Play Ping Sound (afplay)
    ↓
Show Notification (osascript)
    ↓
Log to file
```

## Features

- 🔔 **macOS Notification** - Native notification center integration
- 🔊 **Ping Sound** - System ping sound plays automatically
- 📝 **Activity Log** - Logs each completion to `~/.claude/agent-notifications.log`
- ⚡ **Fast** - Scans only last 50 lines of transcript
- 🛡️ **Safe** - Silent failure on non-macOS systems

## Prerequisites

- **macOS** (uses `afplay` and `osascript`)
- Claude Code running in CLI mode
- No additional tools required (uses system commands)

## Installation

### Step 1: Add Hook to Settings

1. Open your Claude Code settings file:
   ```bash
   # Project-level
   vim .claude/settings.json

   # OR User-level (recommended for this hook)
   vim ~/.claude/settings.json
   ```

2. Add this hook configuration under the `hooks` object:

```json
{
  "hooks": {
    "SubagentStop": [
      {
        "matcher": {},
        "hooks": [
          {
            "type": "command",
            "command": "#!/bin/bash\n\n# Check if we're on macOS (required for afplay and osascript)\nif [[ \"$OSTYPE\" != \"darwin\"* ]]; then\n    exit 0\nfi\n\n# Check if this is a subagent completion and if transcript exists\nif [ -z \"$CLAUDE_TRANSCRIPT_PATH\" ]; then\n    # Fallback: use session transcript path if available\n    TRANSCRIPT_PATH=\"$HOME/.claude/transcripts/latest.json\"\nelse\n    TRANSCRIPT_PATH=\"$CLAUDE_TRANSCRIPT_PATH\"\nfi\n\n# Check if transcript file exists\nif [ ! -f \"$TRANSCRIPT_PATH\" ]; then\n    exit 0\nfi\n\n# Check if factory-guide agent was used in the last few lines\n# Look for agent invocation in transcript (last 50 lines to be efficient)\nif tail -50 \"$TRANSCRIPT_PATH\" 2>/dev/null | grep -qi \"factory-guide\"; then\n    # Play ping sound\n    afplay /System/Library/Sounds/Ping.aiff 2>/dev/null &\n    \n    # Send macOS notification\n    osascript -e 'display notification \"The factory-guide agent has completed its task.\" with title \"Claude Code\" sound name \"Ping\"' 2>/dev/null &\n    \n    # Optional: Log the completion\n    echo \"[$(date '+%Y-%m-%d %H:%M:%S')] factory-guide agent completed\" >> \"$HOME/.claude/agent-notifications.log\"\nfi\n\nexit 0",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Step 2: Restart Claude Code

```bash
# If running in terminal, restart the session
claude --continue
```

### Step 3: Test the Hook

Invoke the factory-guide agent and wait for it to complete:

```
"Show me the factory guide templates"
```

You should:
- 🔊 Hear a ping sound
- 🔔 See a macOS notification
- 📝 Find a log entry in `~/.claude/agent-notifications.log`

## Configuration

### Customize Agent Name

To monitor a different agent, change the grep pattern:

```bash
# Change this line:
if tail -50 "$TRANSCRIPT_PATH" 2>/dev/null | grep -qi "factory-guide"; then

# To monitor a different agent:
if tail -50 "$TRANSCRIPT_PATH" 2>/dev/null | grep -qi "your-agent-name"; then
```

### Customize Notification Message

```bash
# Change this line:
osascript -e 'display notification "The factory-guide agent has completed its task." with title "Claude Code" sound name "Ping"'

# To your custom message:
osascript -e 'display notification "Your custom message here!" with title "Your Title" sound name "Ping"'
```

### Customize Sound

macOS system sounds available:
- `Ping.aiff` (default)
- `Glass.aiff`
- `Hero.aiff`
- `Submarine.aiff`
- `Blow.aiff`
- `Bottle.aiff`
- `Frog.aiff`
- `Funk.aiff`
- `Pop.aiff`
- `Purr.aiff`

Change both locations:
```bash
# Sound file
afplay /System/Library/Sounds/Glass.aiff

# Notification sound
osascript -e 'display notification "..." with title "..." sound name "Glass"'
```

### Disable Logging

Remove this line to disable logging:
```bash
echo "[$(date '+%Y-%m-%d %H:%M:%S')] factory-guide agent completed" >> "$HOME/.claude/agent-notifications.log"
```

### Monitor Multiple Agents

To notify for multiple agents:

```bash
# Replace the single grep with multiple checks
if tail -50 "$TRANSCRIPT_PATH" 2>/dev/null | grep -qiE "(factory-guide|rr-architect|rr-frontend-engineer)"; then
    afplay /System/Library/Sounds/Ping.aiff 2>/dev/null &
    osascript -e 'display notification "An agent has completed its task." with title "Claude Code" sound name "Ping"' 2>/dev/null &
fi
```

## Troubleshooting

### No Sound Playing

**Check sound file exists:**
```bash
ls -la /System/Library/Sounds/Ping.aiff
afplay /System/Library/Sounds/Ping.aiff
```

**Check volume:**
- Ensure system volume is not muted
- Check notification settings in System Preferences

### No Notification Appearing

**Check notification permissions:**
1. System Preferences → Notifications
2. Find "Terminal" or "iTerm" (your terminal app)
3. Ensure notifications are enabled

**Test notification manually:**
```bash
osascript -e 'display notification "Test" with title "Test" sound name "Ping"'
```

### Hook Not Triggering

**Check hook is installed:**
```bash
cat ~/.claude/settings.json | grep -A 20 SubagentStop
```

**Check transcript path:**
```bash
# Find where transcripts are stored
ls -la ~/.claude/transcripts/
```

**Test the grep pattern:**
```bash
# Check if agent name appears in transcript
grep -i "factory-guide" ~/.claude/transcripts/*.json
```

### Log File Not Created

**Check write permissions:**
```bash
touch ~/.claude/agent-notifications.log
ls -la ~/.claude/agent-notifications.log
```

**View log:**
```bash
tail -f ~/.claude/agent-notifications.log
```

## Platform Support

### macOS ✅
Fully supported with native commands.

### Linux ⚠️
Requires modification:
- Replace `afplay` with `paplay` or `aplay`
- Replace `osascript` with `notify-send`

```bash
# Linux version
paplay /usr/share/sounds/freedesktop/stereo/complete.oga &
notify-send "Claude Code" "The factory-guide agent has completed its task."
```

### Windows ⚠️
Requires modification:
- Replace with PowerShell commands
- Use `[System.Media.SystemSounds]::Exclamation.Play()`
- Use Windows notification API

## Safety Notes

**Safety Features:**
- ✅ Platform check (exits gracefully on non-macOS)
- ✅ File existence checks before reading
- ✅ Background execution (`&`) doesn't block
- ✅ Error suppression (`2>/dev/null`)
- ✅ Silent failure on any error
- ✅ Fast execution (<1 second)
- ✅ No destructive operations

**Privacy:**
- Hook only reads transcript to check agent name
- Log file only contains timestamps (no sensitive data)
- Notification shows generic message

## Advanced

### Custom Notification with Agent Info

Extract agent details from transcript:

```bash
# Get the actual agent name dynamically
AGENT_NAME=$(tail -50 "$TRANSCRIPT_PATH" 2>/dev/null | grep -o '"subagent_type":"[^"]*"' | tail -1 | cut -d'"' -f4)

if [ -n "$AGENT_NAME" ]; then
    osascript -e "display notification 'The $AGENT_NAME agent has completed.' with title 'Claude Code' sound name 'Ping'"
fi
```

### Different Sounds for Different Agents

```bash
if tail -50 "$TRANSCRIPT_PATH" | grep -qi "factory-guide"; then
    afplay /System/Library/Sounds/Ping.aiff &
elif tail -50 "$TRANSCRIPT_PATH" | grep -qi "rr-architect"; then
    afplay /System/Library/Sounds/Glass.aiff &
elif tail -50 "$TRANSCRIPT_PATH" | grep -qi "rr-frontend-engineer"; then
    afplay /System/Library/Sounds/Hero.aiff &
fi
```

### Rich Notifications with Buttons

```bash
# macOS notification with action button
osascript <<EOF
display notification "factory-guide completed" with title "Claude Code" subtitle "Agent Task Complete" sound name "Ping"
EOF
```

### Integration with Other Tools

**Slack notification:**
```bash
# After successful completion
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"factory-guide agent completed!"}' \
  YOUR_SLACK_WEBHOOK_URL
```

**Email notification:**
```bash
echo "factory-guide agent completed at $(date)" | mail -s "Claude Code Agent" your@email.com
```

## Examples

### Example Log Output

```
[2025-10-30 19:45:23] factory-guide agent completed
[2025-10-30 20:12:45] factory-guide agent completed
[2025-10-30 21:03:12] factory-guide agent completed
```

### Example Notification

```
┌─────────────────────────────────────┐
│ Claude Code                    [×]  │
├─────────────────────────────────────┤
│ The factory-guide agent has         │
│ completed its task.                 │
│                                     │
│ [View]                       Now    │
└─────────────────────────────────────┘
```

## Uninstall

Remove the hook from `.claude/settings.json` and delete the log file:

```bash
# Remove log file
rm ~/.claude/agent-notifications.log

# Edit settings and remove the SubagentStop hook
vim ~/.claude/settings.json
```

---

**Generated by hook-factory** | 2025-10-30
**Template:** custom
**Version:** 1.0
**Platform:** macOS
