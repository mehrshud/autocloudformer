# tests/test_core.py
from typing import Dict
from unittest.mock import MagicMock
from auto_cloud_formation import core
import pytest

@pytest.fixture
def mock_user() -> Dict:
    return {"id": 1, "name": "Test User"}

@pytest.fixture
def mock_notification_system() -> MagicMock:
    return MagicMock()

def test_get_user_details(mock_user: Dict) -> None:
    # Arrange
    user_id = mock_user["id"]
    # Act
    result = core.get_user_details(user_id)
    # Assert
    assert result == mock_user

def test_scale_resources(mock_user: Dict, mock_notification_system: MagicMock) -> None:
    # Arrange
    user = mock_user
    notification_system = mock_notification_system
    # Act
    core.scale_resources(user, notification_system)
    # Assert
    mock_notification_system.send_notification.assert_called_once()
