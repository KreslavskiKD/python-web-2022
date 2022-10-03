from app.database import DataBase
from dependency_injector import containers, providers
from app.repositories import UserRepository
from app.services import UserService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[".auth.auth_router", ".database"]
    )

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(DataBase, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
