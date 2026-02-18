# tests/__init__.py
import pytest
from unittest.mock import MagicMock
from typing import Dict

# Import your module here, e.g., from my_module import MyModule

@pytest.fixture
def mock_user() -> Dict[str, int]:
    """Returns a mock user with id and name."""
    return {"id": 1, "name": "test_user"}


def test_init_user(mock_user: Dict[str, int]) -> None:
    """Tests the User class initialization."""
    # Arrange
    user_id = mock_user["id"]
    user_name = mock_user["name"]
    
    # Act
    # Initialize your User class here, e.g., user = User(user_id, user_name)
    
    # Assert
    # Add your assertions here, e.g., assert user.id == user_id

def test_invalid_user_id(mock_user: Dict[str, int]) -> None:
    """Tests the User class with an invalid id."""
    # Arrange
    user_id = "invalid_id"
    user_name = mock_user["name"]
    
    # Act and Assert
    # Try to initialize your User class with an invalid id and assert it raises an error
    with pytest.raises(TypeError):
        # Initialize your User class here with an invalid id, e.g., User(user_id, user_name)

def test_invalid_user_name(mock_user: Dict[str, int]) -> None:
    """Tests the User class with an invalid name."""
    # Arrange
    user_id = mock_user["id"]
    user_name = 123
    
    # Act and Assert
    # Try to initialize your User class with an invalid name and assert it raises an error
    with pytest.raises(TypeError):
        # Initialize your User class here with an invalid name, e.g., User(user_id, user_name)
