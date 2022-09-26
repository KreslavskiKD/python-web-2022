import pytest

from app.models import User
from app.contracts import Locations
from app.auth.router import register, unregister, allusers
from app.auth.dto import UserRegister, UserUnregister
from app.exceptions import LoginAlreadyTakenError, UserNotFoundError

user = UserRegister(login="test", pswd="user")
unuser = UserUnregister(uuid="1")
answ_user = User(
    login="test",
    uuid="1",
    favlist=Locations(owner="1", locations=[]),
    posts=[],
)


def test_registred():  # noqa: D103
    register(user)
    users = allusers()
    assert users == {"1": answ_user}


def test_registred_once():  # noqa: D103
    with pytest.raises(LoginAlreadyTakenError):
        register(user)
        register(user)
        users = allusers()
        assert users == {"1": answ_user}


def test_unregistred():  # noqa: D103
    unregister(unuser)
    users = allusers()
    assert users == {}
