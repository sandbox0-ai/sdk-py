from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.device_login_poll_request import DeviceLoginPollRequest
from ...models.error_envelope import ErrorEnvelope
from ...models.success_device_login_poll_response import SuccessDeviceLoginPollResponse
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: DeviceLoginPollRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/oidc/{provider}/device/poll".format(provider=provider,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]:
    if response.status_code == 200:
        response_200 = SuccessDeviceLoginPollResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeviceLoginPollRequest,

) -> Response[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]:
    """ Poll OIDC device login

    Args:
        provider (str):
        body (DeviceLoginPollRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeviceLoginPollRequest,

) -> Optional[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]:
    """ Poll OIDC device login

    Args:
        provider (str):
        body (DeviceLoginPollRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]
     """


    return sync_detailed(
        provider=provider,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeviceLoginPollRequest,

) -> Response[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]:
    """ Poll OIDC device login

    Args:
        provider (str):
        body (DeviceLoginPollRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeviceLoginPollRequest,

) -> Optional[Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]]:
    """ Poll OIDC device login

    Args:
        provider (str):
        body (DeviceLoginPollRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessDeviceLoginPollResponse]
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,

    )).parsed
