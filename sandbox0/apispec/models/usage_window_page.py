from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.usage_window import UsageWindow


T = TypeVar("T", bound="UsageWindowPage")


@_attrs_define
class UsageWindowPage:
    """
    Attributes:
        windows (list['UsageWindow']):
        next_cursor (str):
    """

    windows: list["UsageWindow"]
    next_cursor: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        windows = []
        for windows_item_data in self.windows:
            windows_item = windows_item_data.to_dict()
            windows.append(windows_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "windows": windows,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_window import UsageWindow

        d = dict(src_dict)
        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = UsageWindow.from_dict(windows_item_data)

            windows.append(windows_item)

        next_cursor = d.pop("next_cursor")

        usage_window_page = cls(
            windows=windows,
            next_cursor=next_cursor,
        )

        usage_window_page.additional_properties = d
        return usage_window_page

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
