from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_watch_subscribe_request_action import FileWatchSubscribeRequestAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileWatchSubscribeRequest")


@_attrs_define
class FileWatchSubscribeRequest:
    """
    Attributes:
        action (FileWatchSubscribeRequestAction):
        path (str):
        recursive (Union[Unset, bool]):
    """

    action: FileWatchSubscribeRequestAction
    path: str
    recursive: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        path = self.path

        recursive = self.recursive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "path": path,
            }
        )
        if recursive is not UNSET:
            field_dict["recursive"] = recursive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = FileWatchSubscribeRequestAction(d.pop("action"))

        path = d.pop("path")

        recursive = d.pop("recursive", UNSET)

        file_watch_subscribe_request = cls(
            action=action,
            path=path,
            recursive=recursive,
        )

        file_watch_subscribe_request.additional_properties = d
        return file_watch_subscribe_request

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
