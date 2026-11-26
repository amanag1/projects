from api_integration.pipeline import execute_plan, idempotency_key, plan_batch

def test_plan_rejects_missing_fields_and_flags_duplicates():
    rows = [{"email": "a@example.com", "name": "A"}, {"email": "", "name": "B"},
            {"email": "a@example.com", "name": "A"}]
    plan = plan_batch(rows, ("email",), {"email": "contact"}, ("email",))
    assert [x["status"] for x in plan] == ["ready", "rejected", "duplicate_in_batch"]

def test_dry_run_never_calls_writer():
    called = []
    plan = plan_batch([{"id": 1}], ("id",), {"id": "external_id"}, ("id",))
    result = execute_plan(plan, lambda payload, key: called.append(payload), dry_run=True)
    assert not called
    assert result[0].status == "previewed"

def test_idempotency_is_stable():
    assert idempotency_key({"b": 2, "a": 1}, ("a", "b")) == idempotency_key({"a": 1, "b": 2}, ("b", "a"))
