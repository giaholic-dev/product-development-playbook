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
