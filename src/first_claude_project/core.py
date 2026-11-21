"""Core domain logic. Keep it free of I/O so it is easy to test."""

DEFAULT_GREETING = "Hello"


def greet(name: str = "world", greeting: str = DEFAULT_GREETING) -> str:
    """Return a greeting for ``name``.

    Args:
        name: Who to greet. Surrounding whitespace is ignored.
        greeting: The greeting word to use. Surrounding whitespace is ignored.

    Raises:
        ValueError: If ``name`` or ``greeting`` is empty or only whitespace.
    """
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must not be empty")
    cleaned_greeting = greeting.strip()
    if not cleaned_greeting:
        raise ValueError("greeting must not be empty")
    return f"{cleaned_greeting}, {cleaned_name}!"
