from typing import Iterator

from .repositories import UserRepository
from .models import User
from app.auth import dto


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self, user: dto.UserRegister) -> User:
        return self._repository.add(login=user.login, password=user.pswd)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
