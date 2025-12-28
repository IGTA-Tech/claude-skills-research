# Hook Factory - Claude Code Hook Generator

**Generate production-ready Claude Code hooks from natural language requests.**

## Overview

Hook Factory is a skill for Claude Code that automates the creation of hooks with proper safety checks, validation, and documentation. It transforms simple requests like "auto-format Python files" into complete, production-ready hook configurations.

### What It Does

- 🎯 **Analyzes** natural language requests to determine hook type
- 🏗️ **Generates** complete hook configurations with safety wrappers
- ✅ **Validates** hooks for correctness and safety
- 📚 **Creates** comprehensive documentation
- 💾 **Saves** everything to `generated-hooks/` ready to use

### Key Features (v2.0)

- **10 Production Templates** - Formatting, testing, validation, sessions, notifications, security
- **7 Event Types** - PostToolUse, SubagentStop, SessionStart, PreToolUse, UserPromptSubmit, Stop, PrePush
- **Interactive Mode** - 7-question guided flow with smart defaults and auto-install
- **Automated Installation** - Python and Bash installers with backup/rollback
- **Enhanced Validation** - Secrets detection, event-specific rules, command validation
- **5 Language Support** - Python, JavaScript, TypeScript, Rust, Go
- **Automatic Safety** - Tool detection, silent failure, no destructive ops
- **Rich Documentation** - Installation guides, troubleshooting, customization

## Quick Start

### Installation

This skill is already installed in the `generated-skills/hook-factory/` directory.

### Usage with Claude Code

Simply describe what you want:

```
"I need a hook to auto-format Python files after editing"
```

Claude Code will:
1. Invoke the hook-factory skill
2. Generate the hook configuration
3. Validate it for safety
4. Save to `generated-hooks/auto-format-code-after-editing-python/`
5. Provide installation instructions

### Command Line Usage

You can also use the hook factory directly from command line:

```bash
# Natural language generation
cd generated-skills/hook-factory
python hook_factory.py -r "auto-format Python files after editing"

# Template-based generation
python hook_factory.py -t post_tool_use_format -l python

# List available templates
python hook_factory.py --list
```

## Supported Hook Types

### 1. PostToolUse Auto-Format

Automatically format code after editing.

**Example Request:**
```
"Auto-format my Python code after editing"
"Format JavaScript files with prettier"
```

**What It Creates:**
- Hook that runs after Write/Edit tools
- Language-specific formatter (black, prettier, rustfmt, gofmt)
- Tool detection and silent failure

**Languages:** Python, JavaScript, TypeScript, Rust, Go

### 2. PostToolUse Git Auto-Add

Automatically stage files with git after editing.

**Example Request:**
```
"Automatically add files to git when I edit them"
"Auto-stage modified files"
```

**What It Creates:**
- Hook that runs after Write/Edit tools
- Git repository detection
- Silent failure if not a git repo

**Languages:** All

### 3. SubagentStop Test Runner

Run tests when agent completes work.

**Example Request:**
```
"Run tests after agent finishes coding"
"Execute pytest when agent completes"
```

**What It Creates:**
- Hook that runs when agent finishes
- Test framework detection
- Language-specific test commands

**Languages:** Python (pytest), JavaScript (jest), Rust (cargo), Go (go test)

### 4. SessionStart Context Loader

Load project context when session starts.

**Example Request:**
```
"Load my TODO.md at session start"
"Show project status when Claude starts"
```

**What It Creates:**
- Hook that runs on session startup/resume
- File existence checks
- Graceful handling if file missing

**Languages:** All

## File Structure

```
generated-skills/hook-factory/
├── SKILL.md               # Skill manifest (read by Claude Code)
├── README.md              # This file
├── hook_factory.py        # Main orchestrator (CLI entry point)
├── generator.py           # Template substitution engine
├── validator.py           # JSON validation & safety checks
├── templates.json         # Hook pattern templates
└── examples/              # Reference implementations
    ├── auto-format-python/
    │   ├── hook.json
    │   └── README.md
    ├── git-auto-add/
    │   ├── hook.json
    │   └── README.md
    ├── test-runner/
    │   ├── hook.json
    │   └── README.md
    └── load-context/
        ├── hook.json
        └── README.md
```

## Output Structure

Generated hooks are saved to `generated-hooks/` at project root:

```
generated-hooks/
└── [hook-name]/
    ├── hook.json      # Complete hook configuration (validated JSON)
    └── README.md      # Installation guide, usage, troubleshooting
```

### hook.json Format

```json
{
  "matcher": {
    "tool_names": ["Write", "Edit"]
  },
  "hooks": [
    {
      "type": "command",
      "command": "if ! command -v black &> /dev/null; then\n    exit 0\nfi\n\nif [[ \"$CLAUDE_TOOL_FILE_PATH\" == *.py ]]; then\n    black \"$CLAUDE_TOOL_FILE_PATH\" || exit 0\nfi",
      "timeout": 60
    }
  ],
  "_metadata": {
    "generated_by": "hook-factory",
    "generated_at": "2025-10-30T10:15:00Z",
    "template": "post_tool_use_format",
    "language": "python"
  }
}
```

## Safety & Validation

Every generated hook is validated for:

### Critical Checks (Errors)
- ❌ Destructive operations (rm -rf, git push --force, etc.)
- ❌ Missing required fields (matcher, hooks, type, command)
- ❌ Invalid JSON syntax
- ❌ Invalid timeouts (<1s or >600s)

### Best Practice Checks (Warnings)
- ⚠️ Missing tool detection for external tools
- ⚠️ Missing silent failure patterns
- ⚠️ Unknown tool names in matchers
- ⚠️ Potentially invalid glob patterns
- ⚠️ Potential hardcoded secrets

### Safety Features in Generated Hooks

All hooks include:

1. **Tool Detection**
   ```bash
   if ! command -v black &> /dev/null; then
       exit 0
   fi
   ```

2. **Silent Failure**
   ```bash
   black "$CLAUDE_TOOL_FILE_PATH" || exit 0
   ```

3. **File Checks**
   ```bash
   if [ -z "$CLAUDE_TOOL_FILE_PATH" ]; then
       exit 0
   fi
   ```

4. **Appropriate Timeouts**
   - PostToolUse: 60s (must be fast)
   - SubagentStop: 120s (can be slower)
   - SessionStart: 60s (should be fast)

## Installation of Generated Hooks

### Manual Installation (Current)

1. **Navigate to generated hook**
   ```bash
   cd generated-hooks/[hook-name]
   ```

2. **Review files**
   ```bash
   cat README.md
   cat hook.json
   ```

3. **Copy to Claude Code settings**
   - Open `.claude/settings.json` (project) or `~/.claude/settings.json` (user)
   - Add hook configuration to appropriate event type array
   - Save and restart Claude Code

4. **Verify**
   - Check logs: `~/.claude/logs/`
   - Test by performing trigger action

### Automated Installation (Coming Soon)

Future versions will include install scripts.

## Examples

### Example 1: Auto-Format Python

**Request:**
```
"I want to auto-format my Python code with black after editing"
```

**Generated Files:**
```
generated-hooks/auto-format-code-after-editing-python/
├── hook.json      # PostToolUse hook with black formatter
└── README.md      # Installation and usage guide
```

**Hook Behavior:**
- Triggers after editing any `.py` file
- Checks if `black` is installed
- Formats the file
- Silent failure if black missing or format fails
- Completes in <1 second

### Example 2: Git Auto-Add

**Request:**
```
"Automatically stage files with git when I edit them"
```

**Generated Files:**
```
generated-hooks/auto-add-files-to-git-after-editing/
├── hook.json      # PostToolUse hook with git add
└── README.md      # Installation and usage guide
```

**Hook Behavior:**
- Triggers after editing any file
- Checks if git repository
- Stages the modified file
- Silent failure if not a git repo
- Completes in <1 second

### Example 3: Test Runner

**Request:**
```
"Run pytest tests when the agent finishes coding"
```

**Generated Files:**
```
generated-hooks/run-tests-when-agent-completes-python/
├── hook.json      # SubagentStop hook with pytest
└── README.md      # Installation and usage guide
```

**Hook Behavior:**
- Triggers when agent completes its task
- Checks if `pytest` is installed
- Runs tests with verbose output
- Silent failure if pytest missing or tests fail
- Can take longer (120s timeout)

## Customization

### Modifying Generated Hooks

After generation, you can customize hooks by editing `hook.json`:

**Change formatter options:**
```json
"command": "black --line-length 100 \"$CLAUDE_TOOL_FILE_PATH\" || exit 0"
```

**Add file filtering:**
```bash
if [[ "$CLAUDE_TOOL_FILE_PATH" == src/*.py ]]; then
    black "$CLAUDE_TOOL_FILE_PATH" || exit 0
fi
```

**Combine multiple formatters:**
```bash
if [[ "$CLAUDE_TOOL_FILE_PATH" == *.py ]]; then
    isort "$CLAUDE_TOOL_FILE_PATH" || exit 0
    black "$CLAUDE_TOOL_FILE_PATH" || exit 0
elif [[ "$CLAUDE_TOOL_FILE_PATH" == *.js ]]; then
    prettier --write "$CLAUDE_TOOL_FILE_PATH" || exit 0
fi
```

### Creating Custom Templates

To add new hook patterns:

1. Edit `templates.json`
2. Add new template with metadata and variables
3. Update keyword matching in `generator.py`
4. Create example in `examples/`
5. Test with `python hook_factory.py`

## Troubleshooting

### Hook Factory Issues

**"Could not determine hook type from request"**
- Use more specific keywords (format, test, git add, load)
- Try explicit template: `python hook_factory.py -t template_name -l language`
- List templates: `python hook_factory.py --list`

**Validation errors**
- Review error messages and fix suggestions
- Check for destructive commands
- Ensure tool detection is present
- Verify JSON syntax

### Generated Hook Issues

**Hook not triggering**
- Check Claude Code logs: `~/.claude/logs/`
- Verify event type matches use case
- Check matcher patterns
- Ensure hook is in correct event type array

**Command errors**
- Verify required tools are installed
- Test command manually in terminal
- Check timeout settings
- Review README.md troubleshooting section

## Technical Details

### Architecture

```
User Request
    ↓
[Keyword Matching] → Simple pattern detection
    ↓
[Template Selection] → Choose from 4 patterns
    ↓
[Variable Substitution] → Fill in language-specific values
    ↓
[Safety Validation] → Check for issues
    ↓
[File Generation] → Create hook.json + README.md
    ↓
Generated Hook in generated-hooks/
```

### Dependencies

- **Python:** 3.7+
- **Standard Library Only:** No external dependencies

### Validation Rules

See `validator.py` for complete validation logic:

- **Destructive patterns:** rm -rf, git push --force, DROP TABLE, chmod 777
- **Required safety:** Tool detection, silent failure
- **Timeout limits:** 1s - 600s
- **Valid tool names:** Read, Write, Edit, Bash, etc.

## Limitations

**Hook Factory v2.0** is a production-ready system. Current capabilities:

- ✅ **Supported:** 10 production hook templates
- ✅ **Supported:** 5 languages (Python, JS, TS, Rust, Go)
- ✅ **Supported:** 7 event types (PostToolUse, SubagentStop, SessionStart, PreToolUse, UserPromptSubmit, Stop, PrePush)
- ✅ **Supported:** Interactive mode with 7-question flow
- ✅ **Supported:** Automated installation/uninstall (Python + Bash)
- ✅ **Supported:** Enhanced validation (secrets, events, commands)
- ✅ **Supported:** macOS and Linux (Unix environments)

**Current Limitations:**

- ❌ **Not supported:** Windows (Unix commands, bash-specific syntax)
- ❌ **Not yet:** Template composition (combine multiple patterns)
- ❌ **Not yet:** GUI interface (CLI only)
- ❌ **Not yet:** Educational annotations explaining design choices
- ❌ **Not yet:** Test scripts to simulate hook execution
- ❌ **Not yet:** Advanced intent analysis (better keyword matching)

## Future Enhancements

**Potential v3.0 Features:**

- 🧩 Template composition (combine multiple patterns into one hook)
- 🎓 Educational annotations explaining each design choice
- 🧪 Test scripts to simulate hook execution before installation
- 🎯 Advanced intent analysis with better keyword matching
- 🪟 Windows support (PowerShell-based hooks)
- 🎨 GUI interface for visual hook building
- 📊 Hook analytics and usage tracking

## Contributing

To contribute new hook patterns:

1. Add template to `templates.json` with full metadata
2. Update keyword matching in `generator.py`
3. Create working example in `examples/`
4. Add validation rules if needed in `validator.py`
5. Update this README.md and SKILL.md

## Resources

- **Claude Code Hooks Documentation:** https://docs.claude.com/en/docs/claude-code/hooks
- **Hook Reference Examples:** See `examples/` directory
- **Validation Logic:** See `validator.py`
- **Template Format:** See `templates.json`

## Version History

- **2.0.0** (2025-11-06) - Major update with interactive mode and automated installation
  - 10 production hook templates (was 4)
  - 7 event types supported (was 3)
  - Interactive mode with 7-question flow and smart defaults
  - Automated installation system (Python + Bash installers)
  - Enhanced validation (secrets detection, event-specific rules, command validation)
  - macOS/Linux optimization
  - Auto-install integration
  - Backup/rollback system

- **1.0.0** (2025-10-30) - Initial release
  - 4 core hook patterns
  - 5 language support
  - Natural language generation
  - Comprehensive validation
  - Safety-first approach

## License

Part of Claude Code Skills Factory - Example skill for educational purposes.

---

**Generated by Claude Code Skills Factory**
**Last Updated:** 2025-10-30
**Maintainer:** hook-factory skill
