from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_sandbox_root_fs_identity_response import (
    SuccessSandboxRootFSIdentityResponse,
)
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/rootfs/identity".format(
            id=id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRootFSIdentityResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]:
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
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]:
    """Read external runtime and RootFS identity

     Requires sandbox:read. Reads one owner-scoped control-plane database snapshot without guest
    execution, node probing or automatic resume. Binds runtime coordinates to the durable filesystem,
    committed head and immutable image digest. This is provenance, not current storage liveness, an
    uncommitted-write guarantee or credential-clean attestation. A later lifecycle can invalidate the
    observation; mutations must still condition on the expected runtime generation and their own
    admission evidence.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]:
    """Read external runtime and RootFS identity

     Requires sandbox:read. Reads one owner-scoped control-plane database snapshot without guest
    execution, node probing or automatic resume. Binds runtime coordinates to the durable filesystem,
    committed head and immutable image digest. This is provenance, not current storage liveness, an
    uncommitted-write guarantee or credential-clean attestation. A later lifecycle can invalidate the
    observation; mutations must still condition on the expected runtime generation and their own
    admission evidence.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]:
    """Read external runtime and RootFS identity

     Requires sandbox:read. Reads one owner-scoped control-plane database snapshot without guest
    execution, node probing or automatic resume. Binds runtime coordinates to the durable filesystem,
    committed head and immutable image digest. This is provenance, not current storage liveness, an
    uncommitted-write guarantee or credential-clean attestation. A later lifecycle can invalidate the
    observation; mutations must still condition on the expected runtime generation and their own
    admission evidence.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]]:
    """Read external runtime and RootFS identity

     Requires sandbox:read. Reads one owner-scoped control-plane database snapshot without guest
    execution, node probing or automatic resume. Binds runtime coordinates to the durable filesystem,
    committed head and immutable image digest. This is provenance, not current storage liveness, an
    uncommitted-write guarantee or credential-clean attestation. A later lifecycle can invalidate the
    observation; mutations must still condition on the expected runtime generation and their own
    admission evidence.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRootFSIdentityResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
