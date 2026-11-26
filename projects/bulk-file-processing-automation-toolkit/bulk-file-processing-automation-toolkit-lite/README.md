# Bulk File Processing Toolkit — Lite

A dependency-free CLI for organizing a folder by file extension, previewing changes, producing a SHA-256 manifest, and identifying duplicate file contents.

## Requirements
Python 3.10+. Standard library only.

## Quick start
```bash
python app.py organize ./incoming --output ./organized --dry-run
python app.py organize ./incoming --output ./organized --apply
python app.py manifest ./incoming --output manifest.json
python app.py duplicates ./incoming
```

The default is a preview. Use `--apply` to copy files into extension-named folders. Existing destination files are never overwritten; a numbered suffix is selected instead. The source folder is not modified.

## Configuration
See [sample_data/rules.json](sample_data/rules.json). Rules can define extension labels and ignored names. The CLI currently uses the safe built-in extension grouping; the sample file is a starting point for extending the workflow.

## Tests
```bash
python -m unittest discover -s tests -v
```
