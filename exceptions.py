class BaseError(Exception):
    message = NotImplemented


class RequestError(BaseError):
    message = NotImplemented

class LogisticError(BaseError):
    message = NotImplemented

class NotEnoughSpace(LogisticError):
    message = 'Not enogh space in stol'

class NotEnoughProduct(LogisticError):
    message = ' Not enough goods'

class UnknownProduct(LogisticError):
    message = 'Unknown'

class TooManyDifferentProducts(LogisticError):
    message = "Too many different products"

class InvalidRequest(RequestError):
    message = ""

class InvalidStorageName(RequestError):
    message = ""
