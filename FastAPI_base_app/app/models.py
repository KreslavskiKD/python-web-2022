
from pydantic import BaseModel
from app.contracts import List as ListModel


class User(BaseModel):
    login: str
    pswd: str
    uuid: str
    favlist: ListModel
    posts: list[int]
