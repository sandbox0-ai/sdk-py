from enum import Enum


class CredentialProjectionType(str, Enum):
    HTTP_HEADERS = "http_headers"
    SSH_PROXY = "ssh_proxy"
    TLS_CLIENT_CERTIFICATE = "tls_client_certificate"
    USERNAME_PASSWORD = "username_password"

    def __str__(self) -> str:
        return str(self.value)
