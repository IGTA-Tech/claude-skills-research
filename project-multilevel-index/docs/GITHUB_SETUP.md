# 🚀 GitHub 发布指南

本指南将帮助你将插件发布到 GitHub 并设置开源项目。

---

## 📋 前提条件

- [x] 已有 GitHub 账号
- [x] 已安装 Git
- [x] 本地代码已就绪

---

## 步骤 1: 在 GitHub 创建仓库

### 1.1 访问 GitHub

前往 https://github.com/new

### 1.2 填写仓库信息

- **Repository name**: `project-multilevel-index`
- **Description**: `🔄 A fractal self-referential documentation system for code projects - Inspired by Gödel, Escher, Bach`
- **Visibility**: Public ✅
- **Initialize**: 不要勾选任何选项（README, .gitignore, license）

### 1.3 创建仓库

点击 "Create repository"

---

## 步骤 2: 连接本地仓库

### 2.1 添加远程仓库

在本地项目目录执行：

```bash
cd h:\Project\Claud_skill\project-multilevel-index

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/project-multilevel-index.git

# 验证远程仓库
git remote -v
```

### 2.2 重命名主分支

```bash
# 将 master 重命名为 main（GitHub 默认）
git branch -M main
```

### 2.3 推送代码

```bash
# 首次推送
git push -u origin main
```

---

## 步骤 3: 配置仓库设置

### 3.1 添加仓库描述和主题

1. 进入仓库页面
2. 点击 "About" 旁的设置图标 ⚙️
3. 填写：
   - **Description**: `🔄 A fractal self-referential documentation system for code projects`
   - **Website**: 留空或填写文档链接
   - **Topics** (标签):
     - `claude-code`
     - `documentation`
     - `dependency-graph`
     - `code-indexing`
     - `mermaid`
     - `fractal`
     - `self-reference`
     - `plugin`
     - `typescript`
     - `python`

### 3.2 启用 Issues 和 Discussions

1. 进入 **Settings** → **General**
2. 确保勾选:
   - ✅ Issues
   - ✅ Discussions
3. 点击 **Save changes**

### 3.3 设置 Discussions

1. 进入 **Discussions** 标签
2. 启用 Discussions
3. 创建分类:
   - 💡 Ideas (想法和建议)
   - 🙏 Q&A (问答)
   - 📢 Announcements (公告)
   - 🎉 Show and tell (展示和分享)

---

## 步骤 4: 创建首个 Release

### 4.1 准备 Release

1. 进入仓库页面
2. 点击右侧的 **Releases** → **Create a new release**

### 4.2 填写 Release 信息

- **Tag version**: `v1.0.1`
- **Target**: `main`
- **Release title**: `v1.0.1 - Initial Release 🎉`
- **Description**: 复制 [RELEASE_NOTES.md](RELEASE_NOTES.md) 的内容

### 4.3 添加二进制文件（可选）

可以上传打包的压缩文件：

```bash
# 创建发布包
cd h:\Project\Claud_skill
zip -r project-multilevel-index-v1.0.1.zip project-multilevel-index \
  -x "project-multilevel-index/.git/*" \
  -x "project-multilevel-index/test-project/PROJECT_INDEX.md" \
  -x "project-multilevel-index/test-project/**/FOLDER_INDEX.md"
```

### 4.4 发布

- 勾选 ✅ **Set as the latest release**
- 点击 **Publish release**

---

## 步骤 5: 配置 GitHub Pages (可选)

如果想托管文档：

1. 进入 **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `main` / `docs` (如果有 docs 文件夹)
4. 点击 **Save**

---

## 步骤 6: 添加徽章和链接

### 6.1 更新 README 中的链接

将 README.md 中的所有 `YOUR_USERNAME` 替换为你的实际 GitHub 用户名：

```bash
# 使用 sed 批量替换（macOS/Linux）
sed -i 's/YOUR_USERNAME/你的用户名/g' README.md
sed -i 's/YOUR_USERNAME/你的用户名/g' CONTRIBUTING.md
sed -i 's/YOUR_USERNAME/你的用户名/g' INSTALL_GUIDE.md
sed -i 's/YOUR_USERNAME/你的用户名/g' RELEASE_NOTES.md
sed -i 's/YOUR_USERNAME/你的用户名/g' .github/ISSUE_TEMPLATE/config.yml

# Windows PowerShell
(Get-Content README.md) -replace 'YOUR_USERNAME','你的用户名' | Set-Content README.md
```

### 6.2 提交更新

```bash
git add .
git commit -m "docs: update GitHub username in all documentation"
git push
```

---

## 步骤 7: 社区推广

### 7.1 分享到社区

- 在 Claude Code 社区分享
- Reddit r/ClaudeAI
- Twitter/X 使用话题 #ClaudeCode
- Dev.to 撰写介绍文章

### 7.2 创建演示视频（可选）

使用 [Asciinema](https://asciinema.org/) 录制终端演示：

```bash
asciinema rec demo.cast
# 运行演示命令
# Ctrl+D 结束录制
asciinema upload demo.cast
```

### 7.3 添加贡献者指南

确保 CONTRIBUTING.md 准确反映你的流程和期望。

---

## 步骤 8: 持续维护

### 8.1 设置 GitHub Actions (未来)

创建 `.github/workflows/test.yml` 进行自动化测试。

### 8.2 定期更新

- 响应 Issues 和 Pull Requests
- 定期发布新版本
- 更新 CHANGELOG.md

### 8.3 管理 Releases

后续版本发布流程：

```bash
# 1. 更新版本号
# 编辑 .claude-plugin/plugin.json

# 2. 更新 CHANGELOG.md
# 添加新版本的变更

# 3. 提交版本变更
git add .
git commit -m "chore: bump version to v1.1.0"
git push

# 4. 创建 Tag
git tag v1.1.0
git push origin v1.1.0

# 5. 在 GitHub 创建 Release
# 使用新的 tag 创建 release
```

---

## ✅ 检查清单

发布前最终检查：

- [ ] 所有文档中的 `YOUR_USERNAME` 已替换
- [ ] README.md 徽章链接正确
- [ ] LICENSE 文件存在
- [ ] .gitignore 配置正确
- [ ] Issue 模板配置完成
- [ ] PR 模板存在
- [ ] CONTRIBUTING.md 清晰明确
- [ ] 测试项目可正常运行
- [ ] 首次提交已推送
- [ ] Release 已创建
- [ ] Topics/标签已添加
- [ ] Discussions 已启用

---

## 🎉 完成！

恭喜！你的开源项目已成功发布到 GitHub！

**下一步**:
1. 在社区分享你的项目
2. 响应第一个 Issue 或 PR
3. 持续改进和维护

**项目地址**: https://github.com/YOUR_USERNAME/project-multilevel-index

---

## 📞 需要帮助？

- [GitHub 文档](https://docs.github.com)
- [开源指南](https://opensource.guide/)
- [GitHub Community](https://github.community/)
