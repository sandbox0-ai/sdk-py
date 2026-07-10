from enum import Enum


class SandboxRuntimeMetricGapReason(str, Enum):
    COLLECTION_ERROR = "collection_error"
    NO_DATA = "no_data"
    SERIES_RESET = "series_reset"
    UNAVAILABLE = "unavailable"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
