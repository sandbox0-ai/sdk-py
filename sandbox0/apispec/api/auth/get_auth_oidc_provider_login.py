from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider: str,
    *,
    return_url: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["return_url"] = return_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth/oidc/{provider}/login".format(
            provider=provider,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorEnvelope]]:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

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
) -> Response[Union[Any, ErrorEnvelope]]:
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
    return_url: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorEnvelope]]:
    """Initiate OIDC login

    Args:
        provider (str):
        return_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        provider=provider,
        return_url=return_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    return_url: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorEnvelope]]:
    """Initiate OIDC login

    Args:
        provider (str):
        return_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope]
    """

    return sync_detailed(
        provider=provider,
        client=client,
        return_url=return_url,
    ).parsed


async def asyncio_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    return_url: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorEnvelope]]:
    """Initiate OIDC login

    Args:
        provider (str):
        return_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        provider=provider,
        return_url=return_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    return_url: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorEnvelope]]:
    """Initiate OIDC login

    Args:
        provider (str):
        return_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope]
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
            return_url=return_url,
        )
    ).parsed
