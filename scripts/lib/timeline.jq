# Provider IDs are scoped to the issue and event kind. Events without an ID
# retain their complete observed payload as a snapshot-level comparison key.
# This is not a generated provider ID or a stable identity across observations.
def timeline_key:
  [.issue_number, .event,
    if .id != null then ["id", .id] else ["record", .] end];

def timeline_unique:
  unique_by(timeline_key)
  | sort_by(.issue_number, .created_at, .event, timeline_key);

def timeline_valid:
  type == "array"
  and all(.[];
    type == "object"
    and (.issue_number | type == "number" and . > 0 and floor == .)
    and (.event | type == "string" and length > 0))
  and (map(timeline_key) | length == (unique | length));
