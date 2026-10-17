from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.sandbox_pause_request import SandboxPauseRequest
from ...models.success_pause_sandbox_response import SuccessPauseSandboxResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: SandboxPauseRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/pause".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]:
    if response.status_code == 200:
        response_200 = SuccessPauseSandboxResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = SuccessPauseSandboxResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ErrorEnvelope.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]:
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
    body: SandboxPauseRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]:
    """Pause a sandbox

     The default checkpoints only the writable RootFS. Set memory=true to also retain process execution
    state before releasing the runtime. A 202 response means checkpoint publication and cleanup are
    still pending. For conditional memory pause, send expected_runtime_generation and Idempotency-Key
    together with memory=true. Retries bind the same source generation and checkpoint operation;
    mismatched or aborted operations conflict.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxPauseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SandboxPauseRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]:
    """Pause a sandbox

     The default checkpoints only the writable RootFS. Set memory=true to also retain process execution
    state before releasing the runtime. A 202 response means checkpoint publication and cleanup are
    still pending. For conditional memory pause, send expected_runtime_generation and Idempotency-Key
    together with memory=true. Retries bind the same source generation and checkpoint operation;
    mismatched or aborted operations conflict.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxPauseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessPauseSandboxResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SandboxPauseRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]:
    """Pause a sandbox

     The default checkpoints only the writable RootFS. Set memory=true to also retain process execution
    state before releasing the runtime. A 202 response means checkpoint publication and cleanup are
    still pending. For conditional memory pause, send expected_runtime_generation and Idempotency-Key
    together with memory=true. Retries bind the same source generation and checkpoint operation;
    mismatched or aborted operations conflict.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxPauseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: SandboxPauseRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessPauseSandboxResponse]]:
    """Pause a sandbox

     The default checkpoints only the writable RootFS. Set memory=true to also retain process execution
    state before releasing the runtime. A 202 response means checkpoint publication and cleanup are
    still pending. For conditional memory pause, send expected_runtime_generation and Idempotency-Key
    together with memory=true. Retries bind the same source generation and checkpoint operation;
    mismatched or aborted operations conflict.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxPauseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessPauseSandboxResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
