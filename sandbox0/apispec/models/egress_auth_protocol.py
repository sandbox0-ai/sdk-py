from enum import Enum

class EgressAuthProtocol(str, Enum):
    GRPC = "grpc"
    HTTP = "http"
    HTTPS = "https"
    MQTT = "mqtt"
    REDIS = "redis"
    SOCKS5 = "socks5"
    SSH = "ssh"
    TLS = "tls"

    def __str__(self) -> str:
        return str(self.value)
