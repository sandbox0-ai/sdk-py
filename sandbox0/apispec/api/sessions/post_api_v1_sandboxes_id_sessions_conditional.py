from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conditional_execution_session_request import (
    ConditionalExecutionSessionRequest,
)
from ...models.error_envelope import ErrorEnvelope
from ...models.success_execution_session_response import SuccessExecutionSessionResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ConditionalExecutionSessionRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/sessions/conditional".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    if response.status_code == 200:
        response_200 = SuccessExecutionSessionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SuccessExecutionSessionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
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
    body: ConditionalExecutionSessionRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Create an execution session in an exact runtime generation

     Requires a currently running sandbox with the exact sandbox identity and runtime generation. Never
    auto-resumes. The gateway checks regional state and the supervisor checks identity atomically
    through initial process startup. A stale idempotent retry fails after runtime replacement. This
    condition governs creation; the session lifecycle policy still governs later attempts and recovery.
    Older servers return an unsupported route; clients must not fall back to unconditional creation.

    Args:
        id (str):
        idempotency_key (str):
        body (ConditionalExecutionSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]
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
    body: ConditionalExecutionSessionRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Create an execution session in an exact runtime generation

     Requires a currently running sandbox with the exact sandbox identity and runtime generation. Never
    auto-resumes. The gateway checks regional state and the supervisor checks identity atomically
    through initial process startup. A stale idempotent retry fails after runtime replacement. This
    condition governs creation; the session lifecycle policy still governs later attempts and recovery.
    Older servers return an unsupported route; clients must not fall back to unconditional creation.

    Args:
        id (str):
        idempotency_key (str):
        body (ConditionalExecutionSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionResponse]
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
    body: ConditionalExecutionSessionRequest,
    idempotency_key: str,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Create an execution session in an exact runtime generation

     Requires a currently running sandbox with the exact sandbox identity and runtime generation. Never
    auto-resumes. The gateway checks regional state and the supervisor checks identity atomically
    through initial process startup. A stale idempotent retry fails after runtime replacement. This
    condition governs creation; the session lifecycle policy still governs later attempts and recovery.
    Older servers return an unsupported route; clients must not fall back to unconditional creation.

    Args:
        id (str):
        idempotency_key (str):
        body (ConditionalExecutionSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]
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
    body: ConditionalExecutionSessionRequest,
    idempotency_key: str,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Create an execution session in an exact runtime generation

     Requires a currently running sandbox with the exact sandbox identity and runtime generation. Never
    auto-resumes. The gateway checks regional state and the supervisor checks identity atomically
    through initial process startup. A stale idempotent retry fails after runtime replacement. This
    condition governs creation; the session lifecycle policy still governs later attempts and recovery.
    Older servers return an unsupported route; clients must not fall back to unconditional creation.

    Args:
        id (str):
        idempotency_key (str):
        body (ConditionalExecutionSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
