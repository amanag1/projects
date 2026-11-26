# Project 6 — AI-Powered Document Q&A & Knowledge Assistant

A practical document assistant that answers questions from a supplied knowledge base and shows the supporting passages. It is designed around grounded answers, traceability and human review—not an unverified chatbot demo.

## Business problem
Teams repeatedly search policies, procedures, manuals and project documents. This creates slow responses, duplicated effort and inconsistent answers.

## What this solution demonstrates
- Ingest text-based PDF, TXT and Markdown documents.
- Split content into traceable chunks with document and page metadata.
- Retrieve relevant passages before answering.
- Return citations/snippets so users can inspect the evidence.
- Use a pluggable LLM adapter; deterministic extractive mode remains available for local demos.
- Mark low-evidence answers for human review instead of inventing certainty.
- Keep ingestion and query operations logged without storing secrets.
- Include tests for empty documents, missing evidence, malformed input and citation integrity.

## Differentiation beyond AI-generated code
The deliverable includes a controlled ingestion pipeline, document provenance, retrieval checks, evidence thresholds, abstention behaviour, repeatable tests and a review path. An LLM response is not treated as automatically correct.

## Current implementation scope
This repository starts with a dependency-light retrieval and evidence layer. Production deployments should add a persistent vector store, authentication, tenant isolation, encrypted storage, provider-specific evaluation and monitoring appropriate to the client's data and compliance requirements.

## Structure
`src/knowledge_assistant/`, `tests/`, `docs/`, `scripts/`, `docker/`, `deploy/helm/`, `.github/workflows/`.

## Run
```bash
python -m pip install -e ".[dev]"
knowledge-assistant --help
pytest -q
```

Do not upload confidential or personal documents to a third-party model provider without the client's explicit approval.
