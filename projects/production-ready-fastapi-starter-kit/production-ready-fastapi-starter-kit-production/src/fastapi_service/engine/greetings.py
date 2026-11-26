def format_greeting(name: str) -> str:
    normalized = name.strip()
    if not normalized:
        raise ValueError("Name must not be blank")
    return f"Hello, {normalized}!"
