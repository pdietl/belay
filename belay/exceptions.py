class BelayException(Exception):
    """Root Belay Exception class."""


class AuthenticationError(BelayException):
    """Invalid password or similar."""


class FeatureUnavailableError(BelayException):
    """Feature unavailable for your board's implementation."""


class SpecialFunctionNameError(BelayException):
    """Reserved function name that may impact Belay functionality.

    Currently limited to:

        * Names that start and end with double underscore, ``__``.

        * Names that start with ``_belay`` or ``__belay``
    """


class ReconstructionError(BelayException):
    """Too many commands were given."""


class ConnectionLost(BelayException):
    """Lost connection to device."""
