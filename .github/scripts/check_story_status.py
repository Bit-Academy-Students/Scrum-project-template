import json
import os
import subprocess
import sys

ALLOWED_STATUSES = {
    s.strip()
    for s in os.environ.get("MERGE_STATUSES", "In progress,In review").split(",")
}

QUERY = """
query($owner: String!, $name: String!, $number: Int!) {
  repository(owner: $owner, name: $name) {
    pullRequest(number: $number) {
      closingIssuesReferences(first: 10) {
        nodes {
          number
          state
          issueType { name }
          assignees(first: 5) { totalCount }
          projectItems(first: 20) {
            nodes {
              project { number title closed }
              fieldValueByName(name: "Status") {
                ... on ProjectV2ItemFieldSingleSelectValue { name }
              }
            }
          }
        }
      }
    }
  }
}
"""


def main():
    if not os.environ.get("GH_TOKEN"):
        sys.exit("Missing PROJECT_TOKEN Actions secret (not available for fork or Dependabot PRs).")

    owner, name = os.environ["GITHUB_REPOSITORY"].split("/")
    result = subprocess.run(
        [
            "gh", "api", "graphql",
            "-f", f"query={QUERY}",
            "-F", f"owner={owner}",
            "-F", f"name={name}",
            "-F", f"number={os.environ['PR_NUMBER']}",
        ],
        check=True, text=True, capture_output=True,
    )
    pr = json.loads(result.stdout)["data"]["repository"]["pullRequest"]
    issues = pr["closingIssuesReferences"]["nodes"]

    if len(issues) != 1:
        sys.exit(
            f"The pull request must close exactly one story with 'Closes #<number>', found {len(issues)}."
        )

    issue = issues[0]
    number = issue["number"]
    problems = []

    if (issue.get("issueType") or {}).get("name") != "User Story":
        problems.append("issue type must be 'User Story'")
    if issue["assignees"]["totalCount"] != 1:
        problems.append("story must have exactly one assignee")

    override = os.environ.get("PROJECT_NUMBER", "").strip()
    items = [
        i for i in issue["projectItems"]["nodes"]
        if not i["project"]["closed"]
        and (not override or str(i["project"]["number"]) == override)
    ]
    if len(items) != 1:
        problems.append(f"story must be in exactly one open project, found {len(items)}")
    else:
        status = (items[0].get("fieldValueByName") or {}).get("name")
        if status not in ALLOWED_STATUSES:
            allowed = " or ".join(sorted(ALLOWED_STATUSES))
            problems.append(f"story status is '{status}', expected {allowed}")

    if problems:
        sys.exit(f"Story #{number}: " + "; ".join(problems) + ". Fix it, then re-run this check.")

    print(f"Story #{number} is in status '{status}' and ready to merge.")


if __name__ == "__main__":
    main()
