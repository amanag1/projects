# System requirements

- Python 3.11+ for local development
- Docker Engine and Compose plugin for container workflow
- Kubernetes and Helm only if using the deployment starter chart
- A secrets manager and ingress/gateway policy for shared environments

The sample app is stateless. Resource requests and limits in the Helm chart are starter values and must be tuned with load testing.
