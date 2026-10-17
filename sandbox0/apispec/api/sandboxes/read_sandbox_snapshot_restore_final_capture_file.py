from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_restart_final_capture_file_response import (
    SuccessSandboxRestartFinalCaptureFileResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    operation_id: str,
    namespace: str,
    name: str,
    *,
    capture_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["capture_id"] = capture_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/snapshot-restore-operations/{operation_id}/final-capture/namespaces/{namespace}/{name}".format(
            id=id,
            operation_id=operation_id,
            namespace=namespace,
            name=name,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRestartFinalCaptureFileResponse.from_dict(
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    operation_id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    capture_id: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]:
    """Read a file from the exact stopped restart source

     Requires sandbox:read and the exact capture_id from status. Never reads live or guest storage,
    creates files, or resumes execution. found=false attests an absent file only after retained backing
    and external absence are verified. Missing journals, mounts, authority and routes are errors, never
    logout. Read closes after acknowledgement. Responses must not be logged or cached.

    Args:
        id (str):
        operation_id (str):
        namespace (str):
        name (str):
        capture_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        operation_id=operation_id,
        namespace=namespace,
        name=name,
        capture_id=capture_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    operation_id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    capture_id: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]:
    """Read a file from the exact stopped restart source

     Requires sandbox:read and the exact capture_id from status. Never reads live or guest storage,
    creates files, or resumes execution. found=false attests an absent file only after retained backing
    and external absence are verified. Missing journals, mounts, authority and routes are errors, never
    logout. Read closes after acknowledgement. Responses must not be logged or cached.

    Args:
        id (str):
        operation_id (str):
        namespace (str):
        name (str):
        capture_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]
    """

    return sync_detailed(
        id=id,
        operation_id=operation_id,
        namespace=namespace,
        name=name,
        client=client,
        capture_id=capture_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    operation_id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    capture_id: str,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]:
    """Read a file from the exact stopped restart source

     Requires sandbox:read and the exact capture_id from status. Never reads live or guest storage,
    creates files, or resumes execution. found=false attests an absent file only after retained backing
    and external absence are verified. Missing journals, mounts, authority and routes are errors, never
    logout. Read closes after acknowledgement. Responses must not be logged or cached.

    Args:
        id (str):
        operation_id (str):
        namespace (str):
        name (str):
        capture_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        operation_id=operation_id,
        namespace=namespace,
        name=name,
        capture_id=capture_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    operation_id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    capture_id: str,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]]:
    """Read a file from the exact stopped restart source

     Requires sandbox:read and the exact capture_id from status. Never reads live or guest storage,
    creates files, or resumes execution. found=false attests an absent file only after retained backing
    and external absence are verified. Missing journals, mounts, authority and routes are errors, never
    logout. Read closes after acknowledgement. Responses must not be logged or cached.

    Args:
        id (str):
        operation_id (str):
        namespace (str):
        name (str):
        capture_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRestartFinalCaptureFileResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            operation_id=operation_id,
            namespace=namespace,
            name=name,
            client=client,
            capture_id=capture_id,
        )
    ).parsed
