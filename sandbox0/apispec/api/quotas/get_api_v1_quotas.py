from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_team_quota_list_response import SuccessTeamQuotaListResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/quotas",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]:
    if response.status_code == 200:
        response_200 = SuccessTeamQuotaListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]:
    """List effective quotas for the current team

     Requires quota:read. Returns every effective policy. Capacity rows include PostgreSQL-backed usage,
    concurrency rows include current live lease usage, and rate rows return committed, reserved, and
    used as zero with remaining null because distributed Redis token balances are not exposed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]:
    """List effective quotas for the current team

     Requires quota:read. Returns every effective policy. Capacity rows include PostgreSQL-backed usage,
    concurrency rows include current live lease usage, and rate rows return committed, reserved, and
    used as zero with remaining null because distributed Redis token balances are not exposed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTeamQuotaListResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]:
    """List effective quotas for the current team

     Requires quota:read. Returns every effective policy. Capacity rows include PostgreSQL-backed usage,
    concurrency rows include current live lease usage, and rate rows return committed, reserved, and
    used as zero with remaining null because distributed Redis token balances are not exposed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaListResponse]]:
    """List effective quotas for the current team

     Requires quota:read. Returns every effective policy. Capacity rows include PostgreSQL-backed usage,
    concurrency rows include current live lease usage, and rate rows return committed, reserved, and
    used as zero with remaining null because distributed Redis token balances are not exposed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTeamQuotaListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
