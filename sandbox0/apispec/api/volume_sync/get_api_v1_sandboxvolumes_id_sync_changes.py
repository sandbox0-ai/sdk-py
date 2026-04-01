from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_volume_sync_change_list_response import (
    SuccessVolumeSyncChangeListResponse,
)
from ...models.volume_sync_reseed_required_error_envelope import (
    VolumeSyncReseedRequiredErrorEnvelope,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    after: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 256,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["after"] = after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxvolumes/{id}/sync/changes".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
]:
    if response.status_code == 200:
        response_200 = SuccessVolumeSyncChangeListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = VolumeSyncReseedRequiredErrorEnvelope.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
]:
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
    after: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 256,
) -> Response[
    Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
]:
    """List volume sync journal entries

    Args:
        id (str):
        after (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
        after=after,
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
    after: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 256,
) -> Optional[
    Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
]:
    """List volume sync journal entries

    Args:
        id (str):
        after (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
    """

    return sync_detailed(
        id=id,
        client=client,
        after=after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 256,
) -> Response[
    Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
]:
    """List volume sync journal entries

    Args:
        id (str):
        after (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
        after=after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 256,
) -> Optional[
    Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
]:
    """List volume sync journal entries

    Args:
        id (str):
        after (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SuccessVolumeSyncChangeListResponse, VolumeSyncReseedRequiredErrorEnvelope]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            after=after,
            limit=limit,
        )
    ).parsed
