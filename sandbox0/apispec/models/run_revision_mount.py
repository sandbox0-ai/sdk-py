from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RunRevisionMount")



@_attrs_define
class RunRevisionMount:
    """ 
        Attributes:
            snapshot_id (str):
            mount_path (str):
            read_only (Union[Unset, bool]): Run snapshot mounts are immutable and are materialized as read-only volumes at
                runtime. Default: True.
     """

    snapshot_id: str
    mount_path: str
    read_only: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        mount_path = self.mount_path

        read_only = self.read_only


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "snapshot_id": snapshot_id,
            "mount_path": mount_path,
        })
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id")

        mount_path = d.pop("mount_path")

        read_only = d.pop("read_only", UNSET)

        run_revision_mount = cls(
            snapshot_id=snapshot_id,
            mount_path=mount_path,
            read_only=read_only,
        )


        run_revision_mount.additional_properties = d
        return run_revision_mount

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
