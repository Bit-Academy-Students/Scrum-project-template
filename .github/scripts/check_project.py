#!/usr/bin/env python3
"""Flag incomplete Scrum stories in an organisation GitHub Project."""

import datetime as dt
import json
import os
import subprocess
import sys

OWNER = os.environ["PROJECT_OWNER"]
PROJECT_NUMBER = int(os.environ["PROJECT_NUMBER"])
BACKLOG_STATUS = os.environ.get("BACKLOG_STATUS", "Backlog")
DONE_STATUS = os.environ.get("DONE_STATUS", "Done")
SPRINT_STATUSES = {
    value.strip() for value in os.environ.get(
        "SPRINT_STATUSES", "Sprint (To do),In progress,In review"
    ).split(",")
}

QUERY = """
query($owner: String!, $number: Int!) {
  organization(login: $owner) {
    projectV2(number: $number) {
      items(first: 100) {
        nodes {
          id
          type
          content {
            ... on Issue {
              number
              body
              repository { nameWithOwner }
              assignees(first: 1) { totalCount }
            }
          }
          fieldValues(first: 30) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue { name field { name } }
              ... on ProjectV2ItemFieldNumberValue { number field { name } }
              ... on ProjectV2ItemFieldIterationValue {
                title
                startDate
                duration
                field { name }
              }
            }
          }
        }
      }
    }
  }
}
"""

REQUIRED_SECTIONS = (
    "### User story",
    "### Acceptatiecriteria",
    "### Testplan",
    "### Ontwerp / UML-diagrammen",
)


def run(*args, input_text=None):
    return subprocess.run(
        args,
        input=input_text,
        check=True,
        text=True,
        capture_output=True,
    ).stdout


def project_items():
    result = run(
        "gh", "api", "graphql",
        "-f", f"query={QUERY}",
        "-F", f"owner={OWNER}",
        "-F", f"number={PROJECT_NUMBER}",
    )
    data = json.loads(result)
    project = data.get("data", {}).get("organization", {}).get("projectV2")
    if not project:
        sys.exit(f"Project {OWNER}/{PROJECT_NUMBER} could not be read.")
    return project["items"]["nodes"]


def values(item):
    result = {}
    for value in item["fieldValues"]["nodes"]:
        field = value.get("field") or {}
        name = field.get("name")
        if not name:
            continue
        if "number" in value:
            result[name] = value["number"]
        elif "title" in value:
            result[name] = value
        elif "name" in value:
            result[name] = value["name"]
    return result


def add_label(repo, issue, label, color, description):
    subprocess.run(
        ["gh", "label", "create", label, "--repo", repo, "--color", color, "--description", description, "--force"],
        check=False,
        text=True,
        capture_output=True,
    )
    subprocess.run(
        ["gh", "issue", "edit", str(issue), "--repo", repo, "--add-label", label],
        check=False,
        text=True,
        capture_output=True,
    )


def remove_label(repo, issue, label):
    subprocess.run(
        ["gh", "issue", "edit", str(issue), "--repo", repo, "--remove-label", label],
        check=False,
        text=True,
        capture_output=True,
    )


def iteration_has_ended(iteration):
    if not iteration or not iteration.get("startDate") or not iteration.get("duration"):
        return False
    start = dt.date.fromisoformat(iteration["startDate"])
    end = start + dt.timedelta(days=iteration["duration"])
    return end < dt.date.today()


def main():
    for item in project_items():
        content = item.get("content")
        if item.get("type") != "ISSUE" or not content:
            continue

        fields = values(item)
        status = fields.get("Status")
        repo = content["repository"]["nameWithOwner"]
        issue = content["number"]
        body = content.get("body") or ""

        backlog_problems = []
        if status == BACKLOG_STATUS:
            backlog_problems.extend(
                f"missing section: {section[4:]}"
                for section in REQUIRED_SECTIONS
                if section not in body
            )
            if not fields.get("Priority"):
                backlog_problems.append("missing Priority")
            if fields.get("Points") is None:
                backlog_problems.append("missing Points")

        if backlog_problems:
            add_label(
                repo, issue, "needs-refinement", "d93f0b",
                "Story is incomplete for the Scrum backlog.",
            )
            print(f"#{issue}: needs refinement ({'; '.join(backlog_problems)})")
        else:
            remove_label(repo, issue, "needs-refinement")

        sprint_problems = []
        if status in SPRINT_STATUSES and content["assignees"]["totalCount"] != 1:
            sprint_problems.append("story must have exactly one assignee")
        if status != DONE_STATUS and iteration_has_ended(fields.get("Iteration")):
            sprint_problems.append("iteration has ended; move, split, or finish the story")

        if sprint_problems:
            add_label(
                repo, issue, "needs-sprint-attention", "fbca04",
                "Story needs a sprint-planning decision.",
            )
            print(f"#{issue}: needs sprint attention ({'; '.join(sprint_problems)})")
        else:
            remove_label(repo, issue, "needs-sprint-attention")


if __name__ == "__main__":
    main()