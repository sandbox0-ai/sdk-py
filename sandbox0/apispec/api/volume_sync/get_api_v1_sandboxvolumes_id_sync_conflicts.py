from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_volume_sync_conflict_list_response import (
    SuccessVolumeSyncConflictListResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    status: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 256,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["status"] = status

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxvolumes/{id}/sync/conflicts".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessVolumeSyncConflictListResponse]:
    if response.status_code == 200:
        response_200 = SuccessVolumeSyncConflictListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessVolumeSyncConflictListResponse]:
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
    status: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 256,
) -> Response[SuccessVolumeSyncConflictListResponse]:
    """List volume sync conflicts

    Args:
        id (str):
        status (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessVolumeSyncConflictListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 256,
) -> Optional[SuccessVolumeSyncConflictListResponse]:
    """List volume sync conflicts

    Args:
        id (str):
        status (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessVolumeSyncConflictListResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        status=status,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 256,
) -> Response[SuccessVolumeSyncConflictListResponse]:
    """List volume sync conflicts

    Args:
        id (str):
        status (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessVolumeSyncConflictListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 256,
) -> Optional[SuccessVolumeSyncConflictListResponse]:
    """List volume sync conflicts

    Args:
        id (str):
        status (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessVolumeSyncConflictListResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            status=status,
            limit=limit,
        )
    ).parsed
