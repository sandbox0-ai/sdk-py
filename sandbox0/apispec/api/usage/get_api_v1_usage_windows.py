from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_usage_windows_response import SuccessUsageWindowsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    window_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["window_type"] = window_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/usage/windows",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]:
    if response.status_code == 200:
        response_200 = SuccessUsageWindowsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    window_type: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]:
    """List usage windows for the current team

     Returns immutable, closed usage windows belonging to the authenticated
    team. The opaque cursor can be retained and reused to incrementally
    import newly recorded windows.

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        window_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        window_type=window_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    window_type: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]:
    """List usage windows for the current team

     Returns immutable, closed usage windows belonging to the authenticated
    team. The opaque cursor can be retained and reused to incrementally
    import newly recorded windows.

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        window_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessUsageWindowsResponse]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        window_type=window_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    window_type: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]:
    """List usage windows for the current team

     Returns immutable, closed usage windows belonging to the authenticated
    team. The opaque cursor can be retained and reused to incrementally
    import newly recorded windows.

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        window_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        window_type=window_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    window_type: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessUsageWindowsResponse]]:
    """List usage windows for the current team

     Returns immutable, closed usage windows belonging to the authenticated
    team. The opaque cursor can be retained and reused to incrementally
    import newly recorded windows.

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        window_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessUsageWindowsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            window_type=window_type,
        )
    ).parsed
