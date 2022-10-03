from app.containers import Container
from app.services import UserService
from dependency_injector.wiring import Provide, inject
from app.exceptions import UserNotFoundError

from fastapi import APIRouter, Depends, Response, status
from . import dto


auth_router = APIRouter(prefix="/auth")


@auth_router.get("/users")
@inject
def get_list(
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()


@auth_router.get("/users/{user_id}")
@inject
def get_by_id(
    user_id: str,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        return user_service.get_user_by_id(user_id)
    except UserNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@auth_router.post("/users", status_code=status.HTTP_201_CREATED)
@inject
def add(
    user: dto.UserRegister,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.create_user(user)


@auth_router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
    user_id: str,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except UserNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@auth_router.get("/status")
def get_status():
    return {"status": "OK"}
