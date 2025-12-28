---
name: code-review-assistant
description: |
  Systematic code review checklist and pre-commit quality gates for PRs.
  Use when: reviewing pull requests, checking code quality, before committing code.
  Keywords: review, PR, pull request, checklist, quality, commit, 審查, 檢查, 簽入.
---

# Code Review Assistant

This skill provides systematic checklists for code review and pre-commit verification.

## Quick Reference

### Comment Prefixes

| Prefix | Meaning | Action Required |
|--------|---------|------------------|
| **❗ BLOCKING** | Must fix before merge | 🔴 Required |
| **⚠️ IMPORTANT** | Should fix, but not blocking | 🟡 Recommended |
| **💡 SUGGESTION** | Nice-to-have improvement | 🟢 Optional |
| **❓ QUESTION** | Need clarification | 🔵 Discuss |
| **📝 NOTE** | Informational, no action | ⚪ Informational |

### Review Checklist Categories

1. **Functionality** - Does it work?
2. **Design** - Right architecture?
3. **Quality** - Clean code?
4. **Readability** - Easy to understand?
5. **Tests** - Adequate coverage?
6. **Security** - No vulnerabilities?
7. **Performance** - Efficient?
8. **Errors** - Properly handled?
9. **Docs** - Updated?
10. **Dependencies** - Necessary?

### Pre-Commit Checklist

- [ ] Build succeeds (zero errors, zero warnings)
- [ ] All tests pass
- [ ] Code follows project standards
- [ ] No security vulnerabilities
- [ ] Documentation updated
- [ ] Branch synced with target

## Detailed Guidelines

For complete standards, see:
- [Review Checklist](./review-checklist.md)
- [Pre-Commit Checklist](./checkin-checklist.md)

## Example Review Comments

```markdown
❗ BLOCKING: Potential SQL injection vulnerability here.
Please use parameterized queries instead of string concatenation.

⚠️ IMPORTANT: This method is doing too much (120 lines).
Consider extracting validation logic to a separate method.

💡 SUGGESTION: Consider using a Map here instead of an array for O(1) lookup.

❓ QUESTION: Why are we using setTimeout here instead of async/await?

📝 NOTE: This is a clever solution! Nice use of reduce here.
```

## Core Principles

1. **Be Respectful** - Review code, not the person
2. **Be Thorough** - Check functionality, not just syntax
3. **Be Timely** - Review within 24 hours
4. **Be Clear** - Explain WHY, not just WHAT

---

## Configuration Detection

This skill supports project-specific configuration.

### Detection Order

1. Check `CONTRIBUTING.md` for "Disabled Skills" section
   - If this skill is listed, it is disabled for this project
2. Check `CONTRIBUTING.md` for "Code Review Language" section
3. If not found, **default to English**

### First-Time Setup

If no configuration found and context is unclear:

1. Ask the user: "This project hasn't configured code review language. Which option would you like? (English / 中文)"
2. After user selection, suggest documenting in `CONTRIBUTING.md`:

```markdown
## Code Review Language

This project uses **[chosen option]** for code review comments.
<!-- Options: English | 中文 -->
```

### Configuration Example

In project's `CONTRIBUTING.md`:

```markdown
## Code Review Language

This project uses **English** for code review comments.
<!-- Options: English | 中文 -->

### Comment Prefixes
BLOCKING, IMPORTANT, SUGGESTION, QUESTION, NOTE
```

---

**License**: CC BY 4.0 | **Source**: [universal-dev-standards](https://github.com/AsiaOstrich/universal-dev-standards)
