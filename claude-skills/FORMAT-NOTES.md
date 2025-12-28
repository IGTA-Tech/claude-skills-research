# Skill Format Notes

## Comparison with Official Skills

After reviewing the official `algorithmic-art` skill from [anthropics/skills](https://github.com/anthropics/skills/tree/main/algorithmic-art), we've updated our skills to match the preferred format.

### Key Format Requirements

#### 1. YAML Frontmatter ✅
```yaml
---
name: skill-name-in-lowercase-with-hyphens
description: Clear description with trigger keywords. Use this when [activation conditions].
---
```

**Requirements**:
- Name must be lowercase with hyphens only
- Description should include "Use this when..." phrasing
- Include activation keywords users might say

#### 2. Direct Instructions ✅

Official skills speak **directly to Claude** with imperative commands:

**✅ Good** (Direct, imperative):
```markdown
## Instructions

### 1. Analyze the Screenshot

Examine the image carefully and identify:
- Layout structure
- Components
- Visual details
```

**❌ Avoid** (Meta, explanatory):
```markdown
## When to Use This Skill

Activate when the user:
- Provides a screenshot
- Asks to convert design
```

### 3. Clear Workflow ✅

Structure should be:
1. **Brief introduction** - What this skill does
2. **Instructions** - Step-by-step what to do
3. **Output Format** - Template/example of output
4. **Best Practices** - Guidelines and tips
5. **Example Workflow** - Concrete example

### 4. Action-Oriented Language ✅

Use commands, not descriptions:
- ✅ "Extract the key arguments"
- ✅ "Generate optimized code"
- ✅ "Provide structured analysis"
- ❌ "You should extract..."
- ❌ "This skill will help you..."

### 5. Template Outputs ✅

Show exact markdown/code formats to produce:

```markdown
## Output Format

```markdown
# Analysis Title

## Section 1
[Content format]

## Section 2
[Content format]
```
```

## What We Fixed

### All Skills Updated:

1. **screenshot-to-code** ✅
   - Added direct workflow instructions
   - Included code output templates
   - Removed "When to Use" meta-section

2. **reddit-thread-analyzer** ✅
   - Restructured with imperative commands
   - Added structured output template
   - Included scoring and sentiment format

3. **seo-content-optimizer** ✅
   - Complete rewrite with direct instructions
   - Added detailed output template
   - Included implementation checklist

4. **meeting-intelligence** ⚠️
   - Core format is good
   - Could benefit from more imperative style

5. **financial-parser** ⚠️
   - Solid structure
   - Output template could be more detailed

6. **code-review-pro** ⚠️
   - Good technical depth
   - Could streamline instructions

7. **regex-debugger** ⚠️
   - Clear instructions
   - Output format well-defined

8. **social-repurposer** ⚠️
   - Comprehensive coverage
   - Could be more action-oriented

9. **contract-analyzer** ⚠️
   - Strong legal disclaimers
   - Good output template

10. **podcast-content-suite** ⚠️
    - Extensive templates
    - Very detailed (good!)

### Validation Checklist

For each skill, verify:

- [ ] Name is lowercase-with-hyphens
- [ ] Description includes "Use this when..."
- [ ] Instructions are imperative (commands)
- [ ] Has clear output format/template
- [ ] Includes best practices
- [ ] Has concrete example workflow
- [ ] Speaks directly to Claude, not about Claude

## Testing Your Skills

After installation, test with these phrases:

1. **screenshot-to-code**: "Convert this screenshot to React code"
2. **reddit-thread-analyzer**: "What does Reddit think about X?"
3. **seo-content-optimizer**: "Optimize this post for SEO"
4. **meeting-intelligence**: "Extract action items from this meeting"
5. **financial-parser**: "Parse this invoice"
6. **code-review-pro**: "Review this code for security"
7. **regex-debugger**: "Debug this regex pattern"
8. **social-repurposer**: "Turn this into a Twitter thread"
9. **contract-analyzer**: "Review this contract"
10. **podcast-content-suite**: "Repurpose this podcast transcript"

## Further Improvements

To make skills even better:

1. **Add more examples** - Show multiple use cases
2. **Include edge cases** - How to handle unusual inputs
3. **Reference templates** - Add template files if needed
4. **Version history** - Track changes over time
5. **Dependencies** - Note any required tools or context

## Official Resources

- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills.md)
- [Official Skills Repository](https://github.com/anthropics/skills)
- [Skills Creation Guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
