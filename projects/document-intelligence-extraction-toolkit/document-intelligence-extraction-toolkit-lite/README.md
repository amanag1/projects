# Document Intelligence Toolkit — Lite

A local, dependency-free CLI for extracting useful information from TXT, Markdown and CSV files.

## Requirements
Python 3.10+. No third-party packages.

## Run
```bash
python app.py ./sample_data --output results.json
```

Pass a single file or a directory. Directory processing is non-recursive by default. Add `--recursive` to include subdirectories. Use `--pretty` for readable JSON.

## Output
Each record contains filename, extension, byte size, character count, word count, headings (Markdown), discovered email addresses and URLs, and extracted text.

## Scope
PDF and DOCX are intentionally not supported in Lite. Use the Production edition for text-based PDF extraction. OCR is not included in either edition.
