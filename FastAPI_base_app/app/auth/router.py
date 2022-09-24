from app.data_base import data_base
from app.models import User

from fastapi import APIRouter

from typing import List


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
def register(user: User):
    """Registers specified user in the database."""
    data_base.register(user)


@auth_router.post("/unregister")
def unregister(user: User):
    """Unregisters specified user from the database."""
    data_base.unregister(user)


# todo remove later -- debug only
@auth_router.get("/allusers")
def allusers() -> List[User]:
    """Shows the list of all users in the database."""
    return list(data_base.users)
