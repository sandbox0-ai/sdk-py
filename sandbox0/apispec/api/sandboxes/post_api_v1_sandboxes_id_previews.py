from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.sandbox_preview_create_request import SandboxPreviewCreateRequest
from ...models.success_sandbox_preview_response import SuccessSandboxPreviewResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SandboxPreviewCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/previews".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]:
    if response.status_code == 201:
        response_201 = SuccessSandboxPreviewResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]:
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
    body: SandboxPreviewCreateRequest,
) -> Response[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]:
    """Create a private sandbox preview grant

     Creates a short-lived, sandbox-runtime-bound authorization for previewing a loopback HTTP
    server through the region public exposure domain. The returned URL performs a one-time
    browser bootstrap and then redirects to a clean same-origin URL. This does not publish or
    modify sandbox services.

    Args:
        id (str):
        body (SandboxPreviewCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]
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
    body: SandboxPreviewCreateRequest,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]:
    """Create a private sandbox preview grant

     Creates a short-lived, sandbox-runtime-bound authorization for previewing a loopback HTTP
    server through the region public exposure domain. The returned URL performs a one-time
    browser bootstrap and then redirects to a clean same-origin URL. This does not publish or
    modify sandbox services.

    Args:
        id (str):
        body (SandboxPreviewCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxPreviewResponse]
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
    body: SandboxPreviewCreateRequest,
) -> Response[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]:
    """Create a private sandbox preview grant

     Creates a short-lived, sandbox-runtime-bound authorization for previewing a loopback HTTP
    server through the region public exposure domain. The returned URL performs a one-time
    browser bootstrap and then redirects to a clean same-origin URL. This does not publish or
    modify sandbox services.

    Args:
        id (str):
        body (SandboxPreviewCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]
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
    body: SandboxPreviewCreateRequest,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxPreviewResponse]]:
    """Create a private sandbox preview grant

     Creates a short-lived, sandbox-runtime-bound authorization for previewing a loopback HTTP
    server through the region public exposure domain. The returned URL performs a one-time
    browser bootstrap and then redirects to a clean same-origin URL. This does not publish or
    modify sandbox services.

    Args:
        id (str):
        body (SandboxPreviewCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxPreviewResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
