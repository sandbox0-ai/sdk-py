from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.quota_dimension import QuotaDimension
from ...models.success_deleted_response import SuccessDeletedResponse
from typing import cast



def _get_kwargs(
    dimension: QuotaDimension,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/quotas/{dimension}".format(dimension=dimension,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorEnvelope, SuccessDeletedResponse]]:
    if response.status_code == 200:
        response_200 = SuccessDeletedResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorEnvelope, SuccessDeletedResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dimension: QuotaDimension,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ErrorEnvelope, SuccessDeletedResponse]]:
    """ Delete team quota

    Args:
        dimension (QuotaDimension):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessDeletedResponse]]
     """


    kwargs = _get_kwargs(
        dimension=dimension,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dimension: QuotaDimension,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ErrorEnvelope, SuccessDeletedResponse]]:
    """ Delete team quota

    Args:
        dimension (QuotaDimension):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessDeletedResponse]
     """


    return sync_detailed(
        dimension=dimension,
client=client,

    ).parsed

async def asyncio_detailed(
    dimension: QuotaDimension,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ErrorEnvelope, SuccessDeletedResponse]]:
    """ Delete team quota

    Args:
        dimension (QuotaDimension):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessDeletedResponse]]
     """


    kwargs = _get_kwargs(
        dimension=dimension,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dimension: QuotaDimension,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ErrorEnvelope, SuccessDeletedResponse]]:
    """ Delete team quota

    Args:
        dimension (QuotaDimension):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessDeletedResponse]
     """


    return (await asyncio_detailed(
        dimension=dimension,
client=client,

    )).parsed
