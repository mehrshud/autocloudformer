# src/tests/test_notifications.py
from unittest import mock
from pytest import fixture
from typing import Dict

@fixture
def user_data() -> Dict:
    return {"id": 1, "name": "Test User"}

@fixture
def notification_system_mock():
    with mock.patch("src.notifications.NotificationSystem") as mock_system:
        yield mock_system

def test_send_notification_success(notification_system_mock, user_data: Dict) -> None:
    # Arrange
    notification_system_mock().send_notification.return_value = True

    # Act
    result = notification_system_mock().send_notification(user_data["id"], "Test message")

    # Assert
    assert result is True
    notification_system_mock().send_notification.assert_called_once_with(user_data["id"], "Test message")

def test_send_notification_failure(notification_system_mock, user_data: Dict) -> None:
    # Arrange
    notification_system_mock().send_notification.return_value = False

    # Act
    result = notification_system_mock().send_notification(user_data["id"], "Test message")

    # Assert
    assert result is False
    notification_system_mock().send_notification.assert_called_once_with(user_data["id"], "Test message")

def test_send_notification_empty_message(notification_system_mock, user_data: Dict) -> None:
    # Arrange
    notification_system_mock().send_notification.return_value = False

    # Act
    result = notification_system_mock().send_notification(user_data["id"], "")

    # Assert
    assert result is False
    notification_system_mock().send_notification.assert_called_once_with(user_data["id"], "")
