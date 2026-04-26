from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloneVolumeFileEntry")


@_attrs_define
class CloneVolumeFileEntry:
    """
    Attributes:
        source_volume_id (str): Source sandbox volume ID. It must belong to the same team as the target volume.
        source_path (str): Source regular file path inside the source volume.
        target_path (str): Destination file path inside the target volume.
        overwrite (Union[Unset, bool]): Replace an existing destination file. Existing directories are never
            overwritten. Default: False.
        create_parents (Union[Unset, bool]): Create missing parent directories under the target path. Default: False.
    """

    source_volume_id: str
    source_path: str
    target_path: str
    overwrite: Union[Unset, bool] = False
    create_parents: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_volume_id = self.source_volume_id

        source_path = self.source_path

        target_path = self.target_path

        overwrite = self.overwrite

        create_parents = self.create_parents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_volume_id": source_volume_id,
                "source_path": source_path,
                "target_path": target_path,
            }
        )
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if create_parents is not UNSET:
            field_dict["create_parents"] = create_parents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_volume_id = d.pop("source_volume_id")

        source_path = d.pop("source_path")

        target_path = d.pop("target_path")

        overwrite = d.pop("overwrite", UNSET)

        create_parents = d.pop("create_parents", UNSET)

        clone_volume_file_entry = cls(
            source_volume_id=source_volume_id,
            source_path=source_path,
            target_path=target_path,
            overwrite=overwrite,
            create_parents=create_parents,
        )

        clone_volume_file_entry.additional_properties = d
        return clone_volume_file_entry

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
