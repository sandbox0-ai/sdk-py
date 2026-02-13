from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_sandbox_network_policy_response import (
    SuccessSandboxNetworkPolicyResponse,
)
from ...models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: TplSandboxNetworkPolicy,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/sandboxes/{id}/network".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessSandboxNetworkPolicyResponse]:
    if response.status_code == 200:
        response_200 = SuccessSandboxNetworkPolicyResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessSandboxNetworkPolicyResponse]:
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
    body: TplSandboxNetworkPolicy,
) -> Response[SuccessSandboxNetworkPolicyResponse]:
    """Update sandbox network policy

    Args:
        id (str):
        body (TplSandboxNetworkPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessSandboxNetworkPolicyResponse]
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
    body: TplSandboxNetworkPolicy,
) -> Optional[SuccessSandboxNetworkPolicyResponse]:
    """Update sandbox network policy

    Args:
        id (str):
        body (TplSandboxNetworkPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessSandboxNetworkPolicyResponse
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
    body: TplSandboxNetworkPolicy,
) -> Response[SuccessSandboxNetworkPolicyResponse]:
    """Update sandbox network policy

    Args:
        id (str):
        body (TplSandboxNetworkPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessSandboxNetworkPolicyResponse]
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
    body: TplSandboxNetworkPolicy,
) -> Optional[SuccessSandboxNetworkPolicyResponse]:
    """Update sandbox network policy

    Args:
        id (str):
        body (TplSandboxNetworkPolicy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessSandboxNetworkPolicyResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
