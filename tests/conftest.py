# tests/conftest.py
import pytest
from unittest.mock import Mock
from typing import Dict

@pytest.fixture
def user() -> Dict:
    """Returns a user fixture."""
    return {"id": 1, "name": "John Doe"}

@pytest.fixture
def mock_api_endpoint() -> Mock:
    """Returns a mock API endpoint."""
    return Mock()

def test_user_creation(user: Dict) -> None:
    """Tests user creation."""
    # Arrange
    expected_user = {"id": 1, "name": "John Doe"}
    
    # Act
    actual_user = user
    
    # Assert
    assert actual_user == expected_user

def test_api_endpoint_call(mock_api_endpoint: Mock) -> None:
    """Tests API endpoint call."""
    # Arrange
    mock_api_endpoint.return_value = {"status": 200}
    
    # Act
    response = mock_api_endpoint()
    
    # Assert
    assert response["status"] == 200

def test_empty_user() -> None:
    """Tests empty user."""
    # Arrange
    user: Dict = {}
    
    # Act and Assert
    with pytest.raises(KeyError):
        user["id"]

def test_api_endpoint_error(mock_api_endpoint: Mock) -> None:
    """Tests API endpoint error."""
    # Arrange
    mock_api_endpoint.side_effect = Exception("API endpoint error")
    
    # Act and Assert
    with pytest.raises(Exception):
        mock_api_endpoint()
