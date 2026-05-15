from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    id: str,
    *,
    container: Union[Unset, str] = 'procd',
    tail_lines: Union[Unset, int] = 200,
    limit_bytes: Union[Unset, int] = 1048576,
    follow: Union[Unset, bool] = False,
    previous: Union[Unset, bool] = False,
    timestamps: Union[Unset, bool] = False,
    since_seconds: Union[Unset, int] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["container"] = container

    params["tail_lines"] = tail_lines

    params["limit_bytes"] = limit_bytes

    params["follow"] = follow

    params["previous"] = previous

    params["timestamps"] = timestamps

    params["since_seconds"] = since_seconds


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/logs".format(id=id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorEnvelope, str]]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorEnvelope, str]]:
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
    container: Union[Unset, str] = 'procd',
    tail_lines: Union[Unset, int] = 200,
    limit_bytes: Union[Unset, int] = 1048576,
    follow: Union[Unset, bool] = False,
    previous: Union[Unset, bool] = False,
    timestamps: Union[Unset, bool] = False,
    since_seconds: Union[Unset, int] = UNSET,

) -> Response[Union[ErrorEnvelope, str]]:
    """ Get sandbox process logs

     Returns sandbox process output mirrored through the sandbox main container.
    Procd service logs are filtered out and remain available through Kubernetes pod logs.
    When `follow=false`, the response is a bounded text/plain snapshot.
    When `follow=true`, the response is a text/plain stream until the client disconnects.
    Kubernetes log selection parameters such as `tail_lines` and `limit_bytes`
    are applied before procd service log filtering.

    Args:
        id (str):
        container (Union[Unset, str]):  Default: 'procd'.
        tail_lines (Union[Unset, int]):  Default: 200.
        limit_bytes (Union[Unset, int]):  Default: 1048576.
        follow (Union[Unset, bool]):  Default: False.
        previous (Union[Unset, bool]):  Default: False.
        timestamps (Union[Unset, bool]):  Default: False.
        since_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, str]]
     """


    kwargs = _get_kwargs(
        id=id,
container=container,
tail_lines=tail_lines,
limit_bytes=limit_bytes,
follow=follow,
previous=previous,
timestamps=timestamps,
since_seconds=since_seconds,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    container: Union[Unset, str] = 'procd',
    tail_lines: Union[Unset, int] = 200,
    limit_bytes: Union[Unset, int] = 1048576,
    follow: Union[Unset, bool] = False,
    previous: Union[Unset, bool] = False,
    timestamps: Union[Unset, bool] = False,
    since_seconds: Union[Unset, int] = UNSET,

) -> Optional[Union[ErrorEnvelope, str]]:
    """ Get sandbox process logs

     Returns sandbox process output mirrored through the sandbox main container.
    Procd service logs are filtered out and remain available through Kubernetes pod logs.
    When `follow=false`, the response is a bounded text/plain snapshot.
    When `follow=true`, the response is a text/plain stream until the client disconnects.
    Kubernetes log selection parameters such as `tail_lines` and `limit_bytes`
    are applied before procd service log filtering.

    Args:
        id (str):
        container (Union[Unset, str]):  Default: 'procd'.
        tail_lines (Union[Unset, int]):  Default: 200.
        limit_bytes (Union[Unset, int]):  Default: 1048576.
        follow (Union[Unset, bool]):  Default: False.
        previous (Union[Unset, bool]):  Default: False.
        timestamps (Union[Unset, bool]):  Default: False.
        since_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, str]
     """


    return sync_detailed(
        id=id,
client=client,
container=container,
tail_lines=tail_lines,
limit_bytes=limit_bytes,
follow=follow,
previous=previous,
timestamps=timestamps,
since_seconds=since_seconds,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    container: Union[Unset, str] = 'procd',
    tail_lines: Union[Unset, int] = 200,
    limit_bytes: Union[Unset, int] = 1048576,
    follow: Union[Unset, bool] = False,
    previous: Union[Unset, bool] = False,
    timestamps: Union[Unset, bool] = False,
    since_seconds: Union[Unset, int] = UNSET,

) -> Response[Union[ErrorEnvelope, str]]:
    """ Get sandbox process logs

     Returns sandbox process output mirrored through the sandbox main container.
    Procd service logs are filtered out and remain available through Kubernetes pod logs.
    When `follow=false`, the response is a bounded text/plain snapshot.
    When `follow=true`, the response is a text/plain stream until the client disconnects.
    Kubernetes log selection parameters such as `tail_lines` and `limit_bytes`
    are applied before procd service log filtering.

    Args:
        id (str):
        container (Union[Unset, str]):  Default: 'procd'.
        tail_lines (Union[Unset, int]):  Default: 200.
        limit_bytes (Union[Unset, int]):  Default: 1048576.
        follow (Union[Unset, bool]):  Default: False.
        previous (Union[Unset, bool]):  Default: False.
        timestamps (Union[Unset, bool]):  Default: False.
        since_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, str]]
     """


    kwargs = _get_kwargs(
        id=id,
container=container,
tail_lines=tail_lines,
limit_bytes=limit_bytes,
follow=follow,
previous=previous,
timestamps=timestamps,
since_seconds=since_seconds,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    container: Union[Unset, str] = 'procd',
    tail_lines: Union[Unset, int] = 200,
    limit_bytes: Union[Unset, int] = 1048576,
    follow: Union[Unset, bool] = False,
    previous: Union[Unset, bool] = False,
    timestamps: Union[Unset, bool] = False,
    since_seconds: Union[Unset, int] = UNSET,

) -> Optional[Union[ErrorEnvelope, str]]:
    """ Get sandbox process logs

     Returns sandbox process output mirrored through the sandbox main container.
    Procd service logs are filtered out and remain available through Kubernetes pod logs.
    When `follow=false`, the response is a bounded text/plain snapshot.
    When `follow=true`, the response is a text/plain stream until the client disconnects.
    Kubernetes log selection parameters such as `tail_lines` and `limit_bytes`
    are applied before procd service log filtering.

    Args:
        id (str):
        container (Union[Unset, str]):  Default: 'procd'.
        tail_lines (Union[Unset, int]):  Default: 200.
        limit_bytes (Union[Unset, int]):  Default: 1048576.
        follow (Union[Unset, bool]):  Default: False.
        previous (Union[Unset, bool]):  Default: False.
        timestamps (Union[Unset, bool]):  Default: False.
        since_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, str]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
container=container,
tail_lines=tail_lines,
limit_bytes=limit_bytes,
follow=follow,
previous=previous,
timestamps=timestamps,
since_seconds=since_seconds,

    )).parsed
