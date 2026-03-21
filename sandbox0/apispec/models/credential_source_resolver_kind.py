from enum import Enum


class CredentialSourceResolverKind(str, Enum):
    STATIC_HEADERS = "static_headers"
    STATIC_TLS_CLIENT_CERTIFICATE = "static_tls_client_certificate"
    STATIC_USERNAME_PASSWORD = "static_username_password"

    def __str__(self) -> str:
        return str(self.value)
