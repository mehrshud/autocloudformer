# src/tests/test_main.py

import pytest
from typing import Any
from unittest.mock import Mock

from src.main import User

@pytest.fixture
def user() -> User:
    return User(id=1, name="John")

def test_user_creation(user: User) -> None:
    # Arrange
    expected_id = 1
    expected_name = "John"

    # Act
    actual_id = user.id
    actual_name = user.name

    # Assert
    assert actual_id == expected_id
    assert actual_name == expected_name

def test_user_negative_id() -> None:
    # Arrange
    expected_error: type[Exception] = ValueError

    # Act and Assert
    with pytest.raises(expected_error):
        User(id=-1, name="John")

def test_user_empty_name() -> None:
    # Arrange
    expected_error: type[Exception] = ValueError

    # Act and Assert
    with pytest.raises(expected_error):
        User(id=1, name="")

def test_user_to_string(user: User) -> None:
    # Act
    actual_string: str = str(user)

    # Assert
    assert user.name in actual_string
    assert str(user.id) in actual_string

def test_user_repr(user: User) -> None:
    # Act
    actual_string: str = repr(user)

    # Assert
    assert user.__class__.__name__ in actual_string
    assert str(user.id) in actual_string
    assert user.name in actual_string
