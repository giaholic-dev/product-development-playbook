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
shellcheck --shell=bash scripts/export-audit.sh
