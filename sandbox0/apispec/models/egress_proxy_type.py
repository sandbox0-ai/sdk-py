from enum import Enum


class EgressProxyType(str, Enum):
    SOCKS5 = "socks5"

    def __str__(self) -> str:
        return str(self.value)
