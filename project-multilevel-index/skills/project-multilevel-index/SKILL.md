---
name: 项目多级索引系统
description: 当用户请求"初始化索引"、"更新文档"、"生成依赖图"或检测到文件结构性变更时，使用此技能维护分形自指文档系统
version: 2.1.0
---

# 项目多级索引系统 (Project Multi-level Index)

## 🏗️ 架构说明

本技能现在采用 **双模式架构**:

### 1. Claude Code 插件模式 (当前)
- **位置**: `skills/project-multilevel-index/`
- **用途**: Claude Code CLI 专属,通过插件系统使用
- **特性**: Hooks 自动触发、插件市场分发

### 2. Universal 通用模式 (多平台)
- **位置**: `universal/`
- **用途**: 支持 Claude Code、Cursor、Kiro、Windsurf 等多平台
- **特性**: 平台无关的核心逻辑、适配器架构

**关系**: 插件模式内部调用 universal/core/ 的通用逻辑,两者共享核心引擎。

---

## 📚 快速导航

### Claude Code 插件 (当前模式)
- **核心概念**: [core/concepts.md](core/concepts.md)
- **国际化**: [core/i18n.md](core/i18n.md)
- **命令实现**:
  - [/init-index](commands_impl/init-index.md) - 初始化索引系统
  - [/update-index](commands_impl/update-index.md) - 更新索引
  - [/check-index](commands_impl/check-index.md) - 一致性检查
  - [/set-language](commands_impl/set-language.md) - 切换语言

### Universal 通用核心
- **平台接口**: [../../universal/core/platform-interface.md](../../universal/core/platform-interface.md)
- **分析器**: [../../universal/core/analyzer/](../../universal/core/analyzer/)
  - [dependency-parser.md](../../universal/core/analyzer/dependency-parser.md) - 依赖分析
  - [export-parser.md](../../universal/core/analyzer/export-parser.md) - 导出分析
  - [position-inferrer.md](../../universal/core/analyzer/position-inferrer.md) - 位置推断
- **生成器**: [../../universal/core/generator/](../../universal/core/generator/)
  - [init-workflow.md](../../universal/core/generator/init-workflow.md) - 初始化工作流
  - [update-workflow.md](../../universal/core/generator/update-workflow.md) - 更新工作流
  - [check-workflow.md](../../universal/core/generator/check-workflow.md) - 检查工作流
- **适配器**: [../../universal/adapters/](../../universal/adapters/)
  - [claude-code/adapter.md](../../universal/adapters/claude-code/adapter.md) - Claude Code 适配器

---

## 🚀 执行流程

### 通用流程（所有命令）

1. **加载语言配置**（必须）
   - 详见 [core/i18n.md](core/i18n.md)
   - 读取 `.claude/locale-config.json`
   - 加载对应语言文件到 `LANG` 对象

2. **初始化 Claude Code 适配器**
   - 加载 `universal/adapters/claude-code/adapter.md`
   - 适配器提供平台特定的文件操作方法

3. **调用 Universal 核心工作流**
   - 传入适配器实例和语言配置
   - 执行平台无关的核心逻辑

4. **输出结果**
   - 使用 `LANG` 对象中的翻译文本
   - 替换占位符（如 `{directory}`, `{count}`）

---

## 命令概览

### `/init-index` - 初始化索引系统

**使用场景**: 首次运行或重建整个索引系统

**执行步骤**:
1. 加载语言配置
2. 初始化 Claude Code 适配器
3. **调用** `universal/core/generator/init-workflow.md`
4. 适配器使用 Read/Write/Edit 工具执行文件操作
5. 输出总结报告

**详细实现**: [commands_impl/init-index.md](commands_impl/init-index.md)

**核心工作流**: [../../universal/core/generator/init-workflow.md](../../universal/core/generator/init-workflow.md)

---

### `/update-index` - 更新索引

**使用场景**: 文件修改后手动更新或 Hook 自动调用

**执行步骤**:
1. 加载语言配置
2. 初始化 Claude Code 适配器
3. **调用** `universal/core/generator/update-workflow.md`
4. 传入变更文件列表
5. 适配器执行增量更新
6. 报告更新结果

**详细实现**: [commands_impl/update-index.md](commands_impl/update-index.md)

**核心工作流**: [../../universal/core/generator/update-workflow.md](../../universal/core/generator/update-workflow.md)

---

### `/check-index` - 一致性检查

**使用场景**: 验证索引系统完整性

**执行步骤**:
1. 加载语言配置
2. 初始化 Claude Code 适配器
3. **调用** `universal/core/generator/check-workflow.md`
4. 适配器执行完整性检查
5. 生成检查报告

**详细实现**: [commands_impl/check-index.md](commands_impl/check-index.md)

**核心工作流**: [../../universal/core/generator/check-workflow.md](../../universal/core/generator/check-workflow.md)

---

### `/set-language` - 切换语言

**使用场景**: 快速切换界面语言

**执行步骤**:
1. 询问用户选择语言（zh-CN / en-US）
2. 创建或更新 `.claude/locale-config.json`
3. 验证语言文件存在
4. 确认切换成功

**详细实现**: [commands_impl/set-language.md](commands_impl/set-language.md)

---

## 🔧 PostToolUse Hook 自动更新

当检测到文件修改（Write/Edit）时：

1. **加载语言配置**
2. **应用过滤规则**（详见 `locales/{language}/hooks.json`）
   - 跳过索引文件自身
   - 跳过非代码文件
   - 跳过大文件（>500KB）
   - 跳过排除目录

3. **判断是否为结构性变更**
   - 检查是否包含依赖关键字（import, require, use...）
   - 检查是否包含导出关键字（export, public, class...）

4. **执行更新**
   - 结构性变更 → 调用 `/update-index`
   - 仅文件头变更 → 只更新文件头
   - 其他 → 跳过

5. **静默处理**
   - 小改动：不提示
   - 重大变更：输出一行信息

---

## 🌍 多语言支持

### 支持的语言

- **zh-CN**: 简体中文（默认）
- **en-US**: 美国英语

### 切换方式

1. **配置文件方式**（推荐）
   ```bash
   # 创建配置文件
   mkdir -p .claude
   cat > .claude/locale-config.json << 'EOF'
   {
     "language": "en-US",
     "fallback": "zh-CN"
   }
   EOF
   ```

2. **命令方式**
   ```
   /set-language
   ```

3. **环境变量方式**
   ```bash
   export CLAUDE_LOCALE=en-US
   ```

4. **初始化时询问**
   - `/init-index` 会询问用户选择语言

### 技术术语

以下术语在所有语言中保持英文：
- Input, Output, Pos
- PROJECT_INDEX, FOLDER_INDEX
- SKILL.md

---

## 📖 扩展阅读

- **核心概念详解**: [core/concepts.md](core/concepts.md)
- **国际化实现**: [core/i18n.md](core/i18n.md)
- **语言文件**: `locales/zh-CN/` 和 `locales/en-US/`
- **文件模板**: `templates/`

---

## 🎯 设计原则

1. **避免过度更新**: 只在真正的结构性变化时更新索引
2. **保护用户内容**: 更新时保留用户手动添加的注释
3. **清晰的反馈**: 重要操作有明确提示
4. **性能优先**: 大型项目使用增量更新
5. **易于理解**: 文档清晰，示例丰富
6. **防止循环**: 索引文件修改时不触发更新
7. **国际化**: 支持多语言界面
8. **用户至上**: 不确定的操作先询问用户

---

## 🔗 相关文档

- **Universal 核心文档**: [../../universal/](../../universal/)
- **适配器开发指南**: [../../universal/adapters/README.md](../../universal/adapters/README.md)
- **平台对比**: [../../universal/.kiro/specs/platforms.yml](../../universal/.kiro/specs/platforms.yml)

---

**版本**: 2.1.0
**更新日期**: 2025-12-23
**新特性**: 双模式架构 + Universal 多平台核心 + 适配器系统
