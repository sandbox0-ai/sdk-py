from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_created_response import SuccessCreatedResponse
from ...models.success_written_response import SuccessWrittenResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: File,
    path: str,
    mkdir: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["path"] = path

    params["mkdir"] = mkdir

    params["recursive"] = recursive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/files".format(
            id=id,
        ),
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SuccessCreatedResponse, SuccessWrittenResponse]]:
    if response.status_code == 200:
        response_200 = SuccessWrittenResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SuccessCreatedResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SuccessCreatedResponse, SuccessWrittenResponse]]:
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
    body: File,
    path: str,
    mkdir: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Response[Union[SuccessCreatedResponse, SuccessWrittenResponse]]:
    """Write file or create directory

     Use `path` query param and `mkdir=true` to create directories, otherwise writes file content.

    Args:
        id (str):
        path (str):
        mkdir (Union[Unset, bool]):
        recursive (Union[Unset, bool]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SuccessCreatedResponse, SuccessWrittenResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        path=path,
        mkdir=mkdir,
        recursive=recursive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: File,
    path: str,
    mkdir: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Optional[Union[SuccessCreatedResponse, SuccessWrittenResponse]]:
    """Write file or create directory

     Use `path` query param and `mkdir=true` to create directories, otherwise writes file content.

    Args:
        id (str):
        path (str):
        mkdir (Union[Unset, bool]):
        recursive (Union[Unset, bool]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SuccessCreatedResponse, SuccessWrittenResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        path=path,
        mkdir=mkdir,
        recursive=recursive,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: File,
    path: str,
    mkdir: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Response[Union[SuccessCreatedResponse, SuccessWrittenResponse]]:
    """Write file or create directory

     Use `path` query param and `mkdir=true` to create directories, otherwise writes file content.

    Args:
        id (str):
        path (str):
        mkdir (Union[Unset, bool]):
        recursive (Union[Unset, bool]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SuccessCreatedResponse, SuccessWrittenResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        path=path,
        mkdir=mkdir,
        recursive=recursive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: File,
    path: str,
    mkdir: Union[Unset, bool] = UNSET,
    recursive: Union[Unset, bool] = UNSET,
) -> Optional[Union[SuccessCreatedResponse, SuccessWrittenResponse]]:
    """Write file or create directory

     Use `path` query param and `mkdir=true` to create directories, otherwise writes file content.

    Args:
        id (str):
        path (str):
        mkdir (Union[Unset, bool]):
        recursive (Union[Unset, bool]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SuccessCreatedResponse, SuccessWrittenResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            path=path,
            mkdir=mkdir,
            recursive=recursive,
        )
    ).parsed
