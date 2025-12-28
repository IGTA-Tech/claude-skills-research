# 国际化使用指南 (I18N Guide)

## 🌍 快速开始

项目多级索引系统现已支持中英文双语！

### 切换到英文

**方法 1: 使用命令**（推荐）
```
/set-language
```
选择 `2. English (en-US)`

**方法 2: 手动创建配置文件**
```bash
mkdir -p .claude
cat > .claude/locale-config.json << 'EOF'
{
  "language": "en-US",
  "fallback": "zh-CN"
}
EOF
```

### 切换到中文（默认）

使用命令选择 `1. 简体中文 (zh-CN)`，或删除配置文件。

---

## 📂 项目结构（新版2.0）

```
project-multilevel-index/
├── locales/                          # 语言文件
│   ├── zh-CN/                        # 简体中文
│   │   ├── messages.json            # 命令输出、通知
│   │   ├── skill.json               # 技能描述
│   │   ├── templates.json           # 文件头模板
│   │   └── hooks.json               # Hook提示
│   └── en-US/                        # 美国英语
│       └── [同上结构]
│
├── skills/project-multilevel-index/
│   ├── SKILL.md                     # 主入口（简化版200行）
│   ├── core/                        # 核心模块
│   │   ├── i18n.md                  # 国际化加载逻辑
│   │   └── concepts.md              # 核心概念
│   ├── commands_impl/               # 命令实现
│   │   ├── init-index.md           # /init-index
│   │   ├── update-index.md         # /update-index
│   │   ├── check-index.md          # /check-index
│   │   └── set-language.md         # /set-language
│   └── templates/                   # 文件模板（保持不变）
│
└── .claude/
    └── locale-config.json           # 用户语言配置
```

---

## 🎯 支持的语言

- **zh-CN**: 简体中文（默认）
- **en-US**: 美国英语

---

## 💡 使用示例

### 示例 1: 初始化英文索引

```bash
# 1. 切换语言
/set-language
# 选择: 2

# 2. 初始化索引
/init-index
```

**输出（英文）**:
```
Current directory is /home/user/my-project, confirm this is the project root?

Scanning project...
Found:
- JavaScript/TypeScript: 45 files
- Python: 12 files
- Total 57 code files across 8 folders

✅ Complete! Created PROJECT_INDEX.md, check project architecture.

Generated:
- 57 file header comments
- 8 FOLDER_INDEX.md files
- 1 PROJECT_INDEX.md
```

### 示例 2: 检查索引（中文）

```bash
# 1. 切换回中文
/set-language
# 选择: 1

# 2. 检查索引
/check-index
```

**输出（中文）**:
```
正在检查索引系统...

索引一致性检查报告
===================

文件头完整性: 57/57 ✅
文件夹索引: 8/8 ✅
依赖关系: ✅ 无循环依赖
索引结构: ✅

🎉 索引系统运行完美！
```

---

## 🔧 配置说明

### 配置文件位置

`.claude/locale-config.json`

### 配置选项

```json
{
  "language": "en-US",           // 当前语言
  "fallback": "zh-CN",           // 备用语言
  "availableLanguages": [        // 可用语言列表
    "zh-CN",
    "en-US"
  ]
}
```

### 环境变量（可选）

```bash
# Linux/macOS
export CLAUDE_LOCALE=en-US

# Windows PowerShell
$env:CLAUDE_LOCALE = "en-US"
```

**优先级**:
1. 项目配置文件（.claude/locale-config.json）
2. 环境变量（CLAUDE_LOCALE）
3. 默认值（zh-CN）

---

## 📝 技术术语处理

以下术语在所有语言中保持英文（不翻译）：

- **Input** - 文件依赖
- **Output** - 文件导出
- **Pos** - 文件定位
- **PROJECT_INDEX** - 项目索引
- **FOLDER_INDEX** - 文件夹索引
- **Mermaid** - 图表格式

这样做的原因：
1. 保持技术一致性
2. 便于跨语言理解
3. 避免翻译歧义

---

## 🌟 新增功能（v2.0）

### 1. 模块化架构

- 主SKILL.md从 1098行 精简到 200行
- 命令独立成文件，易于维护
- 核心概念独立文档

### 2. 完整国际化

- 命令输出双语支持
- 文件头注释双语
- Hook提示双语
- 错误消息双语

### 3. 新命令

- `/set-language` - 快速切换语言

### 4. 更好的文档

- 每个命令都有详细实现文档
- 国际化加载逻辑单独文档
- 核心概念独立说明

---

## 🚀 贡献翻译

想要添加新语言？欢迎贡献！

### 步骤：

1. **复制语言文件**
   ```bash
   mkdir -p locales/ja-JP
   cp -r locales/en-US/* locales/ja-JP/
   ```

2. **翻译JSON文件**
   - 翻译 `messages.json`
   - 翻译 `skill.json`
   - 翻译 `templates.json`
   - 翻译 `hooks.json`

3. **保持结构不变**
   - 不要修改JSON的键名
   - 保持占位符（{directory}, {count}等）
   - 保持技术术语（Input, Output, Pos）

4. **测试翻译**
   ```json
   {
     "language": "ja-JP",
     "fallback": "en-US"
   }
   ```

5. **提交PR**

---

## ❓ 常见问题

### Q: 切换语言后需要重新初始化索引吗？

A: 不需要。已生成的索引文件不会改变，只有新生成的内容才使用新语言。

### Q: 可以混用中英文吗？

A: 不建议。系统每次只使用一种语言，混用可能导致输出不一致。

### Q: 如何查看当前使用的语言？

A: 查看 `.claude/locale-config.json` 文件，或运行任意命令查看输出语言。

### Q: 语言文件在哪里？

A: `locales/zh-CN/` 和 `locales/en-US/` 目录。

### Q: 如何重置为默认语言？

A: 删除 `.claude/locale-config.json` 文件，或使用 `/set-language` 选择中文。

---

## 📞 反馈和支持

如有问题或建议，请：
1. 查看 [SKILL.md](skills/project-multilevel-index/SKILL.md)
2. 查看 [core/i18n.md](skills/project-multilevel-index/core/i18n.md)
3. 提交 Issue

---

**版本**: 2.0.0
**更新日期**: 2025-12-22
**新特性**: 模块化架构 + 完整国际化支持
