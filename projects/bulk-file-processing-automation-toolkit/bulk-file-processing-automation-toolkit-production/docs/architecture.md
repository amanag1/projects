# Architecture

The service separates transport, configuration and filesystem processing.

- `api/routes.py` validates the upload count, streams request bodies to an isolated temporary workspace, and returns a ZIP response.
- `core/settings.py` loads bounded upload settings from environment variables.
- `engine/organizer.py` groups files by extension and creates a SHA-256 manifest.
- `main.py` wires the FastAPI application and operational endpoints.

The API is synchronous and stateless. It does not provide a durable queue, database-backed job history or persistent artifact storage.
