# 命令详细说明 (Commands Reference)

[简体中文](#简体中文) | [English](#english)

---

## 简体中文

本文档详细介绍项目多级索引系统的所有命令及其使用方法。

> **💡 提示**: 所有命令都需要 `/project-multilevel-index:` 前缀（这是 Claude Code 插件的命名空间要求）

---

## 命令列表

| 命令 | 功能 | 使用场景 |
|------|------|---------|
| [`init-index`](#1-init-index---初始化索引系统) | 初始化索引系统 | 首次使用或重建索引 |
| [`update-index`](#2-update-index---更新索引) | 手动更新索引 | 大量修改后同步索引 |
| [`check-index`](#3-check-index---一致性检查) | 一致性检查 | 验证索引完整性 |
| [`set-language`](#4-set-language---切换语言) | 切换语言 | 切换中英文界面 |

---

## 1. init-index - 初始化索引系统

### 功能

首次使用或完全重建项目的索引系统。

### 命令

```bash
/project-multilevel-index:init-index
```

### 执行流程

1. **确认项目根目录**: Claude 会询问当前目录是否正确
2. **扫描项目结构**: 递归扫描所有代码文件
3. **分析依赖关系**: 解析 import/export 等依赖声明
4. **生成文件头注释**: 为每个代码文件添加 Input/Output/Pos 注释
5. **生成文件夹索引**: 在每个文件夹创建 FOLDER_INDEX.md
6. **生成项目索引**: 在根目录创建 PROJECT_INDEX.md
7. **生成依赖关系图**: 创建 Mermaid 格式的可视化依赖图
8. **输出统计报告**: 显示生成的文件数量和结构

### 示例对话

```
User: /project-multilevel-index:init-index

Claude: 确认当前目录是 h:/my-project 吗？

User: 是的

Claude:
正在扫描项目...
发现:
- TypeScript: 45 文件
- Python: 12 文件

正在生成索引...
✅ 完成！

已生成:
- 57 个文件头注释
- 8 个 FOLDER_INDEX.md
- 1 个 PROJECT_INDEX.md
- 依赖关系图包含 32 个节点

请查看 PROJECT_INDEX.md 了解项目架构。
```

### 输出文件

#### 文件头注释示例（TypeScript）

```typescript
/**
 * Input: express, bcrypt, ./models/User, ./middleware/auth
 * Output: router (Express Router), POST /login, POST /register
 * Pos: API层-认证路由，处理用户登录注册
 *
 * 本注释在文件修改时自动更新
 */

import express from 'express';
import bcrypt from 'bcrypt';
// ...
```

#### FOLDER_INDEX.md 示例

```markdown
# src/controllers Folder Index

## Architecture

API控制器层，处理HTTP请求和响应。
每个控制器对应一个业务领域，调用服务层完成业务逻辑。

## File Manifest

### userController.ts
- **Role**: 用户管理控制器
- **Function**: 处理用户相关的HTTP请求
- **Dependencies**: userService, express
- **Used By**: routes/userRoutes.ts

### authController.ts
- **Role**: 认证控制器
- **Function**: 处理登录、注册、登出等认证请求
- **Dependencies**: authService, express, bcrypt
- **Used By**: routes/authRoutes.ts

---
⚠️ **Self-Reference**: Update this index when folder contents change
```

#### PROJECT_INDEX.md 示例

详见 [EXAMPLES.md](EXAMPLES.md#project_indexmd-示例)

### 适用场景

- ✅ **首次使用**: 刚安装插件，想要为现有项目建立索引
- ✅ **项目重构**: 大规模重构后需要重建索引
- ✅ **索引损坏**: 索引文件被误删或损坏
- ✅ **新团队成员**: 快速了解项目结构

### 注意事项

- ⚠️ **会覆盖现有索引**: 已有的 FOLDER_INDEX.md 和 PROJECT_INDEX.md 会被覆盖
- ⚠️ **文件头注释会更新**: 现有的 Input/Output/Pos 注释会被重新生成
- ⚠️ **耗时取决于项目大小**: 大型项目可能需要几分钟

---

## 2. update-index - 更新索引

### 功能

手动更新索引系统，适用于大量修改后或自动更新失效时。

### 命令

```bash
/project-multilevel-index:update-index
```

### 执行流程

1. **检测文件变更**: 比对当前代码与索引中的记录
2. **重新分析**: 对变更的文件重新分析依赖关系
3. **更新文件头**: 更新受影响文件的头注释
4. **更新文件夹索引**: 更新相关的 FOLDER_INDEX.md
5. **更新项目索引**: 更新 PROJECT_INDEX.md 和依赖图
6. **输出变更报告**: 列出所有更新的文件

### 示例对话

```
User: /project-multilevel-index:update-index

Claude:
正在检测变更...

发现变更:
- src/services/authService.ts (新增依赖: bcrypt)
- src/controllers/authController.ts (新增导出: logout)

正在更新索引...

已更新:
- 2 个文件头注释
- 1 个 FOLDER_INDEX.md (src/services/)
- PROJECT_INDEX.md
- 依赖关系图

✅ 索引更新完成！
```

### 适用场景

- ✅ **批量修改后**: 一次性修改了多个文件
- ✅ **自动更新失效**: Hook 未触发或出现问题
- ✅ **手动同步**: 想要确保索引完全同步
- ✅ **定期维护**: 定期检查并更新索引

### 与 init-index 的区别

| 特性 | init-index | update-index |
|------|-----------|-------------|
| **范围** | 全部文件 | 仅变更文件 |
| **速度** | 较慢 | 较快 |
| **覆盖性** | 完全覆盖 | 增量更新 |
| **适用场景** | 首次使用 | 日常维护 |

---

## 3. check-index - 一致性检查

### 功能

检查索引系统的完整性和一致性，发现潜在问题。

### 命令

```bash
/project-multilevel-index:check-index
```

### 检查项目

1. **文件头完整性**: 所有代码文件是否都有正确的头注释
2. **文件夹索引完整性**: 每个文件夹是否都有 FOLDER_INDEX.md
3. **依赖关系准确性**: Input/Output 是否与实际代码一致
4. **循环依赖检测**: 是否存在循环依赖
5. **孤立文件检测**: 是否有未被索引的代码文件
6. **索引结构规范**: 索引文件格式是否符合规范

### 示例对话

```
User: /project-multilevel-index:check-index

Claude:
索引一致性检查报告
==================

✅ 文件头完整性: 55/57 (2 个文件缺少注释)
  - src/utils/legacy.js
  - src/temp/test.ts

✅ 文件夹索引: 8/8 正常

⚠️ 依赖关系: 发现 1 个循环依赖
  - src/a.ts → src/b.ts → src/c.ts → src/a.ts

✅ 索引结构: 符合规范

✅ 孤立文件: 无

建议:
1. 运行 /project-multilevel-index:update-index 补充缺失注释
2. 重构循环依赖: a.ts ↔ b.ts ↔ c.ts

总体评分: 8/10 (良好)
```

### 输出报告格式

#### ✅ 正常项

```
✅ 文件头完整性: 57/57 完整
```

#### ⚠️ 警告项

```
⚠️ 依赖关系: 发现 3 个循环依赖
  - moduleA → moduleB → moduleA
  - serviceX → serviceY → serviceZ → serviceX
  - controllerP → controllerQ → controllerP
```

#### ❌ 错误项

```
❌ 文件夹索引: 3/8 缺失
  - src/utils/ 缺少 FOLDER_INDEX.md
  - src/models/ 缺少 FOLDER_INDEX.md
  - src/middleware/ 缺少 FOLDER_INDEX.md
```

### 适用场景

- ✅ **定期检查**: 每周或每月检查一次索引健康状态
- ✅ **合并前检查**: PR 合并前确保索引完整
- ✅ **重构后验证**: 大规模重构后验证索引准确性
- ✅ **问题排查**: 发现索引异常时的诊断工具

### 建议修复流程

1. **查看检查报告**: 了解存在哪些问题
2. **优先修复错误项**: 缺失的索引文件、严重的结构问题
3. **处理警告项**: 循环依赖、不一致的依赖关系
4. **运行 update-index**: 自动修复可修复的问题
5. **手动调整**: 处理自动修复无法解决的问题
6. **再次检查**: 确认所有问题已解决

---

## 4. set-language - 切换语言

### 功能

切换插件的界面语言（中文/英文）。

### 命令

```bash
/project-multilevel-index:set-language
```

### 执行流程

1. **显示当前语言**: 显示当前使用的语言
2. **列出可选语言**: 简体中文、English
3. **用户选择**: 选择目标语言
4. **保存配置**: 创建或更新 `.claude/locale-config.json`
5. **确认切换**: 显示切换成功的消息

### 示例对话

```
User: /project-multilevel-index:set-language

Claude:
当前语言: 简体中文 (zh-CN)

可选语言:
1. 简体中文 (zh-CN)
2. English (en-US)

请选择语言（输入数字）:

User: 2

Claude:
✅ 语言已切换为: English (en-US)

配置已保存到: .claude/locale-config.json

下次执行命令时将使用英文界面。
```

### 支持的语言

- 🇨🇳 **简体中文 (zh-CN)**: 默认语言
- 🇺🇸 **English (en-US)**: 英文界面

### 配置文件

切换语言后会在项目根目录创建 `.claude/locale-config.json`:

```json
{
  "language": "en-US",
  "fallback": "zh-CN"
}
```

### 手动配置

也可以手动创建配置文件：

```bash
mkdir -p .claude
echo '{"language": "en-US", "fallback": "zh-CN"}' > .claude/locale-config.json
```

### 适用场景

- ✅ **国际团队**: 团队成员使用不同语言
- ✅ **学习用途**: 学习英文技术文档
- ✅ **演示展示**: 根据观众语言切换界面

### 影响范围

切换语言会影响：
- ✅ 命令执行时的提示信息
- ✅ 生成的索引文件中的说明文字
- ✅ 错误和警告消息
- ✅ 统计报告的格式

不会影响：
- ❌ 已生成的索引文件（需要重新生成）
- ❌ 代码文件本身
- ❌ 项目源代码

---

## CLI 工具命令

如果您使用独立的 CLI 工具 `codex`，请参考以下命令：

### 初始化索引

```bash
codex init
```

### 自定义选项

```bash
codex init --max-depth 5 --max-nodes 30
```

### 可用选项

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `--max-depth` | 最大目录深度 | 5 |
| `--max-nodes` | 依赖图最大节点数 | 50 |
| `--exclude` | 排除的目录模式 | node_modules,dist,build |
| `--language` | 输出语言 | zh-CN |

📖 **完整 CLI 文档**: [cli/README.md](cli/README.md)

---

## 常见问题

### Q1: 为什么命令需要前缀 `/project-multilevel-index:`?

**A**: 这是 Claude Code 插件系统的命名空间要求，防止不同插件的命令冲突。

### Q2: 可以同时运行多个命令吗?

**A**: 不建议。命令之间可能有依赖关系，建议按顺序执行。

### Q3: 命令执行失败怎么办?

**A**:
1. 检查命令是否拼写正确
2. 确认插件已正确安装
3. 查看错误消息，根据提示修复
4. 必要时运行 `/project-multilevel-index:check-index` 诊断问题

### Q4: init-index 和 update-index 应该用哪个?

**A**:
- **首次使用**: 用 `init-index`
- **日常更新**: 用 `update-index`（更快）
- **索引损坏**: 用 `init-index` 重建

---

## 相关文档

- [EXAMPLES.md](EXAMPLES.md) - 命令使用示例
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - 故障排查指南
- [PLATFORM_SUPPORT.md](PLATFORM_SUPPORT.md) - 平台支持说明
- [cli/README.md](cli/README.md) - CLI 工具文档

---

## English

This document provides detailed information about all commands in the Project Multi-level Index System.

> **💡 Tip**: All commands require the namespace prefix `/project-multilevel-index:` (Claude Code plugin requirement)

---

## Command List

| Command | Function | Use Case |
|---------|----------|----------|
| [`init-index`](#1-init-index---initialize-index-system) | Initialize index system | First-time setup or rebuild |
| [`update-index`](#2-update-index---update-index) | Manual index update | Sync after bulk changes |
| [`check-index`](#3-check-index---consistency-check) | Consistency check | Verify index integrity |
| [`set-language`](#4-set-language---switch-language) | Switch language | Change UI language |

---

## 1. init-index - Initialize Index System

### Function

First-time setup or complete rebuild of the project index system.

### Command

```bash
/project-multilevel-index:init-index
```

### Execution Flow

1. **Confirm project root**: Claude asks if current directory is correct
2. **Scan project structure**: Recursively scan all code files
3. **Analyze dependencies**: Parse import/export statements
4. **Generate file headers**: Add Input/Output/Pos comments to each code file
5. **Generate folder indexes**: Create FOLDER_INDEX.md in each folder
6. **Generate project index**: Create PROJECT_INDEX.md at root
7. **Generate dependency graph**: Create Mermaid visualization
8. **Output statistics**: Display summary of generated files

### Example Dialog

```
User: /project-multilevel-index:init-index

Claude: Confirm current directory is h:/my-project?

User: Yes

Claude:
Scanning project...
Found:
- TypeScript: 45 files
- Python: 12 files

Generating indexes...
✅ Complete!

Generated:
- 57 file headers
- 8 FOLDER_INDEX.md files
- 1 PROJECT_INDEX.md
- Dependency graph with 32 nodes

See PROJECT_INDEX.md for project architecture.
```

### Use Cases

- ✅ **First-time setup**: Just installed plugin, want to index existing project
- ✅ **Project refactoring**: Rebuild index after major refactoring
- ✅ **Index corruption**: Index files were deleted or corrupted
- ✅ **New team member**: Quickly understand project structure

---

## 2. update-index - Update Index

### Function

Manually update index system after bulk changes or when auto-update fails.

### Command

```bash
/project-multilevel-index:update-index
```

### Execution Flow

1. **Detect changes**: Compare current code with index records
2. **Re-analyze**: Re-analyze dependencies of changed files
3. **Update file headers**: Update affected file header comments
4. **Update folder indexes**: Update relevant FOLDER_INDEX.md files
5. **Update project index**: Update PROJECT_INDEX.md and dependency graph
6. **Output change report**: List all updated files

### Use Cases

- ✅ **After bulk changes**: Modified multiple files at once
- ✅ **Auto-update failed**: Hook didn't trigger or had issues
- ✅ **Manual sync**: Want to ensure index is fully synchronized
- ✅ **Regular maintenance**: Periodically check and update index

---

## 3. check-index - Consistency Check

### Function

Check index system integrity and consistency, discover potential issues.

### Command

```bash
/project-multilevel-index:check-index
```

### Check Items

1. **File header completeness**: All code files have correct header comments
2. **Folder index completeness**: Every folder has FOLDER_INDEX.md
3. **Dependency accuracy**: Input/Output matches actual code
4. **Circular dependency detection**: Check for circular dependencies
5. **Orphaned file detection**: Check for unindexed code files
6. **Index structure compliance**: Index files follow proper format

### Example Dialog

```
User: /project-multilevel-index:check-index

Claude:
Index Consistency Check Report
==============================

✅ File header completeness: 55/57 (2 files missing comments)
  - src/utils/legacy.js
  - src/temp/test.ts

✅ Folder indexes: 8/8 OK

⚠️ Dependencies: Found 1 circular dependency
  - src/a.ts → src/b.ts → src/c.ts → src/a.ts

✅ Index structure: Compliant

✅ Orphaned files: None

Recommendations:
1. Run /project-multilevel-index:update-index to add missing comments
2. Refactor circular dependency: a.ts ↔ b.ts ↔ c.ts

Overall score: 8/10 (Good)
```

---

## 4. set-language - Switch Language

### Function

Switch plugin UI language (Chinese/English).

### Command

```bash
/project-multilevel-index:set-language
```

### Supported Languages

- 🇨🇳 **Simplified Chinese (zh-CN)**: Default
- 🇺🇸 **English (en-US)**: English interface

### Configuration File

After switching language, creates `.claude/locale-config.json`:

```json
{
  "language": "en-US",
  "fallback": "zh-CN"
}
```

---

## CLI Tool Commands

If you're using the standalone CLI tool `codex`:

### Initialize Index

```bash
codex init
```

### Custom Options

```bash
codex init --max-depth 5 --max-nodes 30
```

### Available Options

| Option | Description | Default |
|--------|-------------|---------|
| `--max-depth` | Maximum directory depth | 5 |
| `--max-nodes` | Max nodes in dependency graph | 50 |
| `--exclude` | Exclude directory patterns | node_modules,dist,build |
| `--language` | Output language | zh-CN |

📖 **Full CLI Documentation**: [cli/README.md](cli/README.md)

---

## Related Documentation

- [EXAMPLES.md](EXAMPLES.md) - Command usage examples
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Troubleshooting guide
- [PLATFORM_SUPPORT.md](PLATFORM_SUPPORT.md) - Platform support details
- [cli/README.md](cli/README.md) - CLI tool documentation
