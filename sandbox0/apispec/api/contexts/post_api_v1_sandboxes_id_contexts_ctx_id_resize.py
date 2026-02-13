from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resize_context_request import ResizeContextRequest
from ...models.success_resized_response import SuccessResizedResponse
from ...types import Response


def _get_kwargs(
    id: str,
    ctx_id: str,
    *,
    body: ResizeContextRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/contexts/{ctx_id}/resize".format(
            id=id,
            ctx_id=ctx_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessResizedResponse]:
    if response.status_code == 200:
        response_200 = SuccessResizedResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessResizedResponse]:
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
    body: ResizeContextRequest,
) -> Response[SuccessResizedResponse]:
    """Resize context PTY

    Args:
        id (str):
        ctx_id (str):
        body (ResizeContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessResizedResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        ctx_id=ctx_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    ctx_id: str,
    *,
    client: AuthenticatedClient,
    body: ResizeContextRequest,
) -> Optional[SuccessResizedResponse]:
    """Resize context PTY

    Args:
        id (str):
        ctx_id (str):
        body (ResizeContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessResizedResponse
    """

    return sync_detailed(
        id=id,
        ctx_id=ctx_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    ctx_id: str,
    *,
    client: AuthenticatedClient,
    body: ResizeContextRequest,
) -> Response[SuccessResizedResponse]:
    """Resize context PTY

    Args:
        id (str):
        ctx_id (str):
        body (ResizeContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessResizedResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        ctx_id=ctx_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    ctx_id: str,
    *,
    client: AuthenticatedClient,
    body: ResizeContextRequest,
) -> Optional[SuccessResizedResponse]:
    """Resize context PTY

    Args:
        id (str):
        ctx_id (str):
        body (ResizeContextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessResizedResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            ctx_id=ctx_id,
            client=client,
            body=body,
        )
    ).parsed
