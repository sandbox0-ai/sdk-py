from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    process_id: str,
    *,
    cursor: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/processes/{process_id}/events".format(
            id=id,
            process_id=process_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[str]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, int] = UNSET,
) -> Response[str]:
    """Stream process events

     Streams replayed and live process events as Server-Sent Events. cursor is the last observed event
    seq; procd emits cursor_lost if the requested cursor is older than the retained log.

    Args:
        id (str):
        process_id (str):
        cursor (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        id=id,
        process_id=process_id,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, int] = UNSET,
) -> Optional[str]:
    """Stream process events

     Streams replayed and live process events as Server-Sent Events. cursor is the last observed event
    seq; procd emits cursor_lost if the requested cursor is older than the retained log.

    Args:
        id (str):
        process_id (str):
        cursor (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        id=id,
        process_id=process_id,
        client=client,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, int] = UNSET,
) -> Response[str]:
    """Stream process events

     Streams replayed and live process events as Server-Sent Events. cursor is the last observed event
    seq; procd emits cursor_lost if the requested cursor is older than the retained log.

    Args:
        id (str):
        process_id (str):
        cursor (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        id=id,
        process_id=process_id,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, int] = UNSET,
) -> Optional[str]:
    """Stream process events

     Streams replayed and live process events as Server-Sent Events. cursor is the last observed event
    seq; procd emits cursor_lost if the requested cursor is older than the retained log.

    Args:
        id (str):
        process_id (str):
        cursor (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            id=id,
            process_id=process_id,
            client=client,
            cursor=cursor,
        )
    ).parsed
