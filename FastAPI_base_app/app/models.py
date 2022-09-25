from pydantic import BaseModel
from app.contracts import Locations


class User(BaseModel):
    login: str
    uuid: str
    favlist: Locations
    posts: list[int]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False

        return self.uuid == other.uuid

    def __hash__(self):
        return hash((self.login, self.uuid))
