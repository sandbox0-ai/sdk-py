from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.sandbox_execution_state_request import SandboxExecutionStateRequest
from ...models.success_resume_sandbox_response import SuccessResumeSandboxResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: SandboxExecutionStateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/resume".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]:
    if response.status_code == 200:
        response_200 = SuccessResumeSandboxResponse.from_dict(response.json())

        return response_200

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

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

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
) -> Response[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]:
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
    body: SandboxExecutionStateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]:
    """Resume a sandbox

     The default starts a new process runtime from the committed RootFS. Set memory=true to require a
    retained execution image. Missing, incompatible, or failed memory restoration returns an error and
    never authorizes a filesystem-only replacement. Accepted memory operations may continue through
    background recovery after a disconnected request. For conditional memory resume, send memory=true,
    expected_runtime_generation, checkpoint_id and Idempotency-Key together. Keep the same authenticated
    identity, key, checkpoint and source generation on retries. A successful conditional response proves
    this request committed its exact restore; unrelated running state or a later lifecycle conflicts. An
    aborted request cannot create a new restore attempt.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxExecutionStateRequest): Resume execution-state selection. Conditional memory
            resume requires all three body fields together with Idempotency-Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]
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
    body: SandboxExecutionStateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]:
    """Resume a sandbox

     The default starts a new process runtime from the committed RootFS. Set memory=true to require a
    retained execution image. Missing, incompatible, or failed memory restoration returns an error and
    never authorizes a filesystem-only replacement. Accepted memory operations may continue through
    background recovery after a disconnected request. For conditional memory resume, send memory=true,
    expected_runtime_generation, checkpoint_id and Idempotency-Key together. Keep the same authenticated
    identity, key, checkpoint and source generation on retries. A successful conditional response proves
    this request committed its exact restore; unrelated running state or a later lifecycle conflicts. An
    aborted request cannot create a new restore attempt.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxExecutionStateRequest): Resume execution-state selection. Conditional memory
            resume requires all three body fields together with Idempotency-Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessResumeSandboxResponse]
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
    body: SandboxExecutionStateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]:
    """Resume a sandbox

     The default starts a new process runtime from the committed RootFS. Set memory=true to require a
    retained execution image. Missing, incompatible, or failed memory restoration returns an error and
    never authorizes a filesystem-only replacement. Accepted memory operations may continue through
    background recovery after a disconnected request. For conditional memory resume, send memory=true,
    expected_runtime_generation, checkpoint_id and Idempotency-Key together. Keep the same authenticated
    identity, key, checkpoint and source generation on retries. A successful conditional response proves
    this request committed its exact restore; unrelated running state or a later lifecycle conflicts. An
    aborted request cannot create a new restore attempt.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxExecutionStateRequest): Resume execution-state selection. Conditional memory
            resume requires all three body fields together with Idempotency-Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]
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
    body: SandboxExecutionStateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessResumeSandboxResponse]]:
    """Resume a sandbox

     The default starts a new process runtime from the committed RootFS. Set memory=true to require a
    retained execution image. Missing, incompatible, or failed memory restoration returns an error and
    never authorizes a filesystem-only replacement. Accepted memory operations may continue through
    background recovery after a disconnected request. For conditional memory resume, send memory=true,
    expected_runtime_generation, checkpoint_id and Idempotency-Key together. Keep the same authenticated
    identity, key, checkpoint and source generation on retries. A successful conditional response proves
    this request committed its exact restore; unrelated running state or a later lifecycle conflicts. An
    aborted request cannot create a new restore attempt.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (SandboxExecutionStateRequest): Resume execution-state selection. Conditional memory
            resume requires all three body fields together with Idempotency-Key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessResumeSandboxResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
