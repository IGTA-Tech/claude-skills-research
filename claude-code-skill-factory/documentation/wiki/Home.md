# 🏭 Claude Code Skills & Agents Factory

**Build production-ready Claude Skills and Agents in minutes, not days.**

This factory provides battle-tested templates, prompt systems, and examples to generate custom Claude capabilities at scale. Whether you need financial analysis, AWS architecture design, content research, or specialized development agents - we've got you covered.

---

## 🚀 What You Get

| **Production Skills** | **Example Agents** | **Generation System** |
|---|---|---|
| 7 complete, production-ready skills | 42 specialized agents | 2 powerful prompt templates |
| AWS, M365, Content Research, Prompts | Frontend, Backend, Security, QA | Skills Factory + Agents Factory |
| Ready to use immediately | Full YAML frontmatter examples | Generate custom capabilities |

**Time to First Skill**: 5 minutes
**Code Quality**: Enterprise-grade with type hints, error handling, and documentation
**Platforms Supported**: Claude Apps, Claude Code, Claude API

---

## ⚡ Quick Start

### Generate Your First Skill (5 minutes)

**1. Fill the Template** (2 min)
```markdown
Open: documentation/templates/SKILLS_FACTORY_PROMPT.md

Fill in:
BUSINESS_TYPE: Your industry (e.g., "SaaS startup")
USE_CASES: What you need (e.g., "Analyze user feedback, Generate reports")
NUMBER_OF_SKILLS: How many (e.g., 3)
```

**2. Generate** (1 min)
- Copy entire prompt → Paste into Claude
- Claude generates complete skill packages
- Includes SKILL.md, Python files, samples, HOW_TO_USE.md

**3. Install** (2 min)
```bash
# Claude Code
cp skill-folder ~/.claude/skills/

# Claude Apps
Import ZIP file through Skills menu
```

**Done!** Your skill is ready to use.

---

## 📦 What's Inside

### 🎯 7 Production-Ready Skills

**Generate these types of capabilities instantly:**

| Skill | Size | What It Does | Use Case |
|---|---|---|---|
| **[Prompt Factory](generated-skills/prompt-factory/)** | 427 KB | Generate mega-prompts for any role | 69 presets across 15 domains (Technical, Business, Legal, Finance, Executive) |
| **[AWS Solution Architect](generated-skills/aws-solution-architect/)** | 53 KB | Design serverless infrastructure | Startup architecture, cost optimization, IaC templates |
| **[Content Trend Researcher](generated-skills/content-trend-researcher/)** | 35 KB | Multi-platform trend analysis | Google, Reddit, YouTube, Medium, LinkedIn, X - SEO-optimized outlines |
| **[M365 Tenant Manager](generated-skills/ms365-tenant-manager/)** | 40 KB | Microsoft 365 administration | Tenant setup, security policies, PowerShell automation |
| **[Psychology Advisor](generated-skills/psychology-advisor/)** | 31 KB | Evidence-based mental wellness | CBT techniques, mindfulness, stress management, RAIN method |
| **[Agent Factory](generated-skills/agent-factory/)** | 12 KB | Generate Claude Code agents | Enhanced YAML, tool patterns, MCP integration |
| **Financial Models** | 8 KB | DCF valuation & analysis | Ratio calculation, Monte Carlo simulation, sensitivity analysis |

**Total**: 606 KB of production code you don't have to write.

---

### 🤖 42 Example Agents

**Pre-built specialists for your development workflow:**

#### Engineering (12 agents)
- `rr-frontend-engineer` - React/Vue/Angular expert
- `rr-backend-engineer` - API and database design
- `rr-fullstack-engineer` - End-to-end development
- `rr-mobile-engineer` - React Native/Flutter/Native
- `rr-devops` - CI/CD and infrastructure
- `rr-architect` - System design and architecture
- `rr-security-engineer` - Security audits and fixes
- `rr-performance` - Performance optimization
- `rr-test-auto` - Test generation (Playwright)
- `rr-test-runner` - Test execution and reporting
- `rr-qa-lead` - Quality assurance
- `rr-ml-engineer` - Machine learning pipelines

#### Product & Design (8 agents)
- `rr-prd-specialist` - Product requirements
- `rr-product-owner` - Backlog management
- `rr-ui-design` - Interface design
- `rr-ux-research` - User research
- `rr-design-systems` - Component libraries
- `rr-accessibility` - WCAG compliance
- `rr-content-strategy` - Content planning
- `rr-tech-writer` - Documentation

#### Business & Growth (6 agents)
- `rr-market-research` - Market analysis
- `rr-customer-success` - User onboarding
- `rr-biz-strategy` - Business strategy
- `rr-growth` - Growth experiments
- `rr-marketing-analyst` - Marketing data
- `rr-product-analyst` - Product analytics

#### Infrastructure & Data (7 agents)
- `rr-cloud-arch` - AWS/Azure/GCP
- `rr-db-arch` - Database design
- `rr-data-science` - Data analysis
- `rr-analytics` - Analytics implementation
- `rr-api-design` - API architecture
- `rr-incident` - Incident response
- `rr-release` - Release management

#### Management (9 agents)
- `rr-project-manager` - Sprint coordination
- `rr-requirements` - Requirements gathering
- `rr-support` - Customer support
- `rr-ai-research` - AI/ML research
- Plus 5 more workflow agents

**[Browse Full Agent Catalog →](Agents-Catalog)**

---

### 🎨 Generation Templates

**Two powerful prompt systems:**

#### 1. Skills Factory Template
**Purpose**: Generate multi-file Claude Skills
**Output**: Folders with SKILL.md + Python + samples + ZIP
**Best For**: Capabilities that calculate, analyze, or generate
**Examples**: Financial models, data analysis, report generation
**[View Template →](documentation/templates/SKILLS_FACTORY_PROMPT.md)**

#### 2. Agents Factory Template
**Purpose**: Generate specialized Claude Code agents
**Output**: Single .md files with enhanced YAML frontmatter
**Best For**: Development workflows, code reviews, specialized tasks
**Examples**: Code reviewers, testers, deployment agents
**[View Template →](documentation/templates/AGENTS_FACTORY_PROMPT.md)**

---

## 🎯 Choose Your Path

### 👨‍💻 For Developers
**"I need specialized coding assistants"**

→ Use [Agents Factory](documentation/templates/AGENTS_FACTORY_PROMPT.md)
→ Browse [42 Example Agents](Agents-Catalog)
→ Install to `.claude/agents/`
→ **Result**: Auto-invoked specialists for frontend, backend, testing, security

**Time Investment**: 10 minutes
**Benefit**: Consistent code quality, automated reviews, specialized expertise

---

### 🏢 For Enterprises
**"We need standardized capabilities across teams"**

→ Use [Skills Factory](documentation/templates/SKILLS_FACTORY_PROMPT.md)
→ Generate domain-specific skills (compliance, reporting, analysis)
→ Deploy via Skills API
→ **Result**: Consistent analysis, reports, and workflows enterprise-wide

**Time Investment**: 30 minutes per skill
**Benefit**: Standardization, compliance, quality control

---

### ✍️ For Content Creators
**"I need content research and writing assistance"**

→ Install [Content Trend Researcher](generated-skills/content-trend-researcher/)
→ Install [Prompt Factory](generated-skills/prompt-factory/)
→ **Result**: Data-driven outlines, SEO optimization, trend analysis

**Time Investment**: 5 minutes
**Benefit**: 10+ platform analysis, intent mapping, content gap discovery

---

### 🚀 For Startups
**"We need MVP infrastructure and rapid development"**

→ Install [AWS Solution Architect](generated-skills/aws-solution-architect/)
→ Install [Agent Factory](generated-skills/agent-factory/)
→ Generate custom agents for your stack
→ **Result**: Serverless architecture + specialized dev team

**Time Investment**: 15 minutes
**Benefit**: Cost-effective infrastructure, faster development cycles

---

## 🌟 Key Features

### ✅ Production-Ready Output
- Proper YAML frontmatter (kebab-case validation)
- Type-annotated Python with full error handling
- Safe operations (division by zero, missing data)
- Industry-standard documentation

### 🔗 Composable Architecture
- Skills work together seamlessly
- `data-extractor` → `data-analyzer` → `report-generator`
- No duplicate functionality
- Clear input/output contracts

### 📦 Complete Packaging
- SKILL.md with structured documentation
- Multi-file Python implementations
- sample_input.json and expected_output.json
- HOW_TO_USE.md with invocation examples
- ZIP files for Claude Apps import

### ⚡ Smart Detection
- Automatically determines when Python is needed
- Multi-file structure for complex functionality
- Minimal, focused sample data
- Platform-appropriate patterns

### 🎯 Enhanced Agent YAML
- Color coding for visual organization
- Field classification (frontend, backend, ops)
- Expertise levels (beginner, intermediate, expert)
- MCP tool integration (GitHub, Playwright)
- Tool access control (Read/Write/Bash)

---

## 📚 Documentation

### Getting Started
- **[Quick Start Guide](Getting-Started)** - Generate first skill in 5 minutes
- **[Installation Guide](Installation)** - Setup for all platforms
- **[Skills vs Agents](Skills-vs-Agents)** - When to use which

### Catalogs
- **[Skills Catalog](Skills-Catalog)** - 7 production skills with examples
- **[Agents Catalog](Agents-Catalog)** - 42 agents organized by function
- **[Example Skills](claude-skills-examples/)** - 3 reference implementations

### Templates
- **[Skills Factory Prompt](documentation/templates/SKILLS_FACTORY_PROMPT.md)** - Generate Claude Skills
- **[Agents Factory Prompt](documentation/templates/AGENTS_FACTORY_PROMPT.md)** - Generate Agents
- **[YAML Standards](YAML-Standards)** - Frontmatter requirements

### Advanced
- **[Customization Guide](Customization-Guide)** - Adapt skills to your needs
- **[Architecture Patterns](Architecture-Patterns)** - Design best practices
- **[GitHub Automation](GitHub-Automation)** - Workflow system
- **[API Reference](API-Reference)** - Skills API integration

---

## 🤝 Community & Support

### Get Help
- 💬 **[GitHub Discussions](https://github.com/rezashabrang/claude-code-skills-factory/discussions)** - Ask questions, share skills
- 🐛 **[Report Issues](https://github.com/rezashabrang/claude-code-skills-factory/issues)** - Bug reports and feature requests
- 📖 **[Wiki](https://github.com/rezashabrang/claude-code-skills-factory/wiki)** - Complete documentation

### Contribute
- 🌟 **Star this repo** - Help others discover it
- 🍴 **Fork and extend** - Create your own skills
- 📤 **Share your skills** - Submit PRs for new examples
- 📝 **Improve docs** - Better documentation helps everyone

### Resources
- **[Anthropic Skills Docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)** - Official documentation
- **[Skills Marketplace](https://github.com/anthropics/skills)** - Community skills
- **[Claude Code Docs](https://docs.claude.com/claude-code)** - CLI and agents

---

## 🎯 Real-World Impact

### What Users Are Building

**Financial Services**: Custom DCF models with industry-specific assumptions
**Content Agencies**: Multi-platform trend analysis → SEO-optimized content
**DevOps Teams**: Infrastructure-as-code generation for AWS, Azure, GCP
**HR Departments**: Employee onboarding workflows and policy automation
**Legal Teams**: Contract analysis and compliance checking
**Marketing Teams**: Campaign performance analysis and reporting

### By The Numbers

- **606 KB** of production code included
- **69 prompt presets** across 15 domains
- **42 example agents** ready to customize
- **7 production skills** ready to deploy
- **2 generation templates** for infinite expansion
- **5 minutes** to first working skill
- **100% compatible** with all Claude platforms

---

## 🚦 Getting Started Now

### Option A: Use Existing Skills (2 minutes)
```bash
# 1. Choose a skill from generated-skills/
# 2. Copy to ~/.claude/skills/
# 3. Restart Claude Code
# Done!
```

### Option B: Generate Custom Skills (5 minutes)
```bash
# 1. Open documentation/templates/SKILLS_FACTORY_PROMPT.md
# 2. Fill in your requirements
# 3. Paste entire prompt into Claude
# 4. Install generated skill
# Done!
```

### Option C: Install Example Agents (1 minute)
```bash
# Copy agents you need
cp claude-agents-examples/agents/rr-frontend-engineer.md ~/.claude/agents/
cp claude-agents-examples/agents/rr-backend-engineer.md ~/.claude/agents/
# Done!
```

---

## 📌 Quick Links

| Action | Link |
|---|---|
| 🚀 Generate Your First Skill | [Skills Factory Template](documentation/templates/SKILLS_FACTORY_PROMPT.md) |
| 🤖 Browse Example Agents | [Agents Catalog](Agents-Catalog) |
| 📦 Download Production Skills | [Skills Catalog](Skills-Catalog) |
| 📖 Read Full Documentation | [Getting Started Guide](Getting-Started) |
| 💬 Ask Questions | [GitHub Discussions](https://github.com/rezashabrang/claude-code-skills-factory/discussions) |
| 🐛 Report Issues | [GitHub Issues](https://github.com/rezashabrang/claude-code-skills-factory/issues) |
| ⭐ Star This Project | [Give a Star](https://github.com/rezashabrang/claude-code-skills-factory) |

---

## 📄 License & Version

**License**: MIT - Skills you generate are yours to use
**Version**: 1.2.0
**Last Updated**: October 24, 2025
**Status**: Production Ready

**Latest Changes** (v1.2.0):
- ✅ Added Prompt Suite skill (427 KB, 69 presets, 15 domains)
- ✅ Enhanced agent YAML frontmatter (color, field, expertise, MCP)
- ✅ GitHub automation workflows (PR reviews, issue triage, plan conversion)
- ✅ Comprehensive documentation wiki

---

## 🎉 Ready to Build?

**Stop writing the same capabilities over and over.**
**Generate production-ready skills and agents in minutes.**

<div align="center">

### [🚀 Start with Skills Factory →](documentation/templates/SKILLS_FACTORY_PROMPT.md)

### [🤖 Browse Agent Examples →](Agents-Catalog)

### [📖 Read Getting Started →](Getting-Started)

</div>

---

**Built with Claude Code | Powered by Anthropic | Maintained by the Community**
