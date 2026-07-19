from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_message_response import SuccessMessageResponse
from ...models.team_quota_key import TeamQuotaKey
from ...types import Response


def _get_kwargs(
    team_id: str,
    key: TeamQuotaKey,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/teams/{team_id}/quotas/{key}".format(
            team_id=team_id,
            key=key,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessMessageResponse]]:
    if response.status_code == 200:
        response_200 = SuccessMessageResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

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
) -> Response[Union[ErrorEnvelope, SuccessMessageResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    key: TeamQuotaKey,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Delete a team quota policy

     System admin access is required. The effective policy falls back to the region default after the
    override is deleted.

    Args:
        team_id (str):
        key (TeamQuotaKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessMessageResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    key: TeamQuotaKey,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Delete a team quota policy

     System admin access is required. The effective policy falls back to the region default after the
    override is deleted.

    Args:
        team_id (str):
        key (TeamQuotaKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessMessageResponse]
    """

    return sync_detailed(
        team_id=team_id,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    key: TeamQuotaKey,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Delete a team quota policy

     System admin access is required. The effective policy falls back to the region default after the
    override is deleted.

    Args:
        team_id (str):
        key (TeamQuotaKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessMessageResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    key: TeamQuotaKey,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Delete a team quota policy

     System admin access is required. The effective policy falls back to the region default after the
    override is deleted.

    Args:
        team_id (str):
        key (TeamQuotaKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessMessageResponse]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            key=key,
            client=client,
        )
    ).parsed
