from enum import Enum


class EgressTLSMode(str, Enum):
    PASSTHROUGH = "passthrough"
    TERMINATE_REORIGINATE = "terminate-reoriginate"

    def __str__(self) -> str:
        return str(self.value)
