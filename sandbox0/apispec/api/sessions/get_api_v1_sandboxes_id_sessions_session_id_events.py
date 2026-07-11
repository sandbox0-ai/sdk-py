from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_execution_session_event_page_response import (
    SuccessExecutionSessionEventPageResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    session_id: str,
    *,
    after: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["after"] = after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/sessions/{session_id}/events".format(
            id=id,
            session_id=session_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]:
    if response.status_code == 200:
        response_200 = SuccessExecutionSessionEventPageResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 410:
        response_410 = ErrorEnvelope.from_dict(response.json())

        return response_410

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]:
    """List execution session events

     Returns retained events after the supplied sequence. Delivery is cursor-based and at least once.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        after=after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]:
    """List execution session events

     Returns retained events after the supplied sequence. Delivery is cursor-based and at least once.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]
    """

    return sync_detailed(
        id=id,
        session_id=session_id,
        client=client,
        after=after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]:
    """List execution session events

     Returns retained events after the supplied sequence. Delivery is cursor-based and at least once.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        after=after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]]:
    """List execution session events

     Returns retained events after the supplied sequence. Delivery is cursor-based and at least once.

    Args:
        id (str):
        session_id (str):
        after (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionEventPageResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            session_id=session_id,
            client=client,
            after=after,
            limit=limit,
        )
    ).parsed
