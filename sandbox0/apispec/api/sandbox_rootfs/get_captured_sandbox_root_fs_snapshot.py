from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_root_fs_snapshot_response import (
    SuccessSandboxRootFSSnapshotResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    expected_runtime_generation: int,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    params["expected_runtime_generation"] = expected_runtime_generation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/snapshots/capture".format(
            id=id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRootFSSnapshotResponse.from_dict(response.json())

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
    expected_runtime_generation: int,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Read the original generation-conditioned snapshot receipt

     Reads only the capture identified by the authenticated caller, original
    Idempotency-Key and expected runtime generation. Does not admit, dispatch,
    retry, cancel or repair work. Completed receipts can be read after the
    source changes generation or pauses. A 404 is not proof of cancellation
    and must not clear an outstanding operation fence. A missing, expired or
    deleted retained snapshot is never replaced with a new capture.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        expected_runtime_generation=expected_runtime_generation,
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
    expected_runtime_generation: int,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Read the original generation-conditioned snapshot receipt

     Reads only the capture identified by the authenticated caller, original
    Idempotency-Key and expected runtime generation. Does not admit, dispatch,
    retry, cancel or repair work. Completed receipts can be read after the
    source changes generation or pauses. A 404 is not proof of cancellation
    and must not clear an outstanding operation fence. A missing, expired or
    deleted retained snapshot is never replaced with a new capture.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        expected_runtime_generation=expected_runtime_generation,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    expected_runtime_generation: int,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Read the original generation-conditioned snapshot receipt

     Reads only the capture identified by the authenticated caller, original
    Idempotency-Key and expected runtime generation. Does not admit, dispatch,
    retry, cancel or repair work. Completed receipts can be read after the
    source changes generation or pauses. A 404 is not proof of cancellation
    and must not clear an outstanding operation fence. A missing, expired or
    deleted retained snapshot is never replaced with a new capture.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        expected_runtime_generation=expected_runtime_generation,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    expected_runtime_generation: int,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSSnapshotResponse]]:
    """Read the original generation-conditioned snapshot receipt

     Reads only the capture identified by the authenticated caller, original
    Idempotency-Key and expected runtime generation. Does not admit, dispatch,
    retry, cancel or repair work. Completed receipts can be read after the
    source changes generation or pauses. A 404 is not proof of cancellation
    and must not clear an outstanding operation fence. A missing, expired or
    deleted retained snapshot is never replaced with a new capture.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

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
            expected_runtime_generation=expected_runtime_generation,
            idempotency_key=idempotency_key,
        )
    ).parsed
