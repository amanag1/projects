from fastapi_service.engine.greetings import format_greeting


def build_greeting(name: str) -> str:
    return format_greeting(name)
