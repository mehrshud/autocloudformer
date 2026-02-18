# src/tests/test_services.py
from typing import List
from unittest.mock import patch, MagicMock
from pytest import fixture
from src.services import get_user_resources

@fixture
def mock_user() -> dict:
    return {"id": 1, "name": "Test User"}

@patch("src.services.get_resources")
def test_get_user_resources_positive(mock_get_resources: MagicMock, mock_user: dict) -> None:
    # Arrange
    mock_get_resources.return_value = ["resource1", "resource2"]
    
    # Act
    resources: List[str] = get_user_resources(mock_user)
    
    # Assert
    assert resources == ["resource1", "resource2"]

@patch("src.services.get_resources")
def test_get_user_resources_negative(mock_get_resources: MagicMock, mock_user: dict) -> None:
    # Arrange
    mock_get_resources.return_value = []
    
    # Act
    resources: List[str] = get_user_resources(mock_user)
    
    # Assert
    assert resources == []

@patch("src.services.get_resources")
def test_get_user_resources_edge_case(mock_get_resources: MagicMock, mock_user: dict) -> None:
    # Arrange
    mock_get_resources.side_effect = Exception("Test Exception")
    
    # Act and Assert
    try:
        get_user_resources(mock_user)
        assert False, "Test should raise an exception"
    except Exception as e:
        assert str(e) == "Test Exception"
