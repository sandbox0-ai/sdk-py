from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_source_type import RunSourceType
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sandbox_service_run_source import SandboxServiceRunSource
  from ..models.snapshot_run_source import SnapshotRunSource





T = TypeVar("T", bound="RunSource")



@_attrs_define
class RunSource:
    """ 
        Attributes:
            type_ (RunSourceType):
            sandbox_service (Union[Unset, SandboxServiceRunSource]):
            snapshot (Union[Unset, SnapshotRunSource]):
     """

    type_: RunSourceType
    sandbox_service: Union[Unset, 'SandboxServiceRunSource'] = UNSET
    snapshot: Union[Unset, 'SnapshotRunSource'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_service_run_source import SandboxServiceRunSource
        from ..models.snapshot_run_source import SnapshotRunSource
        type_ = self.type_.value

        sandbox_service: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_service, Unset):
            sandbox_service = self.sandbox_service.to_dict()

        snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if sandbox_service is not UNSET:
            field_dict["sandbox_service"] = sandbox_service
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_service_run_source import SandboxServiceRunSource
        from ..models.snapshot_run_source import SnapshotRunSource
        d = dict(src_dict)
        type_ = RunSourceType(d.pop("type"))




        _sandbox_service = d.pop("sandbox_service", UNSET)
        sandbox_service: Union[Unset, SandboxServiceRunSource]
        if isinstance(_sandbox_service,  Unset):
            sandbox_service = UNSET
        else:
            sandbox_service = SandboxServiceRunSource.from_dict(_sandbox_service)




        _snapshot = d.pop("snapshot", UNSET)
        snapshot: Union[Unset, SnapshotRunSource]
        if isinstance(_snapshot,  Unset):
            snapshot = UNSET
        else:
            snapshot = SnapshotRunSource.from_dict(_snapshot)




        run_source = cls(
            type_=type_,
            sandbox_service=sandbox_service,
            snapshot=snapshot,
        )


        run_source.additional_properties = d
        return run_source

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
