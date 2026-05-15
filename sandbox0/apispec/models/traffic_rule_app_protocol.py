from enum import Enum

class TrafficRuleAppProtocol(str, Enum):
    AMQP = "amqp"
    DNS = "dns"
    HTTP = "http"
    MONGODB = "mongodb"
    MQTT = "mqtt"
    REDIS = "redis"
    SOCKS5 = "socks5"
    SSH = "ssh"
    TLS = "tls"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
