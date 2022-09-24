from os import getuid
from typing import Optional

from app.models import User


class DataBaseInterface:
    """This is temporary db interface mock until we learn how to do it properly."""

    users = {}
    posts = {}
    cid = 0

    def __init__(self) -> None:  # noqa: D107
        self.users = {}
        self.posts = {}
        self.cid = 0

    def register(self, user: User) -> Optional[User]:
        """Regiseters user in DB.

        Params: user as a class of User
        Returns: the same user if registered successfully, None otherwise
        """
        was = False
        for _k, v in self.users.items():
            if v.login == user.login:
                was = True

        if not was:
            user.uuid = self.get_uuid()
            user.favlist.owner = user.self.uuid
            self.users[user.uuid] = user
            return user
        else:
            return None

    def unregister(self, user: User) -> Optional[User]:
        """Unregiseters user from DB and removes all data.

        Params: user as a class of User
        Returns: the same user if unregistered successfully, None otherwise
        """
        if user.uuid in self.users:
            del self.users[user.uuid]
            return user
        else:
            return None

    def get_uuid(self) -> str:
        """Makes new unique identifier for new users. Temporary solution now."""
        self.cid += 1
        return str(self.cid)  # str(getuid())  # temporary solution


data_base: DataBaseInterface = DataBaseInterface()
