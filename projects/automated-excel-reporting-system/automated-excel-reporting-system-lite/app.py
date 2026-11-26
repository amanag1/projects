"""Command-line entry point for the Lite edition."""
import argparse
from engine import profile_workbook

def main():
    parser = argparse.ArgumentParser(description="Create a profiled Excel report")
    parser.add_argument("input", help="Source .xlsx workbook")
    parser.add_argument("-o", "--output", default="profiled_report.xlsx")
    args = parser.parse_args()
    result = profile_workbook(args.input, args.output)
    print(f"Created {result['output']} ({len(result['sheets'])} worksheet(s))")

if __name__ == "__main__":
    main()
