"""Synthetic HTTP fixtures verify PR evidence boundaries without GitHub access."""

import copy
import importlib.util
import json
import os
import sys
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("audit_pr", Path(__file__).with_name("audit-pr-evidence.py"))
PR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PR)
REPO = "fixture/repo"
BASE = "https://api.github.com/repos/" + REPO
TIME = "2026-10-22T12:00:00Z"
SHA = "a" * 40


def response(body, link=None, status=200):
    headers = f"HTTP/2.0 {status} OK\r\nX-Github-Request-Id: fixture\r\n"
    if link:
        headers += "Link: " + link + "\r\n"
    return (headers + "\r\n" + json.dumps(body)).encode()


def metadata(number):
    return {"id": number + 1000, "number": number, "url": BASE + "/pulls/" + str(number)}


def record(number, identity, kind, **extra):
    parent_key = "issue_url" if kind == "conversations" else "pull_request_url"
    parent_kind = "issues" if kind == "conversations" else "pulls"
    value = {"id": identity, "body": "fixture body", "user": None,
             parent_key: f"{BASE}/{parent_kind}/{number}", "created_at": TIME,
             "updated_at": TIME, "html_url": f"https://github.com/{REPO}/pull/{number}#fixture-{identity}"}
    if kind == "reviews":
        value.update(state="APPROVED", submitted_at=TIME, commit_id=SHA)
    if kind == "inline_comments":
        value.update(pull_request_review_id=200, path="file.txt", commit_id=SHA)
    value.update(extra)
    return value


class Fixture:
    def __init__(self, numbers=(1,)):
        self.routes = {"repos/" + REPO: response({"id": 10, "full_name": REPO})}
        self.requests = []
        for number in numbers:
            for prefix, end in (("issues", "comments"), ("pulls", "reviews"), ("pulls", "comments")):
                self.routes[self.route(number, prefix, end)] = response([])

    @staticmethod
    def route(number=1, prefix="issues", end="comments", page=1):
        return f"repos/{REPO}/{prefix}/{number}/{end}?per_page=100&page={page}"

    def __call__(self, target):
        self.requests.append(target)
        if target not in self.routes:
            raise PR.EvidenceError("Unexpected synthetic request.")
        value = self.routes[target]
        if isinstance(value, Exception):
            raise value
        return value


class PREvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.destination = Path(self.temp.name) / "github"
        self.fixture = Fixture()
        self.prs = [metadata(1)]

    def collect(self):
        return PR.collect_evidence(REPO, self.prs, self.destination, self.fixture)

    def read(self, name):
        return json.loads((self.destination / name).read_text())

    def test_multipage_conversations_and_distinct_review_history(self):
        first = record(1, 100, "conversations")
        second = record(1, 101, "conversations", body="second")
        self.fixture.routes[Fixture.route()] = response(
            [first], f'<{BASE}/issues/1/comments?per_page=100&page=2>; rel="next"')
        self.fixture.routes[Fixture.route(page=2)] = response([first, second])
        reviews = [
            record(1, 200, "reviews"),
            record(1, 201, "reviews", state="CHANGES_REQUESTED", commit_id="b" * 40),
            record(1, 202, "reviews", state="DISMISSED"),
            record(1, 203, "reviews", state="COMMENTED"),
        ]
        self.fixture.routes[Fixture.route(prefix="pulls", end="reviews")] = response(
            reviews[:2], f'<{BASE}/pulls/1/reviews?per_page=100&page=2>; rel="next"')
        self.fixture.routes[Fixture.route(prefix="pulls", end="reviews", page=2)] = response(reviews[2:])
        self.fixture.routes[Fixture.route(prefix="pulls")] = response([
            record(1, 300, "inline_comments"),
            record(1, 301, "inline_comments", in_reply_to_id=300),
        ])
        coverage = self.collect()
        PR.verify_evidence(REPO, self.prs, self.destination)
        self.assertEqual(len(self.read("pr-conversations.json")), 2)
        self.assertEqual([r["state"] for r in self.read("pr-reviews.json")],
                         ["APPROVED", "CHANGES_REQUESTED", "DISMISSED", "COMMENTED"])
        self.assertFalse(coverage["current_approval_inferred"])
        self.assertEqual(coverage["observations"][0]["raw_count"], 3)
        self.assertEqual(coverage["observations"][0]["retained_count"], 2)
        self.assertTrue(all(o["terminal_no_next"] for o in coverage["observations"]))
        self.assertEqual(self.read("review-comments.json")[1]["in_reply_to_id"], 300)

    def test_multiple_prs_including_complete_empty_and_pending(self):
        self.fixture = Fixture((1, 2))
        self.prs = [metadata(1), metadata(2)]
        self.fixture.routes[Fixture.route(2, "pulls", "reviews")] = response([
            record(2, 210, "reviews", state="PENDING", submitted_at=None, commit_id=None),
        ])
        coverage = self.collect()
        self.assertEqual(len(coverage["observations"]), 6)
        PR.verify_evidence(REPO, self.prs, self.destination)
        self.assertEqual(self.read("pr-reviews.json")[0]["state"], "PENDING")

    def test_canonical_repository_id_pagination_is_allowed(self):
        self.fixture.routes[Fixture.route()] = response(
            [], '<https://api.github.com/repositories/10/issues/1/comments?page=2&per_page=100>; rel="next"')
        self.fixture.routes["repositories/10/issues/1/comments?per_page=100&page=2"] = response([])
        self.collect()
        PR.verify_evidence(REPO, self.prs, self.destination)

    def test_denied_access_or_malformed_response_produces_no_outputs(self):
        for bad in (response({"message": "private fixture"}, status=403),
                    b"HTTP/2.0 200 OK\r\n\r\n[", response({"errors": ["partial"]})):
            with self.subTest(bad=bad[:24]):
                self.fixture.routes[Fixture.route(prefix="pulls", end="reviews")] = bad
                with self.assertRaises(PR.EvidenceError):
                    self.collect()
                self.assertFalse(self.destination.exists())

    def test_timeout_transport_failure_is_not_empty_success(self):
        self.fixture.routes[Fixture.route()] = PR.EvidenceError("Transport unavailable")
        with self.assertRaises(PR.EvidenceError):
            self.collect()
        self.assertFalse(self.destination.exists())

    def test_conflicting_replay_or_missing_id_fails(self):
        good = record(1, 100, "conversations")
        for values in ([good, dict(good, body="changed")], [dict(good, id=None)]):
            self.fixture.routes[Fixture.route()] = response(values)
            with self.assertRaises(PR.EvidenceError):
                self.collect()

    def test_foreign_parent_and_foreign_input_fail(self):
        self.fixture.routes[Fixture.route()] = response([
            record(1, 100, "conversations", issue_url=BASE + "/issues/2")
        ])
        with self.assertRaises(PR.EvidenceError):
            self.collect()
        self.fixture.routes[Fixture.route()] = response([])
        self.prs[0]["url"] = "https://api.github.com/repos/foreign/repo/pulls/1"
        with self.assertRaises(PR.EvidenceError):
            self.collect()

    def test_unsafe_or_nonadvancing_next_link_fails(self):
        urls = (
            "https://foreign.invalid/issues/1/comments?page=2",
            BASE + "/issues/1/comments?per_page=100&page=1",
            BASE + "/issues/1/comments?per_page=100&page=3",
            BASE + "/issues/2/comments?per_page=100&page=2",
            "https://token@api.github.com/repos/fixture/repo/issues/1/comments?page=2",
        )
        for url in urls:
            self.fixture.routes[Fixture.route()] = response([], f'<{url}>; rel="next"')
            with self.assertRaises(PR.EvidenceError):
                self.collect()

    def test_inline_missing_review_or_reply_is_not_complete(self):
        self.fixture.routes[Fixture.route(prefix="pulls")] = response([record(1, 300, "inline_comments")])
        with self.assertRaises(PR.EvidenceError):
            self.collect()
        self.fixture.routes[Fixture.route(prefix="pulls", end="reviews")] = response([
            record(1, 200, "reviews"),
        ])
        self.fixture.routes[Fixture.route(prefix="pulls")] = response([
            record(1, 300, "inline_comments", in_reply_to_id=999),
        ])
        with self.assertRaises(PR.EvidenceError):
            self.collect()

    def test_partial_or_tampered_coverage_is_rejected_offline(self):
        self.collect()
        path = self.destination / "pr-evidence-coverage.json"
        original = self.read(path.name)
        variants = []
        for mutation in ("next", "count", "duplicate", "approval"):
            value = copy.deepcopy(original)
            if mutation == "next":
                value["observations"][0]["pages"][-1]["next"] = Fixture.route(page=2)
            elif mutation == "count":
                value["observations"][0]["retained_count"] = 42
            elif mutation == "duplicate":
                value["observations"][1] = value["observations"][0]
            else:
                value["current_approval_inferred"] = True
            variants.append(value)
        for value in variants:
            path.write_text(json.dumps(value))
            with self.assertRaises(PR.EvidenceError):
                PR.verify_evidence(REPO, self.prs, self.destination)

    def test_duplicate_prs_and_cross_pr_provider_ids_fail(self):
        self.prs = [metadata(1), metadata(1)]
        with self.assertRaises(PR.EvidenceError):
            self.collect()
        self.prs = [metadata(1), metadata(2)]
        self.fixture = Fixture((1, 2))
        self.fixture.routes[Fixture.route(1)] = response([record(1, 100, "conversations")])
        self.fixture.routes[Fixture.route(2)] = response([record(2, 100, "conversations")])
        with self.assertRaises(PR.EvidenceError):
            self.collect()

    def test_existing_output_is_preserved(self):
        self.destination.mkdir()
        path = self.destination / "pr-reviews.json"
        path.write_text("keep")
        with self.assertRaises(PR.EvidenceError):
            self.collect()
        self.assertEqual(path.read_text(), "keep")

    def test_gh_transport_is_get_only_and_sanitizes_failures(self):
        secret = b"private diagnostic"
        result = subprocess.CompletedProcess([], 1, stdout=secret, stderr=secret)
        with patch.object(PR.subprocess, "run", return_value=result) as run:
            with self.assertRaises(PR.EvidenceError) as caught:
                PR.gh_get("repos/fixture/repo")
        self.assertNotIn(secret.decode(), str(caught.exception))
        args, options = run.call_args
        self.assertIn("GET", args[0])
        self.assertIn("--include", args[0])
        self.assertIn("github.com", args[0])
        self.assertEqual(options["env"]["GH_PROMPT_DISABLED"], "1")

    def test_bash_collector_and_cli_round_trip_with_synthetic_gh(self):
        root = Path(self.temp.name)
        binary = root / "bin"
        binary.mkdir()
        routes = root / "routes.json"
        routes.write_text(json.dumps({k: v.decode() for k, v in self.fixture.routes.items()}))
        gh = binary / "gh"
        gh.write_text("#!" + sys.executable + "\n" +
                      "import json, os, sys\n" +
                      "assert sys.argv[1:3] == ['api', '--hostname']\n" +
                      "assert sys.argv[sys.argv.index('--method') + 1] == 'GET'\n" +
                      "assert '--include' in sys.argv\n" +
                      "print(json.load(open(os.environ['FIXTURE_ROUTES']))[sys.argv[-1]], end='')\n")
        gh.chmod(0o700)
        self.destination.mkdir()
        prs = self.destination / "pull-requests.json"
        prs.write_text(json.dumps(self.prs))
        exporter = Path(__file__).with_name("export-audit.sh").resolve()
        command = 'source "$1"; OWNER=fixture; REPOSITORY=repo; EXPORT_DIR="$2"; export_review_comments'
        env = dict(os.environ, PATH=str(binary) + os.pathsep + os.environ["PATH"],
                   FIXTURE_ROUTES=str(routes))
        subprocess.run(["bash", "-euo", "pipefail", "-c", command, "fixture",
                        str(exporter), str(root)], env=env, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        PR.verify_evidence(REPO, self.prs, self.destination)
        self.assertEqual(self.read("pr-conversations.json"), [])
        self.assertEqual(len(self.read("pr-evidence-coverage.json")["observations"]), 3)

    def test_unknown_review_state_and_missing_commit_fail(self):
        for change in ({"state": "NEW_STATE"}, {"commit_id": None}):
            self.fixture.routes[Fixture.route(prefix="pulls", end="reviews")] = response([
                record(1, 200, "reviews", **change)
            ])
            with self.assertRaises(PR.EvidenceError):
                self.collect()


if __name__ == "__main__":
    unittest.main()
