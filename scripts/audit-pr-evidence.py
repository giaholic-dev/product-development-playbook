#!/usr/bin/env python3
"""Collect bounded PR evidence through read-only gh requests; never infer approval."""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit

API_VERSION = "2022-11-28"
FILES = {
    "conversations": "pr-conversations.json",
    "reviews": "pr-reviews.json",
    "inline_comments": "review-comments.json",
}
STATES = {"APPROVED", "CHANGES_REQUESTED", "COMMENTED", "DISMISSED", "PENDING"}


class EvidenceError(Exception):
    """Sanitized collection/validation failure."""


def now():
    return datetime.now(timezone.utc).isoformat()


def positive_id(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def json_load(data):
    def invalid_constant(_):
        raise ValueError("Non-JSON constant")
    try:
        return json.loads(data, parse_constant=invalid_constant)
    except (ValueError, UnicodeError) as exc:
        raise EvidenceError("Malformed JSON evidence.") from exc


def parse_response(raw):
    match = re.search(rb"\r?\n\r?\n", raw)
    if not match:
        raise EvidenceError("Missing HTTP response boundary.")
    try:
        lines = raw[:match.start()].decode("ascii").splitlines()
        status = re.fullmatch(r"HTTP/[0-9.]+ ([0-9]{3})(?: .*)?", lines[0])
        if not status or int(status[1]) != 200:
            raise EvidenceError("Required API request did not return HTTP 200.")
        headers = {}
        for line in lines[1:]:
            name, value = line.split(":", 1)
            name = name.lower()
            headers[name] = headers.get(name, "") + (", " if name in headers else "") + value.strip()
        return headers, json_load(raw[match.end():])
    except (UnicodeError, ValueError, IndexError) as exc:
        raise EvidenceError("Invalid HTTP response metadata.") from exc


def gh_get(endpoint):
    env = dict(os.environ, GH_PROMPT_DISABLED="1")
    env.pop("GH_DEBUG", None)
    try:
        result = subprocess.run(
            ["gh", "api", "--hostname", "github.com", "--method", "GET", "--include",
             "-H", "Accept: application/vnd.github+json",
             "-H", "X-GitHub-Api-Version: " + API_VERSION, endpoint],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, timeout=120, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise EvidenceError("Required API transport unavailable or timed out.") from exc
    if result.returncode:
        raise EvidenceError("Required API request failed; no response body is logged.")
    return result.stdout


class Client:
    def __init__(self, repository, transport=gh_get):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise EvidenceError("Expected one GitHub owner/repository.")
        self.repository = repository
        self.transport = transport
        headers, repo = parse_response(transport("repos/" + repository))
        if not isinstance(repo, dict) or not positive_id(repo.get("id")):
            raise EvidenceError("Missing repository identity.")
        if str(repo.get("full_name", "")).casefold() != repository.casefold():
            raise EvidenceError("Repository response identity differs from selected target.")
        self.repository_id = repo["id"]
        _, principal = parse_response(transport("user"))
        if (not isinstance(principal, dict) or not positive_id(principal.get("id"))
                or not isinstance(principal.get("login"), str) or not principal["login"]):
            raise EvidenceError("Missing observed PR principal identity.")
        self.principal = {k: principal[k] for k in ("id", "login")}
        self.identity_observed_at = now()

    def target(self, url, suffix):
        if not isinstance(url, str):
            raise EvidenceError("Missing required API target reference.")
        parsed = urlsplit(url)
        if parsed.scheme != "https" or parsed.netloc != "api.github.com" or parsed.fragment:
            raise EvidenceError("Unsafe pagination/parent target.")
        allowed = {"/repos/" + self.repository + "/" + suffix,
                   "/repositories/" + str(self.repository_id) + "/" + suffix}
        if parsed.path.casefold() not in {p.casefold() for p in allowed}:
            raise EvidenceError("Pagination/parent target escapes the selected collection.")
        return parsed

    def next_target(self, link, suffix, current_page):
        matches = re.findall(r'<([^>]+)>\s*;\s*rel="([^"]+)"', link)
        if link and (not matches or len(matches) != len(link.split(","))):
            raise EvidenceError("Unrecognized pagination link metadata.")
        next_links = [url for url, relation in matches if relation == "next"]
        if not next_links:
            return None
        if len(next_links) != 1:
            raise EvidenceError("Ambiguous next-page evidence.")
        parsed = self.target(next_links[0], suffix)
        query = parse_qs(parsed.query, keep_blank_values=True)
        if set(query) - {"page", "per_page"} or len(query.get("page", [])) != 1:
            raise EvidenceError("Unsupported pagination parameter.")
        if not query["page"][0].isdigit():
            raise EvidenceError("Invalid next-page identity.")
        page = int(query["page"][0])
        if page != current_page + 1:
            raise EvidenceError("Pagination does not advance to the next page.")
        if "per_page" in query and query["per_page"] != ["100"]:
            raise EvidenceError("Pagination page size changed.")
        # Follow the validated canonical path; never arbitrary linked resources.
        return parsed.path.lstrip("/") + "?" + urlencode({"per_page": 100, "page": page})

    def collect(self, suffix, number, kind):
        endpoint = "repos/" + self.repository + "/" + suffix + "?per_page=100&page=1"
        started, records, pages = now(), {}, []
        for index in range(1, 10001):
            headers, payload = parse_response(self.transport(endpoint))
            if not isinstance(payload, list):
                raise EvidenceError("Required collection is not an array.")
            next_endpoint = self.next_target(headers.get("link", ""), suffix, index)
            for raw in payload:
                record = validate_record(self, raw, number, kind)
                key = record["id"]
                if key in records and records[key] != record:
                    raise EvidenceError("Conflicting duplicate provider identity.")
                records[key] = record
            pages.append({
                "request": endpoint, "status": 200, "returned_count": len(payload),
                "next": next_endpoint, "request_id": headers.get("x-github-request-id"),
                "observed_at": now(),
            })
            if next_endpoint is None:
                break
            endpoint = next_endpoint
        else:
            raise EvidenceError("Pagination resource limit reached; collection is incomplete.")
        evidence = {
            "pull_request_number": number, "kind": kind, "status": "complete",
            "started_at": started, "ended_at": now(), "pages": pages,
            "raw_count": sum(p["returned_count"] for p in pages),
            "retained_count": len(records), "terminal_no_next": True,
        }
        return sorted(records.values(), key=lambda r: r["id"]), evidence


def validate_record(client, raw, number, kind):
    if not positive_id(number):
        raise EvidenceError("Invalid PR parent number.")
    if not isinstance(raw, dict) or not positive_id(raw.get("id")):
        raise EvidenceError("Missing or invalid provider record identity.")
    if not isinstance(raw.get("body"), str):
        raise EvidenceError("Missing required comment/review body.")
    parent_key = "issue_url" if kind == "conversations" else "pull_request_url"
    parent_kind = "issues" if kind == "conversations" else "pulls"
    client.target(raw.get(parent_key, ""), parent_kind + "/" + str(number))
    if urlsplit(raw[parent_key]).query:
        raise EvidenceError("Unexpected parent-reference query.")
    if kind == "reviews":
        if raw.get("state") not in STATES:
            raise EvidenceError("Unsupported review state.")
        if raw["state"] != "PENDING" and not isinstance(raw.get("submitted_at"), str):
            raise EvidenceError("Missing submitted review timestamp.")
        commit = raw.get("commit_id")
        if (commit is None and raw["state"] != "PENDING") or (commit is not None and (
                not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit))):
            raise EvidenceError("Invalid reviewed commit identity.")
    if kind == "inline_comments":
        if not positive_id(raw.get("pull_request_review_id")):
            raise EvidenceError("Missing inline review reference.")
        if not isinstance(raw.get("path"), str):
            raise EvidenceError("Missing inline file reference.")
        reply = raw.get("in_reply_to_id")
        if reply is not None and not positive_id(reply):
            raise EvidenceError("Invalid inline reply identity.")
    record = dict(raw)
    record["pull_request_number"] = number
    return record


def pr_numbers(prs):
    if not isinstance(prs, list):
        raise EvidenceError("Expected collected PR metadata array.")
    numbers, identities = set(), set()
    for pr in prs:
        if not isinstance(pr, dict) or not positive_id(pr.get("number")) or not positive_id(pr.get("id")):
            raise EvidenceError("Invalid PR input identity.")
        if pr["number"] in numbers or pr["id"] in identities:
            raise EvidenceError("Duplicate PR input identity.")
        numbers.add(pr["number"])
        identities.add(pr["id"])
    return sorted(numbers)


def validate_relations(outputs):
    reviews = {r["id"]: r for r in outputs["reviews"]}
    inline = {r["id"]: r for r in outputs["inline_comments"]}
    for comment in inline.values():
        review = reviews.get(comment["pull_request_review_id"])
        if review is None or review["pull_request_number"] != comment["pull_request_number"]:
            raise EvidenceError("Inline comment references an unobserved/foreign review.")
        if comment.get("in_reply_to_id") is not None:
            parent = inline.get(comment["in_reply_to_id"])
            if parent is None or parent["pull_request_number"] != comment["pull_request_number"]:
                raise EvidenceError("Inline reply references an unobserved/foreign comment.")


def collect_evidence(repository, prs, destination, transport=gh_get):
    numbers = pr_numbers(prs)
    destination = Path(destination)
    client = Client(repository, transport)
    for pr in prs:
        client.target(pr.get("url", ""), "pulls/" + str(pr["number"]))
    outputs = {kind: [] for kind in FILES}
    observations = []
    for number in numbers:
        for kind, suffix in (
            ("conversations", "issues/" + str(number) + "/comments"),
            ("reviews", "pulls/" + str(number) + "/reviews"),
            ("inline_comments", "pulls/" + str(number) + "/comments"),
        ):
            records, evidence = client.collect(suffix, number, kind)
            outputs[kind].extend(records)
            observations.append(evidence)
    for records in outputs.values():
        if len(records) != len({r["id"] for r in records}):
            raise EvidenceError("Provider identity reused across distinct PR parents.")
    validate_relations(outputs)
    coverage = {
        "evidence_schema_version": "1.1.0", "api_version": API_VERSION,
        "repository": repository, "repository_id": client.repository_id,
        "identity_observed_at": client.identity_observed_at,
        "principal": client.principal,
        "pr_numbers": numbers, "observations": observations,
        "scope": "authorized-observable-pr-evidence",
        "current_approval_inferred": False,
    }
    paths = list(FILES.values()) + ["pr-evidence-coverage.json"]
    if any((destination / p).exists() or (destination / p).is_symlink() for p in paths):
        raise EvidenceError("Refusing to overwrite PR evidence.")
    destination.mkdir(parents=True, exist_ok=True, mode=0o700)
    staging = Path(tempfile.mkdtemp(prefix=".pr-evidence-", dir=destination))
    try:
        data = {FILES[k]: v for k, v in outputs.items()}
        data["pr-evidence-coverage.json"] = coverage
        for name, value in data.items():
            path = staging / name
            with path.open("x", encoding="utf-8") as stream:
                os.chmod(path, 0o600)
                json.dump(value, stream, ensure_ascii=True, indent=2, allow_nan=False)
                stream.write("\n")
        for name in paths:
            os.replace(staging / name, destination / name)
    finally:
        shutil.rmtree(staging)
    return coverage


def verify_evidence(repository, prs, destination):
    destination = Path(destination)
    coverage = json_load((destination / "pr-evidence-coverage.json").read_bytes())
    numbers = pr_numbers(prs)
    if (not isinstance(coverage, dict)
            or coverage.get("evidence_schema_version") != "1.1.0"
            or coverage.get("api_version") != API_VERSION
            or coverage.get("repository") != repository
            or coverage.get("pr_numbers") != numbers
            or coverage.get("current_approval_inferred") is not False):
        raise EvidenceError("PR coverage identity/version/approval claim mismatch.")
    principal = coverage.get("principal")
    if (not isinstance(principal, dict) or set(principal) != {"id", "login"}
            or not positive_id(principal.get("id")) or not isinstance(principal.get("login"), str)
            or not principal["login"]):
        raise EvidenceError("Invalid retained PR principal identity.")
    # Offline identity and target checking must perform no provider request.
    client = object.__new__(Client)
    client.repository = repository
    client.repository_id = coverage["repository_id"]
    if not positive_id(client.repository_id):
        raise EvidenceError("Invalid retained repository identity.")
    outputs = {}
    for kind, filename in FILES.items():
        records = json_load((destination / filename).read_bytes())
        if not isinstance(records, list):
            raise EvidenceError("Invalid retained PR collection.")
        validated = [validate_record(client, r, r.get("pull_request_number") if isinstance(r, dict) else None, kind) for r in records]
        if any(r["pull_request_number"] not in numbers for r in validated):
            raise EvidenceError("Retained record has foreign PR parent.")
        if len(validated) != len({r["id"] for r in validated}):
            raise EvidenceError("Duplicate retained PR identity.")
        outputs[kind] = validated
    validate_relations(outputs)
    observations = coverage.get("observations")
    if not isinstance(observations, list) or len(observations) != len(numbers) * len(FILES):
        raise EvidenceError("Missing per-PR collection observations.")
    observed = set()
    for observation in observations:
        kind, number = observation["kind"], observation["pull_request_number"]
        key = kind, number
        if kind not in FILES or number not in numbers or key in observed:
            raise EvidenceError("Invalid/duplicate collection observation.")
        observed.add(key)
        pages = observation["pages"]
        if (observation["status"] != "complete" or not observation["terminal_no_next"]
                or not pages or pages[-1]["next"] is not None):
            raise EvidenceError("Incomplete required PR traversal.")
        expected = len([r for r in outputs[kind] if r["pull_request_number"] == number])
        if observation["retained_count"] != expected:
            raise EvidenceError("PR retained-count mismatch.")
        suffix_kind = "issues" if kind == "conversations" else "pulls"
        suffix_end = "reviews" if kind == "reviews" else "comments"
        suffix = f"{suffix_kind}/{number}/{suffix_end}"
        seen_requests = set()
        for index, page in enumerate(pages, 1):
            target = client.target("https://api.github.com/" + page["request"], suffix)
            query = parse_qs(target.query)
            if query != {"per_page": ["100"], "page": [str(index)]}:
                raise EvidenceError("Invalid recorded page identity.")
            if page["status"] != 200 or page["request"] in seen_requests:
                raise EvidenceError("Invalid/repeated recorded page.")
            seen_requests.add(page["request"])
            if not isinstance(page["returned_count"], int) or page["returned_count"] < 0:
                raise EvidenceError("Invalid raw page count.")
            if index < len(pages) and page["next"] != pages[index]["request"]:
                raise EvidenceError("Missing recorded page continuation.")
        raw_count = sum(p["returned_count"] for p in pages)
        if observation["raw_count"] != raw_count or raw_count < expected:
            raise EvidenceError("PR raw-count mismatch.")
    return coverage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("collect", "verify"))
    parser.add_argument("--repository", required=True)
    parser.add_argument("--prs", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    try:
        prs = json_load(args.prs.read_bytes())
        if args.action == "collect":
            collect_evidence(args.repository, prs, args.destination)
        verify_evidence(args.repository, prs, args.destination)
    except (EvidenceError, OSError, KeyError, TypeError, ValueError) as exc:
        message = str(exc) if isinstance(exc, EvidenceError) else "Invalid PR input/output evidence."
        print("ERROR: " + message, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
