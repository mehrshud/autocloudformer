# src/tests/test_api.py

import pytest
from typing import Dict
from unittest.mock import Mock
from src.api import APIEndpoint

@pytest.fixture
def mock_service_layer():
    return Mock()

@pytest.fixture
def api_endpoint(mock_service_layer: Mock) -> APIEndpoint:
    return APIEndpoint(service_layer=mock_service_layer)

def test_api_endpoint_routes_request_to_service_layer(
    api_endpoint: APIEndpoint, mock_service_layer: Mock
):
    # Arrange
    request: Dict[str, str] = {"resource": "cpu"}

    # Act
    api_endpoint.handle_request(request)

    # Assert
    mock_service_layer.process_request.assert_called_once_with(request)

def test_api_endpoint_returns_prediction(
    api_endpoint: APIEndpoint, mock_service_layer: Mock
):
    # Arrange
    request: Dict[str, str] = {"resource": "cpu"}
    mock_service_layer.process_request.return_value = "prediction"

    # Act
    response = api_endpoint.handle_request(request)

    # Assert
    assert response == "prediction"
