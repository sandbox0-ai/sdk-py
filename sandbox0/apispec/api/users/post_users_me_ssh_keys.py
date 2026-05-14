from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_ssh_public_key_request import CreateSSHPublicKeyRequest
from ...models.error_envelope import ErrorEnvelope
from ...models.success_ssh_public_key_response import SuccessSSHPublicKeyResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateSSHPublicKeyRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/me/ssh-keys",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]:
    if response.status_code == 201:
        response_201 = SuccessSSHPublicKeyResponse.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSSHPublicKeyRequest,

) -> Response[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]:
    """ Create a current user SSH public key

    Args:
        body (CreateSSHPublicKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CreateSSHPublicKeyRequest,

) -> Optional[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]:
    """ Create a current user SSH public key

    Args:
        body (CreateSSHPublicKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSSHPublicKeyRequest,

) -> Response[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]:
    """ Create a current user SSH public key

    Args:
        body (CreateSSHPublicKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateSSHPublicKeyRequest,

) -> Optional[Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]]:
    """ Create a current user SSH public key

    Args:
        body (CreateSSHPublicKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSSHPublicKeyResponse]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
