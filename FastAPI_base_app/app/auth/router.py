from app.data_base import data_base
from app.auth.dto import UserRegister
from app.auth.dto import UserUnregister 
from app.models import User

from fastapi import APIRouter

from typing import List


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
def register(user: UserRegister):
    """Registers specified user in the database."""
    data_base.register(login=user.login, pswd=user.pswd)


@auth_router.post("/unregister")
def unregister(user: UserUnregister):
    """Unregisters specified user from the database."""
    data_base.unregister(uuid=user.uuid)


# todo remove later -- debug only
@auth_router.get("/allusers")
def allusers() -> List[User]:
    """Shows the list of all users in the database."""
    return list(data_base.users)
