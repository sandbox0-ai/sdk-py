from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_file_stat_response import SuccessFileStatResponse
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
        "url": "/api/v1/sandboxes/{id}/files/stat".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuccessFileStatResponse]:
    if response.status_code == 200:
        response_200 = SuccessFileStatResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuccessFileStatResponse]:
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
) -> Response[SuccessFileStatResponse]:
    """Stat a file

     Use query params:
    - path=/tmp/a.txt: target file path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessFileStatResponse]
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
) -> Optional[SuccessFileStatResponse]:
    """Stat a file

     Use query params:
    - path=/tmp/a.txt: target file path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessFileStatResponse
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
) -> Response[SuccessFileStatResponse]:
    """Stat a file

     Use query params:
    - path=/tmp/a.txt: target file path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuccessFileStatResponse]
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
) -> Optional[SuccessFileStatResponse]:
    """Stat a file

     Use query params:
    - path=/tmp/a.txt: target file path

    Args:
        id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuccessFileStatResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            path=path,
        )
    ).parsed
