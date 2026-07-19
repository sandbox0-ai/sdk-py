from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_sandbox_root_fs_snapshot_request import (
    CreateSandboxRootFSSnapshotRequest,
)
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_root_fs_snapshot_response import (
    SuccessSandboxRootFSSnapshotResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CreateSandboxRootFSSnapshotRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/snapshots".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    if response.status_code == 201:
        response_201 = SuccessSandboxRootFSSnapshotResponse.from_dict(response.json())

        return response_201

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
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
    body: CreateSandboxRootFSSnapshotRequest,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Create sandbox rootfs snapshot

     Creates an immutable snapshot record from the source sandbox writable
    rootfs. A paused source is snapshotted from its current rootfs head. A
    running source is briefly barriered and checkpointed first; the source
    sandbox remains running after the snapshot operation completes.

    Args:
        id (str):
        body (CreateSandboxRootFSSnapshotRequest): Optional snapshot metadata. The source sandbox
            may be running or paused;
            running sources are checkpointed before the snapshot record is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateSandboxRootFSSnapshotRequest,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Create sandbox rootfs snapshot

     Creates an immutable snapshot record from the source sandbox writable
    rootfs. A paused source is snapshotted from its current rootfs head. A
    running source is briefly barriered and checkpointed first; the source
    sandbox remains running after the snapshot operation completes.

    Args:
        id (str):
        body (CreateSandboxRootFSSnapshotRequest): Optional snapshot metadata. The source sandbox
            may be running or paused;
            running sources are checkpointed before the snapshot record is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateSandboxRootFSSnapshotRequest,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Create sandbox rootfs snapshot

     Creates an immutable snapshot record from the source sandbox writable
    rootfs. A paused source is snapshotted from its current rootfs head. A
    running source is briefly barriered and checkpointed first; the source
    sandbox remains running after the snapshot operation completes.

    Args:
        id (str):
        body (CreateSandboxRootFSSnapshotRequest): Optional snapshot metadata. The source sandbox
            may be running or paused;
            running sources are checkpointed before the snapshot record is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateSandboxRootFSSnapshotRequest,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Create sandbox rootfs snapshot

     Creates an immutable snapshot record from the source sandbox writable
    rootfs. A paused source is snapshotted from its current rootfs head. A
    running source is briefly barriered and checkpointed first; the source
    sandbox remains running after the snapshot operation completes.

    Args:
        id (str):
        body (CreateSandboxRootFSSnapshotRequest): Optional snapshot metadata. The source sandbox
            may be running or paused;
            running sources are checkpointed before the snapshot record is created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
