import pytest
from unittest import mock
from fastapi.testclient import TestClient

from app.db_models import User
from app.exceptions import LoginAlreadyTakenError, UserNotFoundError
from app.main import app
from app.repositories import UserRepository

answ_user = User(id="xyz", login="test1", hashed_password="pwd", locations=[], posts=[])


@pytest.fixture
def client():
    yield TestClient(app)


def test_get_list(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.get_all.return_value = [
        User(id="xyz", login="test1", hashed_password="pwd", locations=[], posts=[]),
        User(id="abc", login="test2", hashed_password="pwd", locations=[], posts=[]),
    ]

    with app.container.user_repository.override(repository_mock):
        response = client.get("/auth/users")

    assert response.status_code == 200
    data = response.json()
    assert data == [
        {
            "id": "xyz",
            "login": "test1",
            "hashed_password": "pwd",
            "locations": [],
            "posts": [],
        },
        {
            "id": "abc",
            "login": "test2",
            "hashed_password": "pwd",
            "locations": [],
            "posts": [],
        },
    ]


def test_get_by_id(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.get_by_id.return_value = answ_user

    with app.container.user_repository.override(repository_mock):
        response = client.get("/auth/users/xyz")

    assert response.status_code == 200
    data = response.json()
    assert data == {
        "id": "xyz",
        "login": "test1",
        "hashed_password": "pwd",
        "locations": [],
        "posts": [],
    }
    repository_mock.get_by_id.assert_called_once_with("xyz")


def test_get_by_id_404(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.get_by_id.side_effect = UserNotFoundError("xyz")

    with app.container.user_repository.override(repository_mock):
        response = client.get("/auth/users/xyz")

    assert response.status_code == 404


@mock.patch("app.repositories.uuid4", return_value="xyz")
def test_register(_, client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.add.return_value = answ_user

    with app.container.user_repository.override(repository_mock):
        response = client.post("/auth/users", json={"login": "test1", "pswd": "pwd"})

    assert response.status_code == 201
    data = response.json()
    assert data == {
        "id": "xyz",
        "login": "test1",
        "hashed_password": "pwd",
        "locations": [],
        "posts": [],
    }
    repository_mock.add.assert_called_once_with(login="test1", password="pwd")


def test_unregister(client):
    repository_mock = mock.Mock(spec=UserRepository)

    with app.container.user_repository.override(repository_mock):
        response = client.delete("/auth/users/xyz")

    assert response.status_code == 204
    repository_mock.delete_by_id.assert_called_once_with("xyz")


def test_unregister_404(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.delete_by_id.side_effect = UserNotFoundError("xyz")

    with app.container.user_repository.override(repository_mock):
        response = client.delete("/auth/users/xyz")

    assert response.status_code == 404
