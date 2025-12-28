# Claude Skills - 100 Production-Ready AI Skills 🚀

The most comprehensive collection of Claude Code skills ever created! Build with automation, powered by OneWave AI.

## 🎯 What's Included

**100 Production-Ready Skills** across 15 categories:

- 🗣️ **Communication** (5) - Slack, SMS, email, LinkedIn optimization
- 💼 **Sales Intelligence** (5) - Deal analysis, call prep, objection handling
- 📈 **Marketing Automation** (5) - Content repurposing, SEO, email optimization
- 🎨 **Creative & Design** (4) - Brand consistency, presentations, assets
- 🧠 **Expert Simulation** (2) - Debates and expert panels
- 📝 **Content Repurposing** (5) - Multi-format content transformation
- ⚽ **Sports** (19) - **Most comprehensive sports AI toolkit ever!**
- 💰 **Finance & Personal** (5) - Portfolio, budget, financial goals
- 📊 **Sales Leadership** (8) - Forecasting, coaching, territory planning
- 🤖 **Meta-Skills** (6) - Revolutionary architectural innovations
- 🎧 **Customer Support** (1) - Knowledge base building
- ✈️ **Travel** (1) - Itinerary optimization
- 💪 **Fitness** (2) - Workout programs and training logs

## 🏆 Highlights

### Skill #100: skill-navigator ⭐
Your intelligent guide to all 99 other skills! Recommends the perfect skill for any task, creates combinations, and helps you discover capabilities you didn't know you had.

### Meta-Skills (Revolutionary!)
- **conversation-archaeologist** - Builds persistent user context
- **weak-signal-synthesizer** - Predicts emerging trends
- **hypothesis-testing-engine** - Automated scientific method
- **cross-conversation-project-manager** - Stateful memory
- **skill-composer-studio** - Programmable AI workflows
- **skill-navigator** - Your personal skill guide

### Sports Skills (19 Total!) ⚽🏀🏈
Complete toolkit for content, analysis, and training

## 🚀 Quick Start

### Installation Methods

#### Option 1: Install Individual Skills (Recommended)

1. **Extract a skill zip file**:
   ```bash
   unzip screenshot-to-code.zip
   ```

2. **Copy to your Claude skills directory**:

   **For Personal Skills** (available in all projects):
   ```bash
   cp -r screenshot-to-code ~/.claude/skills/
   ```

   **For Project Skills** (specific to one project):
   ```bash
   # From your project root
   cp -r screenshot-to-code .claude/skills/
   ```

3. **Restart Claude Code** or run:
   ```bash
   claude --debug
   ```

#### Option 2: Install All Skills at Once

**Personal Skills** (available everywhere):
```bash
# Extract all zips
for file in *.zip; do unzip "$file"; done

# Copy all to personal skills directory
mkdir -p ~/.claude/skills
cp -r screenshot-to-code reddit-analyzer seo-optimizer meeting-intelligence \
      financial-parser code-review-pro regex-debugger social-repurposer \
      contract-analyzer podcast-content-suite ~/.claude/skills/
```

**Project Skills** (specific project):
```bash
# From your project root
mkdir -p .claude/skills
cp -r /path/to/claude-skills/* .claude/skills/
```

## 📚 How Skills Work

### Automatic Activation

Skills are **model-invoked**, meaning Claude automatically decides when to use them based on:
- The skill's description
- Your request/question
- Available context

You don't need to explicitly call them—just ask naturally!

### Examples

**Screenshot to Code**:
```
You: "Convert this screenshot to React code"
Claude: [Automatically uses Screenshot to Code skill]
```

**SEO Optimizer**:
```
You: "Optimize this blog post for 'AI productivity tools'"
Claude: [Automatically uses SEO Content Optimizer skill]
```

**Meeting Intelligence**:
```
You: "Extract action items from this meeting transcript"
Claude: [Automatically uses Meeting Intelligence System skill]
```

## 🎯 Skill Descriptions

### 1. Screenshot to Code
**Use Cases**:
- Converting design mockups to code
- Recreating UI from screenshots
- Building landing pages from images
- Prototyping from designs

**Triggers**: screenshot, UI, convert to code, design to code

---

### 2. Reddit Thread Analyzer
**Use Cases**:
- Market research
- Sentiment analysis
- Community opinion gathering
- Competitive intelligence

**Triggers**: Reddit, thread analysis, what does Reddit think, community opinion

---

### 3. SEO Content Optimizer
**Use Cases**:
- Blog post optimization
- Keyword analysis
- Readability improvement
- Meta description generation
- Content gap analysis

**Triggers**: SEO, optimize content, keyword, meta description, search ranking

---

### 4. Meeting Intelligence System
**Use Cases**:
- Meeting summarization
- Action item extraction
- Decision tracking
- Follow-up email generation
- Blocker identification

**Triggers**: meeting notes, transcript, action items, meeting summary

---

### 5. Financial Document Parser
**Use Cases**:
- Expense tracking
- Invoice processing
- Receipt organization
- Financial reporting
- Tax preparation

**Triggers**: invoice, receipt, bank statement, expense, parse financial

---

### 6. Code Review Pro
**Use Cases**:
- Security vulnerability scanning
- Performance optimization
- Code quality assessment
- Best practice validation
- Refactoring suggestions

**Triggers**: code review, review code, security audit, performance analysis

---

### 7. Regex Visual Debugger
**Use Cases**:
- Regex debugging
- Pattern explanation
- Test case generation
- Regex optimization
- Cross-language conversion

**Triggers**: regex, regular expression, pattern matching, why doesn't my regex work

---

### 8. Social Media Content Repurposer
**Use Cases**:
- Cross-platform content adaptation
- Social media marketing
- Content distribution
- Platform-specific optimization

**Triggers**: repurpose content, Twitter thread, LinkedIn post, social media

---

### 9. Contract Analyzer
**Use Cases**:
- Contract review
- Risk assessment
- Term extraction
- Legal document analysis
- Negotiation preparation

**Triggers**: review contract, NDA, agreement, legal document, concerning clauses

---

### 10. Podcast to Content Suite
**Use Cases**:
- Podcast marketing
- Content repurposing
- Blog post creation
- Social media content
- Newsletter generation

**Triggers**: podcast transcript, repurpose podcast, show notes, podcast to blog

## 🔧 Troubleshooting

### Claude Isn't Using My Skill

1. **Check file location**:
   - Personal: `~/.claude/skills/skill-name/SKILL.md`
   - Project: `.claude/skills/skill-name/SKILL.md`

2. **Verify YAML syntax**:
   ```yaml
   ---
   name: Skill Name
   description: Clear description...
   ---
   ```
   - Must have opening and closing `---`
   - No tabs (use spaces)
   - Valid YAML format

3. **Check description specificity**:
   - Include activation keywords
   - Be explicit about use cases
   - Mention relevant terms users would say

4. **Debug mode**:
   ```bash
   claude --debug
   ```
   This shows skill loading errors.

### Skills Load But Don't Activate

**Make your request more explicit**:

❌ Bad: "Look at this"
✅ Good: "Optimize this blog post for SEO"

❌ Bad: "Help with this"
✅ Good: "Review this contract for concerning clauses"

## 📖 Documentation Format

Each skill uses this structure:

```
skill-name/
└── SKILL.md (required)
```

**SKILL.md format**:
```yaml
---
name: Your Skill Name
description: Brief description with activation triggers
---

# Your Skill Name

## When to Use This Skill
[Explicit activation conditions]

## Instructions
[Step-by-step guidance for Claude]

## Output Format
[Structured output template]

## Examples
[Concrete usage examples]

## Best Practices
[Guidelines for optimal results]
```

## 🎨 Customization

### Modify Skills

1. Extract the skill zip
2. Edit `SKILL.md`
3. Test with `claude --debug`
4. Re-install to skills directory

### Create Your Own Skills

Use these as templates! Key elements:

1. **Clear description** with activation triggers
2. **Detailed instructions** (step-by-step)
3. **Output format** (structured templates)
4. **Examples** (show, don't just tell)
5. **Best practices** (edge cases, optimizations)

## 🤝 Sharing Skills

### With Your Team

**Method 1**: Project Skills (Recommended)
```bash
# Commit to git
git add .claude/skills/
git commit -m "Add Claude skills"
git push
```
Team members automatically get skills after pulling.

**Method 2**: Share Zip Files
Send `.zip` files to teammates who can install individually.

### Creating a Plugin

For wider distribution, package as a Claude Code plugin. See [plugin documentation](https://docs.claude.com/en/docs/claude-code/plugins.md).

## 📈 Usage Tips

### Combining Skills

Skills can work together! Example:

1. Use **Code Review Pro** to analyze code
2. Use **Meeting Intelligence** to extract action items from the review discussion
3. Use **Social Media Repurposer** to share learnings as Twitter thread

### Best Practices

1. **Be specific** in your requests
2. **Include context** (file type, goals, constraints)
3. **Iterate** - skills can refine their output
4. **Provide feedback** - Claude learns from corrections

### Example Workflows

**Content Creator Workflow**:
```
Podcast → Podcast to Content Suite → Social Repurposer → SEO Optimizer
```

**Developer Workflow**:
```
Screenshot → Screenshot to Code → Code Review Pro
```

**Business Workflow**:
```
Meeting → Meeting Intelligence → Contract Analyzer → Financial Parser
```

## 📝 License

These skills are provided as-is for use with Claude Code. Modify and share freely.

## 🐛 Issues & Feedback

If a skill isn't working as expected:

1. Check the troubleshooting section above
2. Run `claude --debug` to see loading errors
3. Verify YAML syntax and file locations
4. Make your request more explicit

## 🌟 Contributing

Feel free to:
- Modify these skills for your needs
- Create variations for specific use cases
- Share improvements with your team
- Build new skills using these as templates

## 📚 Additional Resources

- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills.md)
- [Claude Code Plugins](https://docs.claude.com/en/docs/claude-code/plugins.md)
- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code/)

---

**Ready to supercharge Claude Code? Install a skill and start using it!** 🚀

No explicit commands needed—just ask naturally and Claude will know when to use each skill.
