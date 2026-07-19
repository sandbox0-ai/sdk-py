from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.execution_session_desired_state_request import (
    ExecutionSessionDesiredStateRequest,
)
from ...models.success_execution_session_response import SuccessExecutionSessionResponse
from ...types import Response


def _get_kwargs(
    id: str,
    session_id: str,
    *,
    body: ExecutionSessionDesiredStateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/sandboxes/{id}/sessions/{session_id}/desired-state".format(
            id=id,
            session_id=session_id,
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
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: ExecutionSessionDesiredStateRequest,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Set execution session desired state

    Args:
        id (str):
        session_id (str):
        body (ExecutionSessionDesiredStateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: ExecutionSessionDesiredStateRequest,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Set execution session desired state

    Args:
        id (str):
        session_id (str):
        body (ExecutionSessionDesiredStateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionResponse]
    """

    return sync_detailed(
        id=id,
        session_id=session_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: ExecutionSessionDesiredStateRequest,
) -> Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Set execution session desired state

    Args:
        id (str):
        session_id (str):
        body (ExecutionSessionDesiredStateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    body: ExecutionSessionDesiredStateRequest,
) -> Optional[Union[ErrorEnvelope, SuccessExecutionSessionResponse]]:
    """Set execution session desired state

    Args:
        id (str):
        session_id (str):
        body (ExecutionSessionDesiredStateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessExecutionSessionResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            session_id=session_id,
            client=client,
            body=body,
        )
    ).parsed
