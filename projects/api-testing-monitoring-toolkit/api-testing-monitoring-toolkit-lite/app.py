"""Run checks described in a JSON file."""
import argparse
import json
from engine import run_check

def main():
    parser = argparse.ArgumentParser(description="Run simple API availability checks")
    parser.add_argument("config", help="JSON file containing a checks array")
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()
    with open(args.config, encoding="utf-8") as stream:
        checks = json.load(stream)["checks"]
    results = [run_check(item, args.timeout) for item in checks]
    print(json.dumps({"total": len(results), "passed": sum(x["passed"] for x in results),
                      "failed": sum(not x["passed"] for x in results), "results": results}, indent=2))
    raise SystemExit(1 if any(not x["passed"] for x in results) else 0)

if __name__ == "__main__":
    main()
