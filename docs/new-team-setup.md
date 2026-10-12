# New team setup (quick runbook)

Use this checklist each time you create a new student team repository and project.

## Goal

After this setup, the team should have:

- one repo based on this template
- one project board based on the project template
- issue form + PR template active
- branch review flow active on `main`
- automation working (linked branches + project checker)

---

## 1) Create the team repository

1. Open this template repo.
2. Click **Use this template**.
3. Create a **public** repo in `Bit-Academy-Students`.
4. Add students with write access.

> Note: docs/templates/workflows are copied automatically from this template repo.

---

## 2) Create a project from the project template

1. Go to org Projects.
2. Create a new project from the Scrum project template.
3. Name it for the team (for example `Team X - Scrum board`).

---

## 3) Link repo and project

1. Open the new project settings.
2. Link the new team repository to the project.

This link is required for the checker workflow and for issue/project flow.

---

## 4) Configure project workflows & views

In the team project copy:

- Ensure statuses are:
  - `Draft`
  - `Backlog`
  - `Sprint (To do)`
  - `In progress`
  - `In review`
  - `Done`
- Ensure fields include:
  - `Priority` (MoSCoW)
  - `Points`
  - `Iteration`
- Ensure views include:
  - Drafts/refinement
  - Backlog
  - Current sprint
  - Next sprint
  - Roadmap

Enable built-in workflows:

- Item closed → Done
- Pull request merged → Done
- Item reopened → In progress
- Auto-add issues from the linked repo (filter: `is:issue`, default status: Backlog)

---

## 5) Configure repository branch protection/ruleset

For branch `main`, require:

- pull request before merge
- at least 1 approval
- resolved review conversations

Teachers/admins may keep bypass permission.

---

## 6) Secrets and variables

### Required secret

- `PROJECT_TOKEN` (already available via org secret if configured there)

Token must be able to read org projects and (if needed) interact with issues in repos covered by the workflow behavior.

### Variable

- `PROJECT_NUMBER` is optional if the checker auto-detects the linked project.
- If you use manual override mode, set it to the project number.

---

## 7) First validation test (do this once per team)

1. Create a test issue via **User story** form.
2. Confirm it appears in Backlog.
3. Assign the issue:
   - linked branch should be created automatically.
4. Open a PR with `Closes #<issue-number>`.
5. Confirm PR template appears and review approval is required.
6. Run **Check Scrum project** workflow manually once.
7. Confirm missing fields/sections are detected as expected.

---

## 8) What is still manual every new team

- Create repo from template
- Create/copy project
- Link repo to project
- Check project workflows
- Apply/confirm `main` branch ruleset
- Validate once with test issue + PR

Everything else should be template-driven.