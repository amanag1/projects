# Helm deployment

Build and publish the container image, then install the chart:

```bash
helm upgrade --install document-intelligence ./document-intelligence \
  --set image.repository=YOUR_REGISTRY/document-intelligence \
  --set image.tag=1.0.0
```

Configure ingress, TLS, authentication, resource limits and network policies for your cluster before external exposure.
