"""Small reusable application logic for the Lite edition."""
def greeting(name: str) -> str:
    normalized = name.strip()
    if not normalized:
        raise ValueError("name must not be blank")
    if len(normalized) > 80:
        raise ValueError("name must be 80 characters or fewer")
    return f"Hello, {normalized}!"
