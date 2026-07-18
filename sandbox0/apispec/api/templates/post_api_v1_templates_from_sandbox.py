from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.success_template_response import SuccessTemplateResponse
from ...models.template_from_sandbox_create_request import (
    TemplateFromSandboxCreateRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TemplateFromSandboxCreateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/templates/from-sandbox",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessTemplateResponse]]:
    if response.status_code == 202:
        response_202 = SuccessTemplateResponse.from_dict(response.json())

        return response_202

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

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessTemplateResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TemplateFromSandboxCreateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessTemplateResponse]]:
    """Create template from sandbox

     Asynchronously captures the sandbox's writable root filesystem,
    publishes it to the Sandbox0-configured team registry, and creates a
    digest-pinned template. The capture point is reported by
    `status.creation.capturedAt`, not by acceptance of this request. Keep
    the source sandbox available and avoid rootfs writes until capture
    completes. Poll the returned template with
    `GET /api/v1/templates/{id}` until `status.creation.state` is `ready`
    or `failed`. The caller needs both `template:create` and
    `sandbox:read` permissions.

    Args:
        idempotency_key (Union[Unset, str]):
        body (TemplateFromSandboxCreateRequest): Creates a template by capturing the current root
            filesystem of an existing sandbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTemplateResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TemplateFromSandboxCreateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessTemplateResponse]]:
    """Create template from sandbox

     Asynchronously captures the sandbox's writable root filesystem,
    publishes it to the Sandbox0-configured team registry, and creates a
    digest-pinned template. The capture point is reported by
    `status.creation.capturedAt`, not by acceptance of this request. Keep
    the source sandbox available and avoid rootfs writes until capture
    completes. Poll the returned template with
    `GET /api/v1/templates/{id}` until `status.creation.state` is `ready`
    or `failed`. The caller needs both `template:create` and
    `sandbox:read` permissions.

    Args:
        idempotency_key (Union[Unset, str]):
        body (TemplateFromSandboxCreateRequest): Creates a template by capturing the current root
            filesystem of an existing sandbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTemplateResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TemplateFromSandboxCreateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorEnvelope, SuccessTemplateResponse]]:
    """Create template from sandbox

     Asynchronously captures the sandbox's writable root filesystem,
    publishes it to the Sandbox0-configured team registry, and creates a
    digest-pinned template. The capture point is reported by
    `status.creation.capturedAt`, not by acceptance of this request. Keep
    the source sandbox available and avoid rootfs writes until capture
    completes. Poll the returned template with
    `GET /api/v1/templates/{id}` until `status.creation.state` is `ready`
    or `failed`. The caller needs both `template:create` and
    `sandbox:read` permissions.

    Args:
        idempotency_key (Union[Unset, str]):
        body (TemplateFromSandboxCreateRequest): Creates a template by capturing the current root
            filesystem of an existing sandbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessTemplateResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TemplateFromSandboxCreateRequest,
    idempotency_key: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorEnvelope, SuccessTemplateResponse]]:
    """Create template from sandbox

     Asynchronously captures the sandbox's writable root filesystem,
    publishes it to the Sandbox0-configured team registry, and creates a
    digest-pinned template. The capture point is reported by
    `status.creation.capturedAt`, not by acceptance of this request. Keep
    the source sandbox available and avoid rootfs writes until capture
    completes. Poll the returned template with
    `GET /api/v1/templates/{id}` until `status.creation.state` is `ready`
    or `failed`. The caller needs both `template:create` and
    `sandbox:read` permissions.

    Args:
        idempotency_key (Union[Unset, str]):
        body (TemplateFromSandboxCreateRequest): Creates a template by capturing the current root
            filesystem of an existing sandbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessTemplateResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
