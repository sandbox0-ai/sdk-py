import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.file_info_type import FileInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileInfo")


@_attrs_define
class FileInfo:
    """
    Attributes:
        name (Union[Unset, str]):
        path (Union[Unset, str]):
        type_ (Union[Unset, FileInfoType]):
        size (Union[Unset, int]):
        mode (Union[Unset, str]):
        mod_time (Union[Unset, datetime.datetime]):
        is_link (Union[Unset, bool]):
        link_target (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    type_: Union[Unset, FileInfoType] = UNSET
    size: Union[Unset, int] = UNSET
    mode: Union[Unset, str] = UNSET
    mod_time: Union[Unset, datetime.datetime] = UNSET
    is_link: Union[Unset, bool] = UNSET
    link_target: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        size = self.size

        mode = self.mode

        mod_time: Union[Unset, str] = UNSET
        if not isinstance(self.mod_time, Unset):
            mod_time = self.mod_time.isoformat()

        is_link = self.is_link

        link_target = self.link_target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_
        if size is not UNSET:
            field_dict["size"] = size
        if mode is not UNSET:
            field_dict["mode"] = mode
        if mod_time is not UNSET:
            field_dict["mod_time"] = mod_time
        if is_link is not UNSET:
            field_dict["is_link"] = is_link
        if link_target is not UNSET:
            field_dict["link_target"] = link_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FileInfoType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FileInfoType(_type_)

        size = d.pop("size", UNSET)

        mode = d.pop("mode", UNSET)

        _mod_time = d.pop("mod_time", UNSET)
        mod_time: Union[Unset, datetime.datetime]
        if isinstance(_mod_time, Unset):
            mod_time = UNSET
        else:
            mod_time = isoparse(_mod_time)

        is_link = d.pop("is_link", UNSET)

        link_target = d.pop("link_target", UNSET)

        file_info = cls(
            name=name,
            path=path,
            type_=type_,
            size=size,
            mode=mode,
            mod_time=mod_time,
            is_link=is_link,
            link_target=link_target,
        )

        file_info.additional_properties = d
        return file_info

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
