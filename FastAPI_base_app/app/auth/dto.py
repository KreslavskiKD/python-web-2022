from pydantic import BaseModel


class UserRegister(BaseModel):
    """DTO class for registering a user."""

    login: str
    pswd: str


class UserUnregister(BaseModel):
    """DTO class for unregistering a user."""

    uid: str
