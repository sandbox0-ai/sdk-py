from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sandbox_lifecycle_status import SandboxLifecycleStatus






T = TypeVar("T", bound="RestoreSandboxRootFSResponse")



@_attrs_define
class RestoreSandboxRootFSResponse:
    """ 
        Attributes:
            sandbox_id (str):
            snapshot_id (str):
            status (SandboxLifecycleStatus):
     """

    sandbox_id: str
    snapshot_id: str
    status: SandboxLifecycleStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        snapshot_id = self.snapshot_id

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sandbox_id": sandbox_id,
            "snapshot_id": snapshot_id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        snapshot_id = d.pop("snapshot_id")

        status = SandboxLifecycleStatus(d.pop("status"))




        restore_sandbox_root_fs_response = cls(
            sandbox_id=sandbox_id,
            snapshot_id=snapshot_id,
            status=status,
        )


        restore_sandbox_root_fs_response.additional_properties = d
        return restore_sandbox_root_fs_response

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
