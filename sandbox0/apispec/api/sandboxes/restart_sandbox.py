from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.sandbox_restart_request import SandboxRestartRequest
from ...models.success_sandbox_restart_operation_response import (
    SuccessSandboxRestartOperationResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SandboxRestartRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/restart".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRestartOperationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = SuccessSandboxRestartOperationResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SandboxRestartRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Explicitly replace a sandbox runtime and discard process state

     Preserves the writable RootFS through external publication and writer fencing,
    ends the old processes, and starts a fresh runtime. This is not a reconnect,
    memory restore, or snapshot rollback. Requires sandbox:write and a stable
    Idempotency-Key bound to expected_runtime_generation. A duplicate returns
    the original operation and never restarts a newer generation. Request
    timeout does not cancel committed work. Find the operation by request_key
    if its acknowledgement was lost. Completion proves runtime replacement,
    not guest application health. Never use this as an automatic memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRestartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SandboxRestartRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Explicitly replace a sandbox runtime and discard process state

     Preserves the writable RootFS through external publication and writer fencing,
    ends the old processes, and starts a fresh runtime. This is not a reconnect,
    memory restore, or snapshot rollback. Requires sandbox:write and a stable
    Idempotency-Key bound to expected_runtime_generation. A duplicate returns
    the original operation and never restarts a newer generation. Request
    timeout does not cancel committed work. Find the operation by request_key
    if its acknowledgement was lost. Completion proves runtime replacement,
    not guest application health. Never use this as an automatic memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRestartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SandboxRestartRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Explicitly replace a sandbox runtime and discard process state

     Preserves the writable RootFS through external publication and writer fencing,
    ends the old processes, and starts a fresh runtime. This is not a reconnect,
    memory restore, or snapshot rollback. Requires sandbox:write and a stable
    Idempotency-Key bound to expected_runtime_generation. A duplicate returns
    the original operation and never restarts a newer generation. Request
    timeout does not cancel committed work. Find the operation by request_key
    if its acknowledgement was lost. Completion proves runtime replacement,
    not guest application health. Never use this as an automatic memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRestartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SandboxRestartRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Explicitly replace a sandbox runtime and discard process state

     Preserves the writable RootFS through external publication and writer fencing,
    ends the old processes, and starts a fresh runtime. This is not a reconnect,
    memory restore, or snapshot rollback. Requires sandbox:write and a stable
    Idempotency-Key bound to expected_runtime_generation. A duplicate returns
    the original operation and never restarts a newer generation. Request
    timeout does not cancel committed work. Find the operation by request_key
    if its acknowledgement was lost. Completion proves runtime replacement,
    not guest application health. Never use this as an automatic memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRestartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
