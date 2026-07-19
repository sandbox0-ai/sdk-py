import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.observability_event_source import ObservabilityEventSource
from ...models.sandbox_audit_actor_kind import SandboxAuditActorKind
from ...models.sandbox_observability_event_type import SandboxObservabilityEventType
from ...models.sandbox_observability_outcome import SandboxObservabilityOutcome
from ...models.success_sandbox_observability_events_response import (
    SuccessSandboxObservabilityEventsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    watch: Union[Unset, bool] = False,
    source: Union[Unset, ObservabilityEventSource] = UNSET,
    event_type: Union[Unset, SandboxObservabilityEventType] = UNSET,
    outcome: Union[Unset, SandboxObservabilityOutcome] = UNSET,
    actor_kind: Union[Unset, SandboxAuditActorKind] = UNSET,
    actor_id: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, str] = UNSET,
    operation_id: Union[Unset, str] = UNSET,
    event_id: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["start_time"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["end_time"] = json_end_time

    params["limit"] = limit

    params["cursor"] = cursor

    params["watch"] = watch

    json_source: Union[Unset, str] = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    json_event_type: Union[Unset, str] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type.value

    params["event_type"] = json_event_type

    json_outcome: Union[Unset, str] = UNSET
    if not isinstance(outcome, Unset):
        json_outcome = outcome.value

    params["outcome"] = json_outcome

    json_actor_kind: Union[Unset, str] = UNSET
    if not isinstance(actor_kind, Unset):
        json_actor_kind = actor_kind.value

    params["actor_kind"] = json_actor_kind

    params["actor_id"] = actor_id

    params["action"] = action

    params["resource_type"] = resource_type

    params["operation_id"] = operation_id

    json_event_id: Union[Unset, str] = UNSET
    if not isinstance(event_id, Unset):
        json_event_id = str(event_id)
    params["event_id"] = json_event_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/observability/events".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxObservabilityEventsResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

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
) -> Response[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]:
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
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    watch: Union[Unset, bool] = False,
    source: Union[Unset, ObservabilityEventSource] = UNSET,
    event_type: Union[Unset, SandboxObservabilityEventType] = UNSET,
    outcome: Union[Unset, SandboxObservabilityOutcome] = UNSET,
    actor_kind: Union[Unset, SandboxAuditActorKind] = UNSET,
    actor_id: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, str] = UNSET,
    operation_id: Union[Unset, str] = UNSET,
    event_id: Union[Unset, UUID] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]:
    """Query canonical signed sandbox observability events

     Queries canonical signed per-sandbox audit facts from ClickHouse. Every returned
    event includes an inline signature verification status, while event-ID payload
    conflicts are reported independently. Access requires the enterprise sandbox_audit
    feature and the sandboxaudit:read permission.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        watch (Union[Unset, bool]):  Default: False.
        source (Union[Unset, ObservabilityEventSource]):
        event_type (Union[Unset, SandboxObservabilityEventType]):
        outcome (Union[Unset, SandboxObservabilityOutcome]):
        actor_kind (Union[Unset, SandboxAuditActorKind]):
        actor_id (Union[Unset, str]):
        action (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        operation_id (Union[Unset, str]):
        event_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
        cursor=cursor,
        watch=watch,
        source=source,
        event_type=event_type,
        outcome=outcome,
        actor_kind=actor_kind,
        actor_id=actor_id,
        action=action,
        resource_type=resource_type,
        operation_id=operation_id,
        event_id=event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    watch: Union[Unset, bool] = False,
    source: Union[Unset, ObservabilityEventSource] = UNSET,
    event_type: Union[Unset, SandboxObservabilityEventType] = UNSET,
    outcome: Union[Unset, SandboxObservabilityOutcome] = UNSET,
    actor_kind: Union[Unset, SandboxAuditActorKind] = UNSET,
    actor_id: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, str] = UNSET,
    operation_id: Union[Unset, str] = UNSET,
    event_id: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]:
    """Query canonical signed sandbox observability events

     Queries canonical signed per-sandbox audit facts from ClickHouse. Every returned
    event includes an inline signature verification status, while event-ID payload
    conflicts are reported independently. Access requires the enterprise sandbox_audit
    feature and the sandboxaudit:read permission.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        watch (Union[Unset, bool]):  Default: False.
        source (Union[Unset, ObservabilityEventSource]):
        event_type (Union[Unset, SandboxObservabilityEventType]):
        outcome (Union[Unset, SandboxObservabilityOutcome]):
        actor_kind (Union[Unset, SandboxAuditActorKind]):
        actor_id (Union[Unset, str]):
        action (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        operation_id (Union[Unset, str]):
        event_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
        cursor=cursor,
        watch=watch,
        source=source,
        event_type=event_type,
        outcome=outcome,
        actor_kind=actor_kind,
        actor_id=actor_id,
        action=action,
        resource_type=resource_type,
        operation_id=operation_id,
        event_id=event_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    watch: Union[Unset, bool] = False,
    source: Union[Unset, ObservabilityEventSource] = UNSET,
    event_type: Union[Unset, SandboxObservabilityEventType] = UNSET,
    outcome: Union[Unset, SandboxObservabilityOutcome] = UNSET,
    actor_kind: Union[Unset, SandboxAuditActorKind] = UNSET,
    actor_id: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, str] = UNSET,
    operation_id: Union[Unset, str] = UNSET,
    event_id: Union[Unset, UUID] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]:
    """Query canonical signed sandbox observability events

     Queries canonical signed per-sandbox audit facts from ClickHouse. Every returned
    event includes an inline signature verification status, while event-ID payload
    conflicts are reported independently. Access requires the enterprise sandbox_audit
    feature and the sandboxaudit:read permission.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        watch (Union[Unset, bool]):  Default: False.
        source (Union[Unset, ObservabilityEventSource]):
        event_type (Union[Unset, SandboxObservabilityEventType]):
        outcome (Union[Unset, SandboxObservabilityOutcome]):
        actor_kind (Union[Unset, SandboxAuditActorKind]):
        actor_id (Union[Unset, str]):
        action (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        operation_id (Union[Unset, str]):
        event_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
        cursor=cursor,
        watch=watch,
        source=source,
        event_type=event_type,
        outcome=outcome,
        actor_kind=actor_kind,
        actor_id=actor_id,
        action=action,
        resource_type=resource_type,
        operation_id=operation_id,
        event_id=event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
    watch: Union[Unset, bool] = False,
    source: Union[Unset, ObservabilityEventSource] = UNSET,
    event_type: Union[Unset, SandboxObservabilityEventType] = UNSET,
    outcome: Union[Unset, SandboxObservabilityOutcome] = UNSET,
    actor_kind: Union[Unset, SandboxAuditActorKind] = UNSET,
    actor_id: Union[Unset, str] = UNSET,
    action: Union[Unset, str] = UNSET,
    resource_type: Union[Unset, str] = UNSET,
    operation_id: Union[Unset, str] = UNSET,
    event_id: Union[Unset, UUID] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]]:
    """Query canonical signed sandbox observability events

     Queries canonical signed per-sandbox audit facts from ClickHouse. Every returned
    event includes an inline signature verification status, while event-ID payload
    conflicts are reported independently. Access requires the enterprise sandbox_audit
    feature and the sandboxaudit:read permission.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):  Default: 100.
        cursor (Union[Unset, str]):
        watch (Union[Unset, bool]):  Default: False.
        source (Union[Unset, ObservabilityEventSource]):
        event_type (Union[Unset, SandboxObservabilityEventType]):
        outcome (Union[Unset, SandboxObservabilityOutcome]):
        actor_kind (Union[Unset, SandboxAuditActorKind]):
        actor_id (Union[Unset, str]):
        action (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        operation_id (Union[Unset, str]):
        event_id (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxObservabilityEventsResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor,
            watch=watch,
            source=source,
            event_type=event_type,
            outcome=outcome,
            actor_kind=actor_kind,
            actor_id=actor_id,
            action=action,
            resource_type=resource_type,
            operation_id=operation_id,
            event_id=event_id,
        )
    ).parsed
