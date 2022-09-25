import pytest

from app.auth.router import auth_router as router
from app.models import User
from app.auth.dto import UserRegister
from app.auth.dto import UserUnregister
from app.contracts import Locations

user = UserRegister(login="test", pswd="user")

answ_user = User(
    login="test",
    pswd="user",
    uuid="1",
    favlist=Locations(owner="1", locations=[]),
    posts=[],
)

unuser = UserUnregister(uuid="1")
