from __future__ import annotations

from typing import Any, TYPE_CHECKING

from sandbox0.apispec.api.credential_sources import delete_api_v1_credential_sources_name
from sandbox0.apispec.api.credential_sources import get_api_v1_credential_sources
from sandbox0.apispec.api.credential_sources import get_api_v1_credential_sources_name
from sandbox0.apispec.api.credential_sources import post_api_v1_credential_sources
from sandbox0.apispec.api.credential_sources import put_api_v1_credential_sources_name
from sandbox0.apispec.models.credential_source_metadata import CredentialSourceMetadata
from sandbox0.apispec.models.credential_source_write_request import CredentialSourceWriteRequest
from sandbox0.apispec.models.success_credential_source_list_response import SuccessCredentialSourceListResponse
from sandbox0.apispec.models.success_credential_source_response import SuccessCredentialSourceResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.client import Client


class ClientCredentialSourcesMixin:
    _api: Any

    def list_credential_sources(self: "Client") -> list[CredentialSourceMetadata]:  # type: ignore[misc]
        resp = get_api_v1_credential_sources.sync_detailed(client=self._api)
        data = ensure_data(resp, SuccessCredentialSourceListResponse)
        return data

    def get_credential_source(self: "Client", name: str) -> CredentialSourceMetadata:  # type: ignore[misc]
        resp = get_api_v1_credential_sources_name.sync_detailed(name=name, client=self._api)
        return ensure_data(resp, SuccessCredentialSourceResponse)

    def create_credential_source(self: "Client", request: CredentialSourceWriteRequest) -> CredentialSourceMetadata:  # type: ignore[misc]
        resp = post_api_v1_credential_sources.sync_detailed(client=self._api, body=request)
        return ensure_data(resp, SuccessCredentialSourceResponse)

    def update_credential_source(self: "Client", name: str, request: CredentialSourceWriteRequest) -> CredentialSourceMetadata:  # type: ignore[misc]
        request.name = name
        resp = put_api_v1_credential_sources_name.sync_detailed(name=name, client=self._api, body=request)
        return ensure_data(resp, SuccessCredentialSourceResponse)

    def delete_credential_source(self: "Client", name: str) -> SuccessMessageResponse:  # type: ignore[misc]
        resp = delete_api_v1_credential_sources_name.sync_detailed(name=name, client=self._api)
        return ensure_model(resp, SuccessMessageResponse)
