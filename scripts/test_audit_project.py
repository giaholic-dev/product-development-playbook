"""Synthetic GraphQL fixtures; no provider requests or credentials required."""

import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("audit_project", Path(__file__).with_name("audit-project.py"))
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)
REPO = "fixture/repo"
TIME = "2026-10-23T12:00:00Z"


def field(kind, suffix="", organization=False):
    datatype = P.SCALARS.get(kind, P.RELATIONS.get(kind, P.SINGULAR.get(kind, (kind.upper(),))))[0]
    typ = kind if kind in {"SingleSelect", "MultiSelect", "Iteration"} else ""
    value = {"id": "F" + kind + suffix, "__typename": "ProjectV2" + typ + "Field",
             "name": kind + suffix, "dataType": datatype, "isIssueField": organization}
    if organization:
        value["issueField"] = {"id": "OF" + kind, "__typename": "IssueField" + kind,
                               "name": kind, "dataType": datatype}
    if kind in {"SingleSelect", "MultiSelect"}:
        options = [{"id": "O1", "name": "One"}, {"id": "O2", "name": "Two"}]
        if organization:
            value["issueField"]["options"] = options
        else:
            value["options" if kind == "SingleSelect" else "multiSelectOptions"] = options
    if kind == "Iteration":
        value["configuration"] = {"duration": 7, "startDay": 1, "iterations": [],
                                  "completedIterations": [{"id": "OLD", "title": "Past",
                                                           "startDate": "2026-10-01", "duration": 7}]}
    return value


def item(identifier="I1", kind="ISSUE", external=False, archived=False):
    content_kind = {"ISSUE": "Issue", "PULL_REQUEST": "PullRequest", "DRAFT_ISSUE": "DraftIssue"}
    content = {"__typename": content_kind.get(kind), "id": "C" + identifier}
    if kind in {"ISSUE", "PULL_REQUEST"}:
        repo = "other/repo" if external else REPO
        content.update(number=1, url="https://github.com/" + repo + "/issues/1",
                       repository={"id": "R", "nameWithOwner": repo, "url": "https://github.com/" + repo})
    return {"id": identifier, "type": kind, "isArchived": archived, "createdAt": TIME,
            "updatedAt": TIME, "project": {"id": "P"}, "content": None if kind == "REDACTED" else content}


def scalar(f, kind, identifier="I1", **override):
    value = {"__typename": "ProjectV2ItemField" + kind + "Value", "id": "V" + f["id"] + identifier,
             "createdAt": TIME, "updatedAt": TIME, "item": {"id": identifier}, "field": {"id": f["id"]}}
    value.update({"Text": {"text": ""}, "Number": {"number": 0}, "Date": {"date": "2026-10-23"},
                  "SingleSelect": {"optionId": "O1", "name": "One"},
                  "MultiSelect": {"options": [{"id": "O1", "name": "One"}, {"id": "O2", "name": "Two"}]},
                  "Iteration": {"iterationId": "OLD", "title": "Past", "startDate": "2026-10-01", "duration": 7}}[kind])
    value.update(override)
    if f["isIssueField"]:
        value["__typename"] = "IssueField" + kind + "Value"
        value["field"] = {"id": f["issueField"]["id"]}
        return {"__typename": "ProjectV2ItemIssueFieldValue", "field": {"id": f["id"]}, "issueFieldValue": value}
    return value


class Fixture:
    def __init__(self):
        self.fields = [field(k) for k in P.SCALARS]
        self.fields += [field(k, "Org", True) for k in P.SCALARS if k != "Iteration"]
        self.fields += [field(k) for k in list(P.RELATIONS) + list(P.SINGULAR)]
        self.fields += [field("Text", "Unset")]
        self.items = [item(), item("I2", "DRAFT_ISSUE"), item("I3", external=True, archived=True),
                      item("I4", "REDACTED"), item("I5", "PULL_REQUEST")]
        self.values = {i["id"]: [] for i in self.items}
        self.values["I1"] = [scalar(f, k) for f in self.fields for k in P.SCALARS
                             if f["id"] == "F" + k or f["id"] == "F" + k + "Org"]
        self.relationships = {}
        for kind in list(P.RELATIONS) + list(P.SINGULAR):
            f = next(f for f in self.fields if f["id"] == "F" + kind)
            self.values["I1"].append({"__typename": "ProjectV2ItemField" + kind + "Value", "field": {"id": f["id"]}})
            self.relationships[f["name"]] = [{"id": kind + "1", "url": "https://github.com/fixture"},
                                              {"id": kind + "2", "url": "https://github.com/fixture2"}]
        self.requests = []
        self.hook = lambda query, variables, data: data

    def connection(self, records, cursor):
        offset = 0 if cursor is None else int(cursor)
        page = copy.deepcopy(records[offset:offset + 2])
        end = offset + len(page)
        return {"nodes": page, "totalCount": len(records),
                "pageInfo": {"hasNextPage": end < len(records), "endCursor": str(end) if page else None}}

    def __call__(self, query, variables):
        self.requests.append((query, copy.deepcopy(variables)))
        cursor = variables.get("cursor")
        if "projectV2(number:" in query:
            kind = "user" if "user(login:" in query else "organization"
            data = {kind: {"id": "OWNER", "login": "fixture", "__typename": kind.title(),
                           "projectV2": {"id": "P", "number": 1, "url": "https://github.com/orgs/fixture/projects/1",
                                         "title": "Fixture", "updatedAt": TIME}},
                    "viewer": {"id": "VIEWER", "login": "reader"}}
        elif "fieldValueByName" in query:
            f = next(f for f in self.fields if f["name"] == variables["name"])
            kind = next(k for k in list(P.RELATIONS) + list(P.SINGULAR) if f["id"] == "F" + k)
            value = {"__typename": "ProjectV2ItemField" + kind + "Value", "field": {"id": f["id"]}}
            if kind in P.RELATIONS:
                value[P.RELATIONS[kind][1]] = self.connection(self.relationships[f["name"]], cursor)
            else:
                value[P.SINGULAR[kind][1]] = copy.deepcopy(self.relationships[f["name"]][0])
            data = {"node": {"__typename": "ProjectV2Item", "id": variables["id"], "fieldValueByName": value}}
        else:
            if "fieldValues(first:" in query:
                name, records, typ = "fieldValues", self.values[variables["id"]], "ProjectV2Item"
            elif "fields(first:" in query:
                name, records, typ = "fields", self.fields, "ProjectV2"
            elif "items(first:" in query:
                name, records, typ = "items", self.items, "ProjectV2"
            elif "views(first:" in query:
                name, records, typ = "views", [{"id": "VIEW", "number": 1, "name": "Board", "layout": "BOARD_LAYOUT"}], "ProjectV2"
            else:
                raise AssertionError("Unexpected query")
            data = {"node": {"__typename": typ, "id": variables["id"], name: self.connection(records, cursor)}}
        return self.hook(query, variables, {"data": data})


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.fixture = Fixture()

    def collect(self):
        return P.collect("organization", "fixture", 1, REPO, self.fixture)

    def test_typed_multipage_matrix_and_offline_replay(self):
        out = self.collect()
        with patch.object(P, "gh_query", side_effect=AssertionError("network")):
            P.verify(out, "organization", "fixture", 1, REPO)
        values = out["project-values.json"]
        self.assertEqual(len(values), len(self.fixture.fields) * len(self.fixture.items))
        zero = next(v for v in values if v["item_id"] == "I1" and v["field_id"] == "FNumber")
        self.assertEqual(zero["value"], 0)
        empty = next(v for v in values if v["item_id"] == "I1" and v["field_id"] == "FText")
        self.assertEqual(empty["value"], "")
        self.assertEqual({i["content_disposition"] for i in out["project-items.json"]},
                         {"local", "draft", "external", "inaccessible-redacted"})
        self.assertTrue(out["project-items.json"][2]["isArchived"])
        self.assertTrue(any(v["disposition"] == "inapplicable" for v in values))
        self.assertTrue(any(v["disposition"] == "observed-unset" for v in values))
        self.assertTrue(any(v["disposition"] == "inaccessible-redacted" for v in values))
        self.assertEqual(sum(v.get("origin") == "organization-issue-field" for v in values), 5)
        observations = out["project-coverage.json"]["observations"]
        self.assertTrue(any(o["target"] == ["values", "I1"] and len(o["pages"]) > 1 for o in observations))
        self.assertTrue(any(o["target"] == ["items", "P"] and len(o["pages"]) > 1 for o in observations))

    def test_nested_relationship_own_cursor(self):
        self.fixture.relationships["Label"] += [{"id": "L3"}]
        out = self.collect()
        P.verify(out, "organization", "fixture", 1, REPO)
        labels = next(v for v in out["project-values.json"] if v["item_id"] == "I1" and v["field_id"] == "FLabel")
        self.assertEqual(len(labels["value"]), 3)
        self.assertTrue(any(v.get("cursor") == "2" and v.get("name") == "Label" for _, v in self.fixture.requests))

    def test_null_is_present_and_not_unset(self):
        self.fixture.values["I1"][0]["text"] = None
        out = self.collect()
        value = next(v for v in out["project-values.json"] if v["item_id"] == "I1" and v["field_id"] == "FText")
        self.assertEqual(value["disposition"], "present")
        self.assertIsNone(value["value"])

    def test_user_project_and_complete_empty(self):
        self.fixture.fields, self.fixture.items = [], []
        out = P.collect("user", "fixture", 1, REPO, self.fixture)
        P.verify(out, "user", "fixture", 1, REPO)
        self.assertEqual(out["project-values.json"], [])

    def test_required_failure_controls(self):
        def unknown_type(f):
            f.values["I1"][0]["__typename"] = "NewProviderType"
        def missing_option(f):
            next(v for v in f.values["I1"] if v.get("optionId"))["optionId"] = "missing"
        def foreign_field(f):
            f.values["I1"][0]["field"]["id"] = "foreign"
        def foreign_item(f):
            f.values["I1"][0]["item"]["id"] = "foreign"
        def conflicting_duplicate(f):
            f.values["I1"].append(dict(f.values["I1"][0], text="changed"))
        def bad_number(f):
            next(v for v in f.values["I1"] if "number" in v)["number"] = True
        def unknown_wrapper(f):
            next(v for v in f.values["I1"] if "issueFieldValue" in v)["issueFieldValue"]["__typename"] = "NewIssueValue"
        def missing_iteration(f):
            next(v for v in f.values["I1"] if "iterationId" in v)["iterationId"] = "absent"
        for mutate in (unknown_type, missing_option, foreign_field, foreign_item, conflicting_duplicate,
                       bad_number, unknown_wrapper, missing_iteration):
            with self.subTest(mutate=mutate.__name__):
                self.fixture = Fixture()
                mutate(self.fixture)
                with self.assertRaises(P.ProjectError):
                    self.collect()

    def test_partial_graphql_data_never_becomes_empty_success(self):
        self.fixture.hook = lambda q, v, data: dict(data, errors=[{"message": "denied"}])
        with self.assertRaises(P.ProjectError):
            self.collect()

    def test_value_pagination_failure_after_items_finished(self):
        def hook(q, v, response):
            if "fieldValues(first:" in q and v.get("cursor") == "2":
                response["data"]["node"]["fieldValues"]["pageInfo"]["endCursor"] = "2"
            return response
        self.fixture.hook = hook
        with self.assertRaisesRegex(P.ProjectError, "Nonadvancing"):
            self.collect()

    def test_denied_nested_connection_fails(self):
        def hook(q, v, response):
            if "fieldValueByName" in q and v.get("name") == "Label":
                response["data"]["node"]["fieldValueByName"]["labels"] = None
            return response
        self.fixture.hook = hook
        with self.assertRaises(P.ProjectError):
            self.collect()

    def test_project_drift_fails(self):
        reads = 0
        def hook(q, v, response):
            nonlocal reads
            if "projectV2(number:" in q:
                reads += 1
                if reads > 1:
                    response["data"]["organization"]["projectV2"]["updatedAt"] = "changed"
            return response
        self.fixture.hook = hook
        with self.assertRaisesRegex(P.ProjectError, "changed"):
            self.collect()

    def test_offline_corruption_controls(self):
        original = self.collect()
        for mutate in (
            lambda o: o["project-values.json"].pop(),
            lambda o: o["project-requests.json"].pop(),
            lambda o: o["project-coverage.json"]["observations"].pop(),
            lambda o: o["project-values.json"][0].update(value="forged"),
            lambda o: o["project-coverage.json"].update(evidence_schema_version="999.0.0"),
        ):
            with self.subTest(mutation=mutate):
                out = copy.deepcopy(original)
                mutate(out)
                with self.assertRaises(P.ProjectError):
                    P.verify(out, "organization", "fixture", 1, REPO)

    def test_publish_permissions_no_overwrite_and_cli_verify(self):
        out = self.collect()
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "github"
            P.publish(out, destination)
            self.assertEqual((destination / "project-values.json").stat().st_mode & 0o777, 0o600)
            with self.assertRaises(P.ProjectError):
                P.publish(out, destination)
            result = subprocess.run([sys.executable, str(Path(P.__file__)), "verify", "--owner", "fixture",
                                     "--number", "1", "--repository", REPO, "--destination", str(destination)],
                                    capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_transport_sanitizes_failure(self):
        with patch.object(P.subprocess, "run", return_value=subprocess.CompletedProcess([], 1, b"secret", b"secret")):
            with self.assertRaises(P.ProjectError) as caught:
                P.gh_query("query($id:ID!){node(id:$id){id}}", {"id": "P"})
            self.assertNotIn("secret", str(caught.exception))

    def test_bash_and_cli_collect_with_synthetic_gh(self):
        out = self.collect()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            binary = root / "bin"
            binary.mkdir()
            requests = root / "requests.json"
            requests.write_text(json.dumps(out["project-requests.json"]))
            counter = root / "counter"
            gh = binary / "gh"
            gh.write_text("#!" + sys.executable + "\n" + '''import hashlib,json,os,sys
from pathlib import Path
assert sys.argv[1:] == ['api','--hostname','github.com','graphql','--input','-']
request=json.load(sys.stdin)
counter=Path(os.environ['FIXTURE_COUNTER'])
index=int(counter.read_text()) if counter.exists() else 0
records=json.load(open(os.environ['FIXTURE_REQUESTS']))
record=records[index]
assert record['query_sha256']==hashlib.sha256(request['query'].encode()).hexdigest()
assert record['variables']==request['variables']
counter.write_text(str(index+1))
print(json.dumps(record['response']))
''')
            gh.chmod(0o700)
            destination = root / "github"
            destination.mkdir()
            exporter = Path(__file__).with_name("export-audit.sh").resolve()
            command = '''source "$1"
OWNER=fixture
REPOSITORY=repo
PROJECT_OWNER_KIND=organization
PROJECT_OWNER=fixture
PROJECT_NUMBER=1
EXPORT_DIR="$2"
export_project_evidence
verify_project_evidence
'''
            result = subprocess.run(["bash", "-euo", "pipefail", "-c", command, "fixture",
                                     str(exporter), str(root)], capture_output=True,
                                    env=dict(os.environ, PATH=str(binary) + os.pathsep + os.environ["PATH"],
                                             FIXTURE_REQUESTS=str(requests), FIXTURE_COUNTER=str(counter)))
            self.assertEqual(result.returncode, 0, result.stderr.decode())
            self.assertEqual(int(counter.read_text()), len(out["project-requests.json"]))
            self.assertEqual(json.loads((destination / "project-values.json").read_text()), out["project-values.json"])

    def test_connection_failure_controls(self):
        for failure in ("node", "count", "null", "terminal", "owner"):
            with self.subTest(failure=failure):
                self.fixture = Fixture()
                def hook(q, v, response):
                    if failure == "owner" and "projectV2(number:" in q:
                        response["data"]["organization"] = None
                    if "fieldValues(first:" in q and v["id"] == "I1":
                        node = response["data"]["node"]
                        if failure == "node":
                            node["id"] = "foreign"
                        elif failure == "count":
                            node["fieldValues"]["totalCount"] += 1 if v.get("cursor") else 0
                        elif failure == "null":
                            node["fieldValues"]["nodes"] = [None]
                        elif failure == "terminal":
                            node["fieldValues"]["pageInfo"].pop("hasNextPage")
                    return response
                self.fixture.hook = hook
                with self.assertRaises(P.ProjectError):
                    self.collect()


if __name__ == "__main__":
    unittest.main()
