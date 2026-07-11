from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_session_spec import ExecutionSessionSpec
from ...models.success_execution_session_response import SuccessExecutionSessionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: ExecutionSessionSpec,
    idempotency_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/sessions".format(
            id=id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessExecutionSessionResponse]:
    if response.status_code == 200:
        response_200 = SuccessExecutionSessionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SuccessExecutionSessionResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessExecutionSessionResponse]:
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
    body: ExecutionSessionSpec,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[SuccessExecutionSessionResponse]:
    """Create an execution session

     Creates a durable process-backed session. The client connection does not own the session lifecycle.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (ExecutionSessionSpec): Generic process-backed session specification. The supervisor
            does not interpret application protocols.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessExecutionSessionResponse]
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
    body: ExecutionSessionSpec,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[SuccessExecutionSessionResponse]:
    """Create an execution session

     Creates a durable process-backed session. The client connection does not own the session lifecycle.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (ExecutionSessionSpec): Generic process-backed session specification. The supervisor
            does not interpret application protocols.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessExecutionSessionResponse
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
    body: ExecutionSessionSpec,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[SuccessExecutionSessionResponse]:
    """Create an execution session

     Creates a durable process-backed session. The client connection does not own the session lifecycle.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (ExecutionSessionSpec): Generic process-backed session specification. The supervisor
            does not interpret application protocols.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessExecutionSessionResponse]
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
    body: ExecutionSessionSpec,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[SuccessExecutionSessionResponse]:
    """Create an execution session

     Creates a durable process-backed session. The client connection does not own the session lifecycle.

    Args:
        id (str):
        idempotency_key (Union[Unset, str]):
        body (ExecutionSessionSpec): Generic process-backed session specification. The supervisor
            does not interpret application protocols.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessExecutionSessionResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
