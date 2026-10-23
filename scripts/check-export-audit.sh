#!/usr/bin/env bash
set -Eeuo pipefail

for command in bash shfmt shellcheck python3; do
  command -v "$command" >/dev/null 2>&1 || {
    echo "Missing command: $command"
    exit 1
  }
done

bash -n scripts/export-audit.sh
shfmt -d scripts/export-audit.sh
shellcheck --shell=bash --severity=warning scripts/export-audit.sh

jq --exit-status '
  [.[][]] | unique_by(.id) | sort_by(.number) | map(.number) == [1, 2, 3]
' scripts/fixtures/paginated-issues.json >/dev/null

check_issue_comment_fixture() {
  jq --exit-status --slurpfile pull_requests scripts/fixtures/pull-requests.json '
  ($pull_requests[0] | map(.number) | unique) as $pull_request_numbers
  | [.[][]
      | (.issue_url | split("/") | last | tonumber) as $issue_number
      | select($pull_request_numbers | index($issue_number) | not)
      | . + { issue_number: $issue_number }
    ]
  | unique_by(.id)
  | sort_by(.issue_number, .id)
  | map(.issue_number) == [1, 3]
' "$1" >/dev/null
}

check_issue_comment_fixture scripts/fixtures/paginated-issue-comments.json

# The fixture contract expects issues 1 and 3, so empty input must fail with
# jq's false-result status rather than silently pass or fail from a parse error.
if check_issue_comment_fixture scripts/fixtures/empty-issue-comments.json; then
  echo "ERROR: Empty issue-comment fixture unexpectedly passed."
  exit 1
else
  assertion_status=$?
  if [[ "$assertion_status" -ne 1 ]]; then
    echo "ERROR: Expected jq false-result status 1, got $assertion_status."
    exit 1
  fi
fi

# Preserve distinct ID-less events (including equal timestamps), scope IDs to
# issue/event kind, and collapse only identical observed payloads without IDs.
jq -L scripts/lib --exit-status '
  include "timeline";
  [.[][]] | timeline_unique
  | length == 8
    and timeline_valid
    and ([.[] | select(.event == "cross-referenced") | .source.issue.id] | sort == [100, 100, 200])
    and ([.[] | select(.event == "referenced") | .commit_id] | sort == ["abc", "def"])
    and ([.[] | select(.id == 10)] | length == 3)
' scripts/fixtures/paginated-timeline.json >/dev/null

jq -L scripts/lib --exit-status '
  include "timeline";
  [.[][]] | timeline_unique as $events
  | (($events + [$events[0]]) | timeline_valid | not)
    and ([{"id": 1}] | timeline_valid | not)
    and ({} | timeline_valid | not)
' scripts/fixtures/paginated-timeline.json >/dev/null

# Disposable Git repositories exercise committed-source and failure boundaries.
python3 -m unittest discover -s scripts -p test_audit_source.py

# Synthetic REST responses exercise PR evidence without a live export.
python3 -m unittest discover -s scripts -p test_audit_pr_evidence.py

# Synthetic typed Project and nested GraphQL pagination fixtures.
python3 -m unittest discover -s scripts -p test_audit_project.py

# Aggregate coverage, hashes, compatibility and failure-safe finalization.
python3 -m unittest discover -s scripts -p test_audit_records.py
python3 -m unittest discover -s scripts -p test_audit_package.py
