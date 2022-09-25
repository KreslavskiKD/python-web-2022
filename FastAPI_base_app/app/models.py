from pydantic import BaseModel
from app.contracts import Locations


class User(BaseModel):
    login: str
    uuid: str
    favlist: Locations
    posts: list[int]
