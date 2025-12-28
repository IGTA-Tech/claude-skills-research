# 📚 Claude Skills Development Guide

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/sanshao85/claude-skills-guide?style=social)](https://github.com/sanshao85/claude-skills-guide/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sanshao85/claude-skills-guide?style=social)](https://github.com/sanshao85/claude-skills-guide/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[🇨🇳 中文](./README.md) | **🇺🇸 English**

</div>

> 📖 A comprehensive guide to creating professional Claude Skills - from basics to mastery

---

## 🎯 What is Claude Skills?

**Claude Skills** are standardized capability packages that encapsulate expert knowledge into files, enabling Claude to perform more professionally on specific tasks.

### Core Components

Each Skill consists of three parts:

1. **SKILL.md** - Main instruction file (required)
2. **scripts/** - Executable code (optional)
3. **reference/** - Reference resources (optional)

### How It Works

Skills use a **progressive disclosure** mechanism with three loading levels:

- **Level 1**: Metadata (name + description) - Always loaded, ~100 tokens
- **Level 2**: Instructions (SKILL.md body) - Loaded when triggered, ~5k tokens
- **Level 3**: Resources and code - Loaded on demand

This design maximizes token efficiency by loading detailed content only when needed.

---

## 📦 What's Included?

### 📖 Core Documentation (3 files)

1. **README.md** - Project introduction and quick start
2. **Claude_Skills_开发完全指南.md** - Detailed development guide (2500+ lines, Chinese)
3. **快速参考卡片.md** - Templates and checklists (Chinese)

### 🎨 Official Examples (20 Skills)

**anthropic-skills/** - Official Anthropic Skills repository with:

**Creative & Design:**
- algorithmic-art
- canvas-design
- slack-gif-creator

**Development & Technical:**
- artifacts-builder
- mcp-builder
- webapp-testing

**Enterprise & Communication:**
- brand-guidelines
- internal-comms
- theme-factory

**Document Processing:**
- document-skills/docx
- document-skills/pdf
- document-skills/pptx
- document-skills/xlsx

**Meta Skills:**
- skill-creator
- template-skill

**Additional Examples:**
- claude-cookbooks/skills/ - 3 financial examples

---

## 🚀 Quick Start (5 Minutes)

### Step 1: View a Simple Skill

```bash
# View the simplest template
cat anthropic-skills/template-skill/SKILL.md
```

A basic Skill looks like this:

```markdown
---
name: my-skill
description: Describe what this Skill does and when to use it
---

# My Skill

[Add your instructions here...]

## Examples
- Example 1
- Example 2
```

### Step 2: Create Your First Skill

```bash
# Create directory
mkdir my-first-skill
cd my-first-skill

# Create SKILL.md
cat > SKILL.md << 'EOF'
---
name: greeting-expert
description: Professional greeting generator that creates appropriate greetings based on time and occasion
---

# Greeting Expert

You are a greeting generation expert. Generate appropriate greetings based on user-provided information.

## Instructions

1. Ask the user what type of greeting they need
2. Consider factors like time, occasion, and audience
3. Generate 3-5 greeting options in different styles
4. Explain the appropriate scenario for each greeting

## Examples

User: "I need a morning business greeting"
Response:
1. "Good morning! Wishing you a productive day!" (Formal)
2. "Morning! New day, new beginnings!" (Positive)
3. "Hello! Delighted to see you on this beautiful morning!" (Warm)
EOF
```

### Step 3: Use Your Skill

Upload this Skill folder in Claude.ai, Claude Code, or via API, and you're ready to go!

---

## 📖 Learning Paths

### 🎯 Beginner (1-2 hours)

**Goal**: Understand Skills basics, create simple Skill

1. **Read this README** (15 min)
2. **View template-skill** (15 min)
3. **Study 2-3 simple examples** (30 min)
   - brand-guidelines
   - internal-comms
4. **Create your first Skill** (30 min)
   - SKILL.md only
   - No scripts needed

### 🎓 Intermediate (3-5 hours)

**Goal**: Master best practices, create Skills with scripts

1. **Read core chapters of the guide** (2 hours)
   - Chapter 5: SKILL.md writing
   - Chapter 6: Scripts development
   - Chapter 8: Best practices
2. **Study complex examples** (1 hour)
   - mcp-builder
   - webapp-testing
   - document-skills
3. **Create Skill with scripts** (2 hours)

### 🚀 Advanced (5+ hours)

**Goal**: Master Skills development, create production-grade Skills

1. **Complete the full guide** (3 hours)
2. **Study all official examples** (2 hours)
3. **Create production-grade Skills** (multiple iterations)

---

## 💡 Key Points

### ✅ Good Skills Should:

- **Be concise** - Only teach what Claude doesn't know
- **Be precise** - Description accurately describes use cases
- **Be structured** - Use clear steps and examples
- **Be testable** - Provide specific usage examples
- **Be moderate** - Keep SKILL.md under 500 lines

### ❌ Avoid These Mistakes:

- Over-explaining basics Claude already knows
- Including time-sensitive information that becomes outdated
- Making SKILL.md too long (over 1000 lines)
- Lacking specific usage examples
- Having vague descriptions

---

## 📚 Documentation Navigation

| Need | Recommended Doc |
|------|----------------|
| **Quick overview** | This README |
| **Deep learning** | Claude_Skills_开发完全指南.md (Chinese) |
| **Quick reference** | 快速参考卡片.md (Chinese) |
| **View examples** | anthropic-skills/ |

---

## 🤝 Contributing

Contributions are welcome! Please see [Contributing Guide](./CONTRIBUTING.md) for details.

**Ways to contribute:**
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🎨 Share your skills
- 🌍 Translate docs

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🙏 Acknowledgments

Thanks to:
- [Anthropic](https://www.anthropic.com/) for official documentation and examples
- All contributors for their support and help
- Claude Skills community

---

## ⭐ Star History

If this project helps you, please give it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=sanshao85/claude-skills-guide&type=Date)](https://star-history.com/#sanshao85/claude-skills-guide&Date)

---

**Happy Skill Development!** 🚀

