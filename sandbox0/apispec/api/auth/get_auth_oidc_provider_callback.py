from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.success_login_response import SuccessLoginResponse
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    code: str,
    state: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["code"] = code

    params["state"] = state


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth/oidc/{provider}/callback".format(provider=provider,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ErrorEnvelope, SuccessLoginResponse]]:
    if response.status_code == 200:
        response_200 = SuccessLoginResponse.from_dict(response.json())



        return response_200

    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ErrorEnvelope, SuccessLoginResponse]]:
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
    code: str,
    state: str,

) -> Response[Union[Any, ErrorEnvelope, SuccessLoginResponse]]:
    """ OIDC callback

    Args:
        provider (str):
        code (str):
        state (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope, SuccessLoginResponse]]
     """


    kwargs = _get_kwargs(
        provider=provider,
code=code,
state=state,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    code: str,
    state: str,

) -> Optional[Union[Any, ErrorEnvelope, SuccessLoginResponse]]:
    """ OIDC callback

    Args:
        provider (str):
        code (str):
        state (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope, SuccessLoginResponse]
     """


    return sync_detailed(
        provider=provider,
client=client,
code=code,
state=state,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    code: str,
    state: str,

) -> Response[Union[Any, ErrorEnvelope, SuccessLoginResponse]]:
    """ OIDC callback

    Args:
        provider (str):
        code (str):
        state (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorEnvelope, SuccessLoginResponse]]
     """


    kwargs = _get_kwargs(
        provider=provider,
code=code,
state=state,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
    code: str,
    state: str,

) -> Optional[Union[Any, ErrorEnvelope, SuccessLoginResponse]]:
    """ OIDC callback

    Args:
        provider (str):
        code (str):
        state (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorEnvelope, SuccessLoginResponse]
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
code=code,
state=state,

    )).parsed
