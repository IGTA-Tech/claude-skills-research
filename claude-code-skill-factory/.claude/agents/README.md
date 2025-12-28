# Factory Navigation Agents

**Interactive guide system for building custom Skills, Prompts, and Agents using the Claude Code Skills Factory.**

---

## 🎯 Navigation System Overview

**Architecture**: Orchestrator + 3 Specialists

```
User Request
    ↓
factory-guide (Orchestrator)
    ├→ skills-guide (Build Claude Skills)
    ├→ prompts-guide (Generate Mega-Prompts)
    └→ agents-guide (Build Claude Agents)
```

---

## 🤖 Available Agents (4 Total)

### 1. factory-guide (Orchestrator) - START HERE

**Purpose**: Main entry point - asks what you want to build and delegates to specialists

**Use when**: "I want to build something" or "Help me with the skills factory"

**What it does**:
- Asks 1 simple question: What to build? (Skill, Prompt, or Agent)
- Delegates to appropriate specialist
- Provides final summary

**Tools**: Read, Grep (lightweight)
**Model**: haiku (fast)
**Color**: Purple (orchestration)

**Invoke**:
```
I want to build something for my project
```

---

### 2. skills-guide (Specialist)

**Purpose**: Build custom Claude Skills (multi-file capabilities)

**Questions**: 4-5 straightforward
1. Business type/domain?
2. What tasks should the skill handle?
3. Need Python code or just prompts?
4. How many skills to generate?
5. Any special requirements?

**What it generates**:
- Complete skill folder (SKILL.md, Python if needed, samples)
- ZIP file for distribution
- Validation of YAML frontmatter
- Installation instructions

**Tools**: Read, Write, Bash, Grep, Glob (full file creation)
**Model**: sonnet (intelligent)
**Color**: Blue (strategic)

**Example**:
```
Help me build a skill for analyzing customer feedback
```

**Output**: generated-skills/customer-feedback-analyzer/

---

### 3. prompts-guide (Specialist)

**Purpose**: Generate mega-prompts using prompt-factory skill

**Questions**: 3-4 simple
1. Preset (69 options) or Custom?
2. What role? (if custom)
3. Output format? (XML/Claude/ChatGPT/Gemini)
4. Core or Advanced mode?

**What it does**:
- Guides you to use the prompt-factory skill
- Helps choose from 69 professional presets
- Explains format differences
- Shows how to use generated prompts

**Tools**: Read, Grep (navigation only)
**Model**: haiku (fast guidance)
**Color**: Orange (specialist)

**Example**:
```
I need a prompt for a Senior Backend Engineer
```

**Output**: Mega-prompt ready for any LLM

---

### 4. agents-guide (Specialist)

**Purpose**: Build custom Claude Code Agents (subagents)

**Questions**: 5-6 straightforward
1. What should this agent do?
2. Agent type? (Strategic/Implementation/Quality/Coordination)
3. Which tools?
4. Model preference?
5. Field/domain?
6. Expertise level?

**What it generates**:
- Complete agent .md file
- Enhanced YAML frontmatter (tools, model, color, field, expertise)
- Validation of format
- Installation to .claude/agents/ or ~/.claude/agents/

**Tools**: Read, Write, Grep (file creation)
**Model**: sonnet (intelligent)
**Color**: Green (implementation)

**Example**:
```
Build me an agent that reviews code for security vulnerabilities
```

**Output**: .claude/agents/security-reviewer.md

---

## 🚀 How to Use

### Quick Start

**Just ask**:
```
I want to build something
```

Or be specific:
```
Help me build a skill for healthcare data analysis
I need a prompt for a Marketing Strategist
Create an agent that runs tests
```

**factory-guide will**:
1. Understand your goal
2. Delegate to the right specialist
3. Let the specialist guide you through questions
4. Help you get a complete, working result

---

### Detailed Usage

**For Skills** (Multi-file capabilities):
```
"I want to build a custom Claude Skill"
```
→ factory-guide delegates to skills-guide
→ skills-guide asks 4-5 questions
→ Generates complete skill folder + ZIP
→ Helps you install

**For Prompts** (Mega-prompts):
```
"I need a prompt for a Product Manager"
```
→ factory-guide delegates to prompts-guide
→ prompts-guide helps you use prompt-factory skill
→ Choose preset or custom
→ Get validated mega-prompt

**For Agents** (Claude Code specialists):
```
"Build me a code reviewer agent"
```
→ factory-guide delegates to agents-guide
→ agents-guide asks 5-6 questions
→ Generates agent .md file
→ Installs to .claude/agents/ or ~/.claude/agents/

---

## 📋 What Each Agent Asks

### factory-guide (1-2 questions)
- What do you want to build? (Skill, Prompt, or Agent)
- Any special context? (optional)

### skills-guide (4-5 questions)
- Business type/domain?
- Specific use cases?
- Python or prompts only?
- How many skills?
- Special requirements? (optional)

### prompts-guide (3-4 questions)
- Preset or custom?
- Which preset? (if preset) / What role? (if custom)
- Output format?
- Core or Advanced mode?

### agents-guide (5-6 questions)
- Agent purpose?
- Agent type?
- Tools needed?
- Model preference?
- Field/domain?
- Expertise level?

**Total Questions**: 6-11 depending on path (not overwhelming!)

---

## 🎯 Agent Capabilities

### All Agents Can
- ✅ Ask interactive questions (conversational)
- ✅ Wait for user responses
- ✅ Provide examples and suggestions
- ✅ Validate user input
- ✅ Generate complete outputs
- ✅ Create files
- ✅ Help with installation

### Automation Included
- ✅ Template filling (automatic)
- ✅ Validation (YAML, naming, format)
- ✅ File creation (SKILL.md, agent .md, Python, ZIPs)
- ✅ Installation guidance (step-by-step)

### Works With Existing
- ✅ Uses SKILLS_FACTORY_PROMPT template
- ✅ Uses prompt-factory skill
- ✅ Uses AGENTS_FACTORY_PROMPT template
- ✅ Uses agent-factory skill
- ✅ Enhances (doesn't duplicate) existing system

---

## 💡 Tips

**For Best Results**:
- Be specific in your answers
- Provide examples when describing use cases
- Mention any compliance needs (HIPAA, GDPR, etc.)
- Specify tech stack if relevant

**If Unsure**:
- Just start with factory-guide
- Answer questions naturally
- The agents will guide you
- You can always regenerate or customize

**Testing**:
- Test generated skills/prompts/agents before production
- Customize as needed
- Iterate based on results

---

## 📚 Examples

### Example 1: Building a Healthcare Skill

```
User: "Help me build a healthcare skill"

factory-guide: "What do you want to build? (Skill/Prompt/Agent): ___"

User: "Skill"

skills-guide: "Question 1: Domain?"
User: "Healthcare"

skills-guide: "Question 2: Use cases?"
User: "Medical terminology translation, patient education"

[Continues through questions...]

Result: generated-skills/medical-translator/ + ZIP file
```

### Example 2: Getting a Prompt

```
User: "I need a prompt for a Data Scientist"

factory-guide: [Delegates to prompts-guide]

prompts-guide: "Preset or Custom?"
User: "Preset"

prompts-guide: "Data Scientist is preset #4. Format?"
User: "ChatGPT"

prompts-guide: "Core or Advanced?"
User: "Core"

Result: ChatGPT-ready Data Scientist prompt (5K tokens)
```

### Example 3: Creating an Agent

```
User: "Build a code reviewer agent"

factory-guide: [Delegates to agents-guide]

agents-guide: "What should it do?"
User: "Review code for bugs and security issues"

[Answers 4 more questions...]

Result: .claude/agents/code-reviewer.md
```

---

## 🔧 Troubleshooting

**Agent Not Auto-Invoking**:
- Check /agents to see if it's loaded
- Make description more specific
- Invoke manually: "Use the [agent-name] agent to..."

**Questions Unclear**:
- Just answer naturally - agents will clarify if needed
- Provide examples when helpful
- Ask the agent to rephrase if confused

**Want to Modify Generated Output**:
- Edit the generated files directly
- Or ask the agent to regenerate with changes
- Files are in generated-skills/ or .claude/agents/

---

## 📍 File Locations

**These Agents** (Project-level):
```
.claude/agents/factory-guide.md
.claude/agents/skills-guide.md
.claude/agents/prompts-guide.md
.claude/agents/agents-guide.md
```

**Generated Outputs**:
- Skills: `generated-skills/[skill-name]/`
- Prompts: In conversation (copy-paste)
- Agents: `.claude/agents/[agent-name].md` or `~/.claude/agents/[agent-name].md`

---

## ✅ Quick Reference

| Want to Build | Use Agent | Questions | Output |
|---------------|-----------|-----------|--------|
| **Claude Skill** | skills-guide | 4-5 | Skill folder + ZIP |
| **Mega-Prompt** | prompts-guide | 3-4 | Ready-to-use prompt |
| **Claude Agent** | agents-guide | 5-6 | Agent .md file |
| **Not sure** | factory-guide | 1-2 | Delegates to specialist |

---

## 🎯 Start Here

**First time?** Just ask:
```
I want to build something
```

**Know what you need?** Be specific:
```
Build a skill for [purpose]
Generate a prompt for [role]
Create an agent for [task]
```

**factory-guide will understand and delegate to the right specialist!**

---

**Last Updated**: October 28, 2025
**Version**: 1.0.0
**Status**: ✅ Ready to use

**Welcome to the easiest way to build Skills, Prompts, and Agents!** 🏭
