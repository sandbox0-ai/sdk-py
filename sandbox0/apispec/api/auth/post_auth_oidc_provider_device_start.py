from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_device_login_start_response import (
    SuccessDeviceLoginStartResponse,
)
from ...types import Response


def _get_kwargs(
    provider: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/oidc/{provider}/device/start".format(
            provider=provider,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]:
    if response.status_code == 200:
        response_200 = SuccessDeviceLoginStartResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]:
    """Start OIDC device login

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]
    """

    kwargs = _get_kwargs(
        provider=provider,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]:
    """Start OIDC device login

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]
    """

    return sync_detailed(
        provider=provider,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]:
    """Start OIDC device login

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]
    """

    kwargs = _get_kwargs(
        provider=provider,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]]:
    """Start OIDC device login

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessDeviceLoginStartResponse]
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
        )
    ).parsed
