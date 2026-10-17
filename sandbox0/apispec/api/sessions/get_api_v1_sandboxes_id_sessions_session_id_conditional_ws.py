from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    session_id: str,
    *,
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    attempt_id: str,
    after: Union[Unset, int] = UNSET,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    params["creation_runtime_generation"] = creation_runtime_generation

    params["runtime_generation"] = runtime_generation

    params["attempt_id"] = attempt_id

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/sessions/{session_id}/conditional/ws".format(
            id=id,
            session_id=session_id,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorEnvelope]]:
    if response.status_code == 101:
        response_101 = cast(Any, None)
        return response_101

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorEnvelope]]:
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
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    attempt_id: str,
    after: Union[Unset, int] = UNSET,
    idempotency_key: str,
) -> Response[Union[Any, ErrorEnvelope]]:
    """Attach to one conditional execution session attempt

     Requires the original conditional creation key, exact runtime generation and attempt.
    Never resumes, creates or falls back to an ordinary attachment. A generation change
    revokes the connection; every control message rechecks identity. Replay excludes
    other attempts. Closing the socket does not stop the process or close its input.
    This is process control, not lifecycle, storage or credential admission.
    For a memory-restored original attempt, explicitly supply an earlier
    creation_runtime_generation. Omission retains same-generation semantics.
    The supervisor requires the exact original conditional creation and a
    still-running attempt from that origin in the requested current runtime.
    This does not verify external memory lineage or credential qualification;
    applications must verify those independently before adoption. Never use
    failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        session_id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        attempt_id (str):
        after (Union[Unset, int]):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        creation_runtime_generation=creation_runtime_generation,
        runtime_generation=runtime_generation,
        attempt_id=attempt_id,
        after=after,
        idempotency_key=idempotency_key,
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
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    attempt_id: str,
    after: Union[Unset, int] = UNSET,
    idempotency_key: str,
) -> Optional[Union[Any, ErrorEnvelope]]:
    """Attach to one conditional execution session attempt

     Requires the original conditional creation key, exact runtime generation and attempt.
    Never resumes, creates or falls back to an ordinary attachment. A generation change
    revokes the connection; every control message rechecks identity. Replay excludes
    other attempts. Closing the socket does not stop the process or close its input.
    This is process control, not lifecycle, storage or credential admission.
    For a memory-restored original attempt, explicitly supply an earlier
    creation_runtime_generation. Omission retains same-generation semantics.
    The supervisor requires the exact original conditional creation and a
    still-running attempt from that origin in the requested current runtime.
    This does not verify external memory lineage or credential qualification;
    applications must verify those independently before adoption. Never use
    failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        session_id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        attempt_id (str):
        after (Union[Unset, int]):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope]
    """

    return sync_detailed(
        id=id,
        session_id=session_id,
        client=client,
        creation_runtime_generation=creation_runtime_generation,
        runtime_generation=runtime_generation,
        attempt_id=attempt_id,
        after=after,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    attempt_id: str,
    after: Union[Unset, int] = UNSET,
    idempotency_key: str,
) -> Response[Union[Any, ErrorEnvelope]]:
    """Attach to one conditional execution session attempt

     Requires the original conditional creation key, exact runtime generation and attempt.
    Never resumes, creates or falls back to an ordinary attachment. A generation change
    revokes the connection; every control message rechecks identity. Replay excludes
    other attempts. Closing the socket does not stop the process or close its input.
    This is process control, not lifecycle, storage or credential admission.
    For a memory-restored original attempt, explicitly supply an earlier
    creation_runtime_generation. Omission retains same-generation semantics.
    The supervisor requires the exact original conditional creation and a
    still-running attempt from that origin in the requested current runtime.
    This does not verify external memory lineage or credential qualification;
    applications must verify those independently before adoption. Never use
    failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        session_id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        attempt_id (str):
        after (Union[Unset, int]):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope]]
    """

    kwargs = _get_kwargs(
        id=id,
        session_id=session_id,
        creation_runtime_generation=creation_runtime_generation,
        runtime_generation=runtime_generation,
        attempt_id=attempt_id,
        after=after,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    creation_runtime_generation: Union[Unset, int] = UNSET,
    runtime_generation: int,
    attempt_id: str,
    after: Union[Unset, int] = UNSET,
    idempotency_key: str,
) -> Optional[Union[Any, ErrorEnvelope]]:
    """Attach to one conditional execution session attempt

     Requires the original conditional creation key, exact runtime generation and attempt.
    Never resumes, creates or falls back to an ordinary attachment. A generation change
    revokes the connection; every control message rechecks identity. Replay excludes
    other attempts. Closing the socket does not stop the process or close its input.
    This is process control, not lifecycle, storage or credential admission.
    For a memory-restored original attempt, explicitly supply an earlier
    creation_runtime_generation. Omission retains same-generation semantics.
    The supervisor requires the exact original conditional creation and a
    still-running attempt from that origin in the requested current runtime.
    This does not verify external memory lineage or credential qualification;
    applications must verify those independently before adoption. Never use
    failure as permission to create a new attempt or fall back to cold restart.

    Args:
        id (str):
        session_id (str):
        creation_runtime_generation (Union[Unset, int]):
        runtime_generation (int):
        attempt_id (str):
        after (Union[Unset, int]):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope]
    """

    return (
        await asyncio_detailed(
            id=id,
            session_id=session_id,
            client=client,
            creation_runtime_generation=creation_runtime_generation,
            runtime_generation=runtime_generation,
            attempt_id=attempt_id,
            after=after,
            idempotency_key=idempotency_key,
        )
    ).parsed
