from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_file_list_response import SuccessFileListResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    path: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/files/list".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessFileListResponse]:
    if response.status_code == 200:
        response_200 = SuccessFileListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessFileListResponse]:
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
    path: str,
) -> Response[SuccessFileListResponse]:
    """List directory entries

     Use query params:
    - path=/tmp: target directory path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessFileListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> Optional[SuccessFileListResponse]:
    """List directory entries

     Use query params:
    - path=/tmp: target directory path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessFileListResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        path=path,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> Response[SuccessFileListResponse]:
    """List directory entries

     Use query params:
    - path=/tmp: target directory path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessFileListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
) -> Optional[SuccessFileListResponse]:
    """List directory entries

     Use query params:
    - path=/tmp: target directory path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessFileListResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            path=path,
        )
    ).parsed
