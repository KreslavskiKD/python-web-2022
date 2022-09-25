import pytest

from app.data_base.data_base import DataBase

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


def test_register_ok():  # noqa D103
    test_db.register(login=user.login, pswd=user.pswd)
    assert test_db.users == {"1": answ_user}
    assert test_db.logins == {"1": "test"}
    assert test_db.pswds == {"1": "user"}


def test_register_bad():  # noqa D103
    with pytest.raises(LoginAlreadyTakenError):
        test_db.register(login=user.login, pswd=user.pswd)


def test_unregister():  # noqa D103
    assert "1" == test_db.unregister(uuid=unuser.uuid)
    assert test_db.users == {}
    assert test_db.logins == {}
    assert test_db.pswds == {}


def test_unregister_bad():
    with pytest.raises(UserNotFoundError):
        test_db.unregister(uuid=unuser.uuid)
