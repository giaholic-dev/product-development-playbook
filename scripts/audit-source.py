#!/usr/bin/env python3
"""Retain and verify inert committed-source bytes for the audit exporter."""

import argparse
import fnmatch
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone

POLICY_VERSION = "1.0.0"
PROTECTED_COMPONENTS = {".git", ".ssh", ".aws"}
PROTECTED_NAMES = (
    ".env", ".env.*", ".netrc", ".npmrc", ".pypirc", ".git-credentials",
    "credentials.json", "service-account*.json", "id_rsa", "id_dsa",
    "id_ecdsa", "id_ed25519", "*.key", "*.pem", "*.p12", "*.pfx",
)
TEMPLATE_NAMES = {".env.example", ".env.sample"}
REQUIRED_ROOTS = {"docs", "templates", "examples", "scripts", ".github", ".devcontainer"}
SECRET_PATTERNS = (
    re.compile(rb"(?m)^-----BEGIN (?:[A-Z0-9]+ )?PRIVATE KEY-----"),
    re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    re.compile(rb"\bsk-proj-[A-Za-z0-9_-]{40,}\b"),
)


class SnapshotError(Exception):
    """Safe diagnostic; never include content or credential-bearing arguments."""


def git(root, *args):
    result = subprocess.run(
        ["git", "--no-replace-objects", "-C", str(root), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode:
        raise SnapshotError("Git source read failed; no source payload is logged.")
    return result.stdout


def identity(root):
    return git(root, "rev-parse", "--verify", "HEAD").decode("ascii").strip()


def dirty(root):
    return bool(git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all"))


def safe_path(name):
    if not name or "\x00" in name or "\\" in name:
        raise SnapshotError("Unsafe source path.")
    path = PurePosixPath(name)
    if path.is_absolute() or any(p in {"", ".", ".."} for p in name.split("/")):
        raise SnapshotError("Unsafe source path.")
    if any(":" in p for p in path.parts):
        raise SnapshotError("Non-portable source path.")
    return path


def tree_entries(root, commit):
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit):
        raise SnapshotError("Expected a resolved immutable commit identity.")
    entries = []
    seen = set()
    for record in git(root, "ls-tree", "-r", "-z", "--full-tree", commit).split(b"\0"):
        if not record:
            continue
        meta, raw_path = record.split(b"\t", 1)
        try:
            name = raw_path.decode("utf-8")
            mode, kind, oid = meta.decode("ascii").split(" ")
        except (UnicodeError, ValueError) as exc:
            raise SnapshotError("Unsupported tree path encoding or metadata.") from exc
        safe_path(name)
        # Reject case collisions before writing on case-insensitive hosts.
        folded = name.casefold()
        if folded in seen:
            raise SnapshotError("Duplicate or case-colliding source path.")
        seen.add(folded)
        if (mode, kind) not in {
            ("100644", "blob"), ("100755", "blob"),
            ("120000", "blob"), ("160000", "commit"),
        }:
            raise SnapshotError("Unsupported tracked source mode.")
        entries.append({"path": name, "mode": mode, "git_type": kind, "object_id": oid})
    # A file cannot be another file's parent even on a case-insensitive host.
    for entry in entries:
        parts = PurePosixPath(entry["path"]).parts
        if any("/".join(parts[:i]).casefold() in seen for i in range(1, len(parts))):
            raise SnapshotError("Colliding source parent path.")
    return entries


def exclusion(name, output_relative):
    path = safe_path(name)
    lowered = [p.casefold() for p in path.parts]
    output_parts = [p.casefold() for p in safe_path(output_relative).parts]
    if lowered[:len(output_parts)] == output_parts:
        return "configured-output"
    if any(p in PROTECTED_COMPONENTS for p in lowered):
        return "protected-component"
    base = lowered[-1]
    if base not in TEMPLATE_NAMES and any(fnmatch.fnmatchcase(base, p) for p in PROTECTED_NAMES):
        return "protected-basename"
    return None


def required_source(name):
    path = PurePosixPath(name)
    return name == "README.md" or path.parts[0].casefold() in REQUIRED_ROOTS


def describe(root, entry, output_relative):
    record = dict(entry)
    reason = exclusion(entry["path"], output_relative)
    if reason:
        if required_source(entry["path"]):
            raise SnapshotError("Protected/output exclusion affects required audit source.")
        record.update(disposition="excluded", reason=reason)
        return record, None
    if entry["mode"] == "160000":
        if required_source(entry["path"]):
            raise SnapshotError("Missing required submodule source bytes.")
        record.update(disposition="gitlink-only", reason="external-content-not-collected")
        return record, None
    content = git(root, "cat-file", "blob", entry["object_id"])
    if any(p.search(content) for p in SECRET_PATTERNS):
        raise SnapshotError("Suspected credential material; review source before export.")
    if content.startswith(b"version https://git-lfs.github.com/spec/v1\n"):
        if required_source(entry["path"]):
            raise SnapshotError("Missing required Git LFS source content.")
        disposition = "lfs-pointer-only"
    else:
        disposition = "retained"
    record.update(
        disposition=disposition, size_bytes=len(content),
        sha256=hashlib.sha256(content).hexdigest(),
        stored_as="inert-regular-file",
    )
    return record, content


def ensure_head(root, commit):
    if identity(root) != commit:
        raise SnapshotError("HEAD changed from the selected source; retry as a new run.")


def source_policy():
    return {
        "protected_components": sorted(PROTECTED_COMPONENTS),
        "protected_basenames": list(PROTECTED_NAMES),
        "reviewed_template_candidates": sorted(TEMPLATE_NAMES),
        "required_roots": sorted(REQUIRED_ROOTS),
        "symlinks": "inert-blob-only", "submodules": "identity-only",
        "lfs": "pointer-only", "sensitivity_review_confirmed": True,
        "secret_detection": "bounded-heuristics-not-a-guarantee",
    }


def export_snapshot(root, commit, destination, output_relative="audit", reviewed=False):
    root = Path(root).resolve()
    destination = Path(destination)
    if not reviewed:
        raise SnapshotError("Explicit source-scope review is required before export.")
    safe_path(output_relative)
    ensure_head(root, commit)
    if destination.exists() or destination.is_symlink():
        raise SnapshotError("Refusing to overwrite a source snapshot.")
    entries = tree_entries(root, commit)
    if not any(e["path"] == "README.md" and e["mode"] in {"100644", "100755"} for e in entries):
        raise SnapshotError("The selected commit must contain a regular README.md.")
    observed_start = datetime.now(timezone.utc).isoformat()
    initial_dirty = dirty(root)
    tree = git(root, "rev-parse", commit + "^{tree}").decode("ascii").strip()
    destination.mkdir(mode=0o700)
    try:
        source = destination / "source"
        source.mkdir(mode=0o700)
        records = []
        for entry in entries:
            record, content = describe(root, entry, output_relative)
            if content is not None:
                target = source.joinpath(*safe_path(entry["path"]).parts)
                target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
                with target.open("xb") as stream:
                    os.chmod(target, 0o600)
                    stream.write(content)
            records.append(record)
        ensure_head(root, commit)
        inventory = {
            "snapshot_schema_version": "1.0.0",
            "policy_version": POLICY_VERSION,
            "commit": commit, "tree": tree,
            "dirty_initial": initial_dirty, "dirty_final": dirty(root),
            "source_kind": "committed-git-tree",
            "working_tree_bytes_included": False,
            "output_relative": output_relative,
            "policy": source_policy(),
            "observation_started_at": observed_start,
            "observation_ended_at": datetime.now(timezone.utc).isoformat(),
            "tracked_entries": len(records),
            "all_tracked_blobs_retained": all(r["disposition"] == "retained" for r in records),
            "entries": records,
        }
        inventory_path = destination / "source-inventory.json"
        with inventory_path.open("x", encoding="utf-8") as stream:
            os.chmod(inventory_path, 0o600)
            json.dump(inventory, stream, ensure_ascii=True, indent=2)
            stream.write("\n")
        return inventory
    except BaseException:
        # Only remove the new directory created by this invocation.
        shutil.rmtree(destination)
        raise


def verify_snapshot(root, destination):
    root, destination = Path(root).resolve(), Path(destination)
    inventory_path = destination / "source-inventory.json"
    if inventory_path.is_symlink() or not inventory_path.is_file():
        raise SnapshotError("Missing or unsafe source inventory.")
    try:
        inventory = json.loads(inventory_path.read_text())
        commit = inventory["commit"]
        output_relative = inventory["output_relative"]
        if inventory["snapshot_schema_version"] != "1.0.0":
            raise SnapshotError("Unsupported source inventory version.")
        ensure_head(root, commit)
        entries = tree_entries(root, commit)
        expected = [describe(root, e, output_relative)[0] for e in entries]
        if expected != inventory["entries"] or len(entries) != inventory["tracked_entries"]:
            raise SnapshotError("Source inventory does not match the selected Git tree/policy.")
        tree = git(root, "rev-parse", commit + "^{tree}").decode("ascii").strip()
        if inventory["tree"] != tree or inventory["policy_version"] != POLICY_VERSION:
            raise SnapshotError("Source tree/policy identity mismatch.")
        if inventory["policy"] != source_policy():
            raise SnapshotError("Source policy mismatch.")
        if inventory["all_tracked_blobs_retained"] != all(r["disposition"] == "retained" for r in expected):
            raise SnapshotError("Source coverage claim mismatch.")
        if inventory["working_tree_bytes_included"] or inventory["source_kind"] != "committed-git-tree":
            raise SnapshotError("Unsupported source-byte claim.")
        expected_paths = set()
        for record in expected:
            if "sha256" not in record:
                continue
            name = record["path"]
            path = destination / "source" / name
            # Every parent and leaf must be inert; never follow a substituted symlink.
            relative_parts = ("source",) + safe_path(name).parts
            parent = destination
            for part in relative_parts:
                parent = parent / part
                if parent.is_symlink():
                    raise SnapshotError("Unsafe symlink in source snapshot.")
            if not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
                raise SnapshotError("Missing required retained source payload.")
            content = path.read_bytes()
            if len(content) != record["size_bytes"] or hashlib.sha256(content).hexdigest() != record["sha256"]:
                raise SnapshotError("Source payload hash/size mismatch.")
            expected_paths.add(name)
        actual_paths = {
            p.relative_to(destination / "source").as_posix()
            for p in (destination / "source").rglob("*") if p.is_file() or p.is_symlink()
        }
        if expected_paths != actual_paths:
            raise SnapshotError("Unexpected or missing snapshot payload.")
        ensure_head(root, commit)
        return inventory
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise SnapshotError("Invalid source inventory or payload.") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("export", "verify"))
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--commit")
    parser.add_argument("--output-relative", default="audit")
    parser.add_argument("--reviewed-source", action="store_true")
    args = parser.parse_args()
    try:
        if args.action == "export":
            if not args.commit:
                raise SnapshotError("A resolved source commit is required.")
            export_snapshot(
                args.root, args.commit, args.destination,
                args.output_relative, args.reviewed_source,
            )
        else:
            verify_snapshot(args.root, args.destination)
    except (SnapshotError, OSError) as exc:
        # OSError can contain paths; do not echo it or raw Git stderr.
        message = str(exc) if isinstance(exc, SnapshotError) else "Source filesystem operation failed."
        print("ERROR: " + message, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
