from __future__ import annotations

from typing import Any, Optional, TYPE_CHECKING, Union

from sandbox0.apispec.api.usage import get_api_v1_usage_windows
from sandbox0.apispec.models.success_usage_windows_response import (
    SuccessUsageWindowsResponse,
)
from sandbox0.apispec.models.usage_window_page import UsageWindowPage
from sandbox0.apispec.types import UNSET, Unset
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.client import Client


class ClientUsageMixin:
    _api: Any

    def list_usage_windows(  # type: ignore[misc]
        self: "Client",
        *,
        cursor: Optional[str] = None,
        limit: int = 100,
        window_type: Optional[str] = None,
    ) -> UsageWindowPage:
        cursor_value: Union[Unset, str] = UNSET if cursor is None else cursor
        window_type_value: Union[Unset, str] = (
            UNSET if window_type is None else window_type
        )
        response = get_api_v1_usage_windows.sync_detailed(
            client=self._api,
            cursor=cursor_value,
            limit=limit,
            window_type=window_type_value,
        )
        return ensure_data(response, SuccessUsageWindowsResponse)
