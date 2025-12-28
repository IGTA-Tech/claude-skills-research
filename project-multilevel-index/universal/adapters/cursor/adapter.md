# Cursor 平台适配器

## 平台信息

**平台名称**: Cursor

**官方网站**: https://cursor.sh

**自动化级别**: `semi_auto` (半自动化)

**触发机制**: `embedded_reminders` (嵌入式提醒)

**配置位置**: `.cursor/rules/`, `.cursorrules`

**文件引用语法**: `@path/to/file` (需要 AI 理解)

---

## 平台能力

### 优势特性

✅ **AI 原生编辑器** - 深度集成 AI 辅助编程

✅ **规则系统** - `.cursor/rules/` 目录存放项目规则

✅ **@文件引用** - 可以通过 `@filename` 引用文件

✅ **Composer 模式** - 多文件编辑能力

✅ **上下文理解** - AI 可以理解嵌入式提醒

✅ **VSCode 兼容** - 兼容 VSCode 扩展和配置

### 限制

⚠️ **无 Hook 系统** - 不能自动监听文件变化

⚠️ **依赖 AI 理解** - 需要 AI 主动理解和执行规则

⚠️ **手动触发** - 用户需要提醒 AI 执行更新

⚠️ **文件引用不稳定** - `@file` 语法可能不总是有效

---

## 适配策略

### 方案: 规则文件 + 嵌入式提醒

```
.cursor/rules/
├── doc-maintenance.md       ← 主规则文件 (嵌入提醒)
└── index-system-prompt.md   ← 索引系统说明
```

**工作流程**:
1. 用户修改代码文件
2. AI 读取 `.cursor/rules/doc-maintenance.md`
3. AI 理解嵌入的自引用提醒
4. AI 主动调用索引系统更新

**提醒示例**:
```markdown
🔄 **重要**: 当你修改代码文件时，检测是否有结构性变化 (import/export)。
如果有，执行索引更新流程。
```

---

## 接口实现

此适配器实现 [platform-interface.md](../../core/platform-interface.md) 定义的接口方法。

---

### 1. 文件操作接口

#### readFile(path)

**实现方式**: 使用 AI 的文件读取能力

**Prompt 模板**:
```markdown
请读取文件: {path}

返回完整内容。
```

**代码示例**:
```typescript
async function readFile(path: string): Promise<string> {
  // Cursor 环境下,直接请求 AI 读取文件
  const prompt = `请读取文件: ${path}\n\n返回完整内容。`;
  return await askAI(prompt);
}
```

---

#### writeFile(path, content)

**实现方式**: 使用 AI 的文件写入能力

**Prompt 模板**:
```markdown
请创建文件: {path}

内容如下:
\`\`\`
{content}
\`\`\`
```

**代码示例**:
```typescript
async function writeFile(path: string, content: string): Promise<void> {
  const prompt = `请创建文件: ${path}\n\n内容如下:\n\`\`\`\n${content}\n\`\`\``;
  await askAI(prompt);
}
```

---

#### editFile(path, oldString, newString)

**实现方式**: 使用 AI 的文件编辑能力

**Prompt 模板**:
```markdown
请编辑文件: {path}

将以下内容:
\`\`\`
{oldString}
\`\`\`

替换为:
\`\`\`
{newString}
\`\`\`
```

**代码示例**:
```typescript
async function editFile(
  path: string,
  oldString: string,
  newString: string
): Promise<void> {
  const prompt = `请编辑文件: ${path}\n\n` +
    `将以下内容:\n\`\`\`\n${oldString}\n\`\`\`\n\n` +
    `替换为:\n\`\`\`\n${newString}\n\`\`\``;
  await askAI(prompt);
}
```

---

### 2. 文件系统接口

#### scanFiles(rootPath, patterns)

**实现方式**: 使用文件系统 API

**Prompt 模板**:
```markdown
请扫描目录: {rootPath}

包含模式: {includePatterns}
排除模式: {excludePatterns}

返回所有匹配的文件路径列表。
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
    `包含模式: ${patterns.include.join(', ')}\n` +
    `排除模式: ${patterns.exclude.join(', ')}\n\n` +
    `返回所有匹配的文件路径列表。`;
  const result = await askAI(prompt);
  return JSON.parse(result);
}
```

---

#### getProjectRoot()

**实现方式**: 使用 VSCode API (Cursor 基于 VSCode)

**代码示例**:
```typescript
function getProjectRoot(): string {
  // Cursor 继承自 VSCode,可以使用 workspace API
  return vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd();
}
```

---

### 3. 用户交互接口

#### askConfirmation(message)

**实现方式**: 通过对话请求用户确认

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

**实现方式**: 使用 VSCode 通知 API

**代码示例**:
```typescript
function showMessage(message: string, type: 'info' | 'success' | 'warning' | 'error'): void {
  switch (type) {
    case 'info':
      vscode.window.showInformationMessage(message);
      break;
    case 'success':
      vscode.window.showInformationMessage(`✅ ${message}`);
      break;
    case 'warning':
      vscode.window.showWarningMessage(`⚠️ ${message}`);
      break;
    case 'error':
      vscode.window.showErrorMessage(`❌ ${message}`);
      break;
  }
}
```

---

### 4. 国际化接口

#### getLanguage()

**实现方式**: 读取 `.cursor/locale-config.json` 或使用 VSCode 语言设置

**代码示例**:
```typescript
async function getLanguage(): Promise<string> {
  // 优先级 1: 读取项目配置
  try {
    const config = await readFile('.cursor/locale-config.json');
    const parsed = JSON.parse(config);
    return parsed.language || 'zh-CN';
  } catch {
    // 优先级 2: 使用 VSCode 语言设置
    const vscodeLang = vscode.env.language;
    return vscodeLang.startsWith('zh') ? 'zh-CN' : 'en-US';
  }
}
```

---

#### loadLanguageFiles(lang)

**实现方式**: 使用 `@file` 引用或直接读取

**Prompt 模板**:
```markdown
请加载语言文件:
- universal/locales/{lang}/messages.md
- universal/locales/{lang}/templates.md

返回合并后的翻译对象。
```

**代码示例**:
```typescript
async function loadLanguageFiles(lang: string): Promise<LanguageData> {
  const messagesPath = `universal/locales/${lang}/messages.md`;
  const templatesPath = `universal/locales/${lang}/templates.md`;

  const messages = await readFile(messagesPath);
  const templates = await readFile(templatesPath);

  return {
    messages: parseMarkdownToObject(messages),
    templates: parseMarkdownToObject(templates)
  };
}
```

---

### 5. 平台特定接口

#### generatePlatformConfig(targetPath, language)

**功能**: 生成 Cursor 规则文件

**实现方式**: 创建 `.cursor/rules/` 配置

**代码示例**:
```typescript
async function generatePlatformConfig(
  targetPath: string,
  language: string
): Promise<void> {
  const rulesDir = path.join(targetPath, '.cursor/rules');

  // 创建主规则文件
  const mainRule = generateMainRule(language);
  await writeFile(
    path.join(rulesDir, 'doc-maintenance.md'),
    mainRule
  );

  // 创建索引系统说明
  const systemPrompt = generateSystemPrompt(language);
  await writeFile(
    path.join(rulesDir, 'index-system-prompt.md'),
    systemPrompt
  );

  // 创建 .cursorrules (全局规则)
  const globalRule = generateGlobalRule(language);
  await writeFile(
    path.join(targetPath, '.cursorrules'),
    globalRule
  );
}
```

---

#### enableAutoTrigger()

**功能**: 尽可能启用自动触发 (有限支持)

**实现方式**: 生成强提醒规则

**代码示例**:
```typescript
async function enableAutoTrigger(): Promise<void> {
  // Cursor 无法真正自动触发,只能通过强提醒
  const reminderRule = `
# 🔄 索引系统自动维护规则

**关键**: 当你修改代码文件时，务必检查以下内容:

1. **检测结构性变化**
   - 是否修改了 import/export 语句?
   - 是否添加/删除了函数/类定义?

2. **执行更新** (如果检测到变化)
   - 调用索引更新流程
   - 更新相关文档

3. **保持静默** (如果没有结构性变化)
   - 不更新索引
   - 继续当前任务

**这是一个重要的项目约定，请主动执行!**
`;

  await writeFile('.cursor/rules/auto-trigger-reminder.md', reminderRule);

  showMessage(
    '已生成自动触发提醒规则。注意: Cursor 需要 AI 主动理解并执行。',
    'warning'
  );
}
```

---

## 配置文件模板

### .cursor/rules/doc-maintenance.md

此规则文件包含完整的索引维护逻辑。

**生成方式**: 使用 `generatePlatformConfig()` 方法

**内容结构**:
```markdown
# 项目文档自动维护规则

## 核心职责
当你修改代码文件时，自动维护项目索引系统。

## 检测时机
在以下操作后触发检测:
- 创建新文件
- 修改现有文件
- 删除文件

## 检测逻辑
参考: @universal/core/analyzer/dependency-parser.md
参考: @universal/core/analyzer/export-parser.md

## 更新流程
参考: @universal/core/generator/update-workflow.md

## 国际化
参考: @universal/locales/{language}/messages.md
```

**特点**:
- 使用 `@file` 语法引用 Universal 核心文档
- 嵌入明确的自引用提醒
- 包含完整的维护逻辑

---

### .cursorrules (全局规则)

**内容**:
```markdown
# 项目约定

## 文档维护
本项目使用分形索引系统自动维护文档。

当你修改代码文件时:
1. 检查 `.cursor/rules/doc-maintenance.md`
2. 按照规则执行索引更新

详见: `.cursor/rules/doc-maintenance.md`
```

---

## 使用指南

### 安装步骤

#### 1. 生成 Cursor 配置
```bash
# 在项目根目录执行
在 Cursor 中运行: "请为本项目生成索引系统配置"
```

AI 将执行:
1. 调用 `universal/adapters/cursor/adapter.md`
2. 生成 `.cursor/rules/` 配置文件
3. 创建 `.cursorrules` 全局规则

#### 2. 验证配置
```bash
# 检查生成的文件
ls -la .cursor/rules/
cat .cursorrules
```

应该看到:
- `.cursor/rules/doc-maintenance.md`
- `.cursor/rules/index-system-prompt.md`
- `.cursorrules`

---

### 初始化索引

**方法 1: 通过对话**
```
用户: "请为本项目初始化索引系统"
AI: [读取 .cursor/rules/doc-maintenance.md]
    [调用 universal/core/generator/init-workflow.md]
    [执行初始化...]
```

**方法 2: 手动触发**
```
用户: "读取 @.cursor/rules/doc-maintenance.md 并执行初始化"
AI: [执行...]
```

---

### 日常使用

#### 自动触发 (理想情况)
```
用户修改代码文件 (添加 import)
  ↓
AI 理解到规则中的提醒
  ↓
AI 主动检测结构性变化
  ↓
AI 调用更新流程
  ↓
静默完成更新
```

#### 手动提醒 (实际情况)
```
用户: "我修改了 user.service.ts, 请检查是否需要更新索引"
AI: [读取规则] → [检测变化] → [执行更新]
```

---

### 更新索引

**触发方式**:
1. **AI 主动** (如果 AI 理解了规则)
   - AI 检测到代码变化
   - AI 自动执行更新

2. **用户提醒**
   ```
   "请更新索引"
   "检查文档是否需要更新"
   "我改了代码，更新一下文档"
   ```

**执行流程**:
```
AI 读取 .cursor/rules/doc-maintenance.md
  ↓
调用 universal/core/generator/update-workflow.md
  ↓
分析变更文件
  ↓
更新索引
```

---

### 检查索引一致性

**命令**:
```
用户: "检查索引系统的一致性"
AI: [调用 universal/core/generator/check-workflow.md]
    [生成检查报告]
```

**报告内容**:
- 缺失文件头的文件列表
- FOLDER_INDEX 与实际文件不一致的目录
- 循环依赖检测结果

---

## 平台限制与变通

### 限制 1: 无法自动触发

**影响**: 需要用户提醒或 AI 主动理解

**变通方案**:
1. **强提醒规则**: 在规则文件中使用醒目的提醒
2. **用户习惯**: 培养用户定期提醒的习惯
3. **批量更新**: 在大改动后一次性更新

---

### 限制 2: @文件引用不稳定

**影响**: `@universal/core/...` 可能失效

**变通方案**:
1. **静态内联**: 将核心逻辑复制到规则文件中
2. **手动引用**: 明确告诉 AI 要读取哪些文件
3. **检查机制**: AI 定期验证引用是否有效

---

### 限制 3: 依赖 AI 理解

**影响**: AI 可能忽略规则或理解错误

**变通方案**:
1. **清晰的规则**: 使用简单明确的语言
2. **分步指令**: 将复杂流程分解为多个步骤
3. **用户监督**: 用户定期检查更新是否正确

---

## 测试清单

### 功能测试
- [ ] 生成配置文件成功
- [ ] 初始化索引成功
- [ ] 手动更新索引成功
- [ ] AI 主动更新索引 (如果可能)
- [ ] 检查功能正常
- [ ] 国际化切换正常

### 兼容性测试
- [ ] Windows 环境
- [ ] macOS 环境
- [ ] Linux 环境
- [ ] 与 VSCode 扩展兼容

### 性能测试
- [ ] 小项目 (<50 文件): 可用
- [ ] 中型项目 (100-500 文件): 可用
- [ ] 大型项目 (1000+ 文件): 可用 (可能较慢)

---

## 常见问题

### Q: AI 没有主动执行更新怎么办?

**A**: 这是 Cursor 的常见情况。变通方法:
1. 手动提醒 AI: "请检查并更新索引"
2. 使用明确的命令: "读取规则并执行更新"
3. 定期批量更新: "我改了 10 个文件,统一更新索引"

---

### Q: @文件引用失效怎么办?

**A**: 使用静态内联方式:
1. 将 `universal/core/` 的内容复制到 `.cursor/rules/`
2. 修改规则文件,使用本地路径
3. 明确告诉 AI 要读取的文件路径

---

### Q: 如何提高自动化程度?

**A**:
1. **培养 AI 习惯**: 多次提醒后,AI 可能会形成"习惯"
2. **使用 Composer**: 在 Composer 模式下,AI 更容易理解多文件操作
3. **明确约定**: 在对话开始时明确告诉 AI 要遵守的规则

---

## 最佳实践

### 1. 规则文件管理
- 将规则文件加入 Git
- 定期检查规则文件是否需要更新
- 与团队成员同步规则

### 2. AI 提醒技巧
- 使用简短明确的命令
- 在大改动前提醒 AI 注意文档维护
- 定期要求 AI 检查索引一致性

### 3. 团队协作
- 在 README 中说明使用方法
- 培训团队成员如何提醒 AI
- 建立定期检查机制

---

## 示例项目

参考: `examples/cursor-example/`

包含:
- 完整的 `.cursor/rules/` 配置
- 示例代码文件
- 演示 GIF
- 使用说明

---

## 版本历史

### v1.0.0 (2025-12-23)
- ✅ 基础适配器实现
- ✅ 规则文件生成
- ✅ 手动更新流程
- ✅ 国际化支持

### 未来计划
- 🔧 提高自动化程度的实验
- 🔧 更好的 @文件引用支持
- 🔧 Cursor 插件开发 (如果 API 开放)

---

**下一步**: 参考 [使用指南](#使用指南) 开始使用
