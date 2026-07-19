from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxvolumes/{id}/files/watch".format(
            id=id,
        ),
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
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorEnvelope]]:
    r"""Volume file watch WebSocket

     Upgrades to WebSocket for volume file watch events.
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
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorEnvelope]]:
    r"""Volume file watch WebSocket

     Upgrades to WebSocket for volume file watch events.
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
        Union[Any, ErrorEnvelope]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorEnvelope]]:
    r"""Volume file watch WebSocket

     Upgrades to WebSocket for volume file watch events.
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
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorEnvelope]]:
    r"""Volume file watch WebSocket

     Upgrades to WebSocket for volume file watch events.
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
        Union[Any, ErrorEnvelope]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
