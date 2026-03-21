from enum import Enum


class CredentialProjectionType(str, Enum):
    HTTP_HEADERS = "http_headers"
    TLS_CLIENT_CERTIFICATE = "tls_client_certificate"
    USERNAME_PASSWORD = "username_password"

    def __str__(self) -> str:
        return str(self.value)
