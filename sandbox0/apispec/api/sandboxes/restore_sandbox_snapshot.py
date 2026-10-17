from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.sandbox_snapshot_restore_request import SandboxSnapshotRestoreRequest
from ...models.success_sandbox_snapshot_restore_operation_response import (
    SuccessSandboxSnapshotRestoreOperationResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SandboxSnapshotRestoreRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/snapshot-restore".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxSnapshotRestoreOperationResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 202:
        response_202 = SuccessSandboxSnapshotRestoreOperationResponse.from_dict(
            response.json()
        )

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

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]:
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
    body: SandboxSnapshotRestoreRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]:
    """Restore a selected snapshot and start a fresh runtime

     Explicitly discards source process state and replaces its writable RootFS
    with the exact selected snapshot generation. Requires sandbox:write,
    discard_process_state=true and a stable Idempotency-Key bound to the source
    runtime generation and snapshot identity. Admission pins the selected data,
    including across later snapshot expiry or deletion. External final capture
    retains projected credential custody before source retirement. Head replacement
    and cold resume admission commit together. A duplicate returns the original
    operation and cannot restore again. Request timeout does not cancel accepted
    work; recover its acknowledgement by request_key. Completion proves external
    runtime launch, not guest application health. Never use as a memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxSnapshotRestoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]
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
    body: SandboxSnapshotRestoreRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]:
    """Restore a selected snapshot and start a fresh runtime

     Explicitly discards source process state and replaces its writable RootFS
    with the exact selected snapshot generation. Requires sandbox:write,
    discard_process_state=true and a stable Idempotency-Key bound to the source
    runtime generation and snapshot identity. Admission pins the selected data,
    including across later snapshot expiry or deletion. External final capture
    retains projected credential custody before source retirement. Head replacement
    and cold resume admission commit together. A duplicate returns the original
    operation and cannot restore again. Request timeout does not cancel accepted
    work; recover its acknowledgement by request_key. Completion proves external
    runtime launch, not guest application health. Never use as a memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxSnapshotRestoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]
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
    body: SandboxSnapshotRestoreRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]:
    """Restore a selected snapshot and start a fresh runtime

     Explicitly discards source process state and replaces its writable RootFS
    with the exact selected snapshot generation. Requires sandbox:write,
    discard_process_state=true and a stable Idempotency-Key bound to the source
    runtime generation and snapshot identity. Admission pins the selected data,
    including across later snapshot expiry or deletion. External final capture
    retains projected credential custody before source retirement. Head replacement
    and cold resume admission commit together. A duplicate returns the original
    operation and cannot restore again. Request timeout does not cancel accepted
    work; recover its acknowledgement by request_key. Completion proves external
    runtime launch, not guest application health. Never use as a memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxSnapshotRestoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]
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
    body: SandboxSnapshotRestoreRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]]:
    """Restore a selected snapshot and start a fresh runtime

     Explicitly discards source process state and replaces its writable RootFS
    with the exact selected snapshot generation. Requires sandbox:write,
    discard_process_state=true and a stable Idempotency-Key bound to the source
    runtime generation and snapshot identity. Admission pins the selected data,
    including across later snapshot expiry or deletion. External final capture
    retains projected credential custody before source retirement. Head replacement
    and cold resume admission commit together. A duplicate returns the original
    operation and cannot restore again. Request timeout does not cancel accepted
    work; recover its acknowledgement by request_key. Completion proves external
    runtime launch, not guest application health. Never use as a memory fallback.

    Args:
        id (str):
        idempotency_key (str):
        body (SandboxSnapshotRestoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxSnapshotRestoreOperationResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
