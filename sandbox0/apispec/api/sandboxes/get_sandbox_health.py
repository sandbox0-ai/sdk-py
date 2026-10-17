from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_health_response import SuccessSandboxHealthResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/health".format(
            id=id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxHealthResponse.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]:
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]:
    """Observe independent runtime, execution, terminal and storage health

     Requires sandbox:read. Reads owner-scoped regional authority and bounded independent node and guest
    diagnostics without automatic resume, restart or credential preparation. Guest diagnostics may
    execute a fixed short shell command and allocate a temporary PTY; they create no platform session.
    No probe runs for a paused runtime or a pending lifecycle. Each observation has its own source and
    time. Guest results are advisory and cannot establish runtime or storage authority. Unknown means
    insufficient evidence, not success. A valid launch receipt is not current process liveness; RootFS
    identity and writer lease are not successful storage IO or a guarantee of uncommitted-write
    durability. Storage IO currently remains unknown. Authority is rechecked after probes so a changed
    generation or lifecycle cannot inherit a successful old-runtime observation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]:
    """Observe independent runtime, execution, terminal and storage health

     Requires sandbox:read. Reads owner-scoped regional authority and bounded independent node and guest
    diagnostics without automatic resume, restart or credential preparation. Guest diagnostics may
    execute a fixed short shell command and allocate a temporary PTY; they create no platform session.
    No probe runs for a paused runtime or a pending lifecycle. Each observation has its own source and
    time. Guest results are advisory and cannot establish runtime or storage authority. Unknown means
    insufficient evidence, not success. A valid launch receipt is not current process liveness; RootFS
    identity and writer lease are not successful storage IO or a guarantee of uncommitted-write
    durability. Storage IO currently remains unknown. Authority is rechecked after probes so a changed
    generation or lifecycle cannot inherit a successful old-runtime observation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxHealthResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]:
    """Observe independent runtime, execution, terminal and storage health

     Requires sandbox:read. Reads owner-scoped regional authority and bounded independent node and guest
    diagnostics without automatic resume, restart or credential preparation. Guest diagnostics may
    execute a fixed short shell command and allocate a temporary PTY; they create no platform session.
    No probe runs for a paused runtime or a pending lifecycle. Each observation has its own source and
    time. Guest results are advisory and cannot establish runtime or storage authority. Unknown means
    insufficient evidence, not success. A valid launch receipt is not current process liveness; RootFS
    identity and writer lease are not successful storage IO or a guarantee of uncommitted-write
    durability. Storage IO currently remains unknown. Authority is rechecked after probes so a changed
    generation or lifecycle cannot inherit a successful old-runtime observation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxHealthResponse]]:
    """Observe independent runtime, execution, terminal and storage health

     Requires sandbox:read. Reads owner-scoped regional authority and bounded independent node and guest
    diagnostics without automatic resume, restart or credential preparation. Guest diagnostics may
    execute a fixed short shell command and allocate a temporary PTY; they create no platform session.
    No probe runs for a paused runtime or a pending lifecycle. Each observation has its own source and
    time. Guest results are advisory and cannot establish runtime or storage authority. Unknown means
    insufficient evidence, not success. A valid launch receipt is not current process liveness; RootFS
    identity and writer lease are not successful storage IO or a guarantee of uncommitted-write
    durability. Storage IO currently remains unknown. Authority is rechecked after probes so a changed
    generation or lifecycle cannot inherit a successful old-runtime observation.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxHealthResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
