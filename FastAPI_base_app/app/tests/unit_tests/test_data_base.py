import pytest

from app.database import DataBase

from app.models import User
from app.auth.dto import UserRegister
from app.exceptions import LoginAlreadyTakenError, UserNotFoundError

user = UserRegister(login="test", pswd="user")

# test_db = DataBase(db_url="sqlite:///./postogramm.db")


# def test_register_ok():  # noqa D103
#     test_db.register(login=user.login, pswd=user.pswd)
#     ind = str(test_db.cid)
#     assert test_db.users == {
#         ind: User(
#             login="test",
#             uuid=ind,
#             favlist=[],
#             posts=[],
#         )
#     }
#     assert test_db.logins == {ind: "test"}
#     assert test_db.pswds == {ind: "user"}


# def test_register_bad():  # noqa D103
#     with pytest.raises(LoginAlreadyTakenError):
#         test_db.register(login=user.login, pswd=user.pswd)


# def test_unregister():  # noqa D103
#     ind = str(test_db.cid)
#     assert ind == test_db.unregister(uid=ind)
#     assert test_db.users == {}
#     assert test_db.logins == {}
#     assert test_db.pswds == {}


# def test_unregister_bad():
#     ind = str(test_db.cid)
#     with pytest.raises(UserNotFoundError):
#         test_db.unregister(uid=ind)
