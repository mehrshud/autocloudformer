# src/tests/test_alerts.py
from typing import Dict
from unittest.mock import Mock

import pytest
from AutoCloudFormer import send_alert

@pytest.fixture
def user() -> Dict:
    return {"id": 1, "name": "test_user"}

def test_send_alert_success(user: Dict):
    # Arrange
    sender = Mock()
    send_alert.send_alert = sender
    
    # Act
    send_alert.send_alert(user, "Test alert")
    
    # Assert
    sender.assert_called_once_with(user, "Test alert")

def test_send_alert_failure(user: Dict):
    # Arrange
    sender = Mock(side_effect=Exception("Test error"))
    send_alert.send_alert = sender
    
    # Act and Assert
    with pytest.raises(Exception):
        send_alert.send_alert(user, "Test alert")

def test_send_alert_empty_user():
    # Arrange
    sender = Mock()
    send_alert.send_alert = sender
    
    # Act
    send_alert.send_alert({}, "Test alert")
    
    # Assert
    sender.assert_not_called()

def test_send_alert_empty_message(user: Dict):
    # Arrange
    sender = Mock()
    send_alert.send_alert = sender
    
    # Act
    send_alert.send_alert(user, "")
    
    # Assert
    sender.assert_not_called()
