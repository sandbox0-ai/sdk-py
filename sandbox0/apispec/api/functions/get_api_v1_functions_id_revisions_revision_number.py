from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_function_revision_response import SuccessFunctionRevisionResponse
from ...types import Response


def _get_kwargs(
    id: str,
    revision_number: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/functions/{id}/revisions/{revision_number}".format(
            id=id,
            revision_number=revision_number,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]:
    if response.status_code == 200:
        response_200 = SuccessFunctionRevisionResponse.from_dict(response.json())

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
) -> Response[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]:
    """Get function revision

    Args:
        id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        revision_number=revision_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]:
    """Get function revision

    Args:
        id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessFunctionRevisionResponse]
    """

    return sync_detailed(
        id=id,
        revision_number=revision_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]:
    """Get function revision

    Args:
        id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        revision_number=revision_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    revision_number: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessFunctionRevisionResponse]]:
    """Get function revision

    Args:
        id (str):
        revision_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessFunctionRevisionResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            revision_number=revision_number,
            client=client,
        )
    ).parsed
