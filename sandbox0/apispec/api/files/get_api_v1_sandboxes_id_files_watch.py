from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/files/watch".format(
            id=id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == 101:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
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
) -> Response[Any]:
    r"""File watch WebSocket

     Upgrades to WebSocket for file watch events.
    Client messages:
    - { \"action\": \"subscribe\", \"path\": \"/tmp\", \"recursive\": false }
    - { \"action\": \"unsubscribe\", \"watch_id\": \"watch-id\" }
    Server messages:
    - { \"type\": \"subscribed\", \"watch_id\": \"watch-id\", \"path\": \"/tmp\" }
    - { \"type\": \"event\", \"watch_id\": \"watch-id\", \"event\": \"write\", \"path\": \"/tmp/a.txt\"
    }
    - { \"type\": \"unsubscribed\", \"watch_id\": \"watch-id\" }
    - { \"type\": \"error\", \"error\": \"message\" }

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""File watch WebSocket

     Upgrades to WebSocket for file watch events.
    Client messages:
    - { \"action\": \"subscribe\", \"path\": \"/tmp\", \"recursive\": false }
    - { \"action\": \"unsubscribe\", \"watch_id\": \"watch-id\" }
    Server messages:
    - { \"type\": \"subscribed\", \"watch_id\": \"watch-id\", \"path\": \"/tmp\" }
    - { \"type\": \"event\", \"watch_id\": \"watch-id\", \"event\": \"write\", \"path\": \"/tmp/a.txt\"
    }
    - { \"type\": \"unsubscribed\", \"watch_id\": \"watch-id\" }
    - { \"type\": \"error\", \"error\": \"message\" }

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
