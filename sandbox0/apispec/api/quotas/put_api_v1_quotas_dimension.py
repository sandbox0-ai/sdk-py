from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_envelope import ErrorEnvelope
from ...models.put_team_quota_request import PutTeamQuotaRequest
from ...models.quota_dimension import QuotaDimension
from ...models.success_team_quota_response import SuccessTeamQuotaResponse
from typing import cast



def _get_kwargs(
    dimension: QuotaDimension,
    *,
    body: PutTeamQuotaRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/quotas/{dimension}".format(dimension=dimension,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]:
    if response.status_code == 200:
        response_200 = SuccessTeamQuotaResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]:
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
    body: PutTeamQuotaRequest,

) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]:
    """ Set team quota

    Args:
        dimension (QuotaDimension):
        body (PutTeamQuotaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]
     """


    kwargs = _get_kwargs(
        dimension=dimension,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dimension: QuotaDimension,
    *,
    client: AuthenticatedClient,
    body: PutTeamQuotaRequest,

) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]:
    """ Set team quota

    Args:
        dimension (QuotaDimension):
        body (PutTeamQuotaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTeamQuotaResponse]
     """


    return sync_detailed(
        dimension=dimension,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dimension: QuotaDimension,
    *,
    client: AuthenticatedClient,
    body: PutTeamQuotaRequest,

) -> Response[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]:
    """ Set team quota

    Args:
        dimension (QuotaDimension):
        body (PutTeamQuotaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]
     """


    kwargs = _get_kwargs(
        dimension=dimension,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dimension: QuotaDimension,
    *,
    client: AuthenticatedClient,
    body: PutTeamQuotaRequest,

) -> Optional[Union[ErrorEnvelope, SuccessTeamQuotaResponse]]:
    """ Set team quota

    Args:
        dimension (QuotaDimension):
        body (PutTeamQuotaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTeamQuotaResponse]
     """


    return (await asyncio_detailed(
        dimension=dimension,
client=client,
body=body,

    )).parsed
