from dataclasses import dataclass


@dataclass
class User:
    """The in-memory representation of a user."""

    id: int
    name: str
    email: str
    age: int | None = None
