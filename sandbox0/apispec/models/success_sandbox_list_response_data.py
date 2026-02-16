from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sandbox_summary import SandboxSummary


T = TypeVar("T", bound="SuccessSandboxListResponseData")


@_attrs_define
class SuccessSandboxListResponseData:
    """
    Attributes:
        sandboxes (list['SandboxSummary']):
        count (int): Total matching sandboxes
        has_more (bool): More results available
    """

    sandboxes: list["SandboxSummary"]
    count: int
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandboxes = []
        for sandboxes_item_data in self.sandboxes:
            sandboxes_item = sandboxes_item_data.to_dict()
            sandboxes.append(sandboxes_item)

        count = self.count

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandboxes": sandboxes,
                "count": count,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_summary import SandboxSummary

        d = dict(src_dict)
        sandboxes = []
        _sandboxes = d.pop("sandboxes")
        for sandboxes_item_data in _sandboxes:
            sandboxes_item = SandboxSummary.from_dict(sandboxes_item_data)

            sandboxes.append(sandboxes_item)

        count = d.pop("count")

        has_more = d.pop("has_more")

        success_sandbox_list_response_data = cls(
            sandboxes=sandboxes,
            count=count,
            has_more=has_more,
        )

        success_sandbox_list_response_data.additional_properties = d
        return success_sandbox_list_response_data

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
