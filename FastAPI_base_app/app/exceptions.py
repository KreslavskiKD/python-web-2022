class Error(Exception):
    """Base class for other exceptions."""

    pass


class LoginAlreadyTakenError(Error):
    """Raised when trying to register a user with existing login."""

    pass


class UserNotFoundError(Error):
    """Raised when user is not found in DB."""

    pass
