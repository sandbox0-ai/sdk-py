from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_execution_session_response import SuccessExecutionSessionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    params["creation_runtime_generation"] = creation_runtime_generation

    params["runtime_generation"] = runtime_generation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/sessions/conditional/lookup".format(
            id=id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    if response.status_code == 200:
        response_200 = SuccessExecutionSessionResponse.from_dict(response.json())

        return response_200

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
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
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
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Find a conditional session by its original creation key

     Read-only receipt lookup in an exact currently running generation. Never auto-resumes, creates a
    session, starts an attempt or repairs state. Both the gateway and supervisor verify the sandbox and
    runtime generation. Only conditional creations are eligible. A session_not_found response means that
    key was absent at observation time, not permission to create or proof that an earlier request cannot
    still finish. Other 404 replies may indicate unsupported servers. Clients must not fall back to
    ordinary queries or creation. The returned receipt is not lifecycle/storage authority, current
    credential admission, or permission to attach later. For a memory-restored original attempt,
    explicitly supply an earlier creation_runtime_generation. Omission retains same-generation
    semantics. The supervisor requires the exact original conditional creation and a still-running
    attempt from that origin in the requested current runtime. This does not verify external memory
    lineage or credential qualification; applications must verify those independently before adoption.
    Never use failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        creation_runtime_generation=creation_runtime_generation,
        runtime_generation=runtime_generation,
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
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Find a conditional session by its original creation key

     Read-only receipt lookup in an exact currently running generation. Never auto-resumes, creates a
    session, starts an attempt or repairs state. Both the gateway and supervisor verify the sandbox and
    runtime generation. Only conditional creations are eligible. A session_not_found response means that
    key was absent at observation time, not permission to create or proof that an earlier request cannot
    still finish. Other 404 replies may indicate unsupported servers. Clients must not fall back to
    ordinary queries or creation. The returned receipt is not lifecycle/storage authority, current
    credential admission, or permission to attach later. For a memory-restored original attempt,
    explicitly supply an earlier creation_runtime_generation. Omission retains same-generation
    semantics. The supervisor requires the exact original conditional creation and a still-running
    attempt from that origin in the requested current runtime. This does not verify external memory
    lineage or credential qualification; applications must verify those independently before adoption.
    Never use failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        creation_runtime_generation=creation_runtime_generation,
        runtime_generation=runtime_generation,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Find a conditional session by its original creation key

     Read-only receipt lookup in an exact currently running generation. Never auto-resumes, creates a
    session, starts an attempt or repairs state. Both the gateway and supervisor verify the sandbox and
    runtime generation. Only conditional creations are eligible. A session_not_found response means that
    key was absent at observation time, not permission to create or proof that an earlier request cannot
    still finish. Other 404 replies may indicate unsupported servers. Clients must not fall back to
    ordinary queries or creation. The returned receipt is not lifecycle/storage authority, current
    credential admission, or permission to attach later. For a memory-restored original attempt,
    explicitly supply an earlier creation_runtime_generation. Omission retains same-generation
    semantics. The supervisor requires the exact original conditional creation and a still-running
    attempt from that origin in the requested current runtime. This does not verify external memory
    lineage or credential qualification; applications must verify those independently before adoption.
    Never use failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        creation_runtime_generation=creation_runtime_generation,
        runtime_generation=runtime_generation,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Find a conditional session by its original creation key

     Read-only receipt lookup in an exact currently running generation. Never auto-resumes, creates a
    session, starts an attempt or repairs state. Both the gateway and supervisor verify the sandbox and
    runtime generation. Only conditional creations are eligible. A session_not_found response means that
    key was absent at observation time, not permission to create or proof that an earlier request cannot
    still finish. Other 404 replies may indicate unsupported servers. Clients must not fall back to
    ordinary queries or creation. The returned receipt is not lifecycle/storage authority, current
    credential admission, or permission to attach later. For a memory-restored original attempt,
    explicitly supply an earlier creation_runtime_generation. Omission retains same-generation
    semantics. The supervisor requires the exact original conditional creation and a still-running
    attempt from that origin in the requested current runtime. This does not verify external memory
    lineage or credential qualification; applications must verify those independently before adoption.
    Never use failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            creation_runtime_generation=creation_runtime_generation,
            runtime_generation=runtime_generation,
            idempotency_key=idempotency_key,
        )
    ).parsed
