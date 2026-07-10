from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    session_id: str,
    *,
    after: Union[Unset, int] = UNSET,
    last_event_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(last_event_id, Unset):
        headers["Last-Event-ID"] = last_event_id

    params: dict[str, Any] = {}

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/sessions/{session_id}/events/stream".format(
            id=id,
            session_id=session_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
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
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    last_event_id: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Stream execution session events

     Streams retained and live events using SSE. Reconnect with Last-Event-ID or the after query
    parameter.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        last_event_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        after=after,
        last_event_id=last_event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    last_event_id: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Stream execution session events

     Streams retained and live events using SSE. Reconnect with Last-Event-ID or the after query
    parameter.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        last_event_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        id=id,
        session_id=session_id,
        client=client,
        after=after,
        last_event_id=last_event_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    last_event_id: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Stream execution session events

     Streams retained and live events using SSE. Reconnect with Last-Event-ID or the after query
    parameter.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        last_event_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        after=after,
        last_event_id=last_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    last_event_id: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Stream execution session events

     Streams retained and live events using SSE. Reconnect with Last-Event-ID or the after query
    parameter.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        last_event_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            id=id,
            session_id=session_id,
            client=client,
            after=after,
            last_event_id=last_event_id,
        )
    ).parsed
