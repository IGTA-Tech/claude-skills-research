# .github/CLAUDE.md

This file provides guidance for working with GitHub workflows and automation in this repository.

---

## 🚨 MANDATORY WORKFLOW REQUIREMENT

**CRITICAL**: All work on this project MUST follow this workflow. **NO EXCEPTIONS.**

### Required Process for Every User Request

1. **PLAN MODE FIRST**
   - Use plan mode to create a detailed implementation plan
   - Break down the work into clear, actionable steps
   - **KEEP PLANS SMALL: 5-10 tasks maximum**
   - Estimate effort and identify potential challenges

2. **GET USER APPROVAL**
   - Present the plan to the user
   - Wait for explicit approval before proceeding
   - Address any questions or concerns

3. **CREATE GITHUB ISSUE**
   - Create a GitHub issue with the `plan` label
   - Include the approved plan in the issue body
   - Use markdown checkboxes for tasks: `- [ ] Task name`
   - **MAXIMUM 5-10 TASKS** - The plan-to-issues automation creates one issue per task
   - **For large initiatives**: Create multiple small plan issues, NOT one giant plan

4. **AUTOMATION CREATES SUBTASKS**
   - GitHub workflow creates individual issues for each task
   - All subtasks are linked to the parent issue
   - All added to project board for tracking
   - **WARNING**: 40+ tasks = API rate limits and issue spam

5. **START IMPLEMENTATION**
   - Begin work on subtasks in priority order
   - Update issue status as you progress
   - Reference issue numbers in commits

### Why This Matters

- ✅ **Proper tracking**: Every task is tracked in GitHub issues and project board
- ✅ **Clear planning**: Prevents scope creep and ensures thoughtful approach
- ✅ **Team visibility**: Everyone can see what's being worked on
- ✅ **Audit trail**: Complete history of decisions and implementation
- ✅ **Automation leverage**: Uses the excellent GitHub automation built into this repo

### Example Workflows

**✅ CORRECT - Small Plan (5 tasks)**:
```
User: "Add a new skill for data visualization"

1. Enter plan mode
2. Create plan with 5 tasks:
   - Research data visualization libraries
   - Design SKILL.md structure
   - Implement Python visualization classes
   - Create sample data and HOW_TO_USE.md
   - Test with real data
3. Present plan to user, get approval
4. Create GitHub issue with 'plan' label containing 5 tasks
5. Automation creates 5 subtask issues
6. Begin implementation
```

**❌ WRONG - Too Many Tasks**:
```
User: "Create comprehensive Wiki documentation"

DON'T DO THIS:
- Create issue with 40+ tasks in checkboxes
- Results in 40+ GitHub issues created
- Hits API rate limits
- Creates issue spam

DO THIS INSTEAD:
- Break into 3-4 small plan issues:
  - Plan #1: Wiki Foundation (5 tasks)
  - Plan #2: Core Wiki Pages (6 tasks)
  - Plan #3: Advanced Documentation (5 tasks)
```

**GOLDEN RULE: 5-10 TASKS MAXIMUM PER PLAN ISSUE**

---

## 📋 Task Hierarchy (Plan → Task → Subtask)

### Three-Level Structure

```
PLAN ISSUE (#100)                      - Epic or feature
  ├─ TASK #101 (5-10 tasks)           - Major work item
  │   ├─ SUBTASK #103 (0-5 subtasks)  - Atomic work
  │   ├─ SUBTASK #104
  │   └─ SUBTASK #105
  ├─ TASK #102
  │   ├─ SUBTASK #106
  │   └─ SUBTASK #107
  └─ TASK #108
```

### Level 1: PLAN Issues
- **Purpose**: High-level feature or epic
- **Task Count**: 5-10 tasks (enforced by plan-validator workflow)
- **Labels**: `plan`, `plan-validated`
- **Created**: Manually by team
- **Format**:
  ```markdown
  ## Goal
  [What we're building and why]

  ## Tasks
  - [ ] Task 1: Clear, actionable description
  - [ ] Task 2: Clear, actionable description
  - [ ] Task 3-10: ...

  ## Acceptance Criteria
  - [ ] Criterion 1
  - [ ] Criterion 2
  ```

### Level 2: TASK Issues
- **Purpose**: Major work item (can be completed independently)
- **Title**: "Task: [description]" (auto-generated)
- **Labels**: `task`, `plan-item`, `skip-triage`
- **Created**: Automatically by plan-to-tasks workflow
- **Parent**: Always linked to parent PLAN
- **Subtasks**: Optional (0-5 subtasks, triggered by `needs-subtasks` label)
- **Scope**: Focused piece of work (1-3 days)

### Level 3: SUBTASK Issues
- **Purpose**: Atomic work unit (smallest unit)
- **Title**: "Subtask: [description]" (auto-generated)
- **Labels**: `subtask`, `skip-triage`
- **Created**: Automatically by task-to-subtasks workflow
- **Parent**: Linked to parent TASK and grandparent PLAN
- **Scope**: Single, focused piece of work (1-3 hours)
- **Maximum**: 5 subtasks per task (enforced)

### Workflow States & Labels

**Triage Control**:
- `skip-triage` - Skips automatic classification (removed when ready)
- `needs-subtasks` - Triggers subtask creation (on TASK issues only)

**Status Tracking** (synced with project board):
- `status: triage` - Needs classification
- `status: backlog` - Planned but not ready
- `status: ready` - Ready to start
- `status: in-progress` - Actively being worked on
- `status: in-review` - Under review
- `status: done` - Completed (auto-applied when issue closed)

### Smart Bidirectional Synchronization

**Workflow**: `.github/workflows/smart-sync.yml`

The smart-sync workflow replaces the old issue-to-project-sync and project-to-issue-sync workflows with a single, intelligent system that prevents sync loops and respects rate limits.

**Key Features**:
- ✅ **10-second debouncing**: Prevents rapid back-and-forth updates
- ✅ **Circuit breaker**: Checks rate limits before executing (requires 50+ remaining)
- ✅ **Direction detection**: Automatically determines sync direction based on event source
- ✅ **Silent operation**: No notification spam (updates without comments)
- ✅ **Loop prevention**: One-way sync logic prevents ping-pong loops

**How It Works**:

1. **Event Triggers**:
   - Issue labeled/closed/reopened → Syncs Issue → Project Board
   - Project board status changed → Syncs Project Board → Issue

2. **Safety Checks**:
   - Rate limit check (circuit breaker)
   - 10-second debounce delay
   - Concurrency control (cancel in-progress runs)

3. **Sync Operations**:

   **Issue → Project Board**:
   - Adds issue to project if not present
   - Maps issue status labels to project board columns
   - Updates project board status field
   - Closes/reopens based on issue state

   **Project Board → Issue**:
   - Removes old status labels
   - Adds new status label based on project board column
   - Closes issue if moved to "Done"
   - Reopens issue if moved from "Done"

4. **Status Mapping**:
   ```
   Issue Label          ↔  Project Board Column
   ─────────────────────────────────────────────
   status: triage       ↔  To triage
   status: backlog      ↔  Backlog
   status: ready        ↔  Ready
   status: in-progress  ↔  In Progress
   status: in-review    ↔  In Review
   status: done         ↔  Done
   (closed state)       ↔  Done
   ```

**Best Practices**:
- ✅ DO: Change status on project board OR issue (not both at once)
- ✅ DO: Wait 10 seconds between rapid status changes
- ✅ DO: Use status labels for tracking (they sync automatically)
- ❌ DON'T: Manually update both issue and project board (creates duplicate syncs)
- ❌ DON'T: Make rapid status changes (triggers rate limit protection)

**Troubleshooting**:
- If sync appears stuck: Check rate limits with `gh api rate_limit`
- If status out of sync: Manually trigger by re-labeling or moving on board
- If getting rate limit warnings: Wait for cooldown (syncs will resume automatically)

### Monitoring & Automation

**Three Powerful Automation Workflows**:

#### 1. Workflow Health Monitor (`.github/workflows/workflow-health.yml`)

Automated system health monitoring every 6 hours.

**What It Monitors**:
- ✅ GitHub API rate limits (REST & GraphQL)
- ✅ Workflow success rates (last 24 hours)
- ✅ Task hierarchy statistics (Plans, Tasks, Subtasks)

**Alerting**:
- Creates health alert issues when problems detected
- **Critical**: Rate limits <20% OR success rate <70%
- **Warning**: Rate limits <40% OR success rate <85%

**Manual Trigger**: Go to Actions → Workflow Health Monitor → Run workflow

**What You Get**:
```
📊 Rate Limits: REST 85% | GraphQL 82%
📈 Workflows: 47 runs, 94% success rate
🏗️ Hierarchy: 3 plans (2 open), 18 tasks (12 open), 23 subtasks (15 open)
```

#### 2. Plan Auto-Close (`.github/workflows/plan-auto-close.yml`)

Automatically closes plan issues when all tasks are completed.

**How It Works**:
1. Triggers when any TASK issue is closed
2. Checks if task belongs to a PLAN
3. Counts remaining open tasks for that plan
4. If all tasks done → automatically closes plan with celebration comment
5. Posts progress updates at 25%, 50%, 75% milestones

**Benefits**:
- ✅ No manual plan closure needed
- ✅ Automatic completion tracking
- ✅ Progress milestone notifications
- ✅ Clear completion summaries

**Example Comment**:
```markdown
## ✅ Plan Completed

All 8 tasks have been completed! This plan is now being automatically closed.

📊 Completion Summary
- Total Tasks: 8
- Completed: 8
- Success Rate: 100%

🎉 What's Next?
- Review completed work
- Archive or reference for future projects
```

#### 3. Hierarchy Dashboard (`.github/workflows/hierarchy-dashboard.yml`)

Generates visual Plan→Task→Subtask tree in [HIERARCHY.md](../HIERARCHY.md).

**Updates**:
- Every 12 hours (scheduled)
- When issues are created, closed, or labeled
- Manual trigger via workflow dispatch

**What It Shows**:
- Overview table with completion percentages
- Visual tree of all active plans with tasks and subtasks
- Progress bars for each plan
- Recently completed plans (last 10)

**Example Tree**:
```
📋 Plan #55: Create Wiki Documentation
Progress: 5/8 tasks (62%)

├─ ✅ #58: Create Wiki Home page
│  ├─ ✅ #60: Design page structure
│  └─ ✅ #61: Write content
├─ 🔲 #59: Add skill documentation
├─ ✅ #62: Create navigation
```

**Quick Links**: [View Current Dashboard](../HIERARCHY.md)

### How to Use the Hierarchy

**Creating a Plan**:
1. Create issue with `plan` label
2. Add 5-10 tasks in checklist format
3. Validation workflow checks count & rate limits
4. If valid, adds `plan-validated` label
5. Plan-to-tasks workflow creates TASK issues automatically

**Breaking Down a Task**:
1. Open a TASK issue
2. Add `needs-subtasks` label
3. Create checklist in task body (max 5 items)
4. Task-to-subtasks workflow creates SUBTASK issues automatically

**Working on Tasks/Subtasks**:
1. Remove `skip-triage` label when ready for classification
2. Auto-triage workflow classifies and prioritizes
3. Move to "In Progress" on project board when starting work
4. Close issue when done (auto-syncs to "Done" on board)

### Best Practices

**Plan Issues**:
- ✅ DO: Keep to 5-10 tasks
- ✅ DO: Make tasks independent when possible
- ✅ DO: Write clear, actionable task descriptions
- ❌ DON'T: Create 20+ task plans (split into multiple plans)
- ❌ DON'T: Make tasks too vague or too detailed

**Task Issues**:
- ✅ DO: Add `needs-subtasks` if task is complex
- ✅ DO: Keep subtask count to 5 or fewer
- ✅ DO: Link to parent PLAN in description
- ❌ DON'T: Create subtasks manually (use automation)
- ❌ DON'T: Skip the `skip-triage` label removal step

**Subtask Issues**:
- ✅ DO: Keep scope small and focused (1-3 hours)
- ✅ DO: Link to both parent TASK and grandparent PLAN
- ✅ DO: Close promptly when completed
- ❌ DON'T: Create sub-subtasks (3 levels max)
- ❌ DON'T: Make subtasks too granular

### Examples

**Good Plan (7 tasks)**:
```markdown
## Goal
Implement user authentication system

## Tasks
- [ ] Design login UI components
- [ ] Implement JWT authentication backend
- [ ] Add password reset flow
- [ ] Create user profile management
- [ ] Implement session handling
- [ ] Add OAuth integration (Google, GitHub)
- [ ] Write authentication tests

## Acceptance Criteria
- [ ] Users can log in with email/password
- [ ] JWT tokens expire after 24h
- [ ] OAuth integration works
- [ ] 90%+ test coverage
```

**Good Task with Subtasks** (Task #101):
```markdown
Title: Task: Design login UI components
Labels: task, plan-item, needs-subtasks

## Description
Create all UI components needed for user authentication

## Subtasks
- [ ] Create LoginForm component
- [ ] Create SignupForm component
- [ ] Add form validation
- [ ] Design password strength indicator
- [ ] Create forgot password UI
```

This creates 5 subtask issues automatically.
