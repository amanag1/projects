import pytest
from fastapi_service.services.greetings import build_greeting


def test_build_greeting():
    assert build_greeting("  Lin  ") == "Hello, Lin!"
