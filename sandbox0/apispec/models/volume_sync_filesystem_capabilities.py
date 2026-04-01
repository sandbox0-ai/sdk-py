from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VolumeSyncFilesystemCapabilities")


@_attrs_define
class VolumeSyncFilesystemCapabilities:
    """
    Attributes:
        case_sensitive (bool):
        unicode_normalization_insensitive (bool):
        windows_compatible_paths (bool):
    """

    case_sensitive: bool
    unicode_normalization_insensitive: bool
    windows_compatible_paths: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        case_sensitive = self.case_sensitive

        unicode_normalization_insensitive = self.unicode_normalization_insensitive

        windows_compatible_paths = self.windows_compatible_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "case_sensitive": case_sensitive,
                "unicode_normalization_insensitive": unicode_normalization_insensitive,
                "windows_compatible_paths": windows_compatible_paths,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        case_sensitive = d.pop("case_sensitive")

        unicode_normalization_insensitive = d.pop("unicode_normalization_insensitive")

        windows_compatible_paths = d.pop("windows_compatible_paths")

        volume_sync_filesystem_capabilities = cls(
            case_sensitive=case_sensitive,
            unicode_normalization_insensitive=unicode_normalization_insensitive,
            windows_compatible_paths=windows_compatible_paths,
        )

        volume_sync_filesystem_capabilities.additional_properties = d
        return volume_sync_filesystem_capabilities

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
