# Document Intelligence & Extraction Toolkit

A practical, self-hostable toolkit for turning everyday documents into structured, searchable text and metadata.

## Editions

- **Lite** — local command-line extraction for TXT, Markdown and CSV files. No web server or third-party runtime dependencies.
- **Production** — API-based extraction for TXT, Markdown, CSV and text-based PDF files, with upload limits, validation, structured results, Docker, CI and Helm deployment.

## What it extracts

Plain text, document metadata, word and character counts, Markdown headings, email addresses and URLs. Production also extracts text from PDFs using pypdf.

> OCR is not included. Image-only or scanned PDFs require an OCR pipeline and will not yield meaningful text from this release.

## Quick start

See the edition-specific READMEs:
- [Lite edition](document-intelligence-extraction-toolkit-lite/README.md)
- [Production edition](document-intelligence-extraction-toolkit-production/README.md)

## Intended use

Local document processing, content inventory, migration preparation, lightweight knowledge-base ingestion and integration prototypes. Review extracted content before using it in consequential workflows.

## Security notes

Uploaded files are treated as untrusted data. The Production API enforces an extension allow-list and configurable size limit, processes files in memory, and does not execute document content. Deploy behind authentication and suitable network controls before exposing it to untrusted users.

## Licence

MIT. See [LICENSE](LICENSE).
