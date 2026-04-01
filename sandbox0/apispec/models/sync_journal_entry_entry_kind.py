from enum import Enum


class SyncJournalEntryEntryKind(str, Enum):
    DIRECTORY = "directory"
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
