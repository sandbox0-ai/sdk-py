from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_restart_operation_response import (
    SuccessSandboxRestartOperationResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    request_key: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["request_key"] = request_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/restart-operations".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRestartOperationResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
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
    request_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Find a restart by its original request key

     Read-only acknowledgement recovery. Requires sandbox:read. Does not execute in the guest or submit a
    new restart.

    Args:
        id (str):
        request_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        request_key=request_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    request_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Find a restart by its original request key

     Read-only acknowledgement recovery. Requires sandbox:read. Does not execute in the guest or submit a
    new restart.

    Args:
        id (str):
        request_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        request_key=request_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    request_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Find a restart by its original request key

     Read-only acknowledgement recovery. Requires sandbox:read. Does not execute in the guest or submit a
    new restart.

    Args:
        id (str):
        request_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        request_key=request_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    request_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Find a restart by its original request key

     Read-only acknowledgement recovery. Requires sandbox:read. Does not execute in the guest or submit a
    new restart.

    Args:
        id (str):
        request_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            request_key=request_key,
        )
    ).parsed
