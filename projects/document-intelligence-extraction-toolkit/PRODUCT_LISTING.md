# Gumroad Product Listing

## Product name
Document Intelligence & Extraction Toolkit

## Short summary
Extract clean text and useful metadata from common documents with a lightweight local tool or a production-ready API.

## Lite edition
A simple, dependency-free command-line utility for TXT, Markdown and CSV files. Includes batch processing, JSON output, heading detection, word counts, email and URL discovery, and a dry-run friendly workflow.

## Production edition
Everything needed to run a document extraction service: FastAPI endpoints, PDF text extraction, upload validation and size limits, structured JSON responses, tests, Docker Compose, CI workflow, Helm chart and operational documentation.

## Important limitations
This release extracts embedded text; it does not perform OCR on scanned or image-only PDFs. It does not store uploaded documents or execute their contents. Authentication, rate limiting and network allow-listing should be configured at the deployment boundary before public exposure.

## Suggested pricing
- Lite: $9
- Production: $29

## Included files
Source code, tests, sample data, deployment assets and documentation for both editions.
