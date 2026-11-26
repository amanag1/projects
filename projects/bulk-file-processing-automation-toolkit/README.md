# Bulk File Processing & Automation Toolkit

A practical toolkit for safely organizing large folders of files. Preview changes, organize by extension, calculate SHA-256 hashes, and identify duplicate content without relying on a heavyweight desktop application.

## Editions
- **Lite** — a standard-library Python CLI for local folders.
- **Production** — a container-ready FastAPI service for processing uploaded batches and returning an organized ZIP archive.

Start with the edition README files:
- [Lite edition](bulk-file-processing-automation-toolkit-lite/README.md)
- [Production edition](bulk-file-processing-automation-toolkit-production/README.md)

## Safety
Lite defaults to dry-run mode. Production isolates each request in a temporary workspace, limits upload size, and does not execute uploaded files. Review the security notes before exposing the API beyond a trusted network.

## Requirements
Python 3.10+ for Lite. Production uses Python 3.11+.

## License
MIT. See the repository-level license if supplied.
