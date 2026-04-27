from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clone_volume_file_result_mode import CloneVolumeFileResultMode

T = TypeVar("T", bound="CloneVolumeFileResult")


@_attrs_define
class CloneVolumeFileResult:
    """
    Attributes:
        source_volume_id (str):
        source_path (str):
        target_path (str):
        mode (CloneVolumeFileResultMode):
        size_bytes (int):
    """

    source_volume_id: str
    source_path: str
    target_path: str
    mode: CloneVolumeFileResultMode
    size_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_volume_id = self.source_volume_id

        source_path = self.source_path

        target_path = self.target_path

        mode = self.mode.value

        size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_volume_id": source_volume_id,
                "source_path": source_path,
                "target_path": target_path,
                "mode": mode,
                "size_bytes": size_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_volume_id = d.pop("source_volume_id")

        source_path = d.pop("source_path")

        target_path = d.pop("target_path")

        mode = CloneVolumeFileResultMode(d.pop("mode"))

        size_bytes = d.pop("size_bytes")

        clone_volume_file_result = cls(
            source_volume_id=source_volume_id,
            source_path=source_path,
            target_path=target_path,
            mode=mode,
            size_bytes=size_bytes,
        )

        clone_volume_file_result.additional_properties = d
        return clone_volume_file_result

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
