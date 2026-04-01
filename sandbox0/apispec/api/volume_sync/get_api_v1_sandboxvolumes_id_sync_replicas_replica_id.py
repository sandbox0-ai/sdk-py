from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_volume_sync_replica_response import (
    SuccessVolumeSyncReplicaResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    replica_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxvolumes/{id}/sync/replicas/{replica_id}".format(
            id=id,
            replica_id=replica_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]:
    if response.status_code == 200:
        response_200 = SuccessVolumeSyncReplicaResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]:
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
) -> Response[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]:
    """Get a volume sync replica

    Args:
        id (str):
        replica_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        replica_id=replica_id,
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
) -> Optional[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]:
    """Get a volume sync replica

    Args:
        id (str):
        replica_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]
    """

    return sync_detailed(
        id=id,
        replica_id=replica_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    replica_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]:
    """Get a volume sync replica

    Args:
        id (str):
        replica_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        replica_id=replica_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    replica_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]]:
    """Get a volume sync replica

    Args:
        id (str):
        replica_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessVolumeSyncReplicaResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            replica_id=replica_id,
            client=client,
        )
    ).parsed
