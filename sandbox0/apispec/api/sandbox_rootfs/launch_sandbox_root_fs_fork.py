from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.sandbox_root_fs_fork_launch_request import SandboxRootFSForkLaunchRequest
from ...models.success_sandbox_root_fs_fork_launch_response import (
    SuccessSandboxRootFSForkLaunchResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SandboxRootFSForkLaunchRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/fork-launch".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRootFSForkLaunchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = SuccessSandboxRootFSForkLaunchResponse.from_dict(response.json())

        return response_202

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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]:
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
    body: SandboxRootFSForkLaunchRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]:
    """Launch the original never-run RootFS fork

     Binds the original authenticated caller and Idempotency-Key to a first
    cold launch of the child at generation zero. Supply the original fork
    operation and the child's observed filesystem, head and writer epoch.
    The child must retain its original birth configuration, or its one
    externally committed credential-free network isolation preparation;
    all other fields and automatic-wake disablement must remain unchanged.
    Memory forks and ordinary resumes are excluded. Retries must
    keep the same key and conditions; never refresh them after uncertainty.
    Requires sandbox:write. Admission is durable before node dispatch;
    manager recovery continues the exact lifecycle after a timeout or lost
    reply. No guest command or terminal is required. A 503 does not prove
    that admission failed; use GET with the original key and conditions.
    Completed history survives later lifecycles. Current only compares
    the owner/lifecycle snapshot, not runtime health or a lease. Aborted
    does not prove physical absence. This is not credential admission.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRootFSForkLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]
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
    body: SandboxRootFSForkLaunchRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]:
    """Launch the original never-run RootFS fork

     Binds the original authenticated caller and Idempotency-Key to a first
    cold launch of the child at generation zero. Supply the original fork
    operation and the child's observed filesystem, head and writer epoch.
    The child must retain its original birth configuration, or its one
    externally committed credential-free network isolation preparation;
    all other fields and automatic-wake disablement must remain unchanged.
    Memory forks and ordinary resumes are excluded. Retries must
    keep the same key and conditions; never refresh them after uncertainty.
    Requires sandbox:write. Admission is durable before node dispatch;
    manager recovery continues the exact lifecycle after a timeout or lost
    reply. No guest command or terminal is required. A 503 does not prove
    that admission failed; use GET with the original key and conditions.
    Completed history survives later lifecycles. Current only compares
    the owner/lifecycle snapshot, not runtime health or a lease. Aborted
    does not prove physical absence. This is not credential admission.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRootFSForkLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]
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
    body: SandboxRootFSForkLaunchRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]:
    """Launch the original never-run RootFS fork

     Binds the original authenticated caller and Idempotency-Key to a first
    cold launch of the child at generation zero. Supply the original fork
    operation and the child's observed filesystem, head and writer epoch.
    The child must retain its original birth configuration, or its one
    externally committed credential-free network isolation preparation;
    all other fields and automatic-wake disablement must remain unchanged.
    Memory forks and ordinary resumes are excluded. Retries must
    keep the same key and conditions; never refresh them after uncertainty.
    Requires sandbox:write. Admission is durable before node dispatch;
    manager recovery continues the exact lifecycle after a timeout or lost
    reply. No guest command or terminal is required. A 503 does not prove
    that admission failed; use GET with the original key and conditions.
    Completed history survives later lifecycles. Current only compares
    the owner/lifecycle snapshot, not runtime health or a lease. Aborted
    does not prove physical absence. This is not credential admission.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRootFSForkLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]
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
    body: SandboxRootFSForkLaunchRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]]:
    """Launch the original never-run RootFS fork

     Binds the original authenticated caller and Idempotency-Key to a first
    cold launch of the child at generation zero. Supply the original fork
    operation and the child's observed filesystem, head and writer epoch.
    The child must retain its original birth configuration, or its one
    externally committed credential-free network isolation preparation;
    all other fields and automatic-wake disablement must remain unchanged.
    Memory forks and ordinary resumes are excluded. Retries must
    keep the same key and conditions; never refresh them after uncertainty.
    Requires sandbox:write. Admission is durable before node dispatch;
    manager recovery continues the exact lifecycle after a timeout or lost
    reply. No guest command or terminal is required. A 503 does not prove
    that admission failed; use GET with the original key and conditions.
    Completed history survives later lifecycles. Current only compares
    the owner/lifecycle snapshot, not runtime health or a lease. Aborted
    does not prove physical absence. This is not credential admission.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxRootFSForkLaunchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSForkLaunchResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
