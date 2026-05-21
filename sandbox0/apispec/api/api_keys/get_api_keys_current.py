from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_current_api_key_response import SuccessCurrentAPIKeyResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api-keys/current",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]:
    if response.status_code == 200:
        response_200 = SuccessCurrentAPIKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]:
    """Introspect current API key

     Returns the identity and permissions of the currently authenticated API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]:
    """Introspect current API key

     Returns the identity and permissions of the currently authenticated API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]:
    """Introspect current API key

     Returns the identity and permissions of the currently authenticated API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]]:
    """Introspect current API key

     Returns the identity and permissions of the currently authenticated API key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessCurrentAPIKeyResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
