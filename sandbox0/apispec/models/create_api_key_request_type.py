from enum import Enum


class CreateAPIKeyRequestType(str, Enum):
    SERVICE = "service"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
