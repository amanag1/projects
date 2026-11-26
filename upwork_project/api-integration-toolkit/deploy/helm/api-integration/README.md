# Helm chart scaffold

Chart metadata and resource defaults are provided as a starting point. A deployable worker is intentionally not supplied yet: each client integration needs a concrete provider adapter, scheduling/queue semantics, approved secrets configuration, health checks and retry/dead-letter policy. Do not install this scaffold into a production cluster until those components and tests are implemented.
