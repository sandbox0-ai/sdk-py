from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_restart_final_capture_response import (
    SuccessSandboxRestartFinalCaptureResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    operation_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/restart-operations/{operation_id}/final-capture".format(
            id=id,
            operation_id=operation_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRestartFinalCaptureResponse.from_dict(
            response.json()
        )

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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]:
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]:
    """Get retained cold-restart credential custody

     Requires sandbox:read. Reads durable metadata independently of procd. Pending has no capture ID.
    Stopped identifies one immutable externally stopped source. Acknowledged means the owner receipt is
    durable; released permits ordinary retirement. This is not a completed restart or a credential-
    content digest.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]
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
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]:
    """Get retained cold-restart credential custody

     Requires sandbox:read. Reads durable metadata independently of procd. Pending has no capture ID.
    Stopped identifies one immutable externally stopped source. Acknowledged means the owner receipt is
    durable; released permits ordinary retirement. This is not a completed restart or a credential-
    content digest.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]:
    """Get retained cold-restart credential custody

     Requires sandbox:read. Reads durable metadata independently of procd. Pending has no capture ID.
    Stopped identifies one immutable externally stopped source. Acknowledged means the owner receipt is
    durable; released permits ordinary retirement. This is not a completed restart or a credential-
    content digest.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]
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
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]]:
    """Get retained cold-restart credential custody

     Requires sandbox:read. Reads durable metadata independently of procd. Pending has no capture ID.
    Stopped identifies one immutable externally stopped source. Acknowledged means the owner receipt is
    durable; released permits ordinary retirement. This is not a completed restart or a credential-
    content digest.

    Args:
        id (str):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            operation_id=operation_id,
            client=client,
        )
    ).parsed
