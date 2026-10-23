#!/usr/bin/env python3
"""Read-only, typed Project evidence with independent connection traversal."""

import argparse
import copy
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

PAGE = "pageInfo { hasNextPage endCursor } totalCount"
FIELD_REF = "field { ... on ProjectV2FieldCommon { id } }"
COMMON = "id createdAt updatedAt item { id } " + FIELD_REF
ISSUE_FIELD = """issueField {
 __typename ... on IssueFieldCommon { id name dataType }
 ... on IssueFieldSingleSelect { options { id name } }
 ... on IssueFieldMultiSelect { options { id name } }
}"""
FIELDS = """__typename ... on ProjectV2FieldCommon { id name dataType isIssueField }
... on ProjectV2Field { """ + ISSUE_FIELD + """ }
... on ProjectV2SingleSelectField { options { id name color description } """ + ISSUE_FIELD + """ }
... on ProjectV2MultiSelectField { multiSelectOptions { id name color description } """ + ISSUE_FIELD + """ }
... on ProjectV2IterationField {
 configuration { duration startDay
 iterations { id title startDate duration }
 completedIterations { id title startDate duration } }
}"""
ITEMS = """id type isArchived createdAt updatedAt project { id }
content { __typename
 ... on Issue { id number url repository { id nameWithOwner url } }
 ... on PullRequest { id number url repository { id nameWithOwner url } }
 ... on DraftIssue { id }
}"""
SCALARS = {
    "Text": ("TEXT", "text"),
    "Number": ("NUMBER", "number"),
    "Date": ("DATE", "date"),
    "SingleSelect": ("SINGLE_SELECT", "optionId name"),
    "MultiSelect": ("MULTI_SELECT", "options { id name }"),
    "Iteration": ("ITERATION", "iterationId title startDate duration"),
}
RELATIONS = {
    "Label": ("LABELS", "labels", "id name url"),
    "User": ("ASSIGNEES", "users", "id login url"),
    "PullRequest": ("LINKED_PULL_REQUESTS", "pullRequests", "id number url repository { id nameWithOwner url }"),
    "Reviewer": ("REVIEWERS", "reviewers", "__typename ... on User { id login url } ... on Team { id name url } ... on Mannequin { id login url }"),
}
SINGULAR = {
    "Repository": ("REPOSITORY", "repository", "id nameWithOwner url"),
    "Milestone": ("MILESTONE", "milestone", "id number title url"),
}
REVIEWER_SELECTIONS = {
    "1.0.0": RELATIONS["Reviewer"][2],
    "1.1.0": ("__typename ... on User { id login url } ... on Bot { id login url } "
              "... on Team { id name url } ... on Mannequin { id login url } "
              "... on EnterpriseTeam { id name slug }"),
}
REVIEWER_TYPES = {
    "1.0.0": {"User", "Team", "Mannequin"},
    "1.1.0": {"User", "Bot", "Team", "Mannequin", "EnterpriseTeam"},
}
REVIEWER_SELECTIONS["1.2.0"] = REVIEWER_SELECTIONS["1.1.0"]
REVIEWER_TYPES["1.2.0"] = REVIEWER_TYPES["1.1.0"]
REVIEWER_SELECTIONS["1.3.0"] = REVIEWER_SELECTIONS["1.2.0"]
REVIEWER_TYPES["1.3.0"] = REVIEWER_TYPES["1.2.0"]
SUPPORTED = {"TEXT", "TITLE", "NUMBER", "DATE", "SINGLE_SELECT", "MULTI_SELECT", "ITERATION",
             "LABELS", "ASSIGNEES", "LINKED_PULL_REQUESTS", "REVIEWERS", "REPOSITORY", "MILESTONE"}
VALUES = "__typename\n"
for kind, (_, selection) in SCALARS.items():
    VALUES += "... on ProjectV2ItemField" + kind + "Value { " + COMMON + " " + selection + " }\n"
for kind in list(RELATIONS) + list(SINGULAR):
    VALUES += "... on ProjectV2ItemField" + kind + "Value { " + FIELD_REF + " }\n"
VALUES += "... on ProjectV2ItemIssueFieldValue { " + FIELD_REF + """ issueFieldValue {
 __typename
 ... on IssueFieldValueCommon { field { ... on IssueFieldCommon { id } } }
 ... on IssueFieldTextValue { id text: value }
 ... on IssueFieldNumberValue { id number: value }
 ... on IssueFieldDateValue { id date: value }
 ... on IssueFieldSingleSelectValue { id optionId name }
 ... on IssueFieldMultiSelectValue { id options { id name } }
} }"""
# IssueFieldCommon exposes metadata, not Node.id. Keep historical query bytes
# for transcript replay; new reads select identity through the Node interface.
FIELD_SELECTIONS = {version: FIELDS for version in ("1.0.0", "1.1.0")}
FIELD_SELECTIONS["1.2.0"] = FIELDS.replace(
    "... on IssueFieldCommon { id name dataType }",
    "... on Node { id } ... on IssueFieldCommon { name dataType }")
VALUE_SELECTIONS = {version: VALUES for version in ("1.0.0", "1.1.0")}
VALUE_SELECTIONS["1.2.0"] = VALUES.replace(
    "... on IssueFieldCommon { id }", "... on Node { id }")
FIELD_SELECTIONS["1.3.0"] = FIELD_SELECTIONS["1.2.0"]
VALUE_SELECTIONS["1.3.0"] = VALUE_SELECTIONS["1.2.0"]
BUILTINS = {"CREATED", "UPDATED", "CLOSED", "PARENT_ISSUE", "SUB_ISSUES_PROGRESS"}
OUTPUTS = ("project-items.json", "project-fields.json", "project-values.json", "project-coverage.json",
           "project-requests.json", "project-views.json")


class ProjectError(Exception):
    """A failure whose message does not include provider bodies or credentials."""


def now():
    return datetime.now(timezone.utc).isoformat()


def require(condition, message):
    if not condition:
        raise ProjectError(message)


def identity(value):
    require(isinstance(value, str) and bool(value), "Missing provider identity.")
    return value


def fingerprint(query):
    return hashlib.sha256(query.encode()).hexdigest()


def json_load(data):
    def invalid(_):
        raise ValueError("Non-JSON constant")
    try:
        return json.loads(data, parse_constant=invalid)
    except (ValueError, UnicodeError) as exc:
        raise ProjectError("Malformed JSON evidence.") from exc


def gh_query(query, variables):
    require(query.lstrip().startswith("query("), "Only declared read queries are permitted.")
    env = dict(os.environ, GH_PROMPT_DISABLED="1")
    env.pop("GH_DEBUG", None)
    request = json.dumps({"query": query, "variables": variables}, allow_nan=False)
    try:
        result = subprocess.run(
            ["gh", "api", "--hostname", "github.com", "graphql", "--input", "-"],
            input=request.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=env, timeout=120, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ProjectError("Project transport unavailable or timed out.") from exc
    require(result.returncode == 0, "Required Project request failed; body omitted.")
    return json_load(result.stdout)


class Client:
    def __init__(self, transport=gh_query):
        self.transport = transport
        self.observations = []
        self.requests = []

    def read(self, query, variables):
        response = self.transport(query, variables)
        require(isinstance(response, dict) and not response.get("errors"),
                "GraphQL errors or malformed response; partial data is unusable.")
        data = response.get("data")
        require(isinstance(data, dict), "Required GraphQL data unavailable.")
        self.requests.append({"query_sha256": fingerprint(query), "variables": copy.deepcopy(variables),
                              "response": copy.deepcopy(response)})
        return data

    def traverse(self, query, variables, resolve, key, target):
        cursor, seen_cursors, records, pages = None, set(), {}, []
        started, total = now(), None
        for _ in range(10000):
            data = self.read(query, dict(variables, cursor=cursor))
            connection = resolve(data)
            require(isinstance(connection, dict), "Required connection inaccessible.")
            nodes, info, count = connection.get("nodes"), connection.get("pageInfo"), connection.get("totalCount")
            require(isinstance(nodes, list) and isinstance(info, dict), "Malformed connection.")
            require(isinstance(count, int) and not isinstance(count, bool) and count >= 0,
                    "Missing connection count.")
            require(total is None or total == count, "Connection count changed during traversal.")
            total = count
            for node in nodes:
                require(isinstance(node, dict), "Null/redacted required connection node.")
                provider_key = identity(key(node))
                require(provider_key not in records or records[provider_key] == node,
                        "Conflicting duplicate provider identity.")
                records[provider_key] = node
            more, end = info.get("hasNextPage"), info.get("endCursor")
            require(isinstance(more, bool), "Missing terminal pagination evidence.")
            require(end is None or isinstance(end, str), "Invalid connection cursor.")
            pages.append({"after": cursor, "end_cursor": end, "has_next_page": more,
                          "returned_count": len(nodes), "total_count": count, "observed_at": now()})
            if not more:
                break
            require(bool(nodes) and bool(end) and end != cursor and end not in seen_cursors,
                    "Nonadvancing connection cursor.")
            seen_cursors.add(end)
            cursor = end
        else:
            raise ProjectError("Project pagination resource limit reached.")
        require(len(records) == total, "Connection count does not match retained unique identities.")
        observation = {"target": target, "query_sha256": fingerprint(query), "started_at": started,
                       "ended_at": now(), "pages": pages, "status": "complete",
                       "raw_count": sum(p["returned_count"] for p in pages), "retained_count": len(records)}
        self.observations.append(observation)
        return list(records.values())


def node_connection(data, node_id, kind, connection):
    node = data.get("node")
    require(isinstance(node, dict) and node.get("id") == node_id and node.get("__typename") == kind,
            "Required node inaccessible or identity/type changed.")
    return node.get(connection)


def project_query(connection, selection):
    return ("query($id:ID!,$cursor:String){ node(id:$id) { __typename id ... on ProjectV2 { "
            + connection + "(first:100,after:$cursor){ nodes { " + selection + " } " + PAGE + " } } } }")


def value_key(value):
    field = value.get("field")
    require(isinstance(field, dict), "Missing value field reference.")
    return identity(field.get("id"))


def field_options(field):
    if field.get("isIssueField"):
        source = field.get("issueField")
        require(isinstance(source, dict), "Required organization issue-field definition inaccessible.")
        return source.get("options", [])
    return field.get("options", field.get("multiSelectOptions", []))


def validate_fields(fields, evidence_version="1.3.0"):
    supported = SUPPORTED | (BUILTINS if evidence_version == "1.3.0" else set())
    builtin_types = set()
    for field in fields:
        identity(field.get("id"))
        require(isinstance(field.get("name"), str) and isinstance(field.get("isIssueField"), bool),
                "Malformed field definition.")
        require(field.get("__typename") in {"ProjectV2Field", "ProjectV2SingleSelectField",
                                           "ProjectV2MultiSelectField", "ProjectV2IterationField"},
                "Unsupported Project field type.")
        require(field.get("dataType") in supported, "Unsupported required field data type.")
        if field["dataType"] in BUILTINS:
            require(field["dataType"] not in builtin_types, "Duplicate built-in field type.")
            builtin_types.add(field["dataType"])
        specific = {"SINGLE_SELECT": "ProjectV2SingleSelectField", "MULTI_SELECT": "ProjectV2MultiSelectField",
                    "ITERATION": "ProjectV2IterationField"}
        require(field["__typename"] == specific.get(field["dataType"], "ProjectV2Field"),
                "Field type differs from data type.")
        if field["isIssueField"]:
            source = field.get("issueField")
            require(isinstance(source, dict), "Organization issue field inaccessible.")
            identity(source.get("id"))
            expected = {"TEXT": "Text", "NUMBER": "Number", "DATE": "Date",
                        "SINGLE_SELECT": "SingleSelect", "MULTI_SELECT": "MultiSelect"}
            require(source.get("__typename") == "IssueField" + expected.get(field["dataType"], "?"),
                    "Unsupported organization issue-field definition.")
            require(source.get("dataType") == field["dataType"], "Issue-field data type mismatch.")
        if field["dataType"] in {"SINGLE_SELECT", "MULTI_SELECT"}:
            options = field_options(field)
            require(isinstance(options, list), "Missing option definitions.")
            ids = [identity(o.get("id")) for o in options]
            require(len(set(ids)) == len(ids), "Duplicate option definition.")
        if field["dataType"] == "ITERATION":
            config = field.get("configuration")
            require(isinstance(config, dict), "Missing iteration configuration.")
            iterations = config.get("iterations"), config.get("completedIterations")
            require(all(isinstance(v, list) for v in iterations), "Missing completed/current iterations.")
            ids = [identity(o.get("id")) for group in iterations for o in group]
            require(len(set(ids)) == len(ids), "Duplicate iteration identity.")


def scalar_payload(raw, field, item_id):
    typename = raw.get("__typename")
    origin = "project-custom-or-built-in"
    value = raw
    if typename == "ProjectV2ItemIssueFieldValue":
        require(field["isIssueField"], "Issue-field wrapper references a custom field.")
        value = raw.get("issueFieldValue")
        require(isinstance(value, dict), "Organization issue-field value inaccessible.")
        source_field = value.get("field")
        require(isinstance(source_field, dict) and source_field.get("id") == field["issueField"]["id"],
                "Organization value references missing/foreign issue field.")
        origin = "organization-issue-field"
        prefix = "IssueField"
    else:
        require(not field["isIssueField"], "Organization issue field lacks required wrapper.")
        require(raw.get("item", {}).get("id") == item_id, "Value references foreign item.")
        require(all(isinstance(raw.get(k), str) for k in ("createdAt", "updatedAt")),
                "Missing scalar observation timestamps.")
        prefix = "ProjectV2ItemField"
    identity(value.get("id"))
    kind = next((k for k in SCALARS if value.get("__typename") == prefix + k + "Value"), None)
    require(kind is not None, "Unsupported required scalar or issue-field value.")
    expected, _ = SCALARS[kind]
    require(field["dataType"] == expected or (expected == "TEXT" and field["dataType"] == "TITLE"),
            "Value type differs from field definition.")
    if kind in {"Text", "Number", "Date"}:
        key = kind.lower()
        require(key in value, "Missing scalar payload.")
        payload = value[key]
        if payload is not None:
            if kind == "Number":
                require(isinstance(payload, (int, float)) and not isinstance(payload, bool)
                        and math.isfinite(payload), "Invalid numeric value.")
            else:
                require(isinstance(payload, str), "Invalid string/date payload.")
                if kind == "Date":
                    from datetime import date
                    require(date.fromisoformat(payload).isoformat() == payload, "Invalid date value.")
    elif kind in {"SingleSelect", "MultiSelect"}:
        if kind == "SingleSelect":
            require("optionId" in value and isinstance(value.get("name"), str),
                    "Missing single-select payload.")
            selected = [{"id": value["optionId"], "name": value["name"]}]
        else:
            selected = value.get("options")
            require(isinstance(selected, list), "Missing multi-select payload.")
        options = {o["id"]: o for o in field_options(field)}
        selected_ids = [identity(o.get("id")) for o in selected]
        require(len(selected_ids) == len(set(selected_ids)), "Duplicate selected option.")
        require(all(o["id"] in options and o.get("name") == options[o["id"]].get("name") for o in selected),
                "Selected option missing or changed in field definition.")
        payload = selected
    else:
        config = field["configuration"]
        options = {o["id"]: o for o in config["iterations"] + config["completedIterations"]}
        option = options.get(value.get("iterationId"))
        require(option is not None, "Referenced iteration missing.")
        require(all(value.get(k) == option.get(k) for k in ("title", "startDate", "duration")),
                "Referenced iteration changed.")
        payload = {k: value[k] for k in ("iterationId", "title", "startDate", "duration")}
    return {"provider_type": typename, "value_type": value["__typename"],
            "value_id": value["id"], "origin": origin, "value": payload,
            "raw_value": raw,
            "created_at": value.get("createdAt"), "updated_at": value.get("updatedAt")}


def relationship(client, item, field, kind, evidence_version):
    config = RELATIONS.get(kind, SINGULAR.get(kind))
    _, name, selection = config
    if kind == "Reviewer":
        selection = REVIEWER_SELECTIONS[evidence_version]
    value_type = "ProjectV2ItemField" + kind + "Value"
    if kind in RELATIONS:
        query = ("query($id:ID!,$name:String!,$cursor:String){ node(id:$id){ __typename id "
                 "... on ProjectV2Item { fieldValueByName(name:$name){ __typename ... on "
                 + value_type + "{ " + FIELD_REF + " " + name + "(first:100,after:$cursor){nodes { "
                 + selection + " } " + PAGE + "} } } } } }")
    else:
        query = ("query($id:ID!,$name:String!){ node(id:$id){ __typename id ... on ProjectV2Item { "
                 "fieldValueByName(name:$name){ __typename ... on " + value_type + "{ "
                 + FIELD_REF + " " + name + "{ " + selection + " } } } } } }")

    def resolve(data):
        value = node_connection(data, item["id"], "ProjectV2Item", "fieldValueByName")
        require(isinstance(value, dict) and value.get("__typename") == value_type
                and value_key(value) == field["id"], "Relationship changed or field name is ambiguous.")
        return value.get(name)

    variables = {"id": item["id"], "name": field["name"]}
    if kind in RELATIONS:
        payload = client.traverse(query, variables, resolve, lambda v: v.get("id"),
                                  ["relationship", item["id"], field["id"]])
        if kind == "Reviewer":
            require(all(v.get("__typename") in REVIEWER_TYPES[evidence_version] for v in payload),
                    "Unsupported required reviewer actor type.")
    else:
        payload = resolve(client.read(query, variables))
        require(payload is not None, "Required relationship inaccessible.")
        identity(payload.get("id"))
        client.observations.append({"target": ["relationship", item["id"], field["id"]],
                                    "query_sha256": fingerprint(query), "started_at": now(),
                                    "ended_at": now(), "status": "complete", "singular": True,
                                    "raw_count": 1, "retained_count": 1})
    return {"provider_type": value_type, "origin": "built-in-relationship",
            "value_type": config[0], "value": payload, "value_id": None}


def normalize_item(raw, project_id, repository):
    require(raw.get("project", {}).get("id") == project_id, "Foreign Project item.")
    require(isinstance(raw.get("isArchived"), bool), "Missing item archive state.")
    require(raw.get("type") in {"ISSUE", "PULL_REQUEST", "DRAFT_ISSUE", "REDACTED"},
            "Unknown Project item kind.")
    result = dict(raw)
    content = raw.get("content")
    if raw["type"] == "REDACTED" or content is None:
        result["content"] = None
        result["content_disposition"] = "inaccessible-redacted"
    else:
        require(isinstance(content, dict), "Invalid item content.")
        identity(content.get("id"))
        require(content.get("__typename") == {"ISSUE": "Issue", "PULL_REQUEST": "PullRequest",
                                              "DRAFT_ISSUE": "DraftIssue"}.get(raw["type"]),
                "Item/content kind mismatch.")
        if raw["type"] == "DRAFT_ISSUE":
            result["content_disposition"] = "draft"
        else:
            repo = content.get("repository")
            require(isinstance(repo, dict), "Linked repository identity inaccessible.")
            identity(repo.get("id"))
            require(isinstance(repo.get("nameWithOwner"), str), "Missing linked repository name.")
            result["content_disposition"] = "local" if repo["nameWithOwner"].casefold() == repository.casefold() else "external"
    return result


def item_selection(fields, evidence_version):
    """Observe computed metadata separately from the direct Project value API."""
    selected = [f for f in fields if f["dataType"] in BUILTINS]
    if evidence_version != "1.3.0" or not selected:
        return ITEMS
    kinds = {f["dataType"] for f in selected}
    dates = " ".join(name for kind, name in (("CREATED", "createdAt"), ("UPDATED", "updatedAt"),
                                             ("CLOSED", "closedAt")) if kind in kinds)
    draft_dates = " ".join(name for kind, name in (("CREATED", "createdAt"), ("UPDATED", "updatedAt"))
                           if kind in kinds)
    hierarchy = ""
    if "PARENT_ISSUE" in kinds:
        hierarchy += "parent { id number url repository { id nameWithOwner url } } "
    if "SUB_ISSUES_PROGRESS" in kinds:
        hierarchy += "subIssuesSummary { total completed percentCompleted } "
    selection = ITEMS.replace("... on Issue {", "... on Issue { " + dates + " " + hierarchy)
    selection = selection.replace("... on PullRequest {", "... on PullRequest { " + dates + " ")
    selection = selection.replace("... on DraftIssue {", "... on DraftIssue { " + draft_dates + " ")
    for field in selected:
        selection += (" builtin_" + field["dataType"] + ": fieldValueByName(name:"
                      + json.dumps(field["name"], ensure_ascii=True) + "){ __typename }")
    return selection


def timestamp(value):
    require(isinstance(value, str), "Missing built-in timestamp.")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ProjectError("Invalid built-in timestamp.") from exc
    require(parsed.tzinfo is not None, "Built-in timestamp lacks timezone.")
    return value


def builtin_payload(item, field, raw, repository):
    kind = field["dataType"]
    alias = "builtin_" + kind
    require(alias in item and item[alias] is None and raw is None,
            "Built-in Project value API changed; review the new provider representation.")
    result = {"provider_type": "ProjectV2Item", "value_type": kind,
              "value_id": None, "origin": "built-in-provider-metadata",
              "direct_project_value": None, "display_value_reconstructed": False}
    content = item["content"]
    if content is None:
        return dict(result, disposition="inaccessible-redacted", value=None, source_paths=[])
    if kind in {"PARENT_ISSUE", "SUB_ISSUES_PROGRESS", "CLOSED"} and (
            item["type"] == "DRAFT_ISSUE" or (kind != "CLOSED" and item["type"] != "ISSUE")):
        return dict(result, disposition="inapplicable", value=None, source_paths=[])
    if kind in {"CREATED", "UPDATED"}:
        name = "createdAt" if kind == "CREATED" else "updatedAt"
        require(name in content, "Missing linked-content timestamp.")
        # Project-item and linked-content times can differ (e.g. draft conversion).
        # Retain both with provenance, never guess the UI's computed display value.
        value = {"project_item": timestamp(item.get(name)), "content": timestamp(content[name])}
        paths = ["ProjectV2Item." + name, content["__typename"] + "." + name]
    elif kind == "CLOSED":
        require("closedAt" in content, "Missing linked-content closure observation.")
        value = content["closedAt"]
        if value is not None:
            timestamp(value)
        paths = [content["__typename"] + ".closedAt"]
    elif kind == "PARENT_ISSUE":
        require("parent" in content, "Missing parent-issue observation.")
        value = content["parent"]
        if value is not None:
            require(isinstance(value, dict), "Malformed parent-issue reference.")
            identity(value.get("id"))
            require(isinstance(value.get("number"), int) and not isinstance(value["number"], bool)
                    and value["number"] > 0 and isinstance(value.get("url"), str),
                    "Invalid parent-issue reference.")
            repo = value.get("repository")
            require(isinstance(repo, dict), "Missing parent repository reference.")
            identity(repo.get("id"))
            require(all(isinstance(repo.get(k), str) and repo[k] for k in ("nameWithOwner", "url")),
                    "Invalid parent repository reference.")
            result["reference_scope"] = "local" if repo["nameWithOwner"].casefold() == repository.casefold() else "external"
        paths = ["Issue.parent"]
    else:
        require("subIssuesSummary" in content and isinstance(content["subIssuesSummary"], dict),
                "Missing sub-issues summary observation.")
        value = content["subIssuesSummary"]
        require(all(isinstance(value.get(k), int) and not isinstance(value[k], bool)
                    for k in ("total", "completed", "percentCompleted")), "Invalid sub-issues summary counts.")
        require(0 <= value["completed"] <= value["total"] and 0 <= value["percentCompleted"] <= 100
                and (value["total"] != 0 or value["percentCompleted"] == 0),
                "Inconsistent sub-issues summary counts.")
        paths = ["Issue.subIssuesSummary"]
    return dict(result, disposition="present", value=value, source_paths=paths)


def collect(owner_kind, owner, number, repository, transport=gh_query, evidence_version="1.3.0"):
    require(evidence_version in REVIEWER_SELECTIONS, "Unsupported Project evidence version.")
    require(owner_kind in {"organization", "user"} and re.fullmatch(r"[A-Za-z0-9-]+", owner),
            "Invalid selected Project owner.")
    require(isinstance(number, int) and number > 0 and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository),
            "Invalid selected Project number/repository.")
    client = Client(transport)
    started = now()
    query = ("query($login:String!,$number:Int!){ " + owner_kind
             + "(login:$login){ __typename id login projectV2(number:$number){ id number url title updatedAt } } "
             + "viewer { id login } }")
    data = client.read(query, {"login": owner, "number": number})
    actor = data.get(owner_kind)
    require(isinstance(actor, dict) and str(actor.get("login", "")).casefold() == owner.casefold()
            and actor.get("__typename") == owner_kind.title(), "Project owner inaccessible/mismatched.")
    identity(actor.get("id"))
    project = actor.get("projectV2")
    require(isinstance(project, dict) and project.get("number") == number, "Project inaccessible/mismatched.")
    project_id = identity(project.get("id"))
    principal = data.get("viewer")
    require(isinstance(principal, dict), "Missing observation principal.")
    identity(principal.get("id"))
    identity(principal.get("login"))
    require(isinstance(project.get("url"), str), "Missing Project URL.")
    project = dict(project, owner_kind=owner_kind, owner_login=actor["login"], owner_id=actor["id"])
    fields = client.traverse(project_query("fields", FIELD_SELECTIONS[evidence_version]), {"id": project_id},
                             lambda d: node_connection(d, project_id, "ProjectV2", "fields"),
                             lambda f: f.get("id"), ["fields", project_id])
    validate_fields(fields, evidence_version)
    selected_items = item_selection(fields, evidence_version)
    raw_items = client.traverse(project_query("items", selected_items), {"id": project_id},
                                lambda d: node_connection(d, project_id, "ProjectV2", "items"),
                                lambda i: i.get("id"), ["items", project_id])
    items = [normalize_item(i, project_id, repository) for i in raw_items]
    views = client.traverse(project_query("views", "id number name layout"), {"id": project_id},
                            lambda d: node_connection(d, project_id, "ProjectV2", "views"),
                            lambda v: v.get("id"), ["views", project_id])
    values = []
    value_query = ("query($id:ID!,$cursor:String){ node(id:$id){ __typename id ... on ProjectV2Item { "
                   "fieldValues(first:100,after:$cursor){ nodes { " + VALUE_SELECTIONS[evidence_version] + " } " + PAGE + " } } } }")
    field_map = {f["id"]: f for f in fields}
    for item in items:
        raw_values = client.traverse(value_query, {"id": item["id"]},
                                     lambda d, i=item: node_connection(d, i["id"], "ProjectV2Item", "fieldValues"),
                                     value_key, ["values", item["id"]])
        observed = {value_key(v): v for v in raw_values}
        require(set(observed) <= set(field_map), "Value references unobserved field.")
        for field in fields:
            base = {"project_id": project_id, "item_id": item["id"], "field_id": field["id"]}
            raw = observed.get(field["id"])
            if field["dataType"] in BUILTINS:
                values.append(dict(base, **builtin_payload(item, field, raw, repository)))
                continue
            if raw is None:
                if item["content_disposition"] == "inaccessible-redacted":
                    status = "inaccessible-redacted"
                elif (field["isIssueField"] and item["type"] != "ISSUE") or (
                        field["dataType"] in {"REVIEWERS", "LINKED_PULL_REQUESTS", "REPOSITORY", "MILESTONE", "LABELS"}
                        and item["type"] == "DRAFT_ISSUE"):
                    status = "inapplicable"
                else:
                    status = "observed-unset"
                values.append(dict(base, disposition=status, value=None))
                continue
            typename = raw.get("__typename")
            kind = next((k for k in list(RELATIONS) + list(SINGULAR)
                         if typename == "ProjectV2ItemField" + k + "Value"), None)
            if kind:
                require(field["dataType"] == (RELATIONS.get(kind) or SINGULAR[kind])[0],
                        "Relationship type differs from field definition.")
                payload = relationship(client, item, field, kind, evidence_version)
            else:
                payload = scalar_payload(raw, field, item["id"])
            values.append(dict(base, disposition="present", **payload))
    value_ids = [v["value_id"] for v in values if v.get("value_id") is not None]
    require(len(set(value_ids)) == len(value_ids), "Scalar identity reused across distinct item/field pairs.")
    final_data = client.read(query, {"login": owner, "number": number})
    require(final_data == data, "Project identity/revision or principal changed during collection.")
    final_fields = client.traverse(project_query("fields", FIELD_SELECTIONS[evidence_version]), {"id": project_id},
                                   lambda d: node_connection(d, project_id, "ProjectV2", "fields"),
                                   lambda f: f.get("id"), ["fields-final", project_id])
    final_items = client.traverse(project_query("items", selected_items), {"id": project_id},
                                  lambda d: node_connection(d, project_id, "ProjectV2", "items"),
                                  lambda i: i.get("id"), ["items-final", project_id])
    require({f["id"]: f for f in fields} == {f["id"]: f for f in final_fields}
            and {i["id"]: i for i in raw_items} == {i["id"]: i for i in final_items},
            "Project fields/items changed during observation; retry as a new run.")
    coverage = {"evidence_schema_version": evidence_version, "endpoint": "https://api.github.com/graphql",
                "scope": "authorized-observable-project-values", "repository": repository,
                "project": project, "started_at": started, "ended_at": now(),
                "identity_query_sha256": fingerprint(query), "observations": client.observations,
                "principal": principal, "revision_rechecked": True,
                "request_count": len(client.requests),
                "unobservable_history_reconstructed": False}
    if evidence_version == "1.3.0":
        coverage["computed_metadata_policy"] = {
            "configured_types": sorted({f["dataType"] for f in fields} & BUILTINS),
            "direct_project_values_available": False,
            "timestamp_sources_retained_separately": True,
            "display_values_reconstructed": False,
            "sub_issue_descendants_collected": False,
        }
    return {"project-items.json": items, "project-fields.json": fields,
            "project-values.json": values, "project-coverage.json": coverage,
            "project-requests.json": client.requests, "project-views.json": views}


def verify(outputs, owner_kind, owner, number, repository):
    """Replay only retained, scoped responses; never access the network.

    Recompute joins, typed values and every traversal from the query transcript.
    This detects inconsistent evidence, not a maliciously rewritten package.
    A05 supplies transport hashes; neither mechanism certifies authenticity.
    """
    require(set(outputs) == set(OUTPUTS), "Incomplete Project output set.")
    requests = outputs["project-requests.json"]
    require(isinstance(requests, list), "Invalid Project transcript.")
    offset = 0

    def replay(query, variables):
        nonlocal offset
        require(offset < len(requests), "Missing retained Project response.")
        record = requests[offset]
        offset += 1
        require(isinstance(record, dict) and record.get("query_sha256") == fingerprint(query)
                and record.get("variables") == variables, "Retained query target/cursor mismatch.")
        return record.get("response")

    evidence_version = outputs["project-coverage.json"].get("evidence_schema_version")
    require(evidence_version in REVIEWER_SELECTIONS, "Unsupported Project evidence version.")
    expected = collect(owner_kind, owner, number, repository, replay, evidence_version=evidence_version)
    require(offset == len(requests), "Unexpected extra retained Project response.")
    for name in OUTPUTS:
        if name != "project-coverage.json":
            require(outputs[name] == expected[name], "Project payload does not match retained responses.")
    actual = copy.deepcopy(outputs["project-coverage.json"])
    fresh = expected["project-coverage.json"]
    for coverage in (actual, fresh):
        start = datetime.fromisoformat(coverage.pop("started_at"))
        end = datetime.fromisoformat(coverage.pop("ended_at"))
        require(start.tzinfo is not None and end.tzinfo is not None and start <= end,
                "Invalid Project observation interval.")
        for observation in coverage["observations"]:
            observation_start = datetime.fromisoformat(observation.pop("started_at"))
            observation_end = datetime.fromisoformat(observation.pop("ended_at"))
            require(start <= observation_start <= observation_end <= end,
                    "Project traversal interval outside collection.")
            for page in observation.get("pages", []):
                observed = datetime.fromisoformat(page.pop("observed_at"))
                require(observation_start <= observed <= observation_end, "Page interval mismatch.")
    require(actual == fresh, "Project coverage differs from replayed traversal evidence.")
    return outputs["project-coverage.json"]


def publish(outputs, destination):
    destination = Path(destination)
    require(set(outputs) == set(OUTPUTS), "Incomplete Project output set.")
    require(not any((destination / name).exists() or (destination / name).is_symlink() for name in OUTPUTS),
            "Refusing to overwrite Project evidence.")
    destination.mkdir(parents=True, exist_ok=True, mode=0o700)
    staging = Path(tempfile.mkdtemp(prefix=".project-evidence-", dir=destination))
    try:
        for name, payload in outputs.items():
            path = staging / name
            with path.open("x", encoding="utf-8") as stream:
                os.chmod(path, 0o600)
                json.dump(payload, stream, indent=2, ensure_ascii=True, allow_nan=False)
                stream.write("\n")
        for name in OUTPUTS:
            os.replace(staging / name, destination / name)
    finally:
        shutil.rmtree(staging)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("collect", "verify"))
    parser.add_argument("--owner-kind", choices=("organization", "user"), default="organization")
    parser.add_argument("--owner", required=True)
    parser.add_argument("--number", type=int, required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.action == "collect":
            outputs = collect(args.owner_kind, args.owner, args.number, args.repository)
            verify(outputs, args.owner_kind, args.owner, args.number, args.repository)
            publish(outputs, args.destination)
        else:
            outputs = {name: json_load((args.destination / name).read_bytes()) for name in OUTPUTS}
            verify(outputs, args.owner_kind, args.owner, args.number, args.repository)
    except (ProjectError, OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print("ERROR: Required Project evidence unavailable, invalid or incomplete; no complete profile.", file=sys.stderr)
        if isinstance(error, ProjectError):
            print("Reason: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
