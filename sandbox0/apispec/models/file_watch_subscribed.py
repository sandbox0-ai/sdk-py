from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_watch_subscribed_type import FileWatchSubscribedType

T = TypeVar("T", bound="FileWatchSubscribed")


@_attrs_define
class FileWatchSubscribed:
    """
    Attributes:
        type_ (FileWatchSubscribedType):
        watch_id (str):
        path (str):
    """

    type_: FileWatchSubscribedType
    watch_id: str
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        watch_id = self.watch_id

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "watch_id": watch_id,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FileWatchSubscribedType(d.pop("type"))

        watch_id = d.pop("watch_id")

        path = d.pop("path")

        file_watch_subscribed = cls(
            type_=type_,
            watch_id=watch_id,
            path=path,
        )

        file_watch_subscribed.additional_properties = d
        return file_watch_subscribed

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
