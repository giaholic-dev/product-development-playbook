#!/usr/bin/env bash
set -Eeuo pipefail

for command in bash shfmt shellcheck; do
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

jq --slurpfile pull_requests scripts/fixtures/pull-requests.json '
  ($pull_requests[0] | map(.number) | unique) as $pull_request_numbers
  | [.[][]
      | (.issue_url | split("/") | last | tonumber) as $issue_number
      | select($pull_request_numbers | index($issue_number) | not)
      | . + { issue_number: $issue_number }
    ]
  | unique_by(.id)
  | sort_by(.issue_number, .id)
  | map(.issue_number) == [1, 3]
' scripts/fixtures/paginated-issue-comments.json >/dev/null
