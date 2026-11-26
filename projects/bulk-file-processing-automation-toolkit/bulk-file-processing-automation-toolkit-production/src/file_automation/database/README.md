# Persistence

This release is intentionally stateless: each request uses a temporary workspace and the archive is returned directly. No database is required. A future asynchronous edition can add a durable job table, object-storage references, job status transitions and retention cleanup. Do not represent this synchronous endpoint as a durable queue.
