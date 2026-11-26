# System requirements

- Python 3.11+ for local execution; Python 3.12 slim base image for container builds.
- 1 CPU and 512 MiB RAM are reasonable starting points for light workloads; tune using representative documents.
- Temporary memory usage scales with upload size and extracted text size. Configure `MAX_UPLOAD_BYTES` for available memory.
- Network access is needed only to install dependencies or reach the API from clients.
