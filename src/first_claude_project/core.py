"""Core domain logic. Keep it free of I/O so it is easy to test."""


def greet(name: str = "world") -> str:
    """Return a greeting for ``name``.

    Args:
        name: Who to greet. Surrounding whitespace is ignored.

    Raises:
        ValueError: If ``name`` is empty or only whitespace.
    """
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"
