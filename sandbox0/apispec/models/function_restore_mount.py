from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctionRestoreMount")


@_attrs_define
class FunctionRestoreMount:
    """
    Attributes:
        sandboxvolume_id (str): Revision-owned SandboxVolume prepared when the function revision was published.
        mount_point (str):
        source_sandboxvolume_id (Union[Unset, str]): Source SandboxVolume captured when the function revision was
            published.
        snapshot_id (Union[Unset, str]): Immutable source volume snapshot captured for this function revision.
    """

    sandboxvolume_id: str
    mount_point: str
    source_sandboxvolume_id: Union[Unset, str] = UNSET
    snapshot_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandboxvolume_id = self.sandboxvolume_id

        mount_point = self.mount_point

        source_sandboxvolume_id = self.source_sandboxvolume_id

        snapshot_id = self.snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandboxvolume_id": sandboxvolume_id,
                "mount_point": mount_point,
            }
        )
        if source_sandboxvolume_id is not UNSET:
            field_dict["source_sandboxvolume_id"] = source_sandboxvolume_id
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandboxvolume_id = d.pop("sandboxvolume_id")

        mount_point = d.pop("mount_point")

        source_sandboxvolume_id = d.pop("source_sandboxvolume_id", UNSET)

        snapshot_id = d.pop("snapshot_id", UNSET)

        function_restore_mount = cls(
            sandboxvolume_id=sandboxvolume_id,
            mount_point=mount_point,
            source_sandboxvolume_id=source_sandboxvolume_id,
            snapshot_id=snapshot_id,
        )

        function_restore_mount.additional_properties = d
        return function_restore_mount

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
