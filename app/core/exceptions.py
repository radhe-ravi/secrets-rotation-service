# app/core/exceptions.py


class AppBaseException(Exception):
    """Base exception for the application."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class SecretNotFoundException(AppBaseException):
    pass


class UnauthorizedException(AppBaseException):
    pass


class ProviderException(AppBaseException):
    pass


class DatabaseException(AppBaseException):
    pass
