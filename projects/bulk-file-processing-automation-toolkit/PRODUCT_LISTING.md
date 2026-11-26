# Gumroad product listing

## Product name
Bulk File Processing & Automation Toolkit

## Short summary
Organize folders, inspect file hashes, and process batches safely with a lightweight Python CLI or a container-ready API.

## Description
Stop spending time sorting downloads, project exports, and document archives by hand. This toolkit gives you repeatable file-processing workflows with a preview-first Lite edition and a more structured API edition for team environments.

### Lite edition
- Standard-library Python; no third-party runtime dependencies
- Organize files into extension-based folders
- Dry-run preview before changes are applied
- SHA-256 manifest and duplicate-content detection
- JSON configuration and automated tests

### Production edition
- FastAPI endpoint for multi-file batch processing
- Upload-size and file-count limits
- Isolated per-request workspaces
- Downloadable ZIP result
- Docker Compose, Helm starter chart, CI workflow and operational documentation

### What is included
Two separate codebases, sample configuration, tests, setup instructions, architecture notes and deployment starter files.

**Important:** The Production edition is an API starter, not a managed cloud service or a persistent job queue. Add authentication, rate limiting, storage policies and monitoring before public deployment.
