#!/bin/bash

# Claude Skills Guide - GitHub 发布脚本
# GitHub Publishing Script for Claude Skills Guide

set -e

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                      ║"
echo "║          🚀 Claude Skills Guide - GitHub 发布工具 🚀                 ║"
echo "║                                                                      ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查是否在正确的目录
if [ ! -f "README.md" ] || [ ! -f "LICENSE" ]; then
    echo -e "${RED}❌ 错误：请在项目根目录运行此脚本${NC}"
    exit 1
fi

echo -e "${BLUE}📋 步骤 1/6: 检查 Git 配置...${NC}"
if ! git config user.name > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  未配置 Git 用户名${NC}"
    read -p "请输入你的 GitHub 用户名: " username
    git config user.name "$username"
fi

if ! git config user.email > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  未配置 Git 邮箱${NC}"
    read -p "请输入你的 GitHub 邮箱: " email
    git config user.email "$email"
fi

GIT_USERNAME=$(git config user.name)
GIT_EMAIL=$(git config user.email)
echo -e "${GREEN}✅ Git 配置完成${NC}"
echo -e "   用户名: ${GIT_USERNAME}"
echo -e "   邮箱: ${GIT_EMAIL}"
echo ""

echo -e "${BLUE}📋 步骤 2/6: 获取 GitHub 用户名...${NC}"
read -p "请输入你的 GitHub 用户名（用于仓库 URL）: " GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo -e "${RED}❌ GitHub 用户名不能为空${NC}"
    exit 1
fi

echo -e "${GREEN}✅ GitHub 用户名: ${GITHUB_USERNAME}${NC}"
echo ""

echo -e "${BLUE}📋 步骤 3/6: 更新 README 中的链接...${NC}"
# 替换 README.md 中的 YOUR_USERNAME
sed -i.bak "s/YOUR_USERNAME/${GITHUB_USERNAME}/g" README.md
sed -i.bak "s/YOUR_USERNAME/${GITHUB_USERNAME}/g" README_EN.md
sed -i.bak "s/YOUR_USERNAME/${GITHUB_USERNAME}/g" CONTRIBUTING.md
rm -f README.md.bak README_EN.md.bak CONTRIBUTING.md.bak
echo -e "${GREEN}✅ 链接更新完成${NC}"
echo ""

echo -e "${BLUE}📋 步骤 4/6: 初始化 Git 仓库...${NC}"
if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}✅ Git 仓库初始化完成${NC}"
else
    echo -e "${YELLOW}⚠️  Git 仓库已存在，跳过初始化${NC}"
fi
echo ""

echo -e "${BLUE}📋 步骤 5/6: 添加文件到 Git...${NC}"
git add .
git status
echo ""

read -p "是否继续提交？(y/n): " confirm
if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo -e "${YELLOW}⚠️  已取消${NC}"
    exit 0
fi

git commit -m "Initial commit: Claude Skills Development Guide

- 📚 完整的中文开发指南（2500+ 行）
- 📖 英文 README
- 🎨 20 个官方示例 Skills
- 📝 贡献指南和许可证
- ✨ 快速参考卡片

Complete Chinese development guide (2500+ lines)
English README
20 official example Skills
Contributing guide and license
Quick reference card"

echo -e "${GREEN}✅ 提交完成${NC}"
echo ""

echo -e "${BLUE}📋 步骤 6/6: 准备推送到 GitHub...${NC}"
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}📝 下一步操作：${NC}"
echo ""
echo -e "1. 在 GitHub 上创建新仓库："
echo -e "   ${BLUE}https://github.com/new${NC}"
echo -e "   仓库名: ${GREEN}claude-skills-guide${NC}"
echo -e "   描述: ${GREEN}📚 Claude Skills 开发完全指南 - 从基础到精通${NC}"
echo -e "   ${YELLOW}⚠️  不要初始化 README、.gitignore 或 LICENSE${NC}"
echo ""
echo -e "2. 创建完成后，运行以下命令推送代码："
echo ""
echo -e "${GREEN}git branch -M main${NC}"
echo -e "${GREEN}git remote add origin https://github.com/${GITHUB_USERNAME}/claude-skills-guide.git${NC}"
echo -e "${GREEN}git push -u origin main${NC}"
echo ""
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

read -p "是否现在就推送到 GitHub？(y/n): " push_now
if [ "$push_now" = "y" ] || [ "$push_now" = "Y" ]; then
    echo ""
    echo -e "${BLUE}🚀 开始推送...${NC}"
    
    git branch -M main
    
    # 检查是否已有 remote
    if git remote | grep -q "origin"; then
        echo -e "${YELLOW}⚠️  remote origin 已存在，删除旧的...${NC}"
        git remote remove origin
    fi
    
    git remote add origin "https://github.com/${GITHUB_USERNAME}/claude-skills-guide.git"
    
    echo -e "${YELLOW}⚠️  请确保你已在 GitHub 上创建了仓库！${NC}"
    read -p "按 Enter 继续推送..."
    
    if git push -u origin main; then
        echo ""
        echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${GREEN}║                                                                      ║${NC}"
        echo -e "${GREEN}║                    🎉 发布成功！ 🎉                                   ║${NC}"
        echo -e "${GREEN}║                                                                      ║${NC}"
        echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        echo -e "🌐 仓库地址: ${BLUE}https://github.com/${GITHUB_USERNAME}/claude-skills-guide${NC}"
        echo ""
        echo -e "${YELLOW}📝 建议的后续步骤：${NC}"
        echo -e "1. 在 GitHub 上添加仓库描述和标签"
        echo -e "2. 启用 GitHub Pages（如果需要）"
        echo -e "3. 添加 Topics: claude, ai, skills, guide, tutorial"
        echo -e "4. 分享给社区！"
        echo ""
    else
        echo ""
        echo -e "${RED}❌ 推送失败${NC}"
        echo -e "${YELLOW}可能的原因：${NC}"
        echo -e "1. 仓库尚未在 GitHub 上创建"
        echo -e "2. 没有推送权限"
        echo -e "3. 网络问题"
        echo ""
        echo -e "${YELLOW}请手动运行以下命令：${NC}"
        echo -e "${GREEN}git push -u origin main${NC}"
    fi
else
    echo ""
    echo -e "${GREEN}✅ 准备完成！${NC}"
    echo -e "${YELLOW}记得手动推送代码到 GitHub！${NC}"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}感谢使用 Claude Skills Guide！${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

