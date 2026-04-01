from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeSyncCompatibilityIssue")


@_attrs_define
class VolumeSyncCompatibilityIssue:
    """
    Attributes:
        code (str):
        path (Union[Unset, str]):
        normalized_path (Union[Unset, str]):
        paths (Union[Unset, list[str]]):
        segment (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    code: str
    path: Union[Unset, str] = UNSET
    normalized_path: Union[Unset, str] = UNSET
    paths: Union[Unset, list[str]] = UNSET
    segment: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        path = self.path

        normalized_path = self.normalized_path

        paths: Union[Unset, list[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        segment = self.segment

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if normalized_path is not UNSET:
            field_dict["normalized_path"] = normalized_path
        if paths is not UNSET:
            field_dict["paths"] = paths
        if segment is not UNSET:
            field_dict["segment"] = segment
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        path = d.pop("path", UNSET)

        normalized_path = d.pop("normalized_path", UNSET)

        paths = cast(list[str], d.pop("paths", UNSET))

        segment = d.pop("segment", UNSET)

        message = d.pop("message", UNSET)

        volume_sync_compatibility_issue = cls(
            code=code,
            path=path,
            normalized_path=normalized_path,
            paths=paths,
            segment=segment,
            message=message,
        )

        volume_sync_compatibility_issue.additional_properties = d
        return volume_sync_compatibility_issue

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
