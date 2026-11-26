# Standalone Python Automation Utilities

Small, independently useful tools that solve repetitive operational problems. Each utility should run locally, explain its expected inputs and outputs, preview potentially destructive actions, and produce a clear execution summary.

## Utility roadmap

| Utility | Manual task replaced | Safety / quality control | Value to measure |
|---|---|---|---|
| CSV Schema & Quality Auditor | Inspect files and compare columns manually | Required-field checks, type checks, null/duplicate report, schema-drift detection | Review minutes and defects found |
| Bulk File Organizer | Sort downloads and business files by extension/date | Dry-run preview, collision-safe names, no overwrite by default | Sorting time and misplaced files |
| Folder Reconciliation Reporter | Compare two delivery folders manually | Hash-based comparison, missing/extra/changed report | Reconciliation time and missed files |
| Excel/CSV Consolidator | Combine recurring files manually | Header normalization, source traceability, row counts and validation | Monthly preparation time |
| Duplicate Record Investigator | Find duplicate customer/vendor rows | Configurable match keys, explainable duplicate groups, review export | Duplicate review time and false positives |

## Product principle
Each utility must be useful without an AI subscription. AI can help configure or extend it, but the shipped solution must execute deterministically, validate its work, explain exceptions and let the operator review before changing files or data.

## Demonstrating business value
For each demo, publish a reproducible benchmark: sample size, baseline manual steps, measured manual duration, automated duration, exception count and validation results. Calculate time saved from measurements; do not use invented percentages.

## Planned common folder convention
Each utility will have its own README, sample input, output example, tests and CLI entry point. Shared packaging/deployment files will be added only where they provide practical value.
