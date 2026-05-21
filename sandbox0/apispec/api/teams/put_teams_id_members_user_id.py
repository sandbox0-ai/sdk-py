from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_message_response import SuccessMessageResponse
from ...models.update_team_member_request import UpdateTeamMemberRequest
from ...types import Response


def _get_kwargs(
    id: str,
    user_id: str,
    *,
    body: UpdateTeamMemberRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/teams/{id}/members/{user_id}".format(
            id=id,
            user_id=user_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessMessageResponse]]:
    if response.status_code == 200:
        response_200 = SuccessMessageResponse.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessMessageResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeamMemberRequest,
) -> Response[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Update team member role

    Args:
        id (str):
        user_id (str):
        body (UpdateTeamMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessMessageResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeamMemberRequest,
) -> Optional[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Update team member role

    Args:
        id (str):
        user_id (str):
        body (UpdateTeamMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessMessageResponse]
    """

    return sync_detailed(
        id=id,
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeamMemberRequest,
) -> Response[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Update team member role

    Args:
        id (str):
        user_id (str):
        body (UpdateTeamMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessMessageResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateTeamMemberRequest,
) -> Optional[Union[ErrorEnvelope, SuccessMessageResponse]]:
    """Update team member role

    Args:
        id (str):
        user_id (str):
        body (UpdateTeamMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessMessageResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
