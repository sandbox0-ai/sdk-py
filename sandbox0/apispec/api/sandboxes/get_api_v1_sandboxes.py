from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_api_v1_sandboxes_status import GetApiV1SandboxesStatus
from ...models.success_sandbox_list_response import SuccessSandboxListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: Union[Unset, GetApiV1SandboxesStatus] = UNSET,
    template_id: Union[Unset, str] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["template_id"] = template_id

    params["paused"] = paused

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxListResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetApiV1SandboxesStatus] = UNSET,
    template_id: Union[Unset, str] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorEnvelope, SuccessSandboxListResponse]]:
    """List sandboxes

     List all sandboxes for the authenticated team. In multi-cluster mode, this endpoint aggregates
    results from all enabled clusters.

    Args:
        status (Union[Unset, GetApiV1SandboxesStatus]):
        template_id (Union[Unset, str]):
        paused (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxListResponse]]
    """

    kwargs = _get_kwargs(
        status=status,
        template_id=template_id,
        paused=paused,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetApiV1SandboxesStatus] = UNSET,
    template_id: Union[Unset, str] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxListResponse]]:
    """List sandboxes

     List all sandboxes for the authenticated team. In multi-cluster mode, this endpoint aggregates
    results from all enabled clusters.

    Args:
        status (Union[Unset, GetApiV1SandboxesStatus]):
        template_id (Union[Unset, str]):
        paused (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxListResponse]
    """

    return sync_detailed(
        client=client,
        status=status,
        template_id=template_id,
        paused=paused,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetApiV1SandboxesStatus] = UNSET,
    template_id: Union[Unset, str] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Response[Union[ErrorEnvelope, SuccessSandboxListResponse]]:
    """List sandboxes

     List all sandboxes for the authenticated team. In multi-cluster mode, this endpoint aggregates
    results from all enabled clusters.

    Args:
        status (Union[Unset, GetApiV1SandboxesStatus]):
        template_id (Union[Unset, str]):
        paused (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxListResponse]]
    """

    kwargs = _get_kwargs(
        status=status,
        template_id=template_id,
        paused=paused,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetApiV1SandboxesStatus] = UNSET,
    template_id: Union[Unset, str] = UNSET,
    paused: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 50,
    offset: Union[Unset, int] = 0,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxListResponse]]:
    """List sandboxes

     List all sandboxes for the authenticated team. In multi-cluster mode, this endpoint aggregates
    results from all enabled clusters.

    Args:
        status (Union[Unset, GetApiV1SandboxesStatus]):
        template_id (Union[Unset, str]):
        paused (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 50.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            template_id=template_id,
            paused=paused,
            limit=limit,
            offset=offset,
        )
    ).parsed
