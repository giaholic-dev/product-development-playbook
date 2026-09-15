#!/usr/bin/env bash
set -Eeuo pipefail

EXPORT_SCHEMA_VERSION="1.0.0"
TOOL_VERSION="1.0.0"

print_header() {
  echo "======================================"
  echo " GitHub Audit Export"
  echo "======================================"
  echo
}

require() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing command: $1"
    exit 1
  }
}

check_requirements() {
  require git
  require gh
  require jq
  require zip
  require unzip
}

check_repository() {
  git rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
    echo "Current directory is not a Git repository."
    exit 1
  }
}

parse_remote() {
  local remote="$1"

  if [[ "$remote" =~ ^git@github\.com:([^/[:space:]]+)/([^/[:space:]]+)(\.git)?$ ]]; then
    OWNER="${BASH_REMATCH[1]}"
    REPOSITORY="${BASH_REMATCH[2]%.git}"
  elif [[ "$remote" =~ ^ssh://git@github\.com/([^/[:space:]]+)/([^/[:space:]]+)(\.git)?$ ]]; then
    OWNER="${BASH_REMATCH[1]}"
    REPOSITORY="${BASH_REMATCH[2]%.git}"
  elif [[ "$remote" =~ ^https://github\.com/([^/[:space:]]+)/([^/[:space:]]+)(\.git)?$ ]]; then
    OWNER="${BASH_REMATCH[1]}"
    REPOSITORY="${BASH_REMATCH[2]%.git}"
  else
    echo "Origin must be a supported GitHub SSH or HTTPS remote."
    exit 1
  fi

  [[ -n "$OWNER" && -n "$REPOSITORY" && "$REPOSITORY" != *"/"* ]] || {
    echo "Origin does not identify a GitHub owner and repository."
    exit 1
  }

  REMOTE_IDENTITY="github.com/$OWNER/$REPOSITORY"
}

load_repository() {
  ROOT="$(git rev-parse --show-toplevel)"
  cd "$ROOT"

  parse_remote "$(git remote get-url origin)"
  BRANCH="$(git symbolic-ref --quiet --short HEAD || true)"
  COMMIT="$(git rev-parse HEAD)"
  SHORT_COMMIT="$(git rev-parse --short HEAD)"

  if [[ -n "$BRANCH" ]]; then
    SELECTED_REF="$BRANCH"
    DETACHED_HEAD=false
  else
    SELECTED_REF="$COMMIT"
    DETACHED_HEAD=true
  fi

  DEFAULT_BRANCH="$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null || true)"
  DEFAULT_BRANCH="${DEFAULT_BRANCH#origin/}"
  DIRTY=false
  [[ -n "$(git status --porcelain)" ]] && DIRTY=true

  TIMESTAMP="$(date -u +"%Y-%m-%dT%H-%M-%SZ")"
  EXPORT_ROOT="audit"
  EXPORT_DIR="$EXPORT_ROOT/exports/$TIMESTAMP"
  ZIP_FILE="$EXPORT_ROOT/${REPOSITORY}-audit-$TIMESTAMP.zip"

  [[ ! -e "$EXPORT_DIR" && ! -e "$ZIP_FILE" ]] || {
    echo "Refusing to overwrite an existing audit export for $TIMESTAMP."
    exit 1
  }
}

create_directories() {
  mkdir -p "$EXPORT_DIR/repository" "$EXPORT_DIR/github" "$EXPORT_DIR/git"
}

export_repository() {
  cp README.md "$EXPORT_DIR/repository/" 2>/dev/null || true

  mkdir -p "$EXPORT_DIR/repository/config"
  for path in .editorconfig .gitignore .shellcheckrc .gitattributes CODEOWNERS Makefile; do
    [[ -f "$path" ]] && cp "$path" "$EXPORT_DIR/repository/config/"
  done
  [[ -d docs ]] && cp -R docs "$EXPORT_DIR/repository/"
  [[ -d templates ]] && cp -R templates "$EXPORT_DIR/repository/"
  [[ -d examples ]] && cp -R examples "$EXPORT_DIR/repository/"
  find . -path "./.git" -prune -o -path "./audit" -prune -o -type f -print |
    sort > "$EXPORT_DIR/repository/repository-tree.txt"
}

export_branches() {
  git for-each-ref --sort=refname --format='%(refname:short) %(objectname) %(upstream:short)' refs/heads refs/remotes > "$EXPORT_DIR/git/branches.txt"
}

export_tags() {
  git for-each-ref --sort=refname --format='%(refname:short) %(objectname) %(objecttype)' refs/tags > "$EXPORT_DIR/git/tags.txt"
}

export_recent_commits() {
  git log -n 100 --date=iso-strict --format='%H%x09%P%x09%an%x09%ae%x09%ad%x09%s' > "$EXPORT_DIR/git/recent-commits.tsv"
}

export_repository_status() {
  git status --porcelain=v1 --branch > "$EXPORT_DIR/git/status.txt"
}

temporary_json() {
  mktemp "$1.XXXXXX"
}

publish_json() {
  local temporary="$1"
  local target="$2"
  local expected_type="$3"

  if ! jq --exit-status --arg expected_type "$expected_type" '
    if type != $expected_type then
      error("expected " + $expected_type)
    elif $expected_type == "object" and
      ((has("schema_version") and has("repository") and has("generated_at")) | not) then
      error("missing required manifest metadata")
    else
      .
    end
  ' "$temporary" >/dev/null; then
    rm -f "$temporary"
    echo "ERROR: Invalid JSON output: $target"
    exit 1
  fi

  mv "$temporary" "$target"
}

export_issues() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/issues.json")"

  gh api --paginate --slurp "repos/$OWNER/$REPOSITORY/issues?state=all&per_page=100" |
    jq '[.[][] | select(.pull_request | not)] | unique_by(.id) | sort_by(.number)' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/issues.json" array
}

export_issue_comments() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/issue-comments.json")"

  gh api --paginate --slurp "repos/$OWNER/$REPOSITORY/issues/comments?per_page=100" |
    jq --slurpfile pull_requests "$EXPORT_DIR/github/pull-requests.json" '
      ($pull_requests[0] | map(.number) | unique) as $pull_request_numbers
      | [.[][]
          | (.issue_url | split("/") | last | tonumber) as $issue_number
          | select($pull_request_numbers | index($issue_number) | not)
          | . + { issue_number: $issue_number }
        ]
      | unique_by(.id)
      | sort_by(.issue_number, .id)
    ' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/issue-comments.json" array
}

export_prs() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/pull-requests.json")"

  gh api --paginate --slurp "repos/$OWNER/$REPOSITORY/pulls?state=all&per_page=100" |
    jq '[.[][]] | unique_by(.id) | sort_by(.number)' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/pull-requests.json" array
}

export_labels() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/labels.json")"

  gh api --paginate --slurp "repos/$OWNER/$REPOSITORY/labels?per_page=100" |
    jq '[.[][]] | unique_by(.id) | sort_by(.name)' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/labels.json" array
}

export_milestones() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/milestones.json")"

  gh api --paginate --slurp "repos/$OWNER/$REPOSITORY/milestones?state=all&per_page=100" |
    jq '[.[][]] | unique_by(.id) | sort_by(.number)' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/milestones.json" array
}

export_releases() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/releases.json")"

  gh api --paginate --slurp "repos/$OWNER/$REPOSITORY/releases?per_page=100" |
    jq '[.[][]] | unique_by(.id) | sort_by(.id)' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/releases.json" array
}

collection_count() {
  jq --exit-status 'if type == "array" then length else error("expected array") end' "$1"
}

create_manifest() {
  local branch_json=null
  local default_branch_json=null

  [[ -n "$BRANCH" ]] && branch_json="$(jq -n --arg value "$BRANCH" '$value')"
  [[ -n "$DEFAULT_BRANCH" ]] && default_branch_json="$(jq -n --arg value "$DEFAULT_BRANCH" '$value')"

  jq -n \
    --arg schema_version "$EXPORT_SCHEMA_VERSION" \
    --arg tool_version "$TOOL_VERSION" \
    --arg owner "$OWNER" \
    --arg repository "$REPOSITORY" \
    --arg remote_identity "$REMOTE_IDENTITY" \
    --arg selected_ref "$SELECTED_REF" \
    --arg commit "$COMMIT" \
    --arg generated_at "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
    --argjson branch "$branch_json" \
    --argjson default_branch "$default_branch_json" \
    --argjson detached_head "$DETACHED_HEAD" \
    --argjson dirty "$DIRTY" \
    --argjson issues "$(collection_count "$EXPORT_DIR/github/issues.json")" \
    --argjson issue_comments "$(collection_count "$EXPORT_DIR/github/issue-comments.json")" \
    --argjson pull_requests "$(collection_count "$EXPORT_DIR/github/pull-requests.json")" \
    --argjson labels "$(collection_count "$EXPORT_DIR/github/labels.json")" \
    --argjson milestones "$(collection_count "$EXPORT_DIR/github/milestones.json")" \
    --argjson releases "$(collection_count "$EXPORT_DIR/github/releases.json")" \
    '{
      schema_version: $schema_version,
      tool_version: $tool_version,
      repository: {
        owner: $owner,
        name: $repository,
        remote_identity: $remote_identity,
        selected_ref: $selected_ref,
        branch: $branch,
        default_branch: $default_branch,
        detached_head: $detached_head,
        commit: $commit,
        dirty: $dirty
      },
      generated_at: $generated_at,
      collection_counts: {
        issues: $issues,
        issue_comments: $issue_comments,
        pull_requests: $pull_requests,
        labels: $labels,
        milestones: $milestones,
        releases: $releases
      },
      collection_pagination: {
        issues: true,
        issue_comments: true,
        pull_requests: true,
        labels: true,
        milestones: true,
        releases: true
      }
    }' > "$(temporary_json "$EXPORT_DIR/manifest.json")"
  publish_json "$EXPORT_DIR/manifest.json".* "$EXPORT_DIR/manifest.json" object
}

compress() {
  (
    cd "$EXPORT_ROOT"
    zip -qr "$(basename "$ZIP_FILE")" "exports/$TIMESTAMP"
  )

  [[ -s "$ZIP_FILE" ]] || {
    echo
    echo "ERROR: Failed to create a non-empty zip archive."
    exit 1
  }

  unzip -tq "$ZIP_FILE" >/dev/null || {
    echo "ERROR: Audit package integrity check failed."
    exit 1
  }

  local archive_entry
  for archive_entry in \
    "exports/$TIMESTAMP/manifest.json" \
    "exports/$TIMESTAMP/github/issues.json" \
    "exports/$TIMESTAMP/github/issue-comments.json" \
    "exports/$TIMESTAMP/github/pull-requests.json" \
    "exports/$TIMESTAMP/github/labels.json" \
    "exports/$TIMESTAMP/github/milestones.json" \
    "exports/$TIMESTAMP/github/releases.json"; do
    unzip -Z1 "$ZIP_FILE" | grep -Fx "$archive_entry" >/dev/null || {
      echo "ERROR: Audit package is missing $archive_entry."
      exit 1
    }
  done
}

summary() {
  echo
  echo "Repository : $OWNER/$REPOSITORY"
  echo "Branch     : ${BRANCH:-detached HEAD}"
  echo "Commit     : $SHORT_COMMIT"
  echo
  echo "Audit package:"
  echo "  $ZIP_FILE"
}

main() {
  print_header
  check_requirements
  check_repository
  load_repository
  create_directories
  export_repository
  export_branches
  export_tags
  export_recent_commits
  export_repository_status
  export_issues
  export_prs
  export_issue_comments
  export_labels
  export_milestones
  export_releases
  create_manifest
  compress
  summary
}

main
