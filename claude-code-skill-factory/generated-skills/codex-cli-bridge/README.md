# Codex CLI Bridge Skill

**Bridge between Claude Code and OpenAI Codex CLI for seamless cross-tool collaboration**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-Apache%202.0-orange)

---

## 🎯 What is This?

The **Codex CLI Bridge** creates seamless interoperability between **Claude Code** and **OpenAI's Codex CLI** by:

1. **Generating AGENTS.md from CLAUDE.md** - Translates Claude Code configuration to Codex CLI format
2. **Documenting Skills for Codex Users** - Shows how to use Claude Skills with Codex CLI
3. **Providing Execution Helpers** - Python wrappers for Codex CLI commands

**The Problem**: Teams using both Claude Code and Codex CLI maintain duplicate documentation and can't easily share skills/workflows.

**The Solution**: This bridge auto-generates AGENTS.md from CLAUDE.md with file references (no duplication), enabling both tools to work with the same project structure.

---

## ✨ Key Features

### 1. Documentation Translation
- ✅ **CLAUDE.md → AGENTS.md** automatic generation
- ✅ **Reference-based** (links to files, no duplication)
- ✅ **One-way sync** (CLAUDE.md is source of truth)

### 2. Skill Documentation
- ✅ **Functional skills**: Bash execution examples
- ✅ **Prompt-based skills**: Codex prompt templates
- ✅ **Most relevant method** per skill type

### 3. Safety Mechanisms
- ✅ **Auto-checks Codex CLI** installation
- ✅ **Auto-runs /init** if CLAUDE.md missing
- ✅ **User-friendly notifications**

### 4. Codex Execution Helpers
- ✅ **Python wrappers** for Codex CLI commands
- ✅ **Always uses `codex exec`** (not plain `codex`)
- ✅ **Intelligent model selection** (gpt-5 vs gpt-5-codex)
- ✅ **Sandbox mode helpers** (read-only, workspace-write)

---

## 🚀 Quick Start

### Prerequisites

```bash
# 1. Codex CLI installed
codex --version  # Should show v0.48.0+

# 2. Python 3.7+ with PyYAML
python3 --version
pip3 install PyYAML

# 3. Claude Code project (or auto-create)
```

### Generate AGENTS.md in 3 Steps

```bash
# 1. Navigate to your project
cd /your/claude-code-project

# 2. Run the bridge
python /path/to/codex-cli-bridge/bridge.py

# 3. Done! ✅
# AGENTS.md created in project root
```

**Output**:
```
================================================================
✅ SUCCESS - AGENTS.MD GENERATED
================================================================

📄 Output: /your/project/AGENTS.md
📊 Skills documented: 13
🤖 Agents documented: 59

Next steps:
  1. Review AGENTS.md
  2. Test with Codex CLI
  3. Share with team (works in both Claude Code and Codex CLI)
```

---

## 📦 What's Included

### Python Modules

| Module | Purpose |
|--------|---------|
| `bridge.py` | Main orchestrator (runs complete workflow) |
| `safety_mechanism.py` | Environment validation (Codex CLI + CLAUDE.md checks) |
| `claude_parser.py` | Parse CLAUDE.md and project structure |
| `project_analyzer.py` | Analyze project metadata and structure |
| `agents_md_generator.py` | Generate AGENTS.md (template-based) |
| `skill_documenter.py` | Document skills for Codex CLI users |
| `codex_executor.py` | Codex CLI execution helpers |

### Documentation

| File | Description |
|------|-------------|
| `SKILL.md` | Complete skill reference |
| `README.md` | This file |
| `HOW_TO_USE.md` | Comprehensive usage guide |

### Templates

| Template | Purpose |
|----------|---------|
| `templates/` | AGENTS.md generation templates (future) |

---

## 📖 Usage Examples

### Example 1: Basic Generation

```bash
# Generate AGENTS.md for current directory
python bridge.py
```

### Example 2: Specific Project

```bash
# Generate for a different project
python bridge.py --project /path/to/other/project
```

### Example 3: Validate Only

```bash
# Check environment without generating
python bridge.py --validate
```

### Example 4: Python API

```python
from bridge import CodexCliBridge

# Create bridge
bridge = CodexCliBridge(project_root="/your/project")

# Run complete workflow
success = bridge.run()

if success:
    print("✅ AGENTS.md generated successfully")
```

### Example 5: Codex Execution Helper

```python
from codex_executor import CodexExecutor, CodexModel

executor = CodexExecutor()

# Execute analysis task
result = executor.exec_analysis(
    prompt="Analyze this codebase for security issues",
    model=CodexModel.GPT5
)

print(result.stdout)
```

---

## 🎓 How It Works

### Architecture

```
Claude Code Project
├── CLAUDE.md (Source of truth)
├── .claude/
│   ├── skills/
│   └── agents/
└── documentation/

       ↓ bridge.py

1. Safety Check
   ├── Codex CLI installed? ✅
   └── CLAUDE.md exists? ✅ (auto-create if missing)

2. Parse & Analyze
   ├── Parse CLAUDE.md sections
   ├── Scan skills (functional vs prompt-based)
   ├── Scan agents
   └── Analyze project structure

3. Generate AGENTS.md
   ├── Project overview
   ├── Skills documentation (Codex CLI usage)
   ├── Workflow patterns (slash commands → Codex)
   ├── MCP integration
   └── Command reference

4. Write AGENTS.md
   └── Output: AGENTS.md (reference-based, 19KB example)

Result: Claude Code & Codex CLI Interoperability ✅
```

---

## 🔧 Configuration

### Default Behavior

- **Auto-init**: Yes (runs /init if CLAUDE.md missing)
- **Output**: AGENTS.md in project root
- **Approach**: Reference-based (no file duplication)
- **Sync**: One-way (CLAUDE.md → AGENTS.md)

### Customize Behavior

```bash
# Disable auto-init
python bridge.py --no-auto-init

# Show status only
python bridge.py --status

# Validate only (no generation)
python bridge.py --validate
```

---

## 🧪 Testing

### Test on This Repository

```bash
# Navigate to codex-cli-bridge folder
cd generated-skills/codex-cli-bridge

# Generate AGENTS.md for claude-code-skills-factory
python bridge.py --project ../..

# Check output
cat ../../AGENTS.md
```

**Expected Results**:
- ✅ AGENTS.md created (19KB, 629 lines)
- ✅ 13 skills documented (8 functional, 5 prompt-based)
- ✅ 59 agents documented
- ✅ All file references valid

---

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| "Codex CLI not found" | Install Codex CLI: `which codex` |
| "ModuleNotFoundError: yaml" | Install PyYAML: `pip3 install PyYAML` |
| "CLAUDE.md not found" | Let auto-init create it (default) or run `/init` |
| "stdout is not a terminal" | Use `codex exec` not plain `codex` (skill does this automatically) |
| AGENTS.md out of sync | Regenerate: `python bridge.py` |

### Get Help

```bash
# Show help
python bridge.py --help

# Check status
python bridge.py --status

# Validate environment
python bridge.py --validate
```

See [HOW_TO_USE.md](HOW_TO_USE.md) for comprehensive troubleshooting.

---

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete skill reference
- **[HOW_TO_USE.md](HOW_TO_USE.md)** - Comprehensive usage guide
- **[AGENTS.md](../../AGENTS.md)** - Example output (this repository)
- **[Codex CLI Docs](https://github.com/openai/codex)** - Official Codex documentation

---

## 🎯 Use Cases

### 1. Cross-Tool Teams

**Scenario**: Team uses both Claude Code and Codex CLI

**Solution**:
- Developers using Claude Code maintain CLAUDE.md
- Developers using Codex CLI use AGENTS.md
- Both files reference same skills, agents, documentation
- Bridge keeps AGENTS.md in sync

### 2. Project Migration

**Scenario**: Migrating from Claude Code to Codex CLI (or vice versa)

**Solution**:
- Generate AGENTS.md for existing Claude Code project
- Codex CLI users have instant documentation
- Skills remain usable (Python scripts execute directly)
- Gradual migration possible

### 3. CI/CD Integration

**Scenario**: Auto-sync AGENTS.md when CLAUDE.md changes

**Solution**:
```yaml
# .github/workflows/sync-agents-md.yml
on:
  push:
    paths: ['CLAUDE.md']
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: python /path/to/bridge.py
      - run: git add AGENTS.md && git commit && git push
```

### 4. Skills Marketplace

**Scenario**: Share Claude Skills with Codex CLI users

**Solution**:
- Include both CLAUDE.md and AGENTS.md in skill package
- Claude Code users: Auto-load from CLAUDE.md
- Codex CLI users: Follow AGENTS.md documentation
- Universal compatibility

---

## 🤝 Contributing

This skill was created as part of the **Claude Code Skills Factory**.

**Improvements Welcome**:
- Bidirectional sync (AGENTS.md → CLAUDE.md) - planned for v2.0
- Watch mode (auto-regenerate on file changes)
- Additional templates
- More execution helpers

---

## 📄 License

**Apache 2.0**

---

## 🌟 Version

**v1.0.0** - Initial Release (2025-10-30)

**Features**:
- ✅ CLAUDE.md → AGENTS.md generation
- ✅ Reference-based architecture (no duplication)
- ✅ Safety mechanisms (Codex CLI + CLAUDE.md checks)
- ✅ Skill documentation (functional vs prompt-based)
- ✅ Codex execution helpers
- ✅ Command reference table
- ✅ Workflow patterns (Claude → Codex)

**Future (v2.0)**:
- 🔄 Bidirectional sync
- 🔄 Watch mode
- 🔄 Additional templates
- 🔄 Plugin integration

---

## 🙏 Acknowledgments

- **OpenAI** - Codex CLI
- **Anthropic** - Claude Code
- **Skills Factory** - Comprehensive skill generation templates

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Documentation**: See HOW_TO_USE.md
- **Examples**: See AGENTS.md in this repository

---

**Built with ❤️ for cross-tool collaboration**

**Claude Code ↔ Codex CLI Bridge v1.0.0**
