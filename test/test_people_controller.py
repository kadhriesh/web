import pytest
from fastapi.testclient import TestClient

from bootstrap import app


@pytest.fixture()
def client():
    return TestClient(app)


def test_create_people(client):
    response = client.post(
        "/people",
        json={
            "id": 1,
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com",
        },
    )
    assert response.status_code == 201


def test_list_people(client):
    response = client.get("/people/0")
    assert response.status_code == 404


def test_get_people(client, monkeypatch):
    # monkeypatch.setitem
    #     "api.service.people.PeopleSvc.get_people_by_id",
    #     return_value={
    #         "id": 1,
    #         "first_name": "Alice",
    #         "last_name": "Smith",
    #         "email": "contac2kahir.gmail",
    #     },
    # )
    response = client.get("/people/1")
    assert response.status_code == 200
    assert "Alice" in response.json()["first_name"]
