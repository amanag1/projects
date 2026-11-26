# Architecture

The FastAPI layer validates uploads and delegates extraction to a small service. The engine dispatches by extension: UTF-8 text and Markdown are decoded directly, CSV is normalized into readable rows, and PDF text is extracted with pypdf. The response contains text plus lightweight metadata.

The service is stateless: it does not persist documents. Upload bytes are bounded by the configured limit and held in memory for the duration of the request. A future asynchronous design could use a queue and object storage with explicit retention policies.
