class Error(Exception):
    """Base class for other exceptions."""


class LoginAlreadyTakenError(Error):
    """Raised when trying to register a user with existing login."""


class UserNotFoundError(Error):
    """Raised when user is not found in DB."""

    def __init__(self, entity_id):
        super().__init__(f"user not found, id: {entity_id}")
