from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

from .database import Base


class User(Base):
    """User model for data base"""

    __tablename__ = "users"

    id = Column(String, primary_key=True)
    login = Column(String, unique=True)
    hashed_password = Column(String)
    locations = Column(MutableList.as_mutable(PickleType), default=[])
    posts = Column(MutableList.as_mutable(PickleType), default=[])

    def __repr__(self):
        return (
            f"<User(id={self.id}, "
            f'email="{self.login}", '
            f'hashed_password="{self.hashed_password}", '
            f'locations="{self.locations}", '
            f'posts=""{self.posts})>'
        )
