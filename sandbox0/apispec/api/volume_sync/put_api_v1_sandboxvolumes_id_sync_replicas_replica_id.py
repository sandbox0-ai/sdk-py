from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_volume_sync_replica_response import (
    SuccessVolumeSyncReplicaResponse,
)
from ...models.upsert_sync_replica_request import UpsertSyncReplicaRequest
from ...types import Response


def _get_kwargs(
    id: str,
    replica_id: str,
    *,
    body: UpsertSyncReplicaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/sandboxvolumes/{id}/sync/replicas/{replica_id}".format(
            id=id,
            replica_id=replica_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessVolumeSyncReplicaResponse]:
    if response.status_code == 200:
        response_200 = SuccessVolumeSyncReplicaResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessVolumeSyncReplicaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    replica_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertSyncReplicaRequest,
) -> Response[SuccessVolumeSyncReplicaResponse]:
    """Register or update a volume sync replica

    Args:
        id (str):
        replica_id (str):
        body (UpsertSyncReplicaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessVolumeSyncReplicaResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        replica_id=replica_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    replica_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertSyncReplicaRequest,
) -> Optional[SuccessVolumeSyncReplicaResponse]:
    """Register or update a volume sync replica

    Args:
        id (str):
        replica_id (str):
        body (UpsertSyncReplicaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessVolumeSyncReplicaResponse
    """

    return sync_detailed(
        id=id,
        replica_id=replica_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    replica_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertSyncReplicaRequest,
) -> Response[SuccessVolumeSyncReplicaResponse]:
    """Register or update a volume sync replica

    Args:
        id (str):
        replica_id (str):
        body (UpsertSyncReplicaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessVolumeSyncReplicaResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        replica_id=replica_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    replica_id: str,
    *,
    client: AuthenticatedClient,
    body: UpsertSyncReplicaRequest,
) -> Optional[SuccessVolumeSyncReplicaResponse]:
    """Register or update a volume sync replica

    Args:
        id (str):
        replica_id (str):
        body (UpsertSyncReplicaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessVolumeSyncReplicaResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            replica_id=replica_id,
            client=client,
            body=body,
        )
    ).parsed
