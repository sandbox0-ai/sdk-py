from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.process_input_event import ProcessInputEvent
from ...models.success_process_event_response import SuccessProcessEventResponse
from ...types import Response


def _get_kwargs(
    id: str,
    process_id: str,
    *,
    body: ProcessInputEvent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/processes/{process_id}/events".format(
            id=id,
            process_id=process_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessProcessEventResponse]]:
    if response.status_code == 202:
        response_202 = SuccessProcessEventResponse.from_dict(response.json())

        return response_202

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessProcessEventResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ProcessInputEvent,
) -> Response[Union[ErrorEnvelope, SuccessProcessEventResponse]]:
    """Send process input event

     Sends an idempotent input event to one process channel. event_id is required and repeated identical
    events return the original accepted event.

    Args:
        id (str):
        process_id (str):
        body (ProcessInputEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessProcessEventResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        process_id=process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ProcessInputEvent,
) -> Optional[Union[ErrorEnvelope, SuccessProcessEventResponse]]:
    """Send process input event

     Sends an idempotent input event to one process channel. event_id is required and repeated identical
    events return the original accepted event.

    Args:
        id (str):
        process_id (str):
        body (ProcessInputEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessProcessEventResponse]
    """

    return sync_detailed(
        id=id,
        process_id=process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ProcessInputEvent,
) -> Response[Union[ErrorEnvelope, SuccessProcessEventResponse]]:
    """Send process input event

     Sends an idempotent input event to one process channel. event_id is required and repeated identical
    events return the original accepted event.

    Args:
        id (str):
        process_id (str):
        body (ProcessInputEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessProcessEventResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        process_id=process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ProcessInputEvent,
) -> Optional[Union[ErrorEnvelope, SuccessProcessEventResponse]]:
    """Send process input event

     Sends an idempotent input event to one process channel. event_id is required and repeated identical
    events return the original accepted event.

    Args:
        id (str):
        process_id (str):
        body (ProcessInputEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessProcessEventResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            process_id=process_id,
            client=client,
            body=body,
        )
    ).parsed
