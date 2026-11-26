import csv
from automation_utilities.csv_audit import audit_csv

def test_audit_reports_blanks_and_duplicates(tmp_path):
    path = tmp_path / "contacts.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "name"])
        writer.writeheader()
        writer.writerows([{"email": "x@example.com", "name": "X"},
                          {"email": "x@example.com", "name": ""}])
    result = audit_csv(path, ("email", "name"), ("email",))
    assert result["row_count"] == 2
    assert result["blank_counts"]["name"] == 1
    assert result["duplicate_groups"][0]["count"] == 2
