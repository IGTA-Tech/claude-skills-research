# 📚 Claude Skills 开发指南 / Claude Skills Development Guide

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/sanshao85/claude-skills-guide?style=social)](https://github.com/sanshao85/claude-skills-guide/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sanshao85/claude-skills-guide?style=social)](https://github.com/sanshao85/claude-skills-guide/network/members)
[![GitHub issues](https://img.shields.io/github/issues/sanshao85/claude-skills-guide)](https://github.com/sanshao85/claude-skills-guide/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**🇨🇳 中文** | [🇺🇸 English](./README_EN.md)

</div>

> 📖 学习如何创建专业的 Claude Skills - 从基础到精通
> 📖 Learn how to create professional Claude Skills - from basics to mastery

---

## 🎯 什么是 Claude Skills？

**Claude Skills** 是一种标准化的能力包，将专家知识封装成文件，让 Claude 能够在特定任务上表现得更专业。

### 核心组成

每个 Skill 由三部分构成：

1. **SKILL.md** - 主要指令文件（必需）
2. **scripts/** - 可执行代码（可选）
3. **reference/** - 参考资源（可选）

### 工作原理

Skills 采用**渐进式披露**机制，分三层加载：

- **Level 1**: 元数据（name + description）- 始终加载，~100 tokens
- **Level 2**: 指令（SKILL.md 主体）- 触发时加载，~5k tokens  
- **Level 3**: 资源和代码 - 按需加载

这样设计可以最大化节省 token，只在需要时才加载详细内容。

---

## 📦 本项目包含什么？

### 📖 核心文档（3 个）

1. **README.md**（本文件）- 项目介绍和快速开始
2. **Claude_Skills_开发完全指南.md** - 详细的开发教程（2500+ 行）
3. **快速参考卡片.md** - 模板和检查清单

### 🎨 官方示例（17 个 Skills）

**anthropic-skills/** - Anthropic 官方 Skills 仓库，包含：

**创意设计类**：
- algorithmic-art - 算法艺术生成
- canvas-design - 画布设计
- slack-gif-creator - Slack GIF 创建

**开发技术类**：
- artifacts-builder - Claude.ai Artifacts 构建
- mcp-builder - MCP 服务器构建
- webapp-testing - Web 应用测试

**企业沟通类**：
- brand-guidelines - 品牌规范应用
- internal-comms - 内部沟通
- theme-factory - 主题工厂

**文档处理类**（document-skills/）：
- docx - Word 文档处理
- pdf - PDF 文档处理
- pptx - PowerPoint 处理
- xlsx - Excel 处理

**元 Skills**：
- skill-creator - Skill 创建指南
- template-skill - Skill 模板

**其他示例**：
- claude-cookbooks/skills/ - 包含 3 个财务相关示例

---

## 🚀 快速开始（5 分钟）

### 第 1 步：查看一个简单的 Skill

```bash
# 查看最简单的模板
cat anthropic-skills/template-skill/SKILL.md
```

一个最基本的 Skill 就是这样：

```markdown
---
name: my-skill
description: 描述这个 Skill 做什么以及何时使用
---

# My Skill

[在这里添加你的指令...]

## 示例
- 示例 1
- 示例 2
```

### 第 2 步：创建你的第一个 Skill

```bash
# 创建目录
mkdir my-first-skill
cd my-first-skill

# 创建 SKILL.md
cat > SKILL.md << 'EOF'
---
name: greeting-expert
description: 专业的问候语生成专家，根据时间和场合生成合适的问候语
---

# 问候语专家

你是一个问候语生成专家。根据用户提供的信息生成合适的问候语。

## 指令

1. 询问用户需要什么类型的问候语
2. 考虑时间、场合、对象等因素
3. 生成 3-5 个不同风格的问候语选项
4. 解释每个问候语适合的场景

## 示例

用户："我需要一个早上的商务问候语"
回复：
1. "早上好！祝您今天工作顺利！"（正式）
2. "早安！新的一天，新的开始！"（积极）
3. "您好！很高兴在这个美好的早晨见到您！"（热情）
EOF
```

### 第 3 步：使用你的 Skill

在 Claude.ai、Claude Code 或 API 中上传这个 Skill 文件夹，然后就可以使用了！

---

## 📖 学习路径

### 🎯 初学者（1-2 小时）

**目标**：理解 Skills 基础，创建简单 Skill

1. **阅读本 README**（15 分钟）
2. **查看 template-skill**（15 分钟）
   ```bash
   cat anthropic-skills/template-skill/SKILL.md
   ```
3. **查看 2-3 个简单示例**（30 分钟）
   - brand-guidelines
   - internal-comms
4. **创建你的第一个 Skill**（30 分钟）
   - 只包含 SKILL.md
   - 不需要脚本

### 🎓 进阶者（3-5 小时）

**目标**：掌握最佳实践，创建包含脚本的 Skill

1. **阅读 Claude_Skills_开发完全指南.md 核心章节**（2 小时）
   - 第 5 章：SKILL.md 编写
   - 第 6 章：Scripts 开发
   - 第 8 章：最佳实践
2. **研究复杂示例**（1 小时）
   - mcp-builder
   - webapp-testing
   - document-skills
3. **创建包含脚本的 Skill**（2 小时）

### 🚀 高级者（5+ 小时）

**目标**：精通 Skills 开发，创建生产级 Skill

1. **完整阅读 Claude_Skills_开发完全指南.md**（3 小时）
2. **研究所有官方示例**（2 小时）
3. **创建生产级 Skill**（多次迭代）

---

## 💡 核心要点

### ✅ 好的 Skill 应该：

- **简洁** - 只教 Claude 不知道的东西
- **精准** - description 要准确描述使用场景
- **结构化** - 使用清晰的步骤和示例
- **可测试** - 提供具体的使用示例
- **适度** - SKILL.md 保持在 500 行以内

### ❌ 避免这些错误：

- 过度解释 Claude 已知的基础知识
- 包含会过时的时效性信息
- SKILL.md 过长（超过 1000 行）
- 缺少具体的使用示例
- description 太模糊

---

## 📚 文档导航

| 需求 | 推荐文档 |
|------|---------|
| **快速了解** | 本 README |
| **深入学习** | Claude_Skills_开发完全指南.md |
| **快速查阅** | 快速参考卡片.md |
| **查看示例** | anthropic-skills/ |

---

## 🎨 官方示例索引

### 按复杂度

**简单**（只有 SKILL.md）：
- template-skill
- brand-guidelines
- internal-comms

**中等**（包含 reference/）：
- skill-creator
- mcp-builder

**复杂**（包含 scripts/）：
- webapp-testing
- slack-gif-creator
- document-skills

### 按用途

**学习参考**：
- template-skill - 最基本的模板
- skill-creator - 如何创建 Skill

**创意设计**：
- algorithmic-art
- canvas-design
- theme-factory

**开发工具**：
- artifacts-builder
- mcp-builder
- webapp-testing

**文档处理**：
- document-skills/docx
- document-skills/pdf
- document-skills/pptx
- document-skills/xlsx

---

## 📞 参考资源

### 官方文档

- [Skills 概览](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [最佳实践](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [快速开始](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/quickstart)

### 官方仓库

- [anthropics/skills](https://github.com/anthropics/skills) - 官方示例 Skills
- [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) - 官方教程

---

## ✅ 创建 Skill 检查清单

### 开始前

- [ ] 明确 Skill 的目标和使用场景
- [ ] 确定是否需要 scripts 和 reference
- [ ] 准备好 2-3 个使用示例

### 创建时

- [ ] 编写清晰的 name（小写，连字符）
- [ ] 编写精准的 description（包含使用场景）
- [ ] 提供具体的使用示例
- [ ] 保持 SKILL.md 简洁（< 500 行）
- [ ] 使用结构化的指令格式

### 完成后

- [ ] 在不同场景下测试
- [ ] 检查是否有不必要的内容
- [ ] 确保示例清晰易懂
- [ ] 添加必要的注释

---

## 🎉 开始创建你的第一个 Skill！

选择一个路径开始：

### 路径 1: 查看示例
```bash
# 查看最简单的模板
cat anthropic-skills/template-skill/SKILL.md

# 查看一个实际的 Skill
cat anthropic-skills/brand-guidelines/SKILL.md
```

### 路径 2: 深入学习
```bash
# 阅读完整指南
open Claude_Skills_开发完全指南.md
```

### 路径 3: 立即创建
```bash
# 创建你的 Skill
mkdir my-skill
cd my-skill
# 复制模板并修改...
```      

---

## 🤝 贡献 / Contributing

欢迎贡献！请查看 [贡献指南](./CONTRIBUTING.md) 了解详情。

We welcome contributions! Please see [Contributing Guide](./CONTRIBUTING.md) for details.

**贡献方式 / Ways to contribute:**
- 🐛 报告问题 / Report bugs
- 💡 提出建议 / Suggest features
- 📝 改进文档 / Improve documentation
- 🎨 分享你的 Skill / Share your skills
- 🌍 翻译文档 / Translate docs

---

## 📄 许可证 / License

本项目采用 [MIT License](./LICENSE) 开源。

This project is licensed under the [MIT License](./LICENSE).

---

## 🙏 致谢 / Acknowledgments

- 感谢 [Anthropic](https://www.anthropic.com/) 提供的官方文档和示例
- 感谢所有贡献者的支持和帮助
- 特别感谢 Claude Skills 社区

Thanks to:
- [Anthropic](https://www.anthropic.com/) for official documentation and examples
- All contributors for their support and help
- Claude Skills community

---

## ⭐ Star History

如果这个项目对你有帮助，请给它一个 Star！⭐

If this project helps you, please give it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=sanshao85/claude-skills-guide&type=Date)](https://star-history.com/#sanshao85/claude-skills-guide&Date)

---

**祝你 Skill 开发愉快！ / Happy Skill Development!** 🚀


