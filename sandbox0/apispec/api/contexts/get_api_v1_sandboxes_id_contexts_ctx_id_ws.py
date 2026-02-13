from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: str,
    ctx_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/contexts/{ctx_id}/ws".format(
            id=id,
            ctx_id=ctx_id,
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
    ctx_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Context WebSocket (I/O)

     Upgrades to WebSocket for streaming I/O.
    Client messages (JSON):
    - { \"type\": \"input\", \"data\": \"ls\n\", \"request_id\": \"req-1\" }
    - { \"type\": \"resize\", \"rows\": 24, \"cols\": 80 }
    - { \"type\": \"signal\", \"signal\": \"INT\" }
    Server messages (JSON):
    - { \"type\": \"output\", \"source\": \"stdout\", \"data\": \"hello\n\" }

    Args:
        id (str):
        ctx_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        ctx_id=ctx_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    ctx_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Context WebSocket (I/O)

     Upgrades to WebSocket for streaming I/O.
    Client messages (JSON):
    - { \"type\": \"input\", \"data\": \"ls\n\", \"request_id\": \"req-1\" }
    - { \"type\": \"resize\", \"rows\": 24, \"cols\": 80 }
    - { \"type\": \"signal\", \"signal\": \"INT\" }
    Server messages (JSON):
    - { \"type\": \"output\", \"source\": \"stdout\", \"data\": \"hello\n\" }

    Args:
        id (str):
        ctx_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        ctx_id=ctx_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
