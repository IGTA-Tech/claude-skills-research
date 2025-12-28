# Quick Start Guide

## Installation (30 seconds)

### For Personal Use (All Projects)

```bash
# 1. Extract a skill
unzip screenshot-to-code.zip

# 2. Copy to personal skills
mkdir -p ~/.claude/skills
cp -r screenshot-to-code ~/.claude/skills/

# 3. Restart Claude or run debug
claude --debug
```

### For One Project

```bash
# 1. Extract skill
unzip screenshot-to-code.zip

# 2. Copy to project (from project root)
mkdir -p .claude/skills
cp -r screenshot-to-code .claude/skills/

# 3. Restart Claude
claude --debug
```

## Usage

**Just ask naturally!** Skills activate automatically.

### Example Requests

| What You Say | Skill That Activates |
|--------------|---------------------|
| "Convert this screenshot to React code" | Screenshot to Code |
| "Optimize this blog post for SEO" | SEO Content Optimizer |
| "What does Reddit think about this?" | Reddit Thread Analyzer |
| "Extract action items from this meeting" | Meeting Intelligence |
| "Parse this invoice" | Financial Document Parser |
| "Review this code for security issues" | Code Review Pro |
| "Debug this regex pattern" | Regex Visual Debugger |
| "Turn this article into a Twitter thread" | Social Media Repurposer |
| "Review this contract" | Contract Analyzer |
| "Repurpose this podcast transcript" | Podcast to Content Suite |

## Available Skills

✅ **screenshot-to-code** - UI to code conversion
✅ **reddit-analyzer** - Reddit sentiment analysis
✅ **seo-optimizer** - SEO content optimization
✅ **meeting-intelligence** - Meeting analysis
✅ **financial-parser** - Invoice/receipt parsing
✅ **code-review-pro** - Security & performance review
✅ **regex-debugger** - Regex debugging & explanation
✅ **social-repurposer** - Cross-platform content
✅ **contract-analyzer** - Contract risk analysis
✅ **podcast-content-suite** - Podcast to content marketing

## Troubleshooting

**Skill not activating?**

1. Check file location: `~/.claude/skills/skill-name/SKILL.md`
2. Run `claude --debug` to see errors
3. Be more explicit: "Use SEO optimizer to check this post"

**YAML error?**

Check your SKILL.md has:
```yaml
---
name: Skill Name
description: Description text
---
```

## File Structure

```
~/.claude/skills/           ← Personal (all projects)
  skill-name/
    SKILL.md               ← Required

.claude/skills/            ← Project-specific
  skill-name/
    SKILL.md
```

## Next Steps

1. Install 1-2 skills you'll use most
2. Try them with natural requests
3. Install more as needed
4. Customize for your workflow

**Full documentation**: See README.md
