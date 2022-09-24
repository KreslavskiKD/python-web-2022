import pytest

from app.auth.router import auth_router as router
from app.models import User
from app.data_base.data_base import DataBaseInterface
from app.data_base.data_base import data_base
from app.contracts import List

user = User(
    login="test", pswd="user", uuid="0", favlist=List(owner="0", locations=[]), posts=[]
)

answ_user = User(
    login="test", pswd="user", uuid="1", favlist=List(owner="1", locations=[]), posts=[]
)


def test_registred(monkeypatch):  # noqa: D103
    monkeypatch.setattr(DataBaseInterface, "data_base", DataBaseInterface())
    router.register(user)
    assert data_base.users == {"1", user}


def test_registred_once(monkeypatch):  # noqa: D103
    monkeypatch.setattr(DataBaseInterface, "data_base", DataBaseInterface())
    router.register(user)
    router.register(user)
    assert data_base.users == {"1", user}


def test_unregistred(monkeypatch):  # noqa: D103
    monkeypatch.setattr(DataBaseInterface, "data_base", DataBaseInterface())
    router.register(user)
    assert data_base.users == {"1", user}
    router.unregister(user)
    assert data_base.users == {}
