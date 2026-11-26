# Container packaging
The root Dockerfile installs the reusable integration package. A production worker image must add the client's approved provider adapter, runtime configuration and secret injection method. Do not bake credentials into the image.
