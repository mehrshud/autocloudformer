# tests/test_api.py
from fastapi import status
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch
from conftest import mock_user

client = TestClient(app)

def test_create_user():
    # Arrange
    user_data = {"id": 1, "name": "John"}
    
    # Act
    response = client.post("/users/", json=user_data)
    
    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["id"] == user_data["id"]
    assert response.json()["name"] == user_data["name"]

def test_get_user():
    # Arrange
    user_id = 1
    
    # Act
    with patch("main.get_user", return_value=mock_user):
        response = client.get(f"/users/{user_id}")
    
    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == user_id

def test_get_invalid_user():
    # Arrange
    user_id = 999
    
    # Act
    with patch("main.get_user", side_effect=ValueError("User not found")):
        response = client.get(f"/users/{user_id}")
    
    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
