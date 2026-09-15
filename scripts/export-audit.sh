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
  FINAL_EXPORT_DIR="$EXPORT_ROOT/exports/$TIMESTAMP"
  STAGING_DIR="$EXPORT_ROOT/.staging/$TIMESTAMP-$"
  EXPORT_DIR="$STAGING_DIR"
  ZIP_FILE="$EXPORT_ROOT/${REPOSITORY}-audit-$TIMESTAMP.zip"
  PROJECT_NUMBER="${GITHUB_PROJECT_NUMBER:-1}"
  EXPORT_DISCUSSIONS="${GITHUB_EXPORT_DISCUSSIONS:-false}"

  [[ ! -e "$FINAL_EXPORT_DIR" && ! -e "$ZIP_FILE" && ! -e "$STAGING_DIR" ]] || {
    echo "Refusing to overwrite an existing audit export for $TIMESTAMP."
    exit 1
  }
}

check_github_access() {
  gh auth status --hostname github.com >/dev/null 2>&1 || {
    echo "GitHub CLI is not authenticated for github.com. Run: gh auth login"
    exit 1
  }

  gh repo view "$OWNER/$REPOSITORY" --json nameWithOwner --jq '.nameWithOwner' >/dev/null 2>&1 || {
    echo "Unable to access GitHub repository: $OWNER/$REPOSITORY"
    exit 1
  }
}

cleanup_staging() {
  if [[ -n "${STAGING_DIR:-}" && -d "$STAGING_DIR" && "$STAGING_DIR" == "$EXPORT_ROOT/.staging/"* ]]; then
    rm -rf "$STAGING_DIR"
  fi
}

publish_export() {
  mkdir -p "$(dirname "$FINAL_EXPORT_DIR")"
  mv "$STAGING_DIR" "$FINAL_EXPORT_DIR"
  EXPORT_DIR="$FINAL_EXPORT_DIR"
  STAGING_DIR=""
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

export_project_items() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/project-items.json")"

  gh api graphql --paginate --slurp \
    -f query='
      query($login: String!, $number: Int!, $endCursor: String) {
        organization(login: $login) {
          projectV2(number: $number) {
            items(first: 100, after: $endCursor) {
              nodes {
                id
                type
                createdAt
                updatedAt
                content {
                  ... on Issue { id number title url }
                  ... on PullRequest { id number title url }
                  ... on DraftIssue { id title }
                }
              }
              pageInfo { hasNextPage endCursor }
            }
          }
        }
      }
    ' \
    -f login="$OWNER" \
    -F number="$PROJECT_NUMBER" |
    jq '
      [.[] | .data.organization.projectV2.items.nodes[]]
      | unique_by(.id)
      | sort_by(.id)
    ' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/project-items.json" array
}

export_project_fields() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/project-fields.json")"

  gh api graphql --paginate --slurp \
    -f query='
      query($login: String!, $number: Int!, $endCursor: String) {
        organization(login: $login) {
          projectV2(number: $number) {
            fields(first: 100, after: $endCursor) {
              nodes {
                ... on ProjectV2FieldCommon { id name dataType }
                ... on ProjectV2SingleSelectField {
                  options { id name color description }
                }
                ... on ProjectV2IterationField {
                  configuration { duration startDay iterations { id title startDate } }
                }
              }
              pageInfo { hasNextPage endCursor }
            }
          }
        }
      }
    ' \
    -f login="$OWNER" \
    -F number="$PROJECT_NUMBER" |
    jq '
      [.[] | .data.organization.projectV2.fields.nodes[]]
      | unique_by(.id)
      | sort_by(.name, .id)
    ' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/project-fields.json" array
}

export_project_views() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/project-views.json")"

  gh api graphql --paginate --slurp \
    -f query='
      query($login: String!, $number: Int!, $endCursor: String) {
        organization(login: $login) {
          projectV2(number: $number) {
            views(first: 100, after: $endCursor) {
              nodes { id number name layout }
              pageInfo { hasNextPage endCursor }
            }
          }
        }
      }
    ' \
    -f login="$OWNER" \
    -F number="$PROJECT_NUMBER" |
    jq '
      [.[] | .data.organization.projectV2.views.nodes[]]
      | unique_by(.id)
      | sort_by(.number)
    ' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/project-views.json" array
}

export_issue_timeline() {
  local temporary
  local timeline_directory
  local issue_number

  temporary="$(temporary_json "$EXPORT_DIR/github/issue-timeline.json")"
  timeline_directory="$(mktemp -d "$EXPORT_DIR/github/timeline.XXXXXX")"

  while IFS= read -r issue_number; do
    gh api --paginate --slurp \
      -H "Accept: application/vnd.github+json" \
      "repos/$OWNER/$REPOSITORY/issues/$issue_number/timeline?per_page=100" |
      jq --argjson issue_number "$issue_number" '
        [.[][] | . + { issue_number: $issue_number }]
        | unique_by(.id)
        | sort_by(.created_at, .id)
      ' > "$timeline_directory/$issue_number.json"
  done < <(jq -r '.[].number' "$EXPORT_DIR/github/issues.json")

  if compgen -G "$timeline_directory/*.json" >/dev/null; then
    jq -s '
      add
      | unique_by(.issue_number, .id)
      | sort_by(.issue_number, .created_at, .id)
    ' "$timeline_directory"/*.json > "$temporary"
  else
    printf '[]\n' > "$temporary"
  fi

  rm -rf "$timeline_directory"
  publish_json "$temporary" "$EXPORT_DIR/github/issue-timeline.json" array
}

export_review_comments() {
  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/review-comments.json")"

  gh api --paginate --slurp \
    "repos/$OWNER/$REPOSITORY/pulls/comments?per_page=100" |
    jq '
      [.[][]
        | (.pull_request_url | split("/") | last | tonumber) as $pull_request_number
        | . + { pull_request_number: $pull_request_number }
      ]
      | unique_by(.id)
      | sort_by(.pull_request_number, .path, .line, .id)
    ' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/review-comments.json" array
}

export_discussions() {
  [[ "$EXPORT_DISCUSSIONS" == "true" ]] || return 0

  local temporary
  temporary="$(temporary_json "$EXPORT_DIR/github/discussions.json")"

  gh api graphql --paginate --slurp \
    -f query='
      query($owner: String!, $repository: String!, $endCursor: String) {
        repository(owner: $owner, name: $repository) {
          discussions(first: 100, after: $endCursor) {
            nodes {
              id
              number
              title
              body
              createdAt
              updatedAt
              url
              category { id name }
              author { login }
            }
            pageInfo { hasNextPage endCursor }
          }
        }
      }
    ' \
    -f owner="$OWNER" \
    -f repository="$REPOSITORY" |
    jq '
      [.[] | .data.repository.discussions.nodes[]]
      | unique_by(.id)
      | sort_by(.number)
    ' > "$temporary"

  publish_json "$temporary" "$EXPORT_DIR/github/discussions.json" array
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
  local manifest_temporary

  [[ -n "$BRANCH" ]] && branch_json="$(jq -n --arg value "$BRANCH" '$value')"
  [[ -n "$DEFAULT_BRANCH" ]] && default_branch_json="$(jq -n --arg value "$DEFAULT_BRANCH" '$value')"
  manifest_temporary="$(temporary_json "$EXPORT_DIR/manifest.json")"

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
    --argjson project_items "$(collection_count "$EXPORT_DIR/github/project-items.json")" \
    --argjson project_fields "$(collection_count "$EXPORT_DIR/github/project-fields.json")" \
    --argjson project_views "$(collection_count "$EXPORT_DIR/github/project-views.json")" \
    --argjson issue_timeline "$(collection_count "$EXPORT_DIR/github/issue-timeline.json")" \
    --argjson review_comments "$(collection_count "$EXPORT_DIR/github/review-comments.json")" \
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
        releases: $releases,
        project_items: $project_items,
        project_fields: $project_fields,
        project_views: $project_views,
        issue_timeline: $issue_timeline,
        review_comments: $review_comments
      },
      collection_pagination: {
        issues: true,
        issue_comments: true,
        pull_requests: true,
        labels: true,
        milestones: true,
        releases: true,
        project_items: true,
        project_fields: true,
        project_views: true,
        issue_timeline: true,
        review_comments: true
      }
    }' > "$manifest_temporary"
  publish_json "$manifest_temporary" "$EXPORT_DIR/manifest.json" object
}

validate_integrity() {
  local collection
  local file
  local declared_count
  local actual_count
  local collections=(
    "issues:issues.json"
    "issue_comments:issue-comments.json"
    "pull_requests:pull-requests.json"
    "labels:labels.json"
    "milestones:milestones.json"
    "releases:releases.json"
    "project_items:project-items.json"
    "project_fields:project-fields.json"
    "project_views:project-views.json"
    "issue_timeline:issue-timeline.json"
    "review_comments:review-comments.json"
  )

  [[ -f "$EXPORT_DIR/manifest.json" ]] || {
    echo "ERROR: Missing audit manifest."
    exit 1
  }

  for collection in "${collections[@]}"; do
    local name="${collection%%:*}"
    file="$EXPORT_DIR/github/${collection#*:}"
    [[ -f "$file" ]] || {
      echo "ERROR: Missing required collection: $file"
      exit 1
    }

    jq --exit-status 'type == "array" and (map(.id) | length == (unique | length))' "$file" >/dev/null || {
      echo "ERROR: Invalid or duplicate records in $file"
      exit 1
    }

    actual_count="$(jq length "$file")"
    declared_count="$(jq --raw-output --arg name "$name" '.collection_counts[$name]' "$EXPORT_DIR/manifest.json")"
    [[ "$actual_count" == "$declared_count" ]] || {
      echo "ERROR: Manifest count mismatch for $name."
      exit 1
    }
  done

  jq --exit-status '.collection_pagination | all(.[]; . == true)' "$EXPORT_DIR/manifest.json" >/dev/null || {
    echo "ERROR: Manifest does not confirm pagination completion."
    exit 1
  }

  jq --exit-status --slurpfile issues "$EXPORT_DIR/github/issues.json" '
    all(.[]; .issue_number as $number | $issues[0] | any(.[]; .number == $number))
  ' "$EXPORT_DIR/github/issue-comments.json" >/dev/null || {
    echo "ERROR: Issue comments reference missing issues."
    exit 1
  }

  jq --exit-status --slurpfile issues "$EXPORT_DIR/github/issues.json" '
    all(.[]; .issue_number as $number | $issues[0] | any(.[]; .number == $number))
  ' "$EXPORT_DIR/github/issue-timeline.json" >/dev/null || {
    echo "ERROR: Timeline events reference missing issues."
    exit 1
  }

  jq --exit-status --slurpfile pull_requests "$EXPORT_DIR/github/pull-requests.json" '
    all(.[]; .pull_request_number as $number | $pull_requests[0] | any(.[]; .number == $number))
  ' "$EXPORT_DIR/github/review-comments.json" >/dev/null || {
    echo "ERROR: Review comments reference missing pull requests."
    exit 1
  }

  echo "Integrity checks passed."
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
    "exports/$TIMESTAMP/github/releases.json" \
    "exports/$TIMESTAMP/github/project-items.json" \
    "exports/$TIMESTAMP/github/project-fields.json" \
    "exports/$TIMESTAMP/github/project-views.json" \
    "exports/$TIMESTAMP/github/issue-timeline.json" \
    "exports/$TIMESTAMP/github/review-comments.json"; do
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
  trap cleanup_staging EXIT
  check_github_access
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
  export_project_items
  export_project_fields
  export_project_views
  export_issue_timeline
  export_review_comments
  export_discussions
  create_manifest
  validate_integrity
  publish_export
  compress
  summary
}

main
