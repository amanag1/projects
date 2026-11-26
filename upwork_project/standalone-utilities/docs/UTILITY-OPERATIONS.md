# Utility operations

## CSV quality audit
`automation-utils csv-audit input.csv --required email,name --duplicate-key email`

Read-only. Reports missing required columns, blank values and duplicate-key groups.

## File organizer
`automation-utils organize ./incoming` previews proposed moves.
`automation-utils organize ./incoming --apply` performs moves. Review the preview first; existing destinations are not overwritten.

## Folder reconciliation
`automation-utils folder-diff ./source ./delivery` compares relative paths and SHA-256 hashes without changing either folder.

## Safe-use guidance
Run against a copy of business data first. Keep source backups, review outputs and validate the results before using them for downstream decisions.
