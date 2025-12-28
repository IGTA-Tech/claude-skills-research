# Quick Build Guide - Claude Skills Builder

## Overview
Automated tool to build 40+ sales, marketing, communication, and sports skills systematically.

## Installation

```bash
cd ~/claude-skills
chmod +x build_skills.py
python3 build_skills.py --help
```

## Quick Start

### Step 1: Generate Phase 1 Config (Communication Skills)

```bash
python3 build_skills.py --generate-phase1-config
```

This creates `batch-phase1.json` with 5 communication skills:
- slack-message-formatter
- sms-text-optimizer
- internal-email-composer
- company-announcement-writer
- linkedin-post-optimizer

### Step 2: Build Phase 1

```bash
python3 build_skills.py --batch batch-phase1.json
```

### Step 3: Validate & List

```bash
# List all skills
python3 build_skills.py --list

# Validate specific skill
python3 build_skills.py --validate slack-message-formatter
```

---

## All Phases

### Phase 1: Communication Skills (5 skills) ✅
```bash
python3 build_skills.py --generate-phase1-config
python3 build_skills.py --batch batch-phase1.json
```

### Phase 2: Sales Intelligence (5 skills)
```bash
python3 build_skills.py --generate-phase2-config
python3 build_skills.py --batch batch-phase2.json
```

Skills:
- competitor-price-tracker
- deal-momentum-analyzer
- champion-identifier
- objection-pattern-detector
- sales-call-prep-assistant

### Phase 3: Marketing Automation (5 skills)
```bash
python3 build_skills.py --generate-phase3-config
python3 build_skills.py --batch batch-phase3.json
```

Skills:
- webinar-to-content-multiplier
- competitor-content-analyzer
- seo-keyword-cluster-builder
- email-subject-line-optimizer
- utm-parameter-generator

### Phase 4: Creative & Design (4 skills)
```bash
python3 build_skills.py --generate-phase4-config
python3 build_skills.py --batch batch-phase4.json
```

Skills:
- brand-consistency-checker
- presentation-design-enhancer
- stock-photo-finder
- font-pairing-suggester

### Phase 5: Expert Simulation (2 skills)
```bash
python3 build_skills.py --generate-phase5-config
python3 build_skills.py --batch batch-phase5.json
```

Skills:
- debate-simulator
- expert-panel

### Phase 6: Content Repurposing (5 skills)
```bash
python3 build_skills.py --generate-phase6-config
python3 build_skills.py --batch batch-phase6.json
```

Skills:
- content-repurposer (master skill)
- game-builder
- podcast-studio
- flashcard-generator
- quiz-maker

### Phase 7: Sports Skills (10 skills) 🏈⚽🏀
```bash
python3 build_skills.py --generate-phase7-config
python3 build_skills.py --batch batch-phase7.json
```

Skills:
- game-recap-generator
- fantasy-lineup-optimizer
- player-comparison-tool
- highlight-reel-scripter
- scouting-report-builder
- sports-betting-analyzer
- practice-plan-creator
- play-by-play-generator
- injury-report-tracker
- trash-talk-generator

### Phase 8: Finance & Personal (5 skills)
```bash
python3 build_skills.py --generate-phase8-config
python3 build_skills.py --batch batch-phase8.json
```

Skills:
- portfolio-analyzer
- budget-optimizer
- financial-goal-planner
- tax-strategy-optimizer
- raise-negotiation-prep

### Phase 9: Sales Leadership (8 skills)
```bash
python3 build_skills.py --generate-phase9-config
python3 build_skills.py --batch batch-phase9.json
```

Skills:
- pipeline-health-diagnostics
- sales-forecast-builder
- rep-performance-scorecard
- quota-setting-calculator
- territory-planning-optimizer
- sales-comp-plan-designer
- deal-review-framework
- sales-coaching-plan-generator

---

## Manual Skill Creation

Create individual skill:

```bash
python3 build_skills.py \
  --name my-custom-skill \
  --description "One-line description of what skill does"
```

---

## Workflow

### 1. Generate Config
```bash
python3 build_skills.py --generate-phase1-config
```

### 2. Review Config
```bash
cat batch-phase1.json
```

### 3. Build Skills
```bash
python3 build_skills.py --batch batch-phase1.json
```

### 4. Validate
```bash
python3 build_skills.py --validate slack-message-formatter
```

### 5. Package
ZIP files are automatically created in the build process.

---

## Directory Structure

```
claude-skills/
├── build_skills.py                    # Automation script
├── SKILL-BUILDING-PLAN-2025.md       # Master plan
├── QUICK-BUILD-GUIDE.md              # This file
├── batch-phase1.json                  # Phase configs
├── batch-phase2.json
│
├── slack-message-formatter/           # Individual skill dirs
│   └── SKILL.md
├── slack-message-formatter.zip        # Packaged skills
│
├── sms-text-optimizer/
│   └── SKILL.md
├── sms-text-optimizer.zip
│
└── [... all other skills]
```

---

## Validation Checklist

For each skill, verify:
- [ ] SKILL.md has proper frontmatter (name, description)
- [ ] Instructions section is clear
- [ ] Output format is specified
- [ ] Best practices included
- [ ] Common use cases listed
- [ ] Example requests provided
- [ ] ZIP file created successfully
- [ ] File size is reasonable (2-8 KB)

---

## Testing Skills

### Test in Claude

1. Copy skill ZIP to Claude skills folder:
   ```bash
   cp ~/claude-skills/slack-message-formatter.zip ~/.claude/skills/
   ```

2. Extract:
   ```bash
   cd ~/.claude/skills/
   unzip slack-message-formatter.zip
   ```

3. Test trigger:
   ```
   "Format this message for Slack: [long message]"
   ```

---

## Batch Commands

### Build all communication skills:
```bash
python3 build_skills.py --batch batch-phase1.json
```

### Build all sports skills:
```bash
python3 build_skills.py --batch batch-phase7.json
```

### Validate all skills:
```bash
for skill in slack-message-formatter sms-text-optimizer internal-email-composer; do
  python3 build_skills.py --validate $skill
done
```

---

## Tips

1. **Start with Phase 1** - Communication skills are high-impact
2. **Test as you go** - Validate each phase before moving on
3. **Customize** - Edit SKILL.md files to refine instructions
4. **Iterate** - Based on usage, improve skill prompts
5. **Document** - Keep notes on what works well

---

## Complete Build Order

**Week 1**: Phase 1 - Communication (5 skills)
**Week 2**: Phase 2 - Sales Intelligence (5 skills)
**Week 3**: Phase 3 - Marketing Automation (5 skills)
**Week 4**: Phase 4 - Creative & Design (4 skills)
**Week 5**: Phase 5 - Expert Simulation (2 skills)
**Week 6**: Phase 6 - Content Repurposing (5 skills)
**Week 7**: Phase 7 - Sports (10 skills)
**Week 8**: Phase 8 - Finance & Personal (5 skills)
**Week 9**: Phase 9 - Sales Leadership (8 skills)

**Total**: 49 new skills + 25 existing = 74 total skills

---

## Troubleshooting

### Skill doesn't trigger
- Check description matches use case
- Make trigger phrases more specific
- Review existing skills for conflicts

### Output format wrong
- Update SKILL.md output format section
- Add more examples
- Clarify instructions

### Validation fails
- Check frontmatter format
- Ensure all required sections present
- Run: `python3 build_skills.py --validate skill-name`

---

## Next Steps

1. ✅ Run Phase 1
2. Test skills in Claude
3. Refine based on results
4. Continue with Phase 2-9
5. Update showcase HTML
6. Publish to GitHub

Happy building! 🚀
