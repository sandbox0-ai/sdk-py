from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_team_quota_policy_response import SuccessTeamQuotaPolicyResponse
from ...models.team_quota_capacity_policy_write_request import (
    TeamQuotaCapacityPolicyWriteRequest,
)
from ...models.team_quota_concurrency_policy_write_request import (
    TeamQuotaConcurrencyPolicyWriteRequest,
)
from ...models.team_quota_key import TeamQuotaKey
from ...models.team_quota_rate_policy_write_request import (
    TeamQuotaRatePolicyWriteRequest,
)
from ...types import Response


def _get_kwargs(
    team_id: str,
    key: TeamQuotaKey,
    *,
    body: Union[
        "TeamQuotaCapacityPolicyWriteRequest",
        "TeamQuotaConcurrencyPolicyWriteRequest",
        "TeamQuotaRatePolicyWriteRequest",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/teams/{team_id}/quotas/{key}".format(
            team_id=team_id,
            key=key,
        ),
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, TeamQuotaCapacityPolicyWriteRequest):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, TeamQuotaConcurrencyPolicyWriteRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]:
    if response.status_code == 200:
        response_200 = SuccessTeamQuotaPolicyResponse.from_dict(response.json())

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
) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]:
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
    body: Union[
        "TeamQuotaCapacityPolicyWriteRequest",
        "TeamQuotaConcurrencyPolicyWriteRequest",
        "TeamQuotaRatePolicyWriteRequest",
    ],
) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]:
    """Set a team quota policy

     System admin access is required. Replaces the explicit override for one quota key. The request kind
    must match the canonical kind of the path key.

    Args:
        team_id (str):
        key (TeamQuotaKey):
        body (Union['TeamQuotaCapacityPolicyWriteRequest',
            'TeamQuotaConcurrencyPolicyWriteRequest', 'TeamQuotaRatePolicyWriteRequest']): Capacity
            and concurrency policies require limit and prohibit rate fields. Rate policies require
            tokens, interval_ms, and burst and prohibit limit. Rate intervals are whole milliseconds
            in the inclusive range from 1ms to 1h. The runtime additionally requires burst to be at
            least tokens and kind to match the canonical kind of the path key because OpenAPI 3.0
            cannot express those cross-field and path/body comparisons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        key=key,
        body=body,
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
    body: Union[
        "TeamQuotaCapacityPolicyWriteRequest",
        "TeamQuotaConcurrencyPolicyWriteRequest",
        "TeamQuotaRatePolicyWriteRequest",
    ],
) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]:
    """Set a team quota policy

     System admin access is required. Replaces the explicit override for one quota key. The request kind
    must match the canonical kind of the path key.

    Args:
        team_id (str):
        key (TeamQuotaKey):
        body (Union['TeamQuotaCapacityPolicyWriteRequest',
            'TeamQuotaConcurrencyPolicyWriteRequest', 'TeamQuotaRatePolicyWriteRequest']): Capacity
            and concurrency policies require limit and prohibit rate fields. Rate policies require
            tokens, interval_ms, and burst and prohibit limit. Rate intervals are whole milliseconds
            in the inclusive range from 1ms to 1h. The runtime additionally requires burst to be at
            least tokens and kind to match the canonical kind of the path key because OpenAPI 3.0
            cannot express those cross-field and path/body comparisons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]
    """

    return sync_detailed(
        team_id=team_id,
        key=key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    key: TeamQuotaKey,
    *,
    client: AuthenticatedClient,
    body: Union[
        "TeamQuotaCapacityPolicyWriteRequest",
        "TeamQuotaConcurrencyPolicyWriteRequest",
        "TeamQuotaRatePolicyWriteRequest",
    ],
) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]:
    """Set a team quota policy

     System admin access is required. Replaces the explicit override for one quota key. The request kind
    must match the canonical kind of the path key.

    Args:
        team_id (str):
        key (TeamQuotaKey):
        body (Union['TeamQuotaCapacityPolicyWriteRequest',
            'TeamQuotaConcurrencyPolicyWriteRequest', 'TeamQuotaRatePolicyWriteRequest']): Capacity
            and concurrency policies require limit and prohibit rate fields. Rate policies require
            tokens, interval_ms, and burst and prohibit limit. Rate intervals are whole milliseconds
            in the inclusive range from 1ms to 1h. The runtime additionally requires burst to be at
            least tokens and kind to match the canonical kind of the path key because OpenAPI 3.0
            cannot express those cross-field and path/body comparisons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        key=key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    key: TeamQuotaKey,
    *,
    client: AuthenticatedClient,
    body: Union[
        "TeamQuotaCapacityPolicyWriteRequest",
        "TeamQuotaConcurrencyPolicyWriteRequest",
        "TeamQuotaRatePolicyWriteRequest",
    ],
) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]]:
    """Set a team quota policy

     System admin access is required. Replaces the explicit override for one quota key. The request kind
    must match the canonical kind of the path key.

    Args:
        team_id (str):
        key (TeamQuotaKey):
        body (Union['TeamQuotaCapacityPolicyWriteRequest',
            'TeamQuotaConcurrencyPolicyWriteRequest', 'TeamQuotaRatePolicyWriteRequest']): Capacity
            and concurrency policies require limit and prohibit rate fields. Rate policies require
            tokens, interval_ms, and burst and prohibit limit. Rate intervals are whole milliseconds
            in the inclusive range from 1ms to 1h. The runtime additionally requires burst to be at
            least tokens and kind to match the canonical kind of the path key because OpenAPI 3.0
            cannot express those cross-field and path/body comparisons.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTeamQuotaPolicyResponse]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            key=key,
            client=client,
            body=body,
        )
    ).parsed
