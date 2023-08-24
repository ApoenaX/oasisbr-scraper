import requests.exceptions


class OasisBrApiError(Exception):
    """Base class for exceptions in this module."""


class OasisBrApiConnectionError(OasisBrApiError):
    """Exception raised for errors in the API connection.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


def exception_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError as e:
            raise OasisBrApiConnectionError(e)

    return inner
