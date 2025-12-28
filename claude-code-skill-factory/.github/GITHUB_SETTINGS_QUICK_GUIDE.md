# GitHub Settings Quick Guide

**Repository**: claude-code-skills-factory
**Time Required**: 15-20 minutes
**Date**: November 12, 2025

---

## 🎯 What You're Doing

Setting up branch protection rules and making `dev` the default branch so:
- No one can push directly to `main` (including you)
- All changes go through `dev` branch first
- PRs are validated before merging
- Workflow automation works properly

---

## 📋 Step-by-Step Instructions

### Step 1: Open Repository Settings (1 min)

1. Go to: `https://github.com/alirezarezvani/claude-code-skill-factory`
2. Click the **"Settings"** tab (top right, next to Insights)
3. In the left sidebar, find **"Code and automation"** section
4. Click **"Branches"**

You should now see the "Branches" settings page.

---

### Step 2: Set `dev` as Default Branch (2 min)

**At the top of the Branches page:**

1. Look for **"Default branch"** section (shows current: `main`)
2. Click the **switch icon** (⇄) next to `main`
3. In the dropdown, select **`dev`**
4. Click **"Update"** button
5. A warning appears: **"I understand, update the default branch"**
6. Click the red **"I understand, update the default branch"** button

**Result**: Default branch is now `dev` ✅

---

### Step 3: Protect `main` Branch (8-10 min)

Scroll down to **"Branch protection rules"** section.

#### 3a. Add Rule for `main`

1. Click **"Add rule"** button (or **"Add branch protection rule"**)
2. In **"Branch name pattern"** field, type: `main`

#### 3b. Configure Protection Settings

**Check these boxes in order:**

1. ☑️ **Require a pull request before merging**
   - This expands with sub-options:
   - ☑️ **Require approvals**: Set to **1**
   - ☑️ **Dismiss stale pull request approvals when new commits are pushed**
   - ☑️ **Require approval of the most recent reviewable push**

2. ☑️ **Require status checks to pass before merging**
   - ☑️ **Require branches to be up to date before merging**
   - **Status checks**: Leave empty for now (will populate after first PR)

3. ☑️ **Require conversation resolution before merging**

4. ☑️ **Require linear history**

5. Scroll down to **"Rules applied to everyone including administrators"**
   - ☑️ **Restrict who can push to matching branches**
     - Under this, select: **"Restrict pushes that create matching branches"**
   - **Allow force pushes**: ☐ (leave UNCHECKED)
   - **Allow deletions**: ☐ (leave UNCHECKED)

#### 3c. Save Rule

1. Scroll to bottom
2. Click **"Create"** button (green)

**Result**: `main` branch is now protected ✅

---

### Step 4: Protect `dev` Branch (8-10 min)

Still on the "Branches" settings page.

#### 4a. Add Rule for `dev`

1. Click **"Add rule"** button again
2. In **"Branch name pattern"** field, type: `dev`

#### 4b. Configure Protection Settings

**Check these boxes:**

1. ☑️ **Require a pull request before merging**
   - ☑️ **Require approvals**: Set to **1**
   - ☑️ **Dismiss stale pull request approvals when new commits are pushed**
   - ☑️ **Require approval of the most recent reviewable push**

2. ☑️ **Require status checks to pass before merging**
   - ☑️ **Require branches to be up to date before merging**
   - **Status checks**: Leave empty for now

3. ☑️ **Require conversation resolution before merging**

4. ☑️ **Require linear history**

5. Scroll to **"Rules applied to everyone including administrators"**
   - **Restrict who can push**: ☐ (leave UNCHECKED - allows direct push for flexibility)
   - **Allow force pushes**: ☐ (leave UNCHECKED)
   - **Allow deletions**: ☐ (leave UNCHECKED)

#### 4c. Save Rule

1. Scroll to bottom
2. Click **"Create"** button (green)

**Result**: `dev` branch is now protected ✅

---

## ✅ Verification Checklist

After completing all steps, verify:

### In GitHub UI:

1. Go to Settings → Branches
2. You should see:
   - **Default branch**: `dev` (not `main`)
   - **Branch protection rules**: 2 rules
     - `main` (with all protections)
     - `dev` (with PR requirements)

### Test Protection:

**Test 1**: Try to push to main locally
```bash
git checkout main
git commit --allow-empty -m "test: try to push to main"
git push origin main
```

**Expected**: ❌ Push should be rejected with error:
```
remote: error: GH006: Protected branch update failed
remote: error: Changes must be made through a pull request
```

If you see this error, protection is working! ✅

**Clean up**:
```bash
git reset HEAD~1  # Undo the test commit
git checkout dev
```

---

## 📸 What It Should Look Like

### Default Branch Section:
```
Default branch
──────────────
dev  [Switch to another branch ⇄]

The default branch is considered the "base" branch in your repository,
against which all pull requests and code commits are automatically made,
unless you specify a different branch.
```

### Branch Protection Rules Section:
```
Branch protection rules
───────────────────────

Branch name pattern          Status
main                         Active  [Edit] [Delete]
dev                          Active  [Edit] [Delete]

[Add rule]
```

---

## 🚨 Common Issues

### Issue 1: "Create" button is grayed out

**Solution**: Make sure you entered the branch name pattern (`main` or `dev`)

### Issue 2: Can't find "Branches" in Settings

**Solution**: You need admin access to the repository. Check your permissions.

### Issue 3: Status checks not appearing

**Solution**: This is normal! Status checks only appear after workflows run at least once. We'll select them later.

### Issue 4: Already have branch protection rules

**Solution**: Click "Edit" instead of "Add rule" and update the existing rule with the settings above.

---

## 🎯 What Happens Next

After you complete these steps:

1. ✅ `dev` is the default branch (new PRs automatically target `dev`)
2. ✅ `main` is protected (requires PR + approval + checks)
3. ✅ `dev` is protected (requires PR + approval + checks)
4. ✅ No one can push directly to `main` (including admins)
5. ✅ Direct pushes to `dev` allowed (for flexibility), but merges require PR

**Next**: We'll create workflows that enforce branch naming and PR validation.

---

## ⏱️ Estimated Time

- **Step 1**: Open Settings - 1 min
- **Step 2**: Set default branch - 2 min
- **Step 3**: Protect main - 8-10 min
- **Step 4**: Protect dev - 8-10 min
- **Verification**: 2-3 min

**Total**: ~20 minutes

---

## 📞 Need Help?

If you get stuck:

1. Check the detailed guide: `.github/BRANCH_PROTECTION_CONFIG.md`
2. GitHub Docs: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches
3. Ask me any questions!

---

**Ready?** Start with Step 1! 🚀
