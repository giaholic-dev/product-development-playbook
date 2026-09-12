#!/usr/bin/env bash
set -Eeuo pipefail

print_header(){ echo "======================================"; echo " GitHub Audit Export"; echo "======================================"; echo; }
require(){ command -v "$1" >/dev/null 2>&1 || { echo "Missing command: $1"; exit 1; }; }
check_requirements(){ require git; require gh; require zip; }
check_repository(){ git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "Current directory is not a Git repository."; exit 1; }; }
load_repository(){
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"
REMOTE=$(git remote get-url origin); REMOTE=${REMOTE#*github.com[:/]}; REMOTE=${REMOTE%.git}
OWNER=${REMOTE%%/*}; REPOSITORY=${REMOTE##*/}
BRANCH=$(git branch --show-current)
COMMIT=$(git rev-parse HEAD)
SHORT_COMMIT=$(git rev-parse --short HEAD)
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
EXPORT_ROOT="audit"; EXPORT_DIR="$EXPORT_ROOT/exports/$TIMESTAMP"; ZIP_FILE="$EXPORT_ROOT/${REPOSITORY}-audit-${TIMESTAMP}.zip"
}
create_directories(){ mkdir -p "$EXPORT_DIR"; }
export_repository(){
cp README.md "$EXPORT_DIR/" 2>/dev/null || true
[ -d docs ] && cp -R docs "$EXPORT_DIR/"
[ -d templates ] && cp -R templates "$EXPORT_DIR/"
[ -d examples ] && cp -R examples "$EXPORT_DIR/"
find . -path "./.git" -prune -o -path "./audit" -prune -o -type f -print | sort > "$EXPORT_DIR/repository-tree.txt"
}
export_issues(){ gh issue list --repo "$OWNER/$REPOSITORY" --state all --limit 500 --json number,title,body,state,stateReason,labels,milestone,assignees,createdAt,updatedAt,closedAt > "$EXPORT_DIR/issues.json"; }
export_prs(){ gh pr list --repo "$OWNER/$REPOSITORY" --state all --limit 500 --json number,title,body,state,labels,author,createdAt,updatedAt,mergedAt,closedAt > "$EXPORT_DIR/pull-requests.json"; }
export_labels(){ gh label list --repo "$OWNER/$REPOSITORY" --json name,color,description > "$EXPORT_DIR/labels.json"; }
export_milestones(){ gh api "repos/$OWNER/$REPOSITORY/milestones?state=all" > "$EXPORT_DIR/milestones.json"; }
export_releases(){ gh release list --repo "$OWNER/$REPOSITORY" --json name,tagName,isDraft,isLatest,publishedAt > "$EXPORT_DIR/releases.json"; }
create_manifest(){
cat > "$EXPORT_DIR/manifest.json" <<EOF
{
  "owner":"$OWNER",
  "repository":"$REPOSITORY",
  "branch":"$BRANCH",
  "commit":"$COMMIT",
  "generated_at":"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF
}
compress() {

	ZIP_FILE="$EXPORT_ROOT/${REPOSITORY}-audit-${TIMESTAMP}.zip"
    (
        cd "$EXPORT_ROOT"
        zip -qr "$(basename "$ZIP_FILE")" "exports/$TIMESTAMP"
    )

	if [ ! -f "$ZIP_FILE" ]; then
		echo
		echo "ERROR: Failed to create zip archive."
		exit 1
	fi
}

summary(){ echo; echo "Repository : $OWNER/$REPOSITORY"; echo "Branch     : $BRANCH"; echo "Commit     : $SHORT_COMMIT"; echo; echo "Audit package:"; echo "  $ZIP_FILE"; }
main(){ print_header; check_requirements; check_repository; load_repository; create_directories; export_repository; export_issues; export_prs; export_labels; export_milestones; export_releases; create_manifest; compress; summary; }
main
