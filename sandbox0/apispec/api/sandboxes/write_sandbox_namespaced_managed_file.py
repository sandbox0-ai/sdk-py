from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.managed_file_write_request import ManagedFileWriteRequest
from ...models.success_managed_files_state_response import (
    SuccessManagedFilesStateResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    namespace: str,
    name: str,
    *,
    body: ManagedFileWriteRequest,
    runtime_generation: int,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["runtime_generation"] = runtime_generation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/sandboxes/{id}/managed-file-namespaces/{namespace}/{name}".format(
            id=id,
            namespace=namespace,
            name=name,
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]:
    if response.status_code == 200:
        response_200 = SuccessManagedFilesStateResponse.from_dict(response.json())

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
) -> Response[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedFileWriteRequest,
    runtime_generation: int,
) -> Response[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]:
    """Replace a namespaced managed runtime file conditionally

     The expected mutation sequence is consumed before file I/O. An ambiguous response must be reconciled
    with inspect/read; never automatically retry with a newly fetched sequence. The sequence orders
    platform requests, not native guest refreshes.

    Args:
        id (str):
        namespace (str):
        name (str):
        runtime_generation (int):
        body (ManagedFileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        namespace=namespace,
        name=name,
        body=body,
        runtime_generation=runtime_generation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedFileWriteRequest,
    runtime_generation: int,
) -> Optional[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]:
    """Replace a namespaced managed runtime file conditionally

     The expected mutation sequence is consumed before file I/O. An ambiguous response must be reconciled
    with inspect/read; never automatically retry with a newly fetched sequence. The sequence orders
    platform requests, not native guest refreshes.

    Args:
        id (str):
        namespace (str):
        name (str):
        runtime_generation (int):
        body (ManagedFileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessManagedFilesStateResponse]
    """

    return sync_detailed(
        id=id,
        namespace=namespace,
        name=name,
        client=client,
        body=body,
        runtime_generation=runtime_generation,
    ).parsed


async def asyncio_detailed(
    id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedFileWriteRequest,
    runtime_generation: int,
) -> Response[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]:
    """Replace a namespaced managed runtime file conditionally

     The expected mutation sequence is consumed before file I/O. An ambiguous response must be reconciled
    with inspect/read; never automatically retry with a newly fetched sequence. The sequence orders
    platform requests, not native guest refreshes.

    Args:
        id (str):
        namespace (str):
        name (str):
        runtime_generation (int):
        body (ManagedFileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        namespace=namespace,
        name=name,
        body=body,
        runtime_generation=runtime_generation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    namespace: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: ManagedFileWriteRequest,
    runtime_generation: int,
) -> Optional[Union[ErrorEnvelope, SuccessManagedFilesStateResponse]]:
    """Replace a namespaced managed runtime file conditionally

     The expected mutation sequence is consumed before file I/O. An ambiguous response must be reconciled
    with inspect/read; never automatically retry with a newly fetched sequence. The sequence orders
    platform requests, not native guest refreshes.

    Args:
        id (str):
        namespace (str):
        name (str):
        runtime_generation (int):
        body (ManagedFileWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessManagedFilesStateResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            namespace=namespace,
            name=name,
            client=client,
            body=body,
            runtime_generation=runtime_generation,
        )
    ).parsed
