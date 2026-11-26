import pytest
from engine import greeting


def test_greeting_trims_whitespace():
    assert greeting("  Ada  ") == "Hello, Ada!"


def test_greeting_rejects_blank():
    with pytest.raises(ValueError):
        greeting("  ")
