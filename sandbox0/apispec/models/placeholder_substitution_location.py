from enum import Enum


class PlaceholderSubstitutionLocation(str, Enum):
    BODY = "body"
    HEADER = "header"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
