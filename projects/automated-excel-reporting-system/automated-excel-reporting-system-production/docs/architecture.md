# Architecture

The service exposes a FastAPI upload endpoint. The API validates the workbook extension, stores the upload in a temporary working directory, and delegates workbook inspection to the profiling engine. The engine reads each worksheet with pandas and writes the source data plus a per-column profile to a separate workbook.

The service is stateless. For multi-replica production use, place uploads and generated artifacts in managed object storage and add authentication, quotas, malware scanning and retention controls before exposing it publicly.
