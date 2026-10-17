from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_restart_operation_response import (
    SuccessSandboxRestartOperationResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    operation_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/restart-operations/{operation_id}".format(
            id=id,
            operation_id=operation_id,
        ),
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
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Get durable restart state and bounded retry diagnostics

     Requires sandbox:read. Available independently of procd. A succeeded operation reports its
    historical replacement generation; later lifecycle activity does not cause another restart or make
    this an application-health report.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        operation_id=operation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Get durable restart state and bounded retry diagnostics

     Requires sandbox:read. Available independently of procd. A succeeded operation reports its
    historical replacement generation; later lifecycle activity does not cause another restart or make
    this an application-health report.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]
    """

    return sync_detailed(
        id=id,
        operation_id=operation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Get durable restart state and bounded retry diagnostics

     Requires sandbox:read. Available independently of procd. A succeeded operation reports its
    historical replacement generation; later lifecycle activity does not cause another restart or make
    this an application-health report.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        operation_id=operation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]]:
    """Get durable restart state and bounded retry diagnostics

     Requires sandbox:read. Available independently of procd. A succeeded operation reports its
    historical replacement generation; later lifecycle activity does not cause another restart or make
    this an application-health report.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartOperationResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            operation_id=operation_id,
            client=client,
        )
    ).parsed
