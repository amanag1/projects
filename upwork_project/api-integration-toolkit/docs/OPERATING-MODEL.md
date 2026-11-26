# Operating model

Every integration run follows this sequence:

1. Read source records and attach a run identifier.
2. Validate required fields and expected types.
3. Map source fields to the target contract.
4. Generate stable idempotency keys.
5. Produce a dry-run preview for operator review.
6. Execute only approved, valid records through a provider adapter.
7. Reconcile attempted, accepted, rejected, duplicate and failed counts.
8. Export an exception report for manual resolution.

Provider adapters must implement bounded retries for transient errors, respect rate limits, keep credentials in environment/secret storage and avoid retrying non-idempotent writes without a safe idempotency mechanism.
