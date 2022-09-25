import pytest

from app.data_base import DataBase

from app.models import User
from app.auth.dto import UserRegister
from app.auth.dto import UserUnregister
from app.contracts import Locations
from app.exceptions import LoginAlreadyTakenError, UserNotFoundError

user = UserRegister(login="test", pswd="user")

answ_user = User(
    login="test",
    uuid="1",
    favlist=Locations(owner="1", locations=[]),
    posts=[],
)

unuser = UserUnregister(uuid="1")

test_db = DataBase()


def test_register_ok():
    test_db.register(user)
    assert test_db.users == {1, answ_user}
    assert test_db.logins == {1, "test"}
    assert test_db.pswds == {1, "user"}


def test_register_bad():
    with pytest.raises(LoginAlreadyTakenError):
        test_db.register(user)


def test_unregister():
    test_db.unregister(unuser)
    assert test_db.users == {}
    assert test_db.logins == {}
    assert test_db.pswds == {}


def test_unregister_bad():
    with pytest.raises(UserNotFoundError):
        test_db.unregister(unuser)
