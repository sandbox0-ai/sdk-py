from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.capture_sandbox_root_fs_snapshot_request import (
    CaptureSandboxRootFSSnapshotRequest,
)
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_root_fs_snapshot_response import (
    SuccessSandboxRootFSSnapshotResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CaptureSandboxRootFSSnapshotRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/snapshots/capture".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    if response.status_code == 201:
        response_201 = SuccessSandboxRootFSSnapshotResponse.from_dict(response.json())

        return response_201

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
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
    body: CaptureSandboxRootFSSnapshotRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Capture a generation-conditioned running RootFS snapshot

     Captures one immutable RootFS snapshot from the expected running runtime
    generation without stopping its processes. Admission checks the generation
    while locking the external source and exact writer. Reuse the same key,
    generation and metadata after uncertainty: an accepted capture retains its
    original transaction and returns its original snapshot when completed,
    even if the source subsequently changes generation or pauses. A new capture
    of a paused or mismatched source is rejected. No guest execution, automatic
    resume, process restart or memory checkpoint fallback is performed.
    This distinct endpoint fails closed on servers without conditional capture.

    Args:
        id (str):
        idempotency_key (str):
        body (CaptureSandboxRootFSSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]
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
    body: CaptureSandboxRootFSSnapshotRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Capture a generation-conditioned running RootFS snapshot

     Captures one immutable RootFS snapshot from the expected running runtime
    generation without stopping its processes. Admission checks the generation
    while locking the external source and exact writer. Reuse the same key,
    generation and metadata after uncertainty: an accepted capture retains its
    original transaction and returns its original snapshot when completed,
    even if the source subsequently changes generation or pauses. A new capture
    of a paused or mismatched source is rejected. No guest execution, automatic
    resume, process restart or memory checkpoint fallback is performed.
    This distinct endpoint fails closed on servers without conditional capture.

    Args:
        id (str):
        idempotency_key (str):
        body (CaptureSandboxRootFSSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]
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
    body: CaptureSandboxRootFSSnapshotRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Capture a generation-conditioned running RootFS snapshot

     Captures one immutable RootFS snapshot from the expected running runtime
    generation without stopping its processes. Admission checks the generation
    while locking the external source and exact writer. Reuse the same key,
    generation and metadata after uncertainty: an accepted capture retains its
    original transaction and returns its original snapshot when completed,
    even if the source subsequently changes generation or pauses. A new capture
    of a paused or mismatched source is rejected. No guest execution, automatic
    resume, process restart or memory checkpoint fallback is performed.
    This distinct endpoint fails closed on servers without conditional capture.

    Args:
        id (str):
        idempotency_key (str):
        body (CaptureSandboxRootFSSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]
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
    body: CaptureSandboxRootFSSnapshotRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Capture a generation-conditioned running RootFS snapshot

     Captures one immutable RootFS snapshot from the expected running runtime
    generation without stopping its processes. Admission checks the generation
    while locking the external source and exact writer. Reuse the same key,
    generation and metadata after uncertainty: an accepted capture retains its
    original transaction and returns its original snapshot when completed,
    even if the source subsequently changes generation or pauses. A new capture
    of a paused or mismatched source is rejected. No guest execution, automatic
    resume, process restart or memory checkpoint fallback is performed.
    This distinct endpoint fails closed on servers without conditional capture.

    Args:
        id (str):
        idempotency_key (str):
        body (CaptureSandboxRootFSSnapshotRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
