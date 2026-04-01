from enum import Enum


class SyncJournalEntrySource(str, Enum):
    REPLICA = "replica"
    SANDBOX = "sandbox"

    def __str__(self) -> str:
        return str(self.value)
