from pydantic import BaseModel


class PostModel(BaseModel):  # this is post in Postogram
    """Contract for post."""

    pid: int
    title: str
    time: str  # here should later be some time format
    description: str
    locations: list[int]
    references: str  # here should be later list of users and companies


class User(BaseModel):
    login: str
    uuid: str
    favlist: list[int]
    posts: list[int]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False

        return self.uuid == other.uuid

    def __hash__(self):
        return hash((self.login, self.uuid))
