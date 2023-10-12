import pytest
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient


def test_get_suggestions(client: TestClient):
    """
    Test get suggestions - GET /suggestions
    """
    response = client.get(
        f"/suggestions",
        params={
            "q": "New York",
            "latitude": 43.70011,
            "longitude": -79.4163,
        },
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["suggestions"]) >= 0


def test_get_no_suggestions(client: TestClient):
    """
    Test get suggestions with empty result - GET /suggestions
    """
    response = client.get(
        f"/suggestions",
        params={"q": "SomeRandomCityInTheMiddleOfNowhere"},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["suggestions"] == []


def test_get_suggestions_without_city(client: TestClient):
    """
    Test get suggestions without city - GET /suggestions
    """
    with pytest.raises(RequestValidationError) as error:
        client.get(
            f"/suggestions",
            params={
                "latitude": 43.70011,
                "longitude": -79.4163,
            },
        )
    assert error.value.errors()[0]["msg"] == "Field required"
