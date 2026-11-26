import pytest
from fastapi_service.engine.greetings import format_greeting


def test_format_greeting():
    assert format_greeting("  Sam  ") == "Hello, Sam!"


def test_blank_name_rejected():
    with pytest.raises(ValueError):
        format_greeting(" ")
