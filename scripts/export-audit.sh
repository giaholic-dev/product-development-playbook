#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

EXPORT_SCHEMA_VERSION="2.0.0"
TOOL_VERSION="2.0.1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_HELPER="$SCRIPT_DIR/audit-source.py"
PR_EVIDENCE_HELPER="$SCRIPT_DIR/audit-pr-evidence.py"
PROJECT_HELPER="$SCRIPT_DIR/audit-project.py"
RECORDS_HELPER="$SCRIPT_DIR/audit-records.py"
PACKAGE_HELPER="$SCRIPT_DIR/audit-package.py"

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
  require python3
  python3 -c 'import sys; sys.exit(sys.version_info < (3, 12))' || {
    echo "Python 3.12 or later is required."
    exit 1
  }
  [[ "${GITHUB_AUDIT_SOURCE_REVIEWED:-false}" == "true" ]] || {
    echo "Review the source/data scope first, then set GITHUB_AUDIT_SOURCE_REVIEWED=true."
    exit 1
  }
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
  STAGING_DIR="$EXPORT_ROOT/.staging/$TIMESTAMP-$$"
  EXPORT_DIR="$STAGING_DIR"
  ZIP_FILE="$EXPORT_ROOT/${REPOSITORY}-audit-$TIMESTAMP.zip"
  PROJECT_NUMBER="${GITHUB_PROJECT_NUMBER:-1}"
  PROJECT_OWNER="${GITHUB_PROJECT_OWNER:-$OWNER}"
  PROJECT_OWNER_KIND="${GITHUB_PROJECT_OWNER_KIND:-organization}"
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

create_directories() {
  mkdir -p "$EXPORT_DIR/github" "$EXPORT_DIR/git"
}

export_repository() {
  python3 "$SOURCE_HELPER" export --root "$ROOT" --commit "$COMMIT" \
    --destination "$EXPORT_DIR/repository" --output-relative "$EXPORT_ROOT" --reviewed-source
  local source="$EXPORT_DIR/repository/source"
  cp "$source/README.md" "$EXPORT_DIR/repository/"
  mkdir -p "$EXPORT_DIR/repository/config"
  for path in .editorconfig .gitignore .shellcheckrc .gitattributes CODEOWNERS Makefile; do
    [[ -f "$source/$path" ]] && cp "$source/$path" "$EXPORT_DIR/repository/config/"
  done
  [[ ! -d "$source/docs" ]] || cp -R "$source/docs" "$EXPORT_DIR/repository/"
  [[ ! -d "$source/templates" ]] || cp -R "$source/templates" "$EXPORT_DIR/repository/"
  [[ ! -d "$source/examples" ]] || cp -R "$source/examples" "$EXPORT_DIR/repository/"
  # JSON-escaped path per line avoids ambiguity for tracked newlines.
  jq -r '.entries[].path | tojson' "$EXPORT_DIR/repository/source-inventory.json" \
    >"$EXPORT_DIR/repository/repository-tree.txt"
}

verify_source_snapshot() {
  python3 "$SOURCE_HELPER" verify --root "$ROOT" --destination "$EXPORT_DIR/repository"
}

export_branches() {
  git for-each-ref --sort=refname --format='%(refname:short) %(objectname) %(upstream:short)' refs/heads refs/remotes >"$EXPORT_DIR/git/branches.txt"
}

export_tags() {
  git for-each-ref --sort=refname --format='%(refname:short) %(objectname) %(objecttype)' refs/tags >"$EXPORT_DIR/git/tags.txt"
}

export_recent_commits() {
  git log -n 100 --date=iso-strict --format='%H%x09%P%x09%an%x09%ae%x09%ad%x09%s' >"$EXPORT_DIR/git/recent-commits.tsv"
}

export_repository_status() {
  git status --porcelain=v1 --branch >"$EXPORT_DIR/git/status.txt"
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

export_record_evidence() {
  python3 "$RECORDS_HELPER" collect --repository "$OWNER/$REPOSITORY" \
    --discussions "$EXPORT_DISCUSSIONS" --destination "$EXPORT_DIR/github"
}

export_project_evidence() {
  python3 "$PROJECT_HELPER" collect --owner-kind "$PROJECT_OWNER_KIND" --owner "$PROJECT_OWNER" \
    --number "$PROJECT_NUMBER" --repository "$OWNER/$REPOSITORY" --destination "$EXPORT_DIR/github"
}

verify_project_evidence() {
  python3 "$PROJECT_HELPER" verify --owner-kind "$PROJECT_OWNER_KIND" --owner "$PROJECT_OWNER" \
    --number "$PROJECT_NUMBER" --repository "$OWNER/$REPOSITORY" --destination "$EXPORT_DIR/github"
}

export_review_comments() {
  python3 "$PR_EVIDENCE_HELPER" collect --repository "$OWNER/$REPOSITORY" \
    --prs "$EXPORT_DIR/github/pull-requests.json" --destination "$EXPORT_DIR/github"
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
    --argjson pr_conversations "$(collection_count "$EXPORT_DIR/github/pr-conversations.json")" \
    --argjson pr_reviews "$(collection_count "$EXPORT_DIR/github/pr-reviews.json")" \
    --argjson project_values "$(collection_count "$EXPORT_DIR/github/project-values.json")" \
    --slurpfile project_evidence "$EXPORT_DIR/github/project-coverage.json" \
    --slurpfile pr_evidence "$EXPORT_DIR/github/pr-evidence-coverage.json" \
    --slurpfile source_snapshot "$EXPORT_DIR/repository/source-inventory.json" \
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
      coverage_profile: "legacy-plus-source-pr-and-project-evidence",
      full_profile_complete: false,
      project_evidence: {
        coverage: "github/project-coverage.json",
        transcript: "github/project-requests.json",
        values: "github/project-values.json",
        evidence_schema_version: $project_evidence[0].evidence_schema_version,
        project: $project_evidence[0].project,
        scope: $project_evidence[0].scope
      },
      pr_evidence: {
        coverage: "github/pr-evidence-coverage.json",
        evidence_schema_version: $pr_evidence[0].evidence_schema_version,
        scope: $pr_evidence[0].scope,
        current_approval_inferred: false
      },
      source_snapshot: {
        inventory: "repository/source-inventory.json",
        root: "repository/source",
        commit: $source_snapshot[0].commit,
        tree: $source_snapshot[0].tree,
        source_kind: $source_snapshot[0].source_kind,
        working_tree_bytes_included: false,
        all_tracked_blobs_retained: $source_snapshot[0].all_tracked_blobs_retained,
        policy_version: $source_snapshot[0].policy_version,
        dirty_initial: $source_snapshot[0].dirty_initial,
        dirty_final: $source_snapshot[0].dirty_final
      },
      collection_counts: {
        issues: $issues,
        issue_comments: $issue_comments,
        pull_requests: $pull_requests,
        labels: $labels,
        milestones: $milestones,
        releases: $releases,
        project_values: $project_values,
        project_items: $project_items,
        project_fields: $project_fields,
        project_views: $project_views,
        issue_timeline: $issue_timeline,
        pr_conversations: $pr_conversations,
        pr_reviews: $pr_reviews,
        review_comments: $review_comments
      },
      collection_pagination: {
        issues: true,
        issue_comments: true,
        pull_requests: true,
        labels: true,
        milestones: true,
        releases: true,
        project_values: true,
        project_items: true,
        project_fields: true,
        project_views: true,
        issue_timeline: true,
        pr_conversations: true,
        pr_reviews: true,
        review_comments: true
      }
    }' >"$manifest_temporary"
  publish_json "$manifest_temporary" "$EXPORT_DIR/manifest.json" object
}

seal_manifest() {
  python3 "$PACKAGE_HELPER" seal --package "$EXPORT_DIR"
}

validate_integrity() {
  verify_source_snapshot
  python3 "$PACKAGE_HELPER" verify --package "$EXPORT_DIR"
  echo "Integrity checks passed."
}

compress() {
  python3 "$PACKAGE_HELPER" finalize --package "$EXPORT_DIR" \
    --final-directory "$FINAL_EXPORT_DIR" --archive "$ZIP_FILE" --source-root "$ROOT"
  EXPORT_DIR="$FINAL_EXPORT_DIR"
  STAGING_DIR=""
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
  export_record_evidence
  export_project_evidence
  export_review_comments
  create_manifest
  seal_manifest
  validate_integrity
  compress
  summary
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  main
fi
