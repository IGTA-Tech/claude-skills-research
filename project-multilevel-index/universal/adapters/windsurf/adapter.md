# Windsurf 平台适配器

## 平台信息

**平台名称**: Windsurf

**官方网站**: https://codeium.com/windsurf

**自动化级别**: `manual` (手动触发)

**触发机制**: `static_inline` (静态内联指令)

**配置位置**: `.windsurf/`, `WINDSURF_GUIDE.md`

**文件引用语法**: 无 (需静态内联)

---

## 平台能力

### 优势特性

✅ **AI 辅助编程** - Codeium AI 支持

✅ **VSCode 兼容** - 基于 VSCode,兼容扩展

✅ **流式对话** - 流畅的 AI 对话体验

✅ **代码补全** - 强大的代码补全能力

✅ **简单易用** - 用户友好的界面

### 限制

❌ **无 Hook 系统** - 不能自动监听文件变化

❌ **无规则系统** - 没有类似 Cursor Rules 的功能

❌ **无文件引用** - 不支持 `@file` 或 `#[[file:...]]` 语法

❌ **无 Spec 系统** - 没有结构化配置能力

❌ **完全手动** - 所有操作都需要用户明确指令

---

## 适配策略

### 方案: 静态内联 + 详细指导

```
.windsurf/
├── index-system-guide.md    ← 完整的内联指导文档
└── quick-commands.md         ← 快速命令参考
WINDSURF_GUIDE.md             ← 项目根目录指导
```

**核心思路**:
- **静态内联**: 将 Universal 核心逻辑复制到指导文档中
- **详细步骤**: 提供逐步操作指南
- **明确命令**: 用户可以直接复制粘贴命令

**工作流程**:
1. 用户修改代码文件
2. 用户手动执行命令: "请更新索引"
3. AI 读取 `.windsurf/index-system-guide.md`
4. AI 按照内联的详细步骤执行
5. 完成更新

---

## 接口实现

此适配器实现 [platform-interface.md](../../core/platform-interface.md) 定义的核心接口方法。

---

### 1. 文件操作接口

#### readFile(path)

**实现方式**: 通过明确的指令请求 AI

**Prompt 模板**:
```markdown
请读取文件: {path}

完整显示文件内容。
```

**代码示例**:
```typescript
async function readFile(path: string): Promise<string> {
  // Windsurf 环境下,需要明确告诉 AI 读取文件
  const prompt = `请读取文件: ${path}\n\n完整显示文件内容。`;
  return await askAI(prompt);
}
```

---

#### writeFile(path, content)

**实现方式**: 明确的创建文件指令

**Prompt 模板**:
```markdown
请创建文件: {path}

内容如下:
\`\`\`
{content}
\`\`\`

请将以上内容写入文件。
```

**代码示例**:
```typescript
async function writeFile(path: string, content: string): Promise<void> {
  const prompt = `请创建文件: ${path}\n\n` +
    `内容如下:\n\`\`\`\n${content}\n\`\`\`\n\n` +
    `请将以上内容写入文件。`;
  await askAI(prompt);
}
```

---

#### editFile(path, oldString, newString)

**实现方式**: 明确的替换指令

**Prompt 模板**:
```markdown
请编辑文件: {path}

找到以下内容:
\`\`\`
{oldString}
\`\`\`

替换为:
\`\`\`
{newString}
\`\`\`

请执行替换操作。
```

**代码示例**:
```typescript
async function editFile(
  path: string,
  oldString: string,
  newString: string
): Promise<void> {
  const prompt = `请编辑文件: ${path}\n\n` +
    `找到以下内容:\n\`\`\`\n${oldString}\n\`\`\`\n\n` +
    `替换为:\n\`\`\`\n${newString}\n\`\`\`\n\n` +
    `请执行替换操作。`;
  await askAI(prompt);
}
```

---

### 2. 文件系统接口

#### scanFiles(rootPath, patterns)

**实现方式**: 详细的扫描指令

**Prompt 模板**:
```markdown
请扫描目录: {rootPath}

包含以下文件类型:
- {includePatterns}

排除以下目录和文件:
- {excludePatterns}

返回所有匹配的文件路径列表(每行一个路径)。
```

**代码示例**:
```typescript
async function scanFiles(
  rootPath: string,
  patterns: {
    include: string[];
    exclude: string[];
  }
): Promise<string[]> {
  const prompt = `请扫描目录: ${rootPath}\n\n` +
    `包含以下文件类型:\n- ${patterns.include.join('\n- ')}\n\n` +
    `排除以下目录和文件:\n- ${patterns.exclude.join('\n- ')}\n\n` +
    `返回所有匹配的文件路径列表(每行一个路径)。`;

  const result = await askAI(prompt);
  return result.split('\n').filter(line => line.trim());
}
```

---

#### getProjectRoot()

**实现方式**: 使用 VSCode API

**代码示例**:
```typescript
function getProjectRoot(): string {
  // Windsurf 基于 VSCode
  return vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd();
}
```

---

### 3. 用户交互接口

#### askConfirmation(message)

**实现方式**: 通过对话请求确认

**Prompt 模板**:
```markdown
{message}

请回答 Yes 或 No。
```

**代码示例**:
```typescript
async function askConfirmation(message: string): Promise<boolean> {
  const prompt = `${message}\n\n请回答 Yes 或 No。`;
  const response = await askAI(prompt);
  return response.toLowerCase().includes('yes');
}
```

---

#### showMessage(message, type)

**实现方式**: 格式化输出

**代码示例**:
```typescript
function showMessage(message: string, type: 'info' | 'success' | 'warning' | 'error'): void {
  const icons = {
    info: 'ℹ️',
    success: '✅',
    warning: '⚠️',
    error: '❌'
  };

  const formattedMessage = `${icons[type]} ${message}`;
  console.log(formattedMessage);
}
```

---

### 4. 国际化接口

#### getLanguage()

**实现方式**: 读取配置文件或使用默认值

**优先级**:
1. `.windsurf/locale-config.json`
2. `.claude/locale-config.json`
3. VSCode 语言设置
4. 默认 `zh-CN`

**代码示例**:
```typescript
async function getLanguage(): Promise<string> {
  // 尝试读取配置
  try {
    const config = await readFile('.windsurf/locale-config.json');
    const parsed = JSON.parse(config);
    return parsed.language || 'zh-CN';
  } catch {}

  // 使用默认值
  return 'zh-CN';
}
```

---

#### loadLanguageFiles(lang)

**实现方式**: 静态内联方式 (无法动态引用)

**说明**: 由于 Windsurf 不支持文件引用,需要将语言文件内容直接内联到指导文档中。

**代码示例**:
```typescript
// Windsurf 不支持动态加载
// 需要在生成配置时,将语言文件内容内联到指导文档中
function getInlinedLanguageData(lang: string): LanguageData {
  // 返回预先内联的语言数据
  return lang === 'zh-CN' ? zhCNData : enUSData;
}
```

---

### 5. 平台特定接口

#### generatePlatformConfig(targetPath, language)

**功能**: 生成 Windsurf 指导文档

**实现方式**: 创建详细的内联指导文档

**代码示例**:
```typescript
async function generatePlatformConfig(
  targetPath: string,
  language: string
): Promise<void> {
  const windsurfDir = path.join(targetPath, '.windsurf');
  await createDirectory(windsurfDir);

  // 生成完整的内联指导文档
  const guideContent = generateCompleteGuide(language);
  await writeFile(
    path.join(windsurfDir, 'index-system-guide.md'),
    guideContent
  );

  // 生成快速命令参考
  const quickCommands = generateQuickCommands(language);
  await writeFile(
    path.join(windsurfDir, 'quick-commands.md'),
    quickCommands
  );

  // 生成根目录指导
  const rootGuide = generateRootGuide(language);
  await writeFile(
    path.join(targetPath, 'WINDSURF_GUIDE.md'),
    rootGuide
  );
}

function generateCompleteGuide(language: string): string {
  // 将所有核心逻辑内联到一个文档中
  return `
# 项目索引系统完整指导 (Windsurf)

## 核心概念
${inlineConcepts(language)}

## 初始化流程
${inlineInitWorkflow(language)}

## 更新流程
${inlineUpdateWorkflow(language)}

## 检查流程
${inlineCheckWorkflow(language)}

## 依赖分析算法
${inlineDependencyParser(language)}

## 导出分析算法
${inlineExportParser(language)}

## 位置推断算法
${inlinePositionInferrer(language)}

## 模板
${inlineTemplates(language)}

## 消息文本
${inlineMessages(language)}
`;
}
```

---

#### enableAutoTrigger()

**功能**: 不支持 (Windsurf 无法自动触发)

**实现方式**: 生成手动提醒文档

**代码示例**:
```typescript
async function enableAutoTrigger(): Promise<void> {
  const reminderDoc = `
# ⚠️ 重要提醒

Windsurf 不支持自动触发。

请在修改代码后,手动执行:
\`\`\`
请按照 .windsurf/index-system-guide.md 更新索引
\`\`\`

建议:
- 修改 3+ 文件后,统一更新一次
- 使用快捷命令: "更新索引"
`;

  await writeFile('.windsurf/auto-trigger-reminder.md', reminderDoc);

  showMessage(
    'Windsurf 不支持自动触发,请手动执行更新命令。',
    'warning'
  );
}
```

---

## 配置文件模板

### .windsurf/index-system-guide.md

完整的内联指导文档,包含所有核心逻辑。

**内容结构**:
```markdown
# 项目索引系统完整指导 (Windsurf)

## 📚 系统概述
...

## 🔄 初始化索引

### 步骤 1: 扫描项目文件
\`\`\`
指令: 扫描 src/ 目录下的所有代码文件
包含: .js .ts .py .java ...
排除: node_modules .git dist build ...
\`\`\`

### 步骤 2: 分析每个文件
对于每个文件,执行以下分析:

#### 依赖分析 (Input)
查找 import/require 语句:
- JavaScript/TypeScript: import {...} from '...'
- Python: import ... / from ... import ...
- Java: import ...

提取依赖项列表。

#### 导出分析 (Output)
查找 export/public 语句:
- JavaScript/TypeScript: export class/function/const ...
- Python: def ... / class ... (顶层)
- Java: public class/interface ...

提取导出项列表。

#### 位置推断 (Pos)
根据文件路径判断层级:
- controller → Controller Layer
- service → Service Layer
- model → Model Layer
- utils → Utility Layer

### 步骤 3: 生成文件头注释
为每个文件添加头注释:

JavaScript/TypeScript:
\`\`\`typescript
/**
 * Input: [依赖项列表]
 * Output: [导出项列表]
 * Pos: [层级和定位]
 *
 * 🔄 Self-reference: When this file changes, update:
 * - This file header
 * - [所在目录]/FOLDER_INDEX.md
 * - PROJECT_INDEX.md
 */
\`\`\`

Python:
\`\`\`python
# Input: [依赖项列表]
# Output: [导出项列表]
# Pos: [层级和定位]
#
# 🔄 Self-reference: When this file changes, update:
# - This file header
# - [所在目录]/FOLDER_INDEX.md
# - PROJECT_INDEX.md
\`\`\`

### 步骤 4: 生成 FOLDER_INDEX.md
...

### 步骤 5: 生成 PROJECT_INDEX.md
...

## 🔄 更新索引
...

## ✅ 检查索引
...

## 📖 完整示例
...
```

**特点**:
- **完全自包含**: 所有逻辑都在一个文档中
- **详细步骤**: 每一步都有明确指令
- **可复制粘贴**: 用户可以直接复制命令

---

### .windsurf/quick-commands.md

快速命令参考,方便用户快速使用。

**内容**:
```markdown
# 索引系统快速命令 (Windsurf)

## 🚀 初始化

**命令**:
\`\`\`
请按照 .windsurf/index-system-guide.md 中的"初始化索引"章节,为本项目初始化索引系统。
\`\`\`

**简短版**:
\`\`\`
初始化索引系统
\`\`\`

---

## 🔄 更新索引

**命令**:
\`\`\`
我修改了 [文件路径],请按照 .windsurf/index-system-guide.md 中的"更新索引"章节,更新相关索引。
\`\`\`

**简短版**:
\`\`\`
更新索引
\`\`\`

---

## ✅ 检查索引

**命令**:
\`\`\`
请按照 .windsurf/index-system-guide.md 中的"检查索引"章节,检查索引系统的一致性。
\`\`\`

**简短版**:
\`\`\`
检查索引
\`\`\`

---

## 🌍 切换语言

**中文**:
\`\`\`json
// .windsurf/locale-config.json
{
  "language": "zh-CN"
}
\`\`\`

**英文**:
\`\`\`json
// .windsurf/locale-config.json
{
  "language": "en-US"
}
\`\`\`

---

## 💡 提示

- **批量更新**: 修改多个文件后,一次性更新索引
- **定期检查**: 每周运行一次检查命令
- **简短命令**: 熟悉后,可以使用简短版命令
```

---

### WINDSURF_GUIDE.md (项目根目录)

项目根目录的简要指导,引导用户使用详细文档。

**内容**:
```markdown
# 索引系统使用指导 (Windsurf 用户)

本项目使用**分形多级索引系统**自动维护项目文档。

## 🚀 快速开始

### 1. 初始化索引 (仅首次)

执行命令:
\`\`\`
初始化索引系统
\`\`\`

或查看详细步骤: [.windsurf/index-system-guide.md](.windsurf/index-system-guide.md)

### 2. 日常使用

修改代码后,执行:
\`\`\`
更新索引
\`\`\`

### 3. 定期检查

每周执行:
\`\`\`
检查索引
\`\`\`

---

## 📖 详细文档

- **完整指导**: `.windsurf/index-system-guide.md`
- **快速命令**: `.windsurf/quick-commands.md`

---

## 💡 提示

Windsurf 不支持自动更新,请在以下情况手动执行更新:

- ✅ 添加/删除 import 语句
- ✅ 添加/删除 export 语句
- ✅ 创建/删除文件
- ❌ 仅修改函数实现 (不需要更新)

---

## 🌍 语言设置

创建 `.windsurf/locale-config.json`:
\`\`\`json
{
  "language": "zh-CN"  // 或 "en-US"
}
\`\`\`

---

**版本**: 1.0.0
**平台**: Windsurf
```

---

## 使用指南

### 安装步骤

#### 1. 生成 Windsurf 配置

在 Windsurf 中执行:
\`\`\`
用户: "请为本项目生成索引系统配置 (Windsurf 版本)"
\`\`\`

AI 将:
1. 创建 `.windsurf/` 目录
2. 生成 `index-system-guide.md` (完整内联文档)
3. 生成 `quick-commands.md` (快速命令)
4. 生成 `WINDSURF_GUIDE.md` (根目录指导)

#### 2. 验证配置

\`\`\`bash
# 检查生成的文件
ls -la .windsurf/

# 应该看到:
# .windsurf/index-system-guide.md
# .windsurf/quick-commands.md
# WINDSURF_GUIDE.md
\`\`\`

---

### 初始化索引

**方法 1: 使用快速命令**
\`\`\`
用户: "初始化索引系统"
\`\`\`

**方法 2: 明确引用指导文档**
\`\`\`
用户: "请按照 .windsurf/index-system-guide.md 初始化索引"
\`\`\`

**方法 3: 详细指令**
\`\`\`
用户: "请读取 .windsurf/index-system-guide.md,按照'初始化索引'章节的步骤,为本项目生成索引系统"
\`\`\`

---

### 日常使用

#### 更新索引

**场景**: 修改了 `src/services/user.service.ts`,添加了新的 import

**命令**:
\`\`\`
用户: "我修改了 src/services/user.service.ts,请更新索引"
\`\`\`

或简短版:
\`\`\`
用户: "更新索引"
\`\`\`

**执行流程**:
\`\`\`
AI 读取 .windsurf/index-system-guide.md
  ↓
找到 "更新索引" 章节
  ↓
按照内联的详细步骤执行
  ↓
完成更新
\`\`\`

---

#### 检查索引

**命令**:
\`\`\`
用户: "检查索引"
\`\`\`

或详细版:
\`\`\`
用户: "请按照 .windsurf/index-system-guide.md 检查索引系统的一致性"
\`\`\`

---

### 批量更新

**场景**: 修改了 10 个文件

**命令**:
\`\`\`
用户: "我修改了以下文件:
- src/services/user.service.ts
- src/services/auth.service.ts
- ...

请统一更新索引"
\`\`\`

---

## 平台限制与变通

### 限制 1: 完全手动触发

**影响**: 每次修改都需要用户执行命令

**变通方案**:
1. **批量更新**: 积累多次修改后,一次性更新
2. **快捷命令**: 使用简短的命令,减少输入
3. **定期检查**: 每周运行一次检查,补漏

---

### 限制 2: 无文件引用能力

**影响**: 无法引用 Universal 核心文件,必须静态内联

**变通方案**:
1. **完全内联**: 将所有逻辑复制到指导文档中
2. **自包含文档**: 单个文档包含所有信息
3. **定期同步**: 当 Universal 核心更新时,重新生成配置

---

### 限制 3: 文档可能过大

**影响**: 完全内联导致指导文档非常长

**变通方案**:
1. **章节化**: 使用清晰的章节结构
2. **快速命令**: 提供简短的快捷命令
3. **目录导航**: 添加详细的目录和锚点链接

---

## 最佳实践

### 1. 养成批量更新习惯

**不推荐**:
\`\`\`
修改 file1.ts → 更新索引
修改 file2.ts → 更新索引
修改 file3.ts → 更新索引
\`\`\`

**推荐**:
\`\`\`
修改 file1.ts
修改 file2.ts
修改 file3.ts
→ 统一更新索引 (一次)
\`\`\`

---

### 2. 使用简短命令

熟悉后,直接使用:
\`\`\`
"初始化索引"
"更新索引"
"检查索引"
\`\`\`

AI 会自动读取 `.windsurf/index-system-guide.md`

---

### 3. 定期检查

建立检查习惯:
\`\`\`
每周五: "检查索引"
每次 PR 前: "检查索引"
\`\`\`

---

## 测试清单

### 功能测试
- [ ] 生成配置文件成功
- [ ] 初始化索引成功
- [ ] 手动更新索引成功
- [ ] 检查功能正常
- [ ] 批量更新正常
- [ ] 国际化切换正常

### 文档测试
- [ ] 指导文档完整自包含
- [ ] 步骤清晰易懂
- [ ] 命令可以直接复制使用
- [ ] 示例充分

---

## 常见问题

### Q: 每次都要手动更新,太麻烦怎么办?

**A**:
1. **批量更新**: 不要每次修改都更新,积累多次后一次性更新
2. **快捷命令**: 使用简短命令 "更新索引"
3. **结对编程**: 在结对编程结束时统一更新一次

---

### Q: 指导文档太长,AI 可能读不完怎么办?

**A**:
1. **使用快捷命令**: AI 会智能地只读取需要的章节
2. **明确引用章节**: "按照初始化章节执行"
3. **分步执行**: 如果 AI 理解有困难,分成多个小步骤

---

### Q: Windsurf 与其他平台比较?

**A**:

| 特性 | Claude Code | Cursor | Kiro | Windsurf |
|------|------------|--------|------|----------|
| 自动化 | ✅ Full | ⚡ Semi | ⚡ Semi | ❌ Manual |
| 文件引用 | ✅ | ⚡ | ✅ | ❌ |
| 配置方式 | Hooks | Rules | Spec | Static |
| 易用性 | 最高 | 高 | 中 | 中 |

**Windsurf 优势**:
- 简单易用的界面
- 强大的代码补全
- 流畅的对话体验

**Windsurf 劣势**:
- 需要手动触发所有操作
- 无法自动维护

---

## 示例项目

参考: `examples/windsurf-example/`

包含:
- 完整的 `.windsurf/` 配置
- 内联的指导文档
- 使用演示视频
- 常见问题解答

---

## 版本历史

### v1.0.0 (2025-12-23)
- ✅ Windsurf 适配器实现
- ✅ 静态内联架构
- ✅ 完整指导文档
- ✅ 快捷命令系统
- ✅ 国际化支持

### 未来计划
- 🔧 优化文档结构,减少长度
- 🔧 更多示例和模板
- 🔧 探索 Windsurf API (如果开放)

---

**下一步**: 参考 [使用指南](#使用指南) 开始使用
