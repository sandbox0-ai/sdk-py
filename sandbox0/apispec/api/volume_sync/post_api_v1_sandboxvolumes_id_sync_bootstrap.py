from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_volume_sync_bootstrap_request import (
    CreateVolumeSyncBootstrapRequest,
)
from ...models.success_volume_sync_bootstrap_response import (
    SuccessVolumeSyncBootstrapResponse,
)
from ...models.volume_sync_bootstrap_conflict_error_envelope import (
    VolumeSyncBootstrapConflictErrorEnvelope,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CreateVolumeSyncBootstrapRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxvolumes/{id}/sync/bootstrap".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
]:
    if response.status_code == 201:
        response_201 = SuccessVolumeSyncBootstrapResponse.from_dict(response.json())

        return response_201

    if response.status_code == 409:
        response_409 = VolumeSyncBootstrapConflictErrorEnvelope.from_dict(
            response.json()
        )

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
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
    body: CreateVolumeSyncBootstrapRequest,
) -> Response[
    Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
]:
    """Create a bootstrap snapshot and journal anchor for local-first sync

    Args:
        id (str):
        body (CreateVolumeSyncBootstrapRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]]
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
    body: CreateVolumeSyncBootstrapRequest,
) -> Optional[
    Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
]:
    """Create a bootstrap snapshot and journal anchor for local-first sync

    Args:
        id (str):
        body (CreateVolumeSyncBootstrapRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
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
    body: CreateVolumeSyncBootstrapRequest,
) -> Response[
    Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
]:
    """Create a bootstrap snapshot and journal anchor for local-first sync

    Args:
        id (str):
        body (CreateVolumeSyncBootstrapRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]]
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
    body: CreateVolumeSyncBootstrapRequest,
) -> Optional[
    Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
]:
    """Create a bootstrap snapshot and journal anchor for local-first sync

    Args:
        id (str):
        body (CreateVolumeSyncBootstrapRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SuccessVolumeSyncBootstrapResponse, VolumeSyncBootstrapConflictErrorEnvelope]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
