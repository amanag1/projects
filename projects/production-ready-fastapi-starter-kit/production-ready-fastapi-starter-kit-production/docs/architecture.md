# Architecture

The application follows a small layered structure.

- **API** owns HTTP routes and request/response schemas.
- **Core** owns environment settings, logging and request context middleware.
- **Services** contains application use cases independent of HTTP.
- **Database** documents the persistence integration boundary.
- **UI** describes the API-facing developer interface.

The starter keeps domain logic small so teams can replace the greeting example with real use cases without coupling business logic to FastAPI request objects.
