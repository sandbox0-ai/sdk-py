import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.sandbox_runtime_metric_statistic import SandboxRuntimeMetricStatistic
from ...models.success_sandbox_runtime_metrics_response import (
    SuccessSandboxRuntimeMetricsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    metrics: Union[Unset, str] = UNSET,
    step_seconds: Union[Unset, int] = UNSET,
    statistic: Union[Unset, SandboxRuntimeMetricStatistic] = UNSET,
    max_points: Union[Unset, int] = 240,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["start_time"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["end_time"] = json_end_time

    params["metrics"] = metrics

    params["step_seconds"] = step_seconds

    json_statistic: Union[Unset, str] = UNSET
    if not isinstance(statistic, Unset):
        json_statistic = statistic.value

    params["statistic"] = json_statistic

    params["max_points"] = max_points

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sandboxes/{id}/metrics".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]:
    if response.status_code == 200:
        response_200 = SuccessSandboxRuntimeMetricsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]:
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
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    metrics: Union[Unset, str] = UNSET,
    step_seconds: Union[Unset, int] = UNSET,
    statistic: Union[Unset, SandboxRuntimeMetricStatistic] = UNSET,
    max_points: Union[Unset, int] = 240,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]:
    """Query chart-ready sandbox runtime metrics

     Returns bounded, downsampled sandbox-wide runtime series. When timestamps are
    omitted, the query covers the hour ending now. The maximum range is 30 days.
    Counter rates never cross a runtime reset boundary. Missing data is reported
    as gaps and is never synthesized as zero. This endpoint is separate from
    platform service metrics and metering usage truth.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        metrics (Union[Unset, str]):
        step_seconds (Union[Unset, int]):
        statistic (Union[Unset, SandboxRuntimeMetricStatistic]):
        max_points (Union[Unset, int]):  Default: 240.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        start_time=start_time,
        end_time=end_time,
        metrics=metrics,
        step_seconds=step_seconds,
        statistic=statistic,
        max_points=max_points,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    metrics: Union[Unset, str] = UNSET,
    step_seconds: Union[Unset, int] = UNSET,
    statistic: Union[Unset, SandboxRuntimeMetricStatistic] = UNSET,
    max_points: Union[Unset, int] = 240,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]:
    """Query chart-ready sandbox runtime metrics

     Returns bounded, downsampled sandbox-wide runtime series. When timestamps are
    omitted, the query covers the hour ending now. The maximum range is 30 days.
    Counter rates never cross a runtime reset boundary. Missing data is reported
    as gaps and is never synthesized as zero. This endpoint is separate from
    platform service metrics and metering usage truth.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        metrics (Union[Unset, str]):
        step_seconds (Union[Unset, int]):
        statistic (Union[Unset, SandboxRuntimeMetricStatistic]):
        max_points (Union[Unset, int]):  Default: 240.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        start_time=start_time,
        end_time=end_time,
        metrics=metrics,
        step_seconds=step_seconds,
        statistic=statistic,
        max_points=max_points,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    metrics: Union[Unset, str] = UNSET,
    step_seconds: Union[Unset, int] = UNSET,
    statistic: Union[Unset, SandboxRuntimeMetricStatistic] = UNSET,
    max_points: Union[Unset, int] = 240,
) -> Response[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]:
    """Query chart-ready sandbox runtime metrics

     Returns bounded, downsampled sandbox-wide runtime series. When timestamps are
    omitted, the query covers the hour ending now. The maximum range is 30 days.
    Counter rates never cross a runtime reset boundary. Missing data is reported
    as gaps and is never synthesized as zero. This endpoint is separate from
    platform service metrics and metering usage truth.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        metrics (Union[Unset, str]):
        step_seconds (Union[Unset, int]):
        statistic (Union[Unset, SandboxRuntimeMetricStatistic]):
        max_points (Union[Unset, int]):  Default: 240.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        start_time=start_time,
        end_time=end_time,
        metrics=metrics,
        step_seconds=step_seconds,
        statistic=statistic,
        max_points=max_points,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    metrics: Union[Unset, str] = UNSET,
    step_seconds: Union[Unset, int] = UNSET,
    statistic: Union[Unset, SandboxRuntimeMetricStatistic] = UNSET,
    max_points: Union[Unset, int] = 240,
) -> Optional[Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]]:
    """Query chart-ready sandbox runtime metrics

     Returns bounded, downsampled sandbox-wide runtime series. When timestamps are
    omitted, the query covers the hour ending now. The maximum range is 30 days.
    Counter rates never cross a runtime reset boundary. Missing data is reported
    as gaps and is never synthesized as zero. This endpoint is separate from
    platform service metrics and metering usage truth.

    Args:
        id (str):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        metrics (Union[Unset, str]):
        step_seconds (Union[Unset, int]):
        statistic (Union[Unset, SandboxRuntimeMetricStatistic]):
        max_points (Union[Unset, int]):  Default: 240.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorEnvelope, SuccessSandboxRuntimeMetricsResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            start_time=start_time,
            end_time=end_time,
            metrics=metrics,
            step_seconds=step_seconds,
            statistic=statistic,
            max_points=max_points,
        )
    ).parsed
