from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.function_invoke_request import FunctionInvokeRequest
from ...models.success_function_invoke_response import SuccessFunctionInvokeResponse
from typing import cast



def _get_kwargs(
    id: str,
    name: str,
    *,
    body: FunctionInvokeRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/sandboxes/{id}/functions/{name}/invoke".format(id=id,name=name,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]:
    if response.status_code == 200:
        response_200 = SuccessFunctionInvokeResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: FunctionInvokeRequest,

) -> Response[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]:
    """ Invoke a sandbox function

     Invokes /workspace/functions/{name}.py through the Python function runtime. The default handler is
    `handler`.

    Args:
        id (str):
        name (str):
        body (FunctionInvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]
     """


    kwargs = _get_kwargs(
        id=id,
name=name,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: FunctionInvokeRequest,

) -> Optional[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]:
    """ Invoke a sandbox function

     Invokes /workspace/functions/{name}.py through the Python function runtime. The default handler is
    `handler`.

    Args:
        id (str):
        name (str):
        body (FunctionInvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessFunctionInvokeResponse]
     """


    return sync_detailed(
        id=id,
name=name,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: FunctionInvokeRequest,

) -> Response[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]:
    """ Invoke a sandbox function

     Invokes /workspace/functions/{name}.py through the Python function runtime. The default handler is
    `handler`.

    Args:
        id (str):
        name (str):
        body (FunctionInvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]
     """


    kwargs = _get_kwargs(
        id=id,
name=name,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    body: FunctionInvokeRequest,

) -> Optional[Union[ErrorEnvelope, SuccessFunctionInvokeResponse]]:
    """ Invoke a sandbox function

     Invokes /workspace/functions/{name}.py through the Python function runtime. The default handler is
    `handler`.

    Args:
        id (str):
        name (str):
        body (FunctionInvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessFunctionInvokeResponse]
     """


    return (await asyncio_detailed(
        id=id,
name=name,
client=client,
body=body,

    )).parsed
