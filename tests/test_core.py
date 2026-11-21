import pytest

from first_claude_project import __version__, greet


def test_greet_default() -> None:
    assert greet() == "Hello, world!"


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Ada", "Hello, Ada!"),
        ("  Grace  ", "Hello, Grace!"),
    ],
)
def test_greet_with_name(name: str, expected: str) -> None:
    assert greet(name) == expected


@pytest.mark.parametrize("name", ["", "   "])
def test_greet_rejects_empty_name(name: str) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        greet(name)


def test_version_is_a_string() -> None:
    assert isinstance(__version__, str)
    assert __version__
