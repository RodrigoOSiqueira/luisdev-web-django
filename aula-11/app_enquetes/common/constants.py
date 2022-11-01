from enum import Enum


class HTTPMethod(str, Enum):
    POST = "POST"
    GET = "GET"
