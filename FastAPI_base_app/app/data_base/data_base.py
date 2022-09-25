from os import getuid

from app.models import User
from app.contracts import Locations
from app.exceptions import LoginAlreadyTakenError, UserNotFoundError
from app.utils.singleton import Singleton


class DataBase(metaclass=Singleton):  # noqa D101
    def __init__(self) -> None:
        """This is temporary db class mock until we learn how to do it properly."""
        self.users = {}  # uuid -> user
        self.logins = {}  # uuid -> login
        self.pswds = {}  # uuid -> pswd
        self.posts = {}
        self.cid = 0

    def register(self, login: str, pswd: str) -> User:
        """Regiseters user in DB.

        Params: user as a class of User
        Returns: the same user if registered successfully, None otherwise
        """

        if login not in self.logins:
            uuid = self.get_uuid()
            self.logins[uuid] = login
            self.pswds[uuid] = pswd
            user = User(
                login=login,
                uuid=uuid,
                favlist=Locations(owner=uuid, locations=[]),
                posts=[],
            )
            self.users[uuid] = user
            return user
        else:
            raise LoginAlreadyTakenError()

    def unregister(self, uuid: str) -> User:
        """Unregiseters user from DB and removes all data.

        Params: uuid of the user
        Returns: the same uuid if unregistered successfully, None otherwise
        """
        if uuid in self.users:
            del self.users[uuid]
            return uuid
        else:
            raise UserNotFoundError

    def get_uuid(self) -> str:
        """Makes new unique identifier for new users. Temporary solution now."""
        self.cid += 1
        return str(self.cid)  # str(getuid())  # temporary solution
