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
