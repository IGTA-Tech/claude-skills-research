# Claude Skills - Complete Installation Guide

## 📦 What You're Getting

**Total Skills**: 47 production-ready Claude Code skills
- 🌊 **OneWave AI Custom Skills**: 32 skills  
- 🏢 **Official Anthropic Skills**: 15 skills
- **Total Package Size**: ~130 KB (incredibly lightweight!)

---

## 🚀 Quick Installation - Choose Your Method

### Method 1: Claude Code Desktop (RECOMMENDED)

**Step-by-Step:**

1. **Locate Skills** - All ZIP files are in: `/Users/gabe/claude-skills/`

2. **Open Claude Code** → Go to **Settings** (⚙️ icon)

3. **Navigate to Skills Tab** or **Capabilities Tab**

4. **Click "Install Skill"** or **"Add from ZIP"**

5. **Select Skills** - Browse to `/Users/gabe/claude-skills/` and select `.zip` files

6. **Install** - Skills will extract and appear in your skills list

7. **Activate** - Toggle skills ON in the Capabilities tab

8. **Use** - Type `/skill-name` or just describe your task naturally!

---

### Method 2: Claude.ai Web Interface

1. Download ZIP files to your computer from `/Users/gabe/claude-skills/`

2. Go to **https://claude.ai**

3. Click **Profile** (top right) → **Settings**

4. Look for **"Skills"**, **"Custom Tools"**, or **"Capabilities"** section

5. Click **"Upload"** or **"Add Skill"**

6. Select the `.zip` file(s) you want

7. Skills will be available in new conversations

---

### Method 3: Manual Installation (Advanced)

```bash
# Create Claude skills directory
mkdir -p ~/.claude/skills

# Copy all skills
cp /Users/gabe/claude-skills/*.zip ~/.claude/skills/

# Extract all
cd ~/.claude/skills && for f in *.zip; do unzip -o "$f"; done

# Restart Claude Code - skills will auto-load!
```

---

## 📚 All 47 Skills Quick Reference

### 🌊 OneWave AI (32 Skills)

**Sales & CRM** (11) 🔥 **NEW!**
- sales-methodology-implementer - MEDDIC, BANT, Sandler frameworks
- pipeline-health-analyzer - Fix stalled deals
- personalization-at-scale - 500+ unique emails
- champion-identifier - Find internal advocates
- lookalike-customer-finder - Similar companies
- social-selling-content-generator - LinkedIn posts
- intent-signal-aggregator - Track buyer signals
- inbound-lead-qualifier - Score leads
- contact-hunter - Find contacts
- cold-email-sequence-generator - Email campaigns
- linkedin-sales-navigator-alt - Prospect lists

**Development** (6)
- screenshot-to-code - UI to code
- code-review-pro - Security analysis
- regex-debugger - Debug patterns
- api-documentation-writer - API docs
- database-schema-designer - DB schemas
- technical-writer - Technical docs

**Content & Marketing** (7)
- seo-optimizer - SEO optimization
- social-repurposer - Cross-platform content
- podcast-content-suite - Podcast repurposing
- reddit-analyzer - Sentiment analysis
- landing-page-copywriter - Landing pages
- email-template-generator - Email templates
- webinar-content-repurposer - Webinar content

**Business** (5)
- meeting-intelligence - Action items
- financial-parser - Invoice parsing
- contract-analyzer - Contract review
- job-application-optimizer - Resume optimization
- customer-review-aggregator - Review analysis

**Data & Analytics** (3)
- csv-excel-merger - Merge spreadsheets
- executive-dashboard-generator - Executive reports
- color-palette-extractor - Extract colors

---

### 🏢 Official Anthropic (15 Skills)

- algorithmic-art, canvas-design, slack-gif-creator
- artifacts-builder, mcp-builder, webapp-testing
- brand-guidelines, internal-comms, theme-factory
- docx, pdf, pptx, xlsx
- skill-creator, template-skill

---

## 💡 Quick Start Examples

### Using Slash Commands
```
/seo-optimizer              → Optimize content
/code-review-pro            → Review code
/pipeline-health-analyzer   → Analyze deals
/personalization-at-scale   → Generate emails
```

### Using Natural Language
```
"Review this code for security issues"
"Find 100 companies like my top customers"
"Create a LinkedIn post to attract CTOs"
"Score this inbound lead and route it"
```

---

## 🎯 Install by Role

**Sales Teams** (11 skills):
All files with "sales", "pipeline", "personalization", "champion", "lookalike", "social-selling", "intent", "inbound", "contact", "cold-email", "linkedin" in name

**Developers** (6 skills):
screenshot-to-code, code-review-pro, regex-debugger, api-documentation-writer, database-schema-designer, technical-writer

**Marketers** (9 skills):
seo-optimizer, social-repurposer, podcast-content-suite, reddit-analyzer, landing-page-copywriter, email-template-generator, webinar-content-repurposer, customer-review-aggregator, social-selling-content-generator

---

## 🔧 Troubleshooting

**Skills not showing?**
1. Restart Claude Code
2. Check ~/.claude/skills/ directory
3. Re-extract ZIPs
4. Enable in Capabilities tab

**Skill not working?**
1. Use slash command: `/skill-name`
2. Check SKILL.md for examples
3. Restart conversation
4. Re-install skill

---

## 🌟 What's New

### 8 Advanced Sales Skills Added!
Total sales intelligence: 11 skills covering entire sales process from prospecting to close!

---

**Ready to supercharge Claude? Install now!** 🚀

*Location: `/Users/gabe/claude-skills/`*
*Showcase: `claude-skills-showcase.html`*
*Total: 47 Skills | 130 KB*
