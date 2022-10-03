from contextlib import AbstractContextManager
from typing import Callable, Iterator
from uuid import uuid4

from sqlalchemy.orm import Session


from .db_models import User
from .exceptions import UserNotFoundError


class UserRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        """Repository that holds info about users."""
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        """Returns all users."""
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, user_id: str) -> User:
        """Returns specified user."""
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    def add(self, login: str, password: str) -> User:
        """Adds new user."""
        with self.session_factory() as session:
            user = User(
                id=uuid4(),
                login=login,
                hashed_password=password,
                locations=[],
                posts=[],
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: str) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()
