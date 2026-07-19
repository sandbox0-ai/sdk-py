from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    session_id: str,
    *,
    after: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/sessions/{session_id}/ws".format(
            id=id,
            session_id=session_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorEnvelope]]:
    if response.status_code == 101:
        response_101 = cast(Any, None)
        return response_101

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
) -> Response[Union[Any, ErrorEnvelope]]:
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
) -> Response[Union[Any, ErrorEnvelope]]:
    """Attach to an execution session with WebSocket

     A WebSocket is an ephemeral attachment. Closing it does not stop the session or close process input.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        after=after,
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
) -> Optional[Union[Any, ErrorEnvelope]]:
    """Attach to an execution session with WebSocket

     A WebSocket is an ephemeral attachment. Closing it does not stop the session or close process input.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope]
    """

    return sync_detailed(
        id=id,
        session_id=session_id,
        client=client,
        after=after,
    ).parsed


async def asyncio_detailed(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
) -> Response[Union[Any, ErrorEnvelope]]:
    """Attach to an execution session with WebSocket

     A WebSocket is an ephemeral attachment. Closing it does not stop the session or close process input.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, ErrorEnvelope]]:
    """Attach to an execution session with WebSocket

     A WebSocket is an ephemeral attachment. Closing it does not stop the session or close process input.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope]
    """

    return (
        await asyncio_detailed(
            id=id,
            session_id=session_id,
            client=client,
            after=after,
        )
    ).parsed
