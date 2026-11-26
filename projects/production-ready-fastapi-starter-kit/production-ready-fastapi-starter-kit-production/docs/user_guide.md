# User guide

1. Install the package in editable mode.
2. Configure `.env` for the local environment.
3. Start the development server with Uvicorn.
4. Open `/docs` and try `POST /api/v1/greetings`.
5. Include `X-Request-ID` when calling the API if you need to correlate a request across gateway and application logs.

The example endpoint is intentionally simple; replace it with your own request models and service functions.
