from __future__ import annotations

from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

from sandbox0.apispec.api.functions import get_api_v1_functions
from sandbox0.apispec.api.functions import get_api_v1_functions_id
from sandbox0.apispec.api.functions import get_api_v1_functions_id_revisions
from sandbox0.apispec.api.functions import post_api_v1_functions
from sandbox0.apispec.api.functions import post_api_v1_functions_id_revisions
from sandbox0.apispec.api.functions import put_api_v1_functions_id_aliases_alias
from sandbox0.apispec.models.function_alias import FunctionAlias
from sandbox0.apispec.models.function_alias_update_request import FunctionAliasUpdateRequest
from sandbox0.apispec.models.function_create_request import FunctionCreateRequest
from sandbox0.apispec.models.function_record import FunctionRecord
from sandbox0.apispec.models.function_revision import FunctionRevision
from sandbox0.apispec.models.function_revision_create_request import FunctionRevisionCreateRequest
from sandbox0.apispec.models.function_source_request import FunctionSourceRequest
from sandbox0.apispec.models.success_function_alias_response import SuccessFunctionAliasResponse
from sandbox0.apispec.models.success_function_create_response import SuccessFunctionCreateResponse
from sandbox0.apispec.models.success_function_list_response import SuccessFunctionListResponse
from sandbox0.apispec.models.success_function_response import SuccessFunctionResponse
from sandbox0.apispec.models.success_function_revision_create_response import (
    SuccessFunctionRevisionCreateResponse,
)
from sandbox0.apispec.models.success_function_revision_list_response import (
    SuccessFunctionRevisionListResponse,
)
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.client import Client


@dataclass(frozen=True)
class FunctionCreateResult:
    function: FunctionRecord
    revision: FunctionRevision
    alias: FunctionAlias


@dataclass(frozen=True)
class FunctionRevisionCreateResult:
    revision: FunctionRevision
    promoted: bool


def function_source(sandbox_id: str, service_id: str) -> FunctionSourceRequest:
    return FunctionSourceRequest(sandbox_id=sandbox_id, service_id=service_id)


class ClientFunctionsMixin:
    _api: Any

    def list_functions(self: "Client") -> list[FunctionRecord]:  # type: ignore[misc]
        return _list_functions(self._api)

    def get_function(self: "Client", function_id: str) -> FunctionRecord:  # type: ignore[misc]
        return _get_function(self._api, function_id)

    def create_function(self: "Client", request: FunctionCreateRequest) -> FunctionCreateResult:  # type: ignore[misc]
        return _create_function(self._api, request)

    def create_function_from_sandbox(
        self: "Client",
        sandbox_id: str,
        service_id: str,
        *,
        name: str | None = None,
    ) -> FunctionCreateResult:  # type: ignore[misc]
        return _create_function_from_sandbox(self._api, sandbox_id, service_id, name=name)

    def list_function_revisions(self: "Client", function_id: str) -> list[FunctionRevision]:  # type: ignore[misc]
        return _list_function_revisions(self._api, function_id)

    def create_function_revision(
        self: "Client",
        function_id: str,
        request: FunctionRevisionCreateRequest,
    ) -> FunctionRevisionCreateResult:  # type: ignore[misc]
        return _create_function_revision(self._api, function_id, request)

    def create_function_revision_from_sandbox(
        self: "Client",
        function_id: str,
        sandbox_id: str,
        service_id: str,
        *,
        promote: bool | None = None,
    ) -> FunctionRevisionCreateResult:  # type: ignore[misc]
        return _create_function_revision_from_sandbox(
            self._api,
            function_id,
            sandbox_id,
            service_id,
            promote=promote,
        )

    def set_function_alias(self: "Client", function_id: str, alias: str, revision_number: int) -> FunctionAlias:  # type: ignore[misc]
        return _set_function_alias(self._api, function_id, alias, revision_number)


class Functions:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def list(self) -> list[FunctionRecord]:
        return _list_functions(self._client.api)

    def get(self, function_id: str) -> FunctionRecord:
        return _get_function(self._client.api, function_id)

    def create(self, request: FunctionCreateRequest) -> FunctionCreateResult:
        return _create_function(self._client.api, request)

    def create_from_sandbox(
        self,
        sandbox_id: str,
        service_id: str,
        *,
        name: str | None = None,
    ) -> FunctionCreateResult:
        return _create_function_from_sandbox(self._client.api, sandbox_id, service_id, name=name)

    def list_revisions(self, function_id: str) -> list[FunctionRevision]:
        return _list_function_revisions(self._client.api, function_id)

    def create_revision(self, function_id: str, request: FunctionRevisionCreateRequest) -> FunctionRevisionCreateResult:
        return _create_function_revision(self._client.api, function_id, request)

    def create_revision_from_sandbox(
        self,
        function_id: str,
        sandbox_id: str,
        service_id: str,
        *,
        promote: bool | None = None,
    ) -> FunctionRevisionCreateResult:
        return _create_function_revision_from_sandbox(
            self._client.api,
            function_id,
            sandbox_id,
            service_id,
            promote=promote,
        )

    def set_alias(self, function_id: str, alias: str, revision_number: int) -> FunctionAlias:
        return _set_function_alias(self._client.api, function_id, alias, revision_number)


def _list_functions(api: Any) -> list[FunctionRecord]:
    resp = get_api_v1_functions.sync_detailed(client=api)
    data = ensure_data(resp, SuccessFunctionListResponse)
    return data.functions


def _get_function(api: Any, function_id: str) -> FunctionRecord:
    resp = get_api_v1_functions_id.sync_detailed(id=function_id, client=api)
    data = ensure_data(resp, SuccessFunctionResponse)
    return data.function


def _create_function(api: Any, request: FunctionCreateRequest) -> FunctionCreateResult:
    resp = post_api_v1_functions.sync_detailed(client=api, body=request)
    data = ensure_data(resp, SuccessFunctionCreateResponse)
    return FunctionCreateResult(function=data.function, revision=data.revision, alias=data.alias)


def _create_function_from_sandbox(
    api: Any,
    sandbox_id: str,
    service_id: str,
    *,
    name: str | None = None,
) -> FunctionCreateResult:
    request = FunctionCreateRequest(source=function_source(sandbox_id, service_id))
    if name is not None:
        request.name = name
    return _create_function(api, request)


def _list_function_revisions(api: Any, function_id: str) -> list[FunctionRevision]:
    resp = get_api_v1_functions_id_revisions.sync_detailed(id=function_id, client=api)
    data = ensure_data(resp, SuccessFunctionRevisionListResponse)
    return data.revisions


def _create_function_revision(
    api: Any,
    function_id: str,
    request: FunctionRevisionCreateRequest,
) -> FunctionRevisionCreateResult:
    resp = post_api_v1_functions_id_revisions.sync_detailed(id=function_id, client=api, body=request)
    data = ensure_data(resp, SuccessFunctionRevisionCreateResponse)
    return FunctionRevisionCreateResult(revision=data.revision, promoted=data.promoted)


def _create_function_revision_from_sandbox(
    api: Any,
    function_id: str,
    sandbox_id: str,
    service_id: str,
    *,
    promote: bool | None = None,
) -> FunctionRevisionCreateResult:
    request = FunctionRevisionCreateRequest(source=function_source(sandbox_id, service_id))
    if promote is not None:
        request.promote = promote
    return _create_function_revision(api, function_id, request)


def _set_function_alias(api: Any, function_id: str, alias: str, revision_number: int) -> FunctionAlias:
    resp = put_api_v1_functions_id_aliases_alias.sync_detailed(
        id=function_id,
        alias=alias,
        client=api,
        body=FunctionAliasUpdateRequest(revision_number=revision_number),
    )
    data = ensure_data(resp, SuccessFunctionAliasResponse)
    return data.alias
