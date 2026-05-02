from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.public_gateway_config import PublicGatewayConfig
from ...models.success_public_gateway_response import SuccessPublicGatewayResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PublicGatewayConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/sandboxes/{id}/public-gateway".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]:
    if response.status_code == 200:
        response_200 = SuccessPublicGatewayResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]:
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
    body: PublicGatewayConfig,
) -> Response[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]:
    """Update sandbox public gateway policy

     Replaces the request-level public gateway policy for sandbox public traffic.
    When enabled, matching routes control method, path, authentication, CORS,
    per-route rate limits, timeout, rewrite, and paused sandbox auto-resume.

    Args:
        id (str):
        body (PublicGatewayConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]
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
    body: PublicGatewayConfig,
) -> Optional[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]:
    """Update sandbox public gateway policy

     Replaces the request-level public gateway policy for sandbox public traffic.
    When enabled, matching routes control method, path, authentication, CORS,
    per-route rate limits, timeout, rewrite, and paused sandbox auto-resume.

    Args:
        id (str):
        body (PublicGatewayConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessPublicGatewayResponse]
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
    body: PublicGatewayConfig,
) -> Response[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]:
    """Update sandbox public gateway policy

     Replaces the request-level public gateway policy for sandbox public traffic.
    When enabled, matching routes control method, path, authentication, CORS,
    per-route rate limits, timeout, rewrite, and paused sandbox auto-resume.

    Args:
        id (str):
        body (PublicGatewayConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]
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
    body: PublicGatewayConfig,
) -> Optional[Union[ErrorEnvelope, SuccessPublicGatewayResponse]]:
    """Update sandbox public gateway policy

     Replaces the request-level public gateway policy for sandbox public traffic.
    When enabled, matching routes control method, path, authentication, CORS,
    per-route rate limits, timeout, rewrite, and paused sandbox auto-resume.

    Args:
        id (str):
        body (PublicGatewayConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessPublicGatewayResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
