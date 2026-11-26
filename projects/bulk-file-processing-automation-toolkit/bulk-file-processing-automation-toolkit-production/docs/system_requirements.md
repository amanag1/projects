# System requirements

- Python 3.11+ for local execution
- Docker Engine with Compose plugin for container execution
- Memory and temporary disk capacity sized for the maximum concurrent uploads
- Network access restricted to trusted clients unless authentication and rate controls are added

The default combined request limit is 25 MiB and the default file count is 50. Increase limits only after sizing memory, temporary storage and worker concurrency.
