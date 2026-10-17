from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_root_fs_fork_observation_response import (
    SuccessSandboxRootFSForkObservationResponse,
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
        "url": "/api/v1/sandboxes/{id}/fork".format(
            id=id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRootFSForkObservationResponse.from_dict(
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]:
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]:
    """Read original RootFS fork destination provenance

     Reads one external database observation for the original authenticated
    caller, Idempotency-Key and source runtime generation, including zero.
    Does not submit, retry, cancel or repair work, contact the guest or resume
    a runtime. Requires sandbox:read. A 404 is not proof of cancellation.
    Only RootFS forks qualify: memory forks are rejected. The child must
    remain paused, never run, and retain its original claim and durable head.
    Configuration must match birth or the one externally committed
    credential-free network isolation preparation; other changes are rejected.
    Running-source forks must retain their checkpoint
    proof; paused-source forks must retain the source filesystem binding.
    Later source generations or a retained source tombstone do not create
    a new capture. This is not a credential-safety attestation or a state
    reservation; subsequent mutations require their own identity conditions.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]
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
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]:
    """Read original RootFS fork destination provenance

     Reads one external database observation for the original authenticated
    caller, Idempotency-Key and source runtime generation, including zero.
    Does not submit, retry, cancel or repair work, contact the guest or resume
    a runtime. Requires sandbox:read. A 404 is not proof of cancellation.
    Only RootFS forks qualify: memory forks are rejected. The child must
    remain paused, never run, and retain its original claim and durable head.
    Configuration must match birth or the one externally committed
    credential-free network isolation preparation; other changes are rejected.
    Running-source forks must retain their checkpoint
    proof; paused-source forks must retain the source filesystem binding.
    Later source generations or a retained source tombstone do not create
    a new capture. This is not a credential-safety attestation or a state
    reservation; subsequent mutations require their own identity conditions.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]:
    """Read original RootFS fork destination provenance

     Reads one external database observation for the original authenticated
    caller, Idempotency-Key and source runtime generation, including zero.
    Does not submit, retry, cancel or repair work, contact the guest or resume
    a runtime. Requires sandbox:read. A 404 is not proof of cancellation.
    Only RootFS forks qualify: memory forks are rejected. The child must
    remain paused, never run, and retain its original claim and durable head.
    Configuration must match birth or the one externally committed
    credential-free network isolation preparation; other changes are rejected.
    Running-source forks must retain their checkpoint
    proof; paused-source forks must retain the source filesystem binding.
    Later source generations or a retained source tombstone do not create
    a new capture. This is not a credential-safety attestation or a state
    reservation; subsequent mutations require their own identity conditions.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]
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
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]]:
    """Read original RootFS fork destination provenance

     Reads one external database observation for the original authenticated
    caller, Idempotency-Key and source runtime generation, including zero.
    Does not submit, retry, cancel or repair work, contact the guest or resume
    a runtime. Requires sandbox:read. A 404 is not proof of cancellation.
    Only RootFS forks qualify: memory forks are rejected. The child must
    remain paused, never run, and retain its original claim and durable head.
    Configuration must match birth or the one externally committed
    credential-free network isolation preparation; other changes are rejected.
    Running-source forks must retain their checkpoint
    proof; paused-source forks must retain the source filesystem binding.
    Later source generations or a retained source tombstone do not create
    a new capture. This is not a credential-safety attestation or a state
    reservation; subsequent mutations require their own identity conditions.

    Args:
        id (str):
        expected_runtime_generation (int):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSForkObservationResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            expected_runtime_generation=expected_runtime_generation,
            idempotency_key=idempotency_key,
        )
    ).parsed
